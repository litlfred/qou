import Mathlib.Tactic
import QOU.BringConeSplit

/-!
# The chirality construction on the split model of Bring's own link

Bean `qou-wqto`, issue #7783, step (b). `QOU.BringCone` builds the chirality grading
`Γ_u = L_u ∘ M_i` and its flip `ι = M_j` on the **Hopf** model `ℍ`. Bring's own link is
`UT(Σ₄) = PSL(2,ℝ)/Γ₄` (bean `qou-rydq`, `QOU/Brings/BringConeLinkEulerNumber.lean`), and
its Reeb triad is the `𝔰𝔩₂(ℝ)` triad of the **split** quaternions `M₂(R)`
(`QOU/BringConeSplit.lean`). This file runs the Hopf-model construction on the split
model and records which parts survive. All of it is algebra over generic `[CommRing R]`.

## What carries over, and what does not

1. **The Hopf-model flip `ι = M_j` does not carry over.** In the split model `j² = +1`, so
   `M_j² = id` (`M_j_sq`) and `M_j` fixes the nonzero vector `1 + j` (`M_j_fixes`). It has
   a fixed ray, so by V10's `free_of_reeb_odd_grading` it cannot flip a grading on rays.
   The same holds for `M_k` (`M_k_fixes`).
2. **The compact generator `M_i`, the fibre rotation `V`, is the only ray-free Reeb
   operator.** `M_i² = −id` (`M_i_sq`), and `M_i` has no eigen-ray unless `c² + 1 = 0`
   (`M_i_ray_free`). In the split model `ι` has to be `M_i`, not `M_j`.
3. **A grading needs no second complex structure here.** `M_j` is itself a grading
   (`M_j_sq`), and `M_i` anticommutes with it (`M_i_anticomm_M_j`), so it exchanges the
   two `M_j`-eigenvectors (`M_i_flips_M_j_eigen`). This is V10's shape (`ι` free on rays,
   `chir` odd), built from the Reeb triad alone.
4. **The second complex structure of the Hopf model does not descend to the link.** On a
   quotient by a lattice `Γ₄`, a left multiplication `L_u` is well defined only if `u`
   commutes with every element of `Γ₄`. If the span of `Γ₄` contains `i` and `j`, every
   such `u` is a scalar (`commutes_span_scalar`). So on the global link the commutant of
   the triad leaves only scalars, and `L_u ∘ M_x` reduces to `±M_x`.

## The gap, stated exactly

* **Lattice spanning: a hypothesis, not proved here.** That the R-span of
  Bring's surface group `Γ₄ ⊂ SL(2,ℝ)` contains `i` and `j` would follow from Borel
  density of a cocompact lattice (it is Zariski dense, so it spans `M₂(ℝ)`). Borel density
  is not in the corpus or in the library, so `commutes_span_scalar` takes the spanning as a
  hypothesis.
* **States, not vectors.** These are statements about the `R`-module `M₂(R)` and its
  rays. Points of the link are elements of `SL(2,ℝ)/Γ₄`, and right multiplication by `j`
  or `k` (reduced norm `−1`) does not preserve `SL(2)`, so `M_j` is not a point map on the
  link. Only `M_i` (norm `+1`) acts on points. Which object the physical states are (rays
  of the module, points of `UT(Σ₄)`, or sections over `Σ₄`) is not fixed by the corpus,
  and nothing here decides it.
* **Nothing is wired.** No observable moves, and `archimedean-chirality.md` still asserts
  rather than derives the Reeb involution on states.
-/

namespace QOU.Tetraplectic.Split

variable {R : Type*} [CommRing R]

/-- The split unit `i` (`i² = −1`). -/
def sI : SplitBringCone R := ⟨0, 1, 0, 0⟩
/-- The split unit `j` (`j² = +1`). -/
def sJ : SplitBringCone R := ⟨0, 0, 1, 0⟩
/-- The split unit `k = ij` (`k² = +1`). -/
def sK : SplitBringCone R := ⟨0, 0, 0, 1⟩

