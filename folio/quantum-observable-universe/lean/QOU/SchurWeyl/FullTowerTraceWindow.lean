import QOU.SchurWeyl.MolienBalancedForm
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset

/-!
# QOU.SchurWeyl.FullTowerTraceWindow — which partition weights are ONE trace on the whole tower

Bean `qou-slz5` ("derive the weight").  A trace on `H_n(q)` is `tr = Σ_λ w_λ χ^λ`, and it restricts
coherently along `H_1 ⊂ H_2 ⊂ ⋯` iff the weights are harmonic on the Young graph,
`w_ν = Σ_{s addable} w_{ν+s}`.  This file formalises the structural part of the probe
`computations/deltalambda/full_tower_trace_coherence_probe.py`, which checked it in exact `ℚ(q,y)`
for `n ≤ 6`; here it is proved for every `n`.

## Main results

* **Every Ocneanu weight is a full-tower Markov trace (T2).**  For every Markov parameter `z` with
  `q² − 1 − q z ≠ 0`:
  `sum_dim_ocneanuWeight_eq_one` (normalisation), `sum_addable_ocneanuWeight` (branching
  coherence), `sum_ocneanuWeight_mul` (abstract Markov corner) — generic `[Field F]`, `q²` not a
  root of unity; and over `ℝ`, `SeminormalRep.ocneanuMarkovTraceAt : MarkovTraceFamily ℝ q q⁻¹ z`
  with `SeminormalRep.eq_ocneanu_of_markov`: **every** Markov trace with parameter `z` is the
  `ocneanuWeight q z`-weighted seminormal trace.  This removes the restriction of
  `OcneanuWeight`'s docstring ("the Markov property at general `n` is open") for every
  `z ≠ q − q⁻¹`; previously it was proved at the Wenzl levels and at `z = 0` only.
* **The positivity window (T3).**  `ocneanuWeight_pos_of_le`: for `q > 1` and
  `0 ≤ z ≤ q − q⁻¹` **every** weight is strictly positive (ordered field).  The imaginary-rank
  parametrisation `z(y) = (q − q⁻¹) y²/(y² + 1)` (`zOfY`) lands strictly inside the window
  (`zOfY_mem_window`), fills the open window over `ℝ` (`exists_zOfY_eq`), and turns the Ocneanu
  weight into the probe's product `∏_x (y q^{c} + q^{−c}/y) / ((y + 1/y)^n ∏_x [h]_q)`
  (`ocneanuWeight_zOfY`, generic field).
* **The quantum Plancherel weight is not coherent (T1).**  `qPlancherel_not_coherent`: with
  `w_λ = d_q(λ)²/(f^λ Σ_μ d_q(μ)²)`, `w_{(3)} < w_{(4)} + w_{(3,1)}` for every `q > 0`, `q ≠ 1`;
  the defect is `−(u−1)(u−4)²/(3(u+2)(3u²−8u+8))`, `u = (q + q⁻¹)²` (`qPlancherel_defect_eq`).

## Method

`MolienSymmetrisingTrace` proves three weight identities as polynomial identities in an
interpolation variable `a`, by agreement at the infinitely many Wenzl points `a = Q^r`, and then
evaluates at `a = 0` only.  `eval_eq_of_eval_pow` evaluates the same polynomial identity at
**every** `a`.  The link to the Ocneanu weight is a one-cell computation
(`ocneanuWeight_eq_eval_wenzlPoly`):

```
ocneanuWeight q z μ = W_μ(a(z)) / (1 − a(z))^{|μ|},     a(z) = q z / (q z − q² + 1),
```

and the Markov parameter of the interpolated identity, `a(1 − Q)/(q(1 − a))`, is exactly `z`
(`ocneanuA_markov`).  The Wenzl points `a = Q^r` are the levels; `a = 0` is Molien (`z = 0`);
`a = −y²` is the imaginary-rank point `z(y)`.

## What is NOT proved here

* The endpoint `z = q − q⁻¹` (`a = ∞`, the mirror-Molien trace) is excluded from the Markov-trace
  statements by `q² − 1 − q z ≠ 0`; its weights are positive (`ocneanuWeight_pos_of_le` covers it).
* The converse of the window — that for `z < 0` or `z > q − q⁻¹` some weight is `≤ 0` — is not
  proved.
* The T1 hook table is entered by hand; that the lists enumerate all shapes of sizes 3 and 4 with
  their hook lengths is not machine-derived (it is the standard table, reproduced in the docstring).
* Nothing here selects a point of the window: coherence, positivity and the Markov property leave
  the whole interval `z ∈ [0, q − q⁻¹]`.

## Base ring (§7c)

Generic `[Field F]` for every identity; `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` for the
positivity statements (they need an order); `ℝ` only where the seminormal representations (and
hence the trace) are built, and for the square root in `exists_zOfY_eq`.

References: Ocneanu / Jones (1987) `[jones1987]`, Wenzl (1988) `[wenzl1988]`.

LaTeX label: `thm:full-tower-trace-window`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset Polynomial QOU.QBeta.WenzlWeight QOU.Mathlib QOU.QInteger

section Generic

variable {F : Type*} [Field F]

/-- **Interpolation, at every point.**  Two polynomials agreeing at every `Q^r`, `r ≥ 1`, are
equal (`Q` not a root of unity), so they agree at *every* `a`, not only at `a = 0`. -/
theorem eval_eq_of_eval_pow (Q : F) (hQ0 : Q ≠ 0) (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1)
    (p₁ p₂ : F[X]) (h : ∀ r : ℕ, r ≠ 0 → p₁.eval (Q ^ r) = p₂.eval (Q ^ r)) (a : F) :
    p₁.eval a = p₂.eval a := by
  have hp : p₁ - p₂ = 0 := by
    apply Polynomial.eq_zero_of_infinite_isRoot
    refine Set.Infinite.mono ?_
      (Set.infinite_range_of_injective (pow_succ_injective Q hQ0 hgen))
    rintro _ ⟨r, rfl⟩
    show IsRoot (p₁ - p₂) (Q ^ (r + 1))
    rw [IsRoot.def, eval_sub, h (r + 1) (Nat.succ_ne_zero r), sub_self]
  have h0 := congrArg (eval a) hp
  rwa [eval_sub, eval_zero, sub_eq_zero] at h0

