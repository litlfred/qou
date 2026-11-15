import Mathlib.Tactic
import QOU.BringConeGauge
import QOU.StandardModel.ChiralityGradingConstruction

/-!
# V10's eight `Gen1Quark` labels into the Hopf-model cone: what is forced, what is free

Bean `qou-wqto`, issue #7783, step (c). V10 (`ChiralityGradingConstruction.lean`)
builds the chirality bit on the abstract label set `Gen1Quark`. `QOU.BringCone` builds a
grading `Γ_u` and a chirality flip `M_j` on the quaternionic cone. This file asks what a
map from the eight labels into the cone can be, given only those two structures.

## What is forced

* **The flip can only be matched projectively.** A map with `φ ∘ flipChirality = M_j ∘ φ`
  on vectors is zero (or 2-torsion): `flipChirality` is an involution while
  `M_j² = −id` (`no_vector_equivariant_map`). So the match has to hold on rays, up to a
  sign.
* **The right-handed images are forced by the left-handed ones.** Given images of the
  four left-handed labels in the `Γ_u = −1` eigenspace (`seed`), `gen1Ray seed` sends each
  right-handed label to `M_j` of its left partner. Then:
  - left-handed labels go to `Γ_u = −1`, right-handed ones to `Γ_u = +1`
    (`gen1Ray_gamma`);
  - `flipChirality` becomes `M_j` up to the sign `±1` (`gen1Ray_flip`);
  - any map with these properties is `gen1Ray` of its own left-handed values
    (`gen1Ray_unique`).
* **Particle ↔ antiparticle cannot be `M_j` or `M_k`.** In V10 the particle bit is even
  under the flip (`flavour_and_particle_even_under_flip`), so an operator realising
  particle ↔ antiparticle has to keep each chirality. `M_j` and `M_k` exchange the two
  chiralities, so applied to a `Γ_u = −1` vector they give a `Γ_u = −1` vector only if the
  result is 2-torsion (`reebM_j_not_chirality_preserving`, `reebM_k_not_chirality_preserving`).
  `M_i` keeps each chirality (`reebM_i_preserves_eigenU`). That is a constraint, not a
  derivation: nothing here shows that `M_i` is the charge conjugation.

## What is left free, as an explicit parameter

* **Flavour, and the particle placement, are the `seed`.** Nothing in the cone structure
  separates `u` from `d`, or a particle from its antiparticle, inside the `Γ_u = −1`
  eigenspace. The constant seed `1` at `u = i` satisfies every hypothesis
  (`constSeed_eigen`) and maps `uL` and `dL` to the same vector
  (`constSeed_collapses_flavour`). So the flavour dictionary has to come from somewhere
  else. Probe #7781 found that γγ selection does not fix it either.
* **The base unit `u`.** Every statement takes `u` as a parameter. By
  `QOU.BringConeGauge` the choice is a gauge over ordered fields.

🛑 Hopf model `ℍ`, not Bring's own cone (`QOU/BringConeSplitChirality.lean` covers the
split model, where the flip has to be `M_i` instead of `M_j`). Nothing is wired, and no
observable is predicted.
-/

namespace QOU.StandardModel.Chirality

open QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-- **No vector-level equivariance.** If `φ (flipChirality x) = M_j (φ x)` for every
label, every image is 2-torsion: `flipChirality² = id` but `M_j² = −id`. -/
theorem no_vector_equivariant_map (φ : Gen1Quark → BringCone R)
    (h : ∀ x, φ (flipChirality x) = reebM_j (φ x)) (x : Gen1Quark) :
    φ x + φ x = 0 := by
  have e : φ x = -φ x := by
    calc φ x = φ (flipChirality (flipChirality x)) := by rw [flipChirality_involutive]
      _ = reebM_j (reebM_j (φ x)) := by rw [h, h]
      _ = -φ x := reebM_j_sq _
  calc φ x + φ x = φ x + -φ x := by rw [← e]
    _ = 0 := add_neg_cancel _

/-- The map built from images of the left-handed labels: a left-handed label goes to
its `seed`, a right-handed one to `M_j` of its left partner's `seed`. -/
def gen1Ray (seed : Gen1Quark → BringCone R) : Gen1Quark → BringCone R :=
  fun x => if chirality x = true then seed x else reebM_j (seed (flipChirality x))

theorem gen1Ray_left {seed : Gen1Quark → BringCone R} {x : Gen1Quark}
    (hx : chirality x = true) : gen1Ray seed x = seed x := by
  simp [gen1Ray, hx]

theorem gen1Ray_right {seed : Gen1Quark → BringCone R} {x : Gen1Quark}
    (hx : chirality x = false) : gen1Ray seed x = reebM_j (seed (flipChirality x)) := by
  simp [gen1Ray, hx]

