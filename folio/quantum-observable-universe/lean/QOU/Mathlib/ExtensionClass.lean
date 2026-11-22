import QOU.QuantumObservableUniverse.SelfDualSES
import Mathlib.RingTheory.SimpleModule.Basic
import Mathlib.LinearAlgebra.Projection
import Mathlib.Tactic

/-!
# QOU.Mathlib.ExtensionClass — the topological charge as a splitting obstruction

Beans `qou-fngs`, `qou-zut2`. The corpus reaches its topological integer **two**
ways, neither of them homotopy theory. A third candidate was on the books; this
file supplies the algebra that removes it.

* **Residue.** `conj:topological-charge-quantization` gives
  `Res_q(ω, 1) = Φ(Res_ξ(ω)) = 1`, called there "the algebraic counterpart of
  the Gauss–Bonnet theorem". Its `lean.ref` is a `stub` and resolves to no
  declaration.
* **Winding.** `winding-parity-sign-transport` reads the exponent `n` in
  `(σ₁σ₂⁻¹)ⁿ` as a winding number.
* **Extension class — withdrawn 2026-08-24.** `phase-transition-boundary`
  stated that the mixed-channel Hecke representation is a **non-split**
  extension `0 → V_sym → V_mixed → V_asym → 0` classified by
  `Ext¹_{H_n(q)}(V_asym, V_sym) ≅ ℤ`. There is no such class.

## Why the homological route is gone

Three of the reasons are algebra this file now carries.

`isSplit_of_isSemisimpleRing` — over a semisimple algebra **every** short exact
sequence of modules splits, so `Ext¹` vanishes on every pair and there is
nothing left to classify. `prop:knot-eigenbasis-complete`(1) puts `H_n(q₀)`
exactly there: Jimbo's theorem at a `q₀` that the substrate axiom
(`def:substrate-parameter`) forbids from being a root of unity.

`isCompl_ker_quadratic` — the same splitting from the Hecke quadratic alone,
with no semisimplicity input. `rem:hecke-algebra-from-braiding` already names
the two channels as the `q` and `−q⁻¹` eigenspaces of `σ` on `S²V ⊕ Λ²V`; those
eigenspaces are complementary as soon as `[2]_q = q + q⁻¹` is a unit, which is
the very quantity `phase-transition-boundary` divides its critical temperatures
by. The block presupposed the splitting it went on to deny.

The third reason needs no Lean: `Ext¹_A(M, N)` for a `k`-algebra `A` is a
`k`-module, and this block's ground ring is pinned to `ℝ` by its own `.ts` note
and its own Lean sibling (`abbrev R_q := ℝ`). A real vector space is divisible
and torsion-free, so it is never `≅ ℤ` unless it is `0`. Relocating to a root of
unity would not have helped — there the group is a `ℂ`-vector space.

## What is proved here

**The charge is the failure to split**, and the two ways of saying "it splits"
agree.

`hasRetraction_of_hasSection` is the splitting lemma over any ring, in the
direction actually needed here: a section produces a retraction. The converse
holds too and is not proved — nothing below uses it, and claiming an `iff` I did
not prove is the defect this session spent its time removing.

`isCompl_of_isSplit` is the payoff: a split sequence exhibits `range incl` as a
direct summand, so the middle term is determined by its ends and there is
nothing left for a class in `Ext¹` to record. `isSplit_of_isCompl` is its
converse and the engine of both splitting theorems below.

## The relation to the surviving two routes

`selfDual_isSplit`: the `⋆_q` eigenspace sequence `0 → Ω⁻ → Ω² → Ω²/Ω⁻ → 0`
**splits** whenever `2` is invertible. So it carries **no** charge. That is not
a disappointment, it is the point — it says the topological charge does not live
in the self-duality decomposition, and looking for it there is looking in the
wrong sequence.

The sym/asym sequence is now in the same position, for a sharper reason:
`heckeSES_isSplit` shows it splits on the Hecke quadratic alone. So neither
eigenspace sequence the corpus writes down carries a class, and the integer has
to come from the residue or the winding route or not at all.

One asymmetry between the two is worth keeping. Over `R_q = ℤ[q, q⁻¹]` the
number `2` is **not** invertible (`R_q = ℤ[ℤ]` has units `± qⁿ`), so
`selfDual_isSplit` does not apply over the ground ring at all — exactly the
boundary `rem:self-dual-ses` crosses between its two sentences. `[2]_q` has no
such problem: it is a unit in the archimedean realisation for every `q₀ > 0`,
which is why the Hecke splitting needs no wall-crossing.

