/-
  **§13's remaining inputs, both supplied** — the operator family *constructed*, and the
  determinant's non-vanishing *proved*.  Together with `RothInductionStep` this closes
  Mahler §13: `exists_index_le_of_separated` assumes nothing about the family and nothing
  about the determinant.

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

  ═══ AND THE NON-VANISHING ═══

  `index_le_of_det_bound`'s hypothesis `index d α (det …) ≤ ↑S` is *unsatisfiable* when the
  determinant vanishes, since the index of `0` is `⊤`.  §6 of the source supplies that, and
  the argument needs nothing new: write `A` in a **minimum** separated representation, note
  both families are then independent, apply Lemma 1 to each, and use the multiplication law
  for determinants —

      det (D_{μν} A)  =  U*(x₁,…,x_{m−1}) · V**(x_m),

  a product of two non-zero polynomials over a domain.  `exists_sepW_ne_zero` is that
  composition; every piece of it was already in the arc.

  ⚠ Worth recording how long that sat as "the blocking item": it was blocked on **reading**,
  not on proving.  The pieces had been in place since `SeparatedRepresentation` landed.

  ═══ ⚠ WHAT THIS DOES *NOT* CLOSE ═══

  §13 is *derived*: `exists_index_le_of_separated` assumes nothing about the operator family,
  nothing about the determinant, and no arithmetic side condition beyond `q ≥ √(S/D₂)`.

  ⚠ An earlier version demanded `S·D₂ ≤ r` as well.  That was a **mistake** — see correction 9
  in `QOU/Mathlib/RothInductionStep.lean`.  The two branches of §13's conclusion are
  complementary by construction, so no such condition is needed; and in the recursion's regime
  it reads `Φ_m·r_m ≤ 1`, which is false.

  One constant question remains, and it is the sixth correction in its final form:

  * the row cost is `t = r/D₁` — representation length over degree floor.  The source *chooses*
    `t` with `0 < t ≤ 1`; this arc *derives* it.  The two pieces that would settle it:

      1. a bound `r ≤ d(split-off variable) + 1` on the **minimum representation length** —
         true (expand `P` in powers of the split-off variable) but **not proved here**:
         `exists_separated_representation_fin` splits on the `σ`-monomials, giving
         `r = #{σ-monomials}`, and `exists_indep_representation` only shortens without
         recording by how much;
      2. `RothGrowth`, which makes the split-off variable's degree the *smallest*, so that
         `D₁ ≥ ω · d(split-off)` and hence `t ≲ 1/ω`.

    Together those would give `t ≲ 1/ω` and so determine `ω(m, ε)` — which is the one entry
    `RothLemmaStatement`'s audit came back empty on.
-/
import QOU.Mathlib.RothInductionStep
import QOU.Mathlib.BoundedOrderWronskian
import QOU.Mathlib.SeparatedRepresentation

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

/-! ### The determinant is non-zero

⚠ This was the arc's last unmet input, and §6 of the source is where the answer is — not §7,
and not in any new inequality.  Every piece was already here; what was missing was the
composition.

Mahler's §6: write `A = ∑ₖ Pₖ(x₁,…,x_{m−1}) Σₖ(x_m)` in a **minimum** representation.  Both
families are then linearly independent, so Lemma 1 gives bounded-order Wronskians `U*` and
`V**` that do not vanish.  Differentiating the representation with the *combined* operators
`D_{μν} = D*_μ D**_ν` gives a matrix identity, and by the multiplication law for determinants

    det (D_{μν} A)  =  U*(x₁,…,x_{m−1}) · V**(x_m).

A product of two non-zero polynomials over a domain is non-zero.  That is the whole argument.

Mapped onto this arc: `exists_separated_representation_indep` is the minimum representation,
`exists_bounded_order_mvGenWronskian_ne_zero` is Lemma 1, `sepW_eq`
(`det_separated_wronskian`) is the multiplication law, and `MvPolynomial` over a field is a
domain. -/

/-- **The separated Wronskian of a non-zero polynomial can be made non-zero.**

