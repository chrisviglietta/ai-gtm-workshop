# Data mapping — Google Sheet → Portal pages

Single source of truth lives in `data.js`. Every visible field on the four pages maps to a column from the workshop sheet. Keys in `data.js` are the column names slugified (lowercase, non-alphanumerics → `_`).

## Sheet columns → `data.js` keys

| Sheet column | Key in `data.js` | Used on |
|---|---|---|
| Event Name & Date | `event_name_and_date` | Home (eyebrow), Welcome (eyebrow), Pre-flight (eyebrow), Post-workshop (eyebrow) |
| What is your work email? | `work_email` | Welcome (greeting), Post-workshop (approver mailto FROM) |
| What is your LinkedIn profile? | `linkedin_profile` | Post-workshop (Connect on LinkedIn link) |
| First Name | `first_name` | Welcome ("You're cleared, {first_name}"), Pre-flight (Slack avatar/name), Post-workshop (Meet {first_name}) |
| Last Name | `last_name` | Post-workshop (full name) |
| Company Name | `company_name` | Pre-flight (Slack message), Post-workshop (hero, Meet, Build narrative) |
| Job title | `job_title` | Pre-flight (recap), Post-workshop (hero meta, Meet attribution) |
| Which workflow do you want to build during the workshop? | `workflow_to_build` | Pre-flight (Q1 prefill), Post-workshop (hero subhead, Build narrative) |
| Why this use case, why now? | `why_this_use_case` | Pre-flight (recap "biggest pain"), Post-workshop (Meet quote) |
| Top 1-3 AI initiatives at your company this year? | `ai_initiatives` | Post-workshop (Build context) |
| Clay fluency (1→4) | `clay_fluency` | Pre-flight (decides if Fuel-up is shown as "skip if pro") |
| Clay workspace ID | `clay_workspace_id` | Post-workshop (table link composition) |
| Do you have any dietary restrictions? | `dietary_restrictions` | Welcome (logistics confirmation) |
| Work Email Domain | `work_email_domain` | Internal — domain matching for SFDC join |
| SFDC Account ID | `sfdc_account_id` | Internal only |
| Account SFDC CRM Link | `sfdc_account_link` | Internal only (admin view) |
| Account Tier | `account_tier` | Internal — gates seat priority |
| Account Status | `account_status` | Internal |
| Workspaces Created Last 90 Days | `workspaces_created_90d` | Internal |
| Opportunity Owner Name | `opportunity_owner` | Internal — used to ping AE post-workshop |
| Opportunity Owner Manager | `opportunity_owner_mgr` | Internal |
| Opportunity Stage Name | `opportunity_stage` | Internal |
| Last Stage Change In Days | `last_stage_change_days` | Internal |
| Estimated Deal Size Formula | `estimated_deal_size` | Internal |
| Clay Skill Level Before Workshop | `clay_skill_before` | Post-workshop (Outcomes — "from 2 → 4") |
| Clay Skill Level After Workshop | `clay_skill_after` | Post-workshop (Outcomes) |
| How likely are you to recommend this workshop? | `nps_recommend` | Post-workshop (verifiable strip) |
| Link to Clay table you built | `table_link` | Post-workshop (Build section, Loom panel, table CTA) |
| What does your table do? | `table_does` | Post-workshop (Build narrative) |
| What were the most interesting topics to you? | `most_interesting_topics` | Post-workshop ("What landed" section) |
| What were the least useful topics to you | `least_useful_topics` | Post-workshop (Follow-ups section) |
| Do you have any follow Ups to the table you built at the workshop | `follow_ups` | Post-workshop (Follow-ups) |
| What did you love about the workshop? | `what_you_loved` | Post-workshop (hero subhead, pull-quote) |
| Who on your team needs to see this to greenlight rollout? | `greenlight_approver` | Pre-flight (Q4 prefill), Post-workshop ("{approver} needs to see this" section) |

## Derived fields (computed, not in sheet)

| Key | How it's computed |
|---|---|
| `full_name` | `first_name + " " + last_name` |
| `role_at_company` | `job_title + " at " + company_name` |
| `city` | parsed from `event_name_and_date` (between · and ·) |
| `workshop_date` | parsed from `event_name_and_date` (last segment) |
| `graduate_id` | `WG-{city}-{8-char hash of work_email}` |
| `cohort_size` / `cohort_position` | from a separate cohort roster sheet |
| `icp` / `current_stack` / `biggest_pain` | parsed from `why_this_use_case` + `workflow_to_build` |
| `outcomes` | post-workshop dashboard pulls from the table the graduate built |

## Wiring it up

1. Each page loads `data.js` once: `<script src="data.js"></script>`
2. Each dynamic field gets `data-field="key_name"` (or `data-field-attr="href"` for links).
3. On page load, `applyData()` walks the DOM and fills every tagged element.

## Live sync (optional)

In Google Sheets: **File → Share → Publish to web → CSV → copy URL**.
Then in any page, after `<script src="data.js"></script>`:

```html
<script>
  loadFromCsv("<published-CSV-url>").then(applyData);
</script>
```

The single-row CSV-loader is a starting point. For per-graduate routing (?id=WG-NYC-3F8D17C2) we'd extend `loadFromCsv` to find the row whose graduate_id matches the URL param.
