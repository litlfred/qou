import QOU.Archimedean.BorromeanVolumeCatalan
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-!
# Whitehead link volume — Catalan-constant identity `Vol(L5a1) = 4·G`

The Step-2 geometric input for the Whitehead row of
`conj:b1-hyperbolic-rows-theorem`.  Companion to
`BorromeanVolumeCatalan.lean`:

* the **Borromean rings** complement `𝓑₃` (L6a4) decomposes into **two**
  regular ideal octahedra ⇒ `Vol(𝓑₃) = 8·G`;
* the **Whitehead link** complement (L5a1) is a **single** regular ideal
  octahedron ⇒ `Vol(L5a1) = 4·G = ½·Vol(𝓑₃)` (Thurston; Wielenberg 1978).

Here `G` is Catalan's constant (`catalan_G`, upstream in
`HyperbolicVolumeTranscendence`) and each regular ideal octahedron has
volume `8·Λ(π/4) = 4·G` (Lobachevsky–Catalan identity, `lobachevsky` /
`lobachevsky_pi_div_four_eq_half_catalan`, both from
`BorromeanVolumeCatalan`).

## What is / isn't Lean here (honesty, per AGENTS.md §Axiomatization-is-NOT-a-Proof)

* **Proved sorry-free below**: `Vol(L5a1) = 4·G`, the exact half-Borromean
  relation `Vol(L5a1) = Vol(𝓑₃)/2`, the octahedral form
  `Vol(L5a1) = 8·Λ(π/4)`, positivity, and the numerical bracket
  `3.66 < Vol(L5a1) < 3.67`.  These are algebraic consequences of the
  same `catalan_G` / Lobachevsky infrastructure the Borromean file uses.
* **NOT proved here** (and deliberately not laundered into a theorem): the
  **Volume Conjecture** for the Whitehead link — that the reduced colored
  Jones evaluated at `q = e^{2πi/N}` grows at rate `Vol(L5a1)`.  That
  asymptotic is verified only **numerically** in
  `computations/whitehead_volume_search.py` (growth → 4G, formula-free) and
  `computations/whitehead_c0_run.py` (the sub-leading factor).  It is the
  Step-3 gap of `conj:b1-hyperbolic-rows-theorem` and remains a
  conjecture-class; the numerics are evidence for its instance, not a proof.

## References

- [adams1985hyperbolic] Adams, C. C. (1985), Proc. Amer. Math. Soc. 100, 601-606.
- [wielenberg1978] Wielenberg, N. (1978), "The structure of certain subgroups
  of the Picard group", Math. Proc. Cambridge Philos. Soc. 84, 427-436
  (Whitehead link complement = regular ideal octahedron).
- [lewin1981] Lewin, L. (1981), Polylogarithms and Associated Functions.
-/

namespace QOU.Archimedean.WhiteheadVolume

open Real

/-- Hyperbolic volume of the Whitehead link complement `L5a1`, as the exact
    symbolic value `4 · G` (one regular ideal octahedron).

    -- Ref: [wielenberg1978] the Whitehead complement is a single regular
            ideal octahedron; [adams1985hyperbolic] octahedron volume = 4G. -/
noncomputable def vol_L5a1 : ℝ := 4 * catalan_G

/-- `Vol(L5a1) = 4·G` — definitional. -/
theorem vol_L5a1_eq_4_catalan : vol_L5a1 = 4 * catalan_G := rfl

/-- **Exact half-Borromean relation**: `Vol(L5a1) = Vol(𝓑₃) / 2`.

    The Whitehead complement is one regular ideal octahedron; the Borromean
    complement is two.  Both volumes are `catalan_G` multiples, so the
    relation is an exact algebraic identity (`4G = 8G / 2`), proved
    sorry-free — no numerical approximation. -/
theorem vol_L5a1_eq_half_vol_B3 : vol_L5a1 = vol_B3 / 2 := by
  rw [vol_L5a1_eq_4_catalan, vol_B3_eq_8_catalan]; ring

/-- **Octahedral (Lobachevsky) form**: `Vol(L5a1) = 8·Λ(π/4)`.

    A single regular ideal octahedron has volume `8·Λ(π/4)`; combined with
    the Lobachevsky–Catalan identity `Λ(π/4) = G/2` this is `4G`. -/
theorem vol_L5a1_eq_eight_lobachevsky :
    vol_L5a1 = 8 * lobachevsky (π / 4) := by
  rw [vol_L5a1_eq_4_catalan, lobachevsky_pi_div_four_eq_half_catalan]; ring

/-- `Vol(L5a1) > 0`. -/
theorem vol_L5a1_pos : vol_L5a1 > 0 := by
  rw [vol_L5a1_eq_4_catalan]
  have := catalan_G_pos; linarith

/-- `Vol(L5a1) ≠ 0`. -/
theorem vol_L5a1_ne_zero : vol_L5a1 ≠ 0 := ne_of_gt vol_L5a1_pos

/-- Numerical bracket: `3.66 < Vol(L5a1) < 3.67` (from `0.915 < G < 0.916`).
    Matches the SnapPy census value `3.663862376708…` for L5a1. -/
theorem vol_L5a1_numerical_bounds :
    vol_L5a1 > (3.66 : ℝ) ∧ vol_L5a1 < (3.67 : ℝ) := by
  rw [vol_L5a1_eq_4_catalan]
  obtain ⟨hlo, hhi⟩ := catalan_G_numerical_bounds
  constructor
  · linarith
  · linarith

/-- `Vol(L5a1) < Vol(𝓑₃)` — the Whitehead sits below the Borromean on the
    hyperbolic-volume ladder of Table 3 building-block links (one octahedron
    vs two). -/
theorem vol_L5a1_lt_vol_B3 : vol_L5a1 < vol_B3 := by
  rw [vol_L5a1_eq_4_catalan, vol_B3_eq_8_catalan]
  have := catalan_G_pos; linarith

end QOU.Archimedean.WhiteheadVolume
