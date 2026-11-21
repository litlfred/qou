# Pre-registration: the n − p difference of tr(𝒟²) (fixed before computing)

Date 2026-11-21. Written and committed before `mn_d2_np_difference_probe.py` is run.

**Object.** Same as `PREREGISTRATION-d2-leading-count.md`: 𝒟 = q⁻¹(hol − 1) + (1 − q⁻¹)T³
on W_p, W_n of (ℂ²)^⊗3, with hol = (σ₀σ₁⁻¹)³, h = q − q⁻¹. ∇ = hol − 1 is still unruled.

**Quantity.** Δ(q) := tr_{W_n}(𝒟²) − tr_{W_p}(𝒟²). Report:
- its exact factored form;
- the smallest k with Δ = c·h^k + O(h^{k+1}), and the coefficient c;
- the split of Δ into three pieces: the holonomy-squared part, the Reeb-squared part (zero by
  symmetry if T³ only flips sign), and the cross term.

**Outcome rule.** Report the values whatever they are. Nothing is compared to measured data. If
c or k is the integer 12, that is listed as a coincidence only: the 12 is a ruled fit, and the
unit h is a choice. No other unit, subspace or truncation will be tried afterwards.

Exact sympy, no floats.
