# Access codes

## TL;DR

Each workshop guest gets a unique code shaped like **`maya-4821`** — lowercase first name, dash, 4 digits. The code lives in the URL: visiting `clay.com/workshop/maya-4821` loads that guest's post-workshop page. Wrong code shows a friendly "check your email" screen.

This is a **soft gate**, not real auth. Codes are guessable in principle, but a determined person could already scrape a public URL anyway. The gate's job is to keep links from being shared casually outside the intended audience.

---

## Format

```
{firstname}-{4 digits}        →  maya-4821
{firstname}-{lastinitial}-{4 digits}   (only when there's a name collision in the cohort)  →  maya-o-4821
```

Rules:
- First name → lowercased, ASCII only, spaces and apostrophes stripped (`Mary-Anne` → `maryanne`, `O'Brien` → `obrien`).
- 4 digits → any value `0000`–`9999`. They don't need to be sequential or meaningful.
- Last initial → only added when two guests in the same cohort would otherwise collide on `firstname-XXXX`.
- Codes never expire. A graduate keeps their page forever.

## Where codes live

The Google Sheet that already drives the workshop intake gets one new column:

| Column | Example |
|---|---|
| **Access Code** | `maya-4821` |

That's the source of truth. We generate codes when the row is created (manually or by your form workflow) and never change them.

## How the URL works

```
clay.com/workshop/maya-4821
                  ↑
                  this is the code from the sheet
```

When a page loads:

1. Read the code from the URL (`window.location.pathname`, last segment).
2. Look up the matching row in the published sheet CSV.
3. If found → call `applyData(row)`, render the page.
4. If not found OR no code in URL → render the **lock screen** (see below).

This works for the post-workshop page. The pre-flight, welcome, and home pages can use the same scheme; their URLs just point at a different template.

## The lock screen

Wrong / missing code, the page should show:

> **Check your email.**
> Your workshop link looks like `clay.com/workshop/firstname-1234`. Search your inbox for "Clay AI GTM Workshop" — it's in the confirmation email and the post-workshop wrap-up.
>
> Lost it? [Reply to your confirmation email] and we'll resend.

Friendly tone. No "access denied," no error codes. The point is: someone got a half-broken link or typed it wrong, help them recover.

## Collision handling

When adding a new guest to the sheet:

1. Generate a candidate code: `firstname-{random 4 digits}`.
2. Check the **Access Code** column for an existing match.
3. If match → check whether the existing row is in the **same cohort** as the new guest.
   - **Same cohort:** disambiguate. Both get a last-initial inserted: `maya-c-4821` and `maya-o-3372`. (Update the existing row too — it's a one-time rewrite.)
   - **Different cohort:** generate new 4 digits and try again. We treat the firstname-XXXX namespace as global, not per-cohort, so there's no risk of someone bookmarking the wrong page after a future cohort reuses their code.
4. Re-check until no collision.

In practice, with 4 digits = 10,000 codes per first name and ~22 guests per cohort, collisions are rare. The check is mostly defensive.

## Privacy notes

- The code is in the URL, so it appears in browser history, referrer headers, and any link-preview unfurls (Slack, email, LinkedIn). That's fine for a soft gate — it matches our threat model.
- Don't put codes in the sheet's "Published to web" CSV if the sheet is also used for sensitive ops data. Either:
  - publish only a code-keyed view (one tab with just the columns the page needs), **or**
  - move the public-facing data to a separate sheet that gets republished from the master.

## What's NOT built yet

- No URL routing in the current files — they're flat HTML, one URL per template. Adding the routing is straightforward (a few lines of JS at the top of each page) but waiting until you say go.
- No lock screen page exists yet.
- No bulk code-generation tool. When you're ready, this is a 20-line script that takes a CSV of `first_name, last_name, cohort` and emits an `access_code` column.
- The confirmation email template still references a generic link — needs updating to include the per-guest code once we wire routing.

## When you're ready to build

The order I'd do it in:
1. Add `Access Code` column to the sheet, generate codes for the existing cohort.
2. Update the published-CSV URL in `data.js`'s `loadFromCsv` helper.
3. Add the URL-param parser and lock screen.
4. Update the email template.
