---
# qou-ibbr
title: 'atomic_tr_m_mpfr_50dps muon leg now reads the PROTON y_lambda table: a straddle created by cbc8237daa'
status: todo
type: task
created_at: 2026-08-21T16:31:51Z
updated_at: 2026-08-21T16:31:51Z
---


## What happens

`atomic_tr_m_mpfr_50dps` is a two-pin comparison producer: it emits
`atomic-tr-m-mpfr-50dps.witness.json` (muon leg) and
`atomic-tr-m-mpfr-50dps-proton.witness.json` (proton leg), and its recorded
`median_rel_move` across the q₀ migration is 1.1537e-08 — the μ–p gap to
three figures, which is what a correct two-pin comparison should show.

Upstream `cbc8237daa` ("fix(y_lambda_tower): gate against the PROTON table")
switched `y_lambda_tower_infra.CANONICAL` from the muon y_λ table to the
proton one. That commit is right on its own terms — it fixed a genuine
straddle where the closed form was evaluated at the proton pin and gated
against the muon table. But it is global, so **every** consumer of the tower
now gets proton y_λ, including the leg of this producer that is supposed to
be muon.

## The evidence, measured

Regenerating the producer on a tree containing `cbc8237daa`:

    tr_M_at_q0_50dps   1.14575978171993650736…  ->  1.14575982831999277043…
                       ~40.7 ppb

    abs_diff_vs_bridge  ~1e-9  ->  ~5e-8      (50x WORSE)

The second number is the diagnostic, not the first. This producer computes
tr_M two ways and compares; the disagreement between its own two methods grew
fiftyfold. A pin change moves both methods together and leaves their agreement
intact. Only a straddle — one method on proton y_λ, one not — degrades the
*internal* cross-check like that.

40.7 ppb is also not the μ–p gap (11.54 ppb); it is the gap amplified through
y_λ, the same amplification `cbc8237daa`'s own message measures as 2.40e-09 at
n=2.

## Why nothing on main shows it yet

Main's committed witness predates `cbc8237daa` and has not been regenerated
there. The straddle is latent: it appears the moment anyone re-runs this
producer, on any branch. PR #5349 hit it only because the migration
regenerates producers; I reverted that regeneration rather than ship a
straddled number, so #5349 leaves main's witness untouched.

## To close

1. Decide whether the muon leg should still exist at all. Under the
   proton-everywhere directive (AGENTS.md rule 4, recorded 2026-08-19) the
   answer may be no — in which case this producer becomes single-pin and the
   question dissolves.
2. If it should exist, the muon leg must take muon y_λ explicitly. The
   per-anchor caches already exist (`regenerate_y_lambda_mpfr.OUTPUT_BY_ANCHOR`,
   `y-lambda-mpfr-witness.json` vs `y-lambda-mpfr-proton-witness.json`), so
   this is a call-site change, not a rebuild.
3. Re-run and confirm `abs_diff_vs_bridge` returns to ~1e-9. That number, not
   tr_M itself, is the test that the straddle is gone.
