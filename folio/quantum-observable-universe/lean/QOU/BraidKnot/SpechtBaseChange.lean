import QOU.BraidKnot.Specht

/-!
# Base change for `M^μ` — the Specht module is defined over `ℤ`

Everything in `M^μ` that the Specht construction produces has **integer**
coordinates: a polytabloid is a signed sum of basis tabloids, so its coefficient
at each tabloid is a sum of `±1`. This file makes that precise as a functorial
statement — a ring hom `φ : R →+* S` acts on `M^μ` coefficient-wise and carries
`polytabloid` to `polytabloid` — and derives the one consequence the
nondegeneracy argument needs: **a linear relation proved over one ring survives
into another.**

## Why it is wanted

`specht_form_nondegenerate` has to reach every characteristic-zero field, and
the only place the Specht form is easy to control is `ℚ`, where it is positive
definite (`specht_form_nondegenerate_ordered`). The bridge is integrality:

* the coordinate matrix of the polytabloids is an **integer** matrix
  (`coordMatrix_intCast` below);
* a spanning relation established over `ℚ` transfers along `ℚ →+* k`
  (`mem_span_map` below), so the same finite sub-family spans over `k`.

Neither statement mentions the bilinear form, so both live here rather than in
`SpechtIrreducible`, which is where they are consumed.

## What is *not* here

No claim that the polytabloids are independent, and no use of the standard
basis theorem. The sub-family that ends up spanning is extracted over `ℚ` by
generic linear algebra at the point of use; this file only says that whatever
`ℚ`-relation you find keeps holding after base change.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtBaseChange

open QOU.BraidKnot QOU.BraidKnot.Specht

variable {μ : YoungDiagram}

/-! ## 1. Coefficient-wise base change -/

/-- Base change on `M^μ`: apply `φ` to every tabloid coordinate. -/
noncomputable def mapRing {R S : Type} [CommRing R] [CommRing S] (φ : R →+* S)
    (f : Mtab (k := R) μ) : Mtab (k := S) μ :=
  Finsupp.mapRange φ (map_zero φ) f

@[simp] theorem mapRing_apply {R S : Type} [CommRing R] [CommRing S] (φ : R →+* S)
    (f : Mtab (k := R) μ) (d : Tabloid μ) : mapRing φ f d = φ (f d) :=
  Finsupp.mapRange_apply

@[simp] theorem mapRing_add {R S : Type} [CommRing R] [CommRing S] (φ : R →+* S)
    (f g : Mtab (k := R) μ) : mapRing φ (f + g) = mapRing φ f + mapRing φ g := by
  ext d; simp

@[simp] theorem mapRing_smul {R S : Type} [CommRing R] [CommRing S] (φ : R →+* S)
    (c : R) (f : Mtab (k := R) μ) : mapRing φ (c • f) = φ c • mapRing φ f := by
  ext d; simp

@[simp] theorem mapRing_sum {R S : Type} [CommRing R] [CommRing S] (φ : R →+* S)
    {ι : Type} (s : Finset ι) (f : ι → Mtab (k := R) μ) :
    mapRing φ (∑ i ∈ s, f i) = ∑ i ∈ s, mapRing φ (f i) := by
  ext d
  simp [Finsupp.finset_sum_apply, map_sum]

/-! ## 2. `polytabloid` is defined over `ℤ`

The coefficients of `e_t` are `sign π ∈ {±1}` — `ℤ`-valued, hence untouched by
any ring hom beyond the canonical `ℤ`-algebra structure. -/

/-- **Base change carries polytabloids to polytabloids.** -/
theorem mapRing_polytabloid {R S : Type} [CommRing R] [CommRing S] (φ : R →+* S)
    (t : Tableau μ) :
    mapRing φ (polytabloid (k := R) t) = polytabloid (k := S) t := by
  ext d
  rw [mapRing_apply, polytabloid, polytabloid]
  simp only [Finsupp.coe_finset_sum, Finset.sum_apply, Finsupp.coe_smul, Pi.smul_apply,
    Mtab.of, Finsupp.single_apply, map_sum, map_zsmul, apply_ite φ, map_one, map_zero]

/-- The polytabloid coordinates over any ring are the images of the integer
ones. -/
theorem polytabloid_apply_eq_intCast {S : Type} [CommRing S] (t : Tableau μ)
    (d : Tabloid μ) :
    (polytabloid (k := S) t) d = ((polytabloid (k := ℤ) t) d : S) := by
  conv_lhs => rw [← mapRing_polytabloid (Int.castRingHom S) t]
  rw [mapRing_apply]
  rfl

