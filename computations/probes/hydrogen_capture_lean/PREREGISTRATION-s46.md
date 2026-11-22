# Pre-registration: the two exact facts of #8804 §46, formalised

Written before any computation or Lean on this branch
(`claude/hydrogen-capture-s46-lean-2026-11-22`). Source: §46 of
`computations/probes/mn_own_identity/LITERATURE-COMPARISON.md` and
`mn_hydrogen_from_photons_probe.py` on `claude/mn-own-identity-2026-11-21`. There both facts are
recorded as observed after the computation, on a finite family, not proved.

## Conventions (copied from the probe)

- Jimbo Ř on C²⊗C²: Ř e00 = q e00, Ř e01 = e10, Ř e10 = e01 + h e10, Ř e11 = q e11, h = q − q⁻¹;
  σ⁻¹ = σ − h. σ_i acts on strands i, i+1 of (C²)^{⊗4}, i = 0, 1, 2.
- Photon (owner ruling): γ_i(φ) = 1 + φ₀σ_i + φ₁σ_{i+1} + φ₀₁σ_iσ_{i+1}⁻¹.
- Proton left: strands 0–2, electron strand 3, element W_L = γ₀(φ)·γ₀(ψ)·g·K_L with the cabled
  capture K_L = (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹.
- Proton right (the probe's control): proton strands 1–3, electron strand 0; the proton block is
  TRANSLATED (σ_i ↦ σ_{i+1}: photon γ₁, gluon shifted) and the capture is REFLECTED,
  K_R = (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹.
- O_± = Σ_s T³(s)·W_ss over basis states s whose three proton strands carry two zeros (O₊) or one
  zero (O₋); T³ = (#0 − #1)/2 over all four strands. S = O₊ + O₋ ("S_B1").
- χ_(3) = the one-dimensional character σ_i ↦ q of the proton's three-strand algebra.

## Statements to be proved (generic field R, q ≠ 0, q⁴ + q² + 1 ≠ 0)

Let x be ANY element of the free algebra on two letters s₀, s₁ (so every word in σ₀^{±1}, σ₁^{±1}
and every linear combination, in particular every product of photons and gluon words), N_L(x) its
image with s_i ↦ σ_i, N_R(x) its image with s_i ↦ σ_{i+1}.

- **(i) Factorisation.** S(N_L(x)·K_L) = χ_(3)(x) · S(K_L). Corollary for
  x = γ(φ)γ(ψ)g with fully symbolic φ, ψ:
  S = (1 + qφ₀ + qφ₁ + φ₀₁)(1 + qψ₀ + qψ₁ + ψ₀₁) · χ_(3)(g) · S(K_L), and
  χ_(3)(g) = 1, 1, q, q² for g = 1, V = σ₀σ₁⁻¹, σ₁, σ₁σ₀.
  Also S(K_L) itself is to be computed exactly (expected −h²[3]_q/q², the §46 corrected value,
  since χ_(3)(V³) = 1 and the merged `capL_S`).
- **(ii) Mirror.** O₊^R(N_R(x)·K_R) = −O₋^L(N_L(x)·K_L), and also
  O₋^R(N_R(x)·K_R) = −O₊^L(N_L(x)·K_L), for every x.

Expected mechanism (a hypothesis, to be checked, not assumed): K_L commutes with σ₀, σ₁; the
one-zero and one-one weight spaces are isomorphic B₄-modules, so K_L acts by the same scalar on
their (2,1)-isotypic parts; the image of the proton algebra on each weight space is 5-dimensional
(1, σ₀, σ₁, σ₀σ₁, σ₁σ₀; σ₀σ₁σ₀ is a combination of these because (C²)^{⊗3} has no (1³) part).
For (ii) the strand-reversal-and-spin-flip map conjugates σ_i to σ_{2−i}, and a three-strand
word and its σ₀ ↔ σ₁ image have equal characters (conjugation by the half twist).

If the general statement fails, the fallback is the four listed arms g ∈ {1, V, σ₁, σ₁σ₀} with
the photon weights symbolic, and the report says exactly which.

## What would refute them

- (i) is refuted by one element x (in particular one of the four arms, or one of the five basis
  words) with S(N_L(x)K_L) − χ_(3)(x)S(K_L) ≠ 0 as a rational function of q (and φ, ψ).
- (ii) is refuted by one x with O₊^R(N_R(x)K_R) + O₋^L(N_L(x)K_L) ≠ 0 (or the second pair).
- The mechanism is refuted (without refuting the facts) if K_L fails to commute with σ₀ or σ₁, or
  if σ₀σ₁σ₀ is not a combination of the five basis words on both weight spaces.

## Verification plan

1. sympy over ℚ(q) and ℚ(q, φ, ψ), exact, on the full 16-dimensional space: the four arms, the
   five basis words, both identities, both placements. No float64.
2. Lean, generic `[Field R]`, sorry-free, new file
   `QOU/BraidsAndKnots/HydrogenCaptureFactorisation.lean` importing
   `HydrogenCaptureWeightSpace`; verified with lean-direct only; `#print axioms`.
3. Out of scope: the adjacent capture σ₂⁻² (it does not commute with σ₁, so the mechanism above
   does not apply); any physical reading of the orientation.
