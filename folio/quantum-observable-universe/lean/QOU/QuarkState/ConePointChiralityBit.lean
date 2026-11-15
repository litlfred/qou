/-
# Can the cone point `u` pick the weak vertex's L/R bit? Not equivariantly.

Bean `qou-hlx7`, owner decision D-W1 = A (2026-11-15): test whether 6b's polarization
point `u` (the chirality unit on the model cone, #7825) selects which of the two
one-sided flavour flips `W_L = q⁻¹J`, `W_R = qJ` (`OneSidedWeakVertex.lean`) is the weak
vertex.

## The modelling requirement

An assignment "cone point `u` ↦ vertex" is a function `τ : cone → Bool` (`true` = L-only,
`false` = R-only), attached to letters `ℓ u`. For it to be *selected by `u`* rather than
fixed by hand, it must respect the cone's gauge symmetry. Unit quaternions act on `u` by
conjugation (`hopf_leftMul`, 6b). On the algebra side they act by ANY family of `K`-algebra
homomorphisms `ρ g`, including the trivial one. The requirement is equivariance:
`ℓ (g·u) = ρ g (ℓ u)` and `vertex (τ (g·u)) (ℓ (g·u)) = ρ g (vertex (τ u) (ℓ u))`.

## Proved here (sorry-free)

* `map_oneSidedL`, `map_oneSidedR`: a `K`-algebra homomorphism carries the L-only (R-only)
  flip of a letter to the L-only (R-only) flip of the image letter. **Algebra maps
  preserve the type**, because they fix `q`, which labels the lines.
* `oneSidedL_ne_oneSidedR`: in a nontrivial algebra the two flips differ unless `q² = 1`.
* `type_invariant`: hence an equivariant `τ` is constant along every gauge orbit.
* `conjBy_unitJ_unitI`: conjugation by the unit `j` sends `u = i` to `−i`. The antipode is
  in the orbit, and by 6b (`chiralGammaU_neg`) it is the photon swap `Γ ↦ −Γ`.
* **`cone_point_cannot_pick_bit`**: every equivariant assignment gives the same vertex type
  at `u` and at `−u`. So the vertex type cannot follow which polarization line `Γ_u`
  calls left-handed. Scope (b) under the equivariance requirement.

## What does swap the type

Only the bar involution (`q ↦ q⁻¹`, `oneSidedL_flip`), which is not `K`-linear. So the L/R
bit of the one-sided vertex is the same datum as the orientation `q` vs `q⁻¹`,
equivalently which crossing carries the weight `q` (`two_smul_oneSidedL_eq_skein`). It is
not the cone point. A non-equivariant assignment (a gauge fixing) can of course pick
either; that is a choice, and this file does not make it.

Base ring (§7c): generic `[Field K]`, `[Ring A] [Algebra K A]`, cone over generic
`[CommRing R]`. No `ℝ`.
-/
import QOU.QuarkState.OneSidedWeakVertex
import QOU.StandardModel.ChiralityPolarizationHopf

namespace QOU.QuarkState.ConePointBit

open QOU.QuarkState.Helicity QOU.QuarkState.OneSidedWeakVertex

section Maps

variable {K A B : Type*} [Field K] [Ring A] [Ring B] [Algebra K A] [Algebra K B]
variable {q : K}

theorem map_Pp (φ : A →ₐ[K] B) (s : A) : φ (Pp q s) = Pp q (φ s) := by
  simp [Pp, map_smul, map_add, map_one]

theorem map_Pm (φ : A →ₐ[K] B) (s : A) : φ (Pm q s) = Pm q (φ s) := by
  simp [Pm, map_smul, map_sub, map_one]

theorem map_flip (φ : A →ₐ[K] B) (s : A) : φ (Helicity.flip q s) = Helicity.flip q (φ s) := by
  simp [Helicity.flip, map_sub, map_smul, map_one]

theorem map_isLetter (φ : A →ₐ[K] B) {s : A} (hs : IsLetter q s) : IsLetter q (φ s) := by
  unfold IsLetter at hs ⊢
  rw [← map_mul, hs, map_add, map_smul, map_one]

/-- **Algebra maps preserve the L-only type.** -/
theorem map_oneSidedL (φ : A →ₐ[K] B) (s : A) : φ (oneSidedL q s) = oneSidedL q (φ s) := by
  simp [oneSidedL, map_add, map_mul, map_Pp, map_Pm, map_flip]

theorem map_oneSidedR (φ : A →ₐ[K] B) (s : A) : φ (oneSidedR q s) = oneSidedR q (φ s) := by
  simp [oneSidedR, map_add, map_mul, map_Pp, map_Pm, map_flip]

end Maps

section Distinct

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] [Nontrivial A]
variable {q : K} {s : A}

/-- The two one-sided flips differ unless `q² = 1`. -/
theorem oneSidedL_ne_oneSidedR (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s)
    (hq1 : q ^ 2 ≠ 1) : oneSidedL q s ≠ oneSidedR q s := by
  intro he
  rw [oneSidedL_eq hq hq2 hs, oneSidedR_eq hq hq2 hs] at he
  have h0 : (q - q⁻¹) • grading q s = 0 := by rw [sub_smul, he, sub_self]
  have h1 : (q - q⁻¹) • (1 : A) = 0 := by
    have := congrArg (· * grading q s) h0
    simpa [smul_mul_assoc, grading_sq hq hq2 hs] using this
  have hc : q - q⁻¹ = 0 := by
    by_contra hc
    apply one_ne_zero (α := A)
    have h2 := congrArg ((q - q⁻¹)⁻¹ • ·) h1
    simp [smul_smul, inv_mul_cancel₀ hc] at h2
  apply hq1
  have : q = q⁻¹ := sub_eq_zero.mp hc
  calc q ^ 2 = q * q := sq q
    _ = q * q⁻¹ := by rw [← this]
    _ = 1 := mul_inv_cancel₀ hq

