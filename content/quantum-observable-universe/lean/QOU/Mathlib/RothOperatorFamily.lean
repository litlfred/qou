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

  ═══ THE CONSTANT QUESTION, CLOSED ═══

  The sixth correction was about the row cost `t`.  It is now bounded by the growth constant
  alone: `exists_index_le_of_rothGrowth` gives

      index ≤ 2/ω + 2·max(S/r, q),

  so `ω ≥ 2/ε` makes the row cost at most `ε`.  Two steps got there:

  * `SeparatedRepresentation` bounds the minimum representation length by `d + 1` (Mahler's
    `n ≤ r_m + 1`), which makes `t` a ratio of **degrees**, `(d+1)/D₁`, rather than of a
    representation length.  ⚠ That bound is entirely about **which side the representation is
    grouped on**: the `x`-side gives one term per `x`-monomial, a *product* of degrees, and no
    growth condition rescues a row cost of that size.
  * `RothGrowth` (`QOU/Mathlib/RothLemmaStatement.lean`) orders the degrees so the split-off
    variable's is smallest, giving `(d+1)/D₁ ≤ 2/ω`.

  The join is written out rather than asserted: two true theorems that *look* like they fit is
  exactly the fifth correction's failure mode.  The only real work in it is the degree floor —
  §13 wants a **natural** `D₁ ≤ d₁ k`, the growth condition supplies a **rational** bound
  `ω·d ≤ d₁ k`, and `⌈ω·d⌉` sits between them.

  ⚠ **This is a fact about `RothGrowth` as this arc defines it.**  The source's parameter
  condition is property `Γ_m` (§11), which is in the illegible region and has not been read.
  If the two differ, what is proved concerns `RothLemmaUniform`, not Roth's lemma.
-/
import QOU.Mathlib.RothInductionStep
import QOU.Mathlib.BoundedOrderWronskian
import QOU.Mathlib.SeparatedRepresentation
import QOU.Mathlib.RothLemmaStatement

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

/-! ### Mahler's `n ≤ r_m + 1`, carried through

The length of the minimum representation is what the row cost `t = r/D₁` is made of, so a
bound on it is a bound on `t`.  `SeparatedRepresentation` supplies `r ≤ d + 1` when the
split-off group is a single variable of degree at most `d`; the two results below carry that
through the non-vanishing argument and into §13's conclusion.

⚠ Which side the representation is grouped on decides this completely: grouping on the
`x`-side gives `r = #{x\text{-monomials}}`, a *product* of degrees, and the row cost is then
hopeless.  See `exists_separated_representation_monomial_right`. -/

/-- `exists_sepW_ne_zero` with the length bound attached. -/
theorem exists_sepW_ne_zero_le_degreeOf {K : Type*} [Field K] [CharZero K] [DecidableEq σ]
    (P : MvPolynomial (σ ⊕ Unit) K) (hP : P ≠ 0) {d : ℕ}
    (hd : degreeOf (Sum.inr ()) P ≤ d) :
    ∃ (r : ℕ) (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial Unit K)
      (Dx : Fin r → List σ) (Dy : Fin r → List Unit),
      0 < r ∧ r ≤ d + 1 ∧ (∀ i, (Dx i).length ≤ (i : ℕ)) ∧ (∀ j, (Dy j).length ≤ (j : ℕ)) ∧
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) K) * rename Sum.inr (ψ k) ∧
      sepW Dx Dy φ ψ ≠ 0 := by
  classical
  obtain ⟨r, φ, ψ, hcard, hφ, hψ, hPeq⟩ :=
    exists_separated_representation_indep_le_degreeOf P hd
  have hr : 0 < r := by
    rcases Nat.eq_zero_or_pos r with rfl | h
    · exact absurd (hPeq.trans (by simp)) hP
    · exact h
  obtain ⟨Dx, hDx, hWx⟩ := exists_bounded_order_mvGenWronskian_ne_zero hr φ hφ
  obtain ⟨Dy, hDy, hWy⟩ := exists_bounded_order_mvGenWronskian_ne_zero hr ψ hψ
  refine ⟨r, φ, ψ, Dx, Dy, hr, hcard, hDx, hDy, hPeq, ?_⟩
  rw [sepW_eq]
  refine mul_ne_zero ?_ ?_
  · intro h
    have h0 : (rename Sum.inl (mvGenWronskian Dx φ) : MvPolynomial (σ ⊕ Unit) K)
        = rename Sum.inl 0 := by rw [h, map_zero]
    exact hWx (rename_injective _ Sum.inl_injective h0)
  · intro h
    have h0 : (rename Sum.inr (mvGenWronskian Dy ψ) : MvPolynomial (σ ⊕ Unit) K)
        = rename Sum.inr 0 := by rw [h, map_zero]
    exact hWy (rename_injective _ Sum.inr_injective h0)

