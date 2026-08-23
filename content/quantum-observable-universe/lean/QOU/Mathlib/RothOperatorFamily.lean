/-
  **§13's operator family, constructed** — the input `index_le_of_det_bound` needs and the
  arc did not have.

  Bean `qou-4lbh`.

  ⚠ Not Mathlib-only: it imports `QOU/Mathlib/RothInductionStep.lean` and through it the rest
  of the arc.

  ═══ WHAT THE SOURCE ASKS FOR ═══

  Mahler §13 expands the generalized Wronskian as `det (A_{μν} A)` where

      A_{μν} = Δ_{j_{μ1}, …, j_{μ,m−1}, ν−1},
      ∑_{h < m} j_{μh} ≤ μ − 1,        j_{μm} = ν − 1.

  Two features of that shape matter and neither is decoration:

  * the **column** index fixes the order in the distinguished variable exactly — `ν − 1`
    copies of `x_m` — which is where the growing cost `ν/r_m` comes from;
  * the **row** index constrains only the *other* variables, and only through a bound.  So
    the row's contribution to the cost is bounded **uniformly in the row**, which is exactly
    the hypothesis `sum_max_le_index_det` needs to be allowed to choose the minimising
    permutation.  A family whose cost varied with the row would not be usable there.

  ═══ WHAT IS HERE ═══

  `rothOpFamily z L μ ν = L μ ++ List.replicate ν z` — the row part, then `ν` copies of the
  distinguished variable — and `cost_rothOpFamily_le`, which is `index_le_of_det_bound`'s
  hypothesis `hc` discharged.

  Taking the row part as a *list* rather than as a multi-index is deliberate: the multi-index
  form needs `exists_multiIndexOf_eq`, whose witness is a `Classical.choose` and therefore
  opaque to any concrete instance.  `exists_rothOpFamily_of_idxWeight_le` recovers the
  multi-index form as a corollary, so nothing is lost and the family stays computable.

  ═══ ⚠ WHAT THIS DOES *NOT* CLOSE ═══

  This is the **cost** half of the construction.  It says: a family of the required shape
  exists, and its cost bound holds.  It does **not** say that the determinant of the
  resulting matrix is non-zero — and `index_le_of_det_bound`'s hypothesis
  `index d α (det …) ≤ ↑S` is *unsatisfiable* when the determinant vanishes, since the index
  of `0` is `⊤`.  Supplying that is `BoundedOrderWronskian`'s business and is not done here.

  So: after this module the recursion still has an unmet input, but it is one input rather
  than two, and it is a non-vanishing statement rather than a construction.
-/
import QOU.Mathlib.RothInductionStep

namespace MvPolynomial

variable {σ : Type*} {R : Type*} [CommRing R]

/-! ### Cost is weight

The bridge that makes the rest of the module short: the "cost" appearing in
`index_le_index_pderivList_add` and in `index_le_of_det_bound`'s `hc` is nothing but the
`idxWeight` of the operator's multi-index.  Once that is said, bounding a cost is bounding a
weight, and `idxWeight`'s additivity does the work. -/

/-- **The cost of an operator list is the weight of its multi-index.** -/
theorem sum_map_inv_eq_idxWeight (d : σ → ℕ) (l : List σ) :
    (l.map (fun k => (1 : ℚ) / (d k : ℚ))).sum = idxWeight d (multiIndexOf l) := by
  induction l with
  | nil => simp
  | cons a t ih =>
      rw [List.map_cons, List.sum_cons, ih, multiIndexOf_cons, idxWeight_add,
        idxWeight_single]
      norm_num

/-- A multi-index of total order at most `N`, on variables of degree at least `D`, has weight
at most `N/D`.

