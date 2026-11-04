"use client";

import { useEffect, useMemo, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import {
  ArrowRight,
  BarChart3,
  Briefcase,
  Building2,
  Check,
  ChevronDown,
  Cpu,
  Database,
  Gift,
  Globe,
  Loader2,
  Lock,
  Mail,
  MessageSquare,
  Palette,
  Radar,
  Search,
  Send,
  Sparkles,
  Target,
  TrendingUp,
  Users,
  Webhook,
  Zap,
  type LucideIcon,
} from "lucide-react";

/* ──────────────────────────────────────────────────────────────
   Config
   ────────────────────────────────────────────────────────────── */

const STEP_MS = 650; // time per workflow step
const GATE_MS = 11000; // lead-capture modal delay

type Status = "queued" | "active" | "done";

const STEPS = [
  "Trigger webhook",
  "Ingest domain",
  "Search company",
  "Build company profile",
  "Extract brand guidelines",
  "Identify TAM",
  "Pick your signals",
  "Score ICP",
  "Prioritize accounts",
  "Map buying committee",
  "Draft paid social",
  "Write VP message",
  "Write RevOps email",
  "Plan direct mail",
  "Weight engagement signals",
  "Build Fit × Engagement tiers",
  "Draft tier 1 plays",
  "Draft tier 2 plays",
  "Set measurement plan",
  "Finalize plan",
];
const TOTAL = STEPS.length;

// Sidebar phases → step index ranges [start, end] inclusive
const PHASES: { label: string; range: [number, number] }[] = [
  { label: "Company profile", range: [0, 3] },
  { label: "Brand guidelines", range: [4, 4] },
  { label: "Total addressable market", range: [5, 5] },
  { label: "Signals", range: [6, 6] },
  { label: "ICP scoring", range: [7, 8] },
  { label: "Channel plays", range: [9, 13] },
  { label: "Engagement score", range: [14, 15] },
  { label: "Tiered plays", range: [16, 19] },
];

/* Graph layout — fixed canvas, nodes absolutely positioned */
const W = 1080;
const H = 830;
const NW = 196;
const NH = 62;

type GNode = {
  id: string;
  step: number;
  title: string;
  kicker: string;
  icon: LucideIcon;
  tint: string;
  x: number;
  y: number;
};

const NODES: GNode[] = [
  { id: "trigger", step: 0, kicker: "Trigger", title: "Webhook", icon: Webhook, tint: "bg-[#FBE189] text-[#9E5802]", x: 442, y: 16 },
  { id: "ingest", step: 1, kicker: "Action", title: "Ingest {domain}", icon: Globe, tint: "bg-[#EEF773] text-[#808000]", x: 442, y: 126 },
  { id: "search", step: 2, kicker: "Enrich", title: "Search company", icon: Search, tint: "bg-[#CFE6FF] text-[#1D5FB0]", x: 142, y: 246 },
  { id: "profile", step: 3, kicker: "AI", title: "Build company profile", icon: Building2, tint: "bg-[#E2D9FF] text-[#5B3FD1]", x: 442, y: 246 },
  { id: "brand", step: 4, kicker: "AI", title: "Brand guidelines", icon: Palette, tint: "bg-[#F8B9E4] text-[#A3237A]", x: 742, y: 246 },
  { id: "tam", step: 5, kicker: "Find", title: "Identify TAM", icon: Users, tint: "bg-[#C8F0D9] text-[#16784A]", x: 292, y: 376 },
  { id: "signals", step: 6, kicker: "Signals", title: "Pick your Signals", icon: Radar, tint: "bg-[#CFE6FF] text-[#1D5FB0]", x: 592, y: 376 },
  { id: "icp", step: 7, kicker: "Score", title: "Score ICP", icon: Target, tint: "bg-[#E2D9FF] text-[#5B3FD1]", x: 442, y: 496 },
  { id: "prio", step: 8, kicker: "Route", title: "Prioritize Accounts", icon: BarChart3, tint: "bg-[#FCC9AB] text-[#B53D0A]", x: 442, y: 606 },
  { id: "committee", step: 9, kicker: "Channel", title: "Buying committee", icon: Users, tint: "bg-[#FCC9AB] text-[#B53D0A]", x: 0, y: 746 },
  { id: "social", step: 10, kicker: "Channel", title: "Paid social", icon: TrendingUp, tint: "bg-[#FCC9AB] text-[#B53D0A]", x: 221, y: 746 },
  { id: "vp", step: 11, kicker: "Channel", title: "VP message", icon: MessageSquare, tint: "bg-[#FCC9AB] text-[#B53D0A]", x: 442, y: 746 },
  { id: "revops", step: 12, kicker: "Channel", title: "RevOps email", icon: Mail, tint: "bg-[#FCC9AB] text-[#B53D0A]", x: 663, y: 746 },
  { id: "mail", step: 13, kicker: "Channel", title: "Direct mail", icon: Gift, tint: "bg-[#FCC9AB] text-[#B53D0A]", x: 884, y: 746 },
];

const EDGES: [string, string][] = [
  ["trigger", "ingest"],
  ["ingest", "search"],
  ["ingest", "profile"],
  ["ingest", "brand"],
  ["search", "tam"],
  ["profile", "tam"],
  ["profile", "signals"],
  ["brand", "signals"],
  ["tam", "icp"],
  ["signals", "icp"],
  ["icp", "prio"],
  ["prio", "committee"],
  ["prio", "social"],
  ["prio", "vp"],
  ["prio", "revops"],
  ["prio", "mail"],
];

const SIGNALS = [
  { title: "Hiring SDRs or RevOps", desc: "3+ open GTM roles posted in the last 30 days.", pts: 15, tag: "Hiring", tagCls: "bg-[#C8F0D9] text-[#16784A]" },
  { title: "Evaluating data vendors", desc: "AI agent detects RFPs and G2 comparison research.", pts: 20, tag: "Custom AI Signal", tagCls: "bg-[#E2D9FF] text-[#5B3FD1]" },
  { title: "Adopted Salesforce + Outreach", desc: "New sequencing tool installed this quarter.", pts: 10, tag: "Tech stack", tagCls: "bg-[#CFE6FF] text-[#1D5FB0]" },
  { title: "New VP of Sales", desc: "Leadership change in the last 90 days.", pts: 15, tag: "Hiring", tagCls: "bg-[#C8F0D9] text-[#16784A]" },
  { title: "Mentions 'pipeline efficiency'", desc: "Earnings calls, blog posts, and exec LinkedIn posts.", pts: 10, tag: "Custom AI Signal", tagCls: "bg-[#E2D9FF] text-[#5B3FD1]" },
  { title: "Churned from competitor", desc: "Removed a legacy enrichment tool from their stack.", pts: 20, tag: "Tech stack", tagCls: "bg-[#CFE6FF] text-[#1D5FB0]" },
];

const FEATURES = [
  { title: "Data", desc: "Waterfall 150+ providers to build a complete profile of every account and contact.", icon: Database, tint: "bg-[#EEF773] text-[#102B03]" },
  { title: "Signals + Intent", desc: "Watch hiring, tech stack, funding, and custom AI signals that predict buying.", icon: Radar, tint: "bg-[#C8F0D9] text-[#0E4F33]" },
  { title: "Prioritization", desc: "Score fit and engagement so reps spend time on accounts ready to move.", icon: BarChart3, tint: "bg-[#D9D6FF] text-[#2B2A8F]" },
  { title: "Conversion", desc: "Draft plays for every channel — email, social, ads, and direct mail.", icon: Send, tint: "bg-[#FCC9AB] text-[#7A2A06]" },
];

/* ──────────────────────────────────────────────────────────────
   Helpers
   ────────────────────────────────────────────────────────────── */

const cleanDomain = (raw: string) =>
  raw.trim().toLowerCase().replace(/^https?:\/\//, "").replace(/^www\./, "").split("/")[0] || "clay.com";

const initials = (domain: string) => {
  const [name = "c", tld = "c"] = domain.split(".");
  return (name[0] + tld[0]).toUpperCase();
};

const statusOf = (step: number, current: number): Status =>
  step < current ? "done" : step === current ? "active" : "queued";

const edgePath = (a: GNode, b: GNode) => {
  const x1 = a.x + NW / 2;
  const y1 = a.y + NH;
  const x2 = b.x + NW / 2;
  const y2 = b.y;
  const dy = (y2 - y1) * 0.55;
  return `M ${x1} ${y1} C ${x1} ${y1 + dy}, ${x2} ${y2 - dy}, ${x2} ${y2}`;
};

/* ──────────────────────────────────────────────────────────────
   Shared bits
   ────────────────────────────────────────────────────────────── */

function ClayLogo({ className = "h-6" }: { className?: string }) {
  // eslint-disable-next-line @next/next/no-img-element
  return <img src="clay-logo.png" alt="Clay" className={`${className} w-auto`} />;
}

function Pill({ status }: { status: Status }) {
  const map = {
    done: "bg-[#C8F0D9] text-[#16784A]",
    active: "bg-[#FBE189] text-[#9E5802]",
    queued: "bg-oat-200 text-oat-400",
  } as const;
  const label = { done: "Done", active: "Running", queued: "Queued" }[status];
  return (
    <span className={`inline-flex items-center gap-1 rounded-full px-2 py-0.5 text-[11px] font-medium ${map[status]}`}>
      {status === "active" && <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-[#FDBE11]" />}
      {label}
    </span>
  );
}

function Reveal({ children, delay = 0, className = "" }: { children: React.ReactNode; delay?: number; className?: string }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 24 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-60px" }}
      transition={{ duration: 0.5, delay, ease: [0.22, 1, 0.36, 1] }}
      className={className}
    >
      {children}
    </motion.div>
  );
}

/* ──────────────────────────────────────────────────────────────
   View 1 — Landing
   ────────────────────────────────────────────────────────────── */

function Header() {
  return (
    <header className="sticky top-0 z-30 border-b border-line bg-oat-100/85 backdrop-blur">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6">
        <div className="flex items-center gap-10">
          <ClayLogo />
          <nav className="hidden items-center gap-7 text-[15px] text-oat-500 lg:flex">
            {["Product", "Solutions", "Resource", "Company"].map((n) => (
              <button key={n} className="flex items-center gap-1 transition-opacity hover:opacity-60">
                {n} <ChevronDown className="h-3.5 w-3.5" />
              </button>
            ))}
            <button className="transition-opacity hover:opacity-60">Pricing</button>
          </nav>
        </div>
        <div className="flex items-center gap-2">
          <button className="hidden rounded-lg px-4 py-2 text-[15px] hover:bg-oat-200 sm:block">Log in</button>
          <button className="hidden rounded-lg border border-oat-300 bg-white px-4 py-2 text-[15px] hover:bg-oat-200 sm:block">Get a demo</button>
          <button className="rounded-lg bg-black px-4 py-2 text-[15px] text-white hover:bg-oat-500">Sign up</button>
        </div>
      </div>
    </header>
  );
}

function Landing({ onSubmit }: { onSubmit: (domain: string) => void }) {
  const [domain, setDomain] = useState("clay.com");

  return (
    <motion.div key="landing" exit={{ opacity: 0, y: -16 }} transition={{ duration: 0.35 }}>
      <Header />
      <main className="mx-auto max-w-7xl px-4 pb-24 pt-20 sm:px-6 sm:pt-28">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
          className="mx-auto max-w-3xl text-center"
        >
          <span className="inline-flex items-center gap-1.5 rounded-full border border-oat-300 bg-white px-3 py-1 text-xs font-medium text-oat-400">
            <Sparkles className="h-3.5 w-3.5 text-[#FF7714]" /> ABM Plan Generator
          </span>
          <h1 className="mt-6 text-[44px] font-semibold leading-[1.05] tracking-[-0.03em] sm:text-[64px]">
            Your personalized ABM strategy for 2027
          </h1>
          <p className="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-oat-400">
            Drop in your domain. Clay finds the customers who already won&apos;t you, scores the accounts that look like them,
            picks the signals worth watching, and drafts the plays for every channel.
          </p>

          <form
            onSubmit={(e) => {
              e.preventDefault();
              onSubmit(cleanDomain(domain));
            }}
            className="mx-auto mt-10 flex max-w-xl flex-col gap-2 rounded-2xl border border-oat-300 bg-white p-2 text-left shadow-[0_8px_30px_rgba(27,26,24,0.06)] sm:flex-row sm:items-center"
          >
            <label className="flex-1 px-3 py-1">
              <span className="block text-[11px] font-medium uppercase tracking-wide text-oat-400">Your company domain*</span>
              <input
                required
                value={domain}
                onChange={(e) => setDomain(e.target.value)}
                placeholder="clay.com"
                className="w-full bg-transparent text-base outline-none placeholder:text-oat-300"
              />
            </label>
            <button
              type="submit"
              className="group flex items-center justify-center gap-2 rounded-xl bg-black px-5 py-3.5 text-[15px] font-medium text-white transition hover:bg-oat-500"
            >
              Build no-CRM motion
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
            </button>
          </form>
        </motion.div>

        <div className="mt-24 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {FEATURES.map((f, i) => (
            <motion.div
              key={f.title}
              initial={{ opacity: 0, y: 24 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: 0.25 + i * 0.08 }}
              className="rounded-2xl border border-line bg-white p-6 transition-shadow hover:shadow-[0_8px_30px_rgba(27,26,24,0.08)]"
            >
              <div className={`flex h-11 w-11 items-center justify-center rounded-xl ${f.tint}`}>
                <f.icon className="h-5 w-5" />
              </div>
              <h3 className="mt-5 text-lg font-semibold tracking-tight">{f.title}</h3>
              <p className="mt-2 text-sm leading-relaxed text-oat-400">{f.desc}</p>
            </motion.div>
          ))}
        </div>
      </main>
    </motion.div>
  );
}

