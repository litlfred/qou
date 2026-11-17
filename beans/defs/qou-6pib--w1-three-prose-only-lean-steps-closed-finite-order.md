---
# qou-6pib
title: 'W1: three prose-only Lean steps closed — finite order by pigeonhole, Mobius three-point rigidity, the gauge/spectral-curve dictionary'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T11:39:57Z
updated_at: 2026-10-04T15:14:21Z
parent: qou-6qbv
---

## What was closed (2026-09-12, PR #7208)

Three W1 tranches each reached their conclusion through a step their own header
declined to formalise. Two of the three were **not actually hard** — the difficulty
was in how they had been stated, not in the mathematics.

### 1. Finite order of a branch-locus-preserving scaling — `QOU/Mass/BranchLocusFiniteOrder.lean`

#6769 and #7185 both carried *"an automorphism covering `z ↦ l·z` permutes the branch
locus `B`, hence has finite order"* as one prose step. It is **two** halves:

- *permutes `B`* — genuinely geometric (coverings, ramification). **Still prose.**
- *a map sending a finite set of nonzero points into itself has finite order* — **not
  geometric at all.** `exists_pow_eq_one_of_stabilizes`: the `S.card + 1` orbit points
  `l^0·r … l^{S.card}·r` land in a set of size `S.card`, two coincide, the common
  factor `l^i·r` is nonzero. Pigeonhole. Bound `n ≤ S.card`.

Hypothesis is **maps into**, not permutes — the weaker one, which is what a covering
argument hands you before injectivity is known; finiteness upgrades it. Corollaries
`not_stabilizes_of_one_lt_real` / `..._complex` kill every real `l > 1`; the ℂ one is
the live case since `B ⊂ ℂ`, and `B` qualifies because `D(0) = 16 ≠ 0`.

### 2. Möbius three-point rigidity — `QOU/Mass/MoebiusThreePointRigidity.lean`

#7185 deferred `Stab(B) ↪ S₆` as needing *"Möbius machinery Mathlib does not carry in
usable form"*. **It needs none.** Cleared of its denominator, `w` is fixed iff
`a·w + b = w·(c·w + d)`, i.e. `c·w² + (d−a)·w − b = 0` — a quadratic. So:

- `quadratic_zero_of_three_roots` — three *distinct* roots ⇒ all coefficients zero.
  Two subtractions and a cancellation; no discriminants, no `Polynomial`.
- `moebius_id_of_three_fixed` — three distinct fixed points ⇒ the identity's data.
- `moebius_proportional_of_three_agree` — the sharper form, and the one that **is** the
  injectivity: two data agreeing at three distinct points have all `2×2` minors
  vanishing. Hence `Stab(B)` is finite of order at most `6·5·4`.

### 3. The gauge / spectral-curve dictionary — `QOU/Mass/QDifferenceGaugeMatrix.lean`

#7208 cited DVRSZ eq. (2.4.1) rather than proving it. Now at matrix level:
`scalar_gauge_eq` (the gauge law for `F = c·1`, cleared of the inverse),
`det_charMatrix_smul` (`det(X·1 − t·A) = tⁿ·det((X/t)·1 − A)` — the curve **moves**),
`det_charMatrix_conj` (the contrast — conjugation does not move it, which is why a
Higgs field *has* a well-defined SW spectral curve).

## The reusable lesson

**Two of the three were blocked by their statement, not their content.** "Möbius
machinery" and "branched-cover machinery" are real Mathlib gaps — but neither step
actually needed them. Clearing denominators turned the Möbius fixed-point condition
into a quadratic (no chart at `∞` required); clearing the inverse turned DVRSZ (2.4.1)
into a hypothesis with no invertibility side-condition and no `Matrix.inv` junk value.
**When a Lean gap is blamed on missing machinery, check first whether the obstruction
is the formulation.**

## Still open, and said so in every header

- The **covering-space step** — an automorphism of `Σ` permutes `B`. Irreducibly
  geometric; the one remaining prose link, now the *only* one.
- The **group packaging** of `Stab(B) ↪ S₆` as a subgroup of `PGL₂` with the injection
  a homomorphism — bookkeeping over `Matrix.GeneralLinearGroup`, not mathematics.

All three new files: `scripts/lean-shadow-verify.sh` exit 0, `#print axioms` clean
(`propext / Classical.choice / Quot.sound`), no `sorryAx`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-12 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 56 Update (PR #8271)
- Opened PR https://github.com/litlfred/qou/pull/8271 (`b2cbd4734e5f10beb2130e3555212a3d78a87989`, C1 `22c4bf632182163314cbb930ffed44b139fa5265`).
- Compiled under Lean 4.24.0 (`0` `sorry`, `0` `axiom`, `0` warnings) and verified `0` advisories across all 6 static vacuity & borrowed-name audits, with 80-dps `mpmath` witness `computations/probes/round56-devacuify-6qbv-b9cj.witness.json` (`scriptHash = c44bdf430d4f`).