⚠ Note the direction of the quantifier: it is not that *every* bounded-order family works —
most give a vanishing determinant — but that *some* does.  That is what
`index_le_of_det_bound`'s `hS` needs, since a vanishing determinant has index `⊤` and
satisfies no bound at all. -/
theorem exists_sepW_ne_zero {τ : Type*} {K : Type*} [Field K] [CharZero K]
    [DecidableEq σ] [DecidableEq τ]
    (P : MvPolynomial (σ ⊕ τ) K) (hP : P ≠ 0) :
    ∃ (r : ℕ) (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K)
      (Dx : Fin r → List σ) (Dy : Fin r → List τ),
      0 < r ∧ (∀ i, (Dx i).length ≤ (i : ℕ)) ∧ (∀ j, (Dy j).length ≤ (j : ℕ)) ∧
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k) ∧
      sepW Dx Dy φ ψ ≠ 0 := by
  classical
  obtain ⟨r, φ, ψ, hφ, hψ, hPeq⟩ := exists_separated_representation_indep P
  have hr : 0 < r := by
    rcases Nat.eq_zero_or_pos r with rfl | h
    · exact absurd (hPeq.trans (by simp)) hP
    · exact h
  obtain ⟨Dx, hDx, hWx⟩ := exists_bounded_order_mvGenWronskian_ne_zero hr φ hφ
  obtain ⟨Dy, hDy, hWy⟩ := exists_bounded_order_mvGenWronskian_ne_zero hr ψ hψ
  refine ⟨r, φ, ψ, Dx, Dy, hr, hDx, hDy, hPeq, ?_⟩
  rw [sepW_eq]
  refine mul_ne_zero ?_ ?_
  · intro h
    have h0 : (rename Sum.inl (mvGenWronskian Dx φ) : MvPolynomial (σ ⊕ τ) K)
        = rename Sum.inl 0 := by rw [h, map_zero]
    exact hWx (rename_injective _ Sum.inl_injective h0)
  · intro h
    have h0 : (rename Sum.inr (mvGenWronskian Dy ψ) : MvPolynomial (σ ⊕ τ) K)
        = rename Sum.inr 0 := by rw [h, map_zero]
    exact hWy (rename_injective _ Sum.inr_injective h0)

/-- A non-zero polynomial's index is bounded by *some* rational — the form `hS` wants.

This is the only place the non-vanishing is used, and it is used for exactly one thing:
`index d α 0 = ⊤` is below no `↑S`. -/
theorem exists_index_le_of_ne_zero (d : σ → ℕ) (α : σ → R) {P : MvPolynomial σ R}
    (hP : P ≠ 0) : ∃ S : ℚ, index d α P ≤ ((S : ℚ) : WithTop ℚ) := by
  have hne : index d α P ≠ ⊤ := fun hcon =>
    hP ((translate_eq_zero_iff α).mp ((index_eq_top_iff d α).mp hcon))
  obtain ⟨a, ha⟩ := WithTop.ne_top_iff_exists.mp hne
  exact ⟨a, le_of_eq ha.symm⟩

/-- The **column-graded** cost bound for a mixed operator family.

