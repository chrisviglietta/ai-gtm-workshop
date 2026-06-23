-- ════════════════════════════════════════════════════════════════════
-- email_is_registered — passwordless email allowlist check for the portal
--
-- Run this once in the Supabase dashboard → SQL Editor (for project
-- misoqdrrryiqckdwgcyk). The portal's login modal calls this function via
-- the anon key to verify an entered work email is in the `graduates` table,
-- WITHOUT exposing the email list to the browser.
-- ════════════════════════════════════════════════════════════════════

-- 1) Keep the graduates table private — the anon key cannot read rows directly.
--    (If other apps rely on anon reading this table, add explicit policies.)
alter table public.graduates enable row level security;

-- 2) Answer only "is this email registered?" (true/false). SECURITY DEFINER
--    lets it read the table even with RLS on, so the list itself stays hidden.
create or replace function public.email_is_registered(p_email text)
returns boolean
language sql
security definer
set search_path = public
as $$
  select exists (
    select 1
    from public.graduates
    where lower(work_email) = lower(trim(p_email))
  );
$$;

-- 3) Allow the public (anon) and signed-in roles to call just this function.
grant execute on function public.email_is_registered(text) to anon, authenticated;

-- Quick test (should return true for a known registered email):
--   select public.email_is_registered('maya@linear.app');
