# Δ_λ / binding front — convergence + fit rollback (2026-07-24)

Coordination pass over the week's binding surge (owner-directed session
review). No new mathematical results are claimed here; this records the
state of the open Δ_λ/binding PRs, the fit rollback, and the recommended
convergence path so effort composes rather than collides.

## Context

The week added ~1075 commits to `main`. On the binding vector, six large
PRs opened 07-19/20, all branched from `6873628` — the commit **before**
main's un-laundering revert `e872909145`
(*"restore honest statuses — un-launder keystone conjectures, unwire
fitted `B_precur` dashboard"*). They share a big mechanical base
(≈18 `.qa.json` sidecars + witness + ~32 small `+2/−2` `.py` edits) plus
a distinct Δ_λ content core each, so they conflict with one another and
with post-revert `main`.

The pre-revert base is the key hazard: **merging any of the six as-is
would re-introduce fitted content that `main` has already reverted.**

## The six Cluster-A PRs

| PR | Angle | Files | Disposition |
|----|-------|------:|-------------|
| #4132 | H3-vs-H4 "No Fudge" | 108 | converge candidate |
| #4133 | Prolongation kernel Bₙ | 110 | converge candidate |
| #4134 | Deuteron B2 algebraic | 111 | converge candidate |
| #4137 | Anti-skew projector | 111 | converge candidate |
| #4135 | 4He Fibonacci-root | 114 | **fit — CLOSED** |
| #4136 | 6Li `[10]_q/[6]_q` | 114 | **fit — CLOSED** |

## Fit rollback (owner directive: "rollback fitted unless we can derive")

Two carried per-isotope corrections tuned to hit AME targets — the
anti-fit / "no seventh fit-based ansatz" rule (AGENTS.md §Δ_λ gate;
§"Axiomatization is NOT a Proof"):

- **#4136** — multiplier `[10]_q/[6]_q` chosen so 6Li `B_gate` reaches
  "exactly 31.991 MeV" (`B_AME`/`E_gate` residual driven to 1.0001).
- **#4135** — a Fibonacci-anyon root evaluated to close 4He's "1.7 MeV
  gap".

Neither multiplier/root is derivable independent of the target in-turn
(that *is* the open Δ_λ problem), so both were **closed** (branches
preserved per the never-delete policy). They may reopen if the
multiplier/root is later **derived** from the rep/knot geometry with no
reference to the measured value — then labelled and re-scoped.

**Nothing fitted is on `main`.** `main`'s `B_gate`/`B_vol` are the honest
parameter-free forms (`a_V = E₀·ln(1/W_free) ≈ 7.584 MeV/nucleon`,
derived), and `e872909145` already un-laundered the fitted `B_precur`.

## Recommended convergence path

1. Rebase the remaining four (#4132/#4133/#4134/#4137) onto **post-revert**
   `main` — surfaces the un-laundering conflict deliberately.
2. Pick **one** canonical Δ_λ content PR; layer the other three angles as
   thin deltas rather than four parallel ~110-file forks.
3. Keep the fits out unless derived.

## Disciplined leads to keep (unchanged from #4058's 7-vector map)

- **V3 A_ω** — the 3d-index leg is **done**: figure-eight 3d-index closed
  (#3868/#3885), u=0 Stokes integer `{3,4}` **derived** (not fit; the
  `−3 = disc(ℚ(√−3))` identification was refuted scope-a — it's the DT
  invariant). Remaining A_ω wall: the deformed-index (u≠0) odd-face
  normalization vs the `[0.147, 0.168]` band bracketing
  `Vol(4₁)/(4π)=0.16153`, plus the `hratio` divisor-cancellation Lean
  lemma in `FaddeevRigidityReduction` (a genuine multi-week Mathlib gap —
  do **not** axiomatize to "close" G3).
- **#4127** — octahedral 4-dilogarithm μ₀ −9% ("missing 3 tetrahedra",
  McPhail-Snyder–Reshetikhin 2509.02354); explicitly scope-(a), no fit,
  `q₀`-fixed probes. The clean bar-even lead.
- **#3805** — superseded stale scaffold (its 3d-index goal is done on the
  siblings above); could be closed as historical.

## Cross-refs

- 7-vector attack map: [`keystone-multivector-attack.md`](keystone-multivector-attack.md) (PR #4058).
- A_ω evidence base: `docs/audits/2026-07-18-g3-stokes-keystone-evidence-base.md`,
  `2026-07-18-figure-eight-3d-index-closed.md`,
  `2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`.
