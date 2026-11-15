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

      index ≤ 1/ω + 2·max(S/r, q),

  so `ω ≥ 1/ε` makes the row cost at most `ε`.  Under §11's `ω = 1/t` that leading term is
  exactly the source's `t` — see correction 24 at `cost_sepW_le`, which is what removed a
  spurious factor `2`.  Two steps got there:

  * `SeparatedRepresentation` bounds the minimum representation length by `d + 1` (Mahler's
    `n ≤ r_m + 1`), which makes `t` a ratio of **degrees**, `d/D₁`, rather than of a
    representation length — the `+1` cancels against `cost_sepW_le`'s `r - 1`.  ⚠ That bound
    is entirely about **which side the representation is grouped on**: the `x`-side gives one
    term per `x`-monomial, a *product* of degrees, and no growth condition rescues a row cost
    of that size.
  * `RothGrowth` (`QOU/Mathlib/RothLemmaStatement.lean`) orders the degrees so the split-off
    variable's is smallest, giving `d/D₁ ≤ 1/ω`.

  The join is written out rather than asserted: two true theorems that *look* like they fit is
  exactly the fifth correction's failure mode.  The only real work in it is the degree floor —
  §13 wants a **natural** `D₁ ≤ d₁ k`, the growth condition supplies a **rational** bound
  `ω·d ≤ d₁ k`, and `⌈ω·d⌉` sits between them.

  §11 has since been read from the page scans: property `Γ_m`'s first clause is exactly
  `RothGrowth` with `ω = 1/t`, so this is a fact about the source's condition and the caveat
  that used to stand here is withdrawn.  ⚠ `Γ_m`'s two *other* clauses are still not carried
  anywhere in this arc, which makes its statements stronger than the source's, not weaker —
  see `RothLemmaMahler`.
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
rejected and §13's square root.

