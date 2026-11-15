import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.LinearAlgebra.BilinearMap

/-!
# QOU.QuantumGeometry.q_codifferential_formula — Closed formula for δ_q

The formal adjoint of `d_q` with respect to the Webster inner product is
`δ_q = q⁻¹ δ + (1 - q⁻¹) L_ξ* ∘ ι_ξ`, characterised by the adjoint relation
`⟨d_q α, β⟩_θ = ⟨α, δ_q β⟩_θ`.

Works over an arbitrary commutative ring `R` (e.g. `ℤ`, `ℤ[q, q⁻¹]`, `ℝ`).
The substrate parameter `q` is taken as a unit in `R`.

LaTeX label: `prop:q-codifferential-formula`

## Form of the statement — read this before citing the file

**This file declares no `axiom`.** The contact-manifold data is bundled into
a `structure ContactFormAlgebra R F`, and the results below are theorems
about *every* such structure. The earlier version of this file asserted the
same content as **13 standalone axioms** over an opaque `axiom DiffForm :
Type u`; that form is strictly weaker, because a statement about one opaque
constant is not falsifiable — there is nothing to instantiate it at.

**No *geometric* `ContactFormAlgebra` is constructed here.** That is the
honest residual gap, and it is visible in every signature below: the theorems
are conditional on being handed such a structure. `#print axioms` reads clean
because the gap now lives in the *hypotheses* rather than in the axiom list —
which is the point of the change, but is not the same thing as the geometry
having been built. Building one (the Tanaka–Webster connection on a strictly
pseudoconvex CR manifold, or the Markov-trace pairing over `ℤ[q,q⁻¹]`) is
separate work.

What *is* constructed is `ContactFormAlgebra.degenerate`, the zero-pairing
model over any `R`-module. It exists to discharge two questions a reader
should ask of a conditional result: the structure is consistent, so the
theorems are not vacuous; and its pairing is degenerate, which is what makes
it the counterexample below.

## What the previous axiomatisation got wrong

`axiom adjoint_exists_unique'` asserted that **every** function
`L : DiffForm R → DiffForm R` has a unique adjoint. That is too strong, and
`ContactFormAlgebra.additive_of_hasAdjoint` below makes the failure explicit:
the defining relation `⟨L α, β⟩ = ⟨α, L* β⟩` forces `α ↦ ⟨L α, β⟩` to be
additive, because the right-hand side is additive in `α` by bilinearity of
the pairing. So assuming an adjoint for *arbitrary* `L` forces the pairing to
see every function — including wildly non-additive ones — as additive. The
Tanaka–Webster statement is about **linear** operators; the fields below are
typed `F →ₗ[R] F` accordingly, and the existence half of the old axiom is not
needed at all, since `δq` is exhibited rather than merely asserted to exist.

Uniqueness is recovered as `δq_unique`, under the hypothesis it actually
needs: non-degeneracy of the pairing. The old axiom asserted uniqueness with
no such hypothesis, which is false for a degenerate pairing — the identically
zero pairing satisfies bilinearity and admits every function as an adjoint.

## References
- [leitner2026] Ch. 2, §geometric-interpretations

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over `ℤ`).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.QuantumGeometry

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over `ℤ`).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ

def q_param : R_q := LaurentPolynomial.T 1

def q_inv_param : R_q := LaurentPolynomial.T (-1)

end

universe u v

variable {R : Type u} [CommRing R] {F : Type v} [AddCommGroup F] [Module R F]

/-! ## The contact-form algebra

The differential-form algebra of a contact manifold, as far as the
codifferential formula needs it: an `R`-module `F` carrying a bilinear
Webster pairing and six linear geometric operators, with the three
adjointness relations that relate them.

Three things that were separate axioms in the previous version are now
carried by Mathlib's own structures and cost nothing:

* `DiffForm` being an `R`-module — the `[AddCommGroup F] [Module R F]`
  binders above;