/-! ## 1. Squares: one compact, two hyperbolic -/

/-- `M_i² = −id`: the fibre rotation has order four, like the Hopf model. -/
theorem M_i_sq (p : SplitBringCone R) : M_i (M_i p) = -p := by
  dsimp [M_i]; ext <;> simp

/-- `M_j² = id`: the geodesic-flow generator is an involution on vectors, unlike the
Hopf model's `reebM_j_sq`. -/
theorem M_j_sq (p : SplitBringCone R) : M_j (M_j p) = p := by
  dsimp [M_j]; ext <;> simp

/-- `M_k² = id`. -/
theorem M_k_sq (p : SplitBringCone R) : M_k (M_k p) = p := by
  dsimp [M_k]; ext <;> simp

/-! ## 2. The Hopf-model flip has fixed rays here -/

/-- **`M_j` fixes `1 + j`.** -/
theorem M_j_fixes : M_j ((1 : SplitBringCone R) + sJ) = 1 + sJ := by
  dsimp [M_j, sJ]; ext <;> simp

/-- **`M_k` fixes `1 + k`.** -/
theorem M_k_fixes : M_k ((1 : SplitBringCone R) + sK) = 1 + sK := by
  dsimp [M_k, sK]; ext <;> simp

theorem one_add_sJ_ne_zero [Nontrivial R] : (1 : SplitBringCone R) + sJ ≠ 0 := by
  intro h
  have := congrArg (fun x : SplitBringCone R => x.re) h
  simp [sJ] at this

theorem one_add_sK_ne_zero [Nontrivial R] : (1 : SplitBringCone R) + sK ≠ 0 := by
  intro h
  have := congrArg (fun x : SplitBringCone R => x.re) h
  simp [sK] at this

/-- **`M_j` has an eigen-ray**, eigenvalue `1`. So the Hopf-model choice `ι = M_j` is not
fixed-point free on rays of the split model, and V10's `free_of_reeb_odd_grading` rules it
out as a chirality flip there. -/
theorem M_j_not_ray_free [Nontrivial R] :
    ∃ p : SplitBringCone R, p ≠ 0 ∧ M_j p = (1 : R) • p :=
  ⟨1 + sJ, one_add_sJ_ne_zero, by rw [one_smul]; exact M_j_fixes⟩

/-- The same for `M_k`. -/
theorem M_k_not_ray_free [Nontrivial R] :
    ∃ p : SplitBringCone R, p ≠ 0 ∧ M_k p = (1 : R) • p :=
  ⟨1 + sK, one_add_sK_ne_zero, by rw [one_smul]; exact M_k_fixes⟩

/-! ## 3. The fibre rotation is ray-free, and flips the triad's own grading -/

/-- **`M_i` has no eigen-ray** unless `c² + 1 = 0`: whenever `−1` is not a square in `R`
and scalars cancel, `M_i` fixes no ray. -/
theorem M_i_ray_free {p : SplitBringCone R} {c : R}
    (hcancel : ∀ (a : R) (x : SplitBringCone R), a • x = 0 → x ≠ 0 → a = 0)
    (hp : p ≠ 0) (h : M_i p = c • p) : c * c + 1 = 0 := by
  have h2 : M_i (M_i p) = (c * c) • p := by
    rw [h]
    have : M_i (c • p) = c • M_i p := by
      dsimp [M_i]; ext <;> simp
    rw [this, h, smul_smul]
  rw [M_i_sq] at h2
  apply hcancel _ p _ hp
  rw [add_smul, one_smul, ← h2, neg_add_cancel]

/-- **`M_i` anticommutes with `M_j`.** -/
theorem M_i_anticomm_M_j (p : SplitBringCone R) : M_j (M_i p) = -M_i (M_j p) := by
  dsimp [M_i, M_j]; ext <;> simp

