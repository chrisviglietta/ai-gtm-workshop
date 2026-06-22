# Pre-flight checklist tracking

## What we're tracking

Three pre-flight items per guest:

| Item | Counts as done when… |
|---|---|
| **Fuel-up** | Guest clicks **"I watched this"** under the Clay University crash course |
| **Brainstorm** | Guest fills all 5 prompts and clicks **"Submit my answers"** |
| **Comms check** | Guest clicks **"I posted this"** — OR (later) we auto-detect from the Slack post |

Each completion is **append-only** — once done, it stays done. Re-opening the page shows the green-check state from the sheet.

## Sheet schema

Add the following columns to the **same Google Sheet** that holds workshop intake:

| Column | Type | Example |
|---|---|---|
| `Fuel-Up Done` | bool | `TRUE` |
| `Fuel-Up Done At` | ISO timestamp | `2026-05-13T14:32:08-04:00` |
| `Brainstorm Done` | bool | `TRUE` |
| `Brainstorm Done At` | ISO timestamp | `2026-05-14T09:11:42-04:00` |
| `Brainstorm Answers` | JSON string | `{"workflow":"…","data":"…","system":"…","approver":"…","team":"…"}` |
| `Comms Check Done` | bool | `FALSE` |
| `Comms Check Done At` | ISO timestamp | (empty until clicked) |
| `Comms Check Slack URL` | string | (optional — Slack message permalink if we auto-detect) |
| `Last Activity At` | ISO timestamp | `2026-05-14T09:11:42-04:00` |
| `Follow-Up Needed` | computed bool | `TRUE` if `NOW − intake_at > 48h AND any item not done` |

`Last Activity At` is updated by the page on every save. `Follow-Up Needed` is a sheet **formula column** — keeps the logic in the sheet, not in the page:

```
=IF(AND(NOW() - INTAKE_AT > 2,
        NOT(AND(FUEL_UP_DONE, BRAINSTORM_DONE, COMMS_CHECK_DONE))),
   TRUE, FALSE)
```

## Auto-save flow

Each completion fires immediately when its trigger button is clicked. We don't wait for a "Save my progress" — the page persists each item the moment it changes.

```
User clicks "I watched this"
   │
   ▼
Page sets fuel_up_done = true in local state
   │
   ▼
Page POSTs to Google Apps Script Web App endpoint:
   { graduate_id, item: "fuel_up", done: true, ts: "2026-…" }
   │
   ▼
Apps Script writes to the matching row in the sheet
   │
   ▼
Page swaps the button → green "Done" pill (no full reload)
```

### Why Apps Script

- Reads/writes the sheet directly with `SpreadsheetApp.getActiveSpreadsheet()`.
- Free, no infra to manage.
- Deploy as a Web App (Anyone, including anonymous, can access) → returns a URL the page can `fetch()`.
- Auth: page sends the access code (`maya-4821`) as the secret; Apps Script verifies it matches the row's stored code before writing.

### Apps Script sketch

```javascript
function doPost(e){
  const { graduate_id, access_code, item, done, ts, payload } = JSON.parse(e.postData.contents);
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Cohort");
  const rows = sheet.getDataRange().getValues();
  const header = rows[0];

  const idCol = header.indexOf("Graduate ID");
  const codeCol = header.indexOf("Access Code");

  // find the row, verify the code, refuse if mismatch
  for (let i = 1; i < rows.length; i++){
    if (rows[i][idCol] !== graduate_id) continue;
    if (rows[i][codeCol] !== access_code) {
      return ContentService.createTextOutput(JSON.stringify({ ok: false, error: "auth" }));
    }
    // write completion + timestamp
    const itemCol = header.indexOf(itemColumnName(item));
    const tsCol   = header.indexOf(itemColumnName(item) + " At");
    sheet.getRange(i + 1, itemCol + 1).setValue(done);
    sheet.getRange(i + 1, tsCol + 1).setValue(ts);
    sheet.getRange(i + 1, header.indexOf("Last Activity At") + 1).setValue(ts);

    // store brainstorm answers if present
    if (item === "brainstorm" && payload){
      sheet.getRange(i + 1, header.indexOf("Brainstorm Answers") + 1).setValue(JSON.stringify(payload));
    }
    return ContentService.createTextOutput(JSON.stringify({ ok: true }));
  }
  return ContentService.createTextOutput(JSON.stringify({ ok: false, error: "not_found" }));
}

function itemColumnName(item){
  return { fuel_up: "Fuel-Up Done", brainstorm: "Brainstorm Done", comms_check: "Comms Check Done" }[item];
}
```