* left- and right-linearity of `⟨·,·⟩_θ` — the type `F →ₗ[R] F →ₗ[R] R`,
  i.e. `LinearMap.BilinForm`, is bilinear *by construction*, so the two
  linearity axioms and the four lemmas the old proof derived from them
  (`hzl`, `hzr`, `hsl`, `hsr`) are all discharged by `map_add` / `map_smul`;
* linearity of the six operators — the type `F →ₗ[R] F`. -/
structure ContactFormAlgebra (R : Type u) [CommRing R]
    (F : Type v) [AddCommGroup F] [Module R F] where
  /-- The Webster inner product `⟨·,·⟩_θ`, valued in `R`. Bilinear by construction. -/
  inner : F →ₗ[R] F →ₗ[R] R
  /-- The classical exterior derivative `d`. -/
  d : F →ₗ[R] F
  /-- The classical codifferential `δ`, the formal adjoint of `d`. -/
  δ : F →ₗ[R] F
  /-- The Reeb Lie derivative `L_ξ`. -/
  lieReeb : F →ₗ[R] F
  /-- The adjoint Reeb derivative `L_ξ*`. -/
  lieReebStar : F →ₗ[R] F
  /-- The interior product `ι_ξ`. -/
  iotaReeb : F →ₗ[R] F
  /-- The contact-form wedge `θ ∧ (·)`. -/
  thetaWedge : F →ₗ[R] F
  /-- `δ` is the formal adjoint of `d`. -/
  δ_adjoint_d : ∀ α β : F, inner (d α) β = inner α (δ β)
  /-- `ι_ξ` is the formal adjoint of `θ ∧ (·)`. -/
  iota_adjoint_theta : ∀ α β : F, inner (thetaWedge α) β = inner α (iotaReeb β)
  /-- `L_ξ*` is the formal adjoint of `L_ξ`. -/
  lieStar_adjoint_lie : ∀ α β : F, inner (lieReeb α) β = inner α (lieReebStar β)

namespace ContactFormAlgebra

variable (A : ContactFormAlgebra R F)

/-- The `q`-exterior derivative `d_q = q⁻¹ d + (1 - q⁻¹) θ ∧ L_ξ`.

    This was `axiom d_q` plus `axiom d_q_decomposition'` in the previous
    version: an opaque operator, plus an axiom saying what it equals. It is a
    *definition*, so the decomposition is now `rfl` and both axioms are gone. -/
def dq (q : Rˣ) : F →ₗ[R] F :=
  ((q⁻¹ : Rˣ) : R) • A.d + (1 - ((q⁻¹ : Rˣ) : R)) • (A.thetaWedge ∘ₗ A.lieReeb)

/-- The `q`-codifferential `δ_q = q⁻¹ δ + (1 - q⁻¹) L_ξ* ∘ ι_ξ`. -/
def δq (q : Rˣ) : F →ₗ[R] F :=
  ((q⁻¹ : Rˣ) : R) • A.δ + (1 - ((q⁻¹ : Rˣ) : R)) • (A.lieReebStar ∘ₗ A.iotaReeb)

theorem dq_apply (q : Rˣ) (α : F) :
    A.dq q α = ((q⁻¹ : Rˣ) : R) • A.d α
      + (1 - ((q⁻¹ : Rˣ) : R)) • A.thetaWedge (A.lieReeb α) := rfl

theorem δq_apply (q : Rˣ) (β : F) :
    A.δq q β = ((q⁻¹ : Rˣ) : R) • A.δ β
      + (1 - ((q⁻¹ : Rˣ) : R)) • A.lieReebStar (A.iotaReeb β) := rfl

/-- `θ ∧ L_ξ` and `L_ξ* ∘ ι_ξ` are adjoint — the composite of the two
    adjointness fields, and the step the closed formula turns on. -/
theorem thetaLie_adjoint (α β : F) :
    A.inner (A.thetaWedge (A.lieReeb α)) β
      = A.inner α (A.lieReebStar (A.iotaReeb β)) := by
  rw [A.iota_adjoint_theta, A.lieStar_adjoint_lie]