/-- **Normalisation of the interpolating polynomial, at every `a`**:
`Σ_{|ν| = n} f^ν W_ν(a) = (1 − a)^n`. -/
theorem sum_dim_eval_wenzlPoly (Q : F) (hQ0 : Q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (n : ℕ) (a : F) :
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
        (numStandardYoungTableaux ν.1 : F) * (wenzlPoly Q ν.1).eval a) = (1 - a) ^ n := by
  have h := eval_eq_of_eval_pow Q hQ0 hgen
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
      C (numStandardYoungTableaux ν.1 : F) * wenzlPoly Q ν.1) ((1 - X) ^ n) (fun r hr => by
        have hbr := levelBracket_ne_zero_of_gen hgen hr
        simp only [eval_finset_sum, eval_mul, eval_C, eval_pow, eval_sub, eval_one, eval_X,
          eval_pow_wenzlPoly Q hQ0 hbr]
        have hs := sum_dim_wenzlWeight_eq_one Q hQ0 hgen hbr (ne_one_of_gen hgen) n
        have e : ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
            (numStandardYoungTableaux ν.1 : F)
              * ((1 - Q ^ r) ^ ν.1.cells.card * wenzlWeight r Q ν.1)
              = (1 - Q ^ r) ^ n * ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
                  (numStandardYoungTableaux ν.1 : F) * wenzlWeight r Q ν.1 := by
          rw [Finset.mul_sum]
          refine Finset.sum_congr rfl fun ν _ => ?_
          rw [ν.2]
          ring
        rw [e, hs, mul_one]) a
  simpa [eval_finset_sum] using h