/* ──────────────────────────────────────────────────────────────
   View 2 — Generation canvas
   ────────────────────────────────────────────────────────────── */

function Sidebar({ domain, current }: { domain: string; current: number }) {
  return (
    <aside className="lg:sticky lg:top-6 lg:h-[calc(100vh-3rem)] lg:w-72 lg:shrink-0">
      <div className="flex h-full flex-col rounded-2xl border border-line bg-white p-5">
        <div className="flex items-center gap-3">
          <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-black text-sm font-semibold text-white">
            {initials(domain)}
          </div>
          <div className="min-w-0">
            <div className="truncate text-base font-semibold">{domain}</div>
            <div className="text-xs text-oat-400">Your plan so far</div>
          </div>
        </div>

        <div className="my-5 h-1.5 overflow-hidden rounded-full bg-oat-200">
          <motion.div
            className="h-full rounded-full bg-black"
            animate={{ width: `${(Math.min(current, TOTAL) / TOTAL) * 100}%` }}
            transition={{ duration: 0.4 }}
          />
        </div>

        <ol className="space-y-1 overflow-y-auto">
          {PHASES.map((p) => {
            const [s, e] = p.range;
            const st: Status = current > e ? "done" : current >= s ? "active" : "queued";
            return (
              <li key={p.label} className="flex items-center justify-between gap-2 rounded-lg px-2 py-2 hover:bg-oat-200/60">
                <span className="flex items-center gap-2.5 text-sm">
                  <span
                    className={`flex h-5 w-5 items-center justify-center rounded-full border ${
                      st === "done" ? "border-[#16784A] bg-[#16784A] text-white" : st === "active" ? "border-[#FDBE11]" : "border-oat-300"
                    }`}
                  >
                    {st === "done" ? <Check className="h-3 w-3" /> : st === "active" ? <Loader2 className="h-3 w-3 animate-spin text-[#9E5802]" /> : null}
                  </span>
                  <span className={st === "queued" ? "text-oat-400" : ""}>{p.label}</span>
                </span>
                <Pill status={st} />
              </li>
            );
          })}
        </ol>

        <div className="mt-auto hidden pt-5 lg:block">
          <ClayLogo className="h-4 opacity-40" />
        </div>
      </div>
    </aside>
  );
}