### Page-side wiring

In `pre-flight.html`:

```javascript
const ENDPOINT = "https://script.google.com/macros/s/AKfyc.../exec";

async function markDone(item, payload){
  const body = {
    graduate_id: WORKSHOP_DATA.graduate_id,
    access_code: WORKSHOP_DATA.access_code,
    item,
    done: true,
    ts: new Date().toISOString(),
    payload,
  };
  const res = await fetch(ENDPOINT, { method: "POST", body: JSON.stringify(body) });
  const json = await res.json();
  if (!json.ok) throw new Error(json.error);
  return json;
}

// hook up the buttons
document.querySelector("#mark-fuel-up").addEventListener("click", () => markDone("fuel_up"));
document.querySelector("#submit-brainstorm").addEventListener("click", () => {
  const answers = collectBrainstormAnswers(); // reads the 5 textareas
  return markDone("brainstorm", answers);
});
document.querySelector("#mark-comms-check").addEventListener("click", () => markDone("comms_check"));
```

## Optimistic UI

The auto-save call is fire-and-forget from the user's POV:

1. Click button → button visually flips to "Done" instantly.
2. Save runs in the background.
3. If save fails → toast "Couldn't save — we'll retry" + queued retry.

Using localStorage as a backstop: if the network drops or Apps Script throws, the completion is still in localStorage. Next page load reconciles localStorage → sheet.

## Progress bar (guest-facing)

Top of `pre-flight.html`:

```
[ ●●○ ] 2 of 3 complete
```

Increments as each card flips to done. Tangerine fill, oat-200 track. No celebratory moment at 3/3 — keep it understated.

## Rate limiting

Apps Script Web Apps have a quota (~30,000 requests/day, generous for a 22-person cohort, but worth noting). Each page action = at most 1 POST. With 22 graduates × 3 items = 66 max writes per cohort.

## Privacy

- The endpoint accepts the access code as the auth secret. Without the code, no writes succeed.
- Brainstorm answers contain workflow descriptions — sensitive but not high-stakes. Apps Script connection is HTTPS.
- Don't store the access code in localStorage in plain text — read it from the URL each load. (It's already in the URL anyway.)

## Cohort-progress dashboard

Lives at `cohort-progress.html` (mocked now, wired later). Reads the same sheet, shows:

- One row per graduate.
- Three checkbox columns (Fuel-up / Brainstorm / Comms check).
- "Last activity" column.
- "Follow-up needed" badge when the sheet's computed column says so.
- Filter chips: All · Complete · In progress · Needs follow-up.
- Click a row → opens that graduate's pre-flight page in a new tab.

## What to build, in order

1. ✅ This document
2. ✅ Mock dashboard at `cohort-progress.html` with fake cohort data
3. ⬜ Add the new columns to the sheet
4. ⬜ Build the Apps Script endpoint, deploy as Web App
5. ⬜ Wire the three buttons in `pre-flight.html` to `markDone()`
6. ⬜ Replace the dashboard's mock data with a `loadFromCsv` call against the published sheet
7. ⬜ (Later) Slack auto-detection: a separate Apps Script that polls `#ent-workshops` for posts containing the workshop hashtag and matches them to graduate IDs
