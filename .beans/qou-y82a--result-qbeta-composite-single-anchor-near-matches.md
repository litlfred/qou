---
# qou-y82a
title: 'RESULT: qbeta composite single_anchor_near_matches collapses 25 -> 4 from muon to proton'
status: completed
type: task
priority: normal
created_at: 2026-08-24T17:35:38Z
updated_at: 2026-09-05T09:29:10Z
---

## The number

`qbeta_composite_crossanchor_2factor_sweep`, re-run at the proton anchor:

    data.single_anchor_near_matches:  25  ->  4

Nothing else in the witness changes shape. The whole 39% payload delta is that
one list.

## Why it is worth its own bean

It is a statement about the q_beta composite search, not about the migration:
**most of the single-anchor near-matches were artifacts of the muon pin.** A
near-match that survives one anchor and not the other is evidence about the
candidate, and 21 of 25 did not survive.

## It is NOT a truncation, and the guard says otherwise

`witness_shape_guard.py` flags it: "payload collapsed: 161 -> 98 leaves (39%
gone, tolerance 30%) ... almost certainly a partial write (the producer writes
incrementally and was interrupted)."

That heuristic is wrong here. Measured: a completed, uninterrupted 900 s run
(rc=0, no timeout) reproduces 98 leaves exactly. The guard is right to be
suspicious of a shrinking payload in general -- it exists because a gutted
witness scores zero raw floats and reads as a perfect drain (qou-h4xk) -- but a
real anchor-dependent result set can shrink legitimately.

The witness was left UNCOMMITTED in PR #5664 rather than committed with the
gate red or the guard widened. Whoever picks this up should decide whether the
25 -> 4 collapse is a result to report, and only then how the guard should
learn about it. Do not widen the tolerance to make this green.


---

## RESOLVED 2026-08-24 — PR #5700 (draft). The framing above was wrong; recording the correction.

**Root cause, and it is not anchor-dependence of the candidates.** The producer
reads both pins by name (`q_at` = proton, `q_muon_at` = muon) but its stem was
listed under `ideal_muon` in `computations/q0_anchor_manifest.json`, which makes
`q_parameter` override `q_at()` to the muon anchor. BOTH legs of the cross-anchor
comparison therefore sat on the muon pin:

    q_at()      1.1099785955573347  (muon, via the manifest override)
    q_muon_at() 1.1099785956427390  (muon)
    swing       0.00032782   vs the documented 0.04948227  -- 151x low