/-! ## 3. The coordinate matrix

`coordMatrix v i d` is the coefficient of `v i` at the tabloid `d`. When the
`v i` are polytabloids this is an integer matrix, cast. -/

/-- The coordinate matrix of a family of `M^μ` vectors in the tabloid basis. -/
noncomputable def coordMatrix {k : Type} [CommRing k] {ι : Type}
    (v : ι → Mtab (k := k) μ) : Matrix ι (Tabloid μ) k :=
  fun i d => v i d

/-- **Integrality of the polytabloid coordinate matrix.** For any family of
tableaux, the coordinate matrix over `S` is the integer one cast into `S`. -/
theorem coordMatrix_intCast {S : Type} [CommRing S] {ι : Type} (w : ι → Tableau μ) :
    coordMatrix (fun i => polytabloid (k := S) (w i))
      = (coordMatrix (fun i => polytabloid (k := ℤ) (w i))).map (Int.cast : ℤ → S) := by
  ext i d
  exact polytabloid_apply_eq_intCast (w i) d

/-! ## 4. Relations survive base change

The one consequence the nondegeneracy proof consumes: if `x` lies in the span
of a finite family over `R`, then its base change lies in the span of the base
changed family over `S`. Applied with `R = ℚ`, `S = k` and the family a
sub-family of the polytabloids, this is what says a spanning set found over `ℚ`
still spans over `k`. -/

/-- **Span membership transfers along a ring hom.** -/
theorem mem_span_map {R S : Type} [CommRing R] [CommRing S] (φ : R →+* S)
    {ι : Type} [Fintype ι] (w : ι → Mtab (k := R) μ) (x : Mtab (k := R) μ)
    (hx : x ∈ Submodule.span R (Set.range w)) :
    mapRing φ x ∈ Submodule.span S (Set.range (fun i => mapRing φ (w i))) := by
  obtain ⟨c, hc⟩ := (Submodule.mem_span_range_iff_exists_fun R).mp hx
  refine (Submodule.mem_span_range_iff_exists_fun S).mpr ⟨fun i => φ (c i), ?_⟩
  rw [← hc, mapRing_sum]
  exact Finset.sum_congr rfl (fun i _ => (mapRing_smul φ (c i) (w i)).symm)

/-- **The form the caller uses.** A sub-family of the polytabloids that spans
`S^μ` over `ℚ` spans it over any characteristic-zero field.

The `ℚ`-side hypothesis is stated as "every polytabloid is in the span of the
sub-family", which is what generic basis extraction hands back. -/
theorem spechtSubmodule_eq_span_of_rat {k : Type} [Field k] [CharZero k]
    {ι : Type} [Fintype ι] (w : ι → Tableau μ)
    (hQ : ∀ t : Tableau μ, polytabloid (k := ℚ) t ∈
      Submodule.span ℚ (Set.range (fun i => polytabloid (k := ℚ) (w i)))) :
    Submodule.span k (Set.range (fun i => polytabloid (k := k) (w i)))
      = SpechtSubmodule (k := k) μ := by
  refine le_antisymm ?_ ?_
  · rw [SpechtSubmodule]
    exact Submodule.span_mono (by rintro _ ⟨i, rfl⟩; exact ⟨w i, rfl⟩)
  · rw [SpechtSubmodule, Submodule.span_le]
    rintro _ ⟨t, rfl⟩
    -- push the `ℚ`-relation along `ℚ →+* k`; both sides are polytabloids again
    have h := mem_span_map (Rat.castHom k) (fun i => polytabloid (k := ℚ) (w i))
      (polytabloid (k := ℚ) t) (hQ t)
    rw [mapRing_polytabloid] at h
    simpa only [mapRing_polytabloid] using h

/-- Every element of `SpechtSubmodule μ` over a characteristic-zero field `k` lies in the `k`-span of a polytabloid subfamily that spans over `ℚ`. -/
theorem mem_span_of_rat_spechtSubmodule {k : Type} [Field k] [CharZero k]
    {ι : Type} [Fintype ι] (w : ι → Tableau μ)
    (hQ : ∀ t : Tableau μ, polytabloid (k := ℚ) t ∈
      Submodule.span ℚ (Set.range (fun i => polytabloid (k := ℚ) (w i))))
    {x : Mtab (k := k) μ} (hx : x ∈ SpechtSubmodule (k := k) μ) :
    x ∈ Submodule.span k (Set.range (fun i => polytabloid (k := k) (w i))) := by
  rw [spechtSubmodule_eq_span_of_rat w hQ]
  exact hx

end QOU.BraidKnot.SpechtBaseChange