function NodeCard({ node, status, domain }: { node: GNode; status: Status; domain: string }) {
  const Icon = node.icon;
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.92 }}
      animate={{ opacity: status === "queued" ? 0.55 : 1, scale: 1 }}
      transition={{ duration: 0.35 }}
      style={{ left: node.x, top: node.y, width: NW, height: NH }}
      className={`absolute flex items-center gap-3 rounded-xl border bg-white px-3 shadow-[0_2px_8px_rgba(27,26,24,0.05)] transition-colors ${
        status === "active" ? "animate-glow border-[#FDBE11]" : status === "done" ? "border-line" : "border-dashed border-oat-300"
      }`}
    >
      <div className={`flex h-9 w-9 shrink-0 items-center justify-center rounded-lg ${node.tint}`}>
        <Icon className="h-4 w-4" />
      </div>
      <div className="min-w-0 flex-1">
        <div className="text-[10px] font-medium uppercase tracking-wide text-oat-400">{node.kicker}</div>
        <div className="line-clamp-2 text-[12.5px] font-medium leading-tight">{node.title.replace("{domain}", domain)}</div>
      </div>
      <div className="flex h-5 w-5 shrink-0 items-center justify-center">
        <AnimatePresence mode="wait">
          {status === "done" ? (
            <motion.span
              key="done"
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              transition={{ type: "spring", stiffness: 500, damping: 22 }}
              className="flex h-5 w-5 items-center justify-center rounded-full bg-[#16784A] text-white"
            >
              <Check className="h-3 w-3" strokeWidth={3} />
            </motion.span>
          ) : status === "active" ? (
            <motion.span key="active" initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
              <Loader2 className="h-4 w-4 animate-spin text-[#9E5802]" />
            </motion.span>
          ) : null}
        </AnimatePresence>
      </div>
    </motion.div>
  );
}

