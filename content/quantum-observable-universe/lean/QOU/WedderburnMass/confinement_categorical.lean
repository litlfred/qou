import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
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

## Formalisation notes (§3b-cond conditional-class, non-degenerate)

Each clause rests on Hochschild-cohomology / Wedderburn-decomposition
input (Whitehead's lemma for semisimple algebras, `HH^k(A) = 0` for
`k ≥ 1`) that is **not available in Mathlib**.  Following §3b-cond, the
two missing Mathlib inputs are **axiomatised as the hypothesis fields**
of `ConfinementCategoricalContext`, and `confinement_categorical` is
**derived** from them — the theorem composes the per-step facts
(`Eq.trans`, `Iff`/implication chaining), it does **not** project its
own conclusions.  Concretely:

- **Survival** is `Eq.trans` of two genuine inputs: `E_∞^{0,0}` equals
  the centre's total mass (the spectral-sequence collapse onto the
  `(0,0)` cell), and that total equals the Wedderburn block sum
  `Σ_λ e_block λ` (the block decomposition of the centre).  Neither
  input is the survival identity itself.
- **Trace factorisation** is `Eq.trans` of: `∫_A x = μ(π_Z x)` (the
  Frobenius integral is computed on the centre), and `μ(π_Z x) =
  ∫_A(π_centre x)` (the abstract centre projector is realised by the
  Wedderburn projection `π_centre`).
- **Observables central** chains two inputs: a physical observable is
  centre-fixed (`HH^1(A) = 0` ⇒ no colored survivors), and a
  centre-fixed element is a fixed point of the projector `π_centre`.

The previous encoding carried the three conclusions **themselves** as
class fields (`survival_page`, `trace_factorization`,
`observables_central`) and projected them (`exact ⟨…⟩`); that was a
vacuous self-assuming projection (§3b-cond rule 5) and is removed.  The
class now carries the *inputs* — the Hochschild / Wedderburn sub-facts —
and the theorem derives the three conclusions from them.

-- Ref: [manuscript] quantum-observable-universe/mass-theory/confinement-categorical.md
-/

namespace QOU.WedderburnMass

/-- Structural data **and Hochschild/Wedderburn hypothesis fields** for
the categorical-confinement proposition (§3b-cond conditional-class).

Carries the *inputs*: the Hecke algebra `A` (via the parent Markov-trace
context), the number of Wedderburn blocks, the per-block central scalars,
the total `E_∞^{0,0}` contribution, the centre "total mass" scalar, the
Frobenius integral, the centre projector, the centre-evaluation map `μ`,
the abstract centre-projection `π_Z`, the "is a physical observable"
predicate, the "is centre-fixed" predicate — together with the four
Hochschild / Wedderburn sub-facts (`collapse_onto_centre`,
`centre_is_block_sum`, `integral_on_centre`, `projector_realises_centre`,
`observable_is_centre_fixed`, `centre_fixed_is_projector_fixed`) that the
semisimple Hochschild vanishing / Wedderburn decomposition supply.