/-- **Chirality goes to the eigenvalue of `Γ_u`**: left-handed to `−1`, right-handed to
`+1`, provided the seed puts the left-handed labels in the `Γ_u = −1` eigenspace. -/
theorem gen1Ray_gamma {u : BringCone R} {seed : Gen1Quark → BringCone R}
    (hseed : ∀ x, chirality x = true → chiralGammaU u (seed x) = -seed x)
    (x : Gen1Quark) :
    chiralGammaU u (gen1Ray seed x)
      = (if chirality x = true then (-1 : R) else 1) • gen1Ray seed x := by
  cases hx : chirality x
  · have hf : chirality (flipChirality x) = true := by
      rw [gen1_chirality_odd_under_flip, hx]; rfl
    rw [gen1Ray_right hx, reebM_j_flips_eigenU (hseed _ hf)]
    simp
  · rw [gen1Ray_left hx, hseed x hx]
    simp

/-- **`flipChirality` becomes `M_j` up to the sign `±1`** (`+1` from left to right, `−1`
from right to left). This is the ray-level form `no_vector_equivariant_map` allows. -/
theorem gen1Ray_flip (seed : Gen1Quark → BringCone R) (x : Gen1Quark) :
    gen1Ray seed (flipChirality x)
      = (if chirality x = true then (1 : R) else -1) • reebM_j (gen1Ray seed x) := by
  cases hx : chirality x
  · have hf : chirality (flipChirality x) = true := by
      rw [gen1_chirality_odd_under_flip, hx]; rfl
    rw [gen1Ray_left hf, gen1Ray_right hx, reebM_j_sq]
    simp
  · have hf : chirality (flipChirality x) = false := by
      rw [gen1_chirality_odd_under_flip, hx]; rfl
    rw [gen1Ray_right hf, gen1Ray_left hx, flipChirality_involutive]
    simp

/-- **The right-handed images are forced.** A map that sends each left-handed label's
partner to `M_j` of its image equals `gen1Ray` of itself: only the four left-handed
values are free. -/
theorem gen1Ray_unique (φ : Gen1Quark → BringCone R)
    (h : ∀ x, chirality x = true → φ (flipChirality x) = reebM_j (φ x))
    (x : Gen1Quark) : φ x = gen1Ray φ x := by
  cases hx : chirality x
  · have hf : chirality (flipChirality x) = true := by
      rw [gen1_chirality_odd_under_flip, hx]; rfl
    rw [gen1Ray_right hx, ← h _ hf, flipChirality_involutive]
  · rw [gen1Ray_left hx]

/-- **`M_j` cannot realise a chirality-preserving label map.** Applied to a `Γ_u = −1`
vector, it gives a `Γ_u = −1` vector only if the result is 2-torsion. -/
theorem reebM_j_not_chirality_preserving {u p : BringCone R}
    (hp : chiralGammaU u p = -p) (h : chiralGammaU u (reebM_j p) = -reebM_j p) :
    reebM_j p + reebM_j p = 0 := by
  have h1 := reebM_j_flips_eigenU hp
  rw [h1] at h
  calc reebM_j p + reebM_j p = reebM_j p + -reebM_j p := by rw [← h]
    _ = 0 := add_neg_cancel _

/-- The same for `M_k`. -/
theorem reebM_k_not_chirality_preserving {u p : BringCone R}
    (hp : chiralGammaU u p = -p) (h : chiralGammaU u (reebM_k p) = -reebM_k p) :
    reebM_k p + reebM_k p = 0 := by
  have h1 := reebM_k_flips_eigenU hp
  rw [h1] at h
  calc reebM_k p + reebM_k p = reebM_k p + -reebM_k p := by rw [← h]
    _ = 0 := add_neg_cancel _

/-! ### Flavour is not fixed by the cone structure -/

/-- The constant seed `1`. -/
def constSeed : Gen1Quark → BringCone R := fun _ => 1

/-- It satisfies the seed hypothesis at `u = i`: `Γ_i 1 = i·1·i = −1`. -/
theorem constSeed_eigen (x : Gen1Quark) (_ : chirality x = true) :
    chiralGammaU unitI (constSeed (R := R) x) = -constSeed x := by
  simp only [constSeed, chiralGammaU, Tetraplectic.leftMul, reebM_i_eq_mul_unitI, one_mul,
    unitI_mul_unitI]

/-- **And it does not separate flavour**: `uL` and `dL` go to the same vector. So the
`u`/`d` assignment is not determined by the grading, the flip, or the Reeb triad; it is
an input (the `seed`). -/
theorem constSeed_collapses_flavour :
    gen1Ray (constSeed (R := R)) Gen1Quark.uL = gen1Ray constSeed Gen1Quark.dL := by
  rfl

end QOU.StandardModel.Chirality
