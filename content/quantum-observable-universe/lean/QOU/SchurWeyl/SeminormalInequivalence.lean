import QOU.SchurWeyl.QJucysMurphyEigen

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
"not at this one".  The unconditional route needs the eigenvalue **multiset** of each `ρ(L_k)`
rather than one scalar; that is the file's tracked residual (bean `qou-jfr8`).

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

end QOU.SchurWeyl