function WorkflowGraph({ current, domain }: { current: number; domain: string }) {
  const byId = useMemo(() => Object.fromEntries(NODES.map((n) => [n.id, n])), []);

  return (
    <div className="canvas-grid overflow-x-auto rounded-2xl border border-line">
      <div className="relative mx-auto my-8" style={{ width: W, height: H }}>
        <svg className="pointer-events-none absolute inset-0" width={W} height={H}>
          {EDGES.map(([from, to]) => {
            const a = byId[from];
            const b = byId[to];
            const d = edgePath(a, b);
            const live = current >= b.step; // target reached → edge is lit
            const flowing = current === b.step; // target active → animate flow
            return (
              <g key={`${from}-${to}`}>
                <path d={d} fill="none" stroke="#D1CDC7" strokeWidth={1.5} strokeDasharray="4 4" />
                {live && (
                  <motion.path
                    d={d}
                    fill="none"
                    stroke={flowing ? "#FDBE11" : "#1B1A18"}
                    strokeWidth={1.75}
                    initial={{ pathLength: 0 }}
                    animate={{ pathLength: 1 }}
                    transition={{ duration: 0.5, ease: "easeOut" }}
                  />
                )}
                {flowing && (
                  <path d={d} fill="none" stroke="#9E5802" strokeWidth={1.75} strokeDasharray="6 6" className="animate-dash" />
                )}
              </g>
            );
          })}
        </svg>
        {NODES.map((n) => (
          <NodeCard key={n.id} node={n} status={statusOf(n.step, current)} domain={domain} />
        ))}
      </div>
    </div>
  );
}

