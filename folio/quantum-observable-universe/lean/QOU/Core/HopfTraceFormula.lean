import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.LinearAlgebra.Basis.VectorSpace
import Mathlib.LinearAlgebra.FiniteDimensional.Defs

/-!
# Trace is additive over an invariant subspace and its quotient

For an endomorphism `f` of a finite-dimensional vector space `V` preserving a subspace `W`,
`tr f = tr (f|_W) + tr (f on V/W)` (`trace_eq_restrict_add_mapQ`).

Proof: pick a linear section `s` of `π : V → V/W` and the retraction `r = id − s ∘ π` onto `W`,
so `ι ∘ r + s ∘ π = id`. Then `tr f = tr (ι ∘ (r ∘ f)) + tr (s ∘ (π ∘ f))`, and cyclicity turns
the two terms into `tr (r ∘ f ∘ ι) = tr (f|_W)` and `tr (π ∘ f ∘ s) = tr (f on V/W)`.

Bean `qou-h0zz` (step 3, the Hopf trace formula). Linear algebra over a field; no analysis.
-/

namespace QOU.Core.TraceQuotient

open LinearMap Submodule

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V] [FiniteDimensional K V]

/-- **Trace adds over an invariant subspace and its quotient.** -/
theorem trace_eq_restrict_add_mapQ (W : Submodule K V) (f : V →ₗ[K] V)
    (hf : W ≤ W.comap f) :
    trace K V f =
      trace K W (f.restrict (p := W) (q := W) (fun x hx => Submodule.mem_comap.mp (hf hx))) + trace K (V ⧸ W) (W.mapQ W f hf) := by
  obtain ⟨s, hs⟩ := W.mkQ.exists_rightInverse_of_surjective (W.range_mkQ)
  have hsx : ∀ y, W.mkQ (s y) = y := fun y => by
    simpa using congrArg (fun g => g y) hs
  have hmem : ∀ x : V, x - s (W.mkQ x) ∈ W := fun x => by
    rw [← Submodule.Quotient.mk_eq_zero, Submodule.Quotient.mk_sub]
    have := hsx (W.mkQ x); simp only [mkQ_apply] at this ⊢; rw [this, sub_self]
  let r : V →ₗ[K] W :=
    (LinearMap.id - s ∘ₗ W.mkQ).codRestrict W (fun x => by simpa using hmem x)
  have hsplit : W.subtype ∘ₗ r + s ∘ₗ W.mkQ = LinearMap.id := by
    ext x; simp [r]
  have h1 : r ∘ₗ f ∘ₗ W.subtype = f.restrict (p := W) (q := W) (fun x hx => Submodule.mem_comap.mp (hf hx)) := by
    ext ⟨w, hw⟩
    have hfw : W.mkQ (f w) = 0 := by
      simpa [Submodule.Quotient.mk_eq_zero] using hf hw
    simp [r, hfw]
  have h2 : W.mkQ ∘ₗ f ∘ₗ s = W.mapQ W f hf := by
    refine LinearMap.ext fun y => ?_
    conv_rhs => rw [← hsx y]
    simp
  calc trace K V f = trace K V ((W.subtype ∘ₗ r + s ∘ₗ W.mkQ) ∘ₗ f) := by rw [hsplit]; rfl
    _ = trace K V (W.subtype ∘ₗ (r ∘ₗ f)) + trace K V (s ∘ₗ (W.mkQ ∘ₗ f)) := by
        rw [add_comp, map_add, comp_assoc, comp_assoc]
    _ = trace K W ((r ∘ₗ f) ∘ₗ W.subtype) + trace K (V ⧸ W) ((W.mkQ ∘ₗ f) ∘ₗ s) := by
        rw [trace_comp_comm' W.subtype, trace_comp_comm' s]
    _ = _ := by rw [comp_assoc, comp_assoc, h1, h2]

