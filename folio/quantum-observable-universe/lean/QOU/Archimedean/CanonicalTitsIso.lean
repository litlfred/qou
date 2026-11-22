/-
# The canonical Tits `*`-iso fixes the τ-intertwiner gauge (B2 sub-piece ii, final input)

The B2 wall reduces (PR #4199) to one open input: the **canonical**
(q-deformation-pinned) Tits `*`-iso `T = τ` relating the Hecke `(4,1)` module to
the geometric S₅ `(4,1)` module. Schur pins the intertwiner only up to a scalar
`μ` — sibling #4192 (`invariantForm_pullback_smul`) shows `T ↦ μ•T` scales the
transported Markov Gram `Tᵀ·G_Markov·T` by `μ²`, so the proportionality scalar `c`
of `markovGram_transports_to_hodge` is **gauge-dependent** (only its sign is
frame-free, #4192 `sq_pos_of_gauge`).

This file identifies what the *canonical* Tits `*`-iso adds: it is a **`*`-isometry**
— `Tᵀ·G_Markov·T = G_Hodge` *exactly*, both forms in their canonical
(Markov-trace / principal-polarization) normalizations. That single condition
**fixes the μ²-gauge**:

* `canonical_frame_c_eq_one` (sorry-free) — if `T` realises the proportionality
  `Tᵀ·G_Markov·T = c•G_Hodge` **and** is an exact `*`-isometry
  `Tᵀ·G_Markov·T = G_Hodge`, then `c = 1`. So in the canonical (isometric) frame
  the identification `τ(Markov Gram) = G_Hodge` holds with `|c| = 1`; any other
  intertwiner's `c ≠ 1` merely measures its deviation from that normalization.

**What stays OPEN (STRICT, §"Axiomatization is NOT a Proof").** This does NOT
construct `τ`. The remaining input is the *existence* of a `HeckeSideS5Symmetry`
conjugator `T = τ` that is simultaneously (i) an exact `*`-isometry of the two
canonically-normalized forms and (ii) the q-deformation-canonical Tits iso — genuine
Tits-deformation / Geck–Pfeiffer content (the seminormal rep of `H₅(q)` deforming
to Young's orthogonal S₅ rep at `q=1`). No `CanonicalTitsStarIso` / `TauRhoHodgeLift`
instance is registered; `1/(8π)` stays a phase-4 identification; nothing is wired.

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [serre1977] Linear Representations of Finite Groups (Tits deformation)
-/
import QOU.Archimedean.TauS5EquivarianceReduction

namespace QOU.Archimedean.CanonicalTitsIso

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n] {k : Type*} [Field k]

omit [DecidableEq n] in
/-- **The canonical (`*`-isometric) frame pins `c = 1`.** If the τ-intertwiner `T`
realises both the Schur proportionality `Tᵀ·G_Markov·T = c•G_Hodge` and the exact
`*`-isometry `Tᵀ·G_Markov·T = G_Hodge` (the defining property of the canonical Tits
`*`-iso, both forms canonically normalised), then `c = 1`. This is the sense in
which the canonical Tits iso removes the μ²-gauge freedom of #4192: it is the
`c = 1` frame. -/
theorem canonical_frame_c_eq_one {T G_Markov G_Hodge : Matrix n n k} {c : k}
    (hprop : Tᵀ * G_Markov * T = c • G_Hodge)
    (hiso : Tᵀ * G_Markov * T = G_Hodge)
    (hGH : G_Hodge ≠ 0) : c = 1 := by
  have h : c • G_Hodge = (1 : k) • G_Hodge := by rw [← hprop, hiso, one_smul]
  have h2 : (c - 1) • G_Hodge = 0 := by rw [sub_smul, h, sub_self]
  rcases smul_eq_zero.mp h2 with hc | hg
  · exact sub_eq_zero.mp hc
  · exact absurd hg hGH

end QOU.Archimedean.CanonicalTitsIso
