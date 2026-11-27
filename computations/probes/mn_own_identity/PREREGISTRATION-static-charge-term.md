# Pre-registration: ℒ plus the static quark-charge term, energy map fixed by CAL-1 (2026-11-21)

Owner request (thread, 2026-11-21): "1y", i.e. option 1 of §30: test ℒ plus the static
quark-charge term, with its energy map fixed by CAL-1 only. Written before any number in this
test is computed. Earlier numbers it reuses (§28: T_e, Δ_D) are cited, not re-chosen.

## Definitions (fixed before computing)

- ℒ′ = 𝒟² + S, where S = QPair·hol is the static quark-charge term of the corpus
  (`NucleonWeightSpaceTwoTerm`: QPair = 0 on W_p, −⅓·1 on W_n; hol = V³ for the nucleon).
  S has degree 0 in 𝒟. Coefficient +1, the same unit coefficient as the terms of ℒ. No other
  coefficient is considered.
- Energy map: E(X) = λ·T(ℒ′_X), linear, the same as §28. λ = m_e/T(ℒ′_e) (CAL-1).
- The electron's S is 0, because QPair sums over quark strands and the electron
  σ₀σ₁σ₀ has none. **This is an assumption**, recorded here. Any other strand-charge assignment
  for the electron would be a choice, and none is tried.
- Connection: ∇ = hol − q^{writhe}·1 (§28). Two trace arms, the same as §28: P (plain trace;
  the electron is traced over all 8 states) and K (Tr(K^{⊗3}·)/[2]³, the ruled weighting).
- q₀ = the proton pin (`qou_substrate.constants.Q_50_DIGIT_STR`), m_e = `M_E_MEV_STR`. Exact
  sympy throughout, evaluated with mpmath at 60 dps. No float64.

## Exact form expected (to be checked, not assumed)

The n − p of S is tr_{W_n}(−⅓·V³) − 0 = −⅓·tr V³ = −1 + h⁴[3]_q/3 in arm P (Lean:
`trace_Vp3_sub_three` plus conjugacy). In arm K it carries an extra q⁻¹/[2]³. So:

  (E_n − E_p)/m_e = (Δ_D + Δ_S)/T_e.

## Predictions (before computing)

1. Both arms: E_n − E_p < 0 at q₀ (neutron **lighter**). Δ_S ≈ −1 dominates Δ_D ≈ 10⁻³.
2. Magnitude: |E_n − E_p| ≈ 0.1·m_e ≈ 50 keV in both arms. That is about 4 % of the CODATA
   value and has the opposite sign.
3. The limit q → 1 is nonzero: −1/8 in both arms. T_e(1) = 8 in arm P, and T_e(1) = 1 in arm K
   while the weight also gives 1/8.
4. Scope: if 1 and 2 hold, this is a scope (a) negative for ℒ′ with unit coefficient and this
   electron convention. It does not exclude a different coefficient for S, because that
   coefficient is not derived.

The CODATA m_n − m_p = 1.29333 MeV is printed after the numbers, for comparison only.
