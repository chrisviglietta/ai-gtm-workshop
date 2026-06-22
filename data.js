/* ══════════════════════════════════════════════════════════════════
   data.js — single source of truth for the Workshop One-Pager portal

   Every field on Home / Welcome / Pre-Flight / Post-Workshop pages
   maps to a column from the workshop intake + post-workshop survey
   Google sheet. Keys below mirror the sheet column names, slugified.

   To swap in a different graduate, replace this object (or load it
   via fetch from the sheet's published CSV — see loadFromCsv() at
   the bottom of this file).
   ══════════════════════════════════════════════════════════════════ */

window.WORKSHOP_DATA = {
  // ─── INTAKE (pre-workshop) ──────────────────────────────────────
  event_name_and_date:   "AI GTM Workshop · NYC · 18 May 2026",
  work_email:            "maya@linear.app",
  linkedin_profile:      "https://linkedin.com/in/maya-okonkwo",
  first_name:            "Maya",
  last_name:             "Okonkwo",
  company_name:          "Linear",
  job_title:             "Senior GTM Operations Manager",
  workflow_to_build:     "A CRM enrichment loop that surfaces dormant accounts worth re-engaging — refresh firmographics, score against ICP, ping #gtm-revival in Slack.",
  why_this_use_case:     "My enrichment stack doesn't talk to itself. Every refresh is a 14-tab Chrome window and a CSV I lose. We're leaving money on the table inside our existing CRM.",
  ai_initiatives:        ["CRM enrichment + scoring", "Outbound personalization at scale", "Pipeline hygiene automation"],
  clay_fluency:          2,        // 1=Never used → 4=Power user
  clay_workspace_id:     "ws_linear_gtm_main",
  workflow_tags:         ["enrichment", "scoring", "signals"], // drives case-study recommendations
  dietary_restrictions:  "Vegetarian",
  work_email_domain:     "linear.app",

  // ─── ACCOUNT / SFDC ─────────────────────────────────────────────
  sfdc_account_id:       "0014x00001AbCdEf",
  sfdc_account_link:     "https://clay.lightning.force.com/lightning/r/Account/0014x00001AbCdEf/view",
  account_tier:          "Tier 1",
  account_status:        "Active",
  workspaces_created_90d: 3,
  opportunity_owner:     "Devon Park",
  opportunity_owner_mgr: "Sarah Chen",
  opportunity_stage:     "Closed Won",
  last_stage_change_days: 12,
  estimated_deal_size:   "$48,000",

  // ─── POST-WORKSHOP SURVEY ───────────────────────────────────────
  clay_skill_before:     2,
  clay_skill_after:      4,
  nps_recommend:         10,
  table_link:            "https://app.clay.com/workspaces/linear/tables/dormant-account-revival",
  table_does:            "Refreshes firmographics on 2,400 dormant HubSpot accounts via a 3-source waterfall, pulls funding signals from the last 90 days, scores ICP-fit with Claygent, and writes warm leads back to HubSpot + a Monday Slack digest in #gtm-revival.",
  most_interesting_topics: ["Claygent prompts for ICP scoring", "3-source waterfall enrichment", "Slack digest as the action layer"],
  least_useful_topics:   "Honestly, none — but I'd happily go deeper on multi-step AI columns next time.",
  follow_ups:            "Add a job-changes signal to flag champions who've moved. Also want to test routing the weekly digest to AE pods instead of one channel.",
  what_you_loved:        "Pseudocoded the workflow before I walked in. Shipped it live in 4 hours. By Friday it was running on 2,400 HubSpot accounts at Linear.",
  greenlight_approver:   "Sarah Chen — VP Marketing",

  // ─── DERIVED / DISPLAY (computed from above) ────────────────────
  // These aren't sheet columns — they're convenience values built
  // from the raw fields, used in headlines and IDs.
  full_name:             "Maya Okonkwo",
  role_at_company:       "Senior GTM Operations Manager at Linear",
  city:                  "NYC",
  workshop_date:         "18 May 2026",
  graduate_id:           "WG-3F8D17C2",
  cohort_size:           22,
  cohort_position:       1,

  // ICP + stack lines pulled from the operator's profile
  icp:                   "Series B–D B2B SaaS, 200–2,000 FTEs, Eng-led teams in NA/EU",
  current_stack:         ["HubSpot", "Outreach", "Clearbit", "ZoomInfo", "Slack", "Notion"],
  biggest_pain:          "My enrichment stack doesn't talk to itself. Every refresh is a 14-tab Chrome window and a CSV I lose.",

  // Outcomes (computed post-workshop)
  outcomes: [
    { k: "Accounts touched",   v: "2,400" },
    { k: "ICP-fit revivals",   v: "47" },
    { k: "Pipeline reopened",  v: "$1.2M" },
    { k: "Time to ship",       v: "4 hours" }
  ]
};

/* ──────────────────────────────────────────────────────────────────
   Tiny helper — apply data to any element with [data-field="key"].
   Pages call applyData() once on load. Supports text, href, src.
   ────────────────────────────────────────────────────────────────── */
window.applyData = function(d){
  d = d || window.WORKSHOP_DATA;
  document.querySelectorAll("[data-field]").forEach(el => {
    const key = el.getAttribute("data-field");
    const val = d[key];
    if (val == null) return;
    const attr = el.getAttribute("data-field-attr");
    if (attr) el.setAttribute(attr, val);
    else el.textContent = Array.isArray(val) ? val.join(" · ") : val;
  });
};

/* ──────────────────────────────────────────────────────────────────
   Optional: load live from a published-to-web Google Sheet CSV.
   Sheet → File → Share → Publish to web → CSV → paste URL below.
   Then call: loadFromCsv(URL).then(applyData)
   ────────────────────────────────────────────────────────────────── */
window.loadFromCsv = async function(csvUrl){
  const text = await fetch(csvUrl).then(r => r.text());
  const [header, ...rows] = text.trim().split(/\r?\n/).map(line =>
    // naive CSV split — fine for our header set, escape commas in copy
    line.match(/("([^"]|"")*"|[^,]*)(,|$)/g).map(s => s.replace(/,$/, "").replace(/^"|"$/g, "").replace(/""/g, '"'))
  );
  // first data row only — change to map-by-graduate-id for many rows
  const row = rows[0];
  const slug = s => s.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_|_$/g, "");
  const out = {};
  header.forEach((col, i) => { out[slug(col)] = row[i]; });
  Object.assign(window.WORKSHOP_DATA, out);
  return window.WORKSHOP_DATA;
};
