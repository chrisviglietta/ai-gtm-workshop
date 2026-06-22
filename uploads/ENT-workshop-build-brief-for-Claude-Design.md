# Build brief — ENT Workshop Pre-Flight & Post-Flight (for Claude Design)

**For:** Claude Design
**From:** Chris (workshops)
**Strategic context:** [`ENT-workshop-program-PRD.md`](./ENT-workshop-program-PRD.md) — read first if you want the why; this doc focuses on the what
**Surfaces in this brief:** Welcome, Pre-Flight Checklist, Post-Workshop shareable
**Reference patterns:** Yash CCE page (`gtme2-cert.vercel.app/certified/cce-cohort-1-yash-tekriwal`), existing one-pagers (`atlanta/michael-hoover-btcpa.html`)

---

## How to use this brief

This is medium-prescription. Page anatomy, component states, copy, and data bindings are specified — interpret these as the contract. Type scale, layout grid, color application, motion, and exact spacing are yours — interpret these as the room to design.

The two visual reference points to internalize before starting:

- **Yash CCE page** for the post-workshop surface (editorial, oversized H1s, ticker wordmark, source-attributed stats, peer quote treatment, verifiable-credential block)
- **Existing one-pager system** (`michael-hoover-btcpa.html`) for the pre-flight surface (Notion-flavored callouts, pastel tags, 720px max-width, Inter body / Georgia headings)

The Welcome page sits between these two — closer in feel to the pre-flight than the post-workshop, but lighter, since it's the "you're confirmed" moment.

The pre-flight metaphor — rocket / takeoff / system check / cleared for launch — runs through all three pages and is the brand voice for this program. Don't water it down.

---

## Shared system

Things that apply to all three pages.

### Brand stack

- Use the existing Clay branding template you already have applied in your environment
- Body type: Inter (matches existing one-pagers)
- Headline type: Georgia or Clay's editorial display face — match what's on the Yash CCE page
- Color: Clay palette
- Iconography: reuse the existing icon set where it fits (Trophy, Star, Medal, Certificate, Light Bulb, Hammer). Add only the rocket-themed icons this program needs: Rocket, Checklist, Radio (for comms), Fuel
- Tile graphics: reuse the existing `Tile-stack_*` library
- The repeating wordmark ticker pattern from the Yash page (`CLAY · CERTIFIED · GTM ENGINEER · GTME² ·`) — adapt to `CLAY · AI GTM WORKSHOP · {CITY} ·` for this program. Use it on the post-workshop surface

### Voice rules

- Confident, specific, practitioner. No marketing fluff
- The metaphor stays in the copy — not just decoration. "Cleared for launch," "system check," "wheels up," "fuel up"
- Sentence case, not Title Case
- No emoji except the rocket (🚀) and the cleared-for-launch ✈️ — used sparingly
- No exclamation points except in the cleared-for-launch state

### Header & footer (shared)

**Header (all 3 pages):**
- Clay logo (links to clay.com)
- Breadcrumb: `AI GTM Workshop / {City} / {Page Name}`

**Footer (all 3 pages):**
- Clay wordmark
- Three links: Next workshop · Clay University · Clay Slack community
- Support contact: `aly.slater@clay.com`

### Responsive

- Designs need to work from 320px to 1920px
- Mobile is a primary surface — attendees will open the welcome email on their phone
- 720px content max-width on pre-flight and welcome (matches existing one-pagers); post-workshop can go wider where the Yash page does

### Data binding notation

Wherever copy includes `{token}`, that's a field from the attendee's Google Sheet row. Build with placeholder data; the templating layer is out of scope for design but the bindings need to be visible in the spec.

---

## Surface 1 — Welcome page

**URL:** `/{city}/{slug}/welcome`
**When seen:** In the signup confirmation email, immediately after registration
**Time on page:** ~30 seconds before they click into Pre-Flight
**Job:** Confirm registration, set expectations, hand off to the Pre-Flight Checklist

### Page anatomy

1. **Header** — shared
2. **Hero**
   - Eyebrow: `PRE-FLIGHT · {CITY} · {DATE}`
   - H1: `You're cleared for boarding, {first_name}.` followed by rocket
   - Subhead: `Workshop is {date} at {venue}. Three system checks before takeoff — finish them and we hit the ground building.`
