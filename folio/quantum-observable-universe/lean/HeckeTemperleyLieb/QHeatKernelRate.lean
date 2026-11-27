import HeckeTemperleyLieb.QJucysMurphyEigen

/-!
# The per-mode q-heat-kernel rate `μ_λ(q)`, read off the bar-symmetrised Murphy sum

Bean `qou-8vt2` (define `ϑ_K`), fibre-level route. That bean's "net position" said the one
thing standing between the corpus and a **derived** per-mode rate `μ_λ` was missing
infrastructure: the q-Jucys–Murphy family in `H_n(q)` and its block eigenvalue. Both have
since landed:

* `qJM`, `barSymJMSum` and its centrality — `HeckeTemperleyLieb.QJucysMurphy`;
* `barSymJMSum_block_eigenvalue_of_pos` — `HeckeTemperleyLieb.QJucysMurphyEigen`
  (Ram 1997, Thm 4.1), for every `λ ⊢ N`, `N ≥ 1`, at generic `q`.

This file does the next, purely algebraic step. Nothing here is evaluated at any anchor,
and no number from measurement enters.

## What is defined

    g_λ(q) := Σ_{c ∈ λ} (q^c − q^{−c})²                  (`cellBracketSqSum`)
    μ_λ(t) := t⁻¹ · g_λ(t²)        (t a square root of q) (`heatRate`)

## What is proved (all sorry-free)

1. **`g_λ` is the block eigenvalue of a central element.** `Θ − 2N·1` acts on `ρ_λ` as
   `g_λ(q)·1` (`heatRate_block`). So `g_λ` is not a chosen bracket: it is the spectrum of
   the central element `Θ − 2N`, where the shift `2N` is the λ-independent constant from
   `cellContentCoshSum_eq_bracket`.
2. **`g_λ` is bar-even for every `λ`** (`cellBracketSqSum_inv`): `g_λ(q⁻¹) = g_λ(q)`.
3. **The bar-parity law `μ_λ(1/q) = q·μ_λ(q)` holds for every `λ`** (`heatRate_bar`).
   The 2026-08-22 finding in `qou-8vt2` was that the law holds *only* on 2×2-box
   partitions. That finding was about the form `ℏ_q² Σ [c]_q [c+1]_q`. For the form the
   Hecke algebra actually produces, the scope restriction disappears.
4. **The vacuum is the only rate-zero mode** (`cellBracketSqSum_eq_zero_iff`): over `ℝ`, with
   `0 < q`, `q ≠ 1`, `g_λ(q) = 0` iff every cell of `λ` has content `0`. So the shift
   `2N` is not a free normalisation either. It is the unique shift that gives the
   content-`0` cell zero rate.

## What is NOT done

`ϑ_K` is still undefined. This file supplies the rates `μ_λ`. It does not choose the mode set `Λ`, so
it does not fix `d = |Λ|` or the recursion coefficients `a_j = e_j({(q−1)μ_λ})`, and it does
not touch `c₃`. Under the bean's guard, fixing any of those by matching a measured value
would be a fit.

Refs: [ram1997] Theorem 4.1; [murphy1992]; [hoefsmit1974].
-/

namespace QOU.SchurWeyl.HeatKernelRate

open QOU.SchurWeyl

section General

variable {K : Type*} [Field K] {N : ℕ}

/-- **The per-mode bracket** `g_λ(q) = Σ_{c∈λ} (q^c − q^{−c})²`. -/
noncomputable def cellBracketSqSum (lam : Partition N) (q : K) : K :=
  ∑ c ∈ (shape lam).cells, (q ^ (cellContent c) - q ^ (-(cellContent c))) ^ 2

/-- The cosh sum is the bracket sum plus the λ-independent shift `2N`. -/
theorem cellContentCoshSum_eq (lam : Partition N) (q : K) (hq : q ≠ 0) :
    cellContentCoshSum lam q = cellBracketSqSum lam q + 2 * (N : K) := by
  rw [cellContentCoshSum_eq_bracket lam q hq, card_shape]
  rfl

/-- **`g_λ` is the block eigenvalue of the central element `Θ − 2N·1`.**

