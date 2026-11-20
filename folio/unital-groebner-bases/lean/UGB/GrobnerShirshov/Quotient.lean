import UGB.GrobnerShirshov.Basic
import Mathlib.Algebra.Module.Submodule.Basic
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.LinearAlgebra.Basis.Defs

/-!
# `UGB.GrobnerShirshov.Quotient` — the quotient algebra the framework talks about

Every statement of the main theorem is about `A = k⟨G⟩ / I`. **The development had
no quotient.** `AlgElement` says so in its own docstring — "a representation, not
a quotient" — and `CompositionLemma.composition_lemma` carries the claim

> a GS basis (all S-polynomials reduce to zero) implies that normal-form
> monomials form a `k`-basis of the quotient `k⟨G⟩ / (Σ)`

in a **comment**, above a theorem whose type says only `reduce (reduce f) = reduce f`.
The basis claim was not a proposition anywhere. This file makes it one.

Two independent threads reached the same gap: bean qou-auq3 (the Hecke route to
`H_k` for `k > 4` needs normal forms to *be* an algebra) and bean qou-k6ks
(Leitner–Pawloski's `A` is the quotient, so "no quasi-zeros" cannot bite without
one).

## Why it could not be built directly

`AlgElement` is a raw structure carrying a `coeff` function **and** a `support`
`Finset` that is only a *superset* of the true support. So structural equality is
strictly finer than mathematical equality, and the arithmetic already in
`Elem.lean` is not a `Module` on the nose:

* `smul c f` keeps `f.support` even when `c = 0`, so `(0 : k) • f` has support
  `f.support`, not `∅` — `zero_smul` fails as a structure equation;
* `add` unions supports, so associativity holds only up to `Finset.union_assoc`
  plus `funext`.

`Elem.lean` anticipated this and defined `CoeffEq f g := ∀ m, f.coeff m = g.coeff m`
as "the equality that means anything mathematically". Quotienting by it first is
what makes everything below routine — and once `FreeAlg` is a `Module`, the ideal
is a `Submodule` and the quotient algebra is Mathlib's, for free.

## What is proved here, and what is stated

Proved: `CoeffEq` is an equivalence; `FreeAlg` with its `AddCommGroup` and
`Module k` structure; the two-sided ideal of a rewriting system as a `Submodule`;
the quotient `QuotAlg`.

