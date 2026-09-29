import Mathlib.Algebra.Quaternion
import Mathlib.Tactic
import QOU.BringCone

/-!
# The split model of the Bring-cone Reeb triad — `𝔰𝔩₂(ℝ)`, one sign away from `𝔰𝔲(2)`

`QOU.BringCone` models "the Reeb triad of the Bring cone link" by right-multiplication by
the units of the quaternions and proves `[M_i, M_j] = 2 M_k` **and cyclic** — three `+2`'s,
the compact form `𝔰𝔲(2)`. That is the triad of the Hopf link `S³` of the cone over `ℙ¹`.

The link of the Bring cone is not `S³`. Bézout (`1·2·3 = 6`) and adjunction (`K = 𝒪(1)`)
make the embedding canonical, so the link — the unit circle bundle of `𝒪(-1)|_C = K⁻¹ = TC`
— is the unit tangent bundle `UT(Σ₄)`, an `~SL₂` manifold
(`docs/audits/2026-09-03-bring-cone-link-is-the-unit-tangent-bundle.md`). A 3-Sasakian
3-manifold is a spherical space form, and a closed aspherical 3-manifold admits no
non-trivial `SU(2)`-action at all, so no triad of Reeb vector fields on `UT(Σ₄)` can close
into `𝔰𝔲(2)`. What `UT(Σ₄)` does carry is three genuine contact forms — the connection form
(Reeb field: fibre rotation `V`), the Liouville form (Reeb field: geodesic flow `X`) and its
rotation by a quarter turn in the fibre (Reeb field: `X⊥`) — whose Reeb fields are the
left-invariant frame of `PSL(2,ℝ)` and close into `𝔰𝔩₂(ℝ)`:

    [X, X⊥] = V,     [X⊥, V] = X,     [V, X] = −X⊥ .

Exactly one of the three cyclic brackets carries the opposite sign to `𝔰𝔲(2)`. That is the
whole difference between the compact and the split real form, and it is what the word
"degenerate" in "degenerate quaternionic-contact" has to mean if the lemma is to describe
this link at all.

This file makes the point in the lemma's own terms. Replace the quaternions by the **split
quaternions** — `i² = −1`, `j² = +1`, so `k² = +1`; the algebra `M₂(R)`, whose unit-norm
elements are `SL(2, R)` and whose pure-imaginary part is `𝔰𝔩₂(R)` — and run the same
right-multiplication construction. The same proof script gives

    [M_i, M_j] = 2 M_k,     [M_j, M_k] = −2 M_i,     [M_k, M_i] = 2 M_j ,

one sign flipped, and `split_ne_compact` records that the flipped bracket is not the compact
one in any ring of characteristic zero. So the conciliation works **only** as the split
form: the lemma's identities are true, and they are the identities of the wrong real form
for `UT(Σ₄)`. The `𝔰𝔲(2)` survives on this link only as the structure group of the
`ℍ`-valued resolvent bundle — an internal symmetry, which is how
`rem:tetraplectic-su2-gauge-reading` already reads it — not as a triad of Reeb fields.

Pure algebra over a generic `CommRing`, exactly like `BringCone.lean`; nothing archimedean
enters. Bean `qou-m3sh`.
-/

namespace QOU.Tetraplectic.Split

variable {R : Type*} [CommRing R]

/-- The split quaternions over `R`: `i² = −1`, `j² = +1`, `k = ij`, `k² = +1`. This is
`M₂(R)`, with unit-norm elements `SL(2, R)` and imaginary part `𝔰𝔩₂(R)` — the algebra whose
right-multiplication triad models the left-invariant frame of `PSL(2,ℝ)`. -/
abbrev SplitBringCone (R : Type*) [CommRing R] := QuaternionAlgebra R (-1) 0 1

/-- Split Reeb operator `M_i` — right-multiplication by the compact unit `i` (the fibre
rotation `V`). -/
def M_i (p : SplitBringCone R) : SplitBringCone R := p * ⟨0, 1, 0, 0⟩
/-- Split Reeb operator `M_j` — right-multiplication by the hyperbolic unit `j` (the geodesic
flow `X`). -/
def M_j (p : SplitBringCone R) : SplitBringCone R := p * ⟨0, 0, 1, 0⟩
/-- Split Reeb operator `M_k` — right-multiplication by the hyperbolic unit `k = ij` (the
rotated geodesic flow `X⊥`). -/
def M_k (p : SplitBringCone R) : SplitBringCone R := p * ⟨0, 0, 0, 1⟩

/-- `[M_i, M_j] = 2 M_k`: the same as the compact model. -/
theorem twist_ij (p : SplitBringCone R) :
    M_j (M_i p) - M_i (M_j p) = (2 : R) • M_k p := by
  dsimp [M_i, M_j, M_k]
  ext <;> simp <;> ring

/-- `[M_j, M_k] = −2 M_i`: the one sign that flips. In the compact model this is `+2 M_i`. -/
theorem twist_jk (p : SplitBringCone R) :
    M_k (M_j p) - M_j (M_k p) = -((2 : R) • M_i p) := by
  dsimp [M_i, M_j, M_k]
  ext <;> simp <;> ring

/-- `[M_k, M_i] = 2 M_j`: the same as the compact model. -/
theorem twist_ki (p : SplitBringCone R) :
    M_i (M_k p) - M_k (M_i p) = (2 : R) • M_j p := by
  dsimp [M_i, M_j, M_k]
  ext <;> simp <;> ring

/-- The flipped bracket is genuinely different from the compact one: at `p = 1` the split
`[M_j, M_k]` is `−2i` while the compact `[M_j, M_k]` is `+2i`, and these differ whenever
`4 ≠ 0` in `R`. -/
theorem split_ne_compact [CharZero R] :
    M_k (M_j (1 : SplitBringCone R)) - M_j (M_k 1) ≠ (2 : R) • M_i 1 := by
  rw [twist_jk]
  intro h
  have h' := congrArg QuaternionAlgebra.imI h
  simp [M_i] at h'
  norm_num at h'

/-- The structure constants of the two models, side by side: compact `(2, 2, 2)`, split
`(2, −2, 2)`. Read as a Lie algebra on the imaginary units, the first is `𝔰𝔲(2)` and the
second is `𝔰𝔩₂(R)`; a real rescaling of the basis cannot move between them. -/
theorem structure_constants :
    (∀ p : QOU.Tetraplectic.BringCone R,
        QOU.Tetraplectic.reebM_k (QOU.Tetraplectic.reebM_j p)
          - QOU.Tetraplectic.reebM_j (QOU.Tetraplectic.reebM_k p)
          = (2 : R) • QOU.Tetraplectic.reebM_i p)
    ∧ (∀ p : SplitBringCone R, M_k (M_j p) - M_j (M_k p) = -((2 : R) • M_i p)) :=
  ⟨QOU.Tetraplectic.reeb_twist_jk, twist_jk⟩

end QOU.Tetraplectic.Split