`Submodule.exists_isCompl` needs a `DivisionRing`, and that gap is real:
complements are not automatic over a ring, which is why `Ext¹` can be nonzero
somewhere. It is just not nonzero here.

-- Ref: [leitner2026] quantum-observable-universe/information-theory
-/

namespace QOU.Mathlib.ExtensionClass

open QOU.SelfDualSES

universe u v

variable {R : Type u} [Ring R]
variable {C B A : Type v} [AddCommGroup C] [Module R C]
    [AddCommGroup B] [Module R B] [AddCommGroup A] [Module R A]

/-- **A short exact sequence** `0 → C → B → A → 0` of `R`-modules.

    Bundled because the splitting question is about the *sequence*, not about
    any one of its maps: `B` can be a direct sum in more than one way, and it is
    the compatibility with `incl` and `proj` that an extension class records. -/
structure SES (R : Type u) [Ring R] (C B A : Type v)
    [AddCommGroup C] [Module R C] [AddCommGroup B] [Module R B]
    [AddCommGroup A] [Module R A] where
  /-- The inclusion of the sub-object. -/
  incl : C →ₗ[R] B
  /-- The projection to the quotient. -/
  proj : B →ₗ[R] A
  /-- Exactness on the left. -/
  incl_injective : Function.Injective incl
  /-- Exactness on the right. -/
  proj_surjective : Function.Surjective proj
  /-- Exactness in the middle: `range incl = ker proj`. -/
  exact : Function.Exact incl proj

variable (S : SES R C B A)

theorem range_incl_eq_ker_proj :
    LinearMap.range S.incl = LinearMap.ker S.proj :=
  (LinearMap.exact_iff.mp S.exact).symm

/-- **Right splitting**: the projection admits a section. -/
def HasSection : Prop := ∃ s : A →ₗ[R] B, ∀ a, S.proj (s a) = a

/-- **Left splitting**: the inclusion admits a retraction. -/
def HasRetraction : Prop := ∃ r : B →ₗ[R] C, ∀ c, r (S.incl c) = c

/-- **The splitting lemma**, right to left.

    A section `s` makes `b - s (proj b)` land in `ker proj = range incl`, and
    `incl` is injective, so that element has a unique preimage in `C`. The
    retraction sends `b` there. -/
theorem hasRetraction_of_hasSection (h : HasSection S) : HasRetraction S := by
  obtain ⟨s, hs⟩ := h
  -- `b - s (proj b)` lies in `ker proj`, hence in `range incl`
  have hmem : ∀ b : B, b - s (S.proj b) ∈ LinearMap.range S.incl := by
    intro b
    rw [range_incl_eq_ker_proj]
    simp [LinearMap.mem_ker, hs]
  -- the linear map `b ↦ b - s (proj b)`, corestricted to `range incl`
  let e : B →ₗ[R] B := LinearMap.id - s.comp S.proj
  have he : ∀ b, e b = b - s (S.proj b) := fun _ => rfl
  -- invert `incl` on its range
  let inclEquiv : C ≃ₗ[R] LinearMap.range S.incl :=
    LinearEquiv.ofInjective S.incl S.incl_injective
  refine ⟨(inclEquiv.symm.toLinearMap).comp (e.codRestrict _ (fun b => (he b) ▸ hmem b)), ?_⟩
  intro c
  have : e (S.incl c) = S.incl c := by
    rw [he]
    have : S.proj (S.incl c) = 0 := by
      have : S.incl c ∈ LinearMap.ker S.proj := by
        rw [← range_incl_eq_ker_proj]; exact ⟨c, rfl⟩
      simpa using this
    rw [this]
    simp
  show inclEquiv.symm ⟨e (S.incl c), _⟩ = c
  simp only [this]
  exact inclEquiv.symm_apply_apply c

/-- The sequence splits. Unambiguous by the splitting lemma above. -/
def IsSplit : Prop := HasSection S

/-- **A split sequence is a direct sum**, so it carries no extension data.

    This is why "the charge is the failure to split" is the right reading: a
    split sequence is determined by its ends, and there is nothing left for a
    class in `Ext¹` to record. -/