`cost_bound_of_bounded_order` gives the *uniform* bound `r/D₁ + r/D₂`; this keeps the column
index, which is the whole difference between the linear conclusion the sixth correction
rejected and §13's square root. -/
theorem cost_sepW_le {τ : Type*} {r D₁ D₂ : ℕ} (hD₁ : D₁ ≠ 0) (hD₂ : D₂ ≠ 0)
    (d₁ : σ → ℕ) (d₂ : τ → ℕ) (hd₁ : ∀ k, D₁ ≤ d₁ k) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (hDx : ∀ i, (Dx i).length ≤ (i : ℕ)) (hDy : ∀ j, (Dy j).length ≤ (j : ℕ)) (i j : Fin r) :
    (((Dx i).map Sum.inl ++ (Dy j).map Sum.inr).map
        (fun k => (1 : ℚ) / ((Sum.elim d₁ d₂ k : ℕ) : ℚ))).sum
      ≤ (r : ℚ) / (D₁ : ℚ) + (j : ℚ) / (D₂ : ℚ) := by
  have hD₁Q : (0 : ℚ) < (D₁ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₁
  have hD₂Q : (0 : ℚ) < (D₂ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₂
  rw [sum_map_inv_append_sumElim]
  refine add_le_add (le_trans (sum_map_inv_le_length_div hD₁ d₁ hd₁ _) ?_)
    (le_trans (sum_map_inv_le_length_div hD₂ d₂ hd₂ _) ?_)
  · refine div_le_div_of_nonneg_right ?_ hD₁Q.le
    exact_mod_cast le_trans (hDx i) (le_of_lt i.isLt)
  · exact div_le_div_of_nonneg_right (by exact_mod_cast hDy j) hD₂Q.le

/-- **§13 for an arbitrary non-zero polynomial in two variable groups** — every input
supplied, and no side condition beyond `q ≥ √(S/D₂)`.

The existence produces the representation length `r` and a bound `S` on the determinant's
index; the conclusion then holds for any `θ` and `q` meeting two conditions:

* `r/D₁ ≤ θ` — the row cost `t` is below the index being bounded, so there is something to
  bound.  (`index_le_two_mul_max_of_det_bound` needs `t ≤ θ`.)
* `S ≤ q²·D₂` — `q` is a rational stand-in for `√(S/D₂)`, keeping everything in `ℚ`.

⚠ An earlier version of this also demanded `S·D₂ ≤ r`.  That condition is **unnecessary** —
§13's two branches are complementary, so the `max` form needs nothing — and it is **false** in
the recursion's regime, where it reads `Φ_m·r_m ≤ 1`.  See correction 9 in
`QOU/Mathlib/RothInductionStep.lean`.

⚠ What this is *not*: it is not Roth's lemma, and it does not choose `ω(m, ε)`.  It is §13's
inequality with all of §13's inputs discharged. -/
theorem exists_index_le_of_separated {τ : Type*} {K : Type*} [Field K] [CharZero K]
    [DecidableEq σ] [DecidableEq τ] {D₁ D₂ : ℕ} (hD₁ : D₁ ≠ 0) (hD₂ : D₂ ≠ 0)
    (d₁ : σ → ℕ) (d₂ : τ → ℕ) (hd₁ : ∀ k, D₁ ≤ d₁ k) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (α : σ → K) (β : τ → K) (P : MvPolynomial (σ ⊕ τ) K) (hP : P ≠ 0) :
    ∃ (r : ℕ) (S : ℚ), 0 < r ∧ ∀ θ q : ℚ,
      (r : ℚ) / (D₁ : ℚ) ≤ θ → 0 ≤ q → S ≤ q ^ 2 * (D₂ : ℚ) →
      ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P →
      θ ≤ (r : ℚ) / (D₁ : ℚ) + 2 * max (S / (r : ℚ)) q := by
  classical
  obtain ⟨r, φ, ψ, Dx, Dy, hr, hDx, hDy, hPeq, hne⟩ := exists_sepW_ne_zero P hP
  obtain ⟨S, hS⟩ :=
    exists_index_le_of_ne_zero (Sum.elim d₁ d₂) (Sum.elim α β) hne
  have hD₂Q : (0 : ℚ) < (D₂ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₂
  refine ⟨r, S, hr, fun θ q hθt hq0 hq hθ => ?_⟩
  refine index_le_two_mul_max_of_det_bound (Sum.elim d₁ d₂) (Sum.elim α β)
    (fun i j => (Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P θ ((r : ℚ) / (D₁ : ℚ))
    (D₂ : ℚ) S q hr hD₂Q hθt hq0 hq hθ
    (fun i j => cost_sepW_le hD₁ hD₂ d₁ d₂ hd₁ hd₂ Dx Dy hDx hDy i j) ?_
  rw [hPeq, ← sepW]
  exact hS

/-! ### Next

§13 is closed.  What is left is the constant bookkeeping, and it now has a shape:

1. **Bound the minimum representation length.**  `r ≤ d(split-off variable) + 1`, which is
   Mahler's `n ≤ r_m + 1`.  Needs the representation split on the *`τ`*-monomials (the arc
   splits on `σ`) and a length bound threaded through `exists_indep_representation`, which
   currently only shortens without saying by how much.
2. **Feed that to `RothGrowth`.**  With the split-off variable's degree smallest,
   `D₁ ≥ ω·d(split-off)`, so `t = r/D₁ ≲ 1/ω`.  Choosing `ω ≥ 2/ε` then gives `t ≤ ε/2`.
3. **The recursion** (§14): `ω(m, ε)` follows from 2, and `c_m = 2^m − 3` from iterating.

⚠ Provenance: §6 and §13 have been read directly and match.  §11 (property `Γ_m`) and §14 are
in the illegible region and have **not** been read; steps 2 and 3 above are the arc's own
reconstruction of what the growth condition must be doing, not a transcription.  They should
be checked against a clean copy before `ω(m, ε)` or `c_m = 2^m − 3` is asserted. -/



end MvPolynomial