This is what turns Mahler's `∑_{h<m} j_{μh} ≤ μ − 1` into a cost bound: the row constraint is
on the *total order*, and the degree floor converts it to a weight. -/
theorem idxWeight_le_of_sum_le {D N : ℕ} (hD : D ≠ 0) (d : σ → ℕ) (hd : ∀ k, D ≤ d k)
    (e : σ →₀ ℕ) (he : (e.sum fun _ n => n) ≤ N) :
    idxWeight d e ≤ (N : ℚ) / (D : ℚ) := by
  have hDQ : (0 : ℚ) < (D : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD
  have hterm : ∀ k ∈ e.support, ((e k : ℚ)) / (d k : ℚ) ≤ ((e k : ℚ)) / (D : ℚ) := by
    intro k _
    have hinv : (1 : ℚ) / (d k : ℚ) ≤ 1 / (D : ℚ) :=
      one_div_le_one_div_of_le hDQ (by exact_mod_cast hd k)
    calc ((e k : ℚ)) / (d k : ℚ) = (e k : ℚ) * (1 / (d k : ℚ)) := by ring
      _ ≤ (e k : ℚ) * (1 / (D : ℚ)) := mul_le_mul_of_nonneg_left hinv (Nat.cast_nonneg _)
      _ = ((e k : ℚ)) / (D : ℚ) := by ring
  have hsupp : (∑ k ∈ e.support, (e k : ℚ)) = (((e.sum fun _ n => n : ℕ)) : ℚ) := by
    rw [Finsupp.sum]
    push_cast
    rfl
  calc idxWeight d e = ∑ k ∈ e.support, ((e k : ℚ)) / (d k : ℚ) := rfl
    _ ≤ ∑ k ∈ e.support, ((e k : ℚ)) / (D : ℚ) := Finset.sum_le_sum hterm
    _ = (∑ k ∈ e.support, (e k : ℚ)) / (D : ℚ) := by
        simp only [div_eq_mul_inv, ← Finset.sum_mul]
    _ = (((e.sum fun _ n => n : ℕ)) : ℚ) / (D : ℚ) := by rw [hsupp]
    _ ≤ (N : ℚ) / (D : ℚ) :=
        div_le_div_of_nonneg_right (by exact_mod_cast he) hDQ.le

/-! ### The family -/

/-- **§13's operator family.**  Row `μ` contributes the fixed list `L μ`; column `ν`
contributes `ν` copies of the distinguished variable `z`. -/
def rothOpFamily {n : ℕ} (z : σ) (L : Fin n → List σ) : Fin n → Fin n → List σ :=
  fun μ ν => L μ ++ List.replicate (ν : ℕ) z

/-- The cost of `ν` copies of one variable. -/
theorem sum_map_inv_replicate (d : σ → ℕ) (z : σ) (ν : ℕ) :
    (((List.replicate ν z).map (fun k => (1 : ℚ) / (d k : ℚ)))).sum = (ν : ℚ) / (d z : ℚ) := by
  rw [List.map_replicate, List.sum_replicate, nsmul_eq_mul]
  ring

/-- The cost splits: row part plus column part. -/
theorem cost_rothOpFamily {n : ℕ} (d : σ → ℕ) (z : σ) (L : Fin n → List σ) (μ ν : Fin n) :
    ((rothOpFamily z L μ ν).map (fun k => (1 : ℚ) / (d k : ℚ))).sum
      = ((L μ).map (fun k => (1 : ℚ) / (d k : ℚ))).sum + (ν : ℚ) / (d z : ℚ) := by
  rw [rothOpFamily, List.map_append, List.sum_append, sum_map_inv_replicate]

/-- **`hc` discharged.**  A uniform bound `t` on the rows gives the per-column cost bound
`t + ν/(d z)` that `index_le_of_det_bound` asks for.

Note where the uniformity lives: `ht` quantifies over rows with a single `t`.  That is not an
artefact of the statement — `sum_max_le_index_det` picks the permutation minimising the
diagonal sum, and may only do so because the bound does not depend on which row it lands in. -/
theorem cost_rothOpFamily_le {n : ℕ} (d : σ → ℕ) (z : σ) (L : Fin n → List σ) (t : ℚ)
    (ht : ∀ μ, ((L μ).map (fun k => (1 : ℚ) / (d k : ℚ))).sum ≤ t) (μ ν : Fin n) :
    ((rothOpFamily z L μ ν).map (fun k => (1 : ℚ) / (d k : ℚ))).sum
      ≤ t + (ν : ℚ) / (d z : ℚ) := by
  rw [cost_rothOpFamily]
  exact add_le_add_right (ht μ) _

/-- **The multi-index form**, recovered as a corollary.  Given row multi-indices of bounded
weight, a family of the required shape exists.

Stated as an existence because `exists_multiIndexOf_eq` produces its list by choice; the
`rothOpFamily` above stays free of that so concrete instances remain computable. -/
theorem exists_rothOpFamily_of_idxWeight_le {n : ℕ} (d : σ → ℕ) (z : σ)
    (e : Fin n → (σ →₀ ℕ)) (t : ℚ) (he : ∀ μ, idxWeight d (e μ) ≤ t) :
    ∃ L : Fin n → List σ, (∀ μ, multiIndexOf (L μ) = e μ) ∧
      ∀ μ ν : Fin n, ((rothOpFamily z L μ ν).map (fun k => (1 : ℚ) / (d k : ℚ))).sum
        ≤ t + (ν : ℚ) / (d z : ℚ) := by
  choose L hL using fun μ => exists_multiIndexOf_eq (e μ)
  refine ⟨L, hL, cost_rothOpFamily_le d z L t (fun μ => ?_)⟩
  rw [sum_map_inv_eq_idxWeight, hL μ]
  exact he μ

/-! ### §13's conclusion for this family -/

/-- **§13, with the operator family supplied.**

Every hypothesis is now about the data (`d`, `z`, the row lists, `S`, `q`) rather than about
an abstract `D` and an abstract cost bound — except `hS`, which is discussed below.

`t` is `(N : ℚ)/D`: the rows have total order at most `N` and every variable has degree at
least `D`, which is Mahler's `∑_{h<m} j_{μh} ≤ μ−1` converted by `idxWeight_le_of_sum_le`.

⚠ `hS` still asserts that the determinant's index is at most `S`, and that is **unsatisfiable
when the determinant is zero** (`index d α 0 = ⊤`).  Nothing here proves the determinant is
non-zero; that is the bounded-order criterion's job and it is the arc's remaining input. -/
theorem index_le_of_rothOpFamily [DecidableEq σ] {n : ℕ} {D N : ℕ} (hD : D ≠ 0)
    (d : σ → ℕ) (hd : ∀ k, D ≤ d k) (α : σ → R) (z : σ)
    (e : Fin n → (σ →₀ ℕ)) (L : Fin n → List σ) (hL : ∀ μ, multiIndexOf (L μ) = e μ)
    (he : ∀ μ, ((e μ).sum fun _ k => k) ≤ N)
    (P : MvPolynomial σ R) (θ S q : ℚ)
    (hn : 0 < n) (hθt : (N : ℚ) / (D : ℚ) ≤ θ) (hq0 : 0 ≤ q)
    (hq : S ≤ q ^ 2 * (d z : ℚ)) (hSr : S * (d z : ℚ) ≤ (n : ℚ))
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index d α P)
    (hS : index d α (Matrix.of fun μ ν => pderivList (rothOpFamily z L μ ν) P).det
      ≤ ((S : ℚ) : WithTop ℚ)) :
    θ ≤ (N : ℚ) / (D : ℚ) + 2 * q := by
  have hDQ : (0 : ℚ) < (D : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD
  have hzQ : (0 : ℚ) < (d z : ℚ) := lt_of_lt_of_le hDQ (by exact_mod_cast hd z)
  refine index_le_of_det_bound d α (rothOpFamily z L) P θ ((N : ℚ) / (D : ℚ)) (d z : ℚ) S q
    hn hzQ hθt hq0 hq hSr hθ ?_ hS
  refine cost_rothOpFamily_le d z L _ (fun μ => ?_)
  rw [sum_map_inv_eq_idxWeight, hL μ]
  exact idxWeight_le_of_sum_le hD d hd (e μ) (he μ)

/-- **Satisfiability.**  One variable, unit degree, the origin, `P = X₀`, `n = 1`, empty row
list: `N = 0`, `D = 1`, `S = 1`, `q = 1`, and the conclusion reads `1 ≤ 0 + 2`.

⚠ As with the other witnesses in this arc, this certifies that the hypotheses are **jointly
satisfiable** and nothing more.  With `n = 1` there is one column, so neither the truncation
nor the growth of the column cost is exercised. -/
theorem index_le_of_rothOpFamily_witness :
    (1 : ℚ) ≤ ((0 : ℕ) : ℚ) / ((1 : ℕ) : ℚ) + 2 * 1 := by
  have hdet : (Matrix.of fun μ ν : Fin 1 =>
      pderivList (rothOpFamily (0 : Fin 1) (fun _ => ([] : List (Fin 1))) μ ν)
        (X 0 : MvPolynomial (Fin 1) ℚ)).det = X 0 := by
    rw [Matrix.det_fin_one]
    simp [rothOpFamily]
  refine index_le_of_rothOpFamily (σ := Fin 1) (R := ℚ) (n := 1) (D := 1) (N := 0)
    one_ne_zero (fun _ => 1) (fun _ => le_rfl) (fun _ => (0 : ℚ)) 0
    (fun _ => 0) (fun _ => []) (fun _ => rfl) (fun _ => by simp)
    (X 0) 1 1 1
    Nat.one_pos (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    (by rw [index_X]) ?_
  rw [hdet, index_X]

/-- **A non-degenerate instance.**  `σ = Fin 1`, unit degree, the origin, `P = X₀²`, and a
genuine `2 × 2` matrix with **distinct rows** and a **non-vanishing determinant**:

    row lists  L = ![[], [x₀]]        (total orders 0 and 1, so N = 1)
    matrix     ⎡ P    ∂P  ⎤  =  ⎡ X²    2X ⎤        det = 2X² − 4X² = −2X²
               ⎣ ∂P   ∂²P ⎦     ⎣ 2X    2  ⎦

so `S = 2`, and with `q = 3/2` (any rational with `q² ≥ 2`) the conclusion reads `2 ≤ 1 + 3`.

Why this one and not another `1 × 1`: here the **column cost genuinely grows** — column `0`
costs `0` in row `0` and column `1` costs `1` more — and the two rows are different, so the
determinant is not forced to zero by repetition.  That is the configuration `index_det_ge`'s
permutation step and `hc`'s `t + ν/rr` shape exist for.

⚠ Still not exercised: the truncation.  `θ − t = 1` and `rr = 1`, so the cut-off `(θ−t)·rr`
is `1` and lands inside a `2`-column matrix without clipping either column.  `max 0` never
fires here; `RothArith.sum_max_truncation_active` is the guard that makes it fire. -/
theorem index_le_of_rothOpFamily_two_witness :
    (2 : ℚ) ≤ ((1 : ℕ) : ℚ) / ((1 : ℕ) : ℚ) + 2 * (3 / 2) := by
  have hpd2 : pderiv (0 : Fin 1) (2 : MvPolynomial (Fin 1) ℚ) = 0 := by
    rw [show (2 : MvPolynomial (Fin 1) ℚ) = C 2 from (map_ofNat C 2).symm, pderiv_C]
  have hdet : (Matrix.of fun μ ν : Fin 2 =>
      pderivList (rothOpFamily (0 : Fin 1) ![[], [(0 : Fin 1)]] μ ν)
        (X 0 ^ 2 : MvPolynomial (Fin 1) ℚ)).det = -(2 * X 0 ^ 2) := by
    rw [Matrix.det_fin_two]
    simp [rothOpFamily, hpd2]
    ring
  have hidx : index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ))
      (-(2 * X 0 ^ 2) : MvPolynomial (Fin 1) ℚ) = (2 : ℚ) := by
    rw [show (-(2 * X 0 ^ 2) : MvPolynomial (Fin 1) ℚ) = C (-2 : ℚ) * X 0 ^ 2 by
          rw [map_neg, map_ofNat]; ring,
      index_C_mul _ _ (by norm_num : (-2 : ℚ) ≠ 0), index_X_sq]
  refine index_le_of_rothOpFamily (σ := Fin 1) (R := ℚ) (n := 2) (D := 1) (N := 1)
    one_ne_zero (fun _ => 1) (fun _ => le_rfl) (fun _ => (0 : ℚ)) 0
    (fun μ => multiIndexOf (![[], [(0 : Fin 1)]] μ)) ![[], [(0 : Fin 1)]]
    (fun _ => rfl) (fun μ => ?_)
    (X 0 ^ 2) 2 2 (3 / 2)
    (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    (by rw [index_X_sq]) ?_
  · fin_cases μ <;> simp [multiIndexOf, Finsupp.sum_single_index]
  · rw [hdet, hidx]

/-! ### Next

The arc's remaining input is now a **single** statement, and it is not an inequality:

⚠ **the determinant of `Matrix.of fun μ ν => pderivList (rothOpFamily z L μ ν) P` is
non-zero** for a suitable choice of row lists.

`BoundedOrderWronskian` has the criterion in the form the arc needs it — linear independence
of a family is equivalent to some bounded-order generalized Wronskian being non-zero — but
that is stated for `mvGenWronskian D f`, a Wronskian of `m` *distinct* functions, whereas
§13's matrix is derivatives of a *single* `P`.  Relating the two is the next piece of work,
and it is where §7 of the source (which this arc has not read) belongs.

Until then `index_le_of_rothOpFamily` is conditional on `hS`, and `hS` cannot be discharged
for any `P` whose matrix has vanishing determinant. -/

end MvPolynomial