function SignalsSection({ visible }: { visible: boolean }) {
  return (
    <section className="mt-12">
      <Reveal>
        <div className="flex items-end justify-between gap-4">
          <div>
            <div className="text-xs font-medium uppercase tracking-wide text-oat-400">Step 15 · Signals</div>
            <h2 className="mt-1 text-2xl font-semibold tracking-tight">Signals + Engagement Score</h2>
          </div>
          <span className="hidden rounded-full bg-oat-200 px-3 py-1 text-xs text-oat-400 sm:block">Max 90 pts</span>
        </div>
      </Reveal>
      <div className="mt-5 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {SIGNALS.map((s, i) => (
          <Reveal key={s.title} delay={i * 0.07}>
            <div className={`h-full rounded-2xl border border-line bg-white p-5 transition ${visible ? "" : "opacity-60"}`}>
              <div className="flex items-start justify-between gap-3">
                <span className={`rounded-full px-2.5 py-0.5 text-[11px] font-medium ${s.tagCls}`}>{s.tag}</span>
                <span className="rounded-md bg-black px-2 py-0.5 text-xs font-semibold text-white">+{s.pts} pts</span>
              </div>
              <h3 className="mt-4 font-semibold">{s.title}</h3>
              <p className="mt-1.5 text-sm leading-relaxed text-oat-400">{s.desc}</p>
            </div>
          </Reveal>
        ))}
      </div>
    </section>
  );
}