end Distinct

section Gauge

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] [Nontrivial A]
variable {q : K}

/-- The vertex of type `b` (`true` = L-only, `false` = R-only). -/
noncomputable def vertex (q : K) (b : Bool) (s : A) : A :=
  if b then oneSidedL q s else oneSidedR q s

omit [Nontrivial A] in
theorem map_vertex (φ : A →ₐ[K] A) (b : Bool) (s : A) :
    φ (vertex q b s) = vertex q b (φ s) := by
  cases b <;> simp [vertex, map_oneSidedL, map_oneSidedR]

theorem vertex_inj (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hq1 : q ^ 2 ≠ 1) {s : A}
    (hs : IsLetter q s) {b b' : Bool} (h : vertex q b s = vertex q b' s) : b = b' := by
  cases b <;> cases b' <;> simp [vertex] at h ⊢
  · exact oneSidedL_ne_oneSidedR hq hq2 hs hq1 h.symm
  · exact oneSidedL_ne_oneSidedR hq hq2 hs hq1 h

/-- **An equivariant type assignment is constant along gauge orbits.** `act` is any action
of `G` on points, and `ρ g` any `K`-algebra endomorphism (the trivial one included). -/
theorem type_invariant {G X : Type*} (act : G → X → X) (ρ : G → (A →ₐ[K] A))
    (ℓ : X → A) (τ : X → Bool) (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hq1 : q ^ 2 ≠ 1)
    (hℓ : ∀ x, IsLetter q (ℓ x)) (g : G) (x : X)
    (hcov : ℓ (act g x) = ρ g (ℓ x))
    (heq : vertex q (τ (act g x)) (ℓ (act g x)) = ρ g (vertex q (τ x) (ℓ x))) :
    τ (act g x) = τ x := by
  rw [map_vertex, ← hcov] at heq
  exact vertex_inj hq hq2 hq1 (hℓ _) heq

end Gauge

section Cone

open QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-- Conjugation by the unit `j` sends the chirality point `u = i` to its antipode `−i`. -/
theorem conjBy_unitJ_unitI : conjBy (unitJ : BringCone R) unitI = -unitI := by
  ext <;> simp [conjBy, unitJ, unitI]

theorem normSq_unitJ : Quaternion.normSq (unitJ : BringCone R) = 1 := by
  rw [Quaternion.normSq_def']; simp [unitJ]

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] [Nontrivial A] {q : K}

/-- **The cone point cannot pick the L/R bit equivariantly.** For any letter field `ℓ` on
the cone and any assignment `τ` that is equivariant under the unit-quaternion gauge (acting
on `u` by conjugation and on the algebra by any `K`-algebra maps `ρ g`), the vertex type
at `u = i` equals the type at its antipode `−i`, which `chiralGammaU_neg` identifies as the
photon swap `Γ ↦ −Γ`. -/
theorem cone_point_cannot_pick_bit (ρ : BringCone R → (A →ₐ[K] A)) (ℓ : BringCone R → A)
    (τ : BringCone R → Bool) (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hq1 : q ^ 2 ≠ 1)
    (hℓ : ∀ x, IsLetter q (ℓ x))
    (hcov : ∀ g x, Quaternion.normSq g = 1 → ℓ (conjBy g x) = ρ g (ℓ x))
    (heq : ∀ g x, Quaternion.normSq g = 1 →
      vertex q (τ (conjBy g x)) (ℓ (conjBy g x)) = ρ g (vertex q (τ x) (ℓ x))) :
    τ (-unitI) = τ unitI := by
  have := type_invariant (fun g x => conjBy g x) ρ ℓ τ hq hq2 hq1 hℓ unitJ unitI
    (hcov _ _ normSq_unitJ) (heq _ _ normSq_unitJ)
  simpa [conjBy_unitJ_unitI] using this

omit [Nontrivial A] in
/-- **Non-vacuity**: a constant assignment (a fixed convention, `ρ = id`, one letter `s`)
satisfies both equivariance hypotheses. So the theorem says that the equivariant
assignments are exactly the ones that ignore which line `u` calls left-handed. -/
theorem const_assignment_equivariant (s : A) (b : Bool) :
    (∀ g x, Quaternion.normSq (g : BringCone R) = 1 →
      (fun _ : BringCone R => s) (conjBy g x) = AlgHom.id K A ((fun _ : BringCone R => s) x)) ∧
    (∀ g x, Quaternion.normSq (g : BringCone R) = 1 →
      vertex q ((fun _ : BringCone R => b) (conjBy g x)) ((fun _ : BringCone R => s) (conjBy g x))
        = AlgHom.id K A (vertex q ((fun _ : BringCone R => b) x)
            ((fun _ : BringCone R => s) x))) :=
  ⟨fun _ _ _ => rfl, fun _ _ _ => rfl⟩

end Cone

end QOU.QuarkState.ConePointBit
