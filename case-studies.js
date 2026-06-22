/* ══════════════════════════════════════════════════════════════════
   case-studies.js — Clay customer case studies database
   Source: Workshop - Clay Customer Case Studies PDF
   ══════════════════════════════════════════════════════════════════ */

window.CLAY_CASE_STUDIES = [
  // ── CRM ENRICHMENT ────────────────────────────────────────
  { id: 'vanta-crm-enrich', co: 'Vanta', logo: 'V', color: 'blueberry',
    person: 'Mark Lail', personRole: 'Director of Revenue Operations',
    category: 'CRM enrichment', tags: ['enrichment'],
    title: 'Waterfall enrichment across multiple providers',
    problem: 'Fragmented enrichment tools created conflicting CRM data with no single source of truth.',
    solution: [
      'Pull contact data from multiple enrichment providers',
      'Waterfall logic selects most reliable data points',
      'Unified enrichment output tailored per CRM record',
      'Sync enriched contacts into Salesforce CRM',
    ],
    impact: [
      { num: '80%+',   label: 'enrichment coverage achieved' },
      { num: '1,000+', label: 'new enriched contacts/month' },
      { num: '100%',   label: 'automated research tasks' },
    ] },

  { id: 'terrapinn-crm-enrich', co: 'Terrapinn', logo: 'T', color: 'tangerine',
    person: 'Sharon Roessen', personRole: 'COO',
    category: 'CRM enrichment', tags: ['enrichment'],
    title: '8M records enriched across 35 verticals',
    problem: 'An 8-million-record database across 35 verticals lacked enrichment to target effectively.',
    solution: [
      'Clay enriches 8M records with firmographic signals',
      'Classify records against ICPs across 35 verticals',
      'Tailor campaigns using vertical-specific context',
      'Push enriched records into Salesforce',
    ],
    impact: [
      { num: '+28%',  label: 'email open rate lift' },
      { num: '21.5M', label: 'more email opens YoY' },
      { num: '+35%',  label: 'more emails sent' },
    ] },

  { id: 'coverflex-crm-enrich', co: 'Coverflex', logo: 'C', color: 'ube',
    person: 'Pedro Azevedo', personRole: 'Marketing & Growth Ops Leader',
    category: 'CRM enrichment', tags: ['enrichment','signals'],
    title: '1M+ prospects with decision-maker routing',
    problem: "Fragmented data tools couldn't enrich millions of prospect records across multiple countries.",
    solution: [
      'Enrich 1M+ prospects from LinkedIn and APIs',
      'Identify decision-makers; route by signal strength',
      'Append emails, LinkedIn posts, and job changes',
      'Push signal-qualified leads into HubSpot',
    ],
    impact: [
      { num: '3M+',  label: 'companies scanned monthly' },
      { num: '1M+',  label: 'prospects enriched' },
      { num: '200+', label: 'additional demos/month' },
    ] },

  { id: 'oyster-crm-enrich', co: 'Oyster', logo: 'O', color: 'lime',
    person: 'Petra Hajal', personRole: 'Marketing Operations',
    category: 'CRM enrichment', tags: ['enrichment','scoring'],
    title: 'ICP-fit scoring tied to CRM enrichment',
    problem: 'Scattered data across multiple tools prevented maintaining a unified, enriched CRM.',
    solution: [
      'Enrich accounts and contacts with firmographic data',
      'Score ICP fit; map to CRM records',
      'Append decision-maker contacts and intent signals',
      'Sync enriched records back to CRM',
    ],
    impact: [
      { num: '40 hrs', label: 'saved monthly per rep' },
      { num: '4x',     label: 'increase in accounts reached' },
    ] },

  { id: 'exitfive-crm-enrich', co: 'Exit Five', logo: 'E', color: 'lemon',
    person: 'Dan Murphy', personRole: 'COO',
    category: 'CRM enrichment', tags: ['enrichment','abm'],
    title: '27K contacts enriched with firmographics',
    problem: 'CRM held only email addresses with no firmographic data to segment their audience.',
    solution: [
      'Import 27K contacts from HubSpot into Clay',
      'Route to matching enrichment providers',
      'Append job title, company size, revenue per contact',
      'Push enriched firmographic records back to HubSpot',
    ],
    impact: [
      { num: '100%', label: 'automation of event targeting' },
      { num: '2x',   label: 'sponsorship deal velocity' },
    ] },

  { id: 'mistral-crm-enrich', co: 'Mistral AI', logo: 'M', color: 'tangerine',
    person: 'Joel Davidson', personRole: 'VP of Revenue Operations',
    category: 'CRM enrichment', tags: ['enrichment'],
    title: '10+ firmographic providers per account',
    problem: 'Single-vendor data gaps leave global firmographic records incomplete across 100+ countries.',
    solution: [
      'Query 10+ firmographic providers per account',
      'AI standardizes and fills revenue gaps automatically',
      'Estimated revenue drives segmentation, routing, scoring',
      'Sync enriched records into Salesforce',
    ],
    impact: [
      { num: '10+',     label: 'data providers waterfalled' },
      { num: '25,000+', label: 'accounts enriched' },
      { num: '5',       label: 'data points combined by AI' },
    ] },

  { id: 'verkada-eu-enrich', co: 'Verkada', logo: 'V', color: 'blueberry',
    person: 'Cody Leovic', personRole: 'Senior Growth Manager, EMEA',
    category: 'CRM enrichment', tags: ['enrichment'],
    title: '150+ regional data sources for EU coverage',
    problem: 'Fragmented European data vendors made multi-country account enrichment painfully slow.',
    solution: [
      'Waterfall queries 150+ regional data sources',
      'Validate results across multiple regional providers',
      'Enrich with country-specific verified data',
      'Push enriched records to Salesforce per campaign',
    ],
    impact: [
      { num: '62%',  label: 'better enrichment vs incumbent' },
      { num: '95%+', label: 'email validation accuracy' },
      { num: '80%+', label: 'coverage in niche geographies' },
    ] },

  { id: 'merge-crm-enrich', co: 'Merge', logo: 'M', color: 'ube',
    person: 'Tim Bourcier', personRole: 'RevOps & Marketing Lead',
    category: 'CRM enrichment', tags: ['enrichment'],
    title: '50,000 accounts categorized by use case',
    problem: 'Siloed data across tools left reps without account context for thousands of use cases.',
    solution: [
      'Enrich 50,000+ accounts using multiple sources',
      'Classify each account by industry and use case',
      'Tailor offering based on relevant use case',
      'Push enriched fields back into Salesforce',
    ],
    impact: [
      { num: '20%',     label: 'response rate improvement' },
      { num: '10+ hrs', label: 'saved weekly per rep' },
      { num: '50,000+', label: 'accounts enriched' },
    ] },

  { id: 'hex-crm-enrich', co: 'Hex', logo: 'H', color: 'dragon',
    person: 'Bryanna Clancy', personRole: 'Marketing Ops & GTM Engineering Leader',
    category: 'CRM enrichment', tags: ['enrichment','scoring'],
    title: 'Custom data dimensions for technical buyers',
    problem: 'Traditional enrichment vendors lack custom data dimensions needed for technical enterprise deals.',
    solution: [
      'AI agents enrich 50,000+ contacts across custom dimensions',
      'Score data maturity, AI capabilities, and tech stack',
      'Map buying groups and decision-makers per account',
      'Push enriched profiles into Salesforce',
    ],
    impact: [
      { num: '88%',     label: 'data gap filled vs prior vendor' },
      { num: '50,000+', label: 'contacts enriched via waterfall' },
    ] },

  { id: 'harmonic-crm-enrich', co: 'Harmonic', logo: 'H', color: 'slushie',
    person: 'Darri Atlason', personRole: 'Head of Growth',
    category: 'CRM enrichment', tags: ['enrichment','signals'],
    title: 'Auto-enrich with job-change tracking',
    problem: 'Lead and account records decayed rapidly, making manual data updates unsustainable for SDR workflows.',
    solution: [
      'Clay auto-enriches contacts tracking job changes',
      'Route enriched leads by territory and account ownership',
      'Tailor outreach using recent signals',
      'Push updated records to CRM and sequences',
    ],
    impact: [
      { num: '50 hrs/mo', label: 'manual enrichment eliminated' },
      { num: '3x',        label: 'response rate' },
      { num: '2x',        label: 'SDR outbound capacity' },
    ] },

  { id: 'regency-crm-enrich', co: 'Regency Supply', logo: 'R', color: 'lemon',
    person: 'Andrew Thomas', personRole: 'Director of Marketing',
    category: 'CRM enrichment', tags: ['enrichment','rep-productivity'],
    title: 'On-demand contact enrichment in HubSpot',
    problem: 'Sales reps lacked on-demand contact enrichment and automated job-change tracking inside their CRM.',
    solution: [
      'Webhook pulls contacts and matches LinkedIn profile',
      'Predefined criteria triggers firmographic enrichment',
      'Reps receive tailored summaries per contact',
      'Push enriched data and job alerts to HubSpot',
    ],
    impact: [
      { num: '5,000+', label: 'contacts monitored for job changes' },
      { num: '100%',   label: 'self-serve enrichment' },
      { num: '0',      label: 'manual steps required' },
    ] },

  { id: 'openai-crm-enrich', co: 'OpenAI', logo: 'O', color: 'lime',
    person: 'Keith Jones', personRole: 'GTM Systems Lead',
    category: 'CRM enrichment', tags: ['enrichment'],
    title: 'Multi-source waterfall inside the CRM workflow',
    problem: 'Sellers lacked multi-source enrichment natively within their CRM workflow.',
    solution: [
      'Multi-source waterfall enrichment on CRM records',
      'Route enrichment requests across providers',
      'Deliver curated lead batches per account',
      'Push enriched records back into Salesforce',
    ],
    impact: [
      { num: '150/day', label: 'lead enrichments per rep' },
    ] },

  { id: 'intercom-crm-enrich', co: 'Intercom', logo: 'I', color: 'slushie',
    person: 'Alexander DeMoulin', personRole: 'Director of GTM Ops',
    category: 'CRM enrichment', tags: ['enrichment','scoring'],
    title: 'Niche ICP attribute enrichment',
    problem: 'Standard enrichment tools lacked precision to identify niche ICP signals.',
    solution: [
      'Enrich CRM records via 150+ providers',
      'Test niche attributes correlated with strong adoption',
      'Surface raw qualifying signals per account for reps',
      'Push enriched ICP data into Salesforce',
    ],
    impact: [
      { num: '150+',      label: 'data providers used' },
      { num: 'Thousands', label: 'records enriched with niche attributes' },
    ] },

  { id: 'rippling-crm-enrich', co: 'Rippling', logo: 'R', color: 'blueberry',
    person: 'Davison Chung', personRole: 'Growth Lead',
    category: 'CRM enrichment', tags: ['enrichment','outbound'],
    title: 'Self-serve enrichment for a 30-person growth team',
    problem: 'Manual data work blocked accurate, large-scale lead enrichment across the growth team.',
    solution: [
      'Import leads into Clay tables automatically',
      'Enrich with firmographic and contact providers',
      'Tag leads with persona-specific attributes',
      'Store in Snowflake; sync to Salesforce',
    ],
    impact: [
      { num: '2x',   label: 'cold email performance lift' },
      { num: '30',   label: 'growth team self-serve enabled' },
      { num: '100%', label: 'automated enrichment workflows' },
    ] },

  { id: 'sana-crm-enrich', co: 'Sana', logo: 'S', color: 'tangerine',
    person: 'Fredrika Hillström', personRole: 'GTM Operations Manager',
    category: 'CRM enrichment', tags: ['enrichment'],
    title: 'Waterfall on 150,000 Salesforce accounts',
    problem: 'Rapid team growth left 150,000 CRM accounts with unreliable firmographics reps didn\u2019t trust.',
    solution: [
      'Waterfall-enrich 150,000 Salesforce accounts',
      'Standardize firmographics; apply conditional rules',
      'Surface custom fields like L&D team size per account',
      'Push corrected records back into Salesforce',
    ],
    impact: [
      { num: '+60%',   label: 'lift in CRM accuracy' },
      { num: '85,000', label: 'accounts enriched with core data' },
      { num: '30,000', label: 'enriched with custom parameters' },
    ] },

  { id: 'legora-crm-enrich', co: 'Legora', logo: 'L', color: 'ube',
    person: 'Francesca Pavan', personRole: 'Director of Demand Generation',
    category: 'CRM enrichment', tags: ['enrichment','abm'],
    title: '700+ law firms mapped globally',
    problem: 'Salesforce lacked industry, headcount, and location data for precise targeting.',
    solution: [
      'Enrich Salesforce records with firmographic data',
      'Classify firms by industry, archetype, and size',
      'Tag each account with attorney count and location',
      'Push enriched records back into Salesforce',
    ],
    impact: [
      { num: '90%',  label: 'contact match rate' },
      { num: '+70%', label: 'faster campaign launches' },
      { num: '700+', label: 'law firms mapped globally' },
    ] },

  { id: 'elevenlabs-crm-enrich', co: 'ElevenLabs', logo: 'E', color: 'dragon',
    person: 'Raman Khanna', personRole: 'Growth',
    category: 'CRM enrichment', tags: ['enrichment','scoring'],
    title: 'Scoring built on continuously refreshed enrichment',
    problem: 'CRM data decayed faster than manual teams could enrich, breaking downstream scoring and routing.',
    solution: [
      'Waterfall-enrich firmographic and contact fields',
      'Classify each account against refreshed ICP definitions',
      'Tag industry, size, seniority, department per record',
      'Write enriched records back to Salesforce',
    ],
    impact: [
      { num: '1,000s', label: 'accounts auto-reclassified' },
      { num: '+50%',   label: 'SQLs from enrichment-powered scoring' },
      { num: '4x',     label: 'demand-gen SQLs' },
    ] },

  // ── RESEARCH AT SCALE ─────────────────────────────────────
  { id: 'pump-research', co: 'Pump', logo: 'P', color: 'lime',
    person: 'Stuart Lundberg', personRole: 'Head of Operations',
    category: 'Research at scale', tags: ['research','prospecting'],
    title: 'Pre-built territory lists at rep onboarding',
    problem: 'New reps spent 90 days on manual account research before reaching full productivity.',
    solution: [
      'Enrich accounts via 150+ data sources',
      'Match companies to codified ICP tech-stack criteria',
      'Build territory lists with contacts and context',
      'Deliver pre-built lists to each new rep',
    ],
    impact: [
      { num: '6x',  label: 'faster rep ramp time' },
      { num: '25%', label: 'more revenue per rep' },
      { num: '30+', label: 'reps onboarded with pre-built lists' },
    ] },

  { id: 'sendoso-research', co: 'Sendoso', logo: 'S', color: 'tangerine',
    person: 'Austin Sandmeyer', personRole: 'Head of Growth Marketing',
    category: 'Research at scale', tags: ['research','outbound'],
    title: 'Tailored gift sends via SmartSend',
    problem: 'Manual prospect research took too long, capping SDR output and revenue potential.',
    solution: [
      'Import 500+ target contacts from CRM into Clay',
      'Enrich with LinkedIn activity, posts, and job changes',
      'Generate tailored gift and email messaging',
      'Trigger personalized gift sends via Sendoso SmartSend',
    ],
    impact: [
      { num: '14',   label: 'opportunities booked in week 1' },
      { num: '10x',  label: 'outbound productivity' },
      { num: '500+', label: 'target accounts scanned continuously' },
    ] },

  { id: 'align-research', co: 'A-LIGN', logo: 'A', color: 'lime',
    person: 'Arthur Lorente', personRole: 'Director of GTM Operations',
    category: 'Research at scale', tags: ['research','rep-productivity'],
    title: 'Non-technical staff manipulating CRM data',
    problem: 'Multi-step CRM data handoffs took 48 hours, blocking ops teams from strategic work.',
    solution: [
      'Ingest data requests and CRM records into Clay',
      'Process, clean, and transform without admin tickets',
      'Enable non-technical staff to manipulate CRM data',
      'Push verified data directly to Salesforce',
    ],
    impact: [
      { num: '24x',      label: 'faster (48h \u2192 2h per cycle)' },
      { num: '46 hours', label: 'saved weekly on handoffs' },
    ] },

  // ── TAM SOURCING ──────────────────────────────────────────
  { id: 'mistral-tam', co: 'Mistral AI', logo: 'M', color: 'tangerine',
    person: 'Joel Davidson', personRole: 'VP of Revenue Operations',
    category: 'TAM sourcing', tags: ['prospecting'],
    title: 'Global TAM in 2 weeks',
    problem: 'Mapping a global TAM across 100+ countries manually takes many months.',
    solution: [
      'Source 25,000+ accounts via Find Companies globally',
      'Deduplicate, segment by region and industry',
      'Score and prioritize accounts per territory',
      'Sync enriched accounts into Salesforce',
    ],
    impact: [
      { num: '2 weeks', label: 'to map global TAM (vs 2 months)' },
      { num: '25,000+', label: 'accounts sourced globally' },
      { num: '100+',    label: 'countries covered' },
    ] },

  { id: 'intercom-tam', co: 'Intercom', logo: 'I', color: 'slushie',
    person: 'Alexander DeMoulin', personRole: 'Director of GTM Ops',
    category: 'TAM sourcing', tags: ['prospecting','signals'],
    title: 'Net-new TAM lists in minutes',
    problem: 'Manual TAM list-building took days, blocking timely outbound for a new product.',
    solution: [
      'Continuous flows enrich 4,000+ accounts across 5 signals',
      'Score and filter by Fin-fit signals live',
      'Surface raw qualifying signals per account',
      'Push enriched lists to reps via Salesforce',
    ],
    impact: [
      { num: '4,000+',  label: 'accounts sourced in a month' },
      { num: '21,000',  label: 'contacts enriched in a month' },
      { num: 'Minutes', label: 'to build prospecting list' },
    ] },

  { id: 'sana-tam', co: 'Sana', logo: 'S', color: 'tangerine',
    person: 'Fredrika Hillström', personRole: 'GTM Operations Manager',
    category: 'TAM sourcing', tags: ['prospecting'],
    title: '50 new rep books built in a single day',
    problem: 'Fifty new reps needed ICP-fit accounts, but every Salesforce record was already assigned.',
    solution: [
      'Upload top accounts; find lookalikes via Clay',
      'Exclude existing CRM records; score ICP fit',
      'Match thousands of net-new companies per book',
      'Divide into 50 books and push to Salesforce',
    ],
    impact: [
      { num: '+20%',  label: 'addressable market expansion' },
      { num: '50',    label: 'new rep books in a single day' },
      { num: '1 day', label: 'work that previously took weeks' },
    ] },

  { id: 'legora-tam', co: 'Legora', logo: 'L', color: 'ube',
    person: 'Francesca Pavan', personRole: 'Director of Demand Generation',
    category: 'TAM sourcing', tags: ['prospecting','abm'],
    title: 'Global legal-market TAM in one source of truth',
    problem: 'Mapping a global legal market required stitching fragmented datasets across tools.',
    solution: [
      'Aggregate law firms and legal teams globally',
      'Classify by archetype, size, and HQ',
      'Segment by ICP fit for targeted campaigns',
      'Push enriched TAM lists into Salesforce',
    ],
    impact: [
      { num: '50%',     label: 'lift in qualified leads' },
      { num: '80\u201390%', label: 'contact match rate' },
    ] },

  // ── ACCOUNT / LEAD SCORING ────────────────────────────────
  { id: 'terrapinn-scoring', co: 'Terrapinn', logo: 'T', color: 'tangerine',
    person: 'Sharon Roessen', personRole: 'COO',
    category: 'Account scoring', tags: ['scoring','inbound'],
    title: 'Same-day event registrant scoring',
    problem: 'Event registrants matching ICP couldn\u2019t be acted on without enrichment or automated scoring.',
    solution: [
      'Enrich registrants with firmographic and signal data',
      'Score against sponsor ICP criteria',
      'Surface sponsor-fit context per registrant company',
      'Create follow-up tasks in Gong for reps',
    ],
    impact: [
      { num: '90%',      label: 'reduction in prospect acquisition cost' },
      { num: '+19%',     label: 'revenue per rep' },
      { num: 'Same day', label: 'registrations enriched in Salesforce' },
    ] },

  { id: 'anthropic-scoring', co: 'Anthropic', logo: 'A', color: 'tangerine',
    person: 'Adam Wall', personRole: 'Head of Sales Operations',
    category: 'Account scoring', tags: ['scoring','inbound'],
    title: 'Claude generates custom scoring dimensions',
    problem: 'Massive inbound lead volume overwhelmed a small sales team lacking scoring capacity.',
    solution: [
      'Enrich inbound leads across 150+ providers',
      'Claude AI generates custom industry/segmentation fields',
      'Score each lead using tailored classification signals',
      'Push scored leads into Salesforce',
    ],
    impact: [
      { num: '3x',       label: 'data enrichment coverage' },
      { num: '10+ hrs',  label: 'saved weekly on scoring' },
      { num: '25+',      label: 'custom industry categories' },
    ] },

  { id: 'regency-scoring', co: 'Regency Supply', logo: 'R', color: 'lemon',
    person: 'Andrew Thomas', personRole: 'Director of Marketing',
    category: 'Account scoring', tags: ['scoring','inbound'],
    title: 'Wholesale registration qualification',
    problem: 'Manual verification of wholesale e-commerce registrations created daily bottlenecks.',
    solution: [
      'Webhook captures wholesale registration emails',
      'AI scores leads on business type and legitimacy',
      'Match qualified leads to appropriate sales reps',
      'Route verified leads to reps in CRM',
    ],
    impact: [
      { num: '100%',  label: 'manual qualification automated' },
      { num: '10 h/mo', label: 'rep time saved' },
    ] },

  { id: 'rootly-scoring', co: 'Rootly', logo: 'R', color: 'pom',
    person: 'JJ Tang', personRole: 'Co-founder & CEO',
    category: 'Account scoring', tags: ['scoring','outbound'],
    title: 'Three-tier ICP classification',
    problem: 'Manually identifying ICP-fit accounts caused misaligned targeting and wasted effort.',
    solution: [
      'Claygent scans LinkedIn, job postings, tech stacks',
      'Three-tier scoring classifies each account',
      'High-fit accounts get tailored outreach priority',
      'Route scored leads into outbound workflows',
    ],
    impact: [
      { num: '100%', label: 'outbound workflow automation' },
      { num: '10x',  label: 'outbound volume' },
    ] },

  // ── AUTOMATED OUTBOUND ────────────────────────────────────
  { id: 'coverflex-outbound', co: 'Coverflex', logo: 'C', color: 'ube',
    person: 'Pedro Azevedo', personRole: 'Marketing & Growth Ops Leader',
    category: 'Automated outbound', tags: ['outbound','prospecting'],
    title: 'Personalized landing pages per prospect',
    problem: 'A small team cannot manually prospect and personalize outreach across millions of companies.',
    solution: [
      'Enrich 1M+ prospects from 3M+ company database',
      'Route qualified leads by signal and criteria',
      'Generate custom landing pages, emails, and assets',
      'Push sequences to Lemlist and HubSpot',
    ],
    impact: [
      { num: '200+', label: 'additional demos/month' },
      { num: '5x',   label: 'team output capacity' },
      { num: '1M+',  label: 'prospects in enriched DB' },
    ] },

  { id: 'oyster-outbound', co: 'Oyster', logo: 'O', color: 'lime',
    person: 'Petra Hajal', personRole: 'Marketing Operations',
    category: 'Automated outbound', tags: ['outbound','signals'],
    title: 'Intent-based outbound at scale',
    problem: 'Manual intent-based outbound left lower-priority accounts unreached and pipeline untapped.',
    solution: [
      'Aggregate intent signals from G2 and web sources',
      'Score and route accounts by intent strength',
      'Tailor messaging to each buying stage',
      'Push enriched accounts to sales sequences',
    ],
    impact: [
      { num: '40 hrs', label: 'saved monthly per rep' },
      { num: '4x',     label: 'accounts reached via intent' },
    ] },

  { id: 'pump-outbound', co: 'Pump', logo: 'P', color: 'lime',
    person: 'Stuart Lundberg', personRole: 'Head of Operations',
    category: 'Automated outbound', tags: ['outbound'],
    title: 'Technographic-driven personalization',
    problem: 'Generic outbound fails to break through with technical buyers.',
    solution: [
      'Enrich accounts with technographic and hiring signals',
      'Classify prospects by tech stack and growth stage',
      'Generate messaging citing tech stack',
      'Send personalized outbound to prospects',
    ],
    impact: [
      { num: '30%', label: 'lead-to-meeting lift' },
      { num: '25%', label: 'response rate increase' },
    ] },

  { id: 'verkada-outbound', co: 'Verkada', logo: 'V', color: 'blueberry',
    person: 'Cody Leovic', personRole: 'Senior Growth Manager, EMEA',
    category: 'Automated outbound', tags: ['outbound','prospecting'],
    title: 'Direct mail with verified addresses',
    problem: 'Manual address research caused misdirected direct mail across multi-site EU accounts.',
    solution: [
      'Pull LinkedIn URLs; run Google Business lookups',
      'Cross-reference LinkedIn location with office addresses',
      'Select gifts based on prospect interests',
      'Push enriched contacts to Salesforce for outreach',
    ],
    impact: [
      { num: '95%',  label: 'address data accuracy' },
      { num: '2x',   label: 'mail pipeline-to-cost ratio' },
      { num: '£80K', label: 'annual savings' },
    ] },

  { id: 'recharge-outbound', co: 'Recharge', logo: 'R', color: 'dragon',
    person: 'Evan Rosenstein', personRole: 'Head of Growth',
    category: 'Automated outbound', tags: ['outbound','plg'],
    title: '8x outbound campaign volume',
    problem: 'Manual campaign creation limited outbound to one campaign per quarter.',
    solution: [
      'Pull behavioral signals from Snowflake, CRM, enrichment',
      'Segment by usage, GMV, and engagement',
      'Revenue-specific messaging generated per prospect',
      'Flow sequences into Outreach',
    ],
    impact: [
      { num: '+20%', label: 'opportunity conversion rate' },
      { num: '+12%', label: 'outbound conversion lift' },
      { num: '8x',   label: 'campaign volume' },
    ] },

  { id: 'harmonic-outbound', co: 'Harmonic', logo: 'H', color: 'slushie',
    person: 'Darri Atlason', personRole: 'Head of Growth',
    category: 'Automated outbound', tags: ['outbound','signals'],
    title: 'Funding-event-driven outreach',
    problem: 'SDRs manually tracked funding events across scattered tools, slowing outbound outreach.',
    solution: [
      'Track funding events via API in real time',
      'Identify co-investors and funding details',
      'Tailor messages citing relevant context',
      'Send personalized outreach via SalesLoft',
    ],
    impact: [
      { num: '2x',       label: 'SDR outbound capacity' },
      { num: '3x',       label: 'response rate' },
      { num: '50 h/mo', label: 'manual work eliminated' },
    ] },

  { id: 'sendoso-outbound', co: 'Sendoso', logo: 'S', color: 'tangerine',
    person: 'Austin Sandmeyer', personRole: 'Head of Growth Marketing',
    category: 'Automated outbound', tags: ['outbound','lifecycle'],
    title: 'Closed-lost re-engagement',
    problem: 'Closed-lost deals sat dormant because manual re-engagement could not scale.',
    solution: [
      'Import closed-lost opportunities and stalled leads',
      'Summarize deal history from notes and call transcripts',
      'Generate emails referencing prior interest',
      'Send automated sequences via Instantly',
    ],
    impact: [
      { num: '16',  label: 'meetings booked in 2 weeks' },
      { num: '75%', label: 'open rate on re-engagement' },
    ] },

  { id: 'intercom-outbound', co: 'Intercom', logo: 'I', color: 'slushie',
    person: 'Alexander DeMoulin', personRole: 'Director of GTM Ops',
    category: 'Automated outbound', tags: ['outbound','prospecting'],
    title: '21K contacts enriched in a month',
    problem: 'Manual data prep consumed days, preventing reps from focusing on productive conversations.',
    solution: [
      'Enrich 21,000 contacts via 150+ providers',
      'Score accounts by ICP-fit signals automatically',
      'Surface per-account qualification reasons',
      'Push enriched lists into Salesforce',
    ],
    impact: [
      { num: '140%',    label: 'outbound-sourced pipeline growth' },
      { num: 'Minutes', label: 'to build prospecting list' },
      { num: '21,000',  label: 'contacts enriched in a month' },
    ] },

  { id: 'rippling-outbound', co: 'Rippling', logo: 'R', color: 'blueberry',
    person: 'Davison Chung', personRole: 'Growth Lead',
    category: 'Automated outbound', tags: ['outbound'],
    title: '100K personalized emails/month',
    problem: 'Personalizing hundreds of thousands of cold emails monthly required manual work that could not scale.',
    solution: [
      'Import leads into Clay tables for enrichment',
      'Segment leads by persona and company size',
      'Generate 12+ tailored email variants per segment',
      'Push personalized sequences into Outreach',
    ],
    impact: [
      { num: '2x',       label: 'YoY cold email performance' },
      { num: '12+',      label: 'tailored variants per segment' },
      { num: '100,000s', label: 'personalized emails/month' },
    ] },

  // ── INBOUND ENRICHMENT ────────────────────────────────────
  { id: 'anthropic-inbound', co: 'Anthropic', logo: 'A', color: 'tangerine',
    person: 'Adam Wall', personRole: 'Head of Sales Operations',
    category: 'Inbound enrichment', tags: ['inbound','enrichment'],
    title: 'Triple coverage on inbound leads',
    problem: 'A single data provider left massive gaps when enriching high-volume inbound leads.',
    solution: [
      'Waterfall-enrich inbound leads across providers',
      'Deduplicate and standardize firmographic fields',
      'Append email, phone, domain, size, funding per lead',
      'Push fully enriched records into Salesforce',
    ],
    impact: [
      { num: '3x',   label: 'enrichment coverage lift' },
      { num: '150+', label: 'data providers accessed' },
    ] },

  { id: 'harmonic-inbound', co: 'Harmonic', logo: 'H', color: 'slushie',
    person: 'Darri Atlason', personRole: 'Head of Growth',
    category: 'Inbound enrichment', tags: ['inbound','signals'],
    title: 'Inbound form-to-rep in minutes',
    problem: 'Manual inbound lead processing delayed follow-ups and led to missed opportunities.',
    solution: [
      'Form submissions auto-enriched with contact details',
      'Leads routed to sales rep by territory',
      'Personalized messages crafted from enriched data',
      'Reps follow up via automated sequences',
    ],
    impact: [
      { num: '50 h/mo', label: 'manual work eliminated' },
      { num: '3x',      label: 'response rate improvement' },
      { num: '2x',      label: 'SDR outbound capacity' },
    ] },

  { id: 'openai-inbound', co: 'OpenAI', logo: 'O', color: 'lime',
    person: 'Keith Jones', personRole: 'GTM Systems Lead',
    category: 'Inbound enrichment', tags: ['inbound','enrichment'],
    title: 'Inbound coverage via 150+ providers',
    problem: 'Single-provider inbound enrichment left huge coverage gaps amid surging enterprise demand.',
    solution: [
      'Waterfall queries 150+ providers per inbound lead',
      'Score and route leads using enriched data',
      'Complete lead profiles enable tailored response',
      'Push enriched, scored leads into Salesforce',
    ],
    impact: [
      { num: '2x',        label: 'enrichment coverage vs prior' },
      { num: '< 2 weeks', label: 'to refine provider combination' },
      { num: '80%+',      label: 'inbound enrichment coverage' },
    ] },

  // ── PLG ASSIST ────────────────────────────────────────────
  { id: 'mistral-plg', co: 'Mistral AI', logo: 'M', color: 'tangerine',
    person: 'Joel Davidson', personRole: 'VP of Revenue Operations',
    category: 'PLG assist', tags: ['plg','signals'],
    title: 'Product-usage signals for expansion',
    problem: 'Sales reps lacked real-time product usage signals to prioritize expansion conversations.',
    solution: [
      'Pull usage data from BigQuery and invoicing',
      'Route consumption signals and threshold alerts',
      'Surface account-specific signals and expansion trends',
      'Push enriched consumption records into Salesforce',
    ],
    impact: [
      { num: '6 weeks', label: 'to deploy (vs 6 months ETL)' },
      { num: '$500K',   label: 'saved on integration platforms' },
    ] },

  { id: 'anthropic-plg', co: 'Anthropic', logo: 'A', color: 'tangerine',
    person: 'Adam Wall', personRole: 'Head of Sales Operations',
    category: 'PLG assist', tags: ['plg','enrichment'],
    title: 'Resolving PLG signups to work emails',
    problem: 'PLG signups use personal emails, hiding high-value company accounts from the sales team.',
    solution: [
      'Ingest PLG signups from API, Bedrock, Vertex',
      'Waterfall data providers to resolve work emails',
      'Enrich company domain, size, and funding round',
      'Push enriched records into Salesforce',
    ],
    impact: [
      { num: '150+', label: 'data providers via waterfall' },
      { num: '3',    label: 'PLG signup channels enriched' },
    ] },

  { id: 'recharge-plg', co: 'Recharge', logo: 'R', color: 'dragon',
    person: 'Evan Rosenstein', personRole: 'Head of Growth',
    category: 'PLG assist', tags: ['plg','outbound'],
    title: 'GMV-threshold sales triggers',
    problem: 'PLG stalled when teams relied solely on engaged leads to convert.',
    solution: [
      'Pull product usage and GMV signals from Snowflake',
      'Flag accounts crossing $50K+ GMV thresholds',
      'Generate revenue-impact messaging per prospect',
      'Push targeted sequences into Outreach',
    ],
    impact: [
      { num: '10x',     label: 'call conversion rate' },
      { num: '8x',      label: 'simultaneous PLG campaigns' },
      { num: '20,000+', label: 'merchants in addressable base' },
    ] },

  // ── SIGNAL ALERTS ─────────────────────────────────────────
  { id: 'vanta-signals', co: 'Vanta', logo: 'V', color: 'blueberry',
    person: 'Mark Lail', personRole: 'Director of Revenue Operations',
    category: 'Signal alerts', tags: ['signals'],
    title: 'Four signal types tracked in real time',
    problem: 'Manual tracking of funding, hiring, and compliance signals cannot scale across accounts.',
    solution: [
      'Monitor RSS feeds, job boards, and compliance sites',
      'Auto-create signal records; route to reps',
      'Enrich signals with company context',
      'Push prioritized alerts into Salesforce',
    ],
    impact: [
      { num: '100%', label: 'automated research tasks' },
      { num: '4',    label: 'distinct signal types tracked' },
      { num: '80%+', label: 'enrichment on signal-triggered accounts' },
    ] },

  { id: 'oyster-signals', co: 'Oyster', logo: 'O', color: 'lime',
    person: 'Petra Hajal', personRole: 'Marketing Operations',
    category: 'Signal alerts', tags: ['signals','lifecycle'],
    title: 'Dormant-account revival via hiring signals',
    problem: 'Dormant accounts lacked timely buying signals needed for relevant re-engagement.',
    solution: [
      'Track hiring and growth signals across dormant accounts',
      'Score dormant accounts by ICP fit and activity',
      'Tailor outreach citing detected trigger and new contacts',
      'Route enriched leads to BDRs via email',
    ],
    impact: [
      { num: '40 hrs', label: 'saved monthly per rep' },
      { num: '4x',     label: 'accounts reached' },
    ] },

  { id: 'verkada-signals', co: 'Verkada', logo: 'V', color: 'blueberry',
    person: 'Cody Leovic', personRole: 'Senior Growth Manager, EMEA',
    category: 'Signal alerts', tags: ['signals','lifecycle'],
    title: 'First-party signal mining (EU)',
    problem: 'European privacy laws made third-party intent signals ineffective for lead reengagement.',
    solution: [
      'AI mines emails, Gong transcripts, and product usage',
      'Categorize buying signals; route to campaigns',
      'Tailor reengagement using competitor intelligence',
      'Push enriched signals into Salesforce campaigns',
    ],
    impact: [
      { num: '100%',     label: 'lift in outbound reply rate' },
      { num: '10 years', label: 'first-party data unlocked' },
    ] },

  { id: 'merge-signals', co: 'Merge', logo: 'M', color: 'ube',
    person: 'Tim Bourcier', personRole: 'RevOps & Marketing Lead',
    category: 'Signal alerts', tags: ['signals'],
    title: '1,500 enterprise accounts scanned weekly',
    problem: 'A lean sales team cannot manually monitor 1,500+ enterprise accounts for engagement signals.',
    solution: [
      'AI scans 1,500 enterprise accounts weekly',
      'Flag product launches, partnerships, and org changes',
      'Draft tailored outreach mapped to integration category',
      'Surface alerts with drafted messages to account owners',
    ],
    impact: [
      { num: '+15%',   label: 'enterprise meetings booked' },
      { num: '1,500+', label: 'enterprise accounts scanned' },
      { num: '20%',    label: 'better response rates' },
    ] },

  { id: 'hex-signals', co: 'Hex', logo: 'H', color: 'dragon',
    person: 'Bryanna Clancy', personRole: 'Marketing Ops & GTM Engineering Leader',
    category: 'Signal alerts', tags: ['signals','inbound'],
    title: 'High-intent visitor routing into Slack',
    problem: 'High-intent website visitors weren\u2019t able to be identified and engaged by assigned reps.',
    solution: [
      'Monitor high-intent pages and enrich ICP visitors',
      'Match visitors to assigned reps and SDRs',
      'Engagement summary listing use cases and contact info',
      'Fire Slack notifications tagging assigned reps',
    ],
    impact: [
      { num: '+50%',  label: 'win-rate lift for signal accounts' },
      { num: 'Three', label: 'high-intent page types monitored' },
    ] },

  { id: 'recharge-signals', co: 'Recharge', logo: 'R', color: 'dragon',
    person: 'Evan Rosenstein', personRole: 'Head of Growth',
    category: 'Signal alerts', tags: ['signals','lifecycle','plg'],
    title: 'Lifecycle events across 8 unified sources',
    problem: 'Fragmented data across 8 siloed systems prevented proactive lifecycle event detection.',
    solution: [
      'Unify 8 sources: Snowflake, CRM, behavioral, enrichment',
      'Flag acquisition, expansion, and churn events',
      'Segment by GMV thresholds and engagement signals',
      'Trigger proactive outreach via Outreach sequences',
    ],
    impact: [
      { num: '8',   label: 'data systems unified' },
      { num: '3',   label: 'lifecycle stages automated' },
      { num: '10x', label: 'call conversion rate' },
    ] },

  { id: 'sendoso-signals', co: 'Sendoso', logo: 'S', color: 'tangerine',
    person: 'Austin Sandmeyer', personRole: 'Head of Growth Marketing',
    category: 'Signal alerts', tags: ['signals','lifecycle'],
    title: 'Job-change re-engagement at scale',
    problem: 'Job changes among former customers go undetected, leaving warm re-engagement opportunities untapped.',
    solution: [
      'Detect job changes across former contacts',
      'Trigger Clay workflow to enrich updated profiles',
      'Draft congrats emails with tailored gifts',
      'Send personalized outreach emails automatically',
    ],
    impact: [
      { num: '+20%',  label: 'higher response rates' },
      { num: '3x',    label: 'more prospects engaged' },
      { num: '$1M+',  label: 'pipeline generated in pilot' },
    ] },

  { id: 'rootly-signals', co: 'Rootly', logo: 'R', color: 'pom',
    person: 'JJ Tang', personRole: 'Co-founder & CEO',
    category: 'Signal alerts', tags: ['signals','outbound'],
    title: 'Real-time incident-signal outreach',
    problem: 'Manual processes cannot capitalize on real-time incident signals fast enough for timely outreach.',
    solution: [
      'Monitor incident signals via integrated monitoring',
      'Route incidents through Clay workflows',
      'Enrich contacts and tailor messages per incident',
      'Send personalized emails to decision-makers in minutes',
    ],
    impact: [
      { num: '<5 mins', label: 'response time from signal' },
      { num: '100%',    label: 'outbound workflow automation' },
      { num: '3',       label: 'tools consolidated into Clay' },
    ] },

  { id: 'sana-signals', co: 'Sana', logo: 'S', color: 'tangerine',
    person: 'Fredrika Hillström', personRole: 'GTM Operations Manager',
    category: 'Signal alerts', tags: ['signals','scoring'],
    title: 'Custom intent signals layered on firmographics',
    problem: 'Reps lacked actionable intent signals to prioritize high-value accounts confidently at scale.',
    solution: [
      'Enrich 30,000 accounts with custom intent signals',
      'Layer signals atop firmographics; route per rep',
      'Surface account-specific triggers like job changes',
      'Deliver actionable alerts directly to assigned reps',
    ],
    impact: [
      { num: '30,000', label: 'accounts with custom signals' },
      { num: '140',    label: 'reps receiving intent signals' },
    ] },

  { id: 'legora-signals', co: 'Legora', logo: 'L', color: 'ube',
    person: 'Francesca Pavan', personRole: 'Director of Demand Generation',
    category: 'Signal alerts', tags: ['signals','abm'],
    title: 'Non-standard affinity discovery',
    problem: 'No enrichment provider captures non-standard prospect affinities, making manual signal discovery unscalable.',
    solution: [
      'AI researches contacts for unique signals',
      'Filter and confirm ICP-aligned prospects with affinity',
      'Craft campaign messaging around shared interest',
      'Launch targeted campaign to 6,000 matched prospects',
    ],
    impact: [
      { num: '+60%', label: 'qualified leads from campaigns' },
      { num: '70%',  label: 'faster campaign launches' },
    ] },

  // ── REP PRODUCTIVITY / MEETING ────────────────────────────
  { id: 'vanta-premeeting', co: 'Vanta', logo: 'V', color: 'blueberry',
    person: 'Mark Lail', personRole: 'Director of Revenue Operations',
    category: 'Pre-meeting notes', tags: ['rep-productivity','signals'],
    title: 'Automatic compliance + competitive briefs',
    problem: 'Manual account research took reps hours, delaying follow-up by days.',
    solution: [
      'AI scans websites for SOC 2 and compliance signals',
      'Trigger research when rep claims Salesforce account',
      'Summarize compliance posture and competitive landscape',
      'Deliver research summaries directly into Salesforce',
    ],
    impact: [
      { num: 'Same day',  label: 'automated call follow-up' },
      { num: '100%',      label: 'research tasks automated' },
      { num: 'Automatic', label: 'account research for reps' },
    ] },

  { id: 'pump-followup', co: 'Pump', logo: 'P', color: 'lime',
    person: 'Stuart Lundberg', personRole: 'Head of Operations',
    category: 'Meeting follow-up', tags: ['rep-productivity','lifecycle'],
    title: 'No-show recovery on autopilot',
    problem: 'Manual follow up on no-show prospects consumed 20 minutes per lead and could not scale.',
    solution: [
      'Enrich no-show leads with company and hiring data',
      'Score leads by growth signals; prioritize outreach',
      'Generate emails citing timely reconsideration reasons',
      'Send follow-ups and push prioritized BDR call lists',
    ],
    impact: [
      { num: '26%',   label: 'no-show recovery rate' },
      { num: '0 min', label: 'marginal time per lead' },
    ] },

  // ── ABM / MARKETING ───────────────────────────────────────
  { id: 'hex-abm', co: 'Hex', logo: 'H', color: 'dragon',
    person: 'Bryanna Clancy', personRole: 'Marketing Ops & GTM Engineering Leader',
    category: 'ABM campaigns', tags: ['abm','signals'],
    title: 'Centralized propensity scoring for ABM',
    problem: 'Scattered buying signals across separate tools overwhelmed reps instead of enabling prioritization.',
    solution: [
      'Track social, fundraising, hiring, alumni signals',
      'Score accounts by propensity to buy centrally',
      'Combine Clay signals with campaign engagement',
      'Feed scored accounts into Hex-native ABM app',
    ],
    impact: [
      { num: '3',           label: 'GTM data vendors consolidated' },
      { num: '4',           label: 'buying signal types tracked' },
      { num: 'Centralized', label: 'source of truth in Clay' },
    ] },

  { id: 'verkada-abm', co: 'Verkada', logo: 'V', color: 'blueberry',
    person: 'Davide Grieco', personRole: 'Head of Growth',
    category: 'ABM campaigns', tags: ['abm'],
    title: '600+ auto-generated landing pages/campaign',
    problem: 'Niche audience targeting required manual research that could not scale across channels.',
    solution: [
      'Scrape HOA directories across all 50 states',
      'Match prospects to LinkedIn; classify ICP skills',
      'Tailor ads, landing pages, mail per signals',
      'Upload enriched audiences to LinkedIn Ads',
    ],
    impact: [
      { num: '2x',   label: 'LinkedIn ad match rates' },
      { num: '600+', label: 'auto-generated landing pages' },
    ] },

  { id: 'verkada-ads', co: 'Verkada', logo: 'V', color: 'blueberry',
    person: 'Davide Grieco', personRole: 'Head of Growth',
    category: 'Ad targeting', tags: ['abm'],
    title: '~100% LinkedIn audience match rate',
    problem: 'Native LinkedIn filters cannot reach niche audiences, leaving half of prospects unmatched.',
    solution: [
      'Ingest prospect name and email lists into Clay',
      'Match each prospect to their LinkedIn profile',
      'Identify unique ICP skills patterns per prospect',
      'Sync matched audiences to LinkedIn Ads',
    ],
    impact: [
      { num: '2x',    label: 'LinkedIn ad match lift' },
      { num: '~100%', label: 'match rate (up from 50%)' },
    ] },

  { id: 'align-competitive', co: 'A-LIGN', logo: 'A', color: 'lime',
    person: 'Arthur Lorente', personRole: 'Director of GTM Operations',
    category: 'Competitive listening', tags: ['signals','abm'],
    title: '2,000 accounts researched across 15 services',
    problem: 'Manual research delivered shallow competitive intel data too slowly for reps to act on.',
    solution: [
      'AI researches 2,000 accounts across 15 services',
      'Map competitor presence and justification per account',
      'Surface competitor and need context per rep',
      'Push displacement insights live into Salesforce',
    ],
    impact: [
      { num: '83%',   label: 'reduction in research costs' },
      { num: '15x',   label: 'more data points than manual' },
      { num: '$6.8M', label: 'pipeline from displacement' },
    ] },

  { id: 'exitfive-event', co: 'Exit Five', logo: 'E', color: 'lemon',
    person: 'Dan Murphy', personRole: 'COO',
    category: 'Event marketing', tags: ['abm','prospecting'],
    title: '27K contacts for regional event targeting',
    problem: 'No geographic data to target the right audience for in-person events.',
    solution: [
      'Enrich 27K contacts with geographic location data',
      'Identify audience clusters by region automatically',
      'Target local subscribers for regional invitations',
      'Push targeted lists to HubSpot for outreach',
    ],
    impact: [
      { num: '27,000', label: 'contacts with geographic data' },
      { num: '100%',   label: 'event targeting automated' },
      { num: '50%',    label: 'of database enriched' },
    ] },

  { id: 'merge-event', co: 'Merge', logo: 'M', color: 'ube',
    person: 'Tim Bourcier', personRole: 'RevOps & Marketing Lead',
    category: 'Event marketing', tags: ['abm','prospecting'],
    title: 'One-person events team, automated',
    problem: 'One-person events team cannot source, brief, and capture leads at scale.',
    solution: [
      'Agent scrapes event platforms for opportunities',
      'Score events by location, speakers, audience fit',
      'Brief reps with attendee roles and solutions',
      'Enrich Slack-captured leads; push to Salesforce',
    ],
    impact: [
      { num: '2x \u2192 5x', label: 'cost-to-pipeline ratio' },
      { num: '+50%',  label: 'event-sourced deals' },
      { num: '25%',   label: 'quarterly pipeline from events' },
    ] },

  { id: 'align-event', co: 'A-LIGN', logo: 'A', color: 'lime',
    person: 'Arthur Lorente', personRole: 'Director of GTM Operations',
    category: 'Event marketing', tags: ['abm','outbound'],
    title: '$9M pipeline from event targeting',
    problem: 'Manually identifying and engaging relevant event prospects didn\u2019t scale.',
    solution: [
      'Enrich event prospect lists via LinkedIn profiles',
      'Match enriched profiles to target ICP criteria',
      'Tailor outreach using LinkedIn role and event context',
      'Push personalized sequences to outreach platform',
    ],
    impact: [
      { num: '$9M', label: 'pipeline influenced via events' },
    ] },
];

