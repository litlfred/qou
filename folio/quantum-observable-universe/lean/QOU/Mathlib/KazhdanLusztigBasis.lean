import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Basis.Defs
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Tactic

/-!
# QOU.Mathlib.KazhdanLusztigBasis — what a Kazhdan–Lusztig basis IS

Bean `qou-gmfz`. `QOU/BraidKnot/KazhdanLusztigClassicalLimit.lean` states the
conjecture that the KLR canonical basis flattens to the Kazhdan–Lusztig basis
of `ℤ[Sₙ]`, but its class carries

    KLBasisElt : Type u

an **arbitrary type** with no Kazhdan–Lusztig structure — no bar involution, no
self-duality, no indexing by the Coxeter group. Any type at all satisfies that
signature, `PUnit` included, which is exactly how the retired `canonical`
instance discharged the conjecture. "Flattens to the KL basis" was therefore not
stated at all.

This module supplies the missing structure, so a downstream class can *require*
its basis type to be a Kazhdan–Lusztig basis rather than permit it to be
anything.

## What this is, and deliberately is not

It is a **specification**, not a construction. `KLBasis` records the defining
properties; nothing here builds one, and nothing here asserts one exists.

That is the honest shape and not a shortcut. Existence of the KL basis is the
Kazhdan–Lusztig theorem, and proving it needs the Iwahori–Hecke algebra of a
Coxeter system, its `T`-basis, the bar involution `q ↦ q⁻¹`,
`T_w ↦ (T_{w⁻¹})⁻¹`, and the degree-bounded unitriangularity that pins the
`P_{v,w}`. **Mathlib has none of it** — checked against this tree's olean set on
2026-08-25: `Mathlib.GroupTheory.Coxeter.{Basic, Inversion, Length, Matrix}`
exist, and there is no Hecke algebra and no Kazhdan–Lusztig anything. Writing a
construction here would mean inventing that machinery, and inventing it in order
to discharge a conjecture stated in terms of it is the same move the bean was
opened to undo.

So: state the specification, prove what follows from it, and let the conjecture
say it is conjectural.

## What the specification buys — the anti-`PUnit` theorem

`nontrivial_of_klBasis` is the point. A `KLBasis` is a `Basis W R M`, so its
elements are linearly independent and each is nonzero over a nontrivial ring.
`PUnit` cannot carry one for any nonempty `W`. Requiring `KLBasisElt` to index a
`KLBasis` is therefore a *constraint*, where `KLBasisElt : Type u` was not.

`bar_smul_self_iff` is the second half: bar-invariance is not automatic. On
`r • C w` it holds exactly when `r` is fixed by the scalar involution, so the
bar-invariant part of the module is cut out by the fixed ring — which is the
content the old `KLBasisElt` had no room to express.

-- Ref: [leitner2026] quantum-observable-universe/knots-particles-confinement
-/

namespace QOU.Mathlib.KL

universe u v

/-- **A bar involution.**

    Semilinearity is written out (`barM_smul`) rather than routed through
    Mathlib's `σ`-semilinear maps, because the only thing needed downstream is
    the compatibility equation itself and the `LinearMap.semilinear` route would
    force a `RingHomInvPair` instance for a ring map that is only involutive.

    For the QOU ground ring `R_q = ℤ[q, q⁻¹]` this is `q ↦ q⁻¹`; nothing here
    depends on that, and the structure is stated over an arbitrary `CommRing` so
    the §7c base-ring wall is respected. -/
structure BarInvolution (R : Type u) (M : Type v)
    [CommRing R] [AddCommGroup M] [Module R M] where
  /-- The involution on scalars — `q ↦ q⁻¹` in the motivating case. -/
  barR : R →+* R
  /-- …which is an involution. -/
  barR_invol : Function.Involutive barR
  /-- The involution on the module. -/
  barM : M →+ M
  /-- …which is an involution. -/
  barM_invol : Function.Involutive barM
  /-- Semilinearity: `bar` twists scalars by `barR`. -/
  barM_smul : ∀ (r : R) (m : M), barM (r • m) = barR r • barM m

namespace BarInvolution

variable {R : Type u} {M : Type v} [CommRing R] [AddCommGroup M] [Module R M]

@[simp] theorem barR_barR (B : BarInvolution R M) (r : R) : B.barR (B.barR r) = r :=
  B.barR_invol r

@[simp] theorem barM_barM (B : BarInvolution R M) (m : M) : B.barM (B.barM m) = m :=
  B.barM_invol m

/-- `barM` is bijective — an involution always is. -/
theorem barM_bijective (B : BarInvolution R M) : Function.Bijective B.barM :=
  B.barM_invol.bijective

/-- The scalars fixed by `barR` form a subring; membership is the predicate that
    decides bar-invariance of a scalar multiple (`bar_smul_self_iff`). -/
def IsBarFixed (B : BarInvolution R M) (r : R) : Prop := B.barR r = r

end BarInvolution

/-- **A Kazhdan–Lusztig basis, as a specification.**

    `basis` is the substantive field: a KL basis is a *basis*, indexed by the
    Coxeter group. That single requirement is what `KLBasisElt : Type u` was
    missing, and it is what rules out `PUnit`.

    `bar_invariant` is the KL self-duality `\overline{C_w} = C_w`, the property
    that (together with degree-bounded unitriangularity against the `T`-basis)
    characterises the basis uniquely.

    **Not included: unitriangularity.** `C_w = T_w + Σ_{v < w} P_{v,w} T_v` with
    `deg P_{v,w} ≤ (ℓ(w) − ℓ(v) − 1)/2` needs the `T`-basis and the Bruhat
    order, i.e. the Hecke algebra this tree does not have. Its absence is why
    this is a specification of what a KL basis *satisfies* rather than a
    characterisation that pins it: two different bar-invariant bases both
    inhabit `KLBasis`. Downstream may therefore use this to *constrain*, never
    to conclude uniqueness. -/
