/-
  Groups acting on H³, and the volume of a quotient — DERIVED, not entered.

  Bean `qou-hq3m`, child of `qou-8mtd`.

  ═══ WHAT WAS ACTUALLY MISSING ═══

  `qou-8mtd` says the volume of a topological 3-manifold is undefined, and adds that
  Mathlib has no hyperbolic 3-manifolds.  The second half is true of Mathlib and
  **misleading about this corpus**, which already has a great deal:
  `HyperbolicVolumeMeasure` builds `hypVolume = dx dy dz / z³` on `upperHalfSpace`
  sorry-free, `TotallyGeodesicFaces` proves vertical planes and hemispheres totally
  geodesic, and `IdealTriangulation` proves the shape-parameter triple.

  What was missing is one specific thing: **a group acting.**  There was a measure on
  H³ and there were individual isometries, but no group, no discrete subgroup, and no
  quotient — which is the whole distance between "we have H³" and "we have a
  hyperbolic 3-manifold":

      H³  --(Γ acts: by isometries, freely, discretely)-->  H³/Γ

  That absence is *why* `Encounter.MostowRigidity.volume` has to be an entered decimal
  literal and `MathlibExt.HyperbolicVolumeBridge.vol` an assumed class field.  Neither
  had anything to attach to.

  ═══ WHAT IS PROVED HERE ═══

  For a group `Γ` of horizontal translations:

  1. `vaddInvariantMeasure` — **Γ preserves hyperbolic volume.**  This is the content.
     It is not assumed: it is discharged by the corpus's own `hypVolume_add_left`,
     whose `v 2 = 0` hypothesis is exactly membership in `horizontal`.
  2. `vadd_mem_upperHalfSpace` — Γ acts on H³ itself, not merely on ℝ³.  A translation
     with a vertical component would fail this, and would not be an isometry.
  3. `vadd_right_injective` / `free_of_ne_zero` — the action is **free**.  This is what
     makes the quotient a manifold rather than an orbifold.
  4. `hypVolume_eq_of_isAddFundamentalDomain` — **the volume of the quotient is
     well-defined**: any two fundamental domains carry the same hyperbolic volume.

  Point 4 is a one-line application of Mathlib's `IsAddFundamentalDomain.measure_eq`,
  and on its own it would be a projection.  What makes it a *result* is that its
  `VAddInvariantMeasure` hypothesis is discharged by point 1 rather than assumed — so
  the volume of this quotient is derived from `hypDensity = 1/z³` and nothing else.
  For the first time in this corpus a manifold's volume has a referent instead of a
  literal.

  ═══ WHAT IS NOT PROVED, AND IS NOT NEARBY ═══

  **Mostow rigidity and Thurston hyperbolisation are untouched**, and nothing here is
  a step toward either.  A horizontal-translation quotient is a genuine hyperbolic
  3-manifold but a very special one.  It is **not** a knot complement, and nothing here
  makes `Vol(4₁)` computable or verifies the literal `2.02988321281930` that
  `figureEight` carries.

  Two limits stated precisely, because the loose version of each would overclaim:

  * **The exhibited lattice is rank 1, and `H³/ℤ` is NOT a cusp.**  A cusp
    cross-section is a torus and needs a **rank-2** lattice.  §5 proves the general
    horizontality lemma, so a rank-2 group satisfies every hypothesis of §1–§4; what
    §6 exhibits is a fundamental domain for the rank-1 case only.
  * **The volume is not computed, and is not claimed finite or nonzero.**  §4 and §6
    establish that the quotient volume is WELL DEFINED — every fundamental domain gives
    the same element of `ℝ≥0∞` — which is a different and weaker statement than knowing
    which element.  `∫ dz/z³` diverges at `z → 0`, so the slab's volume is *expected* to
    be `⊤`; that is **not proved here**, and is left open in `qou-hq3m`.

  The general bridge therefore stays exactly as conditional as it was.  What changes is
  that "the volume of a hyperbolic 3-manifold" is now a *definable* notion in at least
  one honest case, so the bridge's `vol` field is no longer the only way the corpus can
  say those words.

  -- Ref: [thurston1978] Ch. 4 (quotients of H³ by discrete groups)
  -- Ref: [ratcliffe] §8 (fundamental domains and the volume of a quotient)
-/
import QOU.Archimedean.HyperbolicVolumeMeasure
import Mathlib.MeasureTheory.Group.FundamentalDomain

namespace QOU.Archimedean.HyperbolicQuotient

open MeasureTheory Set
open QOU.Archimedean.HyperbolicVolume

/-! ## §1 — The horizontal translation group

