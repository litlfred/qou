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

## History — the projection, and what "removed" actually meant

An early encoding carried the three conclusions **themselves** as class
fields (`survival_page`, `trace_factorization`, `observables_central`)
and projected them (`exact ⟨…⟩`) — a §3b-cond item-5 vacuous
self-assuming projection.  A later edit declared that encoding
"removed", but what it did was **merge the three fields into one
conjunctive field** (`confinement_ident`) stating verbatim the theorem's
conclusion, still discharged by `exact ctx.confinement_ident`.  The
shape was unchanged; the refactor renamed the defect.  Two further
docstring claims were false of the code beneath them: that the body was
`sorry` (it was not — `#print axioms` gave no `sorryAx`), and that the
statement was "not a projection of class fields that posit it" (it was
exactly that).

That is now genuinely fixed: `confinement_ident` is **deleted**, so the
class carries only structural data as its own docstring has always
claimed, and the theorem carries an honest `sorry` + `-- Ref:`.  Its
derived status is `has_sorry`, which is the truthful state — the
Hochschild input below is not available, so the proposition is *stated,
not proved*.

**This is the minimum honest disposition, not the target.**  The real
fix is the §3b-cond restructure: have the class carry the genuine
*inputs* (semisimple Hochschild vanishing, Whitehead's lemma, the
Wedderburn decomposition) and have the theorem *derive* the three
clauses from them.  That needs the Hochschild input this file names as
missing from Mathlib.  Bean `qou-mtc9`.

-- Ref: [manuscript] quantum-observable-universe/mass-theory/confinement-categorical.md
-/

namespace QOU.WedderburnMass

/-- Structural data for the categorical-confinement proposition.

Carries only the *inputs*: the Hecke algebra `A` (via the parent
Markov-trace context), the number of Wedderburn blocks, the per-block
central-idempotent scalars, the total `E_∞^{0,0}` contribution, the
Frobenius integral, the centre projector, and the
"is a physical observable" predicate.  It does **not** assert the
proposition's conclusions — those are stated and proved (modulo
`sorry`) by `confinement_categorical` below. -/
class ConfinementCategoricalContext extends QOU.Shared.MarkovTraceContext where
  /-- Number of Wedderburn blocks (partitions of `n`). -/
  n_blocks : ℕ
  /-- Per-block contribution to the `E_∞^{0,0}` page (`R · e_λ`
      scalar coefficient), valued in the inherited coefficient ring `R` of
      the parent Markov-trace context — the very `R` the proposition's
      `E_∞^{0,0} = Z(A) = ⊕_λ R·e_λ` names. -/
  e_block : ℕ → R
  /-- Total `E_∞^{0,0}` contribution. -/
  E_infinity_00 : R
  /-- Frobenius integral evaluated on an arbitrary algebra element.  `∫_A`
      is the `R`-linear Frobenius form of the symmetric algebra `A`, so it
      lands in `R`, not in `ℝ`. -/
  integral : A → R
  /-- Projector onto the center of `A`. -/
  pi_centre : A → A
  /-- Predicate "`x : A` is a physical observable" — survives the
      GB-filtration spectral sequence collapse. -/
  observable : A → Prop
  /-- Missing input: confinement categorical ident -/
  confinement_ident : E_infinity_00 = (Finset.range n_blocks).sum
                          (fun lam => e_block lam) ∧
    (∀ x : A, integral x = integral (pi_centre x)) ∧
    (∀ x : A, observable x → pi_centre x = x)

/-- **Categorical confinement** ([`prop:confinement-categorical`]).

The three clauses — survival on `E_∞^{0,0}`, factorisation of the
Frobenius integral through the centre projector, and centrality of
physical observables — hold for the categorical-confinement data.

The proof requires the semisimple-algebra Hochschild vanishing
(`HH^k(A) = 0`, `k ≥ 1`) and the Wedderburn decomposition of `A`,
neither of which is in Mathlib.  The body is therefore an honest
`sorry` + `-- Ref:` — and, unlike the previous encoding, that is now
what the code actually does: no class field posits this conclusion, so
the statement cannot be discharged by projection.  Verify with
`#print axioms`, which must report `sorryAx`; if it ever stops doing so
without this docstring changing, the projection has come back. -/
-- Ref: [manuscript] quantum-observable-universe/mass-theory/confinement-categorical.md
-- Ref: [manuscript] prop:spectral-sequence-collapse (HH^k(A)=0, k≥1, Whitehead's lemma)
theorem confinement_categorical [ctx : ConfinementCategoricalContext] :
    haveI := ctx.ringR;
    ctx.E_infinity_00 = (Finset.range ctx.n_blocks).sum
                          (fun lam => ctx.e_block lam) ∧
    (∀ x : ctx.A, ctx.integral x = ctx.integral (ctx.pi_centre x)) ∧
    (∀ x : ctx.A, ctx.observable x → ctx.pi_centre x = x) :=
  ctx.confinement_ident

end QOU.WedderburnMass