AGENTS.md names this class verbatim ("a comparison producer needs BOTH pins and
the manifest cannot serve it ... belongs under `physical_proton`"), with
`mu_substrate_tension_audit_100dps` (155x) as the precedent. Same failure class,
same magnitude.

**Three corrections to this bean's own numbers.**

1. The count was **27, not 25**. The witness truncated at `near_matches[:25]`
   while `n_single_anchor_near_matches` said 27. This bean read the list length.
2. The survivor count is **0, not 4**. The two near-match sets are **disjoint**
   -- all 27 leave, 4 entirely new ones arrive.
3. "A near-match that survives one anchor and not the other is evidence about
   the candidate" -- **not here**. `single_anchor_near_matches` is exactly the
   candidates within TOL_NEAR = 1% of the target, so it is a function of where
   the target sits. Moving the target 2.4% moves a window of half-width 1% clean
   off its old position:

       muon-pinned window   [-2.0403900, -1.9999862]
       proton-pinned window [-2.0900360, -2.0486491]

   Disjoint. The candidate values barely moved (q_at shifts 1.2e-8 relative).
   What moved was the WINDOW. The 27 -> 4 change is a corrected measurement, not
   evidence about any candidate.

**Structure in the 27 lost: they were the "c_3 ~ -2" neighbourhood.** Under the
muon target -2.0201881 the constant `-2` itself misses by 9.993e-3 -- just inside
the 1% window -- and so does everything around it; the set is dominated by `-2`,
`J_Hopf(q)` (J_Hopf(1) = -2) and near-`-2` q-Pochhammer differences. Under the
correct proton target `-2` misses by 3.351e-2, which is the c_3-normalised form
of the 3.47% gap AGENTS.md records for `c_3 = -2 = J_Hopf(q=1)` (independent
check that the corrected run is right). The old set was re-reporting one
already-known fact 27 times over.

**The 4 real proton-anchor near-matches** (new best matcher, still NEGATIVE):
`q²+q⁻² − [4]_q` 1.627e-03, `[4]_q ÷ -2` 7.008e-03, `J_Hopf(q) − -2` 7.123e-03,
`(q;q)_3 − q²+q⁻²` 7.856e-03.

**Scope: (a), scope-limited negative.** No 2-factor composite of THESE atoms,
alone, hits the c_3 target at both anchors within 1 ppm. NOT (b) -- no proved
invariant excludes any ingredient, and the 27 departures are a window artifact.
Recorded in the witness as `scope_classification`. The overall
NEGATIVE_2FACTOR_SATURATED verdict is unchanged and is now, for the first time,
actually tested: under the collapsed swing the criterion could not separate a
closure from a coincidence.

**Shape guard: no change to the guard, no tolerance widening.** It already
carries the right escape hatch, documented in its own §"A NOTE ON LEGITIMATE
SHRINKAGE" -- `--accept` plus the reason in the commit message. Inspected
candidate-by-candidate (above). Rejected: widening `--tolerance` (forbidden, and
blinds the guard corpus-wide), and adding the file to `SELF_DESCRIBING` (that
list is for audit outputs whose payload IS the corpus's findings; this is not
one, and the exemption would be permanent for a one-time correction). The shrink
is now self-explanatory inside the witness via `near_match_window` and
`anchor_separation_relative`.

Also: the bean's "900 s completed run" is a timeout budget, not a duration --
the producer runs in **1.5 s**.

**Producer hardening landed with the fix:** refuses with an explanation on stdout
when the anchors are closer than 1e-9 relative; near-match list untruncated; all
misses carried as mpf and serialized with `_precision.fmt` (raw float64 leaves
81 -> 5, fixed at the producer, no baseline touched). Both assertions now PASS
(both were failing on `main`).

Spun out: **qou-1w90** -- the environment guard's `_version_tuple` orders opaque
hex hashes, so `pyhecke_native_build` reports a false "downgrade" (the same pair
reads as an "upgrade" in the other direction). Not fixed here:
`tools/qou-substrate/` is the qou-aj91 agent's scope.


---

## CLOSED 2026-09-05 — every item verified live on `main` `262ee53eeea`

This bean measured a result, then corrected three of its own numbers, then landed
the producer hardening. All of it is on main; only the status was never moved.

Confirmed in `computations/qbeta/qbeta_composite_crossanchor_2factor_sweep.py`:

| item | site |
|---|---|
| refuse-guard when the two anchors are closer than 1e-9 relative | `:306-311` |
| `anchor_separation_relative` carried in the witness | `:430` |
| `near_match_window` (the two disjoint windows) | `:431` |
| `scope_classification` — the (a) vs (b) record | `:479-490` |

The three self-corrections are the part worth keeping, and they are the reason
this bean should not be read by its title:

1. the count was **27, not 25** (the witness truncated at `near_matches[:25]`);
2. survivors are **0, not 4** — the two sets are **disjoint**;
3. and the framing was wrong: `single_anchor_near_matches` is by construction the
   candidates within `TOL_NEAR = 1 %` of the target, so moving the target 2.4 %
   moves a half-width-1 % window clean off its old position
   (`[-2.0403900, -1.9999862]` → `[-2.0900360, -2.0486491]`). The 27 → 4 change is
   **a corrected measurement, not evidence about any candidate** — the candidate
   values barely moved (`q_at` shifts 1.2e-8 relative); the *window* moved.

The 27 departures were the `c_3 ≈ -2` neighbourhood re-reporting one already-known
fact 27 times: under the correct proton target `-2` misses by 3.351e-2, which is
the `c_3`-normalised form of the 3.47 % gap AGENTS.md records for
`c_3 = -2 = J_Hopf(q=1)`. That agreement is an independent check that the
corrected run is right.

Scope **(a)**, correctly: no 2-factor composite of *these* atoms, alone, hits the
`c_3` target at both anchors within 1 ppm. Not (b) — no proved invariant excludes
any ingredient, and the departures are a window artifact.

**Nothing was left for an agent.** The one spin-out, `qou-1w90` (the environment
guard's `_version_tuple` ordering opaque hex hashes, so `pyhecke_native_build`
reads as a false "downgrade"), was deliberately scoped out to the `qou-aj91`
agent's `tools/qou-substrate/` territory and carries its own bean. The shape
guard was inspected candidate-by-candidate and **not** widened; `--tolerance`
widening and a `SELF_DESCRIBING` exemption were both considered and rejected in
the body, which is the correct disposition under the anti-baseline-widening rule.