**Stated, not proved**: `NormalFormBasis` — the property that the normal-form
monomials form a `k`-basis of `QuotAlg`. It is a definition here, so that
`composition_lemma`'s comment becomes something a theorem can conclude and a
consumer can require. Proving it *is* the diamond lemma, and it additionally
needs the framework's standing axioms. Those were five when this file was
written; they are now **one** — `local_confluence`. `reduction_well_founded`
was proved on 2026-11-20 (`Basic.lean`, Dershowitz–Manna on live supports, bean
qou-2q7r); `confluence` and `normal_form_unique` were proved from the two
(Newman's lemma), and `normal_form_exists` turned out to be **false** and was
replaced by a theorem carrying the unit-leading-coefficient hypothesis it had
dropped (beans qou-ch3j, qou-lzoo). Nothing here discharges the remaining one.
-/

namespace UGB.GrobnerShirshov

universe u v

variable {G : Type u} {k : Type v} [Ring k]

/-! ## §1  `CoeffEq` is an equivalence -/

theorem coeffEq_refl (f : AlgElement G k) : AlgElement.CoeffEq f f := fun _ => rfl

theorem coeffEq_symm {f g : AlgElement G k} (h : AlgElement.CoeffEq f g) :
    AlgElement.CoeffEq g f := fun m => (h m).symm

theorem coeffEq_trans {f g h : AlgElement G k}
    (hfg : AlgElement.CoeffEq f g) (hgh : AlgElement.CoeffEq g h) :
    AlgElement.CoeffEq f h := fun m => (hfg m).trans (hgh m)

/-- The setoid that turns the representation into the thing it represents. -/
instance algSetoid (G : Type u) (k : Type v) [Ring k] : Setoid (AlgElement G k) where
  r := AlgElement.CoeffEq
  iseqv := ⟨coeffEq_refl, coeffEq_symm, coeffEq_trans⟩

/-! ## §2  The free algebra as an actual type

`FreeAlg G k` is `k⟨G⟩`: `AlgElement` modulo "same coefficients everywhere". -/

/-- The free associative algebra `k⟨G⟩`, as a quotient of the representation. -/
def FreeAlg (G : Type u) (k : Type v) [Ring k] : Type (max u v) :=
  Quotient (algSetoid G k)

namespace FreeAlg

/-- The class of a representation. -/
def mk (f : AlgElement G k) : FreeAlg G k := Quotient.mk (algSetoid G k) f

@[simp] theorem mk_eq_mk {f g : AlgElement G k} :
    (mk f : FreeAlg G k) = mk g ↔ AlgElement.CoeffEq f g :=
  Quotient.eq (r := algSetoid G k)

/-- Coefficient extraction descends: it is exactly what `CoeffEq` preserves. -/
def coeff (x : FreeAlg G k) (m : Monomial G) : k :=
  Quotient.liftOn x (fun f => f.coeff m) (fun _ _ h => h m)

@[simp] theorem coeff_mk (f : AlgElement G k) (m : Monomial G) :
    coeff (mk f : FreeAlg G k) m = f.coeff m := rfl

/-- **Elements are determined by their coefficients** — the property `AlgElement`
lacked, and the reason this quotient exists. -/
theorem ext {x y : FreeAlg G k} (h : ∀ m, coeff x m = coeff y m) : x = y := by
  induction x using Quotient.inductionOn with
  | h f => induction y using Quotient.inductionOn with
    | h g => exact Quotient.sound (fun m => h m)

instance : Zero (FreeAlg G k) := ⟨mk AlgElement.zero⟩

-- From here on `AlgElement.add` is in play, which needs decidable equality on
-- generators to union supports.
variable [DecidableEq G]

instance : Add (FreeAlg G k) :=
  ⟨fun x y => Quotient.liftOn₂ x y (fun f g => mk (AlgElement.add f g))
    (fun _ _ _ _ h₁ h₂ => Quotient.sound (fun m => by
      simp only [AlgElement.add_coeff]; rw [h₁ m, h₂ m]))⟩

instance : Neg (FreeAlg G k) :=
  ⟨fun x => Quotient.liftOn x (fun f => mk (AlgElement.neg f))
    (fun _ _ h => Quotient.sound (fun m => by
      simp only [AlgElement.neg_coeff]; rw [h m]))⟩

instance : SMul k (FreeAlg G k) :=
  ⟨fun c x => Quotient.liftOn x (fun f => mk (AlgElement.smul c f))
    (fun _ _ h => Quotient.sound (fun m => by
      simp only [AlgElement.smul_coeff]; rw [h m]))⟩

omit [DecidableEq G] in
@[simp] theorem coeff_zero (m : Monomial G) : coeff (0 : FreeAlg G k) m = 0 := rfl

@[simp] theorem coeff_add (x y : FreeAlg G k) (m : Monomial G) :
    coeff (x + y) m = coeff x m + coeff y m := by
  induction x using Quotient.inductionOn with
  | h f => induction y using Quotient.inductionOn with
    | h g => rfl

omit [DecidableEq G] in
@[simp] theorem coeff_neg (x : FreeAlg G k) (m : Monomial G) :
    coeff (-x) m = -(coeff x m) := by
  induction x using Quotient.inductionOn with
  | h f => rfl

omit [DecidableEq G] in
@[simp] theorem coeff_smul (c : k) (x : FreeAlg G k) (m : Monomial G) :
    coeff (c • x) m = c * coeff x m := by
  induction x using Quotient.inductionOn with
  | h f => rfl

/-- **`k⟨G⟩` is an additive group.** Every law is its coefficient-wise counterpart
in `k`, which is what `ext` reduces it to. -/
instance : AddCommGroup (FreeAlg G k) where
  add_assoc x y z := ext (fun m => by simp [add_assoc])
  zero_add x := ext (fun m => by simp)
  add_zero x := ext (fun m => by simp)
  add_comm x y := ext (fun m => by simp [add_comm])
  neg_add_cancel x := ext (fun m => by simp)
  nsmul := nsmulRec
  zsmul := zsmulRec

/-- **…and a `k`-module.** Note `zero_smul`: this is the law that fails on the
nose for `AlgElement`, because `smul 0 f` keeps `f.support`. Here it holds,
because here elements *are* their coefficients. -/
instance : Module k (FreeAlg G k) where
  one_smul x := ext (fun m => by simp)
  mul_smul a b x := ext (fun m => by simp [mul_assoc])
  smul_zero a := ext (fun m => by simp)
  smul_add a x y := ext (fun m => by simp [mul_add])
  add_smul a b x := ext (fun m => by simp [add_mul])
  zero_smul x := ext (fun m => by simp)

end FreeAlg

-- `variable [DecidableEq G]` above was scoped to `namespace FreeAlg`; the module
-- structure it enables is needed from here on too.
variable [DecidableEq G]

/-! ## §3  The ideal of a rewriting system

The two-sided ideal generated by the relations. Because the contexts are
monomials — and monomials span — `contextMul a r.relation b` for monomial `a, b`
generates the same submodule as arbitrary two-sided multiplication, which is why
`Elem.lean` works with `contextMul` throughout. -/

/-- The generating set: every relation of `sys`, in every monomial context. -/
def relationContexts (sys : RewritingSystem G k) : Set (FreeAlg G k) :=
  {x | ∃ (r : ReductionRule G k) (_ : r ∈ sys.rules) (a b : Monomial G),
        x = FreeAlg.mk (AlgElement.contextMul a r.relation b)}

/-- **The ideal `I = (Σ)`**, as a submodule of `k⟨G⟩` spanned by the relations in
all monomial contexts. -/
def systemIdeal (sys : RewritingSystem G k) : Submodule k (FreeAlg G k) :=
  Submodule.span k (relationContexts sys)

theorem mem_systemIdeal_of_context {sys : RewritingSystem G k}
    {r : ReductionRule G k} (hr : r ∈ sys.rules) (a b : Monomial G) :
    FreeAlg.mk (AlgElement.contextMul a r.relation b) ∈ systemIdeal sys :=
  Submodule.subset_span ⟨r, hr, a, b, rfl⟩

/-! ## §4  The quotient algebra

`A = k⟨G⟩ / I`. This is the object every statement of the main theorem is about,
and the object the development did not have. -/

/-- **The quotient `A = k⟨G⟩ / (Σ)`.** -/
abbrev QuotAlg (sys : RewritingSystem G k) : Type (max u v) :=
  FreeAlg G k ⧸ systemIdeal sys

/-- The projection `k⟨G⟩ ↠ A`. -/
def toQuot (sys : RewritingSystem G k) : FreeAlg G k →ₗ[k] QuotAlg sys :=
  (systemIdeal sys).mkQ

theorem toQuot_eq_zero_iff {sys : RewritingSystem G k} (x : FreeAlg G k) :
    toQuot sys x = 0 ↔ x ∈ systemIdeal sys :=
  Submodule.Quotient.mk_eq_zero _

/-- Every relation dies in the quotient — the defining property, and a check that
`systemIdeal` is the right submodule. -/
theorem relation_eq_zero {sys : RewritingSystem G k}
    {r : ReductionRule G k} (hr : r ∈ sys.rules) (a b : Monomial G) :
    toQuot sys (FreeAlg.mk (AlgElement.contextMul a r.relation b)) = 0 :=
  (toQuot_eq_zero_iff _).mpr (mem_systemIdeal_of_context hr a b)

/-! ## §5  The normal-form basis property, as a proposition

This is the statement `composition_lemma`'s docstring makes in prose. It is a
*definition* here, not a theorem: proving it is the diamond lemma, and it rests
on the framework's two remaining standing axioms. Having it as a proposition is what lets
a theorem conclude it and a consumer require it — which a comment cannot do. -/

/-- The monomials in normal form for `sys`: those no rule's leading monomial
divides (as an infix). -/
def NormalFormMonomial (ord : AdmissibleOrder G) (sys : RewritingSystem G k)
    (m : Monomial G) : Prop :=
  ∀ r ∈ sys.rules, ¬ (r.lm ord) <:+: m

/-- **The conclusion of the composition lemma**, as a proposition about the
quotient: the classes of the normal-form monomials form a `k`-basis of
`A = k⟨G⟩ / (Σ)`.

`composition_lemma` states only `reduce (reduce f) = reduce f` and asserts *this*
in its docstring. Anything wanting the PBW/monomial-basis conclusion — the Hecke
route to `H_k` for `k > 4`, the flatness argument, the "monomial basis of `A`"
half of the main theorem — needs this, and can now name it. -/
def NormalFormBasis [DecidableEq k] (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k) : Prop :=
  ∃ B : Module.Basis {m : Monomial G // NormalFormMonomial ord sys m} k (QuotAlg sys),
    ∀ m : {m : Monomial G // NormalFormMonomial ord sys m},
      B m = toQuot sys (FreeAlg.mk (AlgElement.single m.val (1 : k)))


/-! ## §6  The Composition–Diamond lemma, named and cited

Bokut, Chen & Li, *Gröbner–Shirshov bases for categories*, arXiv:1101.1563,
Theorem 4.4, proves for a small category `C(X)` that the following are
equivalent:

* **(i)** `S` is a Gröbner–Shirshov basis in `kC(X)`;
* **(ii)** `f ∈ Id(S) ⇒ f̄ = a·s̄·b` for some `s ∈ S` and words `a, b`;
* **(iii)** `Irr(S) = {u | u ≠ a·s̄·b}` is a linear basis of `kC(X)/Id(S)`.

and closes with the Remark that decides its relevance here:

> If the category in Theorem 4.4 has only one object, then Theorem 4.4 is exact
> Composition-Diamond lemma for free associative algebras.

**The one-object case is precisely this development's setting.** So Theorem 4.4
is the statement UGB's remaining standing axiom `local_confluence` stands in
for, together with the termination theorem `reduction_well_founded` (an axiom
until 2026-11-20) — five axioms when this was written, before Newman's lemma
discharged `confluence` and `normal_form_unique` and the false
`normal_form_exists` was replaced by a theorem. Its clause (iii) is
`NormalFormBasis` above — the paper's `Irr(S)` is `{u | u ≠ a·s̄·b}`, which is
`NormalFormMonomial`'s "no rule's leading monomial is an infix", the same
condition.

Naming it gives the framework a single citable target in place of five
assumptions, and makes the Hecke consequence below statable. -/

/-- **Composition–Diamond lemma**, one-object case: being a Gröbner–Shirshov
basis is equivalent to the normal-form monomials being a basis of the quotient.

Bokut–Chen–Li 2011, Theorem 4.4 (i) ⟺ (iii), via the Remark on one-object
categories. Stated, not proved — see the section note. -/
def CompositionDiamond [DecidableEq k] (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k) : Prop :=
  IsGrobnerShirshovBasis G k ord sys ↔ NormalFormBasis ord sys

/-- **What a failed GS basis costs**, once the CD-lemma is available: the normal
forms of a non-confluent system are *not* a basis of the algebra it presents.

This is why the Bokut–Shiao completion is not optional for the Hecke route to
`H_k`, `k > 4`. `UGB.GrobnerShirshov.Hecke.hecke_not_gs_basis_four` refutes
clause (i) for the uncompleted system at `n = 4`; by Theorem 4.4 clause (iii)
fails too, so its 24 reduced words cannot be assumed to be a basis of
`kC(X)/Id(S)` — they have to be obtained some other way, which is exactly what
`QOU.Machinery.HeckeH4AlgebraLaws` does by hand, and exactly what does not scale
past `n = 4`. -/
theorem not_normalFormBasis_of_not_gs [DecidableEq k] {ord : AdmissibleOrder G}
    {sys : RewritingSystem G k} (hcd : CompositionDiamond ord sys)
    (hnot : ¬ IsGrobnerShirshovBasis G k ord sys) : ¬ NormalFormBasis ord sys :=
  fun hb => hnot (hcd.mpr hb)

end UGB.GrobnerShirshov