3. **Workshop strip** — three cells in a row
   - Date · `{cohort_date}`
   - Venue · `{venue}`
   - Bring · `Laptop + your CRM creds`
4. **What we know about you** — single card recapping intake answers
   - "Here's what you told us at signup. If anything's off, hit reply and we'll fix it before workshop day."
   - Fields shown: company, ICP, what they want to build, current stack, biggest pain
   - All bound to Sheet columns
5. **The three pre-flight checks** — preview block with three cards
   - Each card: icon, name, one-line description, status pill ("Not started")
   - Cards: Fuel up · Pseudocode · Comms check
   - Status logic: if pre-flight already started, show real status; otherwise all three show "Not started"
6. **Primary CTA**
   - Button: `Start Pre-Flight →`
   - Below: small text — "Takes about 20 minutes. Required to lock in your seat."
7. **What happens after** — one-paragraph teaser
   - "Once you're cleared for launch, you'll show up Wednesday with us already prepped. After the workshop, you'll get a personal page with what you built — share it with your team, send it to your manager, post it on LinkedIn."
8. **Footer** — shared

### Component states

- The "What we know about you" card is read-only on this page. (Editing happens via email reply, not inline — out of scope)
- The three preview cards are non-interactive on the Welcome page. They become the actual pre-flight cards on the next page

### Copy that's locked

The headline (`You're cleared for boarding, {first_name}`) and the metaphor framing throughout — these aren't placeholder copy, they're the brand voice.

---

## Surface 2 — Pre-Flight Checklist

**URL:** `/{city}/{slug}/pre-flight`
**When seen:** Click-through from the Welcome page, anytime before workshop day
**Time on page:** 15–25 minutes (the actual prep work happens here)
**Job:** Get the attendee genuinely ready — videos watched, pseudocoding submitted, Slack post made

### Page anatomy

1. **Header** — shared
2. **Hero**
   - Eyebrow: `PRE-FLIGHT CHECKLIST · {CITY} · {DATE}`
   - H1: `Three system checks. Two required. One workshop you actually take off in.`
   - Subhead: explains gating ("Pseudocoding and the comms check are required — without them, your seat doesn't lock in. Watching the videos is optional if you already know Clay.")
3. **Progress meter** — sticky or near-top, persists scroll position
   - Shows: "X of 2 required complete" with a progress bar
   - Required count is 2, not 3 — videos don't count
4. **Workshop strip** — same as Welcome (date, venue, bring)
5. **Sub-step 1 — Fuel up** (optional)
   - Number badge "1," icon, title "Fuel up," status pill
   - Tagline: "Three short Clay University lessons. Watch what you don't already know."
   - Three video rows; each row: checkbox, title, duration + one-line value, "Watch ↗" link
   - Videos:
     - **Intro to Clay 101 — FETE Jigsaw** · ~12 min · "The framework everything else hangs on" · `https://university.clay.com/lessons/intro-to-clay-101-fete-jigsaw`
     - **Intro to CRM Enrichment** · ~14 min · "The most common workshop use case" · `https://university.clay.com/lessons/intro-to-crm-enrichment`
     - **Prompt Engineering Crash Course — Limitless Research** · ~18 min · "Where the AI half of AI GTM lives" · `https://university.clay.com/lessons/prompt-engineering-crash-course-limitless-research`
   - Status pill states: "Optional · 0 of 3 watched" → "Optional · 2 of 3 watched" → "Complete · 3 of 3"
