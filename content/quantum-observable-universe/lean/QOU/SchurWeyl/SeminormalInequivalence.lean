import QOU.SchurWeyl.QJucysMurphyEigen
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.Polynomial.Roots

/-!
# QOU.SchurWeyl.SeminormalInequivalence — pairwise inequivalence of the `ρ_λ` (q-deformed)

**The second half of SW-5** (bean `qou-jfr8`).  Irreducibility of each `ρ_λ` is the range
statement `AlgHom.range (seminormalRep …) = ⊤`; this file starts the companion claim that the
family is **pairwise inequivalent** — `ρ_λ ≇ ρ_ν` for `λ ≠ ν` — which is what makes
`{ρ_λ : λ ⊢ n}` the *list* of irreducibles rather than merely a supply of them.

## This is the q-deformed statement, and it is not the one already in the corpus

`QOU.BraidKnot.SpechtClassification.specht_pairwise_noniso` proves pairwise non-isomorphism for
the **Specht modules over `k[S_n]` at `q = 1`**, as `Representation k (Perm (Fin n))`, by the
dominance-order route.  The object here is different: an **algebra** map
`Hecke ℝ q q⁻¹ n →ₐ[ℝ] Matrix (SYT μ) (SYT μ) ℝ` at generic `q`.  Neither statement implies the
other, and no dominance order is needed on this side — the `q`-Jucys–Murphy diagonalisation
(`seminormalRep_qJM`) exposes the shape directly in the spectrum.

The `q = 1` file is still the precedent for the *Lean shape*: it declares its own intertwiner
predicate rather than reaching for `FDRep`, to avoid `Module.Finite` plumbing before any
mathematical content is reachable.  `MatRepEquiv` below is the algebra-hom analogue.

## What is proved here, and what it does not give

`seminormalRep_not_matRepEquiv_of_contentCoshSum_ne` is a **conditional** separation: two shapes
whose content-cosh sums differ carry inequivalent representations.  It is exact and cheap — the
bar-symmetrised sum `Θ` is central, `ρ_λ(Θ)` is the *scalar* `cellContentCoshSum λ q`
(`seminormalRep_barSymJMSum`), and a scalar is a similarity invariant.

**It is not the unconditional statement.**  At a *fixed real* `q` the cosh-sum is a single
number, and nothing here rules out two distinct shapes colliding on it.  As Laurent polynomials
in `q` the sums differ — distinct shapes have distinct content multisets and the coefficients are
positive — so they can agree for at most finitely many `q`; but "at most finitely many" is not
"not at this one".

`contentCount_eq_of_matRepEquiv` closes that gap: an equivalence forces the two shapes to have
**the same number of cells of every content**.  The route is not the one the plan anticipated —
no per-generator eigenvalue multiset, no characteristic polynomial, no Newton identities.
Summing over `k` *first* makes the diagonal constant (the cell sweep), so `Σ_k L_k^m` acts by a
scalar for every `m` and the same `scalar_eq` applies verbatim; the family of scalars is then a
polynomial identity in disguise.

`youngDiagram_eq_of_contentCount_eq` then closes it, and needs neither Frobenius coordinates nor
an induction on the diagram: **each diagonal of a Young diagram is downward-closed**, so its
*length* already decides membership, and the diagonal lengths are exactly the content
multiplicities.

So `seminormalRep_not_matRepEquiv_of_ne` is **unconditional**: distinct shapes of the same size
carry inequivalent representations, with no hypothesis beyond `μ ≠ ν` and the genericity
`seminormalRep` already requires.  The conditional
`seminormalRep_not_matRepEquiv_of_contentCoshSum_ne` is kept as the cheap criterion it is — one
scalar, checkable per pair — but it is no longer the strongest statement here.

The unconditional claim is nonetheless *true*: `H_n(q)` over `ℝ` is semisimple whenever `q` is
not a root of unity of order `≤ n`, which `q ≠ 0` with `q ^ 2 ≠ 1` supplies, and the `ρ_λ` are
then a complete pairwise-inequivalent family.  What is open is the formalisation, not the fact.

Refs:
- [ram1997] Ram, *Seminormal representations of Weyl groups and Iwahori–Hecke algebras*,
  https://doi.org/10.1112/S0024611597000373
- [wenzl1988] Wenzl, *Hecke algebras of type `A_n` and subfactors* — semisimplicity away from
  roots of unity.

LaTeX label: `lem:seminormal-pairwise-inequivalent`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells SeminormalRep

/-! ## Equivalence of matrix representations -/

/-- **Two matrix representations of one algebra are equivalent** when an invertible change of
basis intertwines them.

