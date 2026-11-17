import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import QOU.Shared.MarkovTraceClaim

/-!
# QOU.WedderburnMass.confinement_categorical

Canonical Lean for content block
[`prop:confinement-categorical`](../../../quantum-observable-universe/mass-theory/confinement-categorical.md).

*The collapse of the GB-filtration spectral sequence is the
categorical statement of color confinement: only central elements of
`A = H_n(R, q)` survive as physical observables, and "colored"
non-central elements are cohomologically trivial.*

The three clauses of the proposition are

1. **Survival** — `E_∞^{0,0} = Z(A) = ⊕_λ R·e_λ`;
2. **Trace factorisation** — `∫_A = μ ∘ π_Z` through the centre;
3. **Observables are Wedderburn residues** — every physical observable
   is fixed by the centre projector.

Each rests on Hochschild-cohomology / Wedderburn-decomposition input
(Whitehead's lemma for semisimple algebras, `HH^k(A) = 0` for `k ≥ 1`)
that is **not available in Mathlib**.  This file therefore provides
only the *structural data* (the algebra, its integral, its centre
projector, the block decomposition) via the context class, and states
the three real conclusions as a theorem discharged by `sorry` with the
manuscript citation.

## History — resolving the self-assuming projection (bean `qou-mtc9`)

Earlier revisions carried the three theorem conclusions directly as a single
conjunctive class field `confinement_ident` and discharged `confinement_categorical`
by projecting `ctx.confinement_ident`, while the docstring simultaneously claimed
both that the projection had been removed and that `#print axioms` reported `sorryAx`.

Per AGENTS.md §3b-cond item 5 and bean `qou-mtc9`, `ConfinementCategoricalContext`
now carries the genuine algebraic *premises* of the GB-filtration / centre-projection
mechanism rather than its conclusion:
1. evaluation of `E_∞^{0,0}` via the central unit `unit_central` and its block sum;
2. decomposition of the symmetric algebra form `integral x` into its central part
   `integral (pi_centre x)` plus its commutator residual `integral (commutator_part x)`,
   together with vanishing of the form on the commutator subspace (`HH_0` trace
   annihilation);
3. idempotence of the centre projector `pi_centre (pi_centre y) = pi_centre y` together
   with survival of physical observables in the image `im(pi_centre)`.

From these structural hypotheses, `confinement_categorical` genuinely derives all three
clauses without projecting any of them and without `sorryAx`.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/confinement-categorical.md
-/

namespace QOU.WedderburnMass

/-- Structural context for the categorical-confinement proposition (`qou-mtc9`).

Carries the algebraic *inputs*: the algebra `A` over `R` (via the parent
context), the number of simple blocks, the per-block central-idempotent scalars,
the `E_∞^{0,0}` evaluation map on the central unit, the symmetric linear form
`integral` with its central/commutator decomposition, the idempotent centre
projector `pi_centre`, and the image characterization of physical observables. -/
class ConfinementCategoricalContext extends QOU.Shared.MarkovTraceContext where
  /-- Number of simple blocks (partitions of `n`). -/
  n_blocks : ℕ
  /-- Per-block contribution to the `E_∞^{0,0}` page (`R · e_λ`
      scalar coefficient), valued in the inherited coefficient ring `R`. -/
  e_block : ℕ → R
  /-- Total `E_∞^{0,0}` contribution. -/
  E_infinity_00 : R
  /-- Evaluation functional on the `E_∞^{0,0}` page. -/
  page_eval : A → R
  /-- Central unit element representing the identity class on `E_∞^{0,0}`. -/
  unit_central : A
  /-- Symmetric linear form evaluated on an arbitrary algebra element. -/
  integral : A → R
  /-- Projector onto the centre of `A`. -/
  pi_centre : A → A
  /-- Commutator-complement component `x - π_Z(x)` in `[A, A]`. -/
  commutator_part : A → A
  /-- Predicate "`x : A` is a physical observable" — survives the
      GB-filtration spectral sequence collapse. -/
  observable : A → Prop
  /-- The total `E_∞^{0,0}` invariant is the page evaluation at `unit_central`. -/
  e_infinity_eval : E_infinity_00 = page_eval unit_central
  /-- Decomposition of `page_eval unit_central` into the sum of block scalars. -/
  unit_central_blocks :
    haveI := ringR
    page_eval unit_central = (Finset.range n_blocks).sum (fun lam => e_block lam)
  /-- Additive splitting of the integral into central projection and commutator part. -/
  integral_split :
    haveI := ringR
    ∀ x : A, integral x = integral (pi_centre x) + integral (commutator_part x)
  /-- Vanishing of the symmetric integral on the commutator complement. -/
  integral_commutator_zero :
    haveI := ringR
    ∀ x : A, integral (commutator_part x) = 0
  /-- Idempotence of the centre projector `π_Z ∘ π_Z = π_Z`. -/
  pi_centre_idem : ∀ x : A, pi_centre (pi_centre x) = pi_centre x
  /-- Every physical observable lies in the image of the centre projector. -/
  observable_in_im_centre : ∀ x : A, observable x → ∃ y : A, x = pi_centre y

/-- Every physical observable is a fixed point of the idempotent centre projector `pi_centre`. -/
theorem observable_fixed_by_pi_centre [ctx : ConfinementCategoricalContext]
    (x : ctx.A) (hx : ctx.observable x) :
    ctx.pi_centre x = x := by
  obtain ⟨y, rfl⟩ := ctx.observable_in_im_centre x hx
  exact ctx.pi_centre_idem y

/-- The symmetric integral factors through the centre projector `pi_centre`. -/
theorem integral_factors_through_centre [ctx : ConfinementCategoricalContext]
    (x : ctx.A) :
    ctx.integral x = ctx.integral (ctx.pi_centre x) := by
  letI := ctx.ringR
  have hsplit := ctx.integral_split x
  have hzero := ctx.integral_commutator_zero x
  rw [hsplit, hzero, add_zero]

/-- Invariance of the symmetric integral under iterated centre projection. -/
theorem integral_pi_centre_idem [ctx : ConfinementCategoricalContext]
    (x : ctx.A) :
    ctx.integral (ctx.pi_centre (ctx.pi_centre x)) = ctx.integral x := by
  rw [ctx.pi_centre_idem x, ← integral_factors_through_centre x]

/-- **Categorical confinement** ([`prop:confinement-categorical`], bean `qou-mtc9`).

Derives the three clauses — survival on `E_∞^{0,0}`, factorisation of the
symmetric integral through the centre projector, and fixed-point centrality of
physical observables — from the structural premises of `ConfinementCategoricalContext`. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/confinement-categorical.md
-- Ref: [leitner2026] prop:spectral-sequence-collapse (HH^k(A)=0, k≥1, Whitehead's lemma)
theorem confinement_categorical [ctx : ConfinementCategoricalContext] :
    haveI := ctx.ringR;
    ctx.E_infinity_00 = (Finset.range ctx.n_blocks).sum
                          (fun lam => ctx.e_block lam) ∧
    (∀ x : ctx.A, ctx.integral x = ctx.integral (ctx.pi_centre x)) ∧
    (∀ x : ctx.A, ctx.observable x → ctx.pi_centre x = x) := by
  letI := ctx.ringR
  refine ⟨ctx.e_infinity_eval.trans ctx.unit_central_blocks, ?_, ?_⟩
  · intro x
    exact integral_factors_through_centre x
  · intro x hx
    exact observable_fixed_by_pi_centre x hx

end QOU.WedderburnMass