theorem isCompl_of_isSplit (h : IsSplit S) :
    ∃ p : Submodule R B, IsCompl (LinearMap.range S.incl) p := by
  obtain ⟨s, hs⟩ := h
  refine ⟨LinearMap.range s, ?_, ?_⟩
  · rw [Submodule.disjoint_def]
    rintro x hx hxs
    obtain ⟨a, rfl⟩ := hxs
    -- `s a` is in `range incl = ker proj`, so `proj (s a) = 0`; but `proj ∘ s = id`
    have hker : S.proj (s a) = 0 := by
      have hmem : s a ∈ LinearMap.ker S.proj := by
        rw [← range_incl_eq_ker_proj]; exact hx
      simpa using hmem
    have ha : a = 0 := by rw [← hs a]; exact hker
    rw [ha, map_zero]
  · rw [codisjoint_iff_le_sup]
    intro b _
    have hmem : b - s (S.proj b) ∈ LinearMap.range S.incl := by
      rw [range_incl_eq_ker_proj]
      simp [LinearMap.mem_ker, hs]
    have : b = (b - s (S.proj b)) + s (S.proj b) := by abel
    rw [this]
    exact Submodule.add_mem_sup hmem ⟨S.proj b, rfl⟩

/-- **A direct-summand decomposition splits the sequence** — the converse of
    `isCompl_of_isSplit`.

    Given a complement `p` to `range incl = ker proj`, the projection restricted
    to `p` is a bijection onto `A`: injective because `p` meets `ker proj`
    trivially, surjective because every `b` is a sum of something in `ker proj`
    and something in `p`. Its inverse, followed by the inclusion of `p`, is the
    section. -/
theorem isSplit_of_isCompl {p : Submodule R B}
    (hp : IsCompl (LinearMap.range S.incl) p) : IsSplit S := by
  let f : p →ₗ[R] A := S.proj ∘ₗ p.subtype
  have hinj : Function.Injective f := by
    rw [injective_iff_map_eq_zero]
    intro x hx
    have hker : (x : B) ∈ LinearMap.range S.incl := by
      rw [range_incl_eq_ker_proj]
      simpa [LinearMap.mem_ker, f] using hx
    have := hp.disjoint.le_bot ⟨hker, x.2⟩
    exact Subtype.ext (by simpa using this)
  have hsurj : Function.Surjective f := by
    intro a
    obtain ⟨b, hb⟩ := S.proj_surjective a
    have hmem : b ∈ LinearMap.range S.incl ⊔ p := by
      rw [codisjoint_iff.mp hp.codisjoint]; trivial
    obtain ⟨c, hc, y, hy, hcy⟩ := Submodule.mem_sup.mp hmem
    have hc0 : S.proj c = 0 := by
      have : c ∈ LinearMap.ker S.proj := by rw [← range_incl_eq_ker_proj]; exact hc
      simpa using this
    refine ⟨⟨y, hy⟩, ?_⟩
    show S.proj y = a
    have hsum : S.proj c + S.proj y = a := by rw [← map_add, hcy, hb]
    rw [hc0, zero_add] at hsum
    exact hsum
  refine ⟨p.subtype ∘ₗ (LinearEquiv.ofBijective f ⟨hinj, hsurj⟩).symm.toLinearMap, ?_⟩
  intro a
  exact (LinearEquiv.ofBijective f ⟨hinj, hsurj⟩).apply_symm_apply a

/-! ### Semisimplicity leaves nothing to classify

The module-theoretic content of `Ext¹ = 0`, stated without Ext. -/

/-- **Every short exact sequence with semisimple middle term splits.**

    Semisimplicity is exactly the statement that every submodule is a direct
    summand, so `ker proj` has a complement and `isSplit_of_isCompl` applies. -/
theorem isSplit_of_isSemisimpleModule (h : IsSemisimpleModule R B) : IsSplit S := by
  haveI := h
  obtain ⟨p, hp⟩ := exists_isCompl (LinearMap.range S.incl)
  exact isSplit_of_isCompl S hp

/-- **Over a semisimple algebra there are no non-split extensions at all.**

    This is what `Ext¹_{H_n(q)}(V_asym, V_sym) ≅ ℤ` runs into.
    `prop:knot-eigenbasis-complete`(1) makes `H_n(q₀) ≅ ℂ[S_n]` semisimple at
    the substrate (Jimbo, `q₀` not a root of unity), and then **no** pair of
    `H_n(q₀)`-modules admits a non-split extension — not the sym/asym pair and
    not any other. There is no group to be `ℤ`. -/
