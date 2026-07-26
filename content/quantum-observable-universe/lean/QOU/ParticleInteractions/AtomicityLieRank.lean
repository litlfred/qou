import Mathlib.Algebra.Lie.Rank
import Mathlib.Algebra.Lie.Classical
import Mathlib.Tactic

/-!
# Atomicity — the Lie-algebra-rank route to the upper bound (`qou-atsd`, T3-lie)

The atomicity upper bound needs `rank G ≤ 1` for the Tannaka dual `G` — the piece
the elementary matrix route (`AtomicityFromSelfDuality.lean`) could not close,
because algebraic-**group** rank is not in Mathlib. But `rank G = rank Lie(G)`, and
Mathlib **does** have Lie-algebra rank (`LieAlgebra.rank`) together with the
specific-element upper bound

  `rank R L ≤ (ad R L x).charpoly.natTrailingDegree`   (`rank_le_natTrailingDegree_charpoly_ad`).

So the residual reframes to a **Mathlib-reachable** statement: for `Lie(SL₂) = 𝔰𝔩₂`
with the regular diagonal `h = diag(1,−1)`, `ad h` has characteristic polynomial
`X³ − 4X` (eigenvalues `0, 2, −2` on the basis `h, e, f`), whose trailing degree is
`1` — giving `rank 𝔰𝔩₂ ≤ 1`, the atomicity upper bound.

This file lands the **frame** (`rank_le_one_of_ad_charpoly_trailing`): the general
reduction from a trailing-degree-≤1 witness to `rank ≤ 1`. The concrete `𝔰𝔩₂`
charpoly computation `natTrailingDegree (charpoly (ad h)) = 1` — the genuine
remaining core — is bean `qou-atsd-t3-lie`.

-- Ref: [manuscript] conj:binding-manybody-eq-jet-filtration (atomicity); def:tannaka-dual
-/

namespace QOU.Atomicity

open LieAlgebra

/-- **Lie-rank route to the atomicity upper bound (frame).** If a Lie algebra `L`
    over `R` carries an element `x` whose `ad`-characteristic polynomial has
    trailing degree `≤ 1`, then `rank R L ≤ 1`. Immediate from Mathlib's
    specific-element rank bound `rank_le_natTrailingDegree_charpoly_ad`.

    This is the closeable reframing of the atomicity residual: with `rank G =
    rank Lie(G)` it replaces the (Mathlib-absent) algebraic-group root count by a
    Lie-algebra charpoly computation. Applied to `𝔰𝔩₂` and the regular diagonal
    `h` (whose `ad h` charpoly is `X³ − 4X`, trailing degree 1) it yields
    `rank 𝔰𝔩₂ ≤ 1` — the atomicity upper bound. The concrete `𝔰𝔩₂` computation is
    the remaining core (bean `qou-atsd-t3-lie`); no instance is fabricated here. -/
theorem rank_le_one_of_ad_charpoly_trailing
    {R L : Type*} [CommRing R] [Nontrivial R] [LieRing L] [LieAlgebra R L]
    [Module.Finite R L] [Module.Free R L] (x : L)
    (hx : (ad R L x).charpoly.natTrailingDegree ≤ 1) :
    rank R L ≤ 1 :=
  (rank_le_natTrailingDegree_charpoly_ad R x).trans hx

/-! ## The 𝔰𝔩₂ triple and its `ad h` eigenstructure (T3-lie core, in progress)

The standard basis of `𝔰𝔩₂ = sl (Fin 2) R`: `e = E₀₁`, `f = E₁₀`, `h = diag(1,−1)`.
The bracket is the matrix commutator (`sl_bracket`). The Cartan element `h` acts by
`[h,e]=2e`, `[h,f]=−2f`, `[h,h]=0` — so on the basis `(h,e,f)`, `ad h` is
`diag(0,2,−2)`, charpoly `X³−4X`, trailing degree `1`. This section lands the
bracket relations; the basis + charpoly assembly is bean `qou-atsd-t3-lie`. -/

section SL2
open Matrix LieAlgebra.SpecialLinear

variable (R : Type*) [CommRing R]

/-- `e = E₀₁ ∈ 𝔰𝔩₂`. -/
noncomputable def sl2E : sl (Fin 2) R := single 0 1 (by decide) 1
/-- `f = E₁₀ ∈ 𝔰𝔩₂`. -/
noncomputable def sl2F : sl (Fin 2) R := single 1 0 (by decide) 1
/-- `h = diag(1,−1) ∈ 𝔰𝔩₂`. -/
noncomputable def sl2H : sl (Fin 2) R := singleSubSingle 0 1 1

/-- **`[h,e] = 2e`** — the raising eigenvalue. -/
theorem sl2_bracket_h_e : ⁅sl2H R, sl2E R⁆ = (2 : R) • sl2E R := by
  apply Subtype.ext
  rw [sl_bracket]
  simp only [sl2H, sl2E, val_singleSubSingle, val_single, SetLike.val_smul]
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [Matrix.single, Matrix.of_apply, Matrix.mul_apply]
  all_goals ring

/-- **`[h,f] = −2f`** — the lowering eigenvalue. -/
theorem sl2_bracket_h_f : ⁅sl2H R, sl2F R⁆ = (-2 : R) • sl2F R := by
  apply Subtype.ext
  rw [sl_bracket]
  simp only [sl2H, sl2F, val_singleSubSingle, val_single, SetLike.val_smul]
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [Matrix.single, Matrix.of_apply, Matrix.mul_apply]
  all_goals ring

/-- **`[h,h] = 0`** — the Cartan element is `ad`-fixed. -/
theorem sl2_bracket_h_h : ⁅sl2H R, sl2H R⁆ = (0 : sl (Fin 2) R) := by
  apply Subtype.ext
  rw [sl_bracket]
  simp [sl2H, val_singleSubSingle]

/-- **Trace-zero coordinates.** Every `x ∈ 𝔰𝔩₂` decomposes on the triple as
    `x = x₀₀·h + x₀₁·e + x₁₀·f` — the `(1,1)` entry is `−x₀₀` by tracelessness. This
    is the constructive spanning statement for the basis `(h,e,f)`. -/
theorem sl2_decomp (x : sl (Fin 2) R) :
    x = (x.val 0 0) • sl2H R + (x.val 0 1) • sl2E R + (x.val 1 0) • sl2F R := by
  have htr : x.val 0 0 + x.val 1 1 = 0 := by
    have h0 : Matrix.trace x.val = 0 := x.2
    rwa [Matrix.trace_fin_two] at h0
  apply Subtype.ext
  simp only [sl2H, sl2E, sl2F]
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [Matrix.single, Matrix.of_apply]
  linear_combination htr

end SL2

end QOU.Atomicity
