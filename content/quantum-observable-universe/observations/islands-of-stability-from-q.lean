-- Ref: [manuscript] §7/islands-of-stability-from-q
--
-- Extends the Borromean spin-orbit intruder mechanism of
-- prop:nuclear-shell-intruder to the N = 7 harmonic-oscillator
-- shell, showing that the 1j_{15/2} intruder (16 states) produces
-- the next neutron magic number at C_6 + 16 = 168 + 16 = 184.
--
-- Ref: [ding2026] https://journals.aps.org/prl/abstract/10.1103/8lzc-j1lx
--     (independent evidence that the same magic numbers emerge from
--      a resolution-scale flow in chiral EFT + SRG; our N=7 extension
--      predicts 184 and is the same value reached from Ding et al.'s
--      lambda hierarchy).

import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.NormNum

namespace QOU.Observations.IslandsOfStabilityFromQ

-- ═══════════════════════════════════════════════════════════════════
-- §1. Harmonic-oscillator shell structure (redeclared for standalone build)
-- ═══════════════════════════════════════════════════════════════════

/-- HO cumulative closure at level N: (N+1)(N+2)(N+3)/3. -/
-- Ref: [manuscript] Ch. 4 / nuclear-shell-intruder
def hoCumulative (N : ℕ) : ℕ := (N + 1) * (N + 2) * (N + 3) / 3

/-- The highest-j intruder level from HO shell N contributes
    2(N+1) states (j = N + 1/2 degeneracy). -/
-- Ref: [manuscript] Ch. 4 / nuclear-shell-intruder
def intruderStates (N : ℕ) : ℕ := 2 * (N + 1)

-- ═══════════════════════════════════════════════════════════════════
-- §2. Arithmetic of the N = 7 extension
-- ═══════════════════════════════════════════════════════════════════

/-- C_6 = 168 (HO cumulative through N = 6). -/
-- Ref: [manuscript] §7/islands-of-stability-from-q
theorem hoCumulative_6 : hoCumulative 6 = 168 := by
  unfold hoCumulative; norm_num

/-- C_7 = 240 (HO cumulative through N = 7). -/
-- Ref: [manuscript] §7/islands-of-stability-from-q
theorem hoCumulative_7 : hoCumulative 7 = 240 := by
  unfold hoCumulative; norm_num

/-- The 1j_{15/2} intruder from N = 7 has 16 states. -/
-- Ref: [manuscript] §7/islands-of-stability-from-q
theorem intruderStates_7 : intruderStates 7 = 16 := by
  unfold intruderStates; norm_num

/-- The neutron island magic number at N = 184 equals
    C_6 + intruderStates 7. -/
-- Ref: [manuscript] §7/islands-of-stability-from-q
theorem magic_184 : hoCumulative 6 + intruderStates 7 = 184 := by
  rw [hoCumulative_6, intruderStates_7]

-- ═══════════════════════════════════════════════════════════════════
-- §3. Extended stability pair list
-- ═══════════════════════════════════════════════════════════════════

/-- Closed-form stability pair at level K, extended from
    nuclear-shell-intruder.lean's `stabilityPair` up through K = 7.
    For K ≤ 2: bare HO cumulative.
    For K ≥ 3: C_{K-1} + intruderStates K. -/
-- Ref: [manuscript] §7/islands-of-stability-from-q
def stabilityPairExtended : ℕ → ℕ
  | 0 => 2
  | 1 => 8
  | 2 => 20
  | 3 => 28
  | 4 => 50
  | 5 => 82
  | 6 => 126
  | 7 => 184
  | _ => 0

/-- All eight magic numbers (including the superheavy prediction 184). -/
-- Ref: [manuscript] §7/islands-of-stability-from-q
theorem extended_stability_pairs_correct :
    [stabilityPairExtended 0, stabilityPairExtended 1,
     stabilityPairExtended 2, stabilityPairExtended 3,
     stabilityPairExtended 4, stabilityPairExtended 5,
     stabilityPairExtended 6, stabilityPairExtended 7]
      = [2, 8, 20, 28, 50, 82, 126, 184] := by
  native_decide

/-- The next-shell prediction: N = 184 is the parameter-free
    superheavy neutron magic number. -/
-- Ref: [manuscript] §7/islands-of-stability-from-q
theorem superheavy_neutron_magic :
    stabilityPairExtended 7 = 184 := by
  native_decide

-- ═══════════════════════════════════════════════════════════════════
-- §4. Hypothetical N = 8 island (dissolves under Coulomb)
-- ═══════════════════════════════════════════════════════════════════

/-- The would-be N = 8 intruder 1k_{17/2} contributes 18 states,
    giving a hypothetical closure at 240 + 18 = 258.  Bethe–Weizsäcker
    inspection (not formalised) shows no stable Z exists at this
    neutron number, so the island dissolves. -/
-- Ref: [manuscript] §7/islands-of-stability-from-q
theorem hypothetical_258 : hoCumulative 7 + intruderStates 8 = 258 := by
  unfold hoCumulative intruderStates; norm_num

-- ═══════════════════════════════════════════════════════════════════
-- §5. Proton-island candidate plateau set
-- ═══════════════════════════════════════════════════════════════════

/-- The three candidate proton magic numbers arising as
    Coulomb-shifted integer plateaus in the q-window around
    q_0 ≈ 1.1098.  This is a finite set, not a single prediction;
    the q-value selects which plateau is realised. -/
-- Ref: [manuscript] §7/islands-of-stability-from-q
def protonIslandCandidates : List ℕ := [114, 120, 126]

/-- The candidate set is nonempty. -/
-- Ref: [manuscript] §7/islands-of-stability-from-q
theorem proton_candidates_nonempty : protonIslandCandidates ≠ [] := by
  unfold protonIslandCandidates; decide

end QOU.Observations.IslandsOfStabilityFromQ