theorem isSplit_of_isSemisimpleRing [IsSemisimpleRing R] : IsSplit S :=
  isSplit_of_isSemisimpleModule S IsSemisimpleRing.isSemisimpleModule

/-! ### The `⋆_q` sequence carries no charge -/

variable {M : Type v} [AddCommGroup M] [Module R M]

/-- The eigenspace sequence of an involution, as an `SES`:
    `0 → Ω⁻ → Ω² → Ω²/Ω⁻ → 0`. Exactness is free (`minus_ses_exact`). -/
def selfDualSES {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M]
    [Module R M] (i : Involution R M) :
    SES R (minusPart i) M (M ⧸ minusPart i) where
  incl := (minusPart i).subtype
  proj := (minusPart i).mkQ
  incl_injective := Subtype.val_injective
  proj_surjective := Submodule.mkQ_surjective _
  exact := minus_ses_exact i

/-- **The self-duality sequence splits, so it has no extension class.**

    Given `2` invertible and no 2-torsion, `Ω⁺` is a complement to `Ω⁻`
    (`isCompl_plus_minus`), and the quotient map restricted to it is the
    section.

    Read together with the module docstring: this says the topological charge
    does **not** live in the `⋆_q` decomposition. And it does not even say that
    over the ground ring — `2` is not invertible in `R_q = ℤ[q, q⁻¹]`, so the
    hypothesis fails there and the sequence is not known to split at all. -/
theorem selfDual_isSplit {R : Type u} [CommRing R] [Invertible (2 : R)]
    {M : Type v} [AddCommGroup M] [Module R M] (i : Involution R M)
    (htors : ∀ y : M, y + y = 0 → y = 0) :
    IsSplit (selfDualSES i) := by
  -- the section is `M/Ω⁻ ≃ Ω⁺ ↪ M`
  refine ⟨(plusPart i).subtype.comp (quotMinusEquivPlus i htors).toLinearMap, ?_⟩
  intro x
  -- `mkQ ∘ subtype` IS the inverse of the quotient equivalence
  show (minusPart i).mkQ ((quotMinusEquivPlus i htors) x : M) = x
  have hsymm := Submodule.quotientEquivOfIsCompl_symm_apply
    (minusPart i) (plusPart i) ((isCompl_plus_minus i htors).symm)
    ((quotMinusEquivPlus i htors) x)
  rw [show (minusPart i).mkQ ((quotMinusEquivPlus i htors) x : M)
      = Submodule.Quotient.mk ((quotMinusEquivPlus i htors) x : M) from rfl, ← hsymm]
  exact (quotMinusEquivPlus i htors).symm_apply_apply x

/-! ### The sym/asym sequence carries no charge either

`rem:hecke-algebra-from-braiding` gives the braiding `σ = τ(c_{V,V})` the
quadratic `(σ − q)(σ + q⁻¹) = 0` and names its two eigenvalues as the weights of
`S²V` and `Λ²V`. Those two eigenspaces are complementary the moment
`[2]_q = q + q⁻¹` is a unit — no semisimplicity, no root-of-unity hypothesis, no
statement about the base ring beyond that one inverse. -/

/-- **A quadratic with invertible eigenvalue gap splits its eigenspaces.**

    With `a = q` and `b = q⁻¹` this is the Hecke relation, and `a + b = [2]_q`.
    The splitting is explicit: `x = u·(f x + b·x) + u·(a·x − f x)` for
    `u = [2]_q⁻¹`, the first summand killed by `f − a` and the second by
    `f + b`. Nothing else is used, so the conclusion holds over any commutative
    ring in which `[2]_q` is invertible — in particular over `ℝ` at every
    `q₀ > 0`, and over `ℤ[q, q⁻¹]` it does not, which is the only place the
    question could still have been open. -/