A translation of `ℝ³` is an isometry of `H³` exactly when it leaves the height
coordinate alone. `HyperbolicVolumeMeasure` records why this is not a technicality: a
*vertical* translation genuinely changes hyperbolic volume. -/

/-- **The horizontal vectors** — those with zero height. Translations by these are
isometries of `H³`; translations by anything else are not. -/
def horizontal : AddSubgroup (Fin 3 → ℝ) where
  carrier := {v | v 2 = 0}
  zero_mem' := by simp
  add_mem' := by
    intro a b ha hb
    simp only [Set.mem_setOf_eq, Pi.add_apply] at *
    rw [ha, hb, add_zero]
  neg_mem' := by
    intro a ha
    simp only [Set.mem_setOf_eq, Pi.neg_apply] at *
    rw [ha, neg_zero]

@[simp] theorem mem_horizontal {v : Fin 3 → ℝ} : v ∈ horizontal ↔ v 2 = 0 := Iff.rfl

/-- A group of translations that are isometries of `H³`.

Carried as a class so the invariance instance below resolves automatically. It asserts
a real containment, not a marker. -/
class IsHorizontal (Γ : AddSubgroup (Fin 3 → ℝ)) : Prop where
  le_horizontal : Γ ≤ horizontal

variable (Γ : AddSubgroup (Fin 3 → ℝ))

/-- Every element of a horizontal group has zero height. -/
theorem height_eq_zero [IsHorizontal Γ] (g : Γ) : (g : Fin 3 → ℝ) 2 = 0 :=
  IsHorizontal.le_horizontal g.2

/-- The subgroup acts by translation, definitionally. -/
@[simp] theorem vadd_def (g : Γ) (p : Fin 3 → ℝ) : g +ᵥ p = (g : Fin 3 → ℝ) + p := rfl

/-! ## §2 — The action is by isometries of `H³`

Two facts that together say `Γ` acts on hyperbolic space, not merely on `ℝ³`: it
preserves the upper half-space, and it preserves the volume. -/

/-- **Height is unchanged.** -/
@[simp] theorem vadd_height [IsHorizontal Γ] (g : Γ) (p : Fin 3 → ℝ) :
    (g +ᵥ p) 2 = p 2 := by
  rw [vadd_def, Pi.add_apply, height_eq_zero Γ g, zero_add]

/-- **`Γ` acts on `H³`.** A translation with a vertical component would move points out
of (or into) the upper half-space; a horizontal one cannot. -/
theorem vadd_mem_upperHalfSpace [IsHorizontal Γ] (g : Γ) {p : Fin 3 → ℝ}
    (hp : p ∈ upperHalfSpace) : g +ᵥ p ∈ upperHalfSpace := by
  simpa only [upperHalfSpace, Set.mem_setOf_eq, vadd_height Γ g p] using hp

/-- **`Γ` preserves hyperbolic volume — the load-bearing fact.**

Discharged by the corpus's `hypVolume_add_left`, whose `v 2 = 0` hypothesis is exactly
membership in `horizontal`. This instance is what lets the quotient volume below be
*derived* rather than posited. -/
instance vaddInvariantMeasure [IsHorizontal Γ] :
    VAddInvariantMeasure Γ (Fin 3 → ℝ) hypVolume where
  measure_preimage_vadd g _s hs := hypVolume_add_left (height_eq_zero Γ g) hs

/-! ## §3 — The action is free

Freeness is what makes the quotient a *manifold* rather than an orbifold: no nonzero
element of `Γ` may fix a point. For translations this is immediate, and worth recording
precisely because it is the hypothesis that silently fails for a general group. -/

/-- Translation by a fixed group element is injective. -/
theorem vadd_right_injective (g : Γ) : Function.Injective (fun p : Fin 3 → ℝ => g +ᵥ p) :=
  fun _ _ h => add_left_cancel h

/-- **The action is free**: a group element fixing any point is the identity. -/
theorem eq_zero_of_vadd_eq {g : Γ} {p : Fin 3 → ℝ} (h : g +ᵥ p = p) : g = 0 := by
  have hg : (g : Fin 3 → ℝ) = 0 := by
    have := h
    rw [vadd_def] at this
    exact add_right_cancel (by rw [this, zero_add])
  exact Subtype.ext hg

/-- Contrapositive form: a nonzero element fixes nothing. -/
theorem vadd_ne_of_ne_zero {g : Γ} (hg : g ≠ 0) (p : Fin 3 → ℝ) : g +ᵥ p ≠ p :=
  fun h => hg (eq_zero_of_vadd_eq Γ h)

