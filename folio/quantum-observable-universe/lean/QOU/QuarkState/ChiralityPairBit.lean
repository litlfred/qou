/-
# On a γγ pair, the chirality swap is the orientation flip

Owner ruling 2026-11-15 (SM-map thread, "Restate: chirality is the pair bit"): D-H2 = no
still holds for single letters (`flip_ne_swap` in `HelicityCommonSource.lean`), and on a
γγ pair the vertex mirror `V̄` is the chirality mirror of `V`. This file proves the
pair-level identity the ruling cites.

The eigenline swap `ι : s ↦ −s⁻¹ = h − s` keeps a Hecke letter at the SAME parameter `q`
(`swap_hecke`). Extend it to the vertex `V = s · t⁻¹` (two letters `s = σᵢ`,
`t = σᵢ₊₁`) letterwise: `ι(V) = ι(s) · ι(t)⁻¹`. The inverse of the swapped letter is
`flip q (swap q t) = −t` (`flip_swap`, in `HelicityCommonSource.lean`), so

  `ι(V) = (h − s)(−t) = (s − h) t = s⁻¹ t = V̄`   (`iota_vertex`).

The two minus signs cancel. The identity is pure ring arithmetic: it needs no Hecke
relation, so it holds for any two elements, and for every power of the vertex
(`iota_vertex_pow`), in particular the length-3 words `VVV ↦ V̄V̄V̄`.

Contrast (single letter): `ι(s) = −s⁻¹ ≠ s⁻¹` in general, which is `flip_ne_swap`.

Base ring (§7c): generic `[Field K]`, `[Ring A] [Algebra K A]`. No `ℝ`.

-- Ref: [kazhdan-lusztig1979] https://doi.org/10.1007/BF01390031
-/
import QOU.QuarkState.HelicityCommonSource

namespace QOU.QuarkState.Helicity

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]

/-- The γγ vertex `V = s · t⁻¹`. -/
def vertex (q : K) (s t : A) : A := s * flip q t

/-- The mirror vertex `V̄ = s⁻¹ · t`. -/
def mirrorVertex (q : K) (s t : A) : A := flip q s * t

/-- The chirality swap extended letterwise to a vertex: `ι(s) · ι(t)⁻¹`. -/
def iotaVertex (q : K) (s t : A) : A := swap q s * flip q (swap q t)

/-- **On a pair, the chirality swap is the orientation flip:** `ι(V) = V̄`. -/
theorem iota_vertex (q : K) (s t : A) : iotaVertex q s t = mirrorVertex q s t := by
  unfold iotaVertex mirrorVertex
  rw [flip_swap]
  unfold swap flip
  rw [mul_neg, sub_mul, sub_mul, neg_sub]

/-- The same holds for every power of the vertex, e.g. `ι(VVV) = V̄V̄V̄`. -/
theorem iota_vertex_pow (q : K) (s t : A) (n : ℕ) :
    iotaVertex q s t ^ n = mirrorVertex q s t ^ n := by
  rw [iota_vertex]

/-- The swapped letters are still Hecke letters at `q`, so `ι(V)` is a vertex of the
same algebra at the same parameter: it is `vertex q (swap q s) (swap q t)`. -/
theorem iotaVertex_eq_vertex (q : K) (s t : A) :
    iotaVertex q s t = vertex q (swap q s) (swap q t) := rfl

end QOU.QuarkState.Helicity
