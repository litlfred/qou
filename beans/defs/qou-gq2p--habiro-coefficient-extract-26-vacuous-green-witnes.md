---
# qou-gq2p
title: '_habiro_coefficient_extract: 26 vacuous-green witnesses, unblocked by qou-wc8f'
status: completed
type: task
priority: normal
created_at: 2026-08-31T07:33:40Z
updated_at: 2026-09-03T04:25:11Z
---

## Status

**Unblocked.** This family was held by `qou-wc8f` — whether a fresh run of the
Habiro cone produced right or wrong numbers. That is settled (#6381, #6385):
the post-R3 convention-D values are correct, the pre-R3 committed ones were the
stale artifact, and the `qou-wc8f` disposition was reversed accordingly.

## Measured on `main` `e8f5a64a81`

    habiro-coefficients-* witnesses (non-deprecated)   30
    still in the vacuous-green baseline               26

All 26 are written by one producer, `computations/_habiro_coefficient_extract.py`
(`invocation.reproduce`: `python3 -u computations/_habiro_coefficient_extract.py`,
no arguments). This is the **largest remaining single-owner family** in the
`qou-srvu` backlog — see `qou-5ax1`, where it is the second row and, now that
`canonical_isotope_witness` is a LEAVE-on-the-merits, the largest *open* one.

## Why it is one unit of work, not 26

Every witness in the family is all-or-nothing vacuous-green (26 of 26 in the
baseline), because they come off one batch run of one producer. One fix drains
all of them. That is the whole point of `qou-5ax1`'s finding that the backlog is
8 producer families rather than 423 independent problems.

## What the assertion probably is — NOT yet established

The witnesses carry `integral=True` and a `reconstruction_matches` flag (the
shared loader `habiro_coefficients_atomic.load_a_m` **refuses** a witness whose
`reconstruction_matches` is false, per bean `qou-s41x`). A reconstruction check
that the loader already trusts enough to refuse on is the obvious candidate for
promotion to a real assertion.

**Do not take that as a plan.** I have not read the producer's source, and the
whole lesson of `qou-5ax1` is that witness *shape* is evidence about the payload
and not about whether the producer computes anything falsifiable — the largest
family in that table turned out to be a read-many orchestrator whose every
available invariant is true by construction. Read `_habiro_coefficient_extract.py`
before writing an assertion.

## Two cautions carried from the arc that unblocked this

1. **The producer is the input to `topic2_mirror_pair_phi8_boundary_scan`.**
   Re-running it moves that scan's numbers — that is exactly the drift chased
   through `qou-wc8f`. The topic2 witness is now refreshed and asserted at the
   D-frame values (#6385), so a re-run should be a no-op there; **verify that it
   is** rather than assuming, and diff the topic2 witness alongside.

2. **`M_max_used` in the topic2 rows is this producer's Habiro depth.** If it
   moves on a re-run, the a_m depth changed and the downstream multiplicities
   will move with it. That is the signal that caught the R3 migration in the
   first place; treat any movement in it as a finding, not as noise.

## Cost

The 2026-08-25 batch that produced these ran 21:49:01 → 21:57:20 — **~8 minutes
for all 18 mirror-pair slugs**. Small. Log it per the long-compute discipline
anyway (`-u … | tee`), because the diff step is where this family's findings
have historically come from.


---

## DRAINED 2026-09-03 (PR #6448)

All 26 asserted; baseline 363 -> 337. Producer re-run 529 s, FAILURES 0.

| assertion | basis |
|---|---|
| `habiro_reconstruction_is_exact` | `sp.expand(reconstruct(a_m,u) - p_u) == 0`, exact, no tolerance |
| `habiro_coefficients_all_integral` | every `a_m` in the coefficient ring |
| `habiro_expansion_non_empty` | non-vacuity guard for the two above |
| `tr_M_two_route_agreement_within_L1` | vs the corpus L1 1 ppQ target |
| `no_atom_extraction_failed` | summary; `failures[]` only from the exception handler |

**The bean's guess was right, and that was luck rather than method.** This bean
named `reconstruction_matches` as the candidate and said explicitly it was NOT a
plan because witness shape is not evidence a producer computes anything
falsifiable. Reading the source confirmed it *is* — and turned up the sharper
point the shape could not have shown: it is an **exact symbolic identity** that
the shared loader already **refuses** on, so a consumer was gating on a flag the
producer asserted nothing about. Keep making that caveat; the guess being right
does not validate guessing.

**Both cautions this bean carried came back clean, and one is now measured
rather than assumed.** The producer feeds `topic2_mirror_pair_phi8_boundary_scan`
and the re-run was expected to be a no-op there after #6385 pinned it at the
D-frame values. It was: the family diff is purely additive (`REMOVED 0`, all 530
added keys under `/assertions`, one `/timestamp` aside), so **`M_max_used` did
not move** and no downstream multiplicity can have shifted.

## A NEW finding the drain produced — the cross-check is harness-capped

`tr_M_at_q0_rel_err` reads ~1e-30 to 1e-34 across the whole family, which looks
like a spectacular two-route agreement. **It is the harness floor.** Lines
272/281/293 of `_habiro_coefficient_extract.py` evaluate through
`sp.N(..., 30)` — 30 significant digits — so the cross-check **cannot resolve
better than ~1e-30 regardless of how well the two routes actually agree**.

Consequences, in order of who they bite:

1. The L1 assertion is sound anyway: 1e-15 is cleared by ~15 orders, and that
   margin is real because the cap is far below the bar.
2. **Nobody may quote these residuals as evidence of 30-digit agreement** — that
   is reporting the arithmetic, not the mathematics, and is the same defect
   class AGENTS.md bans for float64 agreement at 1e-16. The producer's own
   comment already refuses the float64 version of this mistake for `rel_err`;
   the `sp.N(..., 30)` cap one line below is the same trap in mpmath clothing.
3. If anyone ever wants this cross-check to *demonstrate* L1 rather than merely
   clear it, the 30 has to rise. Not urgent, and not this bean's job.

## Not drained here

`habiro-coefficients-extended.witness.json` is a different producer (the one
`721ab7b812` regenerated at the muon pin) and still carries zero assertions. It
was never in this family's 26 and is out of scope; worth its own look.
