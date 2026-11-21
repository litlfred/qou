# Pre-registration: the lepton two-term trace, derived the way the nucleon one was (2026-11-21)

Bean `qou-99qc`. Owner (2026-11-21), asked to pick the covariance group for the two-term trace once a
lepton strand is present (PR #8707: full braid group vs colour-preserving braids):
*"The two term came out from looking at the Lagrangian and tracking through non-abelian Stokes. Do the
same for the lepton."* So this tranche derives; it does not pick between the two #8707 readings.

Written before any lepton number is computed.

## The nucleon chain being repeated (to be reconstructed in the audit, step by step)

1. `ℒ = 𝒟² + ψ̄𝒟ψ`, `𝒟 = q⁻¹∇ + ħ_q ι_ξ∇` (`CategoricalLagrangian`). The trace splits into a
   bosonic `ħ_q²·τ(ι_ξ∇)²` (QCD) and a matter `ħ_q·τ(ψψ̄ ι_ξ∇)` (QED) term
   (`CategoricalLagrangianTwoTermBridge`).
2. Non-abelian Stokes: the bosonic term becomes the trace of the boundary word (hol), and the matter
   term becomes a charge insertion carried along that boundary word (Gap 1: one insertion per letter).
3. Covariance: the insertion must give the same value at every point of the closed boundary
   (basepoint independence of the Stokes holonomy, up to conjugation), i.e. commute with every
   crossing that can occur. On three quarks this is #8552 T1/T6 and the 16:44 ruling (all pairs).
4. Weighting: the convention-D Markov trace is the quantum trace `Tr(K^{⊗N}·)/[2]_q^N` (derived).
5. Connected part: subtract the per-weight-space mean (the scored object).

## What will be derived for the lepton

- **D1 (pairs).** The charge on a tensor product of strand objects is additive (Leibniz rule).
  The second-order term is its square, so the pair set is fixed by the strand content, with no
  species distinction: quark–quark, quark–lepton (and lepton–lepton if present), all with weight 1.
- **D2 (covariance).** Requirement 3 applied to words that contain a quark–lepton crossing, with the
  strand's charge carried along with the strand. Prediction to test (not assumed): with distinct
  hypercharges a pairs-only insertion is NOT covariant at a quark–lepton crossing for `q² ≠ 1`, and
  the covariant species-weighted quadratic insertions form a small family.
- **D3 (connected part).** Whether every covariant member is scalar on each total-weight space, so
  that its connected part vanishes on every word.

## Numbers (comparison only)

Re-evaluate #8707's routes (P1 W0/W1/W7 plus the rest of its P1 list, P2 families A and D, P4
sectors `n⊗ν` vs `p⊗e⁻`, route L balances, N2) with whatever D1–D3 yield, reusing #8707's engine
and words verbatim. Exact in `ℚ(q)` (q = 2, 3/2), proton `q₀` at 70 dps, `q → 1` order from exact
evaluations at `1 + 10⁻³`, `1 + 10⁻⁴`. CODATA appears as comparison only. The coupling scale (c_em)
is **not** chosen, and nothing is chosen by a residual.

## Premises carried, not decided

- **L (owner-undecided):** the lepton doublet is a fourth `C²` strand braided by the same Jimbo `Ř`.
  Alternative reading **L′**: the lepton is not a braid strand (spectator object, no crossing with
  quarks). Both are reported.
- Charges: quark `Y = 1/3` (u 2/3, d −1/3); lepton doublet `Y = −1` (ν 0, e⁻ −1), `Q = T³ + Y/2`.
- The photon is the ruled `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (it enters only through #8707's words).

## Pass/fail

The tranche reports whether the derivation settles the #8707 covariance question, with (a)/(b) scope
for every exclusion, and frames anything left as an owner choice.
