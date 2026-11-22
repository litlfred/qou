import Mathlib.GroupTheory.Perm.Cycle.Basic
import Mathlib.GroupTheory.GroupAction.Quotient

/-!
# `QOU.RiemannSurface.CombinatorialMapQuotient` — cells of a quotient map are orbits of cells

Bean `qou-m3tr` (Bring milestone M3), step 1, parent `qou-qhcr`.

## Setting

A *combinatorial map* on a finite set of darts `D` is a pair of permutations: `σ` (rotation
about vertices) and a fixed-point-free involution `α` (the edges). Its vertices, edges and faces
are the cycles of `σ`, `α` and `σ * α`. A group `G` acts on the map when it acts on `D`
commuting with `σ` and `α`.

## What is proved (sorry-free)

For **any** permutation `π` of `D` commuting with the `G`-action (`π = σ, α, σ * α` in turn):

* `π` descends to a permutation `quotPerm π` of the dart orbits `D/G`
  (`quotPerm_zpow_mk`: `(π̄)ⁱ ⟦x⟧ = ⟦πⁱ x⟧`);
* `G` acts on the cycles of `π` (`cycleAction`);
* **`cycleOrbitsEquiv`**: the `G`-orbits of the cycles of `π` are in bijection with the cycles of
  `π̄` on `D/G`.