/* ── Pretty workflow-tag → label map ───────────────────────── */
window.WORKFLOW_LABELS = {
  enrichment:        'CRM enrichment',
  outbound:          'Automated outbound',
  scoring:           'Account scoring',
  signals:           'Signal alerts',
  lifecycle:         'Lifecycle marketing',
  inbound:           'Inbound enrichment',
  prospecting:       'Prospecting & TAM',
  plg:               'PLG assist',
  abm:               'ABM campaigns',
  'rep-productivity':'Rep productivity',
  research:          'Research at scale',
};

/* ──────────────────────────────────────────────────────────────────
   Picker: returns top N case studies that match a graduate's tags.
   Each result gets a `matchedTag` — the graduate's workflow tag the
   study lined up against — so the card can show that label.
   ────────────────────────────────────────────────────────────────── */
window.pickCaseStudies = function(gradTags, n){
  n = n || 3;
  const studies = window.CLAY_CASE_STUDIES;
  const orderedTags = Array.from(gradTags || []);
  const tagSet = new Set(orderedTags);

  // score each study by tag overlap, remember the primary matched tag
  const scored = studies.map(s => {
    const matched = s.tags.filter(t => tagSet.has(t));
    let matchedTag = null;
    for (const t of orderedTags){ if (matched.includes(t)){ matchedTag = t; break; } }
    return { s, overlap: matched.length, matchedTag };
  }).filter(x => x.overlap > 0)
    .sort((a, b) => b.overlap - a.overlap);

  // category diversity tie-break
  const picked = [];
  const seenCategory = new Set();
  for (const x of scored){
    if (picked.length >= n) break;
    if (seenCategory.has(x.s.category)) continue;
    picked.push(Object.assign({}, x.s, { matchedTag: x.matchedTag }));
    seenCategory.add(x.s.category);
  }
  for (const x of scored){
    if (picked.length >= n) break;
    if (!picked.find(p => p.id === x.s.id)) picked.push(Object.assign({}, x.s, { matchedTag: x.matchedTag }));
  }
  return picked;
};