theorem isCompl_ker_quadratic {R : Type u} [CommRing R] {M : Type v}
    [AddCommGroup M] [Module R M] (f : M →ₗ[R] M) (a b : R)
    (hquad : (f - a • LinearMap.id) ∘ₗ (f + b • LinearMap.id) = (0 : M →ₗ[R] M))
    (hab : IsUnit (a + b)) :
    IsCompl (LinearMap.ker (f - a • LinearMap.id))
      (LinearMap.ker (f + b • LinearMap.id)) := by
  obtain ⟨v, hv⟩ := hab
  set u : R := ((v⁻¹ : Rˣ) : R) with hu_def
  have hu : u * (a + b) = 1 := by rw [hu_def, ← hv]; exact v.inv_mul
  -- the quadratic, pointwise: `f² = (a − b)·f + a·b`
  have key : ∀ x : M, f (f x) = (a - b) • f x + (a * b) • x := by
    intro x
    have h := LinearMap.congr_fun hquad x
    simp only [LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.add_apply,
      LinearMap.smul_apply, LinearMap.id_apply, LinearMap.zero_apply, map_add,
      map_smul] at h
    have h2 : f (f x) + b • f x - (a • f x + (a * b) • x) = 0 := by
      rw [← h]; module
    linear_combination (norm := module) h2
  constructor
  · -- an element in both eigenspaces satisfies `(a + b)·x = 0`
    rw [Submodule.disjoint_def]
    intro x hx hy
    simp only [LinearMap.mem_ker, LinearMap.sub_apply, LinearMap.add_apply,
      LinearMap.smul_apply, LinearMap.id_apply, sub_eq_zero,
      add_eq_zero_iff_eq_neg] at hx hy
    have hsum : (a + b) • x = 0 := by
      have : a • x + b • x = 0 := by rw [← hx, hy]; module
      rw [add_smul]; exact this
    calc x = (u * (a + b)) • x := by rw [hu, one_smul]
      _ = u • ((a + b) • x) := by rw [mul_smul]
      _ = 0 := by rw [hsum, smul_zero]
  · -- and every element is the sum of its two eigencomponents
    rw [codisjoint_iff_le_sup]
    intro x _
    have hc : u • (f x + b • x) ∈ LinearMap.ker (f - a • LinearMap.id) := by
      have h0 : (f - a • LinearMap.id : M →ₗ[R] M) (f x + b • x) = 0 := by
        have h := LinearMap.congr_fun hquad x
        simp only [LinearMap.comp_apply, LinearMap.add_apply, LinearMap.smul_apply,
          LinearMap.id_apply, LinearMap.zero_apply] at h
        exact h
      simp only [LinearMap.mem_ker, map_smul, h0, smul_zero]
    have hy : u • (a • x - f x) ∈ LinearMap.ker (f + b • LinearMap.id) := by
      have h0 : (f + b • LinearMap.id : M →ₗ[R] M) (a • x - f x) = 0 := by
        simp only [LinearMap.add_apply, LinearMap.smul_apply, LinearMap.id_apply,
          map_sub, map_smul]
        rw [key x]
        module
      simp only [LinearMap.mem_ker, map_smul, h0, smul_zero]
    have hx : x = u • (f x + b • x) + u • (a • x - f x) := by
      have hxx : u • (f x + b • x) + u • (a • x - f x) = (u * (a + b)) • x := by
        rw [mul_smul, add_smul]; module
      rw [hxx, hu, one_smul]
    rw [hx]
    exact Submodule.add_mem_sup hc hy

/-- The eigenspace sequence of a Hecke generator, as an `SES`:
    `0 → ker(σ − q) → M → M ⧸ ker(σ − q) → 0`. Exactness is free, exactly as for
    `selfDualSES`; writing the sequence down proves nothing. -/
def heckeSES {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]
    (f : M →ₗ[R] M) (a : R) :
    SES R (LinearMap.ker (f - a • LinearMap.id)) M
      (M ⧸ LinearMap.ker (f - a • LinearMap.id)) where
  incl := (LinearMap.ker (f - a • LinearMap.id)).subtype
  proj := (LinearMap.ker (f - a • LinearMap.id)).mkQ
  incl_injective := Subtype.val_injective
  proj_surjective := Submodule.mkQ_surjective _
  exact := LinearMap.exact_iff.mpr (by rw [Submodule.ker_mkQ, Submodule.range_subtype])

/-- **The sym/asym sequence splits.**

    This is the refutation of `0 → V_sym → V_mixed → V_asym → 0` being
    non-split, stated over the weakest hypothesis that suffices: the Hecke
    quadratic and `[2]_q` invertible. It does not go through semisimplicity, so
    it survives even a reader who rejects `prop:knot-eigenbasis-complete`(1). -/
