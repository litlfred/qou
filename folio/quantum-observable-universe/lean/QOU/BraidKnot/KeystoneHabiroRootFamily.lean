/-
Copyright (c) 2026 litlfred. All rights reserved.

# The Habiro root family supplies the interpolation points for `bwS0_eq_hecke`

Archimedean companion to
[`KeystoneGaugeRowRigidity.lean`](KeystoneGaugeRowRigidity.lean).  The rigidity
reduction `bwS0_eq_hecke_of_rigidity` needs the gauge row and the value-map
polynomial to agree at **more distinct fold points than their degree** — then they
are equal, and the continuation to `q₀` is forced.  This file supplies those points
from the **root-of-unity family** (the WRT / Habiro data): the fold values
`t_k = ζ + ζ⁻¹ = 2cos(kπ/N)` at level `N` are **all distinct** (`cos` is strictly
antitone on `[0, π]`), so the fibre roots up to level `N` give `N − 1` distinct
interpolation points.

Hence the antecedent of the rigidity reduction is met by **agreement of the gauge
row with the value map across the fibre roots up to any level `N > deg + 1`** — a
*concrete physical* condition (the WRT invariant equals the modular datum at each
root), replacing the abstract "enough points."  `KeystoneLRAmplitudeReal` (#4365)
supplies the `Σ(2,3,5)` slice of that agreement; the full antecedent is the Habiro
root-family agreement (Habiro-injectivity, #3681).

## Results (sorry-free)

* `foldValue_injOn` — `k ↦ 2cos(kπ/N)` is injective on `[1, N−1]` (distinct roots).
* `foldPoints_card` — the finset of fold values has `N − 1` elements.
* `eq_of_root_family_agreement` — if the gauge row and value-map polynomials agree
  on the level-`N` fold points and both have degree `< N − 1`, they are equal (hence
  agree at the substrate `t₀`).

**Honest scope (STRICT).** This proves the *interpolation-points* half of the
Habiro root-family agreement — that enough distinct points exist and that agreement
on them forces equality.  It does **not** prove that the gauge row `bwS0` actually
agrees with the value map at those roots (that is the WRT = modular-data content,
of which #4365 is the `Σ(2,3,5)` case) nor that `bwS0` is a bounded-degree
polynomial (Habiro rigidity, cited).  No `c_k`; no fit; nothing wired.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-- Ref: [habiro2004] https://doi.org/10.1007/s00222-007-0071-0
-/
import QOU.BraidKnot.KeystoneGaugeRowRigidity
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.BraidKnot.KeystoneHabiroRootFamily

open Polynomial Real

/-- The fold value of the level-`N`, index-`k` fibre root: `t_k = ζ + ζ⁻¹ =
2cos(kπ/N)`. -/
noncomputable def foldValue (N k : ℕ) : ℝ := 2 * Real.cos ((k : ℝ) * π / N)

/-- The angle `kπ/N` lies in `[0, π]` when `k ≤ N` (and `0 < N`). -/
theorem angle_mem_Icc {N k : ℕ} (hN : 0 < N) (hk : k ≤ N) :
    (k : ℝ) * π / N ∈ Set.Icc (0 : ℝ) π := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  refine ⟨by positivity, ?_⟩
  rw [div_le_iff₀ hNpos]
  have hkN : (k : ℝ) ≤ N := by exact_mod_cast hk
  nlinarith [Real.pi_pos, hkN]

/-- **The fold values are distinct.** `k ↦ 2cos(kπ/N)` is injective on `[1, N−1]`,
because `cos` is strictly antitone on `[0, π]` and `k ↦ kπ/N` is injective there. -/
theorem foldValue_injOn (N : ℕ) (hN : 0 < N) :
    Set.InjOn (foldValue N) ↑(Finset.Icc 1 (N - 1)) := by
  intro k hk k' hk' heq
  simp only [Finset.coe_Icc, Set.mem_Icc] at hk hk'
  have hkN : k ≤ N := le_trans hk.2 (Nat.sub_le N 1)
  have hk'N : k' ≤ N := le_trans hk'.2 (Nat.sub_le N 1)
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  -- strip the factor 2 and apply cos-injectivity on [0,π]
  have hcos : Real.cos ((k : ℝ) * π / N) = Real.cos ((k' : ℝ) * π / N) := by
    have : (2 : ℝ) * Real.cos ((k : ℝ) * π / N) = 2 * Real.cos ((k' : ℝ) * π / N) := heq
    linarith
  have hangle : (k : ℝ) * π / N = (k' : ℝ) * π / N :=
    Real.strictAntiOn_cos.injOn (angle_mem_Icc hN hkN) (angle_mem_Icc hN hk'N) hcos
  -- kπ/N = k'π/N with π, N > 0 ⇒ k = k' (cancel N, then π)
  have hπ : (0 : ℝ) < π := Real.pi_pos
  have hNr : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hN
  have h1 : (k : ℝ) * π * N = (k' : ℝ) * π * N :=
    (div_eq_div_iff hNr.ne' hNr.ne').mp hangle
  have h2 : (k : ℝ) * π = (k' : ℝ) * π := mul_right_cancel₀ hNr.ne' h1
  have hkk' : (k : ℝ) = (k' : ℝ) := mul_right_cancel₀ (ne_of_gt hπ) h2
  exact_mod_cast hkk'

/-- The finset of level-`N` fold values `{2cos(kπ/N) : 1 ≤ k ≤ N−1}` has exactly
`N − 1` elements. -/
theorem foldPoints_card (N : ℕ) (hN : 0 < N) :
    ((Finset.Icc 1 (N - 1)).image (foldValue N)).card = N - 1 := by
  rw [Finset.card_image_of_injOn (foldValue_injOn N hN), Nat.card_Icc]
  omega

/-- **The root family triggers rigidity.** If the gauge-row polynomial `bwPoly` and
the value-map polynomial `valPoly` agree at every level-`N` fold value and both have
degree `< N − 1`, then they are equal — hence agree at the substrate `t₀`.  The
antecedent is the concrete *root-of-unity agreement* (the WRT invariant equals the
modular datum at each fibre root); by `KeystoneGaugeRowRigidity` this pins the
continuation. -/
theorem eq_of_root_family_agreement
    (bwPoly valPoly : ℝ[X]) (N : ℕ) (hN : 0 < N)
    (hdeg_bw : bwPoly.natDegree < N - 1) (hdeg_val : valPoly.natDegree < N - 1)
    (hagree : ∀ k ∈ Finset.Icc 1 (N - 1),
      bwPoly.eval (foldValue N k) = valPoly.eval (foldValue N k)) :
    bwPoly = valPoly := by
  set S := (Finset.Icc 1 (N - 1)).image (foldValue N) with hS
  have hcard : S.card = N - 1 := foldPoints_card N hN
  refine KeystoneGaugeRowRigidity.eq_of_eval_agree_card bwPoly valPoly S
    (hcard ▸ hdeg_bw) (hcard ▸ hdeg_val) ?_
  intro x hx
  rw [hS, Finset.mem_image] at hx
  obtain ⟨k, hk, rfl⟩ := hx
  exact hagree k hk

end QOU.BraidKnot.KeystoneHabiroRootFamily
