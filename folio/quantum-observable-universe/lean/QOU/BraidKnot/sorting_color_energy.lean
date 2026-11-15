import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Tactic.Ring
import Mathlib.Data.ZMod.Basic

/-!
# QOU.BraidKnot.sorting_color_energy — Hecke eigendecomposition + sorting projection

**Proposition** ([`prop:sorting-color-energy`](../../../measurement-observation/sorting-color-energy.md)).

*Let `σᵢ` be the Hecke generator on `V ⊗ V`.  Then:*

*(1) The R-matrix decomposes `V ⊗ V = Sym²(V) ⊕ Λ²(V)` with
eigenvalues `q` (symmetric) and `−q⁻¹` (antisymmetric).*

*(2) Sorting is the projection from `Λ²(V)` to `Sym²(V)` at `σᵢ`.*

## 2026-09-03 — the projection, and five decorative fields

`SortingColorEnergyContext` carried `V`, `V_sq`, `Sym2`, `Wedge2`, `sigma`,
`q`, `sym_eigenvalue` and `wedge_eigenvalue` as data, plus one claim field
`claim_eigenvalues` stating item (1) verbatim; `sorting_color_energy` was a
`def` whose body was that field.  AGENTS.md §3b-cond item 5.

Worth noting separately: **five of the data fields — `V`, `V_sq`, `Sym2`,
`Wedge2`, `sigma` — never appear in the claim.**  They read as the objects
the proposition is about, and carry none of its content: the field
`claim_eigenvalues` mentions only `sym_eigenvalue`, `wedge_eigenvalue` and
`q`.  So the class *looked* like it axiomatised a representation and
axiomatised two ring elements.

## The manuscript's item (1) is derivable, so this file does not stop at naming

With `sym_eigenvalue` a free element, `sym_eigenvalue = q` is a *definition*
of `sym_eigenvalue`, not a proposition about the Hecke algebra — the same
emptiness as `QOU.BraidKnot.six_term_mass_formula_complete`.  But unlike that
case there is real content within reach, because the eigenvalues are not
arbitrary: they are exactly the roots of the Hecke relation
`(σ − q)(σ + q⁻¹) = 0`, which is the manuscript's own ground relation.

So, sorry-free below:

* `heckeRelation_q` and `heckeRelation_neg_qInv` — `q` and `−q⁻¹` *are* roots.
* `eq_or_eq_of_heckeRelation` — over a ring without zero divisors they are the
  **only** roots.  This is the substance of item (1): a scalar by which `σ`
  acts is forced to be one of the two.
* `sorting_color_energy_of_heckeRelation` — **derives** the block's claim from
  the relation plus the identification of which channel is which.

`sorting_color_energy` itself is the named claim over caller-supplied data
(§1a disposition 3), so it is something the derivation concludes *to* rather
than a field handed back.

`NoZeroDivisors` is required and is not free: over a general `CommRing` a
scalar can satisfy the relation without being either root, so the
classification genuinely needs it.  `R_q = ℤ[q, q⁻¹]` has it.

## What is still unencoded

Everything in item (2), and the representation theory behind item (1):
nothing here constructs `V`, the tensor square, the decomposition
`V ⊗ V = Sym²(V) ⊕ Λ²(V)`, the operator `σᵢ`, or a proof that `σᵢ` satisfies
the Hecke relation and acts by a scalar on each summand.  What is proved is
that *given* it acts by scalars satisfying that relation, the eigenvalues are
the manuscript's — which is the half that does not need the missing
machinery.

**Base ring (§7c).**  `q` is carried as a **unit** `q : Rˣ` over a generic
`[CommRing R]` rather than an element of a field: the only thing inverted is
`q` itself.  This is the manuscript's own ground ring — the Hecke relation
has coefficients in `R_q = ℤ[q, q⁻¹]` (`LaurentPolynomial ℤ`, where `q = T 1`
is a unit) — and no ordering or `Real.*` appears anywhere.

Bean `qou-z9ws`.

-- Ref: [leitner2026] quantum-observable-universe/measurement-observation/sorting-color-energy.md
-/

namespace QOU.BraidKnot

variable {R : Type*} [CommRing R]

/-- **The Hecke relation** at a scalar: `(x − q)(x + q⁻¹) = 0`.

The manuscript's ground relation for the generator `σᵢ`, evaluated at a
scalar by which `σᵢ` acts on a summand. -/
-- Ref: [leitner2026] quantum-observable-universe/measurement-observation/sorting-color-energy.md
def heckeRelation (q : Rˣ) (x : R) : Prop :=
  (x - (q : R)) * (x + ((q⁻¹ : Rˣ) : R)) = 0

/-- `q` is a root of the Hecke relation — the symmetric eigenvalue. -/
theorem heckeRelation_q (q : Rˣ) : heckeRelation q (q : R) := by
  simp [heckeRelation]