function TieringSection({ unlocked }: { unlocked: boolean }) {
  // rows = Fit (high→low), cols = Engagement (low→high)
  const grid = [
    [2, 1, 1],
    [3, 2, 1],
    [3, 3, 2],
  ];
  const tierCls: Record<number, string> = {
    1: "bg-black text-white",
    2: "bg-[#FBE189] text-[#372201]",
    3: "bg-oat-200 text-oat-400",
  };
  const tiers = [
    { t: 1, name: "Tier 1 — Strike now", accounts: 48, play: "1:1 VP message, direct mail, and paid social to the full buying committee.", icon: Zap },
    { t: 2, name: "Tier 2 — Warm up", accounts: 212, play: "RevOps email sequence plus retargeting until engagement crosses 40 pts.", icon: Cpu },
    { t: 3, name: "Tier 3 — Nurture", accounts: 1340, play: "Always-on paid social and monthly signal re-checks.", icon: Briefcase },
  ];

  return (
    <section className="mt-12 pb-16">
      <Reveal>
        <div className="text-xs font-medium uppercase tracking-wide text-oat-400">Step 16 · Prioritization</div>
        <h2 className="mt-1 text-2xl font-semibold tracking-tight">Fit x Engagement</h2>
      </Reveal>
      <div className="mt-5 grid gap-4 lg:grid-cols-[minmax(0,380px)_1fr]">
        <Reveal>
          <div className="rounded-2xl border border-line bg-white p-5">
            <div className="flex gap-3">
              <div className="flex w-5 items-center justify-center">
                <span className="-rotate-90 whitespace-nowrap text-[11px] font-medium uppercase tracking-wide text-oat-400">ICP Fit →</span>
              </div>
              <div className="flex-1">
                <div className="grid grid-cols-3 gap-2">
                  {grid.flat().map((t, i) => (
                    <motion.div
                      key={i}
                      initial={{ opacity: 0, scale: 0.85 }}
                      whileInView={{ opacity: 1, scale: 1 }}
                      viewport={{ once: true }}
                      transition={{ delay: 0.1 + i * 0.05 }}
                      className={`flex aspect-square items-center justify-center rounded-xl text-sm font-semibold ${tierCls[t]}`}
                    >
                      T{t}
                    </motion.div>
                  ))}
                </div>
                <div className="mt-2 text-center text-[11px] font-medium uppercase tracking-wide text-oat-400">Engagement →</div>
              </div>
            </div>
          </div>
        </Reveal>

        <div className="relative space-y-3">
          {tiers.map((t, i) => (
            <Reveal key={t.t} delay={i * 0.08}>
              <div
                className={`flex items-start gap-4 rounded-2xl border border-line bg-white p-5 transition ${
                  !unlocked && t.t <= 2 ? "select-none blur-[5px]" : ""
                }`}
              >
                <div className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-xl ${tierCls[t.t]}`}>
                  <t.icon className="h-4 w-4" />
                </div>
                <div className="flex-1">
                  <div className="flex flex-wrap items-center justify-between gap-2">
                    <h3 className="font-semibold">{t.name}</h3>
                    <span className="text-xs text-oat-400">{t.accounts.toLocaleString()} accounts</span>
                  </div>
                  <p className="mt-1 text-sm leading-relaxed text-oat-400">{t.play}</p>
                </div>
              </div>
            </Reveal>
          ))}
          {!unlocked && (
            <div className="pointer-events-none absolute inset-x-0 top-0 flex h-[calc(66%)] items-center justify-center">
              <span className="flex items-center gap-1.5 rounded-full bg-black px-3 py-1.5 text-xs font-medium text-white">
                <Lock className="h-3.5 w-3.5" /> Tier 1 & 2 plays locked
              </span>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}

function Generator({ domain, current, unlocked }: { domain: string; current: number; unlocked: boolean }) {
  const done = current >= TOTAL;
  const shown = Math.min(current + 1, TOTAL);

  return (
    <motion.div
      key="generator"
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.45, ease: [0.22, 1, 0.36, 1] }}
      className="mx-auto flex max-w-[1500px] flex-col gap-6 p-4 sm:p-6 lg:flex-row"
    >
      <Sidebar domain={domain} current={current} />

      <main className="min-w-0 flex-1">
        <div className="mb-4 flex flex-wrap items-center justify-between gap-3">
          <div>
            <div className="flex items-center gap-1.5 text-xs text-oat-400">
              <span>ABM Plan</span> <span>/</span> <span className="text-oat-500">{domain}</span>
            </div>
            <h1 className="mt-1 text-2xl font-semibold tracking-tight">
              {done ? "Your motion is ready" : "Clay is building your motion..."}
            </h1>
            <p className="mt-0.5 text-sm text-oat-400">{done ? "All steps complete." : STEPS[Math.min(current, TOTAL - 1)]}</p>
          </div>
          <div className="flex items-center gap-2">
            <span className="rounded-full border border-line bg-white px-3 py-1 text-xs font-medium tabular-nums">
              {shown} of {TOTAL} steps
            </span>
            {done ? (
              <span className="flex items-center gap-1.5 rounded-full bg-[#C8F0D9] px-3 py-1 text-xs font-medium text-[#16784A]">
                <Check className="h-3.5 w-3.5" /> Complete
              </span>
            ) : (
              <span className="flex items-center gap-1.5 rounded-full bg-[#FBE189] px-3 py-1 text-xs font-medium text-[#9E5802]">
                <span className="relative flex h-2 w-2">
                  <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-[#FDBE11] opacity-75" />
                  <span className="relative inline-flex h-2 w-2 rounded-full bg-[#FDBE11]" />
                </span>
                Building
              </span>
            )}
          </div>
        </div>

        <WorkflowGraph current={current} domain={domain} />
        <SignalsSection visible={current >= 14} />
        <TieringSection unlocked={unlocked} />
      </main>
    </motion.div>
  );
}

/* ──────────────────────────────────────────────────────────────
   View 3 — Lead capture modal
   ────────────────────────────────────────────────────────────── */

function GateModal({ open, onUnlock }: { open: boolean; onUnlock: (email: string) => void }) {
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return setError("Enter a valid work email.");
    if (/@(gmail|yahoo|hotmail|outlook|icloud)\./i.test(email)) return setError("Please use your work email.");
    setError("");
    setLoading(true);
    setTimeout(() => onUnlock(email), 700);
  };

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 p-4 backdrop-blur-md"
          role="dialog"
          aria-modal="true"
          aria-labelledby="gate-title"
        >
          <motion.div
            initial={{ opacity: 0, y: 24, scale: 0.96 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 12, scale: 0.98 }}
            transition={{ type: "spring", stiffness: 320, damping: 28 }}
            className="w-full max-w-md rounded-3xl bg-white p-8 shadow-[0_30px_80px_rgba(0,0,0,0.25)]"
          >
            <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-[#FDBE11]">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src="clay-icon.png" alt="" className="h-8 w-8 object-contain" />
            </div>
            <h2 id="gate-title" className="mt-6 text-2xl font-semibold tracking-tight">
              Unlock your ABM Plan
            </h2>
            <p className="mt-1.5 text-oat-400">Preview all tier 1 and tier 2 plays.</p>

            <form onSubmit={submit} className="mt-6 space-y-3">
              <label className="block">
                <span className="mb-1.5 block text-sm font-medium">Work email</span>
                <input
                  type="email"
                  autoFocus
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="you@company.com"
                  className="w-full rounded-xl border border-oat-300 px-4 py-3 outline-none transition focus:border-black focus:ring-4 focus:ring-black/5"
                />
              </label>
              {error && <p className="text-sm text-[#C22E3D]">{error}</p>}
              <button
                type="submit"
                disabled={loading}
                className="group flex w-full items-center justify-center gap-2 rounded-xl bg-black py-3.5 font-medium text-white transition hover:bg-oat-500 disabled:opacity-70"
              >
                {loading ? <Loader2 className="h-4 w-4 animate-spin" /> : <>View my plan <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" /></>}
              </button>
            </form>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

/* ──────────────────────────────────────────────────────────────
   Page — state machine
   landing → building (timer) → gated (modal) → unlocked
   ────────────────────────────────────────────────────────────── */

type Phase = "landing" | "building" | "gated" | "unlocked";

export default function Page() {
  const [phase, setPhase] = useState<Phase>("landing");
  const [domain, setDomain] = useState("clay.com");
  const [current, setCurrent] = useState(0);

  const running = phase !== "landing";

  // Advance workflow steps on a timer (keeps running behind the modal).
  useEffect(() => {
    if (!running || current >= TOTAL) return;
    const t = setTimeout(() => setCurrent((c) => c + 1), STEP_MS);
    return () => clearTimeout(t);
  }, [running, current]);

  // Show lead-capture gate after GATE_MS of generation.
  useEffect(() => {
    if (phase !== "building") return;
    const t = setTimeout(() => setPhase("gated"), GATE_MS);
    return () => clearTimeout(t);
  }, [phase]);

  // Lock scroll while gated.
  useEffect(() => {
    document.body.style.overflow = phase === "gated" ? "hidden" : "";
  }, [phase]);

  const start = (d: string) => {
    setDomain(d);
    setCurrent(0);
    setPhase("building");
    window.scrollTo({ top: 0 });
  };

  return (
    <>
      <AnimatePresence mode="wait">
        {phase === "landing" ? (
          <Landing key="landing" onSubmit={start} />
        ) : (
          <Generator key="generator" domain={domain} current={current} unlocked={phase === "unlocked"} />
        )}
      </AnimatePresence>
      <GateModal open={phase === "gated"} onUnlock={() => setPhase("unlocked")} />
    </>
  );
}