6. **Sub-step 2 — Pseudocode the build** (required)
   - Number badge "2," icon, title "Pseudocode the build," status pill ("Required · Not started")
   - Tagline: "Five questions. The clearer your answers, the more we can pre-build for you before you walk in."
   - **WisprFlow CTA** — small pill above the form: "🎙 Type slow? Use WisprFlow to dictate your answers ↗" → `https://wisprflow.ai/get-started?referral=CHRIS143&utm_source=referral`
   - **The 5 form fields** — copy is verbatim, do not paraphrase
     1. Walk us through the workflow you want to build — inputs → outputs → where it lands.
        - *Help text:* "Example: 'Inputs: list of 500 target accounts I imported from Salesforce. Outputs: VP+ Marketing contacts at each, with personalized hooks. Lands in: HubSpot, then Outreach.'"
        - *Field type:* textarea, 4 rows
     2. What data do you have ready to plug in?
        - *Help text:* "CSV upload, Salesforce view, HubSpot list, Notion table, Google Sheet — paste a link or describe it."
        - *Field type:* textarea, 3 rows
     3. What system does the workflow need to write to?
        - *Help text:* "HubSpot, Salesforce, Outreach, Smartlead, Slack, custom — list everything."
        - *Field type:* textarea, 2 rows
     4. Who at your company needs to greenlight rolling this out?
        - *Help text:* "Name + role. Example: 'Sarah Chen — VP Marketing'"
        - *Field type:* single-line text input
     5. Anyone else on your team should be in this room with you?
        - *Help text:* "Names + roles. We can extend invites if there's still space."
        - *Field type:* textarea, 2 rows
   - Submit button: `Submit pseudocoding`
   - Validation: all 5 fields required non-empty. We don't grade quality, just completion