So the cells of the quotient map `(σ̄, ᾱ)` on `D/G` are exactly the `G`-orbits of the cells of
`(σ, α)`. In particular the orbit counts on the left of the hypothesis `hY` of
`genus_eq_four_of_cellular` (PR #8365) are the vertex/edge/face counts of an honest
combinatorial map (`card_cycleOrbits_eq`).

`quotAlpha_fixedPointFree`: if `G` acts freely on edges, the quotient `ᾱ` still has no fixed
point, so `(σ̄, ᾱ)` is again a combinatorial map. `quotPerm_involutive` covers the involution
half.

## What is NOT proved

* `χ = |V| − |E| + |F|` is even for a connected orientable map, so that `g := (2 − χ)/2` is a
  natural number (step 2, the genus formula).
* A compact Riemann surface with a holomorphic `G`-action has a `G`-equivariant map (step 3,
  triangulation). Mathlib has no triangulations of surfaces.

Ref: [farkas-kra1992] Farkas–Kra, *Riemann Surfaces*, §V.1.
-/

namespace QOU.RiemannSurface.CombinatorialMapQuotient

open MulAction Equiv

variable {G D : Type*} [Group G] [MulAction G D]

/-- `π` commutes with the `G`-action. -/
def Equivariant (π : Perm D) (G : Type*) [Group G] [MulAction G D] : Prop :=
  ∀ (g : G) (x : D), π (g • x) = g • π x

variable {π : Perm D}

theorem Equivariant.zpow (hπ : Equivariant π G) (i : ℤ) (g : G) (x : D) :
    (π ^ i) (g • x) = g • (π ^ i) x := by
  have hc : Commute π (toPerm g : Perm D) := by
    ext y; simp [Perm.mul_apply, hπ g y]
  have := congrArg (fun p : Perm D => p x) (hc.zpow_left i).eq
  simpa [Perm.mul_apply] using this

theorem Equivariant.symm (hπ : Equivariant π G) : Equivariant π.symm G := by
  intro g x
  apply π.injective
  rw [Equiv.apply_symm_apply, hπ, Equiv.apply_symm_apply]

theorem Equivariant.mul {π' : Perm D} (hπ : Equivariant π G) (hπ' : Equivariant π' G) :
    Equivariant (π * π') G := by
  intro g x; simp [Perm.mul_apply, hπ' g x, hπ g]

/-! ### The induced permutation of `D/G` -/

theorem orbitRel_map (hπ : Equivariant π G) {x y : D}
    (h : orbitRel G D x y) : orbitRel G D (π x) (π y) := by
  rw [orbitRel_apply, mem_orbit_iff] at h ⊢
  obtain ⟨g, rfl⟩ := h
  exact ⟨g, (hπ g y).symm⟩

/-- The permutation of dart orbits induced by an equivariant `π`. -/
def quotPerm (hπ : Equivariant π G) : Perm (orbitRel.Quotient G D) where
  toFun := Quotient.map' π fun _ _ h => orbitRel_map hπ h
  invFun := Quotient.map' π.symm fun _ _ h => orbitRel_map hπ.symm h
  left_inv := by
    intro q; induction q using Quotient.inductionOn' with
    | h x => simp [Quotient.map'_mk'']
  right_inv := by
    intro q; induction q using Quotient.inductionOn' with
    | h x => simp [Quotient.map'_mk'']

@[simp] theorem quotPerm_mk (hπ : Equivariant π G) (x : D) :
    quotPerm hπ (Quotient.mk'' x : orbitRel.Quotient G D) = Quotient.mk'' (π x) := rfl

@[simp] theorem quotPerm_symm_mk (hπ : Equivariant π G) (x : D) :
    (quotPerm hπ).symm (Quotient.mk'' x : orbitRel.Quotient G D) = Quotient.mk'' (π.symm x) :=
  rfl

theorem quotPerm_zpow_mk (hπ : Equivariant π G) (i : ℤ) (x : D) :
    (quotPerm hπ ^ i) (Quotient.mk'' x : orbitRel.Quotient G D) =
      Quotient.mk'' ((π ^ i) x) := by
  induction i using Int.induction_on generalizing x with
  | zero => rfl
  | succ n ih =>
    rw [zpow_add_one, zpow_add_one, Perm.mul_apply, Perm.mul_apply, quotPerm_mk, ih]
  | pred n ih =>
    rw [zpow_sub_one, zpow_sub_one, Perm.mul_apply, Perm.mul_apply, Perm.inv_def,
      Perm.inv_def, quotPerm_symm_mk, ih]

/-! ### The `G`-action on cycles -/

/-- The cycles of `π`. -/
abbrev Cycles (π : Perm D) := Quotient (Perm.SameCycle.setoid π)

theorem sameCycle_smul (hπ : Equivariant π G) (g : G) {x y : D}
    (h : π.SameCycle x y) : π.SameCycle (g • x) (g • y) := by
  obtain ⟨i, rfl⟩ := h
  exact ⟨i, hπ.zpow i g x⟩

/-- `G` acts on the cycles of an equivariant `π`. -/
def cycleAction (hπ : Equivariant π G) : MulAction G (Cycles π) where
  smul g := Quotient.map' (g • ·) fun _ _ h => sameCycle_smul hπ g h
  one_smul := by
    intro c; induction c using Quotient.inductionOn' with
    | h x => exact congrArg Quotient.mk'' (one_smul G x)
  mul_smul := by
    intro g h c; induction c using Quotient.inductionOn' with
    | h x => exact congrArg Quotient.mk'' (mul_smul g h x)

/-- **Cells of the quotient are orbits of cells.** The `G`-orbits of the cycles of `π` are in
bijection with the cycles of the induced permutation `π̄` of `D/G`. -/
noncomputable def cycleOrbitsEquiv (hπ : Equivariant π G) :
    letI := cycleAction hπ
    orbitRel.Quotient G (Cycles π) ≃ Cycles (quotPerm hπ) := by
  letI := cycleAction hπ
  refine
    { toFun := Quotient.lift
        (Quotient.lift (fun x : D => (Quotient.mk'' (Quotient.mk'' x : orbitRel.Quotient G D) :
            Cycles (quotPerm hπ))) ?_) ?_
      invFun := Quotient.lift
        (Quotient.lift (fun x : D => (Quotient.mk'' (Quotient.mk'' x : Cycles π) :
            orbitRel.Quotient G (Cycles π))) ?_) ?_
      left_inv := ?_
      right_inv := ?_ }
  · -- well-defined on cycles of `π`
    rintro x y ⟨i, rfl⟩
    exact Quotient.sound ⟨i, quotPerm_zpow_mk hπ i x⟩
  · -- well-defined on `G`-orbits of cycles
    intro c c' h
    induction c using Quotient.inductionOn' with
    | h x =>
    induction c' using Quotient.inductionOn' with
    | h y =>
    obtain ⟨g, hg⟩ := h
    have hg' : π.SameCycle (g • y) x := Quotient.exact' hg
    obtain ⟨i, hi⟩ := hg'
    apply Quotient.sound
    refine ⟨-i, ?_⟩
    rw [quotPerm_zpow_mk, ← hi, ← Perm.mul_apply, ← zpow_add, neg_add_cancel, zpow_zero,
      Perm.one_apply]
    exact Quotient.sound ⟨g, rfl⟩
  · -- well-defined on `G`-orbits of darts
    rintro x y ⟨g, rfl⟩
    exact Quotient.sound ⟨g, rfl⟩
  · -- well-defined on cycles of `π̄`
    intro q q' h
    induction q using Quotient.inductionOn' with
    | h x =>
    induction q' using Quotient.inductionOn' with
    | h y =>
    obtain ⟨i, hi⟩ := h
    rw [quotPerm_zpow_mk] at hi
    obtain ⟨g, hg⟩ := (Quotient.exact' hi : orbitRel G D ((π ^ i) x) y)
    apply Quotient.sound
    refine ⟨g, ?_⟩
    show (Quotient.mk'' (g • y) : Cycles π) = Quotient.mk'' x
    have hg2 : g • y = (π ^ i) x := hg
    rw [hg2]
    refine Quotient.sound ⟨-i, ?_⟩
    rw [← Perm.mul_apply, ← zpow_add, neg_add_cancel, zpow_zero, Perm.one_apply]
  · intro c
    induction c using Quotient.inductionOn' with
    | h c =>
    induction c using Quotient.inductionOn' with
    | h x => rfl
  · intro q
    induction q using Quotient.inductionOn' with
    | h q =>
    induction q using Quotient.inductionOn' with
    | h x => rfl

/-- **Counting form.** The number of `G`-orbits of cycles of `π` equals the number of cycles of
`π̄`. With `π = σ, α, σ * α` these are the vertex, edge and face counts on the left of `hY`. -/
theorem card_cycleOrbits_eq (hπ : Equivariant π G) :
    letI := cycleAction hπ
    Nat.card (orbitRel.Quotient G (Cycles π)) = Nat.card (Cycles (quotPerm hπ)) :=
  Nat.card_congr (cycleOrbitsEquiv hπ)

/-! ### The quotient of a map is a map -/

/-- An involution descends to an involution. -/
theorem quotPerm_involutive {α : Perm D} (hα : Equivariant α G) (hinv : α * α = 1) :
    quotPerm hα * quotPerm hα = 1 := by
  ext q
  induction q using Quotient.inductionOn' with
  | h x =>
    show (Quotient.mk'' (α (α x)) : orbitRel.Quotient G D) = Quotient.mk'' x
    rw [← Perm.mul_apply, hinv, Perm.one_apply]

/-- **Edges stay edges.** If `α` has no fixed point and `G` acts freely on the edges (the cycles of
`α`), the quotient `ᾱ` has no fixed point. -/
theorem quotAlpha_fixedPointFree {α : Perm D} (hα : Equivariant α G)
    (hfix : ∀ x, α x ≠ x)
    (hfree : letI := cycleAction hα; ∀ (g : G) (e : Cycles α), g • e = e → g = 1)
    (q : orbitRel.Quotient G D) : quotPerm hα q ≠ q := by
  letI := cycleAction hα
  induction q using Quotient.inductionOn' with
  | h x =>
  intro h
  obtain ⟨g, hg⟩ := (Quotient.exact' h : orbitRel G D (α x) x)
  have hgx : g • x = α x := hg
  have hstab : g • (Quotient.mk'' x : Cycles α) = Quotient.mk'' x := by
    show (Quotient.mk'' (g • x) : Cycles α) = Quotient.mk'' x
    rw [hgx]
    exact Quotient.sound ⟨-1, by simp⟩
  have h1 := hfree g _ hstab
  subst h1
  exact hfix x (by rw [← hgx, one_smul])

end QOU.RiemannSurface.CombinatorialMapQuotient