/-- Intertwined endomorphisms have the same trace. -/
theorem trace_eq_of_intertwine {M N : Type*} [AddCommGroup M] [Module K M] [FiniteDimensional K M]
    [AddCommGroup N] [Module K N] [FiniteDimensional K N] (e : M ≃ₗ[K] N)
    (g : M →ₗ[K] M) (h : N →ₗ[K] N) (he : ∀ x, h (e x) = e (g x)) :
    trace K M g = trace K N h := by
  rw [← trace_conj' g e]
  congr 1
  refine LinearMap.ext fun y => ?_
  rw [LinearEquiv.conj_apply_apply, ← he, LinearEquiv.apply_symm_apply]

/-- **A permutation of cells has trace the number of fixed cells.** For a finite set `X` of
cells and `σ : Perm X`, the map `y ↦ y ∘ σ⁻¹` on `X → K` has trace `#{x | σ x = x}`. This is
why the chain-level characters `χ_{C_k}(g)` are fixed-cell counts. -/
theorem trace_funLeft_perm {X : Type*} [Fintype X] [DecidableEq X] (σ : Equiv.Perm X) :
    trace K (X → K) (LinearMap.funLeft K K σ.symm) =
      ((Finset.univ.filter (fun x => σ x = x)).card : K) := by
  rw [trace_eq_matrix_trace K (Pi.basisFun K X), LinearMap.toMatrix_eq_toMatrix',
    Matrix.trace]
  simp only [Matrix.diag, LinearMap.toMatrix'_apply, LinearMap.funLeft_apply, Function.comp_apply,
    Pi.single_apply]
  rw [Finset.sum_boole]
  congr 2
  ext x
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  constructor
  · intro h; rw [← Equiv.Perm.inv_def] at h
    have := congrArg σ h; simpa using this.symm
  · intro h; rw [Equiv.symm_apply_eq]; exact h.symm

end QOU.Core.TraceQuotient

/-!
# The Hopf trace formula for a two-step chain complex

`C₂ --d₂--> C₁ --d₁--> C₀` with `d₁ ∘ d₂ = 0`, and a chain map `(f₀, f₁, f₂)`. The homology is
`H₀ = C₀ / im d₁`, `H₁ = ker d₁ / im d₂`, `H₂ = ker d₂`. Then
`tr f₀ − tr f₁ + tr f₂ = tr (f on H₀) − tr (f on H₁) + tr (f on H₂)` (`hopf_trace`).

This is the algebraic content of the Hopf trace formula for a finite 2-dimensional cell complex,
such as the cell structure of Bring's surface used in `BringHarmonicTypes.lean`.
-/

namespace QOU.Core.HopfTrace

open LinearMap Submodule QOU.Core.TraceQuotient

variable {K C₀ C₁ C₂ : Type*} [Field K]
  [AddCommGroup C₀] [Module K C₀] [FiniteDimensional K C₀]
  [AddCommGroup C₁] [Module K C₁] [FiniteDimensional K C₁]
  [AddCommGroup C₂] [Module K C₂] [FiniteDimensional K C₂]

/-- A two-step chain complex with a chain endomorphism. -/
structure ChainEnd (K C₀ C₁ C₂ : Type*) [Field K]
    [AddCommGroup C₀] [Module K C₀] [AddCommGroup C₁] [Module K C₁]
    [AddCommGroup C₂] [Module K C₂] where
  d₁ : C₁ →ₗ[K] C₀
  d₂ : C₂ →ₗ[K] C₁
  dd : ∀ x, d₁ (d₂ x) = 0
  f₀ : C₀ →ₗ[K] C₀
  f₁ : C₁ →ₗ[K] C₁
  f₂ : C₂ →ₗ[K] C₂
  comm₁ : ∀ x, d₁ (f₁ x) = f₀ (d₁ x)
  comm₂ : ∀ x, d₂ (f₂ x) = f₁ (d₂ x)

namespace ChainEnd

variable (c : ChainEnd K C₀ C₁ C₂)

theorem range_d₁_inv : range c.d₁ ≤ (range c.d₁).comap c.f₀ := by
  rintro _ ⟨x, rfl⟩; exact ⟨c.f₁ x, c.comm₁ x⟩

theorem ker_d₁_inv : ker c.d₁ ≤ (ker c.d₁).comap c.f₁ := by
  intro x hx; simp only [mem_comap, mem_ker] at hx ⊢; rw [c.comm₁, hx, map_zero]

theorem range_d₂_inv : range c.d₂ ≤ (range c.d₂).comap c.f₁ := by
  rintro _ ⟨x, rfl⟩; exact ⟨c.f₂ x, c.comm₂ x⟩

theorem ker_d₂_inv : ker c.d₂ ≤ (ker c.d₂).comap c.f₂ := by
  intro x hx; simp only [mem_comap, mem_ker] at hx ⊢; rw [c.comm₂, hx, map_zero]

theorem range_d₂_le : range c.d₂ ≤ ker c.d₁ := by
  rintro _ ⟨x, rfl⟩; exact c.dd x

/-- Cycles in degree one. -/
abbrev Z₁ := ker c.d₁
/-- Boundaries in degree one, inside the cycles. -/
abbrev B₁ : Submodule K c.Z₁ := (range c.d₂).comap c.Z₁.subtype

/-- `f₁` on the cycles. -/
def fZ : c.Z₁ →ₗ[K] c.Z₁ :=
  c.f₁.restrict (p := c.Z₁) (q := c.Z₁) (fun x hx => mem_comap.mp (c.ker_d₁_inv hx))

theorem B₁_inv : c.B₁ ≤ c.B₁.comap c.fZ := by
  intro z hz
  simp only [mem_comap, Submodule.coe_subtype] at hz ⊢
  exact c.range_d₂_inv hz

/-- `f` on `H₀ = C₀ / im d₁`. -/
def h₀ : (C₀ ⧸ range c.d₁) →ₗ[K] (C₀ ⧸ range c.d₁) := (range c.d₁).mapQ _ c.f₀ c.range_d₁_inv
/-- `f` on `H₁ = ker d₁ / im d₂`. -/
def h₁ : (c.Z₁ ⧸ c.B₁) →ₗ[K] (c.Z₁ ⧸ c.B₁) := c.B₁.mapQ _ c.fZ c.B₁_inv
/-- `f` on `H₂ = ker d₂`. -/
def h₂ : ker c.d₂ →ₗ[K] ker c.d₂ :=
  c.f₂.restrict (p := ker c.d₂) (q := ker c.d₂) (fun x hx => mem_comap.mp (c.ker_d₂_inv hx))

/-- **Hopf trace formula** for a two-step complex. -/
theorem hopf_trace :
    trace K C₀ c.f₀ - trace K C₁ c.f₁ + trace K C₂ c.f₂ =
      trace K _ c.h₀ - trace K _ c.h₁ + trace K _ c.h₂ := by
  -- split each chain group
  have e0 := trace_eq_restrict_add_mapQ (range c.d₁) c.f₀ c.range_d₁_inv
  have e1 := trace_eq_restrict_add_mapQ (ker c.d₁) c.f₁ c.ker_d₁_inv
  have e2 := trace_eq_restrict_add_mapQ (ker c.d₂) c.f₂ c.ker_d₂_inv
  have eZ := trace_eq_restrict_add_mapQ c.B₁ c.fZ c.B₁_inv
  -- C₁ / ker d₁ ≅ im d₁
  have i1 : trace K _ ((ker c.d₁).mapQ _ c.f₁ c.ker_d₁_inv) =
      trace K _ (c.f₀.restrict (p := range c.d₁) (q := range c.d₁)
        (fun x hx => mem_comap.mp (c.range_d₁_inv hx))) := by
    refine trace_eq_of_intertwine (c.d₁.quotKerEquivRange) _ _ fun x => ?_
    induction x using Submodule.Quotient.induction_on with
    | H y => apply Subtype.ext; simp [c.comm₁]
  -- C₂ / ker d₂ ≅ im d₂ ≅ B₁
  have i2 : trace K _ ((ker c.d₂).mapQ _ c.f₂ c.ker_d₂_inv) =
      trace K _ (c.fZ.restrict (p := c.B₁) (q := c.B₁)
        (fun x hx => mem_comap.mp (c.B₁_inv hx))) := by
    refine trace_eq_of_intertwine
      (c.d₂.quotKerEquivRange.trans (Submodule.comapSubtypeEquivOfLe c.range_d₂_le).symm)
      _ _ fun x => ?_
    induction x using Submodule.Quotient.induction_on with
    | H y => apply Subtype.ext; apply Subtype.ext; simp [fZ, c.comm₂]
  have hZ : trace K _ (c.f₁.restrict (p := ker c.d₁) (q := ker c.d₁)
      (fun x hx => mem_comap.mp (c.ker_d₁_inv hx))) = trace K _ c.fZ := rfl
  rw [e0, e1, e2, hZ, eZ, i1, i2]
  simp only [h₀, h₁, h₂]
  ring

end ChainEnd

end QOU.Core.HopfTrace