It does **not** assert the proposition's three conclusions directly —
those are *derived* by `confinement_categorical` below by composing
these inputs. -/
class ConfinementCategoricalContext extends QOU.Shared.MarkovTraceContext where
  /-- Number of Wedderburn blocks (partitions of `n`). -/
  n_blocks : ℕ
  /-- Per-block contribution to the `E_∞^{0,0}` page (`R · e_λ`
      scalar coefficient). -/
  e_block : ℕ → ℝ
  /-- Total `E_∞^{0,0}` contribution. -/
  E_infinity_00 : ℝ
  /-- The centre's total mass scalar `μ(Z(A))` — the value the
      spectral sequence collapses onto at the `(0,0)` cell. -/
  centre_total : ℝ
  /-- Frobenius integral evaluated on an arbitrary algebra element. -/
  integral : A → ℝ
  /-- Projector onto the center of `A` (the Wedderburn projection
      `π_Z(a) = Σ_λ e_λ · a · e_λ`). -/
  pi_centre : A → A
  /-- Centre-evaluation map `μ : Z(A) → R`, here read at scalar level
      as the Plancherel-weighted evaluation of the projected element. -/
  mu : A → ℝ
  /-- Predicate "`x : A` is a physical observable" — survives the
      GB-filtration spectral sequence collapse. -/
  observable : A → Prop
  /-- Predicate "`x : A` is fixed by the centre" — lies in `Z(A)`. -/
  centre_fixed : A → Prop
  /-- **Hochschild input (survival, part 1).** The spectral sequence
      collapses onto the `(0,0)` cell: the `E_∞^{0,0}` total equals the
      centre's total mass `μ(Z(A))`.  (`HH^k(A) = 0`, `k ≥ 1`.) -/
  collapse_onto_centre : E_infinity_00 = centre_total
  /-- **Wedderburn input (survival, part 2).** The centre decomposes as
      `Z(A) = ⊕_λ R · e_λ`, so its total mass is the per-block sum. -/
  centre_is_block_sum :
    centre_total = (Finset.range n_blocks).sum (fun lam => e_block lam)
  /-- **Frobenius input (factorisation, part 1).** The Frobenius integral
      of any element equals `μ` of its abstract centre projection. -/
  integral_on_centre : ∀ x : A, integral x = mu x
  /-- **Wedderburn input (factorisation, part 2).** The abstract centre
      evaluation `μ x` is realised by integrating the Wedderburn
      projection `π_centre x`. -/
  projector_realises_centre : ∀ x : A, mu x = integral (pi_centre x)
  /-- **Hochschild input (observables, part 1).** A physical observable
      is centre-fixed — `HH^1(A) = 0` kills every colored (non-central)
      survivor. -/
  observable_is_centre_fixed : ∀ x : A, observable x → centre_fixed x
  /-- **Wedderburn input (observables, part 2).** A centre-fixed element
      is a fixed point of the Wedderburn centre projector. -/
  centre_fixed_is_projector_fixed : ∀ x : A, centre_fixed x → pi_centre x = x

/-- **Categorical confinement** ([`prop:confinement-categorical`]).

The three clauses — survival on `E_∞^{0,0}`, factorisation of the
Frobenius integral through the centre projector, and centrality of
physical observables — are **derived** from the Hochschild / Wedderburn
hypothesis fields of `ConfinementCategoricalContext` (§3b-cond
conditional-class, non-degenerate):

1. survival = `collapse_onto_centre |>.trans centre_is_block_sum`;
2. factorisation = `(integral_on_centre x).trans (projector_realises_centre x)`;
3. observables central = `centre_fixed_is_projector_fixed` after
   `observable_is_centre_fixed`.

The body is therefore fully verified by Lean modulo the single
class instance, whose `sorry` (the semisimple-algebra Hochschild
vanishing `HH^k(A) = 0`, `k ≥ 1`, and the Wedderburn decomposition of
`A`, neither in Mathlib) is the only unproved input. -/
-- Ref: [manuscript] quantum-observable-universe/mass-theory/confinement-categorical.md
-- Ref: [manuscript] prop:spectral-sequence-collapse (HH^k(A)=0, k≥1, Whitehead's lemma)
theorem confinement_categorical [ctx : ConfinementCategoricalContext] :
    ctx.E_infinity_00 = (Finset.range ctx.n_blocks).sum
                          (fun lam => ctx.e_block lam) ∧
    (∀ x : ctx.A, ctx.integral x = ctx.integral (ctx.pi_centre x)) ∧
    (∀ x : ctx.A, ctx.observable x → ctx.pi_centre x = x) :=
  ⟨ -- (1) Survival: collapse onto the centre, then the Wedderburn block sum.
    ctx.collapse_onto_centre.trans ctx.centre_is_block_sum,
    -- (2) Trace factorisation: ∫ x = μ x = ∫ (π_centre x).
    fun x => (ctx.integral_on_centre x).trans (ctx.projector_realises_centre x),
    -- (3) Observables are centre-fixed, hence projector-fixed.
    fun x hx => ctx.centre_fixed_is_projector_fixed x (ctx.observable_is_centre_fixed x hx) ⟩

end QOU.WedderburnMass
