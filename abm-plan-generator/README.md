# ABM Plan Generator (Clay clone)

Next.js (App Router) + Tailwind + Framer Motion + Lucide. All UI and the timer-driven
state machine live in `app/page.tsx`.

```bash
npm install && npm run dev
```

Flow: landing → submit domain → workflow canvas animates 20 steps (650ms each) →
lead-capture modal at 11s → work email unlocks tier 1/2 plays. Tune `STEP_MS` / `GATE_MS`
at the top of `app/page.tsx`.