/-- `−q⁻¹` is a root of the Hecke relation — the antisymmetric eigenvalue. -/
theorem heckeRelation_neg_qInv (q : Rˣ) :
    heckeRelation q (-((q⁻¹ : Rˣ) : R)) := by
  simp [heckeRelation]

/-- **They are the only roots** — the substance of item (1).

A scalar by which `σᵢ` acts on a summand, satisfying the Hecke relation, is
forced to be `q` or `−q⁻¹`.  `NoZeroDivisors` is doing real work: over a
general `CommRing` a scalar can satisfy the relation without being either
root. -/
-- Ref: [leitner2026] quantum-observable-universe/measurement-observation/sorting-color-energy.md
theorem eq_or_eq_of_heckeRelation [NoZeroDivisors R] {q : Rˣ} {x : R}
    (h : heckeRelation q x) :
    x = (q : R) ∨ x = -((q⁻¹ : Rˣ) : R) := by
  rcases mul_eq_zero.mp h with h₁ | h₂
  · exact Or.inl (sub_eq_zero.mp h₁)
  · exact Or.inr (add_eq_zero_iff_eq_neg.mp h₂)

/-- **`NoZeroDivisors` is load-bearing, and here is the counterexample.**

In `ZMod 8` with `q = 1`, the Hecke relation reads `(x − 1)(x + 1) = 0`, and
`x = 3` satisfies it while being neither `q = 1` nor `−q⁻¹ = 7`.

Recorded so the hypothesis on `eq_or_eq_of_heckeRelation` is justified by a
witness rather than by the docstring asserting it.

`decide` here is arithmetic in an eight-element ring at one concrete point —
the finite-computation case AGENTS.md §1a explicitly allows, not a structural
claim pushed through the kernel evaluator. -/
theorem exists_heckeRelation_ne_both_of_zeroDivisors :
    ∃ x : ZMod 8, heckeRelation (1 : (ZMod 8)ˣ) x ∧
      x ≠ ((1 : (ZMod 8)ˣ) : ZMod 8) ∧
      x ≠ -(((1 : (ZMod 8)ˣ)⁻¹ : (ZMod 8)ˣ) : ZMod 8) :=
  ⟨3, by unfold heckeRelation; decide, by decide, by decide⟩

/-- **Eigenspace decomposition with explicit Hecke eigenvalues**
([`prop:sorting-color-energy`] item (1)), as a proposition over
caller-supplied data.

`σᵢ` acts as `q` on `Sym²(V)` and as `−q⁻¹` on `Λ²(V)`.

**Named, not asserted** — but, unlike the other carriers drained under this
bean, it is also *derived* here, from the Hecke relation: see
`sorting_color_energy_of_heckeRelation`. -/
-- Ref: [leitner2026] quantum-observable-universe/measurement-observation/sorting-color-energy.md
def sorting_color_energy (q : Rˣ) (sym_eigenvalue wedge_eigenvalue : R) : Prop :=
  sym_eigenvalue = (q : R) ∧ wedge_eigenvalue = -((q⁻¹ : Rˣ) : R)

/-- **Item (1), derived.**

If both eigenvalues satisfy the Hecke relation, and each is known not to be
the *other* channel's value, then they are the manuscript's `q` and `−q⁻¹`.

The two `≠` hypotheses are the channel identification — which summand is
`Sym²` and which is `Λ²`. That is what the missing representation theory
would supply; everything downstream of it is proved. -/
-- Ref: [leitner2026] quantum-observable-universe/measurement-observation/sorting-color-energy.md
theorem sorting_color_energy_of_heckeRelation [NoZeroDivisors R] {q : Rˣ}
    {sym_eigenvalue wedge_eigenvalue : R}
    (hsym : heckeRelation q sym_eigenvalue)
    (hwedge : heckeRelation q wedge_eigenvalue)
    (hsym' : sym_eigenvalue ≠ -((q⁻¹ : Rˣ) : R))
    (hwedge' : wedge_eigenvalue ≠ (q : R)) :
    sorting_color_energy q sym_eigenvalue wedge_eigenvalue :=
  ⟨(eq_or_eq_of_heckeRelation hsym).resolve_right hsym',
   (eq_or_eq_of_heckeRelation hwedge).resolve_left hwedge'⟩

/-- **The claim is refutable at freely-chosen eigenvalues**, which is why it is
named rather than carried as a `sorry`.

At `q = 1` with both eigenvalues `0`, the first conjunct reads `0 = 1`. -/
theorem not_sorting_color_energy_of_free_data :
    ¬ sorting_color_energy (1 : ℤˣ) 0 0 := by
  simp [sorting_color_energy]

end QOU.BraidKnot