/-! ## §4 — The volume of the quotient is well defined

The payoff. `IsAddFundamentalDomain.measure_eq` needs the action to preserve the
measure; §2 supplies that from `hypDensity = 1/z³`, so nothing is assumed. -/

/-- **The hyperbolic volume of `H³/Γ` does not depend on the fundamental domain.**

This is what it means for the quotient to *have* a volume. Compare
`Encounter.MostowRigidity.volume`, which is a real supplied by an instance — here the
number is determined by the measure and the group. -/
theorem hypVolume_eq_of_isAddFundamentalDomain [IsHorizontal Γ] [Countable Γ]
    {D₁ D₂ : Set (Fin 3 → ℝ)}
    (h₁ : IsAddFundamentalDomain Γ D₁ hypVolume)
    (h₂ : IsAddFundamentalDomain Γ D₂ hypVolume) :
    hypVolume D₁ = hypVolume D₂ :=
  h₁.measure_eq h₂

/-! ## §5 — The hypotheses are inhabited

Everything above would be worth nothing over an empty class, so: horizontal groups with
nonzero elements exist, and the rank-1 lattices are among them. Without this section a
reader cannot tell §4 from a vacuous statement. -/

/-- The unit vector along the first axis — horizontal and nonzero. -/
noncomputable def e₀ : Fin 3 → ℝ := fun i => if i = 0 then 1 else 0

@[simp] theorem e₀_height : e₀ 2 = 0 := by simp [e₀]

theorem e₀_ne_zero : e₀ ≠ 0 := by
  intro h
  have : e₀ 0 = 0 := by rw [h]; rfl
  simp [e₀] at this

theorem e₀_mem_horizontal : e₀ ∈ horizontal := e₀_height

/-- **Any group generated by horizontal vectors is horizontal.**

Stated for a general generating set so the rank-2 lattice — the one whose quotient is
an actual cusp — satisfies §1–§4 without further work, even though §6 exhibits a
fundamental domain only in the rank-1 case. -/
theorem isHorizontal_closure {S : Set (Fin 3 → ℝ)} (hS : S ⊆ horizontal) :
    IsHorizontal (AddSubgroup.closure S) where
  le_horizontal := (AddSubgroup.closure_le horizontal).mpr hS

/-- **The rank-1 lattice generated by a horizontal vector is a horizontal group.**

`AddSubgroup.zmultiples v` is `{n • v | n : ℤ}`; it is horizontal whenever `v` is, and
it is countable, so it satisfies every hypothesis §4 needs. -/
instance isHorizontal_zmultiples {v : Fin 3 → ℝ} (hv : v ∈ horizontal) :
    IsHorizontal (AddSubgroup.zmultiples v) where
  le_horizontal := by
    rw [AddSubgroup.zmultiples_eq_closure, AddSubgroup.closure_le]
    rintro x (rfl : x = v)
    exact hv

/-- The rank-1 lattice along `e₀`: a concrete nonzero horizontal group. -/
noncomputable def latticeE₀ : AddSubgroup (Fin 3 → ℝ) := AddSubgroup.zmultiples e₀

instance : IsHorizontal latticeE₀ := isHorizontal_zmultiples e₀_mem_horizontal

theorem e₀_mem_latticeE₀ : e₀ ∈ latticeE₀ := AddSubgroup.mem_zmultiples e₀

/-- **The concrete lattice is nontrivial**, so §4 is not a statement about the trivial
group acting on itself. -/
theorem latticeE₀_ne_bot : latticeE₀ ≠ ⊥ := by
  intro h
  have : e₀ ∈ (⊥ : AddSubgroup (Fin 3 → ℝ)) := h ▸ e₀_mem_latticeE₀
  rw [AddSubgroup.mem_bot] at this
  exact e₀_ne_zero this

/-! ## §6 — A fundamental domain actually exists

§4 is a statement about fundamental domains, so it is worth exactly nothing until one
is exhibited. This section proves the unit slab `0 ≤ x < 1` is a fundamental domain for
the rank-1 lattice, which is what makes §4 an applicable theorem rather than a
conditional over a possibly-empty hypothesis.

That distinction is not hypothetical here: the sibling `HyperbolicVolumeBridge` was
first written with a class admitting `Realises := fun _ _ => False`, under which every
theorem about it held vacuously. Exhibiting the model is the only way to know. -/

/-- Evaluating an integer multiple of `e₀` at the first coordinate returns the integer. -/
@[simp] theorem zsmul_e₀_apply_zero (n : ℤ) : ((n • e₀ : Fin 3 → ℝ)) 0 = (n : ℝ) := by
  simp [e₀, Pi.smul_apply, zsmul_eq_mul]

