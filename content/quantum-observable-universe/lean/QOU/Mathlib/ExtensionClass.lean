import QOU.QuantumObservableUniverse.SelfDualSES
import Mathlib.LinearAlgebra.Projection
import Mathlib.Tactic

/-!
# QOU.Mathlib.ExtensionClass — the topological charge as a splitting obstruction

Bean `qou-fngs`. The corpus reaches its topological integer three ways, none of
them homotopy theory. This file builds the second and relates it to the other
two.

* **Residue.** `thm:topological-charge-quantization` gives
  `Res_q(ω, 1) = Φ(Res_ξ(ω)) = 1`, called there "the algebraic counterpart of
  the Gauss–Bonnet theorem". Its `lean.ref` is a `stub` and resolves to no
  declaration.
* **Extension class.** `phase-transition-boundary` states that the mixed-channel
  Hecke representation is a **non-split** extension
  `0 → V_sym → V_mixed → V_asym → 0`, classified by
  `Ext¹_{H_n(q)}(V_asym, V_sym) ≅ ℤ`, with the Hopf invariant of `π₃(S²)` named
  as the *generator*. Homotopy supplies the interpretation; homological algebra
  supplies the integer.
* **Winding.** `winding-parity-sign-transport` reads the exponent `n` in
  `(σ₁σ₂⁻¹)ⁿ` as a winding number.

## What is actually proved here

Not `Ext¹ ≅ ℤ` — that needs the Hecke modules themselves. What is proved is the
part the corpus's argument turns on: **the charge is the failure to split**, and
the two ways of saying "it splits" agree.

`hasRetraction_of_hasSection` is the splitting lemma over any ring, in the
direction actually needed here: a section produces a retraction. The converse
holds too and is not proved — nothing below uses it, and claiming an `iff` I did
not prove is the defect this session spent its time removing.

`isCompl_of_isSplit` is the payoff: a split sequence exhibits `range incl` as a
direct summand, so the middle term is determined by its ends and there is
nothing left for a class in `Ext¹` to record.

## The relation to the other two routes, made precise

`selfDual_isSplit`: the `⋆_q` eigenspace sequence `0 → Ω⁻ → Ω² → Ω²/Ω⁻ → 0`
**splits** whenever `2` is invertible. So it carries **no** charge. That is not
a disappointment, it is the point — it says the topological charge does not live
in the self-duality decomposition, and looking for it there is looking in the
wrong sequence.

Where it does live is the sym/asym sequence, which the corpus asserts is
non-split. And the two statements are consistent in a way worth noticing: over
`R_q = ℤ[q, q⁻¹]` the number `2` is **not** invertible (`R_q = ℤ[ℤ]` has units
`± qⁿ`), so `selfDual_isSplit` does not apply over the ground ring at all. The
splitting is available only after inverting 2, or in the archimedean
realisation — exactly the boundary `rem:self-dual-ses` crosses between its two
sentences.

`Submodule.exists_isCompl` needs a `DivisionRing`. Complements are not
automatic over a ring, and that gap is the obstruction. A theory in which every
sequence split would have no topological charge to quantise.

-- Ref: [manuscript] quantum-observable-universe/information-theory
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

end QOU.Mathlib.ExtensionClass