/-- **Closed formula for the `q`-codifferential.**
    `δ_q = q⁻¹ δ + (1 - q⁻¹) L_ξ* ∘ ι_ξ` is the formal adjoint of `d_q`.

    Derived from the three adjointness fields plus bilinearity of the Webster
    pairing; nothing here is assumed about `δ_q` itself. -/
theorem inner_dq_eq_inner_δq (q : Rˣ) (α β : F) :
    A.inner (A.dq q α) β = A.inner α (A.δq q β) := by
  rw [dq_apply, δq_apply, map_add, LinearMap.add_apply, map_smul, map_smul,
    LinearMap.smul_apply, LinearMap.smul_apply, A.δ_adjoint_d, A.thetaLie_adjoint,
    map_add, map_smul, map_smul]

end ContactFormAlgebra

/-- **Part (a)**: the formal adjoint `δ_q` of `d_q` exists.

    The previous version derived this from `axiom adjoint_exists_unique'`.
    It is now a consequence of exhibiting `δq`. -/
theorem q_codifferential_exists (A : ContactFormAlgebra R F) (q : Rˣ) :
    ∃ δ_q : F →ₗ[R] F, ∀ α β : F, A.inner (A.dq q α) β = A.inner α (δ_q β) :=
  ⟨A.δq q, A.inner_dq_eq_inner_δq q⟩

/-- **Closed formula for the `q`-codifferential.**
    The formal adjoint of `d_q` is `δ_q = q⁻¹ δ + (1 - q⁻¹) L_ξ* ∘ ι_ξ`.

    This is the declaration `prop:q-codifferential-formula` resolves to. -/
-- Ref: [leitner2026] Ch. 2, prop:q-codifferential-formula (closed form δ_q = q⁻¹δ + (1−q⁻¹)L_ξ*∘ι_ξ)
theorem q_codifferential_formula (A : ContactFormAlgebra R F) (q : Rˣ) :
    ∃ δ_q : F →ₗ[R] F,
      (∀ α β : F, A.inner (A.dq q α) β = A.inner α (δ_q β)) ∧
      (∀ β : F, δ_q β = ((q⁻¹ : Rˣ) : R) • A.δ β
        + (1 - ((q⁻¹ : Rˣ) : R)) • A.lieReebStar (A.iotaReeb β)) :=
  ⟨A.δq q, A.inner_dq_eq_inner_δq q, A.δq_apply q⟩

namespace ContactFormAlgebra

variable (A : ContactFormAlgebra R F)

/-! ## What the old `adjoint_exists_unique'` axiom actually asserted

`axiom adjoint_exists_unique' (L : DiffForm R → DiffForm R) : ∃! L_star, …`
quantified over an **arbitrary function**, not a linear map. The two results
below say why that is the wrong statement, and what the right hypotheses are.
Both are stated for a bare function `L : F → F`, deliberately: that is the
generality the old axiom claimed. -/

/-- **Having an adjoint forces additivity against the pairing.**

    If a bare function `L` admits an adjoint, then `α ↦ ⟨L α, β⟩` is additive
    — not because `L` is, but because the right-hand side `⟨α, L* β⟩` is
    additive in `α` by bilinearity. So the old axiom, asserting an adjoint for
    *every* function, forces the pairing to see every function as additive. -/
theorem additive_of_hasAdjoint (L Lstar : F → F)
    (h : ∀ α β : F, A.inner (L α) β = A.inner α (Lstar β)) (α₁ α₂ β : F) :
    A.inner (L (α₁ + α₂)) β = A.inner (L α₁) β + A.inner (L α₂) β := by
  rw [h, h, h, map_add, LinearMap.add_apply]

/-- The contrapositive, which is the usable form: a function that the pairing
    does **not** see as additive has no adjoint at all. This is what rules out
    the unrestricted `∀ L, ∃! L_star` of the old axiom. -/
theorem not_hasAdjoint_of_not_additive (L : F → F) (α₁ α₂ β : F)
    (hne : A.inner (L (α₁ + α₂)) β ≠ A.inner (L α₁) β + A.inner (L α₂) β) :
    ¬ ∃ Lstar : F → F, ∀ α β : F, A.inner (L α) β = A.inner α (Lstar β) := by
  rintro ⟨Lstar, h⟩
  exact hne (A.additive_of_hasAdjoint L Lstar h α₁ α₂ β)