/-- Every element of the rank-1 lattice is an integer multiple of `e₀`. -/
theorem exists_zsmul_of_mem_latticeE₀ (g : latticeE₀) :
    ∃ n : ℤ, (g : Fin 3 → ℝ) = n • e₀ := by
  obtain ⟨n, hn⟩ := AddSubgroup.mem_zmultiples_iff.mp g.2
  exact ⟨n, hn.symm⟩

/-- The lattice element determined by an integer. -/
noncomputable def ofInt (n : ℤ) : latticeE₀ :=
  ⟨n • e₀, AddSubgroup.mem_zmultiples_iff.mpr ⟨n, rfl⟩⟩

@[simp] theorem coe_ofInt (n : ℤ) : ((ofInt n : latticeE₀) : Fin 3 → ℝ) = n • e₀ := rfl

/-- `ofInt` is onto the lattice: every element is an integer multiple of `e₀`. -/
theorem ofInt_surjective : Function.Surjective ofInt := by
  intro g
  obtain ⟨n, hn⟩ := exists_zsmul_of_mem_latticeE₀ g
  exact ⟨n, Subtype.ext (by rw [coe_ofInt, ← hn])⟩

/-- **The lattice is countable** — required by `IsAddFundamentalDomain.measure_eq`,
and true because the lattice is the image of `ℤ`. -/
instance : Countable latticeE₀ := ofInt_surjective.countable

/-- **The unit slab** in the first coordinate. -/
def slab : Set (Fin 3 → ℝ) := {p | p 0 ∈ Set.Ico (0 : ℝ) 1}

theorem measurableSet_slab : MeasurableSet slab :=
  measurableSet_Ico.preimage (measurable_pi_apply 0)

/-- **The slab is a fundamental domain for the rank-1 lattice.**

Existence and uniqueness of the representative are the two halves of `Int.fract`: the
translate landing in the slab is `-⌊x 0⌋`, and two integers whose difference is less
than `1` in absolute value are equal. -/
theorem isAddFundamentalDomain_slab :
    IsAddFundamentalDomain latticeE₀ slab hypVolume := by
  refine IsAddFundamentalDomain.mk' measurableSet_slab.nullMeasurableSet ?_
  intro x
  -- the first coordinate of `g +ᵥ x`, for `g` the integer multiple `n • e₀`
  have coord : ∀ n : ℤ, (ofInt n +ᵥ x) 0 = (n : ℝ) + x 0 := by
    intro n
    rw [vadd_def, Pi.add_apply, coe_ofInt, zsmul_e₀_apply_zero]
  refine ⟨ofInt (-⌊x 0⌋), ?_, ?_⟩
  · -- existence: `-⌊x 0⌋ + x 0` is the fractional part, which lies in `[0, 1)`
    simp only [slab, Set.mem_setOf_eq, coord, Int.cast_neg]
    constructor
    · have := Int.floor_le (x 0); linarith
    · have := Int.lt_floor_add_one (x 0); linarith
  · -- uniqueness: the slab condition pins `⌊x 0⌋`, via `Int.floor_eq_iff`
    rintro g hg
    obtain ⟨m, hm⟩ := exists_zsmul_of_mem_latticeE₀ g
    have hgx : (g +ᵥ x) 0 = (m : ℝ) + x 0 := by
      rw [vadd_def, Pi.add_apply, hm, zsmul_e₀_apply_zero]
    simp only [slab, Set.mem_setOf_eq, hgx, Set.mem_Ico] at hg
    have hfloor : ⌊x 0⌋ = -m := by
      rw [Int.floor_eq_iff]
      constructor
      · push_cast; linarith [hg.1]
      · push_cast; linarith [hg.2]
    apply Subtype.ext
    rw [hm, coe_ofInt, hfloor, neg_neg]

/-- **The volume of `H³ / latticeE₀` is well defined and computed by the slab.**

Instantiates §4 at the fundamental domain of §6: any other fundamental domain for this
lattice carries the same hyperbolic volume. Nothing here is assumed — the invariance
came from `hypDensity`, and the domain was exhibited. -/
theorem hypVolume_eq_slab_of_isAddFundamentalDomain
    {D : Set (Fin 3 → ℝ)} (hD : IsAddFundamentalDomain latticeE₀ D hypVolume) :
    hypVolume D = hypVolume slab :=
  hypVolume_eq_of_isAddFundamentalDomain latticeE₀ hD isAddFundamentalDomain_slab

end QOU.Archimedean.HyperbolicQuotient