⚠ **The twenty-fourth correction lives in the numerator `r - 1`.**  It used to be `r`, via
`(Dx i).length ≤ i ≤ r` — true, but one larger than what is available, since `i : Fin r` gives
`i ≤ r - 1`.  That single unit is the difference between the source's row cost and twice it:
§13's row term is `(μ-1)/r_{m-1}` with `μ ≤ n`, i.e. numerator `n - 1 = r - 1`, and the chain
`(r-1)/D₁ ≤ d/D₁ ≤ t` closes only with the tight numerator.  With `r` the chain has to go
through `(d+1)/D₁ ≤ 2/ω`, and the factor `2` it picks up is not slack that later cancels — it
is a `2t` where §14 needs a `t`, and `rothConstant m = 2^(m+1) - 3` is pinned against `t`. -/
theorem cost_sepW_le {τ : Type*} {r D₁ D₂ : ℕ} (hD₁ : D₁ ≠ 0) (hD₂ : D₂ ≠ 0)
    (d₁ : σ → ℕ) (d₂ : τ → ℕ) (hd₁ : ∀ k, D₁ ≤ d₁ k) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (hDx : ∀ i, (Dx i).length ≤ (i : ℕ)) (hDy : ∀ j, (Dy j).length ≤ (j : ℕ)) (i j : Fin r) :
    (((Dx i).map Sum.inl ++ (Dy j).map Sum.inr).map
        (fun k => (1 : ℚ) / ((Sum.elim d₁ d₂ k : ℕ) : ℚ))).sum
      ≤ ((r - 1 : ℕ) : ℚ) / (D₁ : ℚ) + (j : ℚ) / (D₂ : ℚ) := by
  have hD₁Q : (0 : ℚ) < (D₁ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₁
  have hD₂Q : (0 : ℚ) < (D₂ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₂
  have hi : (i : ℕ) < r := i.isLt
  rw [sum_map_inv_append_sumElim]
  refine add_le_add (le_trans (sum_map_inv_le_length_div hD₁ d₁ hd₁ _) ?_)
    (le_trans (sum_map_inv_le_length_div hD₂ d₂ hd₂ _) ?_)
  · refine div_le_div_of_nonneg_right ?_ hD₁Q.le
    exact_mod_cast le_trans (hDx i) (by omega : (i : ℕ) ≤ r - 1)
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
      ((r - 1 : ℕ) : ℚ) / (D₁ : ℚ) ≤ θ → 0 ≤ q → S ≤ q ^ 2 * (D₂ : ℚ) →
      ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P →
      θ ≤ ((r - 1 : ℕ) : ℚ) / (D₁ : ℚ) + 2 * max (S / (r : ℚ)) q := by
  classical
  obtain ⟨r, φ, ψ, Dx, Dy, hr, hDx, hDy, hPeq, hne⟩ := exists_sepW_ne_zero P hP
  obtain ⟨S, hS⟩ :=
    exists_index_le_of_ne_zero (Sum.elim d₁ d₂) (Sum.elim α β) hne
  have hD₂Q : (0 : ℚ) < (D₂ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₂
  refine ⟨r, S, hr, fun θ q hθt hq0 hq hθ => ?_⟩
  refine index_le_two_mul_max_of_det_bound (Sum.elim d₁ d₂) (Sum.elim α β)
    (fun i j => (Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P θ (((r - 1 : ℕ) : ℚ) / (D₁ : ℚ))
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
      (∀ k x, degreeOf x (φ k) ≤ degreeOf (Sum.inl x) P) ∧
      (∀ k y, degreeOf y (ψ k) ≤ degreeOf (Sum.inr y) P) ∧
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) K) * rename Sum.inr (ψ k) ∧
      sepW Dx Dy φ ψ ≠ 0 := by
  classical
  obtain ⟨r, φ, ψ, hcard, hφ, hψ, hdφ, hdψ, hPeq⟩ :=
    exists_separated_representation_indep_le_degreeOf P hd
  have hr : 0 < r := by
    rcases Nat.eq_zero_or_pos r with rfl | h
    · exact absurd (hPeq.trans (by simp)) hP
    · exact h
  obtain ⟨Dx, hDx, hWx⟩ := exists_bounded_order_mvGenWronskian_ne_zero hr φ hφ
  obtain ⟨Dy, hDy, hWy⟩ := exists_bounded_order_mvGenWronskian_ne_zero hr ψ hψ
  refine ⟨r, φ, ψ, Dx, Dy, hr, hcard, hDx, hDy, hdφ, hdψ, hPeq, ?_⟩
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
`t` no longer depends on how long a representation happens to be.

⚠ The `t` slot is `d/D₁`, not `(d+1)/D₁`: `cost_sepW_le`'s numerator is `r - 1` and
`r ≤ d + 1`, so the `+1` cancels against it rather than surviving into the bound.  That is
correction 24 — see `cost_sepW_le`. -/
theorem exists_index_le_of_separated_le_degreeOf {K : Type*} [Field K] [CharZero K]
    [DecidableEq σ] {D₁ D₂ : ℕ} (hD₁ : D₁ ≠ 0) (hD₂ : D₂ ≠ 0)
    (d₁ : σ → ℕ) (d₂ : Unit → ℕ) (hd₁ : ∀ k, D₁ ≤ d₁ k) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (α : σ → K) (β : Unit → K) (P : MvPolynomial (σ ⊕ Unit) K) (hP : P ≠ 0)
    {d : ℕ} (hdeg : degreeOf (Sum.inr ()) P ≤ d) :
    ∃ (r : ℕ) (S : ℚ), 0 < r ∧ r ≤ d + 1 ∧ ∀ θ q : ℚ,
      (d : ℚ) / (D₁ : ℚ) ≤ θ → 0 ≤ q → S ≤ q ^ 2 * (D₂ : ℚ) →
      ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P →
      θ ≤ (d : ℚ) / (D₁ : ℚ) + 2 * max (S / (r : ℚ)) q := by
  classical
  obtain ⟨r, φ, ψ, Dx, Dy, hr, hcard, hDx, hDy, hdφ, hdψ, hPeq, hne⟩ :=
    exists_sepW_ne_zero_le_degreeOf P hP hdeg
  obtain ⟨S, hS⟩ := exists_index_le_of_ne_zero (Sum.elim d₁ d₂) (Sum.elim α β) hne
  have hD₁Q : (0 : ℚ) < (D₁ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₁
  have hD₂Q : (0 : ℚ) < (D₂ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₂
  have hrle : ((r - 1 : ℕ) : ℚ) / (D₁ : ℚ) ≤ (d : ℚ) / (D₁ : ℚ) := by
    refine div_le_div_of_nonneg_right ?_ hD₁Q.le
    exact_mod_cast (by omega : r - 1 ≤ d)
  refine ⟨r, S, hr, hcard, fun θ q hθt hq0 hq hθ => ?_⟩
  refine index_le_two_mul_max_of_det_bound (Sum.elim d₁ d₂) (Sum.elim α β)
    (fun i j => (Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P θ ((d : ℚ) / (D₁ : ℚ))
    (D₂ : ℚ) S q hr hD₂Q hθt hq0 hq hθ
    (fun i j => le_trans (cost_sepW_le hD₁ hD₂ d₁ d₂ hd₁ hd₂ Dx Dy hDx hDy i j)
      (by linarith)) ?_
  rw [hPeq, ← sepW]
  exact hS


/-- The degree floor the join needs, packaged.

§13 wants a **natural** `D₁` below every `d₁ k`; the growth condition supplies the
**rational** bound `ω·d ≤ d₁ k`.  `⌈ω·d⌉` sits between them and also carries the cost bound.
Factored out because both forms of the conclusion below need exactly this.

⚠ The cost clause used to read `(dl + 1)/D₁ ≤ 2/ω`, and the factor `2` was `1 + 1/dl ≤ 2` —
the crude bound at `dl = 1`.  With `cost_sepW_le`'s numerator tightened from `r` to `r - 1`
the `+1` is no longer needed: `r - 1 ≤ dl`, and `dl/D₁ ≤ 1/ω` is exact, not crude.  This is
§13's own step `(n-1)/r_{m-1} ≤ r_m/r_{m-1} ≤ t` verbatim. -/
theorem exists_degree_floor (ω : ℚ) (hω : 1 ≤ ω) (d₁ : σ → ℕ) (dl : ℕ) (hd0 : dl ≠ 0)
    (hgrow : ∀ k, ω * (dl : ℚ) ≤ (d₁ k : ℚ)) :
    ∃ D₁ : ℕ, D₁ ≠ 0 ∧ (∀ k, D₁ ≤ d₁ k) ∧ (dl : ℚ) / (D₁ : ℚ) ≤ 1 / ω := by
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

§13's conclusion has a row cost `t = d/D₁`; `RothGrowth` bounds that by `1/ω`.  Those are
two true theorems that *look* like they fit, which is precisely the situation the fifth
correction was about — so the join is written out and the elaborator, not this comment,
decides whether it holds.

The one piece of real work is the degree floor.  `exists_index_le_of_separated_le_degreeOf`
wants a **natural** `D₁` below every `d₁ k`; the growth condition supplies the **rational**
bound `ω·d ≤ d₁ k`.  `⌈ω·d⌉` sits between them, and that is the only reason a ceiling appears
here. -/

/-- **§13's conclusion with the row cost replaced by `1/ω`.**

Given the growth condition, an ordering in which the split-off variable comes last, and a
non-zero `P`, the index is at most `1/ω` plus §13's error term.

§11 has since been read: `Γ_m`'s first clause is `RothGrowth` with `ω = 1/t`, so this is a
theorem about the source's condition, and under that identification the leading term is `t`
— §13's own, on the nose.

⚠ It used to read `2/ω`, and an earlier version of this docstring drew a *conclusion* from
that: "`ω ≥ 2/ε` makes the row cost at most `ε` — this is what `ω(m, ε)` has to be", which a
later pass had to retract as a conflation of the row cost with §14's height parameter `t/m`.
The retraction was right and the premise was still wrong: the `2` was never in §13 at all.
Correction 24 (`cost_sepW_le`) removed it.  ⚠ The lesson is the same one correction 17 taught
about labels — a wrong factor in a docstring is invisible to `lake build`, and here it had
already survived one round of *being reasoned about* without being checked against the source
step it was supposed to mirror. -/
theorem exists_index_le_of_rothGrowth {K : Type*} [Field K] [CharZero K] [DecidableEq σ]
    {m : ℕ} (o : (σ ⊕ Unit) ≃ Fin m) (ω : ℚ) (hω : 1 ≤ ω)
    (d₁ : σ → ℕ) (d₂ : Unit → ℕ)
    (hg : RothGrowth o ω (Sum.elim d₁ d₂))
    (hlast : ∀ k : σ, (o (Sum.inl k) : ℕ) + 1 ≤ (o (Sum.inr ()) : ℕ))
    (hd0 : d₂ () ≠ 0) {D₂ : ℕ} (hD₂ : D₂ ≠ 0) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (α : σ → K) (β : Unit → K) (P : MvPolynomial (σ ⊕ Unit) K) (hP : P ≠ 0)
    (hdeg : degreeOf (Sum.inr ()) P ≤ d₂ ()) :
    ∃ (r : ℕ) (S : ℚ), 0 < r ∧ r ≤ d₂ () + 1 ∧ ∀ θ q : ℚ,
      1 / ω ≤ θ → 0 ≤ q → S ≤ q ^ 2 * (D₂ : ℚ) →
      ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P →
      θ ≤ 1 / ω + 2 * max (S / (r : ℚ)) q := by
  obtain ⟨D₁, hD₁ne, hd₁, hcost⟩ :=
    exists_degree_floor ω hω d₁ (d₂ ()) hd0 (rothGrowth_split o ω hω d₁ d₂ hg hlast)
  obtain ⟨r, S, hr, hcard, hmain⟩ :=
    exists_index_le_of_separated_le_degreeOf hD₁ne hD₂ d₁ d₂ hd₁ hd₂ α β P hP hdeg
  exact ⟨r, S, hr, hcard, fun θ q hθ hq0 hq hidx =>
    le_trans (hmain θ q (le_trans hcost hθ) hq0 hq hidx) (by linarith)⟩


/-! ### ⚠ The tenth correction: "for every bounded-order family" is unsatisfiable

`hfac` and `hres` below quantify over the families realising a separated representation of
`P`, and an earlier version quantified over **all** of them.  That version is **vacuous**.

Take `Dx i = []` for every `i`.  The order condition `|Dx i| ≤ i` holds, since `0 ≤ i`; the
family realises the same representation, because it does not touch `φ` or `ψ`; and for `r ≥ 2`
its Wronskian matrix has all rows equal, so the determinant is `0` and the index is `⊤` — below
no finite bound.  `mvGenWronskian_nil_eq_zero` (`QOU/Mathlib/MvGenWronskian.lean`) is that
computation.  And every `P` admits a length-`2` representation (pad a shorter one with zeros),
so this is not an edge case: the hypothesis was false for **every** `P`.

The repair is to carry `mvGenWronskian Dx φ ≠ 0` and `mvGenWronskian Dy ψ ≠ 0` into `hfac`, and
it costs nothing, because the proof only ever applies `hfac` to the family
`exists_sepW_ne_zero_le_degreeOf` produces — whose Wronskians are non-zero by construction.
The hypothesis had simply been stated more strongly than the argument used.

⚠ **How this was found, and what did not find it.**  It surfaced when the two halves of `hres`
were finally supplied and the non-vanishing hypotheses they need had nowhere to come from.
Neither `lake build` nor `#print axioms` could have caught it, and neither could a witness at
small `r` — at `r = 1` a one-column determinant is `φ 0`, which need not vanish, so the
hypothesis is satisfiable there.  That is correction 9's lesson exactly: **a hypothesis nobody
has had to discharge is indistinguishable from a false one**, and the discharging is what
tests it. -/

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

/-- **§13's conclusion with the realising family handed back.**

`index_le_of_rothGrowth_of_factor_bound` below quantifies `hfac` over *every* bounded-order
family, which is the shape a hypothesis wants but **not** a shape the recursion can discharge:
the induction hypothesis bounds the two Wronskians against `Θ'` for the system descended at the
representation length `r`, and `r` is not known until the representation exists.  A `∀ r`
hypothesis would need a `Θ'` uniform in `r`, and there is none.

So this form runs `exists_sepW_ne_zero_le_degreeOf` first and returns the family, leaving the
factor bound as the *last* thing the caller supplies — by which time `r` is fixed and
`rothGammaFull_descend` can be applied at it.  Everything else is the same derivation;
`index_le_of_rothGrowth_of_factor_bound` is now a two-line corollary.

⚠ The degree clauses are stated against `P`'s own `degreeOf`, not against `d₁`/`d₂`: that is
what `SeparatedRepresentation` proves, and the caller has `P`'s degrees in hand. -/
theorem exists_family_index_le_of_rothGrowth {K : Type*} [Field K] [CharZero K]
    [DecidableEq σ] {m : ℕ} (o : (σ ⊕ Unit) ≃ Fin m) (ω : ℚ) (hω : 1 ≤ ω)
    (d₁ : σ → ℕ) (d₂ : Unit → ℕ)
    (hg : RothGrowth o ω (Sum.elim d₁ d₂))
    (hlast : ∀ k : σ, (o (Sum.inl k) : ℕ) + 1 ≤ (o (Sum.inr ()) : ℕ))
    (hd0 : d₂ () ≠ 0) {D₂ : ℕ} (hD₂ : D₂ ≠ 0) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (α : σ → K) (β : Unit → K) (P : MvPolynomial (σ ⊕ Unit) K) (hP : P ≠ 0)
    (hdeg : degreeOf (Sum.inr ()) P ≤ d₂ ()) :
    ∃ (r : ℕ) (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial Unit K)
      (Dx : Fin r → List σ) (Dy : Fin r → List Unit),
      0 < r ∧ r ≤ d₂ () + 1 ∧
      (∀ i, (Dx i).length ≤ (i : ℕ)) ∧ (∀ j, (Dy j).length ≤ (j : ℕ)) ∧
      (∀ k x, degreeOf x (φ k) ≤ degreeOf (Sum.inl x) P) ∧
      (∀ k y, degreeOf y (ψ k) ≤ degreeOf (Sum.inr y) P) ∧
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) K) * rename Sum.inr (ψ k) ∧
      mvGenWronskian Dx φ ≠ 0 ∧ mvGenWronskian Dy ψ ≠ 0 ∧
      ∀ Φ θ q : ℚ, 0 ≤ Φ →
        index d₁ α (mvGenWronskian Dx φ) + index d₂ β (mvGenWronskian Dy ψ)
            ≤ ((((r : ℚ) * Φ : ℚ)) : WithTop ℚ) →
        1 / ω ≤ θ → 0 ≤ q → (((d₂ () : ℕ) : ℚ) + 1) * Φ ≤ q ^ 2 * (D₂ : ℚ) →
        ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P →
        θ ≤ 1 / ω + 2 * max Φ q := by
  classical
  have hD₂Q : (0 : ℚ) < (D₂ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₂
  obtain ⟨r, φ, ψ, Dx, Dy, hr, hcard, hDx, hDy, hdφ, hdψ, hPeq, hne⟩ :=
    exists_sepW_ne_zero_le_degreeOf P hP hdeg
  rw [sepW_eq] at hne
  have hWx : mvGenWronskian Dx φ ≠ 0 := by
    intro h; rw [h, map_zero, zero_mul] at hne; exact hne rfl
  have hWy : mvGenWronskian Dy ψ ≠ 0 := by
    intro h; rw [h, map_zero, mul_zero] at hne; exact hne rfl
  obtain ⟨D₁, hD₁ne, hd₁, hcost⟩ :=
    exists_degree_floor ω hω d₁ (d₂ ()) hd0 (rothGrowth_split o ω hω d₁ d₂ hg hlast)
  have hD₁Q : (0 : ℚ) < (D₁ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₁ne
  have hrQ : (0 : ℚ) < (r : ℚ) := by exact_mod_cast hr
  have hrle : (r : ℚ) ≤ ((d₂ () : ℕ) : ℚ) + 1 := by
    have : (r : ℚ) ≤ ((d₂ () + 1 : ℕ) : ℚ) := by exact_mod_cast hcard
    push_cast at this; linarith
  refine ⟨r, φ, ψ, Dx, Dy, hr, hcard, hDx, hDy, hdφ, hdψ, hPeq, hWx, hWy, ?_⟩
  intro Φ θ q hΦ0 hfac hθt hq0 hq hθ
  have hS : index (Sum.elim d₁ d₂) (Sum.elim α β)
      (Matrix.of fun i j => pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det
        ≤ ((((r : ℚ) * Φ : ℚ)) : WithTop ℚ) := by
    rw [hPeq, ← sepW, index_sepW]
    exact hfac
  have hqq : (r : ℚ) * Φ ≤ q ^ 2 * (D₂ : ℚ) := le_trans (by nlinarith) hq
  have hmain := index_le_two_mul_max_of_det_bound (Sum.elim d₁ d₂) (Sum.elim α β)
    (fun i j => (Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P θ
    ((((d₂ () : ℕ) : ℚ)) / (D₁ : ℚ)) (D₂ : ℚ) ((r : ℚ) * Φ) q hr hD₂Q
    (le_trans hcost hθt) hq0 hqq hθ
    (fun i j => le_trans (cost_sepW_le hD₁ne hD₂ d₁ d₂ hd₁ hd₂ Dx Dy hDx hDy i j)
      (by
        have : ((r - 1 : ℕ) : ℚ) / (D₁ : ℚ) ≤ (((d₂ () : ℕ) : ℚ)) / (D₁ : ℚ) :=
          div_le_div_of_nonneg_right (by exact_mod_cast (by omega : r - 1 ≤ d₂ ())) hD₁Q.le
        linarith)) hS
  rw [mul_div_cancel_left₀ Φ (ne_of_gt hrQ)] at hmain
  linarith

/-- **§13's two branches, packaged into `RothLemma4`'s `w`** — pure `ℚ` arithmetic.

`index_le_or_sq_of_det_bound` returns `θ − t ≤ 2S/r ∨ (θ − t)²·d ≤ 2S` at `S = r·Φ`.  Both
branches give a `w` with `w ≤ Φ ∨ w² ≤ Φ` and `θ ≤ t + 2w`:

* the first is `w := Φ`, once `2(rΦ)/r` is cancelled to `2Φ`;
* the second is `w := max(0, (θ − t)/2)`, whose square is `(θ − t)²/4 ≤ Φ` by `r ≤ 2d`.

⚠ `r ≤ 2d` is where `n ≤ r_m + 1` is spent — it is `r ≤ d + 1 ≤ 2d` for `d ≥ 1`, the same
step the source writes as `2/r_m ≤ 4/n`.  The `max(0, ·)` is what makes the second branch
unconditional: at `θ < t` the halved difference is negative and `w := 0` serves. -/
theorem exists_w_of_branches {t θ Φ r d : ℚ} (hΦ0 : 0 ≤ Φ) (hd : 0 < d) (hr : 0 < r)
    (hr2 : r ≤ 2 * d)
    (h : θ - t ≤ 2 * (r * Φ) / r ∨ (θ - t) ^ 2 * d ≤ 2 * (r * Φ)) :
    ∃ w : ℚ, (w ≤ Φ ∨ w ^ 2 ≤ Φ) ∧ θ ≤ t + 2 * w := by
  rcases h with h | h
  · refine ⟨Φ, Or.inl le_rfl, ?_⟩
    have hrw : 2 * (r * Φ) / r = 2 * Φ := by field_simp
    rw [hrw] at h
    linarith
  · refine ⟨max 0 ((θ - t) / 2), Or.inr ?_,
      by linarith [le_max_right (0 : ℚ) ((θ - t) / 2)]⟩
    rcases le_or_gt θ t with hle | hlt
    · have hz : max 0 ((θ - t) / 2) = 0 := max_eq_left (by linarith)
      rw [hz]; simpa using hΦ0
    · have hz : max 0 ((θ - t) / 2) = (θ - t) / 2 := max_eq_right (by linarith)
      rw [hz]
      have hstep : (θ - t) ^ 2 * d ≤ 4 * Φ * d := by
        nlinarith [mul_le_mul_of_nonneg_right hr2 hΦ0]
      have hkey : (θ - t) ^ 2 ≤ 4 * Φ := le_of_mul_le_mul_right hstep hd
      have hsq : ((θ - t) / 2) ^ 2 = (θ - t) ^ 2 / 4 := by ring
      rw [hsq]; linarith

/-- **§13's conclusion in `RothLemma4`'s own shape** — the two branches, packaged as `w`, with
the realising family handed back and **no `q` and no side condition**.

`index_le_two_mul_max_of_det_bound` rounds the two branches into `t + 2·max(Φ, q)`, which costs
a rational stand-in `q` for `√Φ` and the junction condition `(d+1)·Φ ≤ q²·D₂`.  That condition
is where the `1/d` slack lives, and it is fatal here: the smallest admissible `q` has
`q² = (1 + 1/d)·Φ`, so `q² ≤ Ψ` fails by exactly `Φ/d` and `RothLemma4`'s `w` cannot be `q`.

`index_le_or_sq_of_det_bound` keeps the branches apart and squared, and then neither problem
arises:

* `θ − t ≤ 2Φ`      → `w := Φ`, first disjunct;
* `(θ − t)²·d ≤ 2rΦ` → `(θ − t)² ≤ 4Φ` by `r ≤ d + 1 ≤ 2d`, so `w := max(0, (θ − t)/2)` has
  `w² ≤ Φ`, second disjunct.

The `max(0, ·)` is what makes the second branch unconditional: when `θ < t` the halved
difference is negative and `w := 0` serves, needing only `0 ≤ Φ`.

⚠ The degree floor is `d₂ ()` itself, not a parameter `D₂ ≤ d₂ ()`.  The second branch divides
by it, so a smaller floor would weaken `r ≤ D₂ + 1` and the `≤ 4Φ` step fails.  On `Unit` there
is nothing to choose anyway. -/
theorem exists_family_index_le_w_of_rothGrowth {K : Type*} [Field K] [CharZero K]
    [DecidableEq σ] {m : ℕ} (o : (σ ⊕ Unit) ≃ Fin m) (ω : ℚ) (hω : 1 ≤ ω)
    (d₁ : σ → ℕ) (d₂ : Unit → ℕ)
    (hg : RothGrowth o ω (Sum.elim d₁ d₂))
    (hlast : ∀ k : σ, (o (Sum.inl k) : ℕ) + 1 ≤ (o (Sum.inr ()) : ℕ))
    (hd0 : d₂ () ≠ 0)
    (α : σ → K) (β : Unit → K) (P : MvPolynomial (σ ⊕ Unit) K) (hP : P ≠ 0)
    (hdeg : degreeOf (Sum.inr ()) P ≤ d₂ ()) :
    ∃ (r : ℕ) (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial Unit K)
      (Dx : Fin r → List σ) (Dy : Fin r → List Unit),
      0 < r ∧ r ≤ d₂ () + 1 ∧
      (∀ i, (Dx i).length ≤ (i : ℕ)) ∧ (∀ j, (Dy j).length ≤ (j : ℕ)) ∧
      (∀ k x, degreeOf x (φ k) ≤ degreeOf (Sum.inl x) P) ∧
      (∀ k y, degreeOf y (ψ k) ≤ degreeOf (Sum.inr y) P) ∧
      P = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) K) * rename Sum.inr (ψ k) ∧
      mvGenWronskian Dx φ ≠ 0 ∧ mvGenWronskian Dy ψ ≠ 0 ∧
      ∀ Φ θ : ℚ, 0 ≤ Φ →
        index d₁ α (mvGenWronskian Dx φ) + index d₂ β (mvGenWronskian Dy ψ)
            ≤ ((((r : ℚ) * Φ : ℚ)) : WithTop ℚ) →
        1 / ω ≤ θ →
        ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P →
        ∃ w : ℚ, (w ≤ Φ ∨ w ^ 2 ≤ Φ) ∧ θ ≤ 1 / ω + 2 * w := by
  classical
  have hd2N : 0 < d₂ () := Nat.pos_of_ne_zero hd0
  have hd2Q : (0 : ℚ) < ((d₂ () : ℕ) : ℚ) := by exact_mod_cast hd2N
  have hd₂ : ∀ k, d₂ () ≤ d₂ k := fun k => by cases k; exact le_rfl
  obtain ⟨r, φ, ψ, Dx, Dy, hr, hcard, hDx, hDy, hdφ, hdψ, hPeq, hne⟩ :=
    exists_sepW_ne_zero_le_degreeOf P hP hdeg
  rw [sepW_eq] at hne
  have hWx : mvGenWronskian Dx φ ≠ 0 := by
    intro h; rw [h, map_zero, zero_mul] at hne; exact hne rfl
  have hWy : mvGenWronskian Dy ψ ≠ 0 := by
    intro h; rw [h, map_zero, mul_zero] at hne; exact hne rfl
  obtain ⟨D₁, hD₁ne, hd₁, hcost⟩ :=
    exists_degree_floor ω hω d₁ (d₂ ()) hd0 (rothGrowth_split o ω hω d₁ d₂ hg hlast)
  have hD₁Q : (0 : ℚ) < (D₁ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₁ne
  have hrQ : (0 : ℚ) < (r : ℚ) := by exact_mod_cast hr
  have hrle : (r : ℚ) ≤ ((d₂ () : ℕ) : ℚ) + 1 := by
    have : (r : ℚ) ≤ ((d₂ () + 1 : ℕ) : ℚ) := by exact_mod_cast hcard
    push_cast at this; linarith
  refine ⟨r, φ, ψ, Dx, Dy, hr, hcard, hDx, hDy, hdφ, hdψ, hPeq, hWx, hWy, ?_⟩
  intro Φ θ hΦ0 hfac hθt hθ
  have hS : index (Sum.elim d₁ d₂) (Sum.elim α β)
      (Matrix.of fun i j => pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det
        ≤ ((((r : ℚ) * Φ : ℚ)) : WithTop ℚ) := by
    rw [hPeq, ← sepW, index_sepW]
    exact hfac
  have hor := index_le_or_sq_of_det_bound (Sum.elim d₁ d₂) (Sum.elim α β)
    (fun i j => (Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P θ
    ((((d₂ () : ℕ) : ℚ)) / (D₁ : ℚ)) (((d₂ () : ℕ) : ℚ)) ((r : ℚ) * Φ) hr hd2Q
    (le_trans hcost hθt) hθ
    (fun i j => le_trans (cost_sepW_le hD₁ne hd0 d₁ d₂ hd₁ hd₂ Dx Dy hDx hDy i j)
      (by
        have : ((r - 1 : ℕ) : ℚ) / (D₁ : ℚ) ≤ (((d₂ () : ℕ) : ℚ)) / (D₁ : ℚ) :=
          div_le_div_of_nonneg_right (by exact_mod_cast (by omega : r - 1 ≤ d₂ ())) hD₁Q.le
        linarith)) hS
  have hr2 : (r : ℚ) ≤ 2 * ((d₂ () : ℕ) : ℚ) := by
    have h1 : (1 : ℚ) ≤ ((d₂ () : ℕ) : ℚ) := by exact_mod_cast hd2N
    linarith
  obtain ⟨w, hw1, hw2⟩ := exists_w_of_branches hΦ0 hd2Q hrQ hr2 hor
  exact ⟨w, hw1, by linarith⟩

/-- **§13's conclusion in the form the recursion consumes.**

`hfac` is what the induction hypothesis supplies: for *any* bounded-order family realising a
separated representation of `P`, the two Wronskians' indices sum to at most `r·Φ`.  Then

    index P ≤ 1/ω + 2·max(Φ, q)        whenever  (d+1)·Φ ≤ q²·D₂.

Both `1/ω` and `Φ` are small in the intended regime, and neither mentions the representation
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
      mvGenWronskian Dx φ ≠ 0 → mvGenWronskian Dy ψ ≠ 0 →
      index d₁ α (mvGenWronskian Dx φ) + index d₂ β (mvGenWronskian Dy ψ)
        ≤ ((((r : ℚ) * Φ : ℚ)) : WithTop ℚ))
    (θ q : ℚ) (hθt : 1 / ω ≤ θ) (hq0 : 0 ≤ q)
    (hq : (((d₂ () : ℕ) : ℚ) + 1) * Φ ≤ q ^ 2 * (D₂ : ℚ))
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P) :
    θ ≤ 1 / ω + 2 * max Φ q := by
  obtain ⟨r, φ, ψ, Dx, Dy, hr, _, hDx, hDy, _, _, hPeq, hWx, hWy, hmain⟩ :=
    exists_family_index_le_of_rothGrowth o ω hω d₁ d₂ hg hlast hd0 hD₂ hd₂ α β P hP hdeg
  exact hmain Φ θ q hΦ0 (hfac r φ ψ Dx Dy hr hDx hDy hPeq hWx hWy) hθt hq0 hq hθ


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
      mvGenWronskian Dx φ ≠ 0 → mvGenWronskian Dy ψ ≠ 0 →
      index (fun j => r * d₁ j) α (mvGenWronskian Dx φ) ≤ ((εU : ℚ) : WithTop ℚ) ∧
        index (fun j => r * d₂ j) β (mvGenWronskian Dy ψ) ≤ ((εV : ℚ) : WithTop ℚ))
    (θ q : ℚ) (hθt : 1 / ω ≤ θ) (hq0 : 0 ≤ q)
    (hq : (((d₂ () : ℕ) : ℚ) + 1) * (εU + εV) ≤ q ^ 2 * (D₂ : ℚ))
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β) P) :
    θ ≤ 1 / ω + 2 * max (εU + εV) q :=
  index_le_of_rothGrowth_of_factor_bound o ω hω d₁ d₂ hg hlast hd0 hD₂ hd₂ α β P hP hdeg
    (εU + εV) hε
    (fun r φ ψ Dx Dy hr hDx hDy hPeq hWx hWy =>
      have h := hres r φ ψ Dx Dy hr hDx hDy hPeq hWx hWy
      factor_bound_of_rescaled (Nat.pos_iff_ne_zero.mp hr) d₁ d₂ α β Dx Dy φ ψ εU εV
        h.1 h.2)
    θ q hθt hq0 hq hθ

/-! ### Next

The chain runs from the induction hypothesis's literal shape to §13's conclusion, and **both
halves of `hres` are now supplied**:

* the `x` half by `index_rescaled_wronskian_le` — §6's Gauss, then `RothLemmaUniform` at
  `m − 1`, then `index_C_mul` to carry the bound back;
* the `y` half by `index_rescaled_wronskian_le_right`, which needs **no induction hypothesis
  at all**: the split-off group is one variable, so the relevant instance is
  `rothLemmaUniform_one`, and that is proved.

Both live in `QOU/Mathlib/RothInductionHypothesis.lean`.

What remains is the **recursion**: quantify the two halves' auxiliary data (`B`, `E`, the
denominators) uniformly in the family — `abs_coeff_det_pderivList_le` is what makes a uniform
`B` available — assemble `hres`, and iterate.

Provenance: §5, §6, §7, §11, §13 and §14 have all now been read directly and match, §11 and
§14 from the page scans (the PDF's OCR layer garbles exactly those two).  The `1/ω` bound was
the arc's own reconstruction and §11 confirmed it: `Γ_m`'s first clause is `RothGrowth` with
`ω = 1/t`.  ⚠ The reconstruction was `2/ω` until §13 was read line by line and its row term
turned out to be `(μ-1)/r_{m-1}`, numerator `μ - 1` — correction 24.

⚠ Two things that reading corrected: the constant is `c_m = 2^{m+1} − 3`, and what iterating
produces is `Θ_m ≤ c_m·t^{2^{−(m−1)}}` — an exponent, not a linear factor.  See the eleventh
correction in `RothLemmaStatement`. -/








end MvPolynomial