theorem heckeSES_isSplit {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M]
    [Module R M] (f : M →ₗ[R] M) (a b : R)
    (hquad : (f - a • LinearMap.id) ∘ₗ (f + b • LinearMap.id) = (0 : M →ₗ[R] M))
    (hab : IsUnit (a + b)) :
    IsSplit (heckeSES f a) := by
  refine isSplit_of_isCompl (heckeSES f a) (p := LinearMap.ker (f + b • LinearMap.id)) ?_
  have hrange : LinearMap.range (heckeSES f a).incl
      = LinearMap.ker (f - a • LinearMap.id) := Submodule.range_subtype _
  rw [hrange]
  exact isCompl_ker_quadratic f a b hquad hab

/-! ### Where the eigenvalue gap can vanish — and where it cannot

`QOU/Mathlib/HeckeExtOne.lean` computes the classification of these extensions
as `R / (α − β)`, so everything turns on the *difference* of the two
eigenvalues. Bean `qou-oyty` records that the corpus carries two Hecke
normalisations and that the difference is not invariant under the rescaling
between them. The two lemmas below locate the degenerate locus for the
normalisation `phase-transition-boundary` actually uses. -/

/-- **`[2]_q = q + q⁻¹` vanishes exactly on `q² + 1 = 0`.**

    The inverse is carried as a hypothesis `q * u = 1` rather than written
    `q⁻¹`, because `R_q = ℤ[q, q⁻¹]` is a ring with no `Inv` instance even
    though `q` is invertible in it (`QOU.GroundRing`).

    In the corpus's normalisation `(σ − q)(σ + q⁻¹) = 0`
    (`rem:hecke-algebra-from-braiding`) the eigenvalue difference is
    `q − (−q⁻¹) = q + q⁻¹`, so this is the locus where the symmetric and
    antisymmetric channels collide — `q = ±i`, not `q = −1`. -/
theorem twoQ_eq_zero_iff {R : Type u} [CommRing R] {q u : R} (hu : q * u = 1) :
    q + u = 0 ↔ q * q + 1 = 0 := by
  constructor
  · intro h
    have h1 : q * (q + u) = 0 := by rw [h, mul_zero]
    rw [mul_add, hu] at h1
    exact h1
  · intro h
    have h1 : q * (q + u) = 0 := by rw [mul_add, hu]; exact h
    calc q + u = (u * q) * (q + u) := by rw [mul_comm u q, hu, one_mul]
      _ = u * (q * (q + u)) := by ring
      _ = 0 := by rw [h1, mul_zero]

/-- **The gap never vanishes over an ordered field.** `q² + 1 ≥ 1 > 0`.

    So the collision locus of the corpus's normalisation is not reached by any
    real substrate value — root of unity or not. Relocating a non-split
    extension to a degenerate `q` is therefore unavailable on the archimedean
    side of the §7c wall, where `phase-transition-boundary` lives. -/
theorem twoQ_ne_zero_of_ordered {R : Type u} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] {q : R} (hq : q ≠ 0) : q + q⁻¹ ≠ 0 := by
  intro h
  have h1 : q * (q + q⁻¹) = 0 := by rw [h, mul_zero]
  rw [mul_add, mul_inv_cancel₀ hq] at h1
  nlinarith [mul_self_nonneg q]

/-- **The sym/asym sequence splits at every real substrate value.**

    Not only at `q₀ ≈ 1.1099`, and not only away from roots of unity: at
    *every* nonzero `q` in an ordered field. This is the archimedean form of
    the refutation, and it is the reason the withdrawn claim cannot be rescued
    by moving it to a degenerate `q` — in this normalisation there is no real
    degenerate `q` to move it to. -/
theorem heckeSES_isSplit_of_ordered {R : Type u} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] {M : Type v} [AddCommGroup M] [Module R M]
    (f : M →ₗ[R] M) {q : R} (hq : q ≠ 0)
    (hquad : (f - q • LinearMap.id) ∘ₗ (f + q⁻¹ • LinearMap.id)
      = (0 : M →ₗ[R] M)) :
    IsSplit (heckeSES f q) :=
  heckeSES_isSplit f q q⁻¹ hquad (isUnit_iff_ne_zero.mpr (twoQ_ne_zero_of_ordered hq))

end QOU.Mathlib.ExtensionClass
