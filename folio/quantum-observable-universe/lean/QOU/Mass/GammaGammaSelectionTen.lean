import QOU.Mass.GammaGammaH6Interface

/-!
# Candidates up to ten vertices: the reading-3 survivors are the powers of the `q`-deformed 3-cycle

Bean `qou-ales`, step 7 (owner order 2026-09-12 "1 3 2", item 2: extend the `H₃`
candidates to `k ≤ 10`). Steps 4–6 stopped at five vertices because the sign lemmas did.
This file carries the Chebyshev closed forms to `k = 10` and extends both selection
theorems.

## What is proved (all sorry-free)

* `lin_six … lin_ten`, `trace_vtx_pow_six … ten` — `V^k = α_k V + β_k 1` and
  `χ_k = tr V^k` in closed form, `x = h²`:
  `χ₆ = x⁶ + 6x⁵ + 9x⁴ − 4x³ − 12x² + 2`, `χ₇ = −x⁷ − 7x⁶ − 14x⁵ + 21x³ + 7x² − 7x − 1`,
  `χ₈ = x⁸ + 8x⁷ + 20x⁶ + 8x⁵ − 30x⁴ − 24x³ + 12x² + 8x − 1`,
  `χ₉ = −x⁹ − 9x⁸ − 27x⁷ − 21x⁶ + 36x⁵ + 54x⁴ − 9x³ − 27x² + 2`,
  `χ₁₀ = x¹⁰ + 10x⁹ + 35x⁸ + 40x⁷ − 35x⁶ − 98x⁵ − 15x⁴ + 60x³ + 15x² − 10x − 1`.
* `chi_signs_six_to_ten` — on `0 < x ≤ 1/10` the signs are `(+, −, −, +, −)`, so with
  step 4 the pattern for `k = 1..10` is `− − + − − + − − + −`:
  **`χ_k > 0 ⇔ 3 ∣ k`** on the whole interval (`vertexPow_frobeniusFeasible_iff_three_dvd`).
  The survivors are the powers of `V³`, the `q`-deformed identity of step 4.
* `frobeniusSelected_borromean_ten` — on `H₃`, with candidates `1 ≤ k ≤ 10`, reading 3 still
  selects `k = 3`, for every `1 < q ≤ 23/20`: the new survivors `k = 6, 9` cost 12 and 18.