/-- **§13 with the row cost made explicit.**

The `t` slot is now `(d+1)/D₁` — the split-off variable's degree over the degree floor of the
*other* variables — rather than the existentially-produced representation length.  That is the
form the growth condition can act on: `RothGrowth` makes the split-off degree the smallest, so
`D₁ ≥ ω·d` and `t ≲ 1/ω`.

⚠ That last step is **not proved here**.  This theorem makes `t` a ratio of *degrees*; turning
that ratio into `1/ω` needs `RothGrowth` and is the remaining piece.  What is settled is that
`t` no longer depends on how long a representation happens to be. -/
theorem exists_index_le_of_separated_le_degreeOf {K : Type*} [Field K] [CharZero K]
    [DecidableEq σ] {D₁ D₂ : ℕ} (hD₁ : D₁ ≠ 0) (hD₂ : D₂ ≠ 0)
    (d₁ : σ → ℕ) (d₂ : Unit → ℕ) (hd₁ : ∀ k, D₁ ≤ d₁ k) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (α : σ → K) (β : Unit → K) (P : MvPolynomial (σ ⊕ Unit) K) (hP : P ≠ 0)
    {d : ℕ} (hdeg : degreeOf (Sum.inr ()) P ≤ d) :
    ∃ (r : ℕ) (S : ℚ), 0 < r ∧ r ≤ d + 1 ∧ ∀ θ q : ℚ,
      ((d : ℚ) + 1) / (D₁ : ℚ) ≤ θ → 0 ≤ q → S ≤ q ^ 2 * (D₂ : ℚ) →
      ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P →
      θ ≤ ((d : ℚ) + 1) / (D₁ : ℚ) + 2 * max (S / (r : ℚ)) q := by
  classical
  obtain ⟨r, φ, ψ, Dx, Dy, hr, hcard, hDx, hDy, hPeq, hne⟩ :=
    exists_sepW_ne_zero_le_degreeOf P hP hdeg
  obtain ⟨S, hS⟩ := exists_index_le_of_ne_zero (Sum.elim d₁ d₂) (Sum.elim α β) hne
  have hD₁Q : (0 : ℚ) < (D₁ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₁
  have hD₂Q : (0 : ℚ) < (D₂ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₂
  have hrle : (r : ℚ) / (D₁ : ℚ) ≤ ((d : ℚ) + 1) / (D₁ : ℚ) := by
    refine div_le_div_of_nonneg_right ?_ hD₁Q.le
    have : (r : ℚ) ≤ ((d + 1 : ℕ) : ℚ) := by exact_mod_cast hcard
    push_cast at this
    linarith
  refine ⟨r, S, hr, hcard, fun θ q hθt hq0 hq hθ => ?_⟩
  refine index_le_two_mul_max_of_det_bound (Sum.elim d₁ d₂) (Sum.elim α β)
    (fun i j => (Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P θ (((d : ℚ) + 1) / (D₁ : ℚ))
    (D₂ : ℚ) S q hr hD₂Q hθt hq0 hq hθ
    (fun i j => le_trans (cost_sepW_le hD₁ hD₂ d₁ d₂ hd₁ hd₂ Dx Dy hDx hDy i j)
      (by linarith)) ?_
  rw [hPeq, ← sepW]
  exact hS


/-- The degree floor the join needs, packaged.

§13 wants a **natural** `D₁` below every `d₁ k`; the growth condition supplies the
**rational** bound `ω·d ≤ d₁ k`.  `⌈ω·d⌉` sits between them and also carries the cost bound.
Factored out because both forms of the conclusion below need exactly this. -/
theorem exists_degree_floor (ω : ℚ) (hω : 1 ≤ ω) (d₁ : σ → ℕ) (dl : ℕ) (hd0 : dl ≠ 0)
    (hgrow : ∀ k, ω * (dl : ℚ) ≤ (d₁ k : ℚ)) :
    ∃ D₁ : ℕ, D₁ ≠ 0 ∧ (∀ k, D₁ ≤ d₁ k) ∧ ((dl : ℚ) + 1) / (D₁ : ℚ) ≤ 2 / ω := by
  have hωpos : (0 : ℚ) < ω := lt_of_lt_of_le zero_lt_one hω
  have hdl1 : (1 : ℚ) ≤ (dl : ℚ) := by exact_mod_cast Nat.one_le_iff_ne_zero.mpr hd0
  have hcnn : (0 : ℤ) ≤ ⌈ω * (dl : ℚ)⌉ := Int.ceil_nonneg (by positivity)
  refine ⟨⌈ω * (dl : ℚ)⌉.toNat, ?_, ?_, ?_⟩ <;>
    [skip; skip; skip]
  all_goals {
    have hcast : ((⌈ω * (dl : ℚ)⌉.toNat : ℕ) : ℚ) = ((⌈ω * (dl : ℚ)⌉ : ℤ) : ℚ) := by
      rw [show ((⌈ω * (dl : ℚ)⌉.toNat : ℕ) : ℚ)
          = (((⌈ω * (dl : ℚ)⌉.toNat : ℕ) : ℤ) : ℚ) by push_cast; ring,
        Int.toNat_of_nonneg hcnn]
    have hfloor : ω * (dl : ℚ) ≤ ((⌈ω * (dl : ℚ)⌉.toNat : ℕ) : ℚ) := by
      rw [hcast]; exact Int.le_ceil _
    first
      | (intro h0
         have h1 : (1 : ℚ) ≤ ((⌈ω * (dl : ℚ)⌉.toNat : ℕ) : ℚ) := by nlinarith
         rw [h0] at h1
         norm_num at h1)
      | (intro k
         have h2 : ⌈ω * (dl : ℚ)⌉ ≤ (d₁ k : ℤ) := Int.ceil_le.mpr (by exact_mod_cast hgrow k)
         omega)
      | (have hpos : (0 : ℚ) < ((⌈ω * (dl : ℚ)⌉.toNat : ℕ) : ℚ) := by nlinarith
         rw [div_le_div_iff₀ hpos hωpos]
         nlinarith) }

/-- The growth condition, read off for the split-off variable. -/
theorem rothGrowth_split {m : ℕ} (o : (σ ⊕ Unit) ≃ Fin m) (ω : ℚ) (hω : 1 ≤ ω)
    (d₁ : σ → ℕ) (d₂ : Unit → ℕ) (hg : RothGrowth o ω (Sum.elim d₁ d₂))
    (hlast : ∀ k : σ, (o (Sum.inl k) : ℕ) + 1 ≤ (o (Sum.inr ()) : ℕ)) :
    ∀ k : σ, ω * ((d₂ () : ℕ) : ℚ) ≤ ((d₁ k : ℕ) : ℚ) := by
  intro k
  have h := rothGrowth_mul_le (o := o) hω hg (j := o (Sum.inl k)) (k := o (Sum.inr ()))
    (hlast k)
  simpa using h

/-! ### The two halves, joined

§13's conclusion has a row cost `t = (d+1)/D₁`; `RothGrowth` bounds that by `2/ω`.  Those are
two true theorems that *look* like they fit, which is precisely the situation the fifth
correction was about — so the join is written out and the elaborator, not this comment,
decides whether it holds.

The one piece of real work is the degree floor.  `exists_index_le_of_separated_le_degreeOf`
wants a **natural** `D₁` below every `d₁ k`; the growth condition supplies the **rational**
bound `ω·d ≤ d₁ k`.  `⌈ω·d⌉` sits between them, and that is the only reason a ceiling appears
here. -/

/-- **§13's conclusion with the row cost replaced by `2/ω`.**

Given the growth condition, an ordering in which the split-off variable comes last, and a
non-zero `P`, the index is at most `2/ω` plus §13's error term.  So `ω ≥ 2/ε` makes the row
cost at most `ε` — this is what `ω(m, ε)` has to be.

⚠ **A fact about `RothGrowth` as this arc defines it.**  The source's parameter condition is
property `Γ_m` (§11), which is in the illegible region and has not been read.  If the two
differ, this is a theorem about `RothLemmaUniform` and not about Roth's lemma. -/
theorem exists_index_le_of_rothGrowth {K : Type*} [Field K] [CharZero K] [DecidableEq σ]
    {m : ℕ} (o : (σ ⊕ Unit) ≃ Fin m) (ω : ℚ) (hω : 1 ≤ ω)
    (d₁ : σ → ℕ) (d₂ : Unit → ℕ)
    (hg : RothGrowth o ω (Sum.elim d₁ d₂))
    (hlast : ∀ k : σ, (o (Sum.inl k) : ℕ) + 1 ≤ (o (Sum.inr ()) : ℕ))
    (hd0 : d₂ () ≠ 0) {D₂ : ℕ} (hD₂ : D₂ ≠ 0) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (α : σ → K) (β : Unit → K) (P : MvPolynomial (σ ⊕ Unit) K) (hP : P ≠ 0)
    (hdeg : degreeOf (Sum.inr ()) P ≤ d₂ ()) :
    ∃ (r : ℕ) (S : ℚ), 0 < r ∧ r ≤ d₂ () + 1 ∧ ∀ θ q : ℚ,
      2 / ω ≤ θ → 0 ≤ q → S ≤ q ^ 2 * (D₂ : ℚ) →
      ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P →
      θ ≤ 2 / ω + 2 * max (S / (r : ℚ)) q := by
  obtain ⟨D₁, hD₁ne, hd₁, hcost⟩ :=
    exists_degree_floor ω hω d₁ (d₂ ()) hd0 (rothGrowth_split o ω hω d₁ d₂ hg hlast)
  obtain ⟨r, S, hr, hcard, hmain⟩ :=
    exists_index_le_of_separated_le_degreeOf hD₁ne hD₂ d₁ d₂ hd₁ hd₂ α β P hP hdeg
  exact ⟨r, S, hr, hcard, fun θ q hθ hq0 hq hidx =>
    le_trans (hmain θ q (le_trans hcost hθ) hq0 hq hidx) (by linarith)⟩


/-! ### What the induction hypothesis supplies

`exists_index_le_of_rothGrowth` leaves `S` — the bound on the determinant's index —
existential and unconstrained.  That is honest but not usable: the recursion has to *know* `S`
is small, and it knows that because `index_sepW` splits the determinant's index into the two
factors' indices, which the induction hypothesis (for the `x`-side) and the base case (for the
single split-off variable) bound.

⚠ Note the factor `r` in `hfac`.  It is not slack: the source's `J(W) ≤ n·Φ_m` carries it, and
it is what makes `S/r ≤ Φ` — which is the quantity correction 9 showed the conclusion actually
depends on.  A hypothesis bounding the factors by `Φ` *without* the `r` would be asking for
something stronger than the recursion can deliver. -/

/-- **§13's conclusion in the form the recursion consumes.**

`hfac` is what the induction hypothesis supplies: for *any* bounded-order family realising a
separated representation of `P`, the two Wronskians' indices sum to at most `r·Φ`.  Then

    index P ≤ 2/ω + 2·max(Φ, q)        whenever  (d+1)·Φ ≤ q²·D₂.

Both `2/ω` and `Φ` are small in the intended regime, and neither mentions the representation
length — the `r` in `hfac` cancels against the `S/r` in §13's conclusion.

⚠ Still not Roth's lemma: `hfac` is an assumption here, and discharging it is the induction. -/
theorem index_le_of_rothGrowth_of_factor_bound {K : Type*} [Field K] [CharZero K]
    [DecidableEq σ] {m : ℕ} (o : (σ ⊕ Unit) ≃ Fin m) (ω : ℚ) (hω : 1 ≤ ω)
    (d₁ : σ → ℕ) (d₂ : Unit → ℕ)
    (hg : RothGrowth o ω (Sum.elim d₁ d₂))
    (hlast : ∀ k : σ, (o (Sum.inl k) : ℕ) + 1 ≤ (o (Sum.inr ()) : ℕ))
    (hd0 : d₂ () ≠ 0) {D₂ : ℕ} (hD₂ : D₂ ≠ 0) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (α : σ → K) (β : Unit → K) (P : MvPolynomial (σ ⊕ Unit) K) (hP : P ≠ 0)
    (hdeg : degreeOf (Sum.inr ()) P ≤ d₂ ())
    (Φ : ℚ) (hΦ0 : 0 ≤ Φ)
    (hfac : ∀ (r : ℕ) (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial Unit K)
        (Dx : Fin r → List σ) (Dy : Fin r → List Unit),
      0 < r → (∀ i, (Dx i).length ≤ (i : ℕ)) → (∀ j, (Dy j).length ≤ (j : ℕ)) →
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) K) * rename Sum.inr (ψ k) →
      index d₁ α (mvGenWronskian Dx φ) + index d₂ β (mvGenWronskian Dy ψ)
        ≤ ((((r : ℚ) * Φ : ℚ)) : WithTop ℚ))
    (θ q : ℚ) (hθt : 2 / ω ≤ θ) (hq0 : 0 ≤ q)
    (hq : (((d₂ () : ℕ) : ℚ) + 1) * Φ ≤ q ^ 2 * (D₂ : ℚ))
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P) :
    θ ≤ 2 / ω + 2 * max Φ q := by
  have hD₂Q : (0 : ℚ) < (D₂ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₂
  obtain ⟨r, φ, ψ, Dx, Dy, hr, hcard, hDx, hDy, hPeq, -⟩ :=
    exists_sepW_ne_zero_le_degreeOf P hP hdeg
  obtain ⟨D₁, hD₁ne, hd₁, hcost⟩ :=
    exists_degree_floor ω hω d₁ (d₂ ()) hd0 (rothGrowth_split o ω hω d₁ d₂ hg hlast)
  have hD₁Q : (0 : ℚ) < (D₁ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₁ne
  have hrQ : (0 : ℚ) < (r : ℚ) := by exact_mod_cast hr
  have hrle : (r : ℚ) ≤ ((d₂ () : ℕ) : ℚ) + 1 := by
    have : (r : ℚ) ≤ ((d₂ () + 1 : ℕ) : ℚ) := by exact_mod_cast hcard
    push_cast at this; linarith
  have hS : index (Sum.elim d₁ d₂) (Sum.elim α β)
      (Matrix.of fun i j => pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det
        ≤ ((((r : ℚ) * Φ : ℚ)) : WithTop ℚ) := by
    rw [hPeq, ← sepW, index_sepW]
    exact hfac r φ ψ Dx Dy hr hDx hDy hPeq
  have hqq : (r : ℚ) * Φ ≤ q ^ 2 * (D₂ : ℚ) := le_trans (by nlinarith) hq
  have hmain := index_le_two_mul_max_of_det_bound (Sum.elim d₁ d₂) (Sum.elim α β)
    (fun i j => (Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P θ
    ((((d₂ () : ℕ) : ℚ) + 1) / (D₁ : ℚ)) (D₂ : ℚ) ((r : ℚ) * Φ) q hr hD₂Q
    (le_trans hcost hθt) hq0 hqq hθ
    (fun i j => le_trans (cost_sepW_le hD₁ne hD₂ d₁ d₂ hd₁ hd₂ Dx Dy hDx hDy i j)
      (by
        have : (r : ℚ) / (D₁ : ℚ) ≤ (((d₂ () : ℕ) : ℚ) + 1) / (D₁ : ℚ) :=
          div_le_div_of_nonneg_right hrle hD₁Q.le
        linarith)) hS
  rw [mul_div_cancel_left₀ Φ (ne_of_gt hrQ)] at hmain
  linarith


/-- **§13's conclusion from bounds at the rescaled degrees** — the literal shape of the
induction hypothesis.

`RothLemmaUniform` bounds the index of a polynomial *at its own declared degrees*.  In the
induction step the sub-problems carry the rescaled degrees `r·d`, so what the hypothesis
supplies is `hres`, not `hfac`.  `factor_bound_of_rescaled` converts one into the other, and
the factor `r` it introduces is exactly the one §13's `S/r` cancels.

⚠ `hres` is still an assumption.  Discharging it is the induction: the `x` side from
`RothLemmaUniform` at `m−1` (degree and height bounds on the Wronskian exist —
`degreeOf_mvGenWronskian_le`, `abs_coeff_mvGenWronskian_le`), the `y` side from
`RothBaseCase`. -/
theorem index_le_of_rothGrowth_of_rescaled_bounds {K : Type*} [Field K] [CharZero K]
    [DecidableEq σ] {m : ℕ} (o : (σ ⊕ Unit) ≃ Fin m) (ω : ℚ) (hω : 1 ≤ ω)
    (d₁ : σ → ℕ) (d₂ : Unit → ℕ)
    (hg : RothGrowth o ω (Sum.elim d₁ d₂))
    (hlast : ∀ k : σ, (o (Sum.inl k) : ℕ) + 1 ≤ (o (Sum.inr ()) : ℕ))
    (hd0 : d₂ () ≠ 0) {D₂ : ℕ} (hD₂ : D₂ ≠ 0) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (α : σ → K) (β : Unit → K) (P : MvPolynomial (σ ⊕ Unit) K) (hP : P ≠ 0)
    (hdeg : degreeOf (Sum.inr ()) P ≤ d₂ ())
    (εU εV : ℚ) (hε : 0 ≤ εU + εV)
    (hres : ∀ (r : ℕ) (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial Unit K)
        (Dx : Fin r → List σ) (Dy : Fin r → List Unit),
      0 < r → (∀ i, (Dx i).length ≤ (i : ℕ)) → (∀ j, (Dy j).length ≤ (j : ℕ)) →
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) K) * rename Sum.inr (ψ k) →
      index (fun j => r * d₁ j) α (mvGenWronskian Dx φ) ≤ ((εU : ℚ) : WithTop ℚ) ∧
        index (fun j => r * d₂ j) β (mvGenWronskian Dy ψ) ≤ ((εV : ℚ) : WithTop ℚ))
    (θ q : ℚ) (hθt : 2 / ω ≤ θ) (hq0 : 0 ≤ q)
    (hq : (((d₂ () : ℕ) : ℚ) + 1) * (εU + εV) ≤ q ^ 2 * (D₂ : ℚ))
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P) :
    θ ≤ 2 / ω + 2 * max (εU + εV) q :=
  index_le_of_rothGrowth_of_factor_bound o ω hω d₁ d₂ hg hlast hd0 hD₂ hd₂ α β P hP hdeg
    (εU + εV) hε
    (fun r φ ψ Dx Dy hr hDx hDy hPeq =>
      have h := hres r φ ψ Dx Dy hr hDx hDy hPeq
      factor_bound_of_rescaled (Nat.pos_iff_ne_zero.mp hr) d₁ d₂ α β Dx Dy φ ψ εU εV
        h.1 h.2)
    θ q hθt hq0 hq hθ

/-! ### Next

The chain now runs from the induction hypothesis's literal shape to §13's conclusion:

    hres  (bounds at the RESCALED degrees — what RothLemmaUniform gives)
      ↓  factor_bound_of_rescaled
    hfac  (the two Wronskians' indices sum to ≤ r·Φ)
      ↓  index_le_of_rothGrowth_of_factor_bound
    index P ≤ 2/ω + 2·max(εU + εV, q)

Everything above `hres` is proved.  What remains is **discharging `hres`**, in two halves:

1. **The `x` half — blocked on transport, not on mathematics.**  `RothLemmaUniform` at `m−1`
   bounds `index (r·d₁) α (mvGenWronskian Dx φ)` given degree and height bounds on that
   Wronskian, and both exist (`degreeOf_mvGenWronskian_le`, `abs_coeff_mvGenWronskian_le`).
   The gap is that these theorems are stated for `σ ⊕ Unit` while `RothLemmaUniform` takes an
   `o : σ ≃ Fin m`.  Bridging that is `Fin (n+1) ≃ Fin n ⊕ Unit` plus `index_rename_equiv`.
2. **The `y` half.**  One variable, so `RothBaseCase` applies directly; the work is matching
   its `ℤ`-coefficient, height-and-denominator hypotheses to what the step has.

Then `c_m = 2^m − 3` by iterating with `rothLemmaUniform_one` as the base.

⚠ Provenance: §5, §6 and §13 have been read directly and match.  §11 (property `Γ_m`) and §14
have **not**.  The `2/ω` bound is the arc's own reconstruction of what a growth condition must
be doing; `c_m = 2^m − 3` stays unasserted. -/







end MvPolynomial