/-- **Branching of the interpolating polynomial, at every `a`**:
`Σ_{s addable} W_{ν+s}(a) = (1 − a) W_ν(a)`. -/
theorem sum_addable_eval_wenzlPoly (Q : F) (hQ0 : Q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (ν : YoungDiagram) (a : F) :
    (∑ s : {s : ℕ × ℕ // IsAddableCell ν s}, (wenzlPoly Q (addCellOrSelf ν s.1)).eval a)
      = (1 - a) * (wenzlPoly Q ν).eval a := by
  have h := eval_eq_of_eval_pow Q hQ0 hgen
    (∑ s : {s : ℕ × ℕ // IsAddableCell ν s}, wenzlPoly Q (addCellOrSelf ν s.1))
    ((1 - X) * wenzlPoly Q ν) (fun r hr => by
      have hbr := levelBracket_ne_zero_of_gen hgen hr
      simp only [eval_finset_sum, eval_mul, eval_sub, eval_one, eval_X,
        eval_pow_wenzlPoly Q hQ0 hbr]
      rw [← sum_addable_wenzlWeight_all Q hQ0 hgen hbr (ne_one_of_gen hgen) ν, Finset.mul_sum,
        Finset.mul_sum]
      refine Finset.sum_congr rfl fun s _ => ?_
      rw [addCellOrSelf_of s.2, card_addCell s.2]
      ring) a
  simpa [eval_finset_sum] using h

/-- **The Markov corner of the interpolating polynomial, at every `a`.**  If at every level
`r ≥ 1` the data `t, t'` satisfy the level-`r` Markov identity, then
`Σ_L W_L(a) t_L = a(1 − Q)/q · Σ_ν W_ν(a) t'_ν` for every `a`. -/
theorem sum_eval_wenzlPoly_mul (Q q : F) (hQ0 : Q ≠ 0) (hq : q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {m : ℕ}
    (t : {ρ : YoungDiagram // ρ.cells.card = m + 2} → F)
    (t' : {ν : YoungDiagram // ν.cells.card = m + 1} → F)
    (hw : ∀ r : ℕ, r ≠ 0 →
      ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, wenzlWeight r Q L.1 * t L
        = Q ^ r / (q * levelBracket r Q)
          * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1}, wenzlWeight r Q ν.1 * t' ν)
    (a : F) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, (wenzlPoly Q L.1).eval a * t L
      = a * ((1 - Q) / q)
        * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1}, (wenzlPoly Q ν.1).eval a * t' ν := by
  have h := eval_eq_of_eval_pow Q hQ0 hgen
    (∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, C (t L) * wenzlPoly Q L.1)
    (X * C ((1 - Q) / q) * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
      C (t' ν) * wenzlPoly Q ν.1) (fun r hr => by
      have hbr := levelBracket_ne_zero_of_gen hgen hr
      simp only [eval_finset_sum, eval_mul, eval_C, eval_X, eval_pow_wenzlPoly Q hQ0 hbr]
      have e1 : ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
          t L * ((1 - Q ^ r) ^ L.1.cells.card * wenzlWeight r Q L.1)
            = (1 - Q ^ r) ^ (m + 2) * ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
                wenzlWeight r Q L.1 * t L := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun L _ => ?_
        rw [L.2]; ring
      have e2 : ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          t' ν * ((1 - Q ^ r) ^ ν.1.cells.card * wenzlWeight r Q ν.1)
            = (1 - Q ^ r) ^ (m + 1) * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
                wenzlWeight r Q ν.1 * t' ν := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun ν _ => ?_
        rw [ν.2]; ring
      rw [e1, e2, hw r hr, one_sub_pow_eq_mul_levelBracket r Q]
      field_simp
      ring) a
  simp only [eval_finset_sum, eval_mul, eval_C, eval_X] at h
  calc ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, (wenzlPoly Q L.1).eval a * t L
      = ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, t L * (wenzlPoly Q L.1).eval a :=
        Finset.sum_congr rfl fun L _ => mul_comm _ _
    _ = _ := by
        rw [h]
        congr 1
        exact Finset.sum_congr rfl fun ν _ => mul_comm _ _

/-! ## The Ocneanu weight is the interpolating polynomial, rescaled

Put `ζ = q² − 1 − q z` and `a(z) = q z/(q z − q² + 1) = −q z/ζ`.  Then `1 − a = (q² − 1)/ζ`, and
the Ocneanu numerator factor of a cell `(i, j)` of content `c = j − i` is
`q^{2i} ζ + q^{2j+1} z = q^{2i}·ζ·(1 − a·Q^c)`, `Q = q²`.  Comparing with `wenzlPoly`:

```
ocneanuWeight q z μ = W_μ(a(z)) / (1 − a(z))^{|μ|}.
```

This is the same rescaling that turns `W_μ(Q^r)` into the level-`r` Wenzl weight; the level points
are `a = Q^r`, and the Molien point `z = 0` is `a = 0`. -/

/-- The interpolation point attached to a Markov parameter: `a(z) = q z / (q z − q² + 1)`. -/
noncomputable def ocneanuA (q z : F) : F := q * z / (q * z - q ^ 2 + 1)

theorem ocneanuA_eq (q z : F) : ocneanuA q z = -(q * z) / (q ^ 2 - 1 - q * z) := by
  unfold ocneanuA
  rw [neg_div, ← div_neg]
  congr 1
  ring

theorem one_sub_ocneanuA (q z : F) (hd : q ^ 2 - 1 - q * z ≠ 0) :
    1 - ocneanuA q z = (q ^ 2 - 1) / (q ^ 2 - 1 - q * z) := by
  rw [ocneanuA_eq]
  field_simp
  ring

/-- `Q^i · Q^{c(i,j)} = Q^j` for the content `c(i,j) = j − i`. -/
theorem pow_mul_zpow_content (Q : F) (hQ : Q ≠ 0) (x : ℕ × ℕ) :
    Q ^ x.1 * Q ^ content x = Q ^ x.2 := by
  unfold QOU.QBeta.WenzlWeight.content
  rw [zpow_sub₀ hQ, zpow_natCast, zpow_natCast]
  field_simp

/-- **One cell** of the comparison. -/
theorem ocneanu_cell (q z : F) (hq : q ≠ 0) (hd : q ^ 2 - 1 - q * z ≠ 0) (hQ : q ^ 2 ≠ 1)
    (x : ℕ × ℕ) (h : ℕ) :
    (q ^ (2 * x.1) * (q ^ 2 - 1 - q * z) + q ^ (2 * x.2 + 1) * z) / (q ^ (2 * h) - 1)
      = (q ^ 2) ^ x.1 * ((1 - q ^ 2) / (1 - (q ^ 2) ^ h)
          * (1 - (q ^ 2) ^ content x * ocneanuA q z)) / (1 - ocneanuA q z) := by
  have hQ0 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have hu := pow_mul_zpow_content (q ^ 2) hQ0 x
  set u := (q ^ 2) ^ content x with hu_def
  have e1 : q ^ (2 * x.1) = (q ^ 2) ^ x.1 := by rw [pow_mul]
  have e2 : q ^ (2 * x.2 + 1) = (q ^ 2) ^ x.1 * u * q := by rw [hu, pow_succ, pow_mul]
  have e3 : q ^ (2 * h) = (q ^ 2) ^ h := by rw [pow_mul]
  rw [e1, e2, e3, one_sub_ocneanuA q z hd, ocneanuA_eq]
  by_cases hh : (q ^ 2) ^ h = 1
  · rw [hh]; simp
  · have h1 : (q ^ 2) ^ h - 1 ≠ 0 := sub_ne_zero.mpr hh
    have h2 : 1 - (q ^ 2) ^ h ≠ 0 := sub_ne_zero.mpr (Ne.symm hh)
    have h3 : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hQ
    field_simp
    ring

/-- **The Ocneanu weight is the rescaled interpolating polynomial**:
`ocneanuWeight q z μ = W_μ(a(z)) / (1 − a(z))^{|μ|}`, whenever `q² − 1 − q z ≠ 0`. -/
theorem ocneanuWeight_eq_eval_wenzlPoly (q z : F) (hq : q ≠ 0) (hd : q ^ 2 - 1 - q * z ≠ 0)
    (hQ : q ^ 2 ≠ 1) (μ : YoungDiagram) :
    ocneanuWeight q z μ
      = (wenzlPoly (q ^ 2) μ).eval (ocneanuA q z) / (1 - ocneanuA q z) ^ μ.cells.card := by
  rw [eval_wenzlPoly, nPart, ← Finset.prod_pow_eq_pow_sum, ← Finset.prod_const,
    ← Finset.prod_mul_distrib, ← Finset.prod_div_distrib, ocneanuWeight, ← Finset.prod_div_distrib]
  refine Finset.prod_congr rfl fun x hx => ?_
  rw [hookLength_eq_hook hx]
  exact ocneanu_cell q z hq hd hQ x (hook μ x)

/-- **The Markov parameter is recovered**: `a(z)·(1 − Q) / (q·(1 − a(z))) = z`. -/
theorem ocneanuA_markov (q z : F) (hq : q ≠ 0) (hd : q ^ 2 - 1 - q * z ≠ 0) (hQ : q ^ 2 ≠ 1) :
    ocneanuA q z * ((1 - q ^ 2) / q) / (1 - ocneanuA q z) = z := by
  have h3 : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hQ
  rw [one_sub_ocneanuA q z hd, ocneanuA_eq]
  field_simp
  ring

/-! ## Normalisation and branching for the Ocneanu weight at every `z` -/

/-- **Normalisation at every Markov parameter**: `Σ_{|ν| = n} f^ν w_ν(q,z) = 1`, for every `z`
with `q² − 1 − q z ≠ 0` (`Q = q²` not a root of unity). -/
theorem sum_dim_ocneanuWeight_eq_one (q z : F) (hq : q ≠ 0) (hd : q ^ 2 - 1 - q * z ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2) ^ k ≠ 1) (n : ℕ) :
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
        (numStandardYoungTableaux ν.1 : F) * ocneanuWeight q z ν.1) = 1 := by
  have hQ : q ^ 2 ≠ 1 := ne_one_of_gen hgen
  have h1a : 1 - ocneanuA q z ≠ 0 := by
    rw [one_sub_ocneanuA q z hd]
    exact div_ne_zero (sub_ne_zero.mpr hQ) hd
  have hs := sum_dim_eval_wenzlPoly (q ^ 2) (pow_ne_zero 2 hq) hgen n (ocneanuA q z)
  have e : ∀ ν : {ν : YoungDiagram // ν.cells.card = n},
      (numStandardYoungTableaux ν.1 : F) * ocneanuWeight q z ν.1
        = (numStandardYoungTableaux ν.1 : F) * (wenzlPoly (q ^ 2) ν.1).eval (ocneanuA q z)
            / (1 - ocneanuA q z) ^ n := by
    intro ν
    rw [ocneanuWeight_eq_eval_wenzlPoly q z hq hd hQ, ν.2, mul_div_assoc]
  rw [Finset.sum_congr rfl fun ν _ => e ν, ← Finset.sum_div, hs,
    div_self (pow_ne_zero n h1a)]

/-- **Branching coherence at every Markov parameter**: `Σ_{s addable} w_{ν+s}(q,z) = w_ν(q,z)`.
This is the condition that the weighted characters restrict correctly along the whole tower
`H_1 ⊂ H_2 ⊂ ⋯` (harmonicity on the Young graph). -/
theorem sum_addable_ocneanuWeight (q z : F) (hq : q ≠ 0) (hd : q ^ 2 - 1 - q * z ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2) ^ k ≠ 1) (ν : YoungDiagram) :
    (∑ s : {s : ℕ × ℕ // IsAddableCell ν s}, ocneanuWeight q z (addCellOrSelf ν s.1))
      = ocneanuWeight q z ν := by
  have hQ : q ^ 2 ≠ 1 := ne_one_of_gen hgen
  have h1a : 1 - ocneanuA q z ≠ 0 := by
    rw [one_sub_ocneanuA q z hd]
    exact div_ne_zero (sub_ne_zero.mpr hQ) hd
  have hs := sum_addable_eval_wenzlPoly (q ^ 2) (pow_ne_zero 2 hq) hgen ν (ocneanuA q z)
  have e : ∀ s : {s : ℕ × ℕ // IsAddableCell ν s},
      ocneanuWeight q z (addCellOrSelf ν s.1)
        = (wenzlPoly (q ^ 2) (addCellOrSelf ν s.1)).eval (ocneanuA q z)
            / (1 - ocneanuA q z) ^ (ν.cells.card + 1) := by
    intro s
    rw [ocneanuWeight_eq_eval_wenzlPoly q z hq hd hQ, addCellOrSelf_of s.2, card_addCell s.2]
  rw [Finset.sum_congr rfl fun s _ => e s, ← Finset.sum_div, hs,
    ocneanuWeight_eq_eval_wenzlPoly q z hq hd hQ, pow_succ]
  field_simp
  ring

/-- **The Markov corner at every `z`, abstractly.**  If at every level `r ≥ 1` the data `t, t'`
satisfy the level-`r` Markov identity, then the Ocneanu-weighted sums satisfy the Markov identity
with parameter `z`. -/
theorem sum_ocneanuWeight_mul (q z : F) (hq : q ≠ 0) (hd : q ^ 2 - 1 - q * z ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2) ^ k ≠ 1) {m : ℕ}
    (t : {ρ : YoungDiagram // ρ.cells.card = m + 2} → F)
    (t' : {ν : YoungDiagram // ν.cells.card = m + 1} → F)
    (hw : ∀ r : ℕ, r ≠ 0 →
      ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, wenzlWeight r (q ^ 2) L.1 * t L
        = (q ^ 2) ^ r / (q * levelBracket r (q ^ 2))
          * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1}, wenzlWeight r (q ^ 2) ν.1 * t' ν) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, ocneanuWeight q z L.1 * t L
      = z * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1}, ocneanuWeight q z ν.1 * t' ν := by
  have hQ : q ^ 2 ≠ 1 := ne_one_of_gen hgen
  have h1a : 1 - ocneanuA q z ≠ 0 := by
    rw [one_sub_ocneanuA q z hd]
    exact div_ne_zero (sub_ne_zero.mpr hQ) hd
  have hs := sum_eval_wenzlPoly_mul (q ^ 2) q (pow_ne_zero 2 hq) hq hgen t t' hw (ocneanuA q z)
  set a := ocneanuA q z with ha
  have e1 : ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, ocneanuWeight q z L.1 * t L
      = (∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, (wenzlPoly (q ^ 2) L.1).eval a * t L)
          / (1 - a) ^ (m + 2) := by
    rw [Finset.sum_div]
    refine Finset.sum_congr rfl fun L _ => ?_
    rw [ocneanuWeight_eq_eval_wenzlPoly q z hq hd hQ, L.2]
    ring
  have e2 : ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1}, ocneanuWeight q z ν.1 * t' ν
      = (∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1}, (wenzlPoly (q ^ 2) ν.1).eval a * t' ν)
          / (1 - a) ^ (m + 1) := by
    rw [Finset.sum_div]
    refine Finset.sum_congr rfl fun ν _ => ?_
    rw [ocneanuWeight_eq_eval_wenzlPoly q z hq hd hQ, ν.2]
    ring
  have hz := ocneanuA_markov q z hq hd hQ
  rw [← ha] at hz
  rw [e1, e2, hs]
  rw [← hz]
  field_simp
  ring

end Generic

namespace SeminormalRep

open QOU.SchurWeyl.TableauCells QOU.SchurWeyl.Seminormal QOU.SchurWeyl.HeckeInclusion

/-- **The Markov corner identity for the Ocneanu weight, at every Markov parameter `z`**
with `q² − 1 − q z ≠ 0`. -/
theorem markov_ocneanuWeight (q : ℝ) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (z : ℝ) (hd : q ^ 2 - 1 - q * z ≠ 0) {m : ℕ} (y : Hecke ℝ q q⁻¹ m) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
        ocneanuWeight q z L.1
          * ((seminormalRep q hq hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y))
              * genMat q (m + 1) (by omega) L.2.ge).trace
      = z * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          ocneanuWeight q z ν.1 * (seminormalRep q hq hq2 m ν.2 y).trace :=
  sum_ocneanuWeight_mul q z hq hd (realGen_of_sq_ne_one hq hq2)
    (fun L => ((seminormalRep q hq hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y))
      * genMat q (m + 1) (by omega) L.2.ge).trace)
    (fun ν => (seminormalRep q hq hq2 m ν.2 y).trace)
    (fun r hr => markov_wenzlWeight q hq hq2 (realGen_of_sq_ne_one hq hq2) hr y)

/-- **The Ocneanu Markov trace at Markov parameter `z`**: the seminormal trace weighted by
`ocneanuWeight q z`, a Markov trace on the whole tower, for every real `z ≠ q − q⁻¹`. -/
noncomputable def ocneanuMarkovTraceAt (q : ℝ) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (z : ℝ) (hd : q ^ 2 - 1 - q * z ≠ 0) :
    HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ z :=
  markovTraceOfWeight q hq0 hq2 (ocneanuWeight q z) z
    (fun n => sum_dim_ocneanuWeight_eq_one q z hq0 hd (realGen_of_sq_ne_one hq0 hq2) n)
    (fun ν => sum_addable_ocneanuWeight q z hq0 hd (realGen_of_sq_ne_one hq0 hq2) ν)
    (fun _ y => markov_ocneanuWeight q hq0 hq2 z hd y)

theorem ocneanuMarkovTraceAt_tr (q : ℝ) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (z : ℝ) (hd : q ^ 2 - 1 - q * z ≠ 0) :
    (ocneanuMarkovTraceAt q hq0 hq2 z hd).tr = wtraceW q hq0 hq2 (ocneanuWeight q z) := rfl

/-- **Every Markov trace with parameter `z` is the Ocneanu-weighted seminormal trace**, for every
real `z ≠ q − q⁻¹`: the closed-form weight `ocneanuWeight q z` is *the* Markov weight. -/
theorem eq_ocneanu_of_markov (q : ℝ) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (z : ℝ) (hd : q ^ 2 - 1 - q * z ≠ 0) (T : HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ z)
    (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    T.tr n x = wtraceW q hq0 hq2 (ocneanuWeight q z) n x :=
  HeckeCoset.markovTrace_unique T (ocneanuMarkovTraceAt q hq0 hq2 z hd) n x

end SeminormalRep

/-! ## The imaginary-rank parametrisation of the window

`z(y) = (q − q⁻¹)·y²/(y² + 1)`.  Its interpolation point is `a(z(y)) = −y²`, and the Ocneanu weight
becomes the product form of the probe `full_tower_trace_coherence_probe.py`:

```
w_μ(y) = ∏_{x ∈ μ} (y q^{c(x)} + q^{−c(x)}/y) / ((y + 1/y)^{|μ|} ∏_{x ∈ μ} [h(x)]_q).
```
-/

section ImaginaryRank

variable {F : Type*} [Field F]

/-- The Markov parameter of the imaginary-rank point `y`: `z(y) = (q − q⁻¹)·y²/(y² + 1)`. -/
noncomputable def zOfY (q y : F) : F := (q - q⁻¹) * y ^ 2 / (y ^ 2 + 1)

theorem sub_zOfY (q y : F) (hq : q ≠ 0) (hy2 : y ^ 2 + 1 ≠ 0) :
    q ^ 2 - 1 - q * zOfY q y = (q ^ 2 - 1) / (y ^ 2 + 1) := by
  unfold zOfY
  field_simp
  ring

theorem ocneanuA_zOfY (q y : F) (hq : q ≠ 0) (hQ : q ^ 2 ≠ 1) (hy2 : y ^ 2 + 1 ≠ 0) :
    ocneanuA q (zOfY q y) = -y ^ 2 := by
  have h3 : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hQ
  rw [ocneanuA_eq, sub_zOfY q y hq hy2]
  unfold zOfY
  field_simp

/-- `W_μ(a) = M_μ(Q) · ∏_x (1 − Q^{c(x)} a)`. -/
theorem eval_wenzlPoly_eq_molien_mul (Q a : F) (μ : YoungDiagram) :
    (wenzlPoly Q μ).eval a = molienWeight Q μ * ∏ x ∈ μ.cells, (1 - Q ^ content x * a) := by
  rw [eval_wenzlPoly, molienWeight, Finset.prod_mul_distrib, mul_assoc]

/-- One cell of the imaginary-rank product. -/
theorem imagRank_cell (q y : F) (hq : q ≠ 0) (hy : y ≠ 0) (hy2 : y ^ 2 + 1 ≠ 0) (c : ℤ) :
    (y * q ^ c + q ^ (-c) / y) / (y + 1 / y)
      = q ^ (-c) * (1 - (q ^ 2) ^ c * -y ^ 2) / (y ^ 2 + 1) := by
  have hu : q ^ c ≠ 0 := zpow_ne_zero c hq
  have e1 : q ^ (-c) = (q ^ c)⁻¹ := zpow_neg q c
  have e2 : (q ^ 2) ^ c = (q ^ c) ^ 2 := by
    rw [← zpow_natCast q 2, ← zpow_mul, mul_comm, zpow_mul, zpow_natCast]
  have hyy : y + 1 / y ≠ 0 := by
    intro h
    apply hy2
    have : y * (y + 1 / y) = 0 := by rw [h, mul_zero]
    rw [mul_add, mul_one_div_cancel hy] at this
    rw [sq]; exact this
  rw [e1, e2]
  field_simp
  ring

/-- **The imaginary-rank product form of the Ocneanu weight.** -/
theorem ocneanuWeight_zOfY (q y : F) (hq : q ≠ 0) (hQ : q ^ 2 ≠ 1) (hy : y ≠ 0)
    (hy2 : y ^ 2 + 1 ≠ 0) (μ : YoungDiagram) :
    ocneanuWeight q (zOfY q y) μ
      = (∏ x ∈ μ.cells, (y * q ^ content x + q ^ (-content x) / y))
          / ((y + 1 / y) ^ μ.cells.card * ∏ x ∈ μ.cells, qIntBal q (hook μ x)) := by
  have h3 : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hQ
  have hd : q ^ 2 - 1 - q * zOfY q y ≠ 0 := by
    rw [sub_zOfY q y hq hy2]; exact div_ne_zero h3 hy2
  rw [ocneanuWeight_eq_eval_wenzlPoly q (zOfY q y) hq hd hQ, ocneanuA_zOfY q y hq hQ hy2,
    eval_wenzlPoly_eq_molien_mul, molienWeight_eq_balanced q hq hQ]
  have key : (∏ x ∈ μ.cells, (y * q ^ content x + q ^ (-content x) / y))
        / (y + 1 / y) ^ μ.cells.card
      = q ^ (-molienContentSum μ) * (∏ x ∈ μ.cells, (1 - (q ^ 2) ^ content x * -y ^ 2))
          / (y ^ 2 + 1) ^ μ.cells.card := by
    rw [molienContentSum, ← Finset.sum_neg_distrib, ← prod_zpow_eq_zpow_sum' q hq,
      ← Finset.prod_const, ← Finset.prod_const, ← Finset.prod_div_distrib,
      ← Finset.prod_mul_distrib,
      ← Finset.prod_div_distrib]
    exact Finset.prod_congr rfl fun x _ => imagRank_cell q y hq hy hy2 (content x)
  rw [← div_div, key, show (1 : F) - -y ^ 2 = y ^ 2 + 1 by ring]
  ring

end ImaginaryRank

/-! ## Positivity on the closed window `0 ≤ z ≤ q − q⁻¹`

For `q > 1` and `0 ≤ q z ≤ q² − 1`, both summands of every numerator factor
`q^{2i}(q² − 1 − q z) + q^{2j+1} z` are non-negative and at least one is positive, and every
denominator factor `q^{2h} − 1` is positive (`h ≥ 1`).  So **every** weight is strictly positive —
the trace is faithful on every Wedderburn block of every `H_n(q)`. -/

section Window

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Every Ocneanu weight is strictly positive on the window** `0 ≤ z`, `q z ≤ q² − 1`, `q > 1`. -/
theorem ocneanuWeight_pos_of_window (q z : R) (hq : 1 < q) (hz0 : 0 ≤ z)
    (hzd : q * z ≤ q ^ 2 - 1) (μ : YoungDiagram) : 0 < ocneanuWeight q z μ := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  unfold ocneanuWeight
  apply div_pos
  · refine Finset.prod_pos fun x _ => ?_
    have hA : 0 ≤ q ^ 2 - 1 - q * z := by linarith
    have hpi : 0 < q ^ (2 * x.1) := pow_pos hq0 _
    have hpj : 0 < q ^ (2 * x.2 + 1) := pow_pos hq0 _
    rcases hz0.lt_or_eq with hz | hz
    · have := mul_pos hpj hz
      have := mul_nonneg hpi.le hA
      linarith
    · subst hz
      have hQ : 1 < q ^ 2 := one_lt_pow₀ hq (by norm_num)
      have := mul_pos hpi (show 0 < q ^ 2 - 1 - q * 0 by linarith)
      linarith
  · refine Finset.prod_pos fun x hx => ?_
    rw [hookLength_eq_hook hx]
    have h1 := one_le_hook hx
    have : 1 < q ^ (2 * hook μ x) := one_lt_pow₀ hq (by omega)
    linarith

/-- The window in the `z` variable: `0 ≤ z ≤ q − q⁻¹`. -/
theorem ocneanuWeight_pos_of_le (q z : R) (hq : 1 < q) (hz0 : 0 ≤ z) (hzd : z ≤ q - q⁻¹)
    (μ : YoungDiagram) : 0 < ocneanuWeight q z μ := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  refine ocneanuWeight_pos_of_window q z hq hz0 ?_ μ
  have := mul_le_mul_of_nonneg_left hzd hq0.le
  rw [mul_sub, mul_inv_cancel₀ hq0.ne', ← sq] at this
  exact this

/-- `z(y)` lies strictly inside the window for `y ≠ 0`, `q > 1`. -/
theorem zOfY_mem_window (q y : R) (hq : 1 < q) (hy : y ≠ 0) :
    0 < zOfY q y ∧ zOfY q y < q - q⁻¹ := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hd : 0 < q - q⁻¹ := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    linarith
  have hy2 : 0 < y ^ 2 := by positivity
  have hy21 : 0 < y ^ 2 + 1 := by linarith
  unfold zOfY
  constructor
  · positivity
  · rw [div_lt_iff₀ hy21]
    nlinarith

/-- **The imaginary-rank weights are strictly positive**, for every `μ`, every `y ≠ 0`, `q > 1`. -/
theorem imagRank_weight_pos (q y : R) (hq : 1 < q) (hy : y ≠ 0) (μ : YoungDiagram) :
    0 < (∏ x ∈ μ.cells, (y * q ^ content x + q ^ (-content x) / y))
          / ((y + 1 / y) ^ μ.cells.card * ∏ x ∈ μ.cells, qIntBal q (hook μ x)) := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hQ : q ^ 2 ≠ 1 := ne_of_gt (one_lt_pow₀ hq (by norm_num))
  have hy2 : y ^ 2 + 1 ≠ 0 := by positivity
  rw [← ocneanuWeight_zOfY q y hq0.ne' hQ hy hy2 μ]
  obtain ⟨h0, h1⟩ := zOfY_mem_window q y hq hy
  exact ocneanuWeight_pos_of_le q (zOfY q y) hq h0.le h1.le μ

end Window

/-- **Every point of the open window is an imaginary-rank point** (over `ℝ`):
for `0 < z < q − q⁻¹`, `y = √(z/(q − q⁻¹ − z))` has `z(y) = z`. -/
theorem exists_zOfY_eq (q z : ℝ) (hz0 : 0 < z) (hzd : z < q - q⁻¹) :
    ∃ y : ℝ, 0 < y ∧ zOfY q y = z := by
  set d := q - q⁻¹ with hd_def
  have hdz : 0 < d - z := by linarith
  refine ⟨Real.sqrt (z / (d - z)), Real.sqrt_pos.mpr (div_pos hz0 hdz), ?_⟩
  unfold zOfY
  rw [← hd_def, Real.sq_sqrt (div_pos hz0 hdz).le]
  field_simp
  ring

/-! ## The quantum Plancherel weight is NOT branching-coherent

`d_q(λ) = [n]_q! / ∏_x [h(x)]_q` (balanced `[m]_q`), `f^λ = n!/∏_x h(x)`, and the quantum
Plancherel weight `w_λ = d_q(λ)² / (f^λ · Σ_{μ ⊢ n} d_q(μ)²)` (measure `f^λ w_λ = d_q²/Σ d_q²`).
At `λ = (3)` the coherence condition `w_{(3)} = w_{(4)} + w_{(3,1)}` fails for every `q > 0`,
`q ≠ 1`.  Hook data (each list = the hook lengths of the shape, read row by row):

| shape | hooks | `f` | `d_q` |
|---|---|---|---|
| `(3)` | `3,2,1` | 1 | 1 |
| `(2,1)` | `3,1,1` | 2 | `[2]` |
| `(1,1,1)` | `3,2,1` | 1 | 1 |
| `(4)` | `4,3,2,1` | 1 | 1 |
| `(3,1)` | `4,2,1,1` | 3 | `[3]` |
| `(2,2)` | `3,2,2,1` | 2 | `[4]/[2]` |
| `(2,1,1)` | `4,1,2,1` | 3 | `[3]` |
| `(1,1,1,1)` | `4,3,2,1` | 1 | 1 |

With `s = q + q⁻¹`, `u = s²`: `[2] = s`, `[3] = u − 1`, `[4]/[2] = u − 2`, and

```
w_{(3)} − w_{(4)} − w_{(3,1)} = −(u − 1)(u − 4)² / (3 (u + 2)(3u² − 8u + 8)),
```

which vanishes only at `u = 4` (`q = 1`, the classical Plancherel measure, which *is* coherent)
on the region `u ≥ 4`.  The table is entered by hand (it is the standard hook data of the eight
shapes); completeness of the partition lists and the hook computation are not machine-derived here.
-/

section QuantumPlancherel

variable {R : Type*} [Field R]

/-- Hook-formula `q`-dimension from a hook list: `[n]_q! / ∏_h [h]_q`
(`qFactBal` is `QOU.QInteger.qFactBal`). -/
noncomputable def hookQDim (q : R) (n : ℕ) (hs : List ℕ) : R :=
  qFactBal q n / (hs.map (qIntBal q)).prod

/-- Hook-formula count of standard tableaux: `n! / ∏_h h`. -/
def hookF (n : ℕ) (hs : List ℕ) : ℕ := n.factorial / hs.prod

/-- The quantum Plancherel weight of the shape with hook list `hs`, relative to the list `P` of hook
lists of all shapes of size `n`: `d_q² / (f · Σ_{μ ∈ P} d_q(μ)²)`. -/
noncomputable def qPlancherelWeight (q : R) (n : ℕ) (P : List (List ℕ)) (hs : List ℕ) : R :=
  hookQDim q n hs ^ 2 / ((hookF n hs : R) * (P.map (fun h => hookQDim q n h ^ 2)).sum)

/-- Hook lists of the three shapes of size 3. -/
def hooks3 : List (List ℕ) := [[3, 2, 1], [3, 1, 1], [3, 2, 1]]

/-- Hook lists of the five shapes of size 4. -/
def hooks4 : List (List ℕ) := [[4, 3, 2, 1], [4, 2, 1, 1], [3, 2, 2, 1], [4, 1, 2, 1], [4, 3, 2, 1]]

theorem ne_zero_of_sub_inv_ne_zero {q : R} (hd : q - q⁻¹ ≠ 0) : q ≠ 0 := by
  rintro rfl; simp at hd

theorem sq_sub_one_ne_zero_of_sub_inv {q : R} (hd : q - q⁻¹ ≠ 0) : q ^ 2 - 1 ≠ 0 := by
  have hq := ne_zero_of_sub_inv_ne_zero hd
  intro h
  apply hd
  have : q - q⁻¹ = (q ^ 2 - 1) / q := by field_simp
  rw [this, h, zero_div]

theorem qIntBal_three_eq_sq_sub_one (q : R) (hd : q - q⁻¹ ≠ 0) :
    qIntBal q 3 = (q + q⁻¹) ^ 2 - 1 := by
  have hq := ne_zero_of_sub_inv_ne_zero hd
  have hq2 := sq_sub_one_ne_zero_of_sub_inv hd
  rw [qIntBal_def, inv_pow]
  field_simp
  ring

theorem qIntBal_four_eq_mul (q : R) (hd : q - q⁻¹ ≠ 0) :
    qIntBal q 4 = (q + q⁻¹) * ((q + q⁻¹) ^ 2 - 2) := by
  have hq := ne_zero_of_sub_inv_ne_zero hd
  have hq2 := sq_sub_one_ne_zero_of_sub_inv hd
  rw [qIntBal_def, inv_pow]
  field_simp
  ring

/-- **The coherence defect of the quantum Plancherel weight at `λ = (3)`, in closed form**
(generic field; the hypotheses only make the quotients honest). -/
theorem qPlancherel_defect_eq (q : R) (hd : q - q⁻¹ ≠ 0)
    (hs : q + q⁻¹ ≠ 0) (h3 : (q + q⁻¹) ^ 2 - 1 ≠ 0) (h4 : (q + q⁻¹) ^ 2 - 2 ≠ 0)
    (hZ3 : (q + q⁻¹) ^ 2 + 2 ≠ 0)
    (hZ4 : 3 * ((q + q⁻¹) ^ 2) ^ 2 - 8 * (q + q⁻¹) ^ 2 + 8 ≠ 0) (h30 : (3 : R) ≠ 0) :
    qPlancherelWeight q 3 hooks3 [3, 2, 1]
        - (qPlancherelWeight q 4 hooks4 [4, 3, 2, 1] + qPlancherelWeight q 4 hooks4 [4, 2, 1, 1])
      = -(((q + q⁻¹) ^ 2 - 1) * ((q + q⁻¹) ^ 2 - 4) ^ 2)
          / (3 * ((q + q⁻¹) ^ 2 + 2) * (3 * ((q + q⁻¹) ^ 2) ^ 2 - 8 * (q + q⁻¹) ^ 2 + 8)) := by
  have hq := ne_zero_of_sub_inv_ne_zero hd
  have hF1 : hookF 3 [3, 2, 1] = 1 := by decide
  have hF2 : hookF 4 [4, 3, 2, 1] = 1 := by decide
  have hF3 : hookF 4 [4, 2, 1, 1] = 3 := by decide
  have q3 : qFactBal q 3 = (q + q⁻¹) * ((q + q⁻¹) ^ 2 - 1) := by
    simp only [qFactBal, Finset.prod_range_succ, Finset.prod_range_zero, qIntBal_one_of_ne_sing hd,
      qIntBal_two q hd, qIntBal_three_eq_sq_sub_one q hd]
    ring
  have q4 : qFactBal q 4 = (q + q⁻¹) * ((q + q⁻¹) ^ 2 - 1) * ((q + q⁻¹) * ((q + q⁻¹) ^ 2 - 2)) := by
    simp only [qFactBal, Finset.prod_range_succ, Finset.prod_range_zero, qIntBal_one_of_ne_sing hd,
      qIntBal_two q hd, qIntBal_three_eq_sq_sub_one q hd, qIntBal_four_eq_mul q hd]
    ring
  set s := q + q⁻¹ with hs_def
  have d321 : hookQDim q 3 [3, 2, 1] = 1 := by
    simp only [hookQDim, q3, List.map_cons, List.map_nil, List.prod_cons, List.prod_nil,
      qIntBal_one_of_ne_sing hd, qIntBal_two q hd, qIntBal_three_eq_sq_sub_one q hd, ← hs_def]
    field_simp
  have d311 : hookQDim q 3 [3, 1, 1] = s := by
    simp only [hookQDim, q3, List.map_cons, List.map_nil, List.prod_cons, List.prod_nil,
      qIntBal_one_of_ne_sing hd, qIntBal_three_eq_sq_sub_one q hd, ← hs_def]
    field_simp
  have d4321 : hookQDim q 4 [4, 3, 2, 1] = 1 := by
    simp only [hookQDim, q4, List.map_cons, List.map_nil, List.prod_cons, List.prod_nil,
      qIntBal_one_of_ne_sing hd, qIntBal_two q hd, qIntBal_three_eq_sq_sub_one q hd,
      qIntBal_four_eq_mul q hd, ← hs_def]
    field_simp
  have d4211 : hookQDim q 4 [4, 2, 1, 1] = s ^ 2 - 1 := by
    simp only [hookQDim, q4, List.map_cons, List.map_nil, List.prod_cons, List.prod_nil,
      qIntBal_one_of_ne_sing hd, qIntBal_two q hd, qIntBal_four_eq_mul q hd, ← hs_def]
    field_simp
  have d3221 : hookQDim q 4 [3, 2, 2, 1] = s ^ 2 - 2 := by
    simp only [hookQDim, q4, List.map_cons, List.map_nil, List.prod_cons, List.prod_nil,
      qIntBal_one_of_ne_sing hd, qIntBal_two q hd, qIntBal_three_eq_sq_sub_one q hd, ← hs_def]
    field_simp
  have d4121 : hookQDim q 4 [4, 1, 2, 1] = s ^ 2 - 1 := by
    simp only [hookQDim, q4, List.map_cons, List.map_nil, List.prod_cons, List.prod_nil,
      qIntBal_one_of_ne_sing hd, qIntBal_two q hd, qIntBal_four_eq_mul q hd, ← hs_def]
    field_simp
  have Z3 : (hooks3.map (fun h => hookQDim q 3 h ^ 2)).sum = s ^ 2 + 2 := by
    simp only [hooks3, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, d321, d311]
    ring
  have Z4 : (hooks4.map (fun h => hookQDim q 4 h ^ 2)).sum
      = 3 * (s ^ 2) ^ 2 - 8 * s ^ 2 + 8 := by
    simp only [hooks4, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, d4321, d4211,
      d3221, d4121]
    ring
  simp only [qPlancherelWeight, Z3, Z4, d321, d4321, d4211, hF1, hF2, hF3, Nat.cast_one,
    Nat.cast_ofNat]
  generalize hZ : 3 * (s ^ 2) ^ 2 - 8 * s ^ 2 + 8 = Z at hZ4 ⊢
  field_simp
  rw [← hZ]
  ring

end QuantumPlancherel

/-- **The quantum Plancherel weight violates branching coherence at `λ = (3)`**, for every `q > 0`,
`q ≠ 1`, in any ordered field: `w_{(3)} < w_{(4)} + w_{(3,1)}`.  So the weights
`d_q(λ)²/(f^λ Σ d_q²)` do not define a trace on the tower `H_3 ⊂ H_4`. -/
theorem qPlancherel_not_coherent {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (q : R) (hq : 0 < q) (hq1 : q ≠ 1) :
    qPlancherelWeight q 3 hooks3 [3, 2, 1]
      < qPlancherelWeight q 4 hooks4 [4, 3, 2, 1] + qPlancherelWeight q 4 hooks4 [4, 2, 1, 1] := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq.ne'
  have hqi0 : 0 < q⁻¹ := inv_pos.mpr hq
  have hsq : 0 < (q - 1) ^ 2 := by
    have : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
    positivity
  have hs2 : 2 < q + q⁻¹ := by
    have h1 : q * (q + q⁻¹) = q ^ 2 + 1 := by rw [mul_add, hqi]; ring
    nlinarith
  have hd : q - q⁻¹ ≠ 0 := by
    intro h
    have h1 : q * (q - q⁻¹) = q ^ 2 - 1 := by rw [mul_sub, hqi]; ring
    rw [h, mul_zero] at h1
    have : (q - 1) * (q + 1) = 0 := by linear_combination -h1
    rcases mul_eq_zero.mp this with h2 | h2
    · exact hq1 (by linarith)
    · linarith
  set s := q + q⁻¹ with hs_def
  have hu : 4 < s ^ 2 := by nlinarith
  have hZ4 : 0 < 3 * (s ^ 2) ^ 2 - 8 * s ^ 2 + 8 := by nlinarith
  have hdef := qPlancherel_defect_eq q hd (by positivity) (by nlinarith) (by nlinarith)
    (by positivity) hZ4.ne' (by norm_num)
  rw [← hs_def] at hdef
  have hneg : -((s ^ 2 - 1) * (s ^ 2 - 4) ^ 2)
      / (3 * (s ^ 2 + 2) * (3 * (s ^ 2) ^ 2 - 8 * s ^ 2 + 8)) < 0 := by
    apply div_neg_of_neg_of_pos
    · have : 0 < (s ^ 2 - 4) ^ 2 := by
        have : s ^ 2 - 4 ≠ 0 := by linarith
        positivity
      have : 0 < s ^ 2 - 1 := by linarith
      nlinarith
    · positivity
  linarith

end QOU.SchurWeyl