* `h6_signs_six_to_ten` — the `H₆` `(3,3)` condition `1 + 2χ_m` for `m = 6..10` has signs
  `(+, −, −, +, −)` on **`0 < x ≤ 1/18`**. The interval narrows again: `1 + 2χ₈` changes sign
  at `x ≈ 0.0581` (inside step 6's `1/12`), so on `(0, 1/12]` the `m = 8` row is not
  sign-definite. `1 < q ≤ 10/9` gives `h² ≤ 0.0446 ≤ 1/18` (`h_sq_le_eighteenth_of_q_le`);
  the pin `h² = 0.0437` is inside, with little room.
* `interface_frobenius_table_ten` — on `1 < q ≤ 10/9`, under the branching hypothesis and a
  two-row weight with `y_(3,3) > 0`: `G⁶, G⁹` feasible, `G⁷, G⁸, G¹⁰` infeasible; hence
  `interface_frobeniusFeasible_iff_three_dvd` for `1 ≤ m ≤ 10`.
* `interfaceSelected_three_ten` — the selection of `G³` among `m ≤ 10` needs only
  `G¹, G²` infeasible and `G³` feasible, so it holds on the **wide** interval `1 < q ≤ 23/20`.

## What is NOT proved

`k > 10`; the branching rule (still the hypothesis `InterfaceBranching`); and whether the
`3 ∣ k` pattern persists for all `k` — it is a statement about `cos(kθ)` with
`2 cos θ = −1 − h²`, i.e. about `θ/π`, which step 4 left open. Nothing here reads AME2020,
a CODATA binding value, or a census.
-/

namespace QOU.Mass.GammaGammaSelectionTen

open QOU.Mass.GammaGammaWordSelection
open QOU.Mass.GammaGammaSelectorH3
open QOU.Mass.GammaGammaVertexOrder
open QOU.Mass.GammaGammaFrobeniusSelection
open QOU.Mass.GammaGammaH6Interface

/-! ## Linearisation coefficients and traces, `k = 6..10` -/

section Generic

variable {R : Type*} [CommRing R]

theorem lin_six (t : R) : lin t 6 = (t ^ 5 - 4 * t ^ 3 + 3 * t, -(t ^ 4 - 3 * t ^ 2 + 1)) := by
  ext <;> simp <;> ring

theorem lin_seven (t : R) :
    lin t 7 = (t ^ 6 - 5 * t ^ 4 + 6 * t ^ 2 - 1, -(t ^ 5 - 4 * t ^ 3 + 3 * t)) := by
  ext <;> simp <;> ring

theorem lin_eight (t : R) :
    lin t 8 = (t ^ 7 - 6 * t ^ 5 + 10 * t ^ 3 - 4 * t, -(t ^ 6 - 5 * t ^ 4 + 6 * t ^ 2 - 1)) := by
  ext <;> simp <;> ring

theorem lin_nine (t : R) :
    lin t 9 = (t ^ 8 - 7 * t ^ 6 + 15 * t ^ 4 - 10 * t ^ 2 + 1,
      -(t ^ 7 - 6 * t ^ 5 + 10 * t ^ 3 - 4 * t)) := by
  ext <;> simp <;> ring

theorem lin_ten (t : R) :
    lin t 10 = (t ^ 9 - 8 * t ^ 7 + 21 * t ^ 5 - 20 * t ^ 3 + 5 * t,
      -(t ^ 8 - 7 * t ^ 6 + 15 * t ^ 4 - 10 * t ^ 2 + 1)) := by
  ext <;> simp <;> ring

end Generic

section Traces

variable {R : Type*} [Field R]

theorem trace_vtx_pow_six {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) : (vtx q a b a' h ^ 6).trace =
      (h ^ 2) ^ 6 + 6 * (h ^ 2) ^ 5 + 9 * (h ^ 2) ^ 4 - 4 * (h ^ 2) ^ 3 - 12 * (h ^ 2) ^ 2 + 2 := by
  rw [trace_pow_eq _ _ (vtx_sq hqinv hh ha ha' hb hq1), vtx_trace hqinv hh ha ha' hq1, lin_six]
  ring

theorem trace_vtx_pow_seven {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) : (vtx q a b a' h ^ 7).trace =
      -(h ^ 2) ^ 7 - 7 * (h ^ 2) ^ 6 - 14 * (h ^ 2) ^ 5 + 21 * (h ^ 2) ^ 3 + 7 * (h ^ 2) ^ 2
        - 7 * h ^ 2 - 1 := by
  rw [trace_pow_eq _ _ (vtx_sq hqinv hh ha ha' hb hq1), vtx_trace hqinv hh ha ha' hq1, lin_seven]
  ring

theorem trace_vtx_pow_eight {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) : (vtx q a b a' h ^ 8).trace =
      (h ^ 2) ^ 8 + 8 * (h ^ 2) ^ 7 + 20 * (h ^ 2) ^ 6 + 8 * (h ^ 2) ^ 5 - 30 * (h ^ 2) ^ 4
        - 24 * (h ^ 2) ^ 3 + 12 * (h ^ 2) ^ 2 + 8 * h ^ 2 - 1 := by
  rw [trace_pow_eq _ _ (vtx_sq hqinv hh ha ha' hb hq1), vtx_trace hqinv hh ha ha' hq1, lin_eight]
  ring

theorem trace_vtx_pow_nine {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) : (vtx q a b a' h ^ 9).trace =
      -(h ^ 2) ^ 9 - 9 * (h ^ 2) ^ 8 - 27 * (h ^ 2) ^ 7 - 21 * (h ^ 2) ^ 6 + 36 * (h ^ 2) ^ 5
        + 54 * (h ^ 2) ^ 4 - 9 * (h ^ 2) ^ 3 - 27 * (h ^ 2) ^ 2 + 2 := by
  rw [trace_pow_eq _ _ (vtx_sq hqinv hh ha ha' hb hq1), vtx_trace hqinv hh ha ha' hq1, lin_nine]
  ring

theorem trace_vtx_pow_ten {q a b a' h : R} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) : (vtx q a b a' h ^ 10).trace =
      (h ^ 2) ^ 10 + 10 * (h ^ 2) ^ 9 + 35 * (h ^ 2) ^ 8 + 40 * (h ^ 2) ^ 7 - 35 * (h ^ 2) ^ 6
        - 98 * (h ^ 2) ^ 5 - 15 * (h ^ 2) ^ 4 + 60 * (h ^ 2) ^ 3 + 15 * (h ^ 2) ^ 2
        - 10 * h ^ 2 - 1 := by
  rw [trace_pow_eq _ _ (vtx_sq hqinv hh ha ha' hb hq1), vtx_trace hqinv hh ha ha' hq1, lin_ten]
  ring

end Traces

/-! ## Signs on the intervals -/

section Signs

/-- Power bounds used by the sign lemmas: `x^n ≤ x / c^(n-1)` for `0 < x ≤ 1/c`. -/
theorem pow_bounds_of_le {x c : ℝ} (hx : 0 < x) (hc : 0 < c) (hx1 : x ≤ 1 / c) :
    x ^ 2 ≤ x / c ∧ x ^ 3 ≤ x / c ^ 2 ∧ x ^ 4 ≤ x / c ^ 3 ∧ x ^ 5 ≤ x / c ^ 4 ∧
      x ^ 6 ≤ x / c ^ 5 ∧ x ^ 7 ≤ x / c ^ 6 ∧ x ^ 8 ≤ x / c ^ 7 ∧ x ^ 9 ≤ x / c ^ 8 ∧
      x ^ 10 ≤ x / c ^ 9 := by
  have hxc : x * c ≤ 1 := by
    have := mul_le_mul_of_nonneg_right hx1 hc.le
    rwa [one_div, inv_mul_cancel₀ hc.ne'] at this
  have step : ∀ n : ℕ, x ^ (n + 1) ≤ x / c ^ n → x ^ (n + 2) ≤ x / c ^ (n + 1) := by
    intro n hn
    have hcn : 0 < c ^ n := pow_pos hc n
    have hcn1 : 0 < c ^ (n + 1) := pow_pos hc (n + 1)
    rw [le_div_iff₀ hcn1]
    rw [le_div_iff₀ hcn] at hn
    calc x ^ (n + 2) * c ^ (n + 1) = (x ^ (n + 1) * c ^ n) * (x * c) := by ring
      _ ≤ x * 1 := mul_le_mul hn hxc (by positivity) hx.le
      _ = x := mul_one x
  have h2 : x ^ 2 ≤ x / c := by
    calc x ^ 2 = x * x := by ring
      _ ≤ x * (1 / c) := mul_le_mul_of_nonneg_left hx1 hx.le
      _ = x / c := by ring
  have h3 := step 1 (by simpa using h2)
  have h4 := step 2 h3
  have h5 := step 3 h4
  have h6 := step 4 h5
  have h7 := step 5 h6
  have h8 := step 6 h7
  have h9 := step 7 h8
  have h10 := step 8 h9
  exact ⟨h2, h3, h4, h5, h6, h7, h8, h9, h10⟩

/-- The signs `(+, −, −, +, −)` of `χ_6..χ_10` for every `0 < x ≤ 1/10`. -/
theorem chi_signs_six_to_ten {x : ℝ} (hx : 0 < x) (hx1 : x ≤ 1 / 10) :
    0 < x ^ 6 + 6 * x ^ 5 + 9 * x ^ 4 - 4 * x ^ 3 - 12 * x ^ 2 + 2 ∧
      -x ^ 7 - 7 * x ^ 6 - 14 * x ^ 5 + 21 * x ^ 3 + 7 * x ^ 2 - 7 * x - 1 < 0 ∧
      x ^ 8 + 8 * x ^ 7 + 20 * x ^ 6 + 8 * x ^ 5 - 30 * x ^ 4 - 24 * x ^ 3 + 12 * x ^ 2 + 8 * x
        - 1 < 0 ∧
      0 < -x ^ 9 - 9 * x ^ 8 - 27 * x ^ 7 - 21 * x ^ 6 + 36 * x ^ 5 + 54 * x ^ 4 - 9 * x ^ 3
        - 27 * x ^ 2 + 2 ∧
      x ^ 10 + 10 * x ^ 9 + 35 * x ^ 8 + 40 * x ^ 7 - 35 * x ^ 6 - 98 * x ^ 5 - 15 * x ^ 4
        + 60 * x ^ 3 + 15 * x ^ 2 - 10 * x - 1 < 0 := by
  obtain ⟨h2, h3, h4, h5, h6, h7, h8, h9, h10⟩ :=
    pow_bounds_of_le hx (by norm_num : (0 : ℝ) < 10) hx1
  norm_num at h2 h3 h4 h5 h6 h7 h8 h9 h10
  have p2 : 0 ≤ x ^ 2 := by positivity
  have p3 : 0 ≤ x ^ 3 := by positivity
  have p4 : 0 ≤ x ^ 4 := by positivity
  have p5 : 0 ≤ x ^ 5 := by positivity
  have p6 : 0 ≤ x ^ 6 := by positivity
  have p7 : 0 ≤ x ^ 7 := by positivity
  have p8 : 0 ≤ x ^ 8 := by positivity
  have p9 : 0 ≤ x ^ 9 := by positivity
  have p10 : 0 ≤ x ^ 10 := by positivity
  refine ⟨by linarith, by linarith, by linarith, by linarith, by linarith⟩

/-- The `(3,3)` condition `1 + 2χ_m`, `m = 6..10`, has signs `(+, −, −, +, −)` for every
`0 < x ≤ 1/18`. (`1 + 2χ₈` changes sign near `x ≈ 0.0581`, so `1/12` is not enough.) -/
theorem h6_signs_six_to_ten {x : ℝ} (hx : 0 < x) (hx1 : x ≤ 1 / 18) :
    0 < 1 + 2 * (x ^ 6 + 6 * x ^ 5 + 9 * x ^ 4 - 4 * x ^ 3 - 12 * x ^ 2 + 2) ∧
      1 + 2 * (-x ^ 7 - 7 * x ^ 6 - 14 * x ^ 5 + 21 * x ^ 3 + 7 * x ^ 2 - 7 * x - 1) < 0 ∧
      1 + 2 * (x ^ 8 + 8 * x ^ 7 + 20 * x ^ 6 + 8 * x ^ 5 - 30 * x ^ 4 - 24 * x ^ 3 + 12 * x ^ 2
        + 8 * x - 1) < 0 ∧
      0 < 1 + 2 * (-x ^ 9 - 9 * x ^ 8 - 27 * x ^ 7 - 21 * x ^ 6 + 36 * x ^ 5 + 54 * x ^ 4
        - 9 * x ^ 3 - 27 * x ^ 2 + 2) ∧
      1 + 2 * (x ^ 10 + 10 * x ^ 9 + 35 * x ^ 8 + 40 * x ^ 7 - 35 * x ^ 6 - 98 * x ^ 5
        - 15 * x ^ 4 + 60 * x ^ 3 + 15 * x ^ 2 - 10 * x - 1) < 0 := by
  obtain ⟨h2, h3, h4, h5, h6, h7, h8, h9, h10⟩ :=
    pow_bounds_of_le hx (by norm_num : (0 : ℝ) < 18) hx1
  norm_num at h2 h3 h4 h5 h6 h7 h8 h9 h10
  have p2 : 0 ≤ x ^ 2 := by positivity
  have p3 : 0 ≤ x ^ 3 := by positivity
  have p4 : 0 ≤ x ^ 4 := by positivity
  have p5 : 0 ≤ x ^ 5 := by positivity
  have p6 : 0 ≤ x ^ 6 := by positivity
  have p7 : 0 ≤ x ^ 7 := by positivity
  have p8 : 0 ≤ x ^ 8 := by positivity
  have p9 : 0 ≤ x ^ 9 := by positivity
  have p10 : 0 ≤ x ^ 10 := by positivity
  refine ⟨by linarith, by linarith, by linarith, by linarith, by linarith⟩

/-- `1 ≤ q ≤ 10/9 ⇒ h² ≤ 1/18` (`h² ≤ 0.0446` there; the pin has `0.0437`). -/
theorem h_sq_le_eighteenth_of_q_le {q : ℝ} (hq1 : 1 ≤ q) (hq2 : q ≤ 10 / 9) :
    (q - q⁻¹) ^ 2 ≤ 1 / 18 := by
  have hq0 : 0 < q := by linarith
  have hi1 : q⁻¹ ≤ 1 := inv_le_one_of_one_le₀ hq1
  have hi2 : 9 / 10 ≤ q⁻¹ := by
    rw [le_inv_comm₀ (by norm_num) hq0]
    calc q ≤ 10 / 9 := hq2
      _ = (9 / 10 : ℝ)⁻¹ := by norm_num
  have hh0 : 0 ≤ q - q⁻¹ := by linarith
  have hh1 : q - q⁻¹ ≤ 19 / 90 := by linarith
  nlinarith

end Signs

/-! ## `H₃`: candidates to ten vertices -/

section H3Ten

/-- The closed forms at the concrete Hoefsmit data, `k = 6..10`, `x = h²`. -/
theorem hoefsmitVtx_traces_ten {q : ℝ} (hq1 : 1 < q) :
    (hoefsmitVtx q ^ 6).trace =
        (hOf q ^ 2) ^ 6 + 6 * (hOf q ^ 2) ^ 5 + 9 * (hOf q ^ 2) ^ 4 - 4 * (hOf q ^ 2) ^ 3
          - 12 * (hOf q ^ 2) ^ 2 + 2 ∧
      (hoefsmitVtx q ^ 7).trace =
        -(hOf q ^ 2) ^ 7 - 7 * (hOf q ^ 2) ^ 6 - 14 * (hOf q ^ 2) ^ 5 + 21 * (hOf q ^ 2) ^ 3
          + 7 * (hOf q ^ 2) ^ 2 - 7 * hOf q ^ 2 - 1 ∧
      (hoefsmitVtx q ^ 8).trace =
        (hOf q ^ 2) ^ 8 + 8 * (hOf q ^ 2) ^ 7 + 20 * (hOf q ^ 2) ^ 6 + 8 * (hOf q ^ 2) ^ 5
          - 30 * (hOf q ^ 2) ^ 4 - 24 * (hOf q ^ 2) ^ 3 + 12 * (hOf q ^ 2) ^ 2 + 8 * hOf q ^ 2
          - 1 ∧
      (hoefsmitVtx q ^ 9).trace =
        -(hOf q ^ 2) ^ 9 - 9 * (hOf q ^ 2) ^ 8 - 27 * (hOf q ^ 2) ^ 7 - 21 * (hOf q ^ 2) ^ 6
          + 36 * (hOf q ^ 2) ^ 5 + 54 * (hOf q ^ 2) ^ 4 - 9 * (hOf q ^ 2) ^ 3
          - 27 * (hOf q ^ 2) ^ 2 + 2 ∧
      (hoefsmitVtx q ^ 10).trace =
        (hOf q ^ 2) ^ 10 + 10 * (hOf q ^ 2) ^ 9 + 35 * (hOf q ^ 2) ^ 8 + 40 * (hOf q ^ 2) ^ 7
          - 35 * (hOf q ^ 2) ^ 6 - 98 * (hOf q ^ 2) ^ 5 - 15 * (hOf q ^ 2) ^ 4
          + 60 * (hOf q ^ 2) ^ 3 + 15 * (hOf q ^ 2) ^ 2 - 10 * hOf q ^ 2 - 1 := by
  obtain ⟨hqinv, hh, ha, ha', hb, hq21⟩ := hoefsmit_relations hq1
  unfold hoefsmitVtx
  exact ⟨trace_vtx_pow_six hqinv hh ha ha' hb hq21, trace_vtx_pow_seven hqinv hh ha ha' hb hq21,
    trace_vtx_pow_eight hqinv hh ha ha' hb hq21, trace_vtx_pow_nine hqinv hh ha ha' hb hq21,
    trace_vtx_pow_ten hqinv hh ha ha' hb hq21⟩

/-- **The `H₃` table for `k = 6..10`**: `k = 6, 9` feasible, `k = 7, 8, 10` infeasible, for
every `1 < q ≤ 23/20` and every weight with `y_(2,1) > 0`. -/
theorem hoefsmit_vertexPow_frobenius_table_ten {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (y : H3Block → ℝ) (hy : 0 < y .std) :
    FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 6) ∧
      ¬ FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 7) ∧
      ¬ FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 8) ∧
      FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 9) ∧
      ¬ FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 10) := by
  have hq : 0 < q := by linarith
  obtain ⟨hx, hx1⟩ := hOf_sq_bounds hq1 hq2
  obtain ⟨s6, s7, s8, s9, s10⟩ := chi_signs_six_to_ten hx hx1
  obtain ⟨t6, t7, t8, t9, t10⟩ := hoefsmitVtx_traces_ten hq1
  simp only [hoefsmitH3_vertexPow_iff hq y]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro _; rw [t6]; exact s6.le
  · intro hf; have := hf hy; rw [t7] at this; linarith
  · intro hf; have := hf hy; rw [t8] at this; linarith
  · intro _; rw [t9]; exact s9.le
  · intro hf; have := hf hy; rw [t10] at this; linarith

/-- **Reading 3 on `H₃`, `1 ≤ k ≤ 10`: feasible iff `3 ∣ k`** — the survivors are the powers
of the `q`-deformed 3-cycle `V³`. -/
theorem vertexPow_frobeniusFeasible_iff_three_dvd {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (y : H3Block → ℝ) (hy : 0 < y .std) (k : ℕ) (hk1 : 1 ≤ k) (hk10 : k ≤ 10) :
    FrobeniusFeasible (hoefsmitH3 q) y (vertexPow k) ↔ 3 ∣ k := by
  obtain ⟨n1, n2, f3, n4, n5⟩ := hoefsmit_vertexPow_frobenius_table hq1 hq2 y hy
  obtain ⟨f6, n7, n8, f9, n10⟩ := hoefsmit_vertexPow_frobenius_table_ten hq1 hq2 y hy
  interval_cases k
  · exact ⟨fun h => absurd h n1, fun h => absurd h (by decide)⟩
  · exact ⟨fun h => absurd h n2, fun h => absurd h (by decide)⟩
  · exact ⟨fun _ => ⟨1, rfl⟩, fun _ => f3⟩
  · exact ⟨fun h => absurd h n4, fun h => absurd h (by decide)⟩
  · exact ⟨fun h => absurd h n5, fun h => absurd h (by decide)⟩
  · exact ⟨fun _ => ⟨2, rfl⟩, fun _ => f6⟩
  · exact ⟨fun h => absurd h n7, fun h => absurd h (by decide)⟩
  · exact ⟨fun h => absurd h n8, fun h => absurd h (by decide)⟩
  · exact ⟨fun _ => ⟨3, rfl⟩, fun _ => f9⟩
  · exact ⟨fun h => absurd h n10, fun h => absurd h (by decide)⟩

/-- **Reading 3 still selects `β_Bor` with candidates up to ten vertices**, for every
`1 < q ≤ 23/20`: `k = 6, 9` are feasible but cost 12 and 18. -/
theorem frobeniusSelected_borromean_ten {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (y : H3Block → ℝ) (hy : 0 < y .std) :
    FrobeniusSelected (hoefsmitH3 q) y (vertexPowCands 10) (fun w => (w.length : ℝ))
      borromean := by
  obtain ⟨n1, n2, f3, _, _⟩ := hoefsmit_vertexPow_frobenius_table hq1 hq2 y hy
  refine ⟨⟨3, by norm_num, by norm_num, vertexPow_three.symm⟩, ?_, ?_⟩
  · rw [← vertexPow_three]; exact f3
  · rintro w' ⟨k, hk1, hk10, rfl⟩ hf
    rw [← vertexPow_three]
    interval_cases k
    · exact absurd hf n1
    · exact absurd hf n2
    all_goals norm_num [vertexPow_length]

end H3Ten

/-! ## `H₆`: bonds to ten vertices -/

section H6Ten

/-- **The `H₆` bond table for `m = 6..10`** on `1 < q ≤ 10/9`: `G⁶, G⁹` feasible,
`G⁷, G⁸, G¹⁰` infeasible. -/
theorem interface_frobenius_table_ten {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 10 / 9)
    (B : WedderburnBlocks ℝ Word H6Block H6Block.dim) (hB : InterfaceBranching q B)
    (y : H6Block → ℝ) (hy : ∀ l, 0 < y l → l.twoRow) (h33 : 0 < y .threeThree) :
    FrobeniusFeasible B y (interfaceBond 6) ∧
      ¬ FrobeniusFeasible B y (interfaceBond 7) ∧
      ¬ FrobeniusFeasible B y (interfaceBond 8) ∧
      FrobeniusFeasible B y (interfaceBond 9) ∧
      ¬ FrobeniusFeasible B y (interfaceBond 10) := by
  have hq2' : q ≤ 23 / 20 := by linarith
  obtain ⟨hx, _⟩ := hOf_sq_bounds hq1 hq2'
  have hx18 : hOf q ^ 2 ≤ 1 / 18 := h_sq_le_eighteenth_of_q_le hq1.le hq2
  obtain ⟨t6, t7, t8, t9, t10⟩ := hoefsmitVtx_traces_ten hq1
  obtain ⟨s6, s7, s8, s9, s10⟩ := h6_signs_six_to_ten hx hx18
  obtain ⟨c6, _, _, c9, _⟩ := chi_signs_six_to_ten hx (by linarith)
  simp only [interface_frobeniusFeasible_iff B hB y]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro l hl
    rcases hy l hl with rfl | rfl | rfl | rfl
    · rw [branchedChar_six]; norm_num
    · rw [branchedChar_fiveOne, t6]; linarith
    · rw [branchedChar_fourTwo, t6]; linarith
    · rw [branchedChar_threeThree, t6]; linarith
  · intro h; have := h .threeThree h33; rw [branchedChar_threeThree, t7] at this; linarith
  · intro h; have := h .threeThree h33; rw [branchedChar_threeThree, t8] at this; linarith
  · intro l hl
    rcases hy l hl with rfl | rfl | rfl | rfl
    · rw [branchedChar_six]; norm_num
    · rw [branchedChar_fiveOne, t9]; linarith
    · rw [branchedChar_fourTwo, t9]; linarith
    · rw [branchedChar_threeThree, t9]; linarith
  · intro h; have := h .threeThree h33; rw [branchedChar_threeThree, t10] at this; linarith

/-- **Reading 3 on the `H₆` interface, `1 ≤ m ≤ 10`, `1 < q ≤ 10/9`: feasible iff `3 ∣ m`.** -/
theorem interface_frobeniusFeasible_iff_three_dvd {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 10 / 9)
    (B : WedderburnBlocks ℝ Word H6Block H6Block.dim) (hB : InterfaceBranching q B)
    (y : H6Block → ℝ) (hy : ∀ l, 0 < y l → l.twoRow) (h33 : 0 < y .threeThree)
    (m : ℕ) (hm1 : 1 ≤ m) (hm10 : m ≤ 10) :
    FrobeniusFeasible B y (interfaceBond m) ↔ 3 ∣ m := by
  obtain ⟨n1, n2, f3, n4, n5⟩ := interface_frobenius_table hq1 (by linarith) B hB y hy h33
  obtain ⟨f6, n7, n8, f9, n10⟩ := interface_frobenius_table_ten hq1 hq2 B hB y hy h33
  interval_cases m
  · exact ⟨fun h => absurd h n1, fun h => absurd h (by decide)⟩
  · exact ⟨fun h => absurd h n2, fun h => absurd h (by decide)⟩
  · exact ⟨fun _ => ⟨1, rfl⟩, fun _ => f3⟩
  · exact ⟨fun h => absurd h n4, fun h => absurd h (by decide)⟩
  · exact ⟨fun h => absurd h n5, fun h => absurd h (by decide)⟩
  · exact ⟨fun _ => ⟨2, rfl⟩, fun _ => f6⟩
  · exact ⟨fun h => absurd h n7, fun h => absurd h (by decide)⟩
  · exact ⟨fun h => absurd h n8, fun h => absurd h (by decide)⟩
  · exact ⟨fun _ => ⟨3, rfl⟩, fun _ => f9⟩
  · exact ⟨fun h => absurd h n10, fun h => absurd h (by decide)⟩

/-- **The pp bond `G³` is still selected among `m ≤ 10`**, and on the **wide** interval
`1 < q ≤ 23/20`: only `G¹, G²` infeasible and `G³` feasible are needed, since every bond
with `m ≥ 3` costs at least six crossings. -/
theorem interfaceSelected_three_ten {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (B : WedderburnBlocks ℝ Word H6Block H6Block.dim) (hB : InterfaceBranching q B)
    (y : H6Block → ℝ) (hy : ∀ l, 0 < y l → l.twoRow) (h33 : 0 < y .threeThree) :
    FrobeniusSelected B y (interfaceCands 10) (fun w => (w.length : ℝ)) (interfaceBond 3) := by
  obtain ⟨n1, n2, f3, _, _⟩ := interface_frobenius_table hq1 hq2 B hB y hy h33
  refine ⟨⟨3, by norm_num, by norm_num, rfl⟩, f3, ?_⟩
  rintro w' ⟨m, hm1, hm10, rfl⟩ hf
  interval_cases m
  · exact absurd hf n1
  · exact absurd hf n2
  all_goals norm_num [interfaceBond_length]

end H6Ten

end QOU.Mass.GammaGammaSelectionTen