structure KLBasis (W : Type u) (R : Type u) (M : Type v)
    [CommRing R] [AddCommGroup M] [Module R M] (B : BarInvolution R M) where
  /-- The basis itself, indexed by the group. -/
  basis : Module.Basis W R M
  /-- Kazhdan–Lusztig self-duality. -/
  bar_invariant : ∀ w : W, B.barM (basis w) = basis w

namespace KLBasis

variable {W R : Type u} {M : Type v}
variable [CommRing R] [AddCommGroup M] [Module R M] {B : BarInvolution R M}

/-- Every KL basis element is nonzero. -/
theorem ne_zero [Nontrivial R] (K : KLBasis W R M B) (w : W) : K.basis w ≠ 0 :=
  K.basis.ne_zero w

/-- Distinct group elements give distinct basis elements. -/
theorem basis_injective [Nontrivial R] (K : KLBasis W R M B) :
    Function.Injective K.basis :=
  K.basis.injective

/-- **The anti-`PUnit` theorem, and the reason this file exists.**

    A module carrying a KL basis indexed by a nonempty `W` is nontrivial. So
    `KLBasisElt := PUnit` — the value the retired `canonical` instance used to
    discharge `conj:kazhdan-lusztig-classical-limit` — cannot inhabit this
    structure, and a downstream class that requires a `KLBasis` is stating a
    constraint rather than a signature anything satisfies. -/
theorem nontrivial_of_klBasis [Nontrivial R] [Nonempty W]
    (K : KLBasis W R M B) : Nontrivial M :=
  ⟨K.basis (Classical.arbitrary W), 0, K.ne_zero _⟩

/-- **Bar-invariance is not automatic, and this says exactly when it holds.**

    `barM` fixes the basis but is *semilinear*, so it does not fix the module:
    on `r • C w` it acts by `barR r`. The scalar multiple is bar-invariant
    precisely when the scalar is fixed by `barR`.

    This is the content that `KLBasisElt : Type u` had no room to express — with
    no bar and no basis, "bar-invariant" was not a condition on anything. -/
theorem bar_smul (K : KLBasis W R M B) (r : R) (w : W) :
    B.barM (r • K.basis w) = B.barR r • K.basis w :=
  -- Term mode deliberately. The tactic form `rw [B.barM_smul, K.bar_invariant]`
  -- left `w` as an unsolved `case w : W` — `rw` has to guess the index from the
  -- rewritten side, and here it cannot. Nothing is inferred below.
  (B.barM_smul r (K.basis w)).trans
    (congrArg (fun m : M => B.barR r • m) (K.bar_invariant w))

/-- **The scalar-multiple form of KL self-duality.** `r • C w` is bar-invariant
    exactly when `r` is fixed by `barR`.

    `Nontrivial R` is needed for the forward direction — over the zero ring
    every element is `0` and the statement is empty, which is the ring-level
    analogue of the vacuity this module exists to prevent. -/
theorem bar_smul_self_iff [Nontrivial R] (K : KLBasis W R M B) (r : R) (w : W) :
    B.barM (r • K.basis w) = r • K.basis w ↔ B.IsBarFixed r := by
  constructor
  · -- Push the equation of vectors through the linear equiv `repr` and read off
    -- the `w` coordinate: `repr (basis w) = single w 1`, so each side's
    -- coefficient there is its own scalar.
    intro h
    rw [K.bar_smul r w] at h
    have h1 := congrArg (fun m : M => K.basis.repr m w) h
    simpa using h1
  · -- `IsBarFixed` is a `def … : Prop` — it IS the equation, so it is used
    -- rather than rewritten with.
    intro h
    exact (K.bar_smul r w).trans (congrArg (fun c : R => c • K.basis w) h)

end KLBasis

/-! ### Instantiating the ground ring — deliberately not done here

    The motivating case is `R_q = ℤ[q, q⁻¹] = LaurentPolynomial ℤ` with the bar
    involution `q ↦ q⁻¹`, which Mathlib provides as
    `LaurentPolynomial.invert` (an `AlgEquiv`, so it reaches `BarInvolution.barR`
    through `toRingEquiv.toRingHom`).

    Building the `BarInvolution` needs `barR_invol`, i.e.
    `invert (invert f) = f`. That is certainly true and certainly provable, and
    it is left undone rather than guessed: this checkout carries Mathlib as
    **oleans only** — `.lake/packages/mathlib/` has no source tree — so the
    lemma cannot be located by search, `LaurentPolynomial.invert_invert` does
    not exist, and `simp` does not close it. Writing a `sorry` for a lemma this
    shallow would put `sorryAx` into the axiom set of everything downstream for
    the sake of a name lookup.

    Follow-up, cheap for anyone with Mathlib sources to hand: find or prove
    `Function.Involutive LaurentPolynomial.invert`, then the `BarInvolution` on
    `R_q` is immediate and this file stops being purely abstract. Tracked on
    bean `qou-gmfz`. -/

end QOU.Mathlib.KL