Stated with an explicit inverse pair `S`, `T` rather than `IsUnit S`, because the index types
`ι` and `κ` differ: `S : Matrix κ ι R` is not square, so `IsUnit` does not apply and the two
one-sided identities are separate data.  Both are needed — `S * T = 1` is what forces the
scalar comparison below, and `T * S = 1` is what makes this a symmetric notion. -/
def MatRepEquiv {R A ι κ : Type*} [CommRing R] [Semiring A] [Algebra R A]
    [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]
    (ρ : A →ₐ[R] Matrix ι ι R) (ρ' : A →ₐ[R] Matrix κ κ R) : Prop :=
  ∃ (S : Matrix κ ι R) (T : Matrix ι κ R),
    S * T = 1 ∧ T * S = 1 ∧ ∀ x : A, ρ' x * S = S * ρ x

variable {R A ι κ : Type*} [CommRing R] [Semiring A] [Algebra R A]
  [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]

/-- **A scalar value is an equivalence invariant.**  If `x` is sent to a scalar matrix by both
representations, the two scalars agree.

This is the whole force of centrality: a central element goes to a scalar in every irreducible
block, and equivalent blocks cannot disagree about which scalar.  `Nonempty κ` is needed and is
not a formality — over the empty index type every matrix is `1`, so any two scalars would be
indistinguishable. -/
theorem MatRepEquiv.scalar_eq [Nonempty κ] {ρ : A →ₐ[R] Matrix ι ι R} {ρ' : A →ₐ[R] Matrix κ κ R}
    (h : MatRepEquiv ρ ρ') {x : A} {c c' : R}
    (hc : ρ x = c • (1 : Matrix ι ι R)) (hc' : ρ' x = c' • (1 : Matrix κ κ R)) : c' = c := by
  obtain ⟨S, T, hST, _, hint⟩ := h
  have key : c' • S = c • S := by
    have hx := hint x
    rw [hc, hc'] at hx
    rwa [Matrix.smul_mul, Matrix.one_mul, Matrix.mul_smul, Matrix.mul_one] at hx
  have h2 : c' • (1 : Matrix κ κ R) = c • (1 : Matrix κ κ R) := by
    calc c' • (1 : Matrix κ κ R) = c' • (S * T) := by rw [hST]
      _ = (c' • S) * T := (Matrix.smul_mul c' S T).symm
      _ = (c • S) * T := by rw [key]
      _ = c • (S * T) := Matrix.smul_mul c S T
      _ = c • (1 : Matrix κ κ R) := by rw [hST]
  have := congrFun (congrFun h2 (Classical.arbitrary κ)) (Classical.arbitrary κ)
  simpa [Matrix.one_apply_eq] using this

/-- **An equivalence conjugates one representation into the other.**  The intertwining identity
`ρ' x * S = S * ρ x` becomes `ρ' x = S * ρ x * T` once `S * T = 1` is used on the right. -/
theorem MatRepEquiv.conj_eq {ρ : A →ₐ[R] Matrix ι ι R} {ρ' : A →ₐ[R] Matrix κ κ R}
    {S : Matrix κ ι R} {T : Matrix ι κ R} (hST : S * T = 1)
    (hint : ∀ x : A, ρ' x * S = S * ρ x) (x : A) : ρ' x = S * ρ x * T := by
  calc ρ' x = ρ' x * (S * T) := by rw [hST, Matrix.mul_one]
    _ = (ρ' x * S) * T := (Matrix.mul_assoc _ _ _).symm
    _ = (S * ρ x) * T := by rw [hint x]

/-- **The character is an equivalence invariant.**  `tr ρ'(x) = tr ρ(x)` for every `x`.

This is the workhorse for *un*conditional separation, and it is strictly stronger than
`scalar_eq`: it applies to every algebra element, not only those landing on scalars, so it can
compare whole spectra rather than one number.  Note it needs only `S * T = 1` and `T * S = 1` —
no genericity, no algebra structure beyond the intertwining. -/
theorem MatRepEquiv.trace_eq {ρ : A →ₐ[R] Matrix ι ι R} {ρ' : A →ₐ[R] Matrix κ κ R}
    (h : MatRepEquiv ρ ρ') (x : A) : (ρ' x).trace = (ρ x).trace := by
  obtain ⟨S, T, hST, hTS, hint⟩ := h
  calc (ρ' x).trace = (S * ρ x * T).trace := by rw [MatRepEquiv.conj_eq hST hint x]
    _ = (T * (S * ρ x)).trace := Matrix.trace_mul_comm _ _
    _ = ((T * S) * ρ x).trace := by rw [Matrix.mul_assoc]
    _ = (ρ x).trace := by rw [hTS, Matrix.one_mul]

/-- **Equivalent representations have equal dimension.**  The `x = 1` instance of `trace_eq`,
read through `CharZero` to land in `ℕ`. -/
theorem MatRepEquiv.card_eq [CharZero R] {ρ : A →ₐ[R] Matrix ι ι R} {ρ' : A →ₐ[R] Matrix κ κ R}
    (h : MatRepEquiv ρ ρ') : Fintype.card κ = Fintype.card ι := by
  have := h.trace_eq 1
  rw [map_one, map_one, Matrix.trace_one, Matrix.trace_one] at this
  exact_mod_cast this

/-! ## The seminormal application -/

/-- **Shapes with different content-cosh sums carry inequivalent representations.**

`Θ = barSymJMSum` is central, and `seminormalRep_barSymJMSum` evaluates it to the scalar
`Σ_{c ∈ μ} (q^{2c} + q^{−2c})`.  By `MatRepEquiv.scalar_eq` an equivalence would force the two
sums to agree.

**Read the hypothesis, not the name.**  This separates exactly the pairs of shapes whose sums
differ *at this `q`*.  It is not `μ ≠ ν → ρ_μ ≇ ρ_ν`; see the module docstring for why one
scalar cannot deliver that, and what does. -/
theorem seminormalRep_not_matRepEquiv_of_contentCoshSum_ne {μ ν : YoungDiagram}
    (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hμ : μ.cells.card = n + 1) (hν : ν.cells.card = n + 1)
    (hne : (∑ c ∈ ν.cells, (q ^ (2 * cellContent c) + q ^ (-(2 * cellContent c))))
         ≠ (∑ c ∈ μ.cells, (q ^ (2 * cellContent c) + q ^ (-(2 * cellContent c))))) :
    ¬ MatRepEquiv (seminormalRep q hq0 hq2 n hμ) (seminormalRep q hq0 hq2 n hν) := by
  intro h
  exact hne (h.scalar_eq (seminormalRep_barSymJMSum q hq0 hq2 n hμ)
    (seminormalRep_barSymJMSum q hq0 hq2 n hν))


/-! ## Stage 2 — the whole power-sum family, not one scalar

`scalar_eq` above compares a *single* number and is therefore conditional.  What removes the
condition is that the same argument runs for **every** power `m`: the element
`Σ_k L_k^m` is again central-acting (its diagonal is constant, by the cell sweep), so an
equivalence forces the content power sums to agree at every `m`.

That family is what pins the shape.  Writing `t = q^{2m}`, the identity says the two content
generating functions `Σ_{c ∈ μ} t^c` and `Σ_{c ∈ ν} t^c` agree at every point of
`{q^2, q^4, q^6, …}`.  Because `q ≠ 0` and `q^2 ≠ 1`, those points are **pairwise distinct** —
`q^2` is positive and `≠ 1`, so its powers are strictly monotone — so the difference is a Laurent
polynomial with infinitely many roots, hence identically zero, hence the two content **multisets**
coincide.  This is the step that a single scalar cannot reach, and it uses the genericity
hypothesis for something other than `zpow` injectivity.
-/

/-- **The `m`-th Murphy power sum acts by the content power sum.**  Generalises
`seminormalRep_barSymJMSum` from the bar-symmetrised `m = ±1` combination to every `m`, by the
same two ingredients: Ram 4.1 makes each `ρ(L_k)` diagonal, and `sum_cellOf_range` makes the
diagonal constant because summing over `k` sweeps every cell exactly once. -/
theorem seminormalRep_jmPowSum {μ : YoungDiagram} (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) (m : ℕ) :
    seminormalRep q hq0 hq2 n hN (∑ k ∈ Finset.range (n + 1), (qJM ℝ q q⁻¹ n k) ^ m)
      = (∑ c ∈ μ.cells, (q ^ (2 * cellContent c)) ^ m)
          • (1 : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ) := by
  classical
  rw [map_sum]
  have hterm : ∀ k ∈ Finset.range (n + 1),
      seminormalRep q hq0 hq2 n hN ((qJM ℝ q q⁻¹ n k) ^ m)
        = Matrix.diagonal (fun T : StandardYoungTableau μ =>
            (q ^ (2 * cellContent (cellOf T (k + 1)))) ^ m) := by
    intro k hk
    rw [Finset.mem_range] at hk
    rw [map_pow, seminormalRep_qJM q hq0 hq2 n hN k (by omega), jmDiagVal, Matrix.diagonal_pow]
    rfl
  rw [Finset.sum_congr rfl hterm]
  ext T U
  simp only [Matrix.sum_apply, Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]
  by_cases h : T = U
  · subst h
    simp only [Matrix.diagonal_apply_eq, if_pos, mul_one]
    exact sum_cellOf_range T hN (fun c => (q ^ (2 * cellContent c)) ^ m)
  · simp only [Matrix.diagonal_apply_ne _ h, if_neg h, mul_zero, Finset.sum_const_zero]

/-- **An equivalence forces every content power sum to agree.**  The unconditional handle on
pairwise inequivalence: not one number, but a whole family indexed by `m`. -/
theorem contentPowSum_eq_of_matRepEquiv {μ ν : YoungDiagram}
    (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hμ : μ.cells.card = n + 1) (hν : ν.cells.card = n + 1)
    (h : MatRepEquiv (seminormalRep q hq0 hq2 n hμ) (seminormalRep q hq0 hq2 n hν)) (m : ℕ) :
    (∑ c ∈ ν.cells, (q ^ (2 * cellContent c)) ^ m)
      = ∑ c ∈ μ.cells, (q ^ (2 * cellContent c)) ^ m :=
  h.scalar_eq (seminormalRep_jmPowSum q hq0 hq2 n hμ m) (seminormalRep_jmPowSum q hq0 hq2 n hν m)


/-! ### The roots core — equal power sums at every `m` force equal exponent multisets

Shape-independent, and stated with `ℕ` exponents so that no shift is needed here; the Young-diagram
contents are shifted into `ℕ` at the call site.  The infinitude of evaluation points is what does
the work, and it comes from `0 < t`, `t ≠ 1`.
-/


/-- `m ↦ t ^ m` is injective for a positive `t ≠ 1`. -/
theorem pow_right_injective_of_pos_of_ne_one {t : ℝ} (ht0 : 0 < t) (ht1 : t ≠ 1) :
    Function.Injective (fun m : ℕ => t ^ m) := by
  intro a b hab
  have hlog : (a : ℝ) * Real.log t = (b : ℝ) * Real.log t := by
    rw [← Real.log_pow, ← Real.log_pow]
    exact congrArg Real.log hab
  have hne : Real.log t ≠ 0 := Real.log_ne_zero_of_pos_of_ne_one ht0 ht1
  exact_mod_cast mul_right_cancel₀ hne hlog

/-- A real polynomial vanishing at every `t ^ m` is the zero polynomial. -/
theorem poly_eq_zero_of_eval_pow {t : ℝ} (ht0 : 0 < t) (ht1 : t ≠ 1)
    (p : Polynomial ℝ) (h : ∀ m : ℕ, p.eval (t ^ m) = 0) : p = 0 := by
  refine p.eq_zero_of_infinite_isRoot ?_
  exact Set.infinite_of_injective_forall_mem
    (pow_right_injective_of_pos_of_ne_one ht0 ht1) (fun m => h m)

/-- The `d`-th coefficient of `∑_{i ∈ s} X ^ (f i)` counts the `i` with `f i = d`. -/
theorem coeff_sum_X_pow {ι : Type*} (s : Finset ι) (f : ι → ℕ) (d : ℕ) :
    (∑ i ∈ s, (Polynomial.X : Polynomial ℝ) ^ (f i)).coeff d
      = ((s.filter (fun i => f i = d)).card : ℝ) := by
  classical
  rw [Polynomial.finset_sum_coeff]
  simp only [Polynomial.coeff_X_pow]
  have hflip : ∀ i ∈ s, (if d = f i then (1 : ℝ) else 0) = (if f i = d then (1 : ℝ) else 0) := by
    intro i _
    by_cases h : f i = d
    · simp [h]
    · simp [h, Ne.symm h]
  rw [Finset.sum_congr rfl hflip, Finset.sum_boole]

/-- **Equal power sums at every `m` force equal exponent multisets.** -/
theorem card_filter_eq_of_powSum_eq {ι κ : Type*} {sμ : Finset ι} {sν : Finset κ}
    {f : ι → ℕ} {g : κ → ℕ} {t : ℝ} (ht0 : 0 < t) (ht1 : t ≠ 1)
    (h : ∀ m : ℕ, ∑ i ∈ sμ, (t ^ f i) ^ m = ∑ j ∈ sν, (t ^ g j) ^ m) (d : ℕ) :
    (sμ.filter (fun i => f i = d)).card = (sν.filter (fun j => g j = d)).card := by
  classical
  set p : Polynomial ℝ :=
    (∑ i ∈ sμ, (Polynomial.X : Polynomial ℝ) ^ (f i))
      - (∑ j ∈ sν, (Polynomial.X : Polynomial ℝ) ^ (g j)) with hpdef
  have hp : p = 0 := by
    refine poly_eq_zero_of_eval_pow ht0 ht1 p (fun m => ?_)
    rw [hpdef]
    simp only [Polynomial.eval_sub, Polynomial.eval_finset_sum, Polynomial.eval_pow,
      Polynomial.eval_X]
    have hswap : ∀ u : ℕ, (t ^ m) ^ u = (t ^ u) ^ m := by
      intro u; rw [← pow_mul, ← pow_mul, Nat.mul_comm]
    simp only [hswap]
    rw [h m, sub_self]
  have hc := congrArg (fun r : Polynomial ℝ => r.coeff d) hp
  simp only [hpdef, Polynomial.coeff_sub, Polynomial.coeff_zero, coeff_sum_X_pow] at hc
  have hreal : ((sμ.filter (fun i => f i = d)).card : ℝ)
      = ((sν.filter (fun j => g j = d)).card : ℝ) := by linarith
  exact_mod_cast hreal


/-! ### The Young-diagram bridge: shifting contents into `ℕ` -/

/-- **A cell's row index is below the cell count.**  The cells `(0,j), …, (i,j)` all lie in `μ`
by up-left closure and are distinct, so there are at least `i + 1` of them.  This is what bounds
the contents from below and lets them be shifted into `ℕ`. -/
theorem row_lt_card {μ : YoungDiagram} {i j : ℕ} (h : (i, j) ∈ μ) : i < μ.cells.card := by
  classical
  have hsub : ((Finset.range (i + 1)).image (fun k => (k, j))) ⊆ μ.cells := by
    intro c hc
    simp only [Finset.mem_image, Finset.mem_range] at hc
    obtain ⟨k, hk, rfl⟩ := hc
    rw [YoungDiagram.mem_cells]
    exact μ.up_left_mem (by omega) (le_refl j) h
  have hcard : ((Finset.range (i + 1)).image (fun k => (k, j))).card = i + 1 := by
    rw [Finset.card_image_of_injective _ (fun a b hab => by simpa using hab), Finset.card_range]
  have := Finset.card_le_card hsub
  omega

/-- Contents are bounded below by `-n` when the diagram has `n + 1` cells. -/
theorem neg_le_cellContent {μ : YoungDiagram} {n : ℕ} (hN : μ.cells.card = n + 1)
    {c : ℕ × ℕ} (hc : c ∈ μ.cells) : -(n : ℤ) ≤ cellContent c := by
  have hmem : (c.1, c.2) ∈ μ := by rw [← YoungDiagram.mem_cells]; simpa using hc
  have := row_lt_card hmem
  rw [hN] at this
  simp only [cellContent]
  omega

/-- The content of a cell, shifted into `ℕ` by the row bound. -/
noncomputable def shiftedContent (n : ℕ) (c : ℕ × ℕ) : ℕ := (cellContent c + n).toNat

theorem shiftedContent_cast {μ : YoungDiagram} {n : ℕ} (hN : μ.cells.card = n + 1)
    {c : ℕ × ℕ} (hc : c ∈ μ.cells) :
    (shiftedContent n c : ℤ) = cellContent c + n := by
  have := neg_le_cellContent hN hc
  simp only [shiftedContent]
  omega

/-- `t ^ shiftedContent` factors as `q ^ (2·content)` times the shift, with `t = q ^ 2`. -/
theorem pow_shiftedContent {μ : YoungDiagram} {n : ℕ} (hN : μ.cells.card = n + 1)
    {q : ℝ} (hq0 : q ≠ 0) {c : ℕ × ℕ} (hc : c ∈ μ.cells) :
    (q ^ 2 : ℝ) ^ (shiftedContent n c) = q ^ (2 * cellContent c) * (q ^ 2 : ℝ) ^ n := by
  have hq2 : (q ^ 2 : ℝ) ≠ 0 := pow_ne_zero 2 hq0
  have hz : ((q ^ 2 : ℝ)) ^ (shiftedContent n c) = ((q ^ 2 : ℝ)) ^ ((shiftedContent n c : ℤ)) := by
    rw [zpow_natCast]
  rw [hz, shiftedContent_cast hN hc, zpow_add₀ hq2, zpow_natCast]
  congr 1
  rw [zpow_mul]
  rfl


/-- **An equivalence forces the two shapes to have the same content multiset.**

The unconditional handle, assembled: `contentPowSum_eq_of_matRepEquiv` gives equality of the
content power sums at *every* `m`; shifting the contents into `ℕ` turns those into honest
polynomial evaluations at `t = q ^ 2`, `t ^ 2`, `t ^ 3`, …; and `card_filter_eq_of_powSum_eq`
converts infinitely many coincidences into equality of coefficients — that is, of the number of
cells of each content.

The genericity hypothesis is doing a *second* job here.  Elsewhere in this arc `q ^ 2 ≠ 1` is
used for injectivity of `c ↦ q ^ (2c)`; here it is what makes the evaluation points
`q ^ 2, q ^ 4, …` pairwise distinct, so that the difference polynomial has infinitely many roots.

What remains between this and `μ = ν` is the classical fact that a Young diagram is determined by
its content multiset — stated in the module header as the one open step, and deliberately not
assumed here. -/
theorem contentCount_eq_of_contentPowSum_eq {μ ν : YoungDiagram}
    (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hμ : μ.cells.card = n + 1) (hν : ν.cells.card = n + 1)
    (hpow : ∀ m : ℕ, (∑ c ∈ ν.cells, (q ^ (2 * cellContent c)) ^ m)
      = ∑ c ∈ μ.cells, (q ^ (2 * cellContent c)) ^ m) (d : ℤ) :
    (ν.cells.filter (fun c => cellContent c = d)).card
      = (μ.cells.filter (fun c => cellContent c = d)).card := by
  classical
  have ht0 : (0 : ℝ) < q ^ 2 := lt_of_le_of_ne (sq_nonneg q) (Ne.symm (pow_ne_zero 2 hq0))
  by_cases hd : 0 ≤ d + (n : ℤ)
  · have hshift : ∀ m : ℕ,
        ∑ c ∈ ν.cells, ((q ^ 2 : ℝ) ^ shiftedContent n c) ^ m
          = ∑ c ∈ μ.cells, ((q ^ 2 : ℝ) ^ shiftedContent n c) ^ m := by
      intro m
      have hν' : ∀ c ∈ ν.cells, ((q ^ 2 : ℝ) ^ shiftedContent n c) ^ m
          = (q ^ (2 * cellContent c)) ^ m * ((q ^ 2 : ℝ) ^ n) ^ m := by
        intro c hc; rw [pow_shiftedContent hν hq0 hc, mul_pow]
      have hμ' : ∀ c ∈ μ.cells, ((q ^ 2 : ℝ) ^ shiftedContent n c) ^ m
          = (q ^ (2 * cellContent c)) ^ m * ((q ^ 2 : ℝ) ^ n) ^ m := by
        intro c hc; rw [pow_shiftedContent hμ hq0 hc, mul_pow]
      rw [Finset.sum_congr rfl hν', Finset.sum_congr rfl hμ', ← Finset.sum_mul, ← Finset.sum_mul,
        hpow m]
    have hcount := card_filter_eq_of_powSum_eq ht0 hq2 hshift ((d + (n : ℤ)).toNat)
    have hre : ∀ (σ : YoungDiagram), σ.cells.card = n + 1 →
        σ.cells.filter (fun c => shiftedContent n c = (d + (n : ℤ)).toNat)
          = σ.cells.filter (fun c => cellContent c = d) := by
      intro σ hσ
      refine Finset.filter_congr (fun c hc => ?_)
      have hcast := shiftedContent_cast hσ hc
      constructor
      · intro hh; omega
      · intro hh; omega
    rwa [hre ν hν, hre μ hμ] at hcount
  · have hempty : ∀ (σ : YoungDiagram), σ.cells.card = n + 1 →
        σ.cells.filter (fun c => cellContent c = d) = ∅ := by
      intro σ hσ
      refine Finset.filter_eq_empty_iff.mpr (fun {c} hc => ?_)
      have := neg_le_cellContent hσ hc
      omega
    rw [hempty ν hν, hempty μ hμ]

/-- **An equivalence forces equal content counts.**  The original form of the previous theorem,
now a corollary of it: `MatRepEquiv` is only ever used to supply the power-sum equality. -/
theorem contentCount_eq_of_matRepEquiv {μ ν : YoungDiagram}
    (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hμ : μ.cells.card = n + 1) (hν : ν.cells.card = n + 1)
    (h : MatRepEquiv (seminormalRep q hq0 hq2 n hμ) (seminormalRep q hq0 hq2 n hν)) (d : ℤ) :
    (ν.cells.filter (fun c => cellContent c = d)).card
      = (μ.cells.filter (fun c => cellContent c = d)).card :=
  contentCount_eq_of_contentPowSum_eq q hq0 hq2 n hμ hν
    (fun m => contentPowSum_eq_of_matRepEquiv q hq0 hq2 n hμ hν h m) d


/-! ### Content multiset determines the diagram

The last step, and it does not need Frobenius coordinates or an induction on the diagram.  The
observation that collapses it: **each diagonal of a Young diagram is downward-closed**, so its
*length* already decides membership.  Writing `diagIndex (i,j) = min i j` for the position of a
cell along its own diagonal, a cell lies in `μ` exactly when its diagonal index is below the
length of that diagonal — and the diagonal lengths are precisely the content multiplicities.

So equal content counts give equal diagonal lengths, which give the same membership predicate,
which is the same diagram.
-/

/-- A downward-closed finite set of naturals is an initial segment. -/
theorem mem_iff_lt_card_of_downward {S : Finset ℕ}
    (hdc : ∀ m ∈ S, ∀ k, k ≤ m → k ∈ S) (k : ℕ) : k ∈ S ↔ k < S.card := by
  constructor
  · intro hk
    have hsub : Finset.range (k + 1) ⊆ S := by
      intro x hx
      rw [Finset.mem_range] at hx
      exact hdc k hk x (by omega)
    have := Finset.card_le_card hsub
    rw [Finset.card_range] at this
    omega
  · intro hk
    by_contra hnot
    have hsub : S ⊆ Finset.range k := by
      intro x hx
      rw [Finset.mem_range]
      by_contra hge
      exact hnot (hdc x hx k (by omega))
    have := Finset.card_le_card hsub
    rw [Finset.card_range] at this
    omega

/-- The position of a cell along its own diagonal, counted from the boundary of the quadrant. -/
def diagIndex (c : ℕ × ℕ) : ℕ := min c.1 c.2

/-- A cell is determined by its content together with its diagonal index. -/
theorem cell_eq_of_content_of_diagIndex {c c' : ℕ × ℕ}
    (hc : cellContent c = cellContent c') (hi : diagIndex c = diagIndex c') : c = c' := by
  obtain ⟨i, j⟩ := c
  obtain ⟨i', j'⟩ := c'
  simp only [cellContent, diagIndex] at hc hi
  have h1 : i = i' ∧ j = j' := by omega
  rw [h1.1, h1.2]

/-- The `d`-diagonal of `μ` — the cells of content `d`.  Its cardinality is the multiplicity of
`d` in the content multiset. -/
noncomputable def diagOf (μ : YoungDiagram) (d : ℤ) : Finset (ℕ × ℕ) := by
  classical
  exact μ.cells.filter (fun c => cellContent c = d)

theorem mem_diagOf {μ : YoungDiagram} {d : ℤ} {c : ℕ × ℕ} :
    c ∈ diagOf μ d ↔ c ∈ μ.cells ∧ cellContent c = d := by
  classical
  simp [diagOf]

/-- **Diagonals are downward-closed.**  Stepping one cell up-and-left along a diagonal stays in
the diagram (up-left closure), keeps the content, and drops the diagonal index by one. -/
theorem diagIndex_image_downward (μ : YoungDiagram) (d : ℤ) :
    ∀ m ∈ (diagOf μ d).image diagIndex, ∀ k, k ≤ m → k ∈ (diagOf μ d).image diagIndex := by
  classical
  intro m hm k hk
  simp only [Finset.mem_image] at hm ⊢
  obtain ⟨c, hc, rfl⟩ := hm
  obtain ⟨hcell, hcont⟩ := mem_diagOf.mp hc
  obtain ⟨i, j⟩ := c
  have hmem : (i, j) ∈ μ := by rw [← YoungDiagram.mem_cells]; simpa using hcell
  simp only [diagIndex] at hk
  set t : ℕ := min i j - k with htdef
  refine ⟨(i - t, j - t), ?_, ?_⟩
  · refine mem_diagOf.mpr ⟨?_, ?_⟩
    · rw [YoungDiagram.mem_cells]
      exact μ.up_left_mem (by omega) (by omega) hmem
    · simp only [cellContent] at hcont ⊢
      omega
  · simp only [diagIndex]
    omega

/-- **Membership is decided by the diagonal length.**  A cell lies in `μ` exactly when its
diagonal index is below the number of cells of its content. -/
theorem mem_iff_diagIndex_lt (μ : YoungDiagram) (i j : ℕ) :
    ((i, j) ∈ μ) ↔ diagIndex (i, j) < (diagOf μ (cellContent (i, j))).card := by
  classical
  set d : ℤ := cellContent (i, j) with hd
  have hinj : Set.InjOn diagIndex (diagOf μ d) := by
    intro a ha b hb hab
    exact cell_eq_of_content_of_diagIndex
      (((mem_diagOf.mp ha).2).trans ((mem_diagOf.mp hb).2).symm) hab
  have hcard : ((diagOf μ d).image diagIndex).card = (diagOf μ d).card :=
    Finset.card_image_of_injOn hinj
  have hiff := mem_iff_lt_card_of_downward (diagIndex_image_downward μ d) (diagIndex (i, j))
  rw [hcard] at hiff
  rw [← hiff]
  simp only [Finset.mem_image]
  constructor
  · intro hmem
    exact ⟨(i, j), mem_diagOf.mpr ⟨by rw [YoungDiagram.mem_cells]; exact hmem, rfl⟩, rfl⟩
  · rintro ⟨c, hc, hci⟩
    obtain ⟨hcell, hcont⟩ := mem_diagOf.mp hc
    have : c = (i, j) := cell_eq_of_content_of_diagIndex (by rw [hcont, hd]) hci
    subst this
    rw [← YoungDiagram.mem_cells]
    simpa using hcell

/-- **A Young diagram is determined by its content multiset.**  Equal content counts give equal
diagonal lengths, and `mem_iff_diagIndex_lt` turns those into the same membership predicate. -/
theorem youngDiagram_eq_of_contentCount_eq {μ ν : YoungDiagram}
    (h : ∀ d : ℤ, (diagOf μ d).card = (diagOf ν d).card) : μ = ν := by
  ext c
  obtain ⟨i, j⟩ := c
  rw [YoungDiagram.mem_cells, YoungDiagram.mem_cells,
    mem_iff_diagIndex_lt μ i j, mem_iff_diagIndex_lt ν i j, h]


/-! ### The unconditional statement -/

/-- **Pairwise inequivalence of the `q`-deformed seminormal representations — unconditional.**

Distinct shapes of the same size carry inequivalent representations.  No hypothesis on the shapes
beyond `μ ≠ ν`, and none on `q` beyond the genericity `seminormalRep` already requires.

The chain, all sorry-free: an equivalence makes `Σ_k L_k^m` act by the same scalar for every `m`
(`contentPowSum_eq_of_matRepEquiv`); that family of coincidences is a polynomial identity in
disguise, because `q ^ 2 ≠ 1` makes the evaluation points `q^2, q^4, …` distinct
(`contentCount_eq_of_matRepEquiv`); and a Young diagram is determined by its content multiset,
because its diagonals are downward-closed (`youngDiagram_eq_of_contentCount_eq`).

Together with irreducibility this is what makes `{ρ_λ : λ ⊢ n}` the *list* of irreducibles of
`H_n(q)` rather than merely a supply of them — the second half of SW-5 (bean `qou-jfr8`). -/
theorem seminormalRep_not_matRepEquiv_of_ne {μ ν : YoungDiagram}
    (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hμ : μ.cells.card = n + 1) (hν : ν.cells.card = n + 1) (hne : μ ≠ ν) :
    ¬ MatRepEquiv (seminormalRep q hq0 hq2 n hμ) (seminormalRep q hq0 hq2 n hν) := by
  classical
  intro h
  refine hne (youngDiagram_eq_of_contentCount_eq (fun d => ?_))
  have hc := contentCount_eq_of_matRepEquiv q hq0 hq2 n hμ hν h d
  simpa [diagOf] using hc.symm

/-- **Equal content power sums force equal diagrams.**  The scalar-level form of
`seminormalRep_not_matRepEquiv_of_ne`, with no representation in the statement at all: if the
central Murphy power sums take the same value on two shapes of the same size, the shapes coincide.

This is the form a *product-map* argument needs.  `seminormalRep_not_matRepEquiv_of_ne` answers
"are these two blocks isomorphic"; assembling `⊕_λ ρ_λ` instead needs "do the block scalars
separate the index set", which is this. -/
theorem youngDiagram_eq_of_contentPowSum_eq {μ ν : YoungDiagram}
    (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hμ : μ.cells.card = n + 1) (hν : ν.cells.card = n + 1)
    (hpow : ∀ m : ℕ, (∑ c ∈ ν.cells, (q ^ (2 * cellContent c)) ^ m)
      = ∑ c ∈ μ.cells, (q ^ (2 * cellContent c)) ^ m) :
    μ = ν := by
  classical
  refine youngDiagram_eq_of_contentCount_eq (fun d => ?_)
  have hc := contentCount_eq_of_contentPowSum_eq q hq0 hq2 n hμ hν hpow d
  simpa [diagOf] using hc.symm

end QOU.SchurWeyl