7. **Sub-step 3 — Comms check** (required, locked until #2 complete)
   - Number badge "3," icon, title "Comms check," status pill
   - Tagline: "Post your pseudocoding to the Clay community Slack. Lets us — and 200+ other practitioners — react before workshop day."
   - **Slack message preview** card — pre-filled with the attendee's Q1, Q2, Q3 answers interpolated in:
     ```
     👋 Hey #ent-workshops — I'm {first_name} from {company_name}. Pre-flight checklist incoming.

     What I'm building: {q1}
     Data I have: {q2}
     Where it needs to land: {q3}

     Excited for {city} on {cohort_date}. 🚀
     ```
   - Two action buttons:
     - Secondary: `📋 Copy message`
     - Primary: `Open Slack ↗` → `https://join.slack.com/t/clayrunhq/shared_invite/zt-3uyf25mqq-czoaZvxA7WJAburC5ehvzw`
   - Marking complete: clicking "Open Slack" marks the step complete (honor system — we can't verify the post itself)
8. **Cleared for launch** — final state block at bottom
   - Locked state (default): muted card, "Cleared for launch when all required checks are complete." with subtext "You'll see your launch summary here once Sub-steps 2 and 3 are done."
   - Cleared state (after both required steps): green/celebratory card, H3 "Cleared for launch ✈️", body "Your pseudocoding is locked in. Wheels up {cohort_date} at {venue}. Your personal one-pager will be live at the start of the workshop."
9. **Footer** — shared

### Component states (per sub-step card)

Each of the three sub-step cards has these states. Design needs to spec all of them:

- **Locked** — sub-step 3 only, before sub-step 2 is complete. Card is dimmed, status pill reads "Locked · finish #2 first," interactions disabled
- **Not started** — default for all sub-steps on first visit. Status pill reads "Required · Not started" (or "Optional · 0 of 3 watched" for sub-step 1)
- **In progress** — sub-step 2 only, when some but not all fields filled. Status pill reads "Required · In progress"
- **Ready to act** — sub-step 3, after sub-step 2 complete but before "Open Slack" clicked. Status pill reads "Required · ready to post"
- **Complete** — number badge fills with success color, status pill reads "Complete," card border or background gets a subtle success treatment

The progress meter at the top updates after each state transition. The full-page "Cleared for launch" block at the bottom changes from locked to cleared when both required steps hit Complete.

### Persistence

The page persists state per attendee, keyed on the slug. Any field edited or step completed survives a page reload. Source of truth is the Google Sheet row (handled by the data layer; design doesn't need to spec the persistence mechanism, just the visual "this is saved" state).

### Copy that's locked

- The 5 pseudocoding questions (verbatim)
- The Slack message template (verbatim, with the three interpolation tokens)
- The video titles and CU URLs
- The WisprFlow URL with the `CHRIS143` referral code
- The Slack invite URL

---

## Surface 3 — Post-Workshop shareable page

**URL:** `/{city}/{slug}` (the public, unprotected attendee URL — designed to be shared)
**When seen:** ~24 hours after workshop ends, sent in a follow-up email
**Time on page:** Variable — attendee skims, manager reads carefully, GTME extracts ammo
**Job:** Serve all three audiences (attendee, manager, GTME) on a single shareable URL. This is the most important surface in the program

This page is **directly modeled on the Yash CCE page**. Reference it open in another tab while designing. Everything below is either "same as Yash" (steal the pattern) or "different from Yash" (the ENT-specific bits).

### Page anatomy

1. **Header** — Clay logo, "Workshop Graduate" label on the right, share affordance
2. **Identity hero** — *same pattern as Yash*
   - Tile graphic
   - Eyebrow: `CLAY · AI GTM WORKSHOP · {CITY} GRADUATE`
   - H1: `{full_name} built {workflow_built_name} at the Clay AI GTM Workshop.`
   - Below H1: one-sentence summary of what they built (pulled from `q1` + `post_workshop_reflection`)
   - Engineer-style metadata block: `{title} at {company_name} · {city} · {cohort_date}` · LinkedIn link
3. **Wordmark ticker** — `CLAY · AI GTM WORKSHOP · {CITY} ·` repeating with rocket icon. *Same visual pattern as Yash's ticker*
4. **About the attendee** — *same pattern as Yash's "Meet Yash"*
   - Tile graphic
   - H2: "Meet {first_name}."
   - Two paragraphs of bio (from intake + LinkedIn enrichment)
   - One pull quote from their NPS "what did you love" answer
   - Title attribution
5. **What this work moved** — *same pattern as Yash's "Yash's outcomes"*
   - Three outcome stats. Each is hero number + one-sentence description + source attribution
     - **Skill gain:** "{nps_skill_after - nps_skill_before}" with format "{before} → {after}, +{delta}" · Source: "NPS survey · {workshop_date}"
     - **Recommend score:** "{nps_recommend_score}/10" · Source: "NPS survey · {workshop_date}"
     - **Workflow shipped:** "{workflow_built_name}" with link to Loom if present · Source: "Live build · {workshop_date}"
   - Verification metadata strip above stats: VERIFIED `{workshop_date}` · PROGRAM `AI GTM Workshop` · CITY `{city}` · GRADUATE ID `WG-{city}-{8-char-hex}`
   - Same rule as Yash: **no fake stats. If a stat isn't sourced, render a placeholder, not a number.**
6. **The build · Real-world workflow** — *same pattern as Yash's L3 case study*
   - Step indicator "✓"
   - H2: `{workflow_built_name}`
   - One paragraph narrative pulled from `q1` + `post_workshop_reflection`
   - Optional Loom embed if `workflow_built_loom_url` is present
   - **Workflow spec block** below the narrative — structured layout showing:
     - Inputs: `{q2}`
     - Outputs: derived from `{q1}`
     - Target system: `{q3}`
     - Tools used: chip row from a tools-list field
7. **Approver block** — *NEW, ENT-specific. Most important section on the page after the hero.*
   - Eyebrow: "Multi-thread"
   - H2: "{approver_name} needs to see this."
   - Body: "{approver_name} — {approver_role} — needs to greenlight rollout. Forward this page so the conversation starts before the next 1:1, not after."
   - Pulled from pseudocoding `q4`. The approver name is parsed into name + role
   - CTA button: `Forward this page →` — opens a `mailto:` draft with subject and body pre-filled (subject: "Wanted to share what I built last week"; body includes the page URL and a 2-sentence note)
   - **This is the multi-threading mechanism in artifact form. It's the single highest-leverage block on the page for moving deals.**
8. **Keep building · Join a Clay cohort** — *NEW, ENT-specific*
   - Eyebrow: "What's next"
   - H2: "Workshop sparked something? Keep building."
   - Body: "Clay cohorts are longer-form, deeper, and structured around the workflows you actually want in production. The workshop graduates who go to cohort are the ones who turn one good build into ten."
   - CTA: `Join a Clay cohort →` linking to `https://university.clay.com/cohorts`
9. **What they learned** — optional reflection block (hide if `post_workshop_reflection` is empty)
   - 2-3 short paragraphs in the attendee's own voice
   - No formatting embellishment — this is intentionally just prose
10. **What this workshop required** — *same pattern as Yash's "What earning the CCE took"*
    - One-paragraph plain-English summary of the workshop program
    - Three sub-blocks, one per pre-flight sub-step: Fuel up · Pseudocode · Comms check
    - Each shows what the attendee did at that step, plus 3-4 bullets describing what the step actually tested
    - Closing rubric note: "Workshops are graded on what gets shipped, not what gets attempted. Graduates ship a workflow with measurable outputs in 4 hours."
11. **Wordmark ticker** — repeat
12. **Verifiable graduate block** — *same pattern as Yash's verifiable credential*
    - Medal icon
    - "This is a verifiable workshop graduate"
    - Metadata: workshop date · city · graduate ID · workflow shipped
    - CTAs:
      - `Share on LinkedIn ↗` — opens LinkedIn share with pre-filled post text: "Just graduated from the Clay AI GTM Workshop in {city}. Built {workflow_built_name} live with the team. Here's what it does: {URL}"
      - `Verify ↗` (links to a verification view, out of scope for this design)
13. **Closing CTA** — "Want this for your team? → " links to next cohort signup
14. **Footer** — shared

### Component states

- **Stat with no source** → render placeholder ("Pending verification") instead of fabricating a number
- **No Loom URL** → hide the Loom embed slot entirely; the narrative paragraph stands alone
- **No reflection text** → hide section 9 entirely
- **No approver in `q4`** → hide section 7 entirely (this should be rare; approver is required pseudocoding)

### Sharing affordances

Three explicit sharing surfaces on this page:

- LinkedIn share button (in the Verifiable graduate block)
- Forward-to-approver email (in the Approver block — `mailto:` link, opens user's mail client)
- Copy URL button (in the header, near the share affordance)

OG image and Twitter card are auto-generated per attendee at `/{city}/{slug}/opengraph-image` and `/{city}/{slug}/twitter-image`. Same pattern as the Yash CCE page. **These need to be designed as templates** — not as one-off cards. Spec the template, the build layer interpolates.

### Copy that's locked

- The verbatim headlines and section labels above
- The "Forward this page" mailto subject line
- The LinkedIn share post template

---

## Asset list

What Design needs to produce or assemble:

- **Page templates** (3): Welcome, Pre-Flight, Post-Workshop — desktop + mobile responsive
- **Component states** for the Pre-Flight sub-step cards: Locked, Not started, In progress, Ready to act, Complete (5 states × 3 cards, though some don't apply to all)
- **Cleared-for-launch state** (locked + cleared variants)
- **OG image template** for the post-workshop page — 1200×630, with bindings for name, workflow built, city, date
- **Twitter card image template** — same dimensions/spec
- **New icons** if not in the existing set: Rocket, Checklist, Radio, Fuel
- **Wordmark ticker** adapted from the Yash CCE pattern: `CLAY · AI GTM WORKSHOP · {CITY} ·`
- **Email template visual spec** for the welcome confirmation email (out of scope for this brief but flagged here so it's not forgotten — will need to match the Welcome page's hero treatment)

---

## Acceptance criteria

The build is acceptable when:

- All three pages render responsively from 320px to 1920px
- All `{token}` bindings are visible in the spec and use placeholder data, not hardcoded text
- Pre-Flight Checklist component states are individually mocked (not just the default state)
- Post-workshop page renders correctly with and without optional fields (Loom, reflection)
- OG image template renders correctly across name lengths from "Jo Lee" to "Christopher Hernandez-Williams"
- Pre-flight metaphor is preserved in copy across all three pages — no surface drops it
- The pages feel like one program, not three disconnected screens. Same brand, same voice, same visual language

---

## Out of scope for this brief

- The data layer / Google Sheet templating mechanism
- The signup form itself (separate intake)
- The NPS survey instrument
- Email lifecycle (welcome email, reminder, post-workshop email) — flagged in asset list but specced separately
- Authentication or paywall
- Real-time progress sync between devices
- Verification view linked from the verifiable graduate block

---

## Questions I'd want Design's POV on

These are open in a way that wants a designer's recommendation, not an engineer's:

- Should the Pre-Flight progress meter be sticky on scroll, or just sit at the top? Sticky is more reassuring but eats vertical real estate on mobile
- The "Cleared for launch" state — celebratory motion (subtle), confetti (overdone), or just a color shift? The metaphor invites celebration but the brand doesn't normally do that
- For the Post-Workshop page on mobile, the Yash CCE page is dense — does the same density work or does the ENT version need more breathing room?
- The Approver block is doing the most work on the post-workshop page. Does it deserve a different visual treatment than the Clay cohort CTA block, or should they be visual peers?
