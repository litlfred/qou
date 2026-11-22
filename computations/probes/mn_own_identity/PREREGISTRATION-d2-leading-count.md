# Pre-registration: a count from the 𝒟² term (fixed before computing)

Date 2026-11-21. Written and committed before `mn_d2_leading_count_probe.py` is run.

**Context.** The 12 in m_p = 2 m_μ F_Bor − 12 m_e was ruled a FIT on 2026-11-18
(`computations/canonical_mass.py` docstring). `mn_twelve_candidates_probe` already lists
several integer 12s with no mechanism; none was selected. This test takes one count from
the 𝒟² term of ℒ, and no other.

**Object.** 𝒟 = q⁻¹∇ + (1 − q⁻¹)ξ with ∇ = hol − 1, hol = (σ₀σ₁⁻¹)³, ξ = T³. This acts on
the nucleon weight spaces W_p ⊕ W_n of (ℂ²)^⊗3 (dimension 3 + 3), with the R-matrix from §21.
∇ = hol − 1 is my identification and has not been ruled.

**Quantity, single definition.** h = q − q⁻¹ (the corpus variable). Write 𝒟 = h·D₁ + O(h²)
as q → 1. Report:
- N := tr(D₁²) on W_p ⊕ W_n, which equals lim_{q→1} tr(𝒟²)/h²;
- the same trace split into W_p and W_n;
- rank(D₁).

**Outcome rule.** I report the values whatever they are. N = 12 would be a mechanism candidate
only, because it depends on two choices that this test does not settle: the unit h (using
1 − q⁻¹ instead scales N by 4) and ∇ = hol − 1. N ≠ 12 is a scope-(a) negative for this one
definition. No other normalisation or subspace will be tried afterwards.

Exact sympy, no floats.
