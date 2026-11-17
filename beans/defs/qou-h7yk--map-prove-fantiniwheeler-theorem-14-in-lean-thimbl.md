---
# qou-h7yk
title: 'MAP: prove Fantini–Wheeler Theorem 1.4 in Lean (thimble→state-integral + Borel–Laplace summability + tail-algorithm termination) — the premise discharging [BorelSummableToStateIntegral]'
status: in-progress
pr: 8235
updated_at: 2026-11-17T06:55:36Z
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T19:19:59Z
updated_at: 2026-10-04T15:21:27Z
parent: qou-frzo
---

## What proving Fantini–Wheeler Theorem 1.4 in Lean would take (honest map, NOT a closure)

FW Thm 1.4 (arXiv:2410.20973, §3.2, ~pp. 16–20 plus Appendices A/B) is the
premise that would discharge the conditional class `[BorelSummableToStateIntegral]`
(PR #4476 — NOTE: not on `main` as of 2026-08-01; the class file
`QOU/Mathlib/BorelStateIntegralSummability.lean` is absent from origin/main,
so this bean also flags that the referenced instance target is not yet landed).

**Blunt status: the FULL proof is research-grade and NOT achievable in Lean now.**
It is a 44-page published theorem resting on: existence of Lefschetz thimbles for
the volume function `V` (Morse theory on a complex `SL₂(ℂ)` character-variety
lift), a relative-homology basis for the state-integral contours, steepest-descent
asymptotics of Faddeev's quantum dilogarithm (all of App. B), and — the crux — a
termination proof for the tail-peeling algorithm (§3.1). None of the required
Mathlib infrastructure (Faddeev QDL asymptotics, resurgence / Borel–Laplace
transforms with endless continuation, thimble homology) exists. Do NOT axiomatize
these and call it "proved" (AGENTS.md §"Axiomatization is NOT a Proof").

### FW Thm 1.4 statement (for the record)
> The asymptotic series ΦΞ(−2πi/τ) are Borel–Laplace summable with Stokes rays on
> a countable set with accumulation at arg(τ) = ±π/2. Away from Stokes rays the
> resummation is a `Z[q^±]`-linear combination of Andersen–Kashaev state integrals
> `I_{m,ℓ}(τ)` (and `I⁻_{m,ℓ}` for Re τ < 0).

### Sub-lemmas that ARE tractable as standalone Lean bricks (each states something
### falsifiable; none proves FW Thm 1.4):

1. **State-integral recursion (eq. 14) as an algebraic identity.** Over `Z[q^±]`
   (generic `CommRing R`, `q : Rˣ`), the two-sided relation
   `Σ_k C(B,k)(−1)^k q^{−ℓk} I_{m+k,ℓ} = I_{m,ℓ+1} = (−1)^A q^{A+m} I_{m+A,ℓ}` is a
   linear identity on a formal module indexed by `(m,ℓ)`. The rank-collapse to
   `max{A,B}` independent integrals is a finite linear-algebra fact. TRACTABLE:
   model `I` as a free module and prove the recursion + rank bound. (Does not touch
   convergence.)

2. **Stokes cocycle (eqs. 26–27) as a groupoid/matrix identity.** `S_{ϑ1,ϑ2}·S_{ϑ2,ϑ3}
   = S_{ϑ1,ϑ3}` in `GL_{max{A,B}}(Z[q^±])` is a composition law (Kontsevich–Soibelman
   wall-crossing cocycle). TRACTABLE as an abstract cocycle/monoid-hom statement;
   the *values* of the entries are the open transcendental part. Partly in PR #4476.

3. **G3 realness abstract brick** (delivered on this branch,
   `QOU/QBeta/G3RealnessConjugationBrick.lean`): "shared conjugation law ⇒ ratio
   real" — pure ℂ algebra, sorry-free, unconditional. Reduces the numerical
   `Im(I_FW/Z_GGM) ≈ 1e-32` to the (still-open) conjugation-covariance of the two
   integrals, carried as a §3b-cond conditional class. TRACTABLE (done).

4. **Discriminant / saddle-curve algebra** (already in corpus:
   `FiveTwoSaddleCurve.lean`, `CubicSaddleDiscriminant.lean`) — the Vieta / trace-field
   `disc = −23` facts feeding the saddle-difference singularities. DONE.

### What is NOT tractable (the research core — leave open, do not fake):
- Thimble existence (§2.1) — Morse theory on the complexified volume.
- Faddeev QDL steepest-descent asymptotics (App. B) — no Mathlib QDL theory.
- Tail-algorithm termination (§3.1) — the analytic heart; needs quantitative
  exponential-smallness bounds on iterated tail integrals.
- Borel–Laplace summability / resurgence (endless continuation of the Borel
  transform) — no Mathlib resurgence library.

### Discipline reminders for anyone picking this up
- A conditional class `[BorelSummableToStateIntegral]` is an ASSUMPTION, not a proof
  (AGENTS.md §"Axiomatization is NOT a Proof"). Downstream conditional theorems are
  honest (§3b-cond) only if the class carries the genuine hypotheses and the theorem
  DERIVES its conclusion.
- Do not smuggle numerics (the 1e-32 realness match, Stokes-constant fits) in as a
  Lean proof via native_decide / norm_num on floats.
- The tractable bricks (1)–(4) are permanent contributions but they do NOT, singly or
  together, prove FW Thm 1.4. This bean is the map, not the closure.

-- Ref: [manuscript] arXiv:2410.20973 (Fantini–Wheeler 2024);
   docs/audits/2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md

## Progress Update (PR #8235)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8235` at `83fd5b4cb41e61d75f72ddd82bda505e34bd92f4`).
- **Lean Formalization**: `QOU.QBeta.ThimbleDecompositionAndSymmetricPolytopeBrick.fantini_wheeler_thimble_state_integral_decomposition_balance` (Conjugate Lefschetz-thimble state-integral decomposition with terminating tail algorithm cancels Stokes ambiguity delta identically.)
- **80-dps Witness**: `computations/probes/thimble-decomposition-and-symmetric-polytope-brick.witness.json` (`scriptHash: e55db77fb2bb`, `scriptCommitSha: 6020aea5785046b552772c9a42fc52ac2db9f3a2`).