/-- `M_i` anticommutes with `M_k` too. -/
theorem M_i_anticomm_M_k (p : SplitBringCone R) : M_k (M_i p) = -M_i (M_k p) := by
  dsimp [M_i, M_k]; ext <;> simp

/-- **`M_i` exchanges the two `M_j`-chiralities**: it sends an `M_j = s` eigenvector to an
`M_j = −s` eigenvector. With `M_j` as the grading (`M_j_sq`) and `M_i` as the flip, this is
V10's shape (flip free on rays, grading odd), using only the Reeb triad. -/
theorem M_i_flips_M_j_eigen {p : SplitBringCone R} {s : R} (hp : M_j p = s • p) :
    M_j (M_i p) = -(s • M_i p) := by
  rw [M_i_anticomm_M_j, hp]
  congr 1
  dsimp [M_i]; ext <;> simp

/-! ## 4. A left multiplication that descends to a lattice quotient is a scalar -/

/-- The elements commuting with `u` form a submodule. -/
def commSubmodule (u : SplitBringCone R) : Submodule R (SplitBringCone R) where
  carrier := {x | u * x = x * u}
  add_mem' {a b} ha hb := by
    simp only [Set.mem_setOf_eq] at *
    rw [mul_add, add_mul, ha, hb]
  zero_mem' := by simp
  smul_mem' c x hx := by
    simp only [Set.mem_setOf_eq] at *
    rw [mul_smul_comm, smul_mul_assoc, hx]

/-- Commuting with `i` and `j` forces `u` to be a scalar, when `2` is cancellable. -/
theorem scalar_of_comm_sI_sJ {u : SplitBringCone R}
    (h2 : ∀ x : R, 2 * x = 0 → x = 0)
    (hi : u * sI = sI * u) (hj : u * sJ = sJ * u) :
    u.imI = 0 ∧ u.imJ = 0 ∧ u.imK = 0 := by
  have a1 := congrArg (fun x : SplitBringCone R => x.re) hi
  have a2 := congrArg (fun x : SplitBringCone R => x.imJ) hi
  have a3 := congrArg (fun x : SplitBringCone R => x.imK) hi
  have b1 := congrArg (fun x : SplitBringCone R => x.re) hj
  have b2 := congrArg (fun x : SplitBringCone R => x.imI) hj
  have b3 := congrArg (fun x : SplitBringCone R => x.imK) hj
  simp [sI, sJ] at a1 a2 a3 b1 b2 b3
  refine ⟨h2 _ ?_, h2 _ ?_, h2 _ ?_⟩ <;>
    first
    | linear_combination b3 | linear_combination -b3
    | linear_combination a3 | linear_combination -a3
    | linear_combination a2

/-- **A left multiplication `L_u` that commutes with every element of a set `S` whose span
contains `i` and `j` is a scalar.** On the link `SL(2)/Γ₄`, `L_u` is well defined exactly
when `u` commutes with `Γ₄`. So if `Γ₄` spans (Borel density, a hypothesis here), the
second complex structure of the Hopf model does not descend: the commutant of the triad
leaves only scalars. -/
theorem commutes_span_scalar {u : SplitBringCone R} {S : Set (SplitBringCone R)}
    (h2 : ∀ x : R, 2 * x = 0 → x = 0)
    (hS : ∀ γ ∈ S, u * γ = γ * u)
    (hi : sI ∈ Submodule.span R S) (hj : sJ ∈ Submodule.span R S) :
    u.imI = 0 ∧ u.imJ = 0 ∧ u.imK = 0 := by
  have hle : Submodule.span R S ≤ commSubmodule u :=
    Submodule.span_le.mpr (fun γ hγ => hS γ hγ)
  exact scalar_of_comm_sI_sJ h2 (hle hi) (hle hj)

end QOU.Tetraplectic.Split