/-- **Uniqueness of `δ_q`, under the hypothesis it actually needs.**

    The old axiom asserted `∃!` with no non-degeneracy hypothesis. That is
    false for a degenerate pairing: the identically zero pairing is bilinear
    and admits *every* function as an adjoint of everything. With right
    non-degeneracy assumed, uniqueness is a two-line consequence of the
    closed formula. -/
theorem δq_unique (hnd : ∀ x y : F, (∀ z : F, A.inner z x = A.inner z y) → x = y)
    (q : Rˣ) (L : F → F)
    (hL : ∀ α β : F, A.inner (A.dq q α) β = A.inner α (L β)) (β : F) :
    L β = A.δq q β := by
  refine hnd _ _ fun z => ?_
  rw [← hL z β]
  exact A.inner_dq_eq_inner_δq q z β


/-! ## A model, and the counterexample it supplies

The structure is not vacuous: `degenerate` below is a `ContactFormAlgebra`
over any `R`-module. It is also the counterexample that settles the
uniqueness half of the old `adjoint_exists_unique'` axiom — its pairing is
identically zero, so every function is an adjoint of every operator. -/

/-- The degenerate model: identically zero Webster pairing, identity
    operators. All three adjointness conditions hold trivially. -/
def degenerate (R : Type u) [CommRing R] (F : Type v) [AddCommGroup F]
    [Module R F] : ContactFormAlgebra R F where
  inner := 0
  d := LinearMap.id
  δ := LinearMap.id
  lieReeb := LinearMap.id
  lieReebStar := LinearMap.id
  iotaReeb := LinearMap.id
  thetaWedge := LinearMap.id
  δ_adjoint_d := by intro α β; simp
  iota_adjoint_theta := by intro α β; simp
  lieStar_adjoint_lie := by intro α β; simp

/-- **The old axiom's uniqueness half does not follow from the rest.**

    In the degenerate model every function whatsoever is an adjoint of `d`,
    so over a nontrivial module the adjoint is not unique. The previous
    version asserted `∃!` with no non-degeneracy hypothesis; this exhibits a
    model of everything else in which that `∃!` is false. `δq_unique` above
    is the repaired statement.

    Scope: this refutes the *unhypothesised* uniqueness claim. It says nothing
    against uniqueness on a genuine strictly pseudoconvex CR manifold, where
    the Webster pairing is non-degenerate and `δq_unique` applies. -/
theorem degenerate_adjoint_not_unique (R : Type u) [CommRing R] (F : Type v)
    [AddCommGroup F] [Module R F] [Nontrivial F] :
    ¬ ∀ L : F → F, ∃! Lstar : F → F,
        ∀ α β : F, (degenerate R F).inner (L α) β
          = (degenerate R F).inner α (Lstar β) := by
  intro h
  obtain ⟨Lstar, _, huniq⟩ := h id
  obtain ⟨x, y, hxy⟩ := exists_pair_ne F
  have h1 : (fun _ : F => x) = Lstar := huniq _ (by intro α β; rfl)
  have h2 : (fun _ : F => y) = Lstar := huniq _ (by intro α β; rfl)
  exact hxy (congrFun (h1.trans h2.symm) x)

/-- Non-degeneracy fails in the degenerate model, so `δq_unique`'s hypothesis
    is doing real work rather than being satisfiable for free. -/
theorem degenerate_not_nondegenerate (R : Type u) [CommRing R] (F : Type v)
    [AddCommGroup F] [Module R F] [Nontrivial F] :
    ¬ ∀ x y : F, (∀ z : F, (degenerate R F).inner z x
      = (degenerate R F).inner z y) → x = y := by
  intro h
  obtain ⟨x, y, hxy⟩ := exists_pair_ne F
  exact hxy (h x y fun _ => rfl)

end ContactFormAlgebra

end QOU.QuantumGeometry