For every `λ ⊢ N` with `N ≥ 1` and generic `q`, the seminormal representation sends
`Θ − 2N·1` to the scalar matrix `g_λ(q)·1`. -/
theorem heatRate_block (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (hN : 0 < N) (lam : Partition N) :
    ∃ ρ : Hecke K q q⁻¹ (N - 1) →ₐ[K] Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) K,
      ρ (barSymJMSum K q q⁻¹ (N - 1) - (2 * (N : K)) • (1 : Hecke K q q⁻¹ (N - 1)))
        = cellBracketSqSum lam q • (1 : Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) K) := by
  obtain ⟨ρ, hρ⟩ := barSymJMSum_block_eigenvalue_of_pos q hq0 hq2 hN lam
  refine ⟨ρ, ?_⟩
  rw [map_sub, hρ, map_smul, map_one, cellContentCoshSum_eq lam q hq0, add_smul,
    add_sub_cancel_right]

/-- **`g_λ` is bar-even, for every `λ`**: `g_λ(q⁻¹) = g_λ(q)`. -/
theorem cellBracketSqSum_inv (lam : Partition N) (q : K) :
    cellBracketSqSum lam q⁻¹ = cellBracketSqSum lam q := by
  unfold cellBracketSqSum
  refine Finset.sum_congr rfl (fun c _ => ?_)
  rw [inv_zpow', inv_zpow', neg_neg]
  ring

/-- **The per-mode rate** `μ_λ = q^{−1/2} · g_λ(q)`, written with `t` a square root of `q`
(`q = t²`). This is the half-integer power the parity law forces (`qou-8vt2`, 2026-08-10), with
the bar-even factor `g_λ` taken from the Hecke algebra rather than chosen. -/
noncomputable def heatRate (t : K) (lam : Partition N) : K :=
  t⁻¹ * cellBracketSqSum lam (t ^ 2)

/-- **The bar-parity law `μ_λ(1/q) = q · μ_λ(q)`, for every `λ`.**

With `q = t²`, the bar involution is `t ↦ t⁻¹`. No 2×2-box restriction is needed. -/
theorem heatRate_bar (t : K) (ht : t ≠ 0) (lam : Partition N) :
    heatRate t⁻¹ lam = t ^ 2 * heatRate t lam := by
  unfold heatRate
  rw [inv_pow, cellBracketSqSum_inv, inv_inv]
  field_simp

end General

section Real

variable {N : ℕ}

/-- Each bracket is nonnegative over `ℝ`. -/
theorem bracket_sq_nonneg (q : ℝ) (c : ℤ) : 0 ≤ (q ^ c - q ^ (-c)) ^ 2 := sq_nonneg _

/-- A single bracket vanishes iff the content is `0`, for `0 < q ≠ 1`. -/
theorem bracket_sq_eq_zero_iff {q : ℝ} (hq0 : 0 < q) (hq1 : q ≠ 1) (c : ℤ) :
    (q ^ c - q ^ (-c)) ^ 2 = 0 ↔ c = 0 := by
  constructor
  · intro h
    have h' : q ^ c = q ^ (-c) := sub_eq_zero.mp (pow_eq_zero_iff (n := 2) two_ne_zero |>.mp h)
    have := zpow_right_injective₀ hq0 hq1 h'
    omega
  · rintro rfl
    simp

/-- **The vacuum is the only rate-zero mode.** Over `ℝ`, for `0 < q ≠ 1`, `g_λ(q) = 0` iff
every cell of `λ` has content `0`. -/
theorem cellBracketSqSum_eq_zero_iff {q : ℝ} (hq0 : 0 < q) (hq1 : q ≠ 1) (lam : Partition N) :
    cellBracketSqSum lam q = 0 ↔ ∀ c ∈ (shape lam).cells, cellContent c = 0 := by
  unfold cellBracketSqSum
  rw [Finset.sum_eq_zero_iff_of_nonneg (fun c _ => bracket_sq_nonneg q _)]
  exact forall₂_congr (fun c _ => bracket_sq_eq_zero_iff hq0 hq1 _)

/-- `g_λ(q) ≥ 0` over `ℝ`: every mode decays or is stationary. -/
theorem cellBracketSqSum_nonneg (q : ℝ) (lam : Partition N) : 0 ≤ cellBracketSqSum lam q :=
  Finset.sum_nonneg (fun _ _ => bracket_sq_nonneg q _)

end Real

end QOU.SchurWeyl.HeatKernelRate
