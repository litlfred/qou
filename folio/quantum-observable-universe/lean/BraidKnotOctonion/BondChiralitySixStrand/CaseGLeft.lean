import BraidKnotOctonion.BondChiralitySixStrand.Core

/-!
# Bond chirality on six strands: `(σ₀σ₁⁻¹)³ · σ₃σ₄σ₃ · (σ₂σ₃⁻¹)³`, proton on strands `0–2` (bond `G`, ruled form)

The weight-space columns needed by `F(O₊)` and `F(O₋)` (mulVec chains, one step per letter),
then `S = F(O₊) + F(O₋)` on the full 64-dimensional space and `F(O±)` at `q = 1`.
Setup and conventions: `BondChiralitySixStrand.Core`.
-/

namespace QOU.BraidsAndKnots.BondChiralitySixStrand

open Matrix

variable {R : Type*} [Field R]

set_option linter.unusedVariables false
set_option maxHeartbeats 1000000

/-- `(σ₀σ₁⁻¹)³ · σ₃σ₄σ₃ · (σ₂σ₃⁻¹)³`, proton on strands `0–2` (bond `G`, ruled form). -/
def wGL : List Letter := [(0, false), (1, true), (0, false), (1, true), (0, false), (1, true), (3, false), (4, false), (3, false), (2, false), (3, true), (2, false), (3, true), (2, false), (3, true)]

def cGL_5_0_v0 (q : R) : Fin 6 → R := ![((1) / q), 0, 0, 0, 0, 0]
theorem cGL_5_0_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (Pi.single 0 1) = cGL_5_0_v0 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGL_5_0_v0; stepTac
def cGL_5_0_v1 (q : R) : Fin 6 → R := ![(1), 0, 0, 0, 0, 0]
theorem cGL_5_0_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGL_5_0_v0 q) = cGL_5_0_v1 q := by
  rw [bridge5_2]; unfold cGL_5_0_v0 cGL_5_0_v1; stepTac
def cGL_5_0_v2 (q : R) : Fin 6 → R := ![((1) / q), 0, 0, 0, 0, 0]
theorem cGL_5_0_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGL_5_0_v1 q) = cGL_5_0_v2 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGL_5_0_v1 cGL_5_0_v2; stepTac
def cGL_5_0_v3 (q : R) : Fin 6 → R := ![(1), 0, 0, 0, 0, 0]
theorem cGL_5_0_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGL_5_0_v2 q) = cGL_5_0_v3 q := by
  rw [bridge5_2]; unfold cGL_5_0_v2 cGL_5_0_v3; stepTac
def cGL_5_0_v4 (q : R) : Fin 6 → R := ![((1) / q), 0, 0, 0, 0, 0]
theorem cGL_5_0_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGL_5_0_v3 q) = cGL_5_0_v4 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGL_5_0_v3 cGL_5_0_v4; stepTac
def cGL_5_0_v5 (q : R) : Fin 6 → R := ![(1), 0, 0, 0, 0, 0]
theorem cGL_5_0_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGL_5_0_v4 q) = cGL_5_0_v5 q := by
  rw [bridge5_2]; unfold cGL_5_0_v4 cGL_5_0_v5; stepTac
def cGL_5_0_v6 (q : R) : Fin 6 → R := ![(q), 0, 0, 0, 0, 0]
theorem cGL_5_0_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGL_5_0_v5 q) = cGL_5_0_v6 q := by
  rw [bridge5_3]; unfold cGL_5_0_v5 cGL_5_0_v6; stepTac
def cGL_5_0_v7 (q : R) : Fin 6 → R := ![(q^2), 0, 0, 0, 0, 0]
theorem cGL_5_0_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, false)).mulVec (cGL_5_0_v6 q) = cGL_5_0_v7 q := by
  rw [bridge5_4]; unfold cGL_5_0_v6 cGL_5_0_v7; stepTac
def cGL_5_0_v8 (q : R) : Fin 6 → R := ![(q^3), 0, 0, 0, 0, 0]
theorem cGL_5_0_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGL_5_0_v7 q) = cGL_5_0_v8 q := by
  rw [bridge5_3]; unfold cGL_5_0_v7 cGL_5_0_v8; stepTac
def cGL_5_0_v9 (q : R) : Fin 6 → R := ![(q^2), 0, 0, 0, 0, 0]
theorem cGL_5_0_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, true)).mulVec (cGL_5_0_v8 q) = cGL_5_0_v9 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_1]; unfold cGL_5_0_v8 cGL_5_0_v9; stepTac
def cGL_5_0_v10 (q : R) : Fin 6 → R := ![(q^3 - q), (q^2), 0, 0, 0, 0]
theorem cGL_5_0_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGL_5_0_v9 q) = cGL_5_0_v10 q := by
  rw [bridge5_0]; unfold cGL_5_0_v9 cGL_5_0_v10; stepTac
def cGL_5_0_v11 (q : R) : Fin 6 → R := ![(q^2 - 1), 0, (q^2), 0, 0, 0]
theorem cGL_5_0_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, true)).mulVec (cGL_5_0_v10 q) = cGL_5_0_v11 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_1]; unfold cGL_5_0_v10 cGL_5_0_v11; stepTac
def cGL_5_0_v12 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / q), (q^2 - 1), (q^3), 0, 0, 0]
theorem cGL_5_0_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGL_5_0_v11 q) = cGL_5_0_v12 q := by
  rw [bridge5_0]; unfold cGL_5_0_v11 cGL_5_0_v12; stepTac
def cGL_5_0_v13 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / q^2), (q^3), (-q^4 + 2*q^2 - 1), 0, 0, 0]
theorem cGL_5_0_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, true)).mulVec (cGL_5_0_v12 q) = cGL_5_0_v13 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_1]; unfold cGL_5_0_v12 cGL_5_0_v13; stepTac
def cGL_5_0_v14 (q : R) : Fin 6 → R := ![((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^3), ((q^4 - 2*q^2 + 1) / q^2), (-q^5 + 2*q^3 - q), 0, 0, 0]
theorem cGL_5_0_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGL_5_0_v13 q) = cGL_5_0_v14 q := by
  rw [bridge5_0]; unfold cGL_5_0_v13 cGL_5_0_v14; stepTac
theorem cGL_5_0_col (q : R) (hq : q ≠ 0) :
    (wordW q idx5 wGL).mulVec (Pi.single 0 1) = cGL_5_0_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_5_0_v0_step q hq, cGL_5_0_v1_step q hq, cGL_5_0_v2_step q hq, cGL_5_0_v3_step q hq, cGL_5_0_v4_step q hq, cGL_5_0_v5_step q hq, cGL_5_0_v6_step q hq, cGL_5_0_v7_step q hq, cGL_5_0_v8_step q hq, cGL_5_0_v9_step q hq, cGL_5_0_v10_step q hq, cGL_5_0_v11_step q hq, cGL_5_0_v12_step q hq, cGL_5_0_v13_step q hq, cGL_5_0_v14_step q hq]
theorem cGL_5_0_entry (q : R) (hq : q ≠ 0) :
    wordW q idx5 wGL 0 0 = ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx5 wGL) 0 0, cGL_5_0_col q hq]; simp [cGL_5_0_v14]

def cGL_5_1_v0 (q : R) : Fin 6 → R := ![0, ((1) / q), 0, 0, 0, 0]
theorem cGL_5_1_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (Pi.single 1 1) = cGL_5_1_v0 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGL_5_1_v0; stepTac
def cGL_5_1_v1 (q : R) : Fin 6 → R := ![0, (1), 0, 0, 0, 0]
theorem cGL_5_1_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGL_5_1_v0 q) = cGL_5_1_v1 q := by
  rw [bridge5_2]; unfold cGL_5_1_v0 cGL_5_1_v1; stepTac
def cGL_5_1_v2 (q : R) : Fin 6 → R := ![0, ((1) / q), 0, 0, 0, 0]
theorem cGL_5_1_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGL_5_1_v1 q) = cGL_5_1_v2 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGL_5_1_v1 cGL_5_1_v2; stepTac
def cGL_5_1_v3 (q : R) : Fin 6 → R := ![0, (1), 0, 0, 0, 0]
theorem cGL_5_1_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGL_5_1_v2 q) = cGL_5_1_v3 q := by
  rw [bridge5_2]; unfold cGL_5_1_v2 cGL_5_1_v3; stepTac
def cGL_5_1_v4 (q : R) : Fin 6 → R := ![0, ((1) / q), 0, 0, 0, 0]
theorem cGL_5_1_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGL_5_1_v3 q) = cGL_5_1_v4 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGL_5_1_v3 cGL_5_1_v4; stepTac
def cGL_5_1_v5 (q : R) : Fin 6 → R := ![0, (1), 0, 0, 0, 0]
theorem cGL_5_1_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGL_5_1_v4 q) = cGL_5_1_v5 q := by
  rw [bridge5_2]; unfold cGL_5_1_v4 cGL_5_1_v5; stepTac
def cGL_5_1_v6 (q : R) : Fin 6 → R := ![0, (q), 0, 0, 0, 0]
theorem cGL_5_1_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGL_5_1_v5 q) = cGL_5_1_v6 q := by
  rw [bridge5_3]; unfold cGL_5_1_v5 cGL_5_1_v6; stepTac
def cGL_5_1_v7 (q : R) : Fin 6 → R := ![0, (q^2), 0, 0, 0, 0]
theorem cGL_5_1_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, false)).mulVec (cGL_5_1_v6 q) = cGL_5_1_v7 q := by
  rw [bridge5_4]; unfold cGL_5_1_v6 cGL_5_1_v7; stepTac
def cGL_5_1_v8 (q : R) : Fin 6 → R := ![0, (q^3), 0, 0, 0, 0]
theorem cGL_5_1_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGL_5_1_v7 q) = cGL_5_1_v8 q := by
  rw [bridge5_3]; unfold cGL_5_1_v7 cGL_5_1_v8; stepTac
def cGL_5_1_v9 (q : R) : Fin 6 → R := ![0, 0, (q^3), 0, 0, 0]
theorem cGL_5_1_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, true)).mulVec (cGL_5_1_v8 q) = cGL_5_1_v9 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_1]; unfold cGL_5_1_v8 cGL_5_1_v9; stepTac
def cGL_5_1_v10 (q : R) : Fin 6 → R := ![0, 0, (q^4), 0, 0, 0]
theorem cGL_5_1_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGL_5_1_v9 q) = cGL_5_1_v10 q := by
  rw [bridge5_0]; unfold cGL_5_1_v9 cGL_5_1_v10; stepTac
def cGL_5_1_v11 (q : R) : Fin 6 → R := ![0, (q^4), (-q^5 + q^3), 0, 0, 0]
theorem cGL_5_1_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, true)).mulVec (cGL_5_1_v10 q) = cGL_5_1_v11 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_1]; unfold cGL_5_1_v10 cGL_5_1_v11; stepTac
def cGL_5_1_v12 (q : R) : Fin 6 → R := ![(q^4), 0, (-q^6 + q^4), 0, 0, 0]
theorem cGL_5_1_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGL_5_1_v11 q) = cGL_5_1_v12 q := by
  rw [bridge5_0]; unfold cGL_5_1_v11 cGL_5_1_v12; stepTac
def cGL_5_1_v13 (q : R) : Fin 6 → R := ![(q^3), (-q^6 + q^4), (q^7 - 2*q^5 + q^3), 0, 0, 0]
theorem cGL_5_1_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, true)).mulVec (cGL_5_1_v12 q) = cGL_5_1_v13 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_1]; unfold cGL_5_1_v12 cGL_5_1_v13; stepTac
def cGL_5_1_v14 (q : R) : Fin 6 → R := ![(-q^6 + 2*q^4 - q^2), (q^3), (q^8 - 2*q^6 + q^4), 0, 0, 0]
theorem cGL_5_1_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGL_5_1_v13 q) = cGL_5_1_v14 q := by
  rw [bridge5_0]; unfold cGL_5_1_v13 cGL_5_1_v14; stepTac
theorem cGL_5_1_col (q : R) (hq : q ≠ 0) :
    (wordW q idx5 wGL).mulVec (Pi.single 1 1) = cGL_5_1_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_5_1_v0_step q hq, cGL_5_1_v1_step q hq, cGL_5_1_v2_step q hq, cGL_5_1_v3_step q hq, cGL_5_1_v4_step q hq, cGL_5_1_v5_step q hq, cGL_5_1_v6_step q hq, cGL_5_1_v7_step q hq, cGL_5_1_v8_step q hq, cGL_5_1_v9_step q hq, cGL_5_1_v10_step q hq, cGL_5_1_v11_step q hq, cGL_5_1_v12_step q hq, cGL_5_1_v13_step q hq, cGL_5_1_v14_step q hq]
theorem cGL_5_1_entry (q : R) (hq : q ≠ 0) :
    wordW q idx5 wGL 1 1 = (q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx5 wGL) 1 1, cGL_5_1_col q hq]; simp [cGL_5_1_v14]

def cGL_5_2_v0 (q : R) : Fin 6 → R := ![0, 0, ((1) / q), 0, 0, 0]
theorem cGL_5_2_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (Pi.single 2 1) = cGL_5_2_v0 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGL_5_2_v0; stepTac
def cGL_5_2_v1 (q : R) : Fin 6 → R := ![0, 0, ((q^2 - 1) / q^2), ((1) / q), 0, 0]
theorem cGL_5_2_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGL_5_2_v0 q) = cGL_5_2_v1 q := by
  rw [bridge5_2]; unfold cGL_5_2_v0 cGL_5_2_v1; stepTac
def cGL_5_2_v2 (q : R) : Fin 6 → R := ![0, 0, ((q^2 - 1) / q^3), 0, ((1) / q), 0]
theorem cGL_5_2_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGL_5_2_v1 q) = cGL_5_2_v2 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGL_5_2_v1 cGL_5_2_v2; stepTac
def cGL_5_2_v3 (q : R) : Fin 6 → R := ![0, 0, ((q^4 - 2*q^2 + 1) / q^4), ((q^2 - 1) / q^3), (1), 0]
theorem cGL_5_2_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGL_5_2_v2 q) = cGL_5_2_v3 q := by
  rw [bridge5_2]; unfold cGL_5_2_v2 cGL_5_2_v3; stepTac
def cGL_5_2_v4 (q : R) : Fin 6 → R := ![0, 0, ((q^4 - 2*q^2 + 1) / q^5), (1), ((-q^4 + 2*q^2 - 1) / q^3), 0]
theorem cGL_5_2_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGL_5_2_v3 q) = cGL_5_2_v4 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGL_5_2_v3 cGL_5_2_v4; stepTac
def cGL_5_2_v5 (q : R) : Fin 6 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), ((-q^4 + 2*q^2 - 1) / q^2), 0]
theorem cGL_5_2_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGL_5_2_v4 q) = cGL_5_2_v5 q := by
  rw [bridge5_2]; unfold cGL_5_2_v4 cGL_5_2_v5; stepTac
def cGL_5_2_v6 (q : R) : Fin 6 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), 0]
theorem cGL_5_2_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGL_5_2_v5 q) = cGL_5_2_v6 q := by
  rw [bridge5_3]; unfold cGL_5_2_v5 cGL_5_2_v6; stepTac
def cGL_5_2_v7 (q : R) : Fin 6 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^4), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5)]
theorem cGL_5_2_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, false)).mulVec (cGL_5_2_v6 q) = cGL_5_2_v7 q := by
  rw [bridge5_4]; unfold cGL_5_2_v6 cGL_5_2_v7; stepTac
def cGL_5_2_v8 (q : R) : Fin 6 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^3), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4)]
theorem cGL_5_2_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGL_5_2_v7 q) = cGL_5_2_v8 q := by
  rw [bridge5_3]; unfold cGL_5_2_v7 cGL_5_2_v8; stepTac
def cGL_5_2_v9 (q : R) : Fin 6 → R := ![0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^3), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5)]
theorem cGL_5_2_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, true)).mulVec (cGL_5_2_v8 q) = cGL_5_2_v9 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_1]; unfold cGL_5_2_v8 cGL_5_2_v9; stepTac
def cGL_5_2_v10 (q : R) : Fin 6 → R := ![((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^3), 0, ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^3), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4)]
theorem cGL_5_2_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGL_5_2_v9 q) = cGL_5_2_v10 q := by
  rw [bridge5_0]; unfold cGL_5_2_v9 cGL_5_2_v10; stepTac
def cGL_5_2_v11 (q : R) : Fin 6 → R := ![((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^4), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^3), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5)]
theorem cGL_5_2_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, true)).mulVec (cGL_5_2_v10 q) = cGL_5_2_v11 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_1]; unfold cGL_5_2_v10 cGL_5_2_v11; stepTac
def cGL_5_2_v12 (q : R) : Fin 6 → R := ![((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^5), ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^4), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^3), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4)]
theorem cGL_5_2_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGL_5_2_v11 q) = cGL_5_2_v12 q := by
  rw [bridge5_0]; unfold cGL_5_2_v11 cGL_5_2_v12; stepTac
def cGL_5_2_v13 (q : R) : Fin 6 → R := ![((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^3), ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^4), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5)]
theorem cGL_5_2_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, true)).mulVec (cGL_5_2_v12 q) = cGL_5_2_v13 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_1]; unfold cGL_5_2_v12 cGL_5_2_v13; stepTac
def cGL_5_2_v14 (q : R) : Fin 6 → R := ![((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^7), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^3), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4)]
theorem cGL_5_2_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGL_5_2_v13 q) = cGL_5_2_v14 q := by
  rw [bridge5_0]; unfold cGL_5_2_v13 cGL_5_2_v14; stepTac
theorem cGL_5_2_col (q : R) (hq : q ≠ 0) :
    (wordW q idx5 wGL).mulVec (Pi.single 2 1) = cGL_5_2_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_5_2_v0_step q hq, cGL_5_2_v1_step q hq, cGL_5_2_v2_step q hq, cGL_5_2_v3_step q hq, cGL_5_2_v4_step q hq, cGL_5_2_v5_step q hq, cGL_5_2_v6_step q hq, cGL_5_2_v7_step q hq, cGL_5_2_v8_step q hq, cGL_5_2_v9_step q hq, cGL_5_2_v10_step q hq, cGL_5_2_v11_step q hq, cGL_5_2_v12_step q hq, cGL_5_2_v13_step q hq, cGL_5_2_v14_step q hq]
theorem cGL_5_2_entry (q : R) (hq : q ≠ 0) :
    wordW q idx5 wGL 2 2 = ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx5 wGL) 2 2, cGL_5_2_col q hq]; simp [cGL_5_2_v14]

def cGL_4_3_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_3_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 3 1) = cGL_4_3_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_3_v0; stepTac
def cGL_4_3_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_3_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_3_v0 q) = cGL_4_3_v1 q := by
  rw [bridge4_2]; unfold cGL_4_3_v0 cGL_4_3_v1; stepTac
def cGL_4_3_v2 (q : R) : Fin 15 → R := ![0, 0, 0, (q), 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_3_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_3_v1 q) = cGL_4_3_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_3_v1 cGL_4_3_v2; stepTac
def cGL_4_3_v3 (q : R) : Fin 15 → R := ![0, (q), 0, 0, 0, 0, (-q^3 + q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_3_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_3_v2 q) = cGL_4_3_v3 q := by
  rw [bridge4_2]; unfold cGL_4_3_v2 cGL_4_3_v3; stepTac
def cGL_4_3_v4 (q : R) : Fin 15 → R := ![0, (1), 0, (-q^3 + q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_3_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_3_v3 q) = cGL_4_3_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_3_v3 cGL_4_3_v4; stepTac
def cGL_4_3_v5 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q), 0, (1), 0, 0, (q^5 - 2*q^3 + q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_3_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_3_v4 q) = cGL_4_3_v5 q := by
  rw [bridge4_2]; unfold cGL_4_3_v4 cGL_4_3_v5; stepTac
def cGL_4_3_v6 (q : R) : Fin 15 → R := ![0, (-q^4 + 2*q^2 - 1), 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q), 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_3_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_3_v5 q) = cGL_4_3_v6 q := by
  rw [bridge4_3]; unfold cGL_4_3_v5 cGL_4_3_v6; stepTac
def cGL_4_3_v7 (q : R) : Fin 15 → R := ![0, (-q^5 + 2*q^3 - q), 0, (q^6 - 2*q^4 + 2*q^2 - 1), 0, 0, ((q^2 - 1) / q), 0, 0, 0, (1), 0, 0, 0, 0]
theorem cGL_4_3_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_3_v6 q) = cGL_4_3_v7 q := by
  rw [bridge4_4]; unfold cGL_4_3_v6 cGL_4_3_v7; stepTac
def cGL_4_3_v8 (q : R) : Fin 15 → R := ![0, (-q^6 + 2*q^4 - q^2), 0, (q^7 - 3*q^5 + 4*q^3 - 2*q), 0, 0, (q^6 - 2*q^4 + 2*q^2 - 1), 0, 0, 0, (q), 0, 0, 0, 0]
theorem cGL_4_3_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_3_v7 q) = cGL_4_3_v8 q := by
  rw [bridge4_3]; unfold cGL_4_3_v7 cGL_4_3_v8; stepTac
def cGL_4_3_v9 (q : R) : Fin 15 → R := ![(-q^6 + 2*q^4 - q^2), (q^7 - 3*q^5 + 3*q^3 - q), 0, (q^6 - 3*q^4 + 4*q^2 - 2), 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q), 0, 0, 0, (1), 0, 0, 0, 0]
theorem cGL_4_3_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_3_v8 q) = cGL_4_3_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_3_v8 cGL_4_3_v9; stepTac
def cGL_4_3_v10 (q : R) : Fin 15 → R := ![(-q^7 + 2*q^5 - q^3), (q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1), (q^7 - 3*q^5 + 3*q^3 - q), ((q^8 - 4*q^6 + 7*q^4 - 6*q^2 + 2) / q), (q^6 - 3*q^4 + 4*q^2 - 2), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), ((q^6 - 2*q^4 + 2*q^2 - 1) / q), 0, 0, ((q^2 - 1) / q), (1), 0, 0, 0]
theorem cGL_4_3_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_3_v9 q) = cGL_4_3_v10 q := by
  rw [bridge4_0]; unfold cGL_4_3_v9 cGL_4_3_v10; stepTac
def cGL_4_3_v11 (q : R) : Fin 15 → R := ![(q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q), (q^6 - 3*q^4 + 3*q^2 - 1), ((q^8 - 4*q^6 + 7*q^4 - 6*q^2 + 2) / q^2), 0, (q^6 - 3*q^4 + 4*q^2 - 2), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q), 0, ((q^2 - 1) / q^2), 0, (1), 0, 0]
theorem cGL_4_3_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_3_v10 q) = cGL_4_3_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_3_v10 cGL_4_3_v11; stepTac
def cGL_4_3_v12 (q : R) : Fin 15 → R := ![(q^9 - 4*q^7 + 6*q^5 - 4*q^3 + q), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^2), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q), ((q^10 - 5*q^8 + 11*q^6 - 13*q^4 + 8*q^2 - 2) / q^3), ((q^8 - 4*q^6 + 7*q^4 - 6*q^2 + 2) / q^2), (q^7 - 3*q^5 + 4*q^3 - 2*q), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), (q^6 - 2*q^4 + 2*q^2 - 1), 0, ((q^4 - 2*q^2 + 1) / q^3), ((q^2 - 1) / q^2), (q), 0, 0]
theorem cGL_4_3_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_3_v11 q) = cGL_4_3_v12 q := by
  rw [bridge4_0]; unfold cGL_4_3_v11 cGL_4_3_v12; stepTac
def cGL_4_3_v13 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^2), ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^3), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^2), ((q^10 - 5*q^8 + 11*q^6 - 13*q^4 + 8*q^2 - 2) / q^4), (q^7 - 3*q^5 + 4*q^3 - 2*q), ((-q^10 + 5*q^8 - 11*q^6 + 13*q^4 - 8*q^2 + 2) / q^2), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), (q^6 - 2*q^4 + 2*q^2 - 1), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^3), 0, ((q^4 - 2*q^2 + 1) / q^4), (q), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0]
theorem cGL_4_3_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_3_v12 q) = cGL_4_3_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_3_v12 cGL_4_3_v13; stepTac
def cGL_4_3_v14 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q), ((q^16 - 6*q^14 + 16*q^12 - 27*q^10 + 32*q^8 - 27*q^6 + 16*q^4 - 6*q^2 + 1) / q^4), ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^3), ((2*q^12 - 9*q^10 + 20*q^8 - 26*q^6 + 21*q^4 - 10*q^2 + 2) / q^5), ((q^10 - 5*q^8 + 11*q^6 - 13*q^4 + 8*q^2 - 2) / q^4), ((-q^10 + 5*q^8 - 11*q^6 + 13*q^4 - 8*q^2 + 2) / q), ((2*q^12 - 7*q^10 + 13*q^8 - 15*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^2), 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q), 0, 0]
theorem cGL_4_3_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_3_v13 q) = cGL_4_3_v14 q := by
  rw [bridge4_0]; unfold cGL_4_3_v13 cGL_4_3_v14; stepTac
theorem cGL_4_3_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 3 1) = cGL_4_3_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_3_v0_step q hq, cGL_4_3_v1_step q hq, cGL_4_3_v2_step q hq, cGL_4_3_v3_step q hq, cGL_4_3_v4_step q hq, cGL_4_3_v5_step q hq, cGL_4_3_v6_step q hq, cGL_4_3_v7_step q hq, cGL_4_3_v8_step q hq, cGL_4_3_v9_step q hq, cGL_4_3_v10_step q hq, cGL_4_3_v11_step q hq, cGL_4_3_v12_step q hq, cGL_4_3_v13_step q hq, cGL_4_3_v14_step q hq]
theorem cGL_4_3_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 3 3 = ((2*q^12 - 9*q^10 + 20*q^8 - 26*q^6 + 21*q^4 - 10*q^2 + 2) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 3 3, cGL_4_3_col q hq]; simp [cGL_4_3_v14]

def cGL_4_4_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_4_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 4 1) = cGL_4_4_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_4_v0; stepTac
def cGL_4_4_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_4_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_4_v0 q) = cGL_4_4_v1 q := by
  rw [bridge4_2]; unfold cGL_4_4_v0 cGL_4_4_v1; stepTac
def cGL_4_4_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (q), 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_4_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_4_v1 q) = cGL_4_4_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_4_v1 cGL_4_4_v2; stepTac
def cGL_4_4_v3 (q : R) : Fin 15 → R := ![0, 0, (q), 0, 0, 0, 0, (-q^3 + q), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_4_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_4_v2 q) = cGL_4_4_v3 q := by
  rw [bridge4_2]; unfold cGL_4_4_v2 cGL_4_4_v3; stepTac
def cGL_4_4_v4 (q : R) : Fin 15 → R := ![0, 0, (1), 0, (-q^3 + q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_4_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_4_v3 q) = cGL_4_4_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_4_v3 cGL_4_4_v4; stepTac
def cGL_4_4_v5 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, (1), 0, 0, (q^5 - 2*q^3 + q), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_4_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_4_v4 q) = cGL_4_4_v5 q := by
  rw [bridge4_2]; unfold cGL_4_4_v4 cGL_4_4_v5; stepTac
def cGL_4_4_v6 (q : R) : Fin 15 → R := ![0, 0, (-q^4 + 2*q^2 - 1), 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q), 0, 0, (1), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_4_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_4_v5 q) = cGL_4_4_v6 q := by
  rw [bridge4_3]; unfold cGL_4_4_v5 cGL_4_4_v6; stepTac
def cGL_4_4_v7 (q : R) : Fin 15 → R := ![0, 0, (-q^5 + 2*q^3 - q), 0, (q^6 - 2*q^4 + 2*q^2 - 1), 0, 0, ((q^2 - 1) / q), 0, 0, 0, (1), 0, 0, 0]
theorem cGL_4_4_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_4_v6 q) = cGL_4_4_v7 q := by
  rw [bridge4_4]; unfold cGL_4_4_v6 cGL_4_4_v7; stepTac
def cGL_4_4_v8 (q : R) : Fin 15 → R := ![0, 0, (-q^6 + 2*q^4 - q^2), 0, (q^7 - 3*q^5 + 4*q^3 - 2*q), 0, 0, (q^6 - 2*q^4 + 2*q^2 - 1), 0, 0, 0, (q), 0, 0, 0]
theorem cGL_4_4_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_4_v7 q) = cGL_4_4_v8 q := by
  rw [bridge4_3]; unfold cGL_4_4_v7 cGL_4_4_v8; stepTac
def cGL_4_4_v9 (q : R) : Fin 15 → R := ![0, 0, (-q^5 + 2*q^3 - q), 0, 0, (q^7 - 3*q^5 + 4*q^3 - 2*q), 0, 0, (q^6 - 2*q^4 + 2*q^2 - 1), 0, 0, 0, (q), 0, 0]
theorem cGL_4_4_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_4_v8 q) = cGL_4_4_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_4_v8 cGL_4_4_v9; stepTac
def cGL_4_4_v10 (q : R) : Fin 15 → R := ![0, (-q^5 + 2*q^3 - q), 0, 0, 0, (q^8 - 3*q^6 + 4*q^4 - 2*q^2), 0, 0, (q^7 - 2*q^5 + 2*q^3 - q), 0, 0, 0, (q^2), 0, 0]
theorem cGL_4_4_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_4_v9 q) = cGL_4_4_v10 q := by
  rw [bridge4_0]; unfold cGL_4_4_v9 cGL_4_4_v10; stepTac
def cGL_4_4_v11 (q : R) : Fin 15 → R := ![(-q^5 + 2*q^3 - q), (q^6 - 3*q^4 + 3*q^2 - 1), 0, 0, (q^8 - 3*q^6 + 4*q^4 - 2*q^2), (-q^9 + 4*q^7 - 7*q^5 + 6*q^3 - 2*q), 0, (q^7 - 2*q^5 + 2*q^3 - q), (-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1), 0, 0, (q^2), (-q^3 + q), 0, 0]
theorem cGL_4_4_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_4_v10 q) = cGL_4_4_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_4_v10 cGL_4_4_v11; stepTac
def cGL_4_4_v12 (q : R) : Fin 15 → R := ![(-q^6 + 2*q^4 - q^2), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q), (q^6 - 3*q^4 + 3*q^2 - 1), (q^8 - 3*q^6 + 4*q^4 - 2*q^2), 0, (-q^10 + 4*q^8 - 7*q^6 + 6*q^4 - 2*q^2), (q^7 - 2*q^5 + 2*q^3 - q), 0, (-q^9 + 3*q^7 - 4*q^5 + 3*q^3 - q), 0, (q^2), 0, (-q^4 + q^2), 0, 0]
theorem cGL_4_4_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_4_v11 q) = cGL_4_4_v12 q := by
  rw [bridge4_0]; unfold cGL_4_4_v11 cGL_4_4_v12; stepTac
def cGL_4_4_v13 (q : R) : Fin 15 → R := ![((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^2), ((q^6 - 3*q^4 + 3*q^2 - 1) / q), (q^7 - 3*q^5 + 4*q^3 - 2*q), (-q^10 + 4*q^8 - 7*q^6 + 6*q^4 - 2*q^2), (q^11 - 5*q^9 + 11*q^7 - 13*q^5 + 8*q^3 - 2*q), (q^6 - 2*q^4 + 2*q^2 - 1), (-q^9 + 3*q^7 - 4*q^5 + 3*q^3 - q), (q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1), 0, (q), (-q^4 + q^2), (q^5 - 2*q^3 + q), 0, 0]
theorem cGL_4_4_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_4_v12 q) = cGL_4_4_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_4_v12 cGL_4_4_v13; stepTac
def cGL_4_4_v14 (q : R) : Fin 15 → R := ![(q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^3), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^2), (-q^10 + 5*q^8 - 11*q^6 + 13*q^4 - 8*q^2 + 2), (q^7 - 3*q^5 + 4*q^3 - 2*q), (q^12 - 5*q^10 + 11*q^8 - 13*q^6 + 8*q^4 - 2*q^2), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q), (q^6 - 2*q^4 + 2*q^2 - 1), (q^11 - 4*q^9 + 7*q^7 - 7*q^5 + 4*q^3 - q), 0, (-q^4 + 2*q^2 - 1), (q), (q^6 - 2*q^4 + q^2), 0, 0]
theorem cGL_4_4_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_4_v13 q) = cGL_4_4_v14 q := by
  rw [bridge4_0]; unfold cGL_4_4_v13 cGL_4_4_v14; stepTac
theorem cGL_4_4_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 4 1) = cGL_4_4_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_4_v0_step q hq, cGL_4_4_v1_step q hq, cGL_4_4_v2_step q hq, cGL_4_4_v3_step q hq, cGL_4_4_v4_step q hq, cGL_4_4_v5_step q hq, cGL_4_4_v6_step q hq, cGL_4_4_v7_step q hq, cGL_4_4_v8_step q hq, cGL_4_4_v9_step q hq, cGL_4_4_v10_step q hq, cGL_4_4_v11_step q hq, cGL_4_4_v12_step q hq, cGL_4_4_v13_step q hq, cGL_4_4_v14_step q hq]
theorem cGL_4_4_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 4 4 = (q^7 - 3*q^5 + 4*q^3 - 2*q) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 4 4, cGL_4_4_col q hq]; simp [cGL_4_4_v14]

def cGL_4_5_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0]
theorem cGL_4_5_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 5 1) = cGL_4_5_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_5_v0; stepTac
def cGL_4_5_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), (1), 0, 0, 0, 0, 0]
theorem cGL_4_5_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_5_v0 q) = cGL_4_5_v1 q := by
  rw [bridge4_2]; unfold cGL_4_5_v0 cGL_4_5_v1; stepTac
def cGL_4_5_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((1) / q), 0, 0, 0, 0, 0]
theorem cGL_4_5_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_5_v1 q) = cGL_4_5_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_5_v1 cGL_4_5_v2; stepTac
def cGL_4_5_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (q^2 - 1), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0]
theorem cGL_4_5_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_5_v2 q) = cGL_4_5_v3 q := by
  rw [bridge4_2]; unfold cGL_4_5_v2 cGL_4_5_v3; stepTac
def cGL_4_5_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0]
theorem cGL_4_5_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_5_v3 q) = cGL_4_5_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_5_v3 cGL_4_5_v4; stepTac
def cGL_4_5_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, 0, 0]
theorem cGL_4_5_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_5_v4 q) = cGL_4_5_v5 q := by
  rw [bridge4_2]; unfold cGL_4_5_v4 cGL_4_5_v5; stepTac
def cGL_4_5_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^5), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, 0, 0]
theorem cGL_4_5_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_5_v5 q) = cGL_4_5_v6 q := by
  rw [bridge4_3]; unfold cGL_4_5_v5 cGL_4_5_v6; stepTac
def cGL_4_5_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^4), 0, 0, ((-q^8 + 4*q^6 - 5*q^4 + 3*q^2 - 1) / q^3), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0]
theorem cGL_4_5_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_5_v6 q) = cGL_4_5_v7 q := by
  rw [bridge4_4]; unfold cGL_4_5_v6 cGL_4_5_v7; stepTac
def cGL_4_5_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^10 + 5*q^8 - 8*q^6 + 7*q^4 - 4*q^2 + 1) / q^5), 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3)]
theorem cGL_4_5_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_5_v7 q) = cGL_4_5_v8 q := by
  rw [bridge4_3]; unfold cGL_4_5_v7 cGL_4_5_v8; stepTac
def cGL_4_5_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^10 + 5*q^8 - 8*q^6 + 7*q^4 - 4*q^2 + 1) / q^5), ((q^12 - 6*q^10 + 13*q^8 - 15*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^4), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^2), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4)]
theorem cGL_4_5_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_5_v8 q) = cGL_4_5_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_5_v8 cGL_4_5_v9; stepTac
def cGL_4_5_v10 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^10 + 5*q^8 - 8*q^6 + 7*q^4 - 4*q^2 + 1) / q^5), 0, ((q^12 - 6*q^10 + 13*q^8 - 15*q^6 + 11*q^4 - 5*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 2*q^2 - 1) / q^4), 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), 0, ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3)]
theorem cGL_4_5_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_5_v9 q) = cGL_4_5_v10 q := by
  rw [bridge4_0]; unfold cGL_4_5_v9 cGL_4_5_v10; stepTac
def cGL_4_5_v11 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^10 + 5*q^8 - 8*q^6 + 7*q^4 - 4*q^2 + 1) / q^6), ((q^12 - 6*q^10 + 13*q^8 - 15*q^6 + 11*q^4 - 5*q^2 + 1) / q^5), ((-q^14 + 7*q^12 - 19*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^6), ((q^6 - 2*q^4 + 2*q^2 - 1) / q^5), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^2), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4)]
theorem cGL_4_5_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_5_v10 q) = cGL_4_5_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_5_v10 cGL_4_5_v11; stepTac
def cGL_4_5_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^14 - 7*q^12 + 19*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^7), ((-q^10 + 5*q^8 - 8*q^6 + 7*q^4 - 4*q^2 + 1) / q^6), ((-q^14 + 7*q^12 - 19*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^5), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^6), ((q^6 - 2*q^4 + 2*q^2 - 1) / q^5), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^3), ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3)]
theorem cGL_4_5_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_5_v11 q) = cGL_4_5_v12 q := by
  rw [bridge4_0]; unfold cGL_4_5_v11 cGL_4_5_v12; stepTac
def cGL_4_5_v13 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^14 - 7*q^12 + 19*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^8), ((-q^14 + 7*q^12 - 19*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^5), ((q^16 - 8*q^14 + 26*q^12 - 48*q^10 + 59*q^8 - 50*q^6 + 29*q^4 - 11*q^2 + 2) / q^6), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^7), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 13*q^4 + 7*q^2 - 2) / q^5), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^4), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q), ((q^12 - 6*q^10 + 14*q^8 - 18*q^6 + 15*q^4 - 7*q^2 + 2) / q^2), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4)]
theorem cGL_4_5_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_5_v12 q) = cGL_4_5_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_5_v12 cGL_4_5_v13; stepTac
def cGL_4_5_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^18 + 8*q^16 - 27*q^14 + 54*q^12 - 73*q^10 + 70*q^8 - 48*q^6 + 23*q^4 - 7*q^2 + 1) / q^9), ((q^14 - 7*q^12 + 19*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^8), ((q^16 - 8*q^14 + 26*q^12 - 48*q^10 + 59*q^8 - 50*q^6 + 29*q^4 - 11*q^2 + 2) / q^5), ((q^14 - 5*q^12 + 12*q^10 - 18*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^8), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^7), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 13*q^4 + 7*q^2 - 2) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^5), ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^4), ((q^12 - 6*q^10 + 14*q^8 - 18*q^6 + 15*q^4 - 7*q^2 + 2) / q), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3)]
theorem cGL_4_5_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_5_v13 q) = cGL_4_5_v14 q := by
  rw [bridge4_0]; unfold cGL_4_5_v13 cGL_4_5_v14; stepTac
theorem cGL_4_5_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 5 1) = cGL_4_5_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_5_v0_step q hq, cGL_4_5_v1_step q hq, cGL_4_5_v2_step q hq, cGL_4_5_v3_step q hq, cGL_4_5_v4_step q hq, cGL_4_5_v5_step q hq, cGL_4_5_v6_step q hq, cGL_4_5_v7_step q hq, cGL_4_5_v8_step q hq, cGL_4_5_v9_step q hq, cGL_4_5_v10_step q hq, cGL_4_5_v11_step q hq, cGL_4_5_v12_step q hq, cGL_4_5_v13_step q hq, cGL_4_5_v14_step q hq]
theorem cGL_4_5_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 5 5 = ((q^16 - 8*q^14 + 26*q^12 - 48*q^10 + 59*q^8 - 50*q^6 + 29*q^4 - 11*q^2 + 2) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 5 5, cGL_4_5_col q hq]; simp [cGL_4_5_v14]

def cGL_4_6_v0 (q : R) : Fin 15 → R := ![0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_6_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 6 1) = cGL_4_6_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_6_v0; stepTac
def cGL_4_6_v1 (q : R) : Fin 15 → R := ![0, (1), 0, 0, 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_6_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_6_v0 q) = cGL_4_6_v1 q := by
  rw [bridge4_2]; unfold cGL_4_6_v0 cGL_4_6_v1; stepTac
def cGL_4_6_v2 (q : R) : Fin 15 → R := ![0, ((1) / q), 0, (-q^2 + 1), 0, 0, ((q^4 - 2*q^2 + 1) / q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_6_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_6_v1 q) = cGL_4_6_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_6_v1 cGL_4_6_v2; stepTac
def cGL_4_6_v3 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((1) / q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_6_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_6_v2 q) = cGL_4_6_v3 q := by
  rw [bridge4_2]; unfold cGL_4_6_v2 cGL_4_6_v3; stepTac
def cGL_4_6_v4 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q^3), 0, (q^4 - 2*q^2 + 1), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 2) / q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_6_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_6_v3 q) = cGL_4_6_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_6_v3 cGL_4_6_v4; stepTac
def cGL_4_6_v5 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_6_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_6_v4 q) = cGL_4_6_v5 q := by
  rw [bridge4_2]; unfold cGL_4_6_v4 cGL_4_6_v5; stepTac
def cGL_4_6_v6 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_6_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_6_v5 q) = cGL_4_6_v6 q := by
  rw [bridge4_3]; unfold cGL_4_6_v5 cGL_4_6_v6; stepTac
def cGL_4_6_v7 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0]
theorem cGL_4_6_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_6_v6 q) = cGL_4_6_v7 q := by
  rw [bridge4_4]; unfold cGL_4_6_v6 cGL_4_6_v7; stepTac
def cGL_4_6_v8 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), 0, ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q^2), 0, 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0]
theorem cGL_4_6_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_6_v7 q) = cGL_4_6_v8 q := by
  rw [bridge4_3]; unfold cGL_4_6_v7 cGL_4_6_v8; stepTac
def cGL_4_6_v9 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^2), 0, ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q^3), 0, 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0]
theorem cGL_4_6_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_6_v8 q) = cGL_4_6_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_6_v8 cGL_4_6_v9; stepTac
def cGL_4_6_v10 (q : R) : Fin 15 → R := ![(q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^3), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^2), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 13*q^4 + 6*q^2 - 1) / q^4), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q^3), 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0]
theorem cGL_4_6_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_6_v9 q) = cGL_4_6_v10 q := by
  rw [bridge4_0]; unfold cGL_4_6_v9 cGL_4_6_v10; stepTac
def cGL_4_6_v11 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^3), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^4), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^3), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 13*q^4 + 6*q^2 - 1) / q^5), 0, ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q^3), ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^6), 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^5), 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0]
theorem cGL_4_6_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_6_v10 q) = cGL_4_6_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_6_v10 cGL_4_6_v11; stepTac
def cGL_4_6_v12 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^2), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^5), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^4), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 19*q^4 - 7*q^2 + 1) / q^6), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 13*q^4 + 6*q^2 - 1) / q^5), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q^2), ((-q^14 + 5*q^12 - 11*q^10 + 16*q^8 - 17*q^6 + 12*q^4 - 5*q^2 + 1) / q^7), ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^5), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0]
theorem cGL_4_6_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_6_v11 q) = cGL_4_6_v12 q := by
  rw [bridge4_0]; unfold cGL_4_6_v11 cGL_4_6_v12; stepTac
def cGL_4_6_v13 (q : R) : Fin 15 → R := ![((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^5), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^6), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^5), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 19*q^4 - 7*q^2 + 1) / q^7), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q^2), ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 19*q^4 + 7*q^2 - 1) / q^5), ((-q^14 + 5*q^12 - 11*q^10 + 16*q^8 - 17*q^6 + 12*q^4 - 5*q^2 + 1) / q^8), ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), ((q^14 - 5*q^12 + 11*q^10 - 16*q^8 + 17*q^6 - 12*q^4 + 5*q^2 - 1) / q^6), 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), ((-q^4 + 2*q^2 - 1) / q^2), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGL_4_6_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_6_v12 q) = cGL_4_6_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_6_v12 cGL_4_6_v13; stepTac
def cGL_4_6_v14 (q : R) : Fin 15 → R := ![((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^4), ((-q^20 + 7*q^18 - 23*q^16 + 49*q^14 - 75*q^12 + 86*q^10 - 75*q^8 + 49*q^6 - 23*q^4 + 7*q^2 - 1) / q^7), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^6), ((-2*q^16 + 11*q^14 - 29*q^12 + 50*q^10 - 59*q^8 + 48*q^6 - 26*q^4 + 8*q^2 - 1) / q^8), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 19*q^4 - 7*q^2 + 1) / q^7), ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 19*q^4 + 7*q^2 - 1) / q^4), ((-2*q^16 + 9*q^14 - 20*q^12 + 32*q^10 - 36*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^9), ((-q^14 + 5*q^12 - 11*q^10 + 16*q^8 - 17*q^6 + 12*q^4 - 5*q^2 + 1) / q^8), ((q^14 - 5*q^12 + 11*q^10 - 16*q^8 + 17*q^6 - 12*q^4 + 5*q^2 - 1) / q^5), 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0]
theorem cGL_4_6_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_6_v13 q) = cGL_4_6_v14 q := by
  rw [bridge4_0]; unfold cGL_4_6_v13 cGL_4_6_v14; stepTac
theorem cGL_4_6_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 6 1) = cGL_4_6_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_6_v0_step q hq, cGL_4_6_v1_step q hq, cGL_4_6_v2_step q hq, cGL_4_6_v3_step q hq, cGL_4_6_v4_step q hq, cGL_4_6_v5_step q hq, cGL_4_6_v6_step q hq, cGL_4_6_v7_step q hq, cGL_4_6_v8_step q hq, cGL_4_6_v9_step q hq, cGL_4_6_v10_step q hq, cGL_4_6_v11_step q hq, cGL_4_6_v12_step q hq, cGL_4_6_v13_step q hq, cGL_4_6_v14_step q hq]
theorem cGL_4_6_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 6 6 = ((-2*q^16 + 9*q^14 - 20*q^12 + 32*q^10 - 36*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^9) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 6 6, cGL_4_6_col q hq]; simp [cGL_4_6_v14]

def cGL_4_7_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_7_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 7 1) = cGL_4_7_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_7_v0; stepTac
def cGL_4_7_v1 (q : R) : Fin 15 → R := ![0, 0, (1), 0, 0, 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_7_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_7_v0 q) = cGL_4_7_v1 q := by
  rw [bridge4_2]; unfold cGL_4_7_v0 cGL_4_7_v1; stepTac
def cGL_4_7_v2 (q : R) : Fin 15 → R := ![0, 0, ((1) / q), 0, (-q^2 + 1), 0, 0, ((q^4 - 2*q^2 + 1) / q), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_7_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_7_v1 q) = cGL_4_7_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_7_v1 cGL_4_7_v2; stepTac
def cGL_4_7_v3 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((1) / q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_7_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_7_v2 q) = cGL_4_7_v3 q := by
  rw [bridge4_2]; unfold cGL_4_7_v2 cGL_4_7_v3; stepTac
def cGL_4_7_v4 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, (q^4 - 2*q^2 + 1), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 2) / q), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_7_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_7_v3 q) = cGL_4_7_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_7_v3 cGL_4_7_v4; stepTac
def cGL_4_7_v5 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_7_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_7_v4 q) = cGL_4_7_v5 q := by
  rw [bridge4_2]; unfold cGL_4_7_v4 cGL_4_7_v5; stepTac
def cGL_4_7_v6 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_7_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_7_v5 q) = cGL_4_7_v6 q := by
  rw [bridge4_3]; unfold cGL_4_7_v5 cGL_4_7_v6; stepTac
def cGL_4_7_v7 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0]
theorem cGL_4_7_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_7_v6 q) = cGL_4_7_v7 q := by
  rw [bridge4_4]; unfold cGL_4_7_v6 cGL_4_7_v7; stepTac
def cGL_4_7_v8 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), 0, ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q^2), 0, 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0]
theorem cGL_4_7_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_7_v7 q) = cGL_4_7_v8 q := by
  rw [bridge4_3]; unfold cGL_4_7_v7 cGL_4_7_v8; stepTac
def cGL_4_7_v9 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q^2), 0, 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0]
theorem cGL_4_7_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_7_v8 q) = cGL_4_7_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_7_v8 cGL_4_7_v9; stepTac
def cGL_4_7_v10 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q), 0, 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^2), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, 0]
theorem cGL_4_7_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_7_v9 q) = cGL_4_7_v10 q := by
  rw [bridge4_0]; unfold cGL_4_7_v9 cGL_4_7_v10; stepTac
def cGL_4_7_v11 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^3), 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q), ((q^12 - 5*q^10 + 11*q^8 - 15*q^6 + 13*q^4 - 6*q^2 + 1) / q^2), 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^2), ((q^12 - 4*q^10 + 7*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^3), 0, 0, ((-q^4 + 2*q^2 - 1) / q), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^2), 0, 0]
theorem cGL_4_7_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_7_v10 q) = cGL_4_7_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_7_v10 cGL_4_7_v11; stepTac
def cGL_4_7_v12 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^3), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q), 0, ((q^12 - 5*q^10 + 11*q^8 - 15*q^6 + 13*q^4 - 6*q^2 + 1) / q), ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^2), 0, ((q^12 - 4*q^10 + 7*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^2), 0, ((-q^4 + 2*q^2 - 1) / q), 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q), 0, 0]
theorem cGL_4_7_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_7_v11 q) = cGL_4_7_v12 q := by
  rw [bridge4_0]; unfold cGL_4_7_v11 cGL_4_7_v12; stepTac
def cGL_4_7_v13 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^5), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q^2), ((q^12 - 5*q^10 + 11*q^8 - 15*q^6 + 13*q^4 - 6*q^2 + 1) / q), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 19*q^4 - 7*q^2 + 1) / q^2), ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), ((q^12 - 4*q^10 + 7*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^2), ((-q^14 + 5*q^12 - 11*q^10 + 16*q^8 - 17*q^6 + 12*q^4 - 5*q^2 + 1) / q^3), 0, ((-q^4 + 2*q^2 - 1) / q^2), ((q^6 - 3*q^4 + 3*q^2 - 1) / q), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^2), 0, 0]
theorem cGL_4_7_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_7_v12 q) = cGL_4_7_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_7_v12 cGL_4_7_v13; stepTac
def cGL_4_7_v14 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^3), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^5), ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 19*q^4 + 7*q^2 - 1) / q^3), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 5*q^2 + 1) / q^2), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 19*q^4 - 7*q^2 + 1) / q), ((q^14 - 5*q^12 + 11*q^10 - 16*q^8 + 17*q^6 - 12*q^4 + 5*q^2 - 1) / q^4), ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), ((-q^14 + 5*q^12 - 11*q^10 + 16*q^8 - 17*q^6 + 12*q^4 - 5*q^2 + 1) / q^2), 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q), 0, 0]
theorem cGL_4_7_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_7_v13 q) = cGL_4_7_v14 q := by
  rw [bridge4_0]; unfold cGL_4_7_v13 cGL_4_7_v14; stepTac
theorem cGL_4_7_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 7 1) = cGL_4_7_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_7_v0_step q hq, cGL_4_7_v1_step q hq, cGL_4_7_v2_step q hq, cGL_4_7_v3_step q hq, cGL_4_7_v4_step q hq, cGL_4_7_v5_step q hq, cGL_4_7_v6_step q hq, cGL_4_7_v7_step q hq, cGL_4_7_v8_step q hq, cGL_4_7_v9_step q hq, cGL_4_7_v10_step q hq, cGL_4_7_v11_step q hq, cGL_4_7_v12_step q hq, cGL_4_7_v13_step q hq, cGL_4_7_v14_step q hq]
theorem cGL_4_7_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 7 7 = ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 7 7, cGL_4_7_col q hq]; simp [cGL_4_7_v14]

def cGL_4_8_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0, 0, 0]
theorem cGL_4_8_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 8 1) = cGL_4_8_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_8_v0; stepTac
def cGL_4_8_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((-q^2 + 1) / q), 0, 0, 0, 0, 0]
theorem cGL_4_8_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_8_v0 q) = cGL_4_8_v1 q := by
  rw [bridge4_2]; unfold cGL_4_8_v0 cGL_4_8_v1; stepTac
def cGL_4_8_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), ((-q^2 + 1) / q^2), 0, 0, 0, 0, 0]
theorem cGL_4_8_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_8_v1 q) = cGL_4_8_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_8_v1 cGL_4_8_v2; stepTac
def cGL_4_8_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0, 0, 0]
theorem cGL_4_8_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_8_v2 q) = cGL_4_8_v3 q := by
  rw [bridge4_2]; unfold cGL_4_8_v2 cGL_4_8_v3; stepTac
def cGL_4_8_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, 0, 0]
theorem cGL_4_8_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_8_v3 q) = cGL_4_8_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_8_v3 cGL_4_8_v4; stepTac
def cGL_4_8_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0, 0, 0, 0]
theorem cGL_4_8_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_8_v4 q) = cGL_4_8_v5 q := by
  rw [bridge4_2]; unfold cGL_4_8_v4 cGL_4_8_v5; stepTac
def cGL_4_8_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0, 0, 0, 0]
theorem cGL_4_8_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_8_v5 q) = cGL_4_8_v6 q := by
  rw [bridge4_3]; unfold cGL_4_8_v5 cGL_4_8_v6; stepTac
def cGL_4_8_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), 0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0]
theorem cGL_4_8_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_8_v6 q) = cGL_4_8_v7 q := by
  rw [bridge4_4]; unfold cGL_4_8_v6 cGL_4_8_v7; stepTac
def cGL_4_8_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4)]
theorem cGL_4_8_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_8_v7 q) = cGL_4_8_v8 q := by
  rw [bridge4_3]; unfold cGL_4_8_v7 cGL_4_8_v8; stepTac
def cGL_4_8_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), ((-q^14 + 5*q^12 - 13*q^10 + 21*q^8 - 22*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^3), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5)]
theorem cGL_4_8_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_8_v8 q) = cGL_4_8_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_8_v8 cGL_4_8_v9; stepTac
def cGL_4_8_v10 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), 0, ((-q^14 + 5*q^12 - 13*q^10 + 21*q^8 - 22*q^6 + 15*q^4 - 6*q^2 + 1) / q^6), ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), 0, ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^2), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4)]
theorem cGL_4_8_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_8_v9 q) = cGL_4_8_v10 q := by
  rw [bridge4_0]; unfold cGL_4_8_v9 cGL_4_8_v10; stepTac
def cGL_4_8_v11 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((-q^14 + 5*q^12 - 13*q^10 + 21*q^8 - 22*q^6 + 15*q^4 - 6*q^2 + 1) / q^6), ((q^16 - 6*q^14 + 18*q^12 - 34*q^10 + 43*q^8 - 37*q^6 + 21*q^4 - 7*q^2 + 1) / q^7), ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^2), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^3), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5)]
theorem cGL_4_8_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_8_v10 q) = cGL_4_8_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_8_v10 cGL_4_8_v11; stepTac
def cGL_4_8_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^16 + 6*q^14 - 18*q^12 + 34*q^10 - 43*q^8 + 37*q^6 - 21*q^4 + 7*q^2 - 1) / q^8), ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((q^16 - 6*q^14 + 18*q^12 - 34*q^10 + 43*q^8 - 37*q^6 + 21*q^4 - 7*q^2 + 1) / q^6), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^2), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4)]
theorem cGL_4_8_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_8_v11 q) = cGL_4_8_v12 q := by
  rw [bridge4_0]; unfold cGL_4_8_v11 cGL_4_8_v12; stepTac
def cGL_4_8_v13 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^16 + 6*q^14 - 18*q^12 + 34*q^10 - 43*q^8 + 37*q^6 - 21*q^4 + 7*q^2 - 1) / q^9), ((q^16 - 6*q^14 + 18*q^12 - 34*q^10 + 43*q^8 - 37*q^6 + 21*q^4 - 7*q^2 + 1) / q^6), ((-q^18 + 7*q^16 - 24*q^14 + 53*q^12 - 81*q^10 + 89*q^8 - 70*q^6 + 38*q^4 - 13*q^2 + 2) / q^7), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^6), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^2), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q^3), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5)]
theorem cGL_4_8_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_8_v12 q) = cGL_4_8_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_8_v12 cGL_4_8_v13; stepTac
def cGL_4_8_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^20 - 7*q^18 + 25*q^16 - 58*q^14 + 95*q^12 - 114*q^10 + 101*q^8 - 65*q^6 + 29*q^4 - 8*q^2 + 1) / q^10), ((-q^16 + 6*q^14 - 18*q^12 + 34*q^10 - 43*q^8 + 37*q^6 - 21*q^4 + 7*q^2 - 1) / q^9), ((-q^18 + 7*q^16 - 24*q^14 + 53*q^12 - 81*q^10 + 89*q^8 - 70*q^6 + 38*q^4 - 13*q^2 + 2) / q^6), ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^9), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^5), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q^2), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4)]
theorem cGL_4_8_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_8_v13 q) = cGL_4_8_v14 q := by
  rw [bridge4_0]; unfold cGL_4_8_v13 cGL_4_8_v14; stepTac
theorem cGL_4_8_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 8 1) = cGL_4_8_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_8_v0_step q hq, cGL_4_8_v1_step q hq, cGL_4_8_v2_step q hq, cGL_4_8_v3_step q hq, cGL_4_8_v4_step q hq, cGL_4_8_v5_step q hq, cGL_4_8_v6_step q hq, cGL_4_8_v7_step q hq, cGL_4_8_v8_step q hq, cGL_4_8_v9_step q hq, cGL_4_8_v10_step q hq, cGL_4_8_v11_step q hq, cGL_4_8_v12_step q hq, cGL_4_8_v13_step q hq, cGL_4_8_v14_step q hq]
theorem cGL_4_8_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 8 8 = ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 8 8, cGL_4_8_col q hq]; simp [cGL_4_8_v14]

def cGL_4_10_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0]
theorem cGL_4_10_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 10 1) = cGL_4_10_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_10_v0; stepTac
def cGL_4_10_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0]
theorem cGL_4_10_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_10_v0 q) = cGL_4_10_v1 q := by
  rw [bridge4_2]; unfold cGL_4_10_v0 cGL_4_10_v1; stepTac
def cGL_4_10_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0]
theorem cGL_4_10_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_10_v1 q) = cGL_4_10_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_10_v1 cGL_4_10_v2; stepTac
def cGL_4_10_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0]
theorem cGL_4_10_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_10_v2 q) = cGL_4_10_v3 q := by
  rw [bridge4_2]; unfold cGL_4_10_v2 cGL_4_10_v3; stepTac
def cGL_4_10_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0]
theorem cGL_4_10_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_10_v3 q) = cGL_4_10_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_10_v3 cGL_4_10_v4; stepTac
def cGL_4_10_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0]
theorem cGL_4_10_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_10_v4 q) = cGL_4_10_v5 q := by
  rw [bridge4_2]; unfold cGL_4_10_v4 cGL_4_10_v5; stepTac
def cGL_4_10_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (q), 0, 0, 0, 0]
theorem cGL_4_10_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_10_v5 q) = cGL_4_10_v6 q := by
  rw [bridge4_3]; unfold cGL_4_10_v5 cGL_4_10_v6; stepTac
def cGL_4_10_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_10_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_10_v6 q) = cGL_4_10_v7 q := by
  rw [bridge4_4]; unfold cGL_4_10_v6 cGL_4_10_v7; stepTac
def cGL_4_10_v8 (q : R) : Fin 15 → R := ![0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_10_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_10_v7 q) = cGL_4_10_v8 q := by
  rw [bridge4_3]; unfold cGL_4_10_v7 cGL_4_10_v8; stepTac
def cGL_4_10_v9 (q : R) : Fin 15 → R := ![0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_10_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_10_v8 q) = cGL_4_10_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_10_v8 cGL_4_10_v9; stepTac
def cGL_4_10_v10 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^2 - 1) / q), (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_10_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_10_v9 q) = cGL_4_10_v10 q := by
  rw [bridge4_0]; unfold cGL_4_10_v9 cGL_4_10_v10; stepTac
def cGL_4_10_v11 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^2 - 1) / q^2), 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_10_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_10_v10 q) = cGL_4_10_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_10_v10 cGL_4_10_v11; stepTac
def cGL_4_10_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^4 - 2*q^2 + 1) / q^3), ((q^2 - 1) / q^2), (q), 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_10_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_10_v11 q) = cGL_4_10_v12 q := by
  rw [bridge4_0]; unfold cGL_4_10_v11 cGL_4_10_v12; stepTac
def cGL_4_10_v13 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), (q), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_10_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_10_v12 q) = cGL_4_10_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_10_v12 cGL_4_10_v13; stepTac
def cGL_4_10_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_10_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_10_v13 q) = cGL_4_10_v14 q := by
  rw [bridge4_0]; unfold cGL_4_10_v13 cGL_4_10_v14; stepTac
theorem cGL_4_10_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 10 1) = cGL_4_10_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_10_v0_step q hq, cGL_4_10_v1_step q hq, cGL_4_10_v2_step q hq, cGL_4_10_v3_step q hq, cGL_4_10_v4_step q hq, cGL_4_10_v5_step q hq, cGL_4_10_v6_step q hq, cGL_4_10_v7_step q hq, cGL_4_10_v8_step q hq, cGL_4_10_v9_step q hq, cGL_4_10_v10_step q hq, cGL_4_10_v11_step q hq, cGL_4_10_v12_step q hq, cGL_4_10_v13_step q hq, cGL_4_10_v14_step q hq]
theorem cGL_4_10_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 10 10 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 10 10, cGL_4_10_col q hq]; simp [cGL_4_10_v14]

def cGL_4_11_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0]
theorem cGL_4_11_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 11 1) = cGL_4_11_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_11_v0; stepTac
def cGL_4_11_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0]
theorem cGL_4_11_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_11_v0 q) = cGL_4_11_v1 q := by
  rw [bridge4_2]; unfold cGL_4_11_v0 cGL_4_11_v1; stepTac
def cGL_4_11_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0]
theorem cGL_4_11_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_11_v1 q) = cGL_4_11_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_11_v1 cGL_4_11_v2; stepTac
def cGL_4_11_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0]
theorem cGL_4_11_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_11_v2 q) = cGL_4_11_v3 q := by
  rw [bridge4_2]; unfold cGL_4_11_v2 cGL_4_11_v3; stepTac
def cGL_4_11_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0]
theorem cGL_4_11_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_11_v3 q) = cGL_4_11_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_11_v3 cGL_4_11_v4; stepTac
def cGL_4_11_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0]
theorem cGL_4_11_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_11_v4 q) = cGL_4_11_v5 q := by
  rw [bridge4_2]; unfold cGL_4_11_v4 cGL_4_11_v5; stepTac
def cGL_4_11_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (q), 0, 0, 0]
theorem cGL_4_11_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_11_v5 q) = cGL_4_11_v6 q := by
  rw [bridge4_3]; unfold cGL_4_11_v5 cGL_4_11_v6; stepTac
def cGL_4_11_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_11_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_11_v6 q) = cGL_4_11_v7 q := by
  rw [bridge4_4]; unfold cGL_4_11_v6 cGL_4_11_v7; stepTac
def cGL_4_11_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_11_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_11_v7 q) = cGL_4_11_v8 q := by
  rw [bridge4_3]; unfold cGL_4_11_v7 cGL_4_11_v8; stepTac
def cGL_4_11_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_11_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_11_v8 q) = cGL_4_11_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_11_v8 cGL_4_11_v9; stepTac
def cGL_4_11_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_11_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_11_v9 q) = cGL_4_11_v10 q := by
  rw [bridge4_0]; unfold cGL_4_11_v9 cGL_4_11_v10; stepTac
def cGL_4_11_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (q^2), (-q^3 + q), 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_11_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_11_v10 q) = cGL_4_11_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_11_v10 cGL_4_11_v11; stepTac
def cGL_4_11_v12 (q : R) : Fin 15 → R := ![0, 0, 0, (q^2), 0, (-q^4 + q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_11_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_11_v11 q) = cGL_4_11_v12 q := by
  rw [bridge4_0]; unfold cGL_4_11_v11 cGL_4_11_v12; stepTac
def cGL_4_11_v13 (q : R) : Fin 15 → R := ![0, 0, 0, (q), (-q^4 + q^2), (q^5 - 2*q^3 + q), 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_11_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_11_v12 q) = cGL_4_11_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_11_v12 cGL_4_11_v13; stepTac
def cGL_4_11_v14 (q : R) : Fin 15 → R := ![0, 0, 0, (-q^4 + 2*q^2 - 1), (q), (q^6 - 2*q^4 + q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_11_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_11_v13 q) = cGL_4_11_v14 q := by
  rw [bridge4_0]; unfold cGL_4_11_v13 cGL_4_11_v14; stepTac
theorem cGL_4_11_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 11 1) = cGL_4_11_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_11_v0_step q hq, cGL_4_11_v1_step q hq, cGL_4_11_v2_step q hq, cGL_4_11_v3_step q hq, cGL_4_11_v4_step q hq, cGL_4_11_v5_step q hq, cGL_4_11_v6_step q hq, cGL_4_11_v7_step q hq, cGL_4_11_v8_step q hq, cGL_4_11_v9_step q hq, cGL_4_11_v10_step q hq, cGL_4_11_v11_step q hq, cGL_4_11_v12_step q hq, cGL_4_11_v13_step q hq, cGL_4_11_v14_step q hq]
theorem cGL_4_11_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 11 11 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 11 11, cGL_4_11_col q hq]; simp [cGL_4_11_v14]

def cGL_4_12_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0]
theorem cGL_4_12_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 12 1) = cGL_4_12_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_12_v0; stepTac
def cGL_4_12_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q^2), ((1) / q), 0]
theorem cGL_4_12_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_12_v0 q) = cGL_4_12_v1 q := by
  rw [bridge4_2]; unfold cGL_4_12_v0 cGL_4_12_v1; stepTac
def cGL_4_12_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q^3), 0, ((1) / q)]
theorem cGL_4_12_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_12_v1 q) = cGL_4_12_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_12_v1 cGL_4_12_v2; stepTac
def cGL_4_12_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), ((q^2 - 1) / q^3), (1)]
theorem cGL_4_12_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_12_v2 q) = cGL_4_12_v3 q := by
  rw [bridge4_2]; unfold cGL_4_12_v2 cGL_4_12_v3; stepTac
def cGL_4_12_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), (1), ((-q^4 + 2*q^2 - 1) / q^3)]
theorem cGL_4_12_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_12_v3 q) = cGL_4_12_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_12_v3 cGL_4_12_v4; stepTac
def cGL_4_12_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), ((-q^4 + 2*q^2 - 1) / q^2)]
theorem cGL_4_12_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_12_v4 q) = cGL_4_12_v5 q := by
  rw [bridge4_2]; unfold cGL_4_12_v4 cGL_4_12_v5; stepTac
def cGL_4_12_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5)]
theorem cGL_4_12_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_12_v5 q) = cGL_4_12_v6 q := by
  rw [bridge4_3]; unfold cGL_4_12_v5 cGL_4_12_v6; stepTac
def cGL_4_12_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4)]
theorem cGL_4_12_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_12_v6 q) = cGL_4_12_v7 q := by
  rw [bridge4_4]; unfold cGL_4_12_v6 cGL_4_12_v7; stepTac
def cGL_4_12_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), 0]
theorem cGL_4_12_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_12_v7 q) = cGL_4_12_v8 q := by
  rw [bridge4_3]; unfold cGL_4_12_v7 cGL_4_12_v8; stepTac
def cGL_4_12_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), 0, 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0]
theorem cGL_4_12_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_12_v8 q) = cGL_4_12_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_12_v8 cGL_4_12_v9; stepTac
def cGL_4_12_v10 (q : R) : Fin 15 → R := ![0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), 0, ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), 0, 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), 0]
theorem cGL_4_12_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_12_v9 q) = cGL_4_12_v10 q := by
  rw [bridge4_0]; unfold cGL_4_12_v9 cGL_4_12_v10; stepTac
def cGL_4_12_v11 (q : R) : Fin 15 → R := ![0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), 0, 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0]
theorem cGL_4_12_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_12_v10 q) = cGL_4_12_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_12_v10 cGL_4_12_v11; stepTac
def cGL_4_12_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), 0, 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), 0]
theorem cGL_4_12_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_12_v11 q) = cGL_4_12_v12 q := by
  rw [bridge4_0]; unfold cGL_4_12_v11 cGL_4_12_v12; stepTac
def cGL_4_12_v13 (q : R) : Fin 15 → R := ![0, 0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^6), 0, 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0]
theorem cGL_4_12_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_12_v12 q) = cGL_4_12_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_12_v12 cGL_4_12_v13; stepTac
def cGL_4_12_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^9), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^5), 0, 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), 0]
theorem cGL_4_12_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_12_v13 q) = cGL_4_12_v14 q := by
  rw [bridge4_0]; unfold cGL_4_12_v13 cGL_4_12_v14; stepTac
theorem cGL_4_12_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 12 1) = cGL_4_12_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_12_v0_step q hq, cGL_4_12_v1_step q hq, cGL_4_12_v2_step q hq, cGL_4_12_v3_step q hq, cGL_4_12_v4_step q hq, cGL_4_12_v5_step q hq, cGL_4_12_v6_step q hq, cGL_4_12_v7_step q hq, cGL_4_12_v8_step q hq, cGL_4_12_v9_step q hq, cGL_4_12_v10_step q hq, cGL_4_12_v11_step q hq, cGL_4_12_v12_step q hq, cGL_4_12_v13_step q hq, cGL_4_12_v14_step q hq]
theorem cGL_4_12_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 12 12 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 12 12, cGL_4_12_col q hq]; simp [cGL_4_12_v14]

def cGL_2_12_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0]
theorem cGL_2_12_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 12 1) = cGL_2_12_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_12_v0; stepTac
def cGL_2_12_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0]
theorem cGL_2_12_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_12_v0 q) = cGL_2_12_v1 q := by
  rw [bridge2_2]; unfold cGL_2_12_v0 cGL_2_12_v1; stepTac
def cGL_2_12_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, ((-q^2 + 1) / q^2), 0, 0, 0, 0]
theorem cGL_2_12_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_12_v1 q) = cGL_2_12_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_12_v1 cGL_2_12_v2; stepTac
def cGL_2_12_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (1), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, ((-q^2 + 1) / q^2), 0, 0]
theorem cGL_2_12_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_12_v2 q) = cGL_2_12_v3 q := by
  rw [bridge2_2]; unfold cGL_2_12_v2 cGL_2_12_v3; stepTac
def cGL_2_12_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, ((-q^2 + 1) / q^3), 0, 0]
theorem cGL_2_12_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_12_v3 q) = cGL_2_12_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_12_v3 cGL_2_12_v4; stepTac
def cGL_2_12_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0]
theorem cGL_2_12_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_12_v4 q) = cGL_2_12_v5 q := by
  rw [bridge2_2]; unfold cGL_2_12_v4 cGL_2_12_v5; stepTac
def cGL_2_12_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0]
theorem cGL_2_12_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_12_v5 q) = cGL_2_12_v6 q := by
  rw [bridge2_3]; unfold cGL_2_12_v5 cGL_2_12_v6; stepTac
def cGL_2_12_v7 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^2), 0, 0]
theorem cGL_2_12_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_12_v6 q) = cGL_2_12_v7 q := by
  rw [bridge2_4]; unfold cGL_2_12_v6 cGL_2_12_v7; stepTac
def cGL_2_12_v8 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, 0, 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q), 0, 0]
theorem cGL_2_12_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_12_v7 q) = cGL_2_12_v8 q := by
  rw [bridge2_3]; unfold cGL_2_12_v7 cGL_2_12_v8; stepTac
def cGL_2_12_v9 (q : R) : Fin 15 → R := ![0, 0, ((q^4 - 2*q^2 + 1) / q^4), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^5), 0, 0, ((-q^4 + 2*q^2 - 1) / q), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^2), 0, 0, 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^2), 0, 0]
theorem cGL_2_12_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_12_v8 q) = cGL_2_12_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_12_v8 cGL_2_12_v9; stepTac
def cGL_2_12_v10 (q : R) : Fin 15 → R := ![0, 0, ((q^4 - 2*q^2 + 1) / q^3), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^5), 0, (-q^4 + 2*q^2 - 1), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^2), 0, 0, 0, ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^3), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^2), 0]
theorem cGL_2_12_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_12_v9 q) = cGL_2_12_v10 q := by
  rw [bridge2_0]; unfold cGL_2_12_v9 cGL_2_12_v10; stepTac
def cGL_2_12_v11 (q : R) : Fin 15 → R := ![0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^7), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^4), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0, ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^2)]
theorem cGL_2_12_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_12_v10 q) = cGL_2_12_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_12_v10 cGL_2_12_v11; stepTac
def cGL_2_12_v12 (q : R) : Fin 15 → R := ![0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^8), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^7), 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^2), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^4), 0, 0, 0, ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), ((q^6 - 2*q^4 + 3*q^2 - 1) / q)]
theorem cGL_2_12_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_12_v11 q) = cGL_2_12_v12 q := by
  rw [bridge2_0]; unfold cGL_2_12_v11 cGL_2_12_v12; stepTac
def cGL_2_12_v13 (q : R) : Fin 15 → R := ![0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^8), ((-q^14 + 5*q^12 - 12*q^10 + 19*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^9), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^8), 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^6), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^5), 0, 0, 0, ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^6), ((q^6 - 2*q^4 + 3*q^2 - 1) / q), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^4)]
theorem cGL_2_12_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_12_v12 q) = cGL_2_12_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_12_v12 cGL_2_12_v13; stepTac
def cGL_2_12_v14 (q : R) : Fin 15 → R := ![0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^7), ((-q^16 + 6*q^14 - 16*q^12 + 27*q^10 - 32*q^8 + 27*q^6 - 16*q^4 + 6*q^2 - 1) / q^10), ((-q^14 + 5*q^12 - 12*q^10 + 19*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^9), 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((q^16 - 6*q^14 + 16*q^12 - 27*q^10 + 32*q^8 - 27*q^6 + 16*q^4 - 6*q^2 + 1) / q^7), ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^6), 0, 0, 0, ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^7), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^6), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^3)]
theorem cGL_2_12_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_12_v13 q) = cGL_2_12_v14 q := by
  rw [bridge2_0]; unfold cGL_2_12_v13 cGL_2_12_v14; stepTac
theorem cGL_2_12_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 12 1) = cGL_2_12_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_12_v0_step q hq, cGL_2_12_v1_step q hq, cGL_2_12_v2_step q hq, cGL_2_12_v3_step q hq, cGL_2_12_v4_step q hq, cGL_2_12_v5_step q hq, cGL_2_12_v6_step q hq, cGL_2_12_v7_step q hq, cGL_2_12_v8_step q hq, cGL_2_12_v9_step q hq, cGL_2_12_v10_step q hq, cGL_2_12_v11_step q hq, cGL_2_12_v12_step q hq, cGL_2_12_v13_step q hq, cGL_2_12_v14_step q hq]
theorem cGL_2_12_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 12 12 = ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^7) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 12 12, cGL_2_12_col q hq]; simp [cGL_2_12_v14]

def cGL_2_13_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0]
theorem cGL_2_13_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 13 1) = cGL_2_13_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_13_v0; stepTac
def cGL_2_13_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0]
theorem cGL_2_13_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_13_v0 q) = cGL_2_13_v1 q := by
  rw [bridge2_2]; unfold cGL_2_13_v0 cGL_2_13_v1; stepTac
def cGL_2_13_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, ((-q^2 + 1) / q^2), 0, 0, 0]
theorem cGL_2_13_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_13_v1 q) = cGL_2_13_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_13_v1 cGL_2_13_v2; stepTac
def cGL_2_13_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, ((-q^2 + 1) / q^2), 0]
theorem cGL_2_13_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_13_v2 q) = cGL_2_13_v3 q := by
  rw [bridge2_2]; unfold cGL_2_13_v2 cGL_2_13_v3; stepTac
def cGL_2_13_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, ((-q^2 + 1) / q^3), 0]
theorem cGL_2_13_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_13_v3 q) = cGL_2_13_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_13_v3 cGL_2_13_v4; stepTac
def cGL_2_13_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0]
theorem cGL_2_13_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_13_v4 q) = cGL_2_13_v5 q := by
  rw [bridge2_2]; unfold cGL_2_13_v4 cGL_2_13_v5; stepTac
def cGL_2_13_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0]
theorem cGL_2_13_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_13_v5 q) = cGL_2_13_v6 q := by
  rw [bridge2_3]; unfold cGL_2_13_v5 cGL_2_13_v6; stepTac
def cGL_2_13_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^2), 0]
theorem cGL_2_13_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_13_v6 q) = cGL_2_13_v7 q := by
  rw [bridge2_4]; unfold cGL_2_13_v6 cGL_2_13_v7; stepTac
def cGL_2_13_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, 0, 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q), 0]
theorem cGL_2_13_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_13_v7 q) = cGL_2_13_v8 q := by
  rw [bridge2_3]; unfold cGL_2_13_v7 cGL_2_13_v8; stepTac
def cGL_2_13_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q)]
theorem cGL_2_13_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_13_v8 q) = cGL_2_13_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_13_v8 cGL_2_13_v9; stepTac
def cGL_2_13_v10 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0, 0, (q^6 - 2*q^4 + 3*q^2 - 1)]
theorem cGL_2_13_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_13_v9 q) = cGL_2_13_v10 q := by
  rw [bridge2_0]; unfold cGL_2_13_v9 cGL_2_13_v10; stepTac
def cGL_2_13_v11 (q : R) : Fin 15 → R := ![0, 0, ((q^4 - 2*q^2 + 1) / q^5), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0, 0, 0, (q^6 - 2*q^4 + 3*q^2 - 1), ((-q^8 + 3*q^6 - 5*q^4 + 4*q^2 - 1) / q)]
theorem cGL_2_13_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_13_v10 q) = cGL_2_13_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_13_v10 cGL_2_13_v11; stepTac
def cGL_2_13_v12 (q : R) : Fin 15 → R := ![0, 0, ((q^4 - 2*q^2 + 1) / q^4), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), 0, ((-q^4 + 2*q^2 - 1) / q), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0, (q^6 - 2*q^4 + 3*q^2 - 1), 0, (-q^8 + 3*q^6 - 5*q^4 + 4*q^2 - 1)]
theorem cGL_2_13_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_13_v11 q) = cGL_2_13_v12 q := by
  rw [bridge2_0]; unfold cGL_2_13_v11 cGL_2_13_v12; stepTac
def cGL_2_13_v13 (q : R) : Fin 15 → R := ![0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^8), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^7), 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^5), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q), (-q^8 + 3*q^6 - 5*q^4 + 4*q^2 - 1), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q)]
theorem cGL_2_13_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_13_v12 q) = cGL_2_13_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_13_v12 cGL_2_13_v13; stepTac
def cGL_2_13_v14 (q : R) : Fin 15 → R := ![0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^9), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^8), 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^5), 0, 0, 0, ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^2), ((q^6 - 2*q^4 + 3*q^2 - 1) / q), (q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1)]
theorem cGL_2_13_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_13_v13 q) = cGL_2_13_v14 q := by
  rw [bridge2_0]; unfold cGL_2_13_v13 cGL_2_13_v14; stepTac
theorem cGL_2_13_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 13 1) = cGL_2_13_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_13_v0_step q hq, cGL_2_13_v1_step q hq, cGL_2_13_v2_step q hq, cGL_2_13_v3_step q hq, cGL_2_13_v4_step q hq, cGL_2_13_v5_step q hq, cGL_2_13_v6_step q hq, cGL_2_13_v7_step q hq, cGL_2_13_v8_step q hq, cGL_2_13_v9_step q hq, cGL_2_13_v10_step q hq, cGL_2_13_v11_step q hq, cGL_2_13_v12_step q hq, cGL_2_13_v13_step q hq, cGL_2_13_v14_step q hq]
theorem cGL_2_13_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 13 13 = ((q^6 - 2*q^4 + 3*q^2 - 1) / q) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 13 13, cGL_2_13_col q hq]; simp [cGL_2_13_v14]

def cGL_2_14_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q)]
theorem cGL_2_14_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 14 1) = cGL_2_14_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_14_v0; stepTac
def cGL_2_14_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1)]
theorem cGL_2_14_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_14_v0 q) = cGL_2_14_v1 q := by
  rw [bridge2_2]; unfold cGL_2_14_v0 cGL_2_14_v1; stepTac
def cGL_2_14_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q)]
theorem cGL_2_14_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_14_v1 q) = cGL_2_14_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_14_v1 cGL_2_14_v2; stepTac
def cGL_2_14_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1)]
theorem cGL_2_14_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_14_v2 q) = cGL_2_14_v3 q := by
  rw [bridge2_2]; unfold cGL_2_14_v2 cGL_2_14_v3; stepTac
def cGL_2_14_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q)]
theorem cGL_2_14_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_14_v3 q) = cGL_2_14_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_14_v3 cGL_2_14_v4; stepTac
def cGL_2_14_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1)]
theorem cGL_2_14_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_14_v4 q) = cGL_2_14_v5 q := by
  rw [bridge2_2]; unfold cGL_2_14_v4 cGL_2_14_v5; stepTac
def cGL_2_14_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (q)]
theorem cGL_2_14_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_14_v5 q) = cGL_2_14_v6 q := by
  rw [bridge2_3]; unfold cGL_2_14_v5 cGL_2_14_v6; stepTac
def cGL_2_14_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (q^2)]
theorem cGL_2_14_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_14_v6 q) = cGL_2_14_v7 q := by
  rw [bridge2_4]; unfold cGL_2_14_v6 cGL_2_14_v7; stepTac
def cGL_2_14_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (q^3)]
theorem cGL_2_14_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_14_v7 q) = cGL_2_14_v8 q := by
  rw [bridge2_3]; unfold cGL_2_14_v7 cGL_2_14_v8; stepTac
def cGL_2_14_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (q^3), (-q^4 + q^2)]
theorem cGL_2_14_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_14_v8 q) = cGL_2_14_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_14_v8 cGL_2_14_v9; stepTac
def cGL_2_14_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (q^3), 0, (-q^5 + q^3)]
theorem cGL_2_14_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_14_v9 q) = cGL_2_14_v10 q := by
  rw [bridge2_0]; unfold cGL_2_14_v9 cGL_2_14_v10; stepTac
def cGL_2_14_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (q^2), (-q^5 + q^3), (q^6 - 2*q^4 + q^2)]
theorem cGL_2_14_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_14_v10 q) = cGL_2_14_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_14_v10 cGL_2_14_v11; stepTac
def cGL_2_14_v12 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (-q^5 + 2*q^3 - q), (q^2), (q^7 - 2*q^5 + q^3)]
theorem cGL_2_14_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_14_v11 q) = cGL_2_14_v12 q := by
  rw [bridge2_0]; unfold cGL_2_14_v11 cGL_2_14_v12; stepTac
def cGL_2_14_v13 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (-q^4 + 2*q^2 - 1), (q^7 - 2*q^5 + q^3), (-q^8 + 3*q^6 - 3*q^4 + 2*q^2)]
theorem cGL_2_14_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_14_v12 q) = cGL_2_14_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_14_v12 cGL_2_14_v13; stepTac
def cGL_2_14_v14 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), (-q^4 + 2*q^2 - 1), (-q^9 + 3*q^7 - 3*q^5 + 2*q^3)]
theorem cGL_2_14_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_14_v13 q) = cGL_2_14_v14 q := by
  rw [bridge2_0]; unfold cGL_2_14_v13 cGL_2_14_v14; stepTac
theorem cGL_2_14_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 14 1) = cGL_2_14_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_14_v0_step q hq, cGL_2_14_v1_step q hq, cGL_2_14_v2_step q hq, cGL_2_14_v3_step q hq, cGL_2_14_v4_step q hq, cGL_2_14_v5_step q hq, cGL_2_14_v6_step q hq, cGL_2_14_v7_step q hq, cGL_2_14_v8_step q hq, cGL_2_14_v9_step q hq, cGL_2_14_v10_step q hq, cGL_2_14_v11_step q hq, cGL_2_14_v12_step q hq, cGL_2_14_v13_step q hq, cGL_2_14_v14_step q hq]
theorem cGL_2_14_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 14 14 = (-q^9 + 3*q^7 - 3*q^5 + 2*q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 14 14, cGL_2_14_col q hq]; simp [cGL_2_14_v14]

def cGL_4_0_v0 (q : R) : Fin 15 → R := ![((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 0 1) = cGL_4_0_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_0_v0; stepTac
def cGL_4_0_v1 (q : R) : Fin 15 → R := ![(1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_0_v0 q) = cGL_4_0_v1 q := by
  rw [bridge4_2]; unfold cGL_4_0_v0 cGL_4_0_v1; stepTac
def cGL_4_0_v2 (q : R) : Fin 15 → R := ![((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_0_v1 q) = cGL_4_0_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_0_v1 cGL_4_0_v2; stepTac
def cGL_4_0_v3 (q : R) : Fin 15 → R := ![(1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_0_v2 q) = cGL_4_0_v3 q := by
  rw [bridge4_2]; unfold cGL_4_0_v2 cGL_4_0_v3; stepTac
def cGL_4_0_v4 (q : R) : Fin 15 → R := ![((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_0_v3 q) = cGL_4_0_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_0_v3 cGL_4_0_v4; stepTac
def cGL_4_0_v5 (q : R) : Fin 15 → R := ![(1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_0_v4 q) = cGL_4_0_v5 q := by
  rw [bridge4_2]; unfold cGL_4_0_v4 cGL_4_0_v5; stepTac
def cGL_4_0_v6 (q : R) : Fin 15 → R := ![(q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_0_v5 q) = cGL_4_0_v6 q := by
  rw [bridge4_3]; unfold cGL_4_0_v5 cGL_4_0_v6; stepTac
def cGL_4_0_v7 (q : R) : Fin 15 → R := ![(q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_0_v6 q) = cGL_4_0_v7 q := by
  rw [bridge4_4]; unfold cGL_4_0_v6 cGL_4_0_v7; stepTac
def cGL_4_0_v8 (q : R) : Fin 15 → R := ![(q^3), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_0_v7 q) = cGL_4_0_v8 q := by
  rw [bridge4_3]; unfold cGL_4_0_v7 cGL_4_0_v8; stepTac
def cGL_4_0_v9 (q : R) : Fin 15 → R := ![0, (q^3), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_0_v8 q) = cGL_4_0_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_0_v8 cGL_4_0_v9; stepTac
def cGL_4_0_v10 (q : R) : Fin 15 → R := ![0, (q^4 - q^2), (q^3), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_0_v9 q) = cGL_4_0_v10 q := by
  rw [bridge4_0]; unfold cGL_4_0_v9 cGL_4_0_v10; stepTac
def cGL_4_0_v11 (q : R) : Fin 15 → R := ![(q^4 - q^2), (-q^5 + 2*q^3 - q), (q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_0_v10 q) = cGL_4_0_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_0_v10 cGL_4_0_v11; stepTac
def cGL_4_0_v12 (q : R) : Fin 15 → R := ![(q^5 - q^3), (-q^6 + 3*q^4 - 2*q^2 + 1), (-q^5 + 2*q^3 - q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_0_v11 q) = cGL_4_0_v12 q := by
  rw [bridge4_0]; unfold cGL_4_0_v11 cGL_4_0_v12; stepTac
def cGL_4_0_v13 (q : R) : Fin 15 → R := ![(-q^6 + 3*q^4 - 2*q^2 + 1), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), (-q^4 + 2*q^2 - 1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_0_v12 q) = cGL_4_0_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_0_v12 cGL_4_0_v13; stepTac
def cGL_4_0_v14 (q : R) : Fin 15 → R := ![(-q^7 + 3*q^5 - 2*q^3 + q), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^2), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_0_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_0_v13 q) = cGL_4_0_v14 q := by
  rw [bridge4_0]; unfold cGL_4_0_v13 cGL_4_0_v14; stepTac
theorem cGL_4_0_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 0 1) = cGL_4_0_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_0_v0_step q hq, cGL_4_0_v1_step q hq, cGL_4_0_v2_step q hq, cGL_4_0_v3_step q hq, cGL_4_0_v4_step q hq, cGL_4_0_v5_step q hq, cGL_4_0_v6_step q hq, cGL_4_0_v7_step q hq, cGL_4_0_v8_step q hq, cGL_4_0_v9_step q hq, cGL_4_0_v10_step q hq, cGL_4_0_v11_step q hq, cGL_4_0_v12_step q hq, cGL_4_0_v13_step q hq, cGL_4_0_v14_step q hq]
theorem cGL_4_0_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 0 0 = (-q^7 + 3*q^5 - 2*q^3 + q) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 0 0, cGL_4_0_col q hq]; simp [cGL_4_0_v14]

def cGL_4_1_v0 (q : R) : Fin 15 → R := ![0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_1_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 1 1) = cGL_4_1_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_1_v0; stepTac
def cGL_4_1_v1 (q : R) : Fin 15 → R := ![0, ((q^2 - 1) / q^2), 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_1_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_1_v0 q) = cGL_4_1_v1 q := by
  rw [bridge4_2]; unfold cGL_4_1_v0 cGL_4_1_v1; stepTac
def cGL_4_1_v2 (q : R) : Fin 15 → R := ![0, ((q^2 - 1) / q^3), 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_1_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_1_v1 q) = cGL_4_1_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_1_v1 cGL_4_1_v2; stepTac
def cGL_4_1_v3 (q : R) : Fin 15 → R := ![0, ((q^4 - 2*q^2 + 1) / q^4), 0, ((q^2 - 1) / q^3), 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_1_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_1_v2 q) = cGL_4_1_v3 q := by
  rw [bridge4_2]; unfold cGL_4_1_v2 cGL_4_1_v3; stepTac
def cGL_4_1_v4 (q : R) : Fin 15 → R := ![0, ((q^4 - 2*q^2 + 1) / q^5), 0, (1), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_1_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_1_v3 q) = cGL_4_1_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_1_v3 cGL_4_1_v4; stepTac
def cGL_4_1_v5 (q : R) : Fin 15 → R := ![0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_1_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_1_v4 q) = cGL_4_1_v5 q := by
  rw [bridge4_2]; unfold cGL_4_1_v4 cGL_4_1_v5; stepTac
def cGL_4_1_v6 (q : R) : Fin 15 → R := ![0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_1_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_1_v5 q) = cGL_4_1_v6 q := by
  rw [bridge4_3]; unfold cGL_4_1_v5 cGL_4_1_v6; stepTac
def cGL_4_1_v7 (q : R) : Fin 15 → R := ![0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^4), 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, 0, 0]
theorem cGL_4_1_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_1_v6 q) = cGL_4_1_v7 q := by
  rw [bridge4_4]; unfold cGL_4_1_v6 cGL_4_1_v7; stepTac
def cGL_4_1_v8 (q : R) : Fin 15 → R := ![0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^3), 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), 0, 0, 0, 0]
theorem cGL_4_1_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_1_v7 q) = cGL_4_1_v8 q := by
  rw [bridge4_3]; unfold cGL_4_1_v7 cGL_4_1_v8; stepTac
def cGL_4_1_v9 (q : R) : Fin 15 → R := ![((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^3), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, 0, 0]
theorem cGL_4_1_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_1_v8 q) = cGL_4_1_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_1_v8 cGL_4_1_v9; stepTac
def cGL_4_1_v10 (q : R) : Fin 15 → R := ![((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^2), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^5), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), ((-q^10 + 5*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^7), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), 0, 0, 0]
theorem cGL_4_1_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_1_v9 q) = cGL_4_1_v10 q := by
  rw [bridge4_0]; unfold cGL_4_1_v9 cGL_4_1_v10; stepTac
def cGL_4_1_v11 (q : R) : Fin 15 → R := ![((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^5), ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^6), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((-q^10 + 5*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^8), 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q^7), 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0]
theorem cGL_4_1_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_1_v10 q) = cGL_4_1_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_1_v10 cGL_4_1_v11; stepTac
def cGL_4_1_v12 (q : R) : Fin 15 → R := ![((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^4), ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^7), ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^6), ((-q^12 + 6*q^10 - 15*q^8 + 20*q^6 - 15*q^4 + 6*q^2 - 1) / q^8), ((-q^10 + 5*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^9), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^8), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^8), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^7), ((q^4 - 2*q^2 + 1) / q^4), 0, 0]
theorem cGL_4_1_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_1_v11 q) = cGL_4_1_v12 q := by
  rw [bridge4_0]; unfold cGL_4_1_v11 cGL_4_1_v12; stepTac
def cGL_4_1_v13 (q : R) : Fin 15 → R := ![((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^7), ((-2*q^16 + 9*q^14 - 22*q^12 + 37*q^10 - 44*q^8 + 37*q^6 - 21*q^4 + 7*q^2 - 1) / q^8), ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^7), ((-q^12 + 6*q^10 - 15*q^8 + 20*q^6 - 15*q^4 + 6*q^2 - 1) / q^9), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), ((q^12 - 6*q^10 + 15*q^8 - 20*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^10), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^8), 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^9), ((q^4 - 2*q^2 + 1) / q^4), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), 0, 0]
theorem cGL_4_1_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_1_v12 q) = cGL_4_1_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_1_v12 cGL_4_1_v13; stepTac
def cGL_4_1_v14 (q : R) : Fin 15 → R := ![((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^6), ((-2*q^18 + 11*q^16 - 29*q^14 + 52*q^12 - 66*q^10 + 63*q^8 - 44*q^6 + 22*q^4 - 7*q^2 + 1) / q^9), ((-2*q^16 + 9*q^14 - 22*q^12 + 37*q^10 - 44*q^8 + 37*q^6 - 21*q^4 + 7*q^2 - 1) / q^8), ((-2*q^14 + 11*q^12 - 27*q^10 + 39*q^8 - 36*q^6 + 21*q^4 - 7*q^2 + 1) / q^10), ((-q^12 + 6*q^10 - 15*q^8 + 20*q^6 - 15*q^4 + 6*q^2 - 1) / q^9), ((q^12 - 6*q^10 + 15*q^8 - 20*q^6 + 15*q^4 - 6*q^2 + 1) / q^6), ((-2*q^14 + 9*q^12 - 20*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^11), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^10), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^7), 0, ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^10), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^9), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), 0, 0]
theorem cGL_4_1_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_1_v13 q) = cGL_4_1_v14 q := by
  rw [bridge4_0]; unfold cGL_4_1_v13 cGL_4_1_v14; stepTac
theorem cGL_4_1_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 1 1) = cGL_4_1_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_1_v0_step q hq, cGL_4_1_v1_step q hq, cGL_4_1_v2_step q hq, cGL_4_1_v3_step q hq, cGL_4_1_v4_step q hq, cGL_4_1_v5_step q hq, cGL_4_1_v6_step q hq, cGL_4_1_v7_step q hq, cGL_4_1_v8_step q hq, cGL_4_1_v9_step q hq, cGL_4_1_v10_step q hq, cGL_4_1_v11_step q hq, cGL_4_1_v12_step q hq, cGL_4_1_v13_step q hq, cGL_4_1_v14_step q hq]
theorem cGL_4_1_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 1 1 = ((-2*q^18 + 11*q^16 - 29*q^14 + 52*q^12 - 66*q^10 + 63*q^8 - 44*q^6 + 22*q^4 - 7*q^2 + 1) / q^9) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 1 1, cGL_4_1_col q hq]; simp [cGL_4_1_v14]

def cGL_4_2_v0 (q : R) : Fin 15 → R := ![0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_2_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 2 1) = cGL_4_2_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_2_v0; stepTac
def cGL_4_2_v1 (q : R) : Fin 15 → R := ![0, 0, ((q^2 - 1) / q^2), 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_2_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_2_v0 q) = cGL_4_2_v1 q := by
  rw [bridge4_2]; unfold cGL_4_2_v0 cGL_4_2_v1; stepTac
def cGL_4_2_v2 (q : R) : Fin 15 → R := ![0, 0, ((q^2 - 1) / q^3), 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_2_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_2_v1 q) = cGL_4_2_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_2_v1 cGL_4_2_v2; stepTac
def cGL_4_2_v3 (q : R) : Fin 15 → R := ![0, 0, ((q^4 - 2*q^2 + 1) / q^4), 0, ((q^2 - 1) / q^3), 0, 0, (1), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_2_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_2_v2 q) = cGL_4_2_v3 q := by
  rw [bridge4_2]; unfold cGL_4_2_v2 cGL_4_2_v3; stepTac
def cGL_4_2_v4 (q : R) : Fin 15 → R := ![0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, (1), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_2_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGL_4_2_v3 q) = cGL_4_2_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGL_4_2_v3 cGL_4_2_v4; stepTac
def cGL_4_2_v5 (q : R) : Fin 15 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_2_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGL_4_2_v4 q) = cGL_4_2_v5 q := by
  rw [bridge4_2]; unfold cGL_4_2_v4 cGL_4_2_v5; stepTac
def cGL_4_2_v6 (q : R) : Fin 15 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_4_2_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_2_v5 q) = cGL_4_2_v6 q := by
  rw [bridge4_3]; unfold cGL_4_2_v5 cGL_4_2_v6; stepTac
def cGL_4_2_v7 (q : R) : Fin 15 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^4), 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), 0, 0, 0]
theorem cGL_4_2_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, false)).mulVec (cGL_4_2_v6 q) = cGL_4_2_v7 q := by
  rw [bridge4_4]; unfold cGL_4_2_v6 cGL_4_2_v7; stepTac
def cGL_4_2_v8 (q : R) : Fin 15 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^3), 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), 0, 0, 0]
theorem cGL_4_2_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGL_4_2_v7 q) = cGL_4_2_v8 q := by
  rw [bridge4_3]; unfold cGL_4_2_v7 cGL_4_2_v8; stepTac
def cGL_4_2_v9 (q : R) : Fin 15 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^4), 0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), 0, 0]
theorem cGL_4_2_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_2_v8 q) = cGL_4_2_v9 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_2_v8 cGL_4_2_v9; stepTac
def cGL_4_2_v10 (q : R) : Fin 15 → R := ![0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^3), 0, 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^3), 0, 0]
theorem cGL_4_2_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_2_v9 q) = cGL_4_2_v10 q := by
  rw [bridge4_0]; unfold cGL_4_2_v9 cGL_4_2_v10; stepTac
def cGL_4_2_v11 (q : R) : Fin 15 → R := ![((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^4), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), 0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^3), ((q^10 - 5*q^8 + 10*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), 0, ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), 0, 0, ((q^4 - 2*q^2 + 1) / q^3), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^4), 0, 0]
theorem cGL_4_2_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_2_v10 q) = cGL_4_2_v11 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_2_v10 cGL_4_2_v11; stepTac
def cGL_4_2_v12 (q : R) : Fin 15 → R := ![((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^3), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^3), 0, ((q^10 - 5*q^8 + 10*q^6 - 10*q^4 + 5*q^2 - 1) / q^3), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^4), 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), 0, ((q^4 - 2*q^2 + 1) / q^3), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^3), 0, 0]
theorem cGL_4_2_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_2_v11 q) = cGL_4_2_v12 q := by
  rw [bridge4_0]; unfold cGL_4_2_v11 cGL_4_2_v12; stepTac
def cGL_4_2_v13 (q : R) : Fin 15 → R := ![((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^7), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), ((q^10 - 5*q^8 + 10*q^6 - 10*q^4 + 5*q^2 - 1) / q^3), ((-q^12 + 6*q^10 - 15*q^8 + 20*q^6 - 15*q^4 + 6*q^2 - 1) / q^4), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), 0, ((q^4 - 2*q^2 + 1) / q^4), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^3), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0]
theorem cGL_4_2_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, true)).mulVec (cGL_4_2_v12 q) = cGL_4_2_v13 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_1]; unfold cGL_4_2_v12 cGL_4_2_v13; stepTac
def cGL_4_2_v14 (q : R) : Fin 15 → R := ![((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^5), ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^8), ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^7), ((q^12 - 6*q^10 + 15*q^8 - 20*q^6 + 15*q^4 - 6*q^2 + 1) / q^5), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^4), ((-q^12 + 6*q^10 - 15*q^8 + 20*q^6 - 15*q^4 + 6*q^2 - 1) / q^3), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), 0, 0]
theorem cGL_4_2_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGL_4_2_v13 q) = cGL_4_2_v14 q := by
  rw [bridge4_0]; unfold cGL_4_2_v13 cGL_4_2_v14; stepTac
theorem cGL_4_2_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGL).mulVec (Pi.single 2 1) = cGL_4_2_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_4_2_v0_step q hq, cGL_4_2_v1_step q hq, cGL_4_2_v2_step q hq, cGL_4_2_v3_step q hq, cGL_4_2_v4_step q hq, cGL_4_2_v5_step q hq, cGL_4_2_v6_step q hq, cGL_4_2_v7_step q hq, cGL_4_2_v8_step q hq, cGL_4_2_v9_step q hq, cGL_4_2_v10_step q hq, cGL_4_2_v11_step q hq, cGL_4_2_v12_step q hq, cGL_4_2_v13_step q hq, cGL_4_2_v14_step q hq]
theorem cGL_4_2_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGL 2 2 = ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^7) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGL) 2 2, cGL_4_2_col q hq]; simp [cGL_4_2_v14]

def cGL_2_2_v0 (q : R) : Fin 15 → R := ![0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_2_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 2 1) = cGL_2_2_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_2_v0; stepTac
def cGL_2_2_v1 (q : R) : Fin 15 → R := ![0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_2_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_2_v0 q) = cGL_2_2_v1 q := by
  rw [bridge2_2]; unfold cGL_2_2_v0 cGL_2_2_v1; stepTac
def cGL_2_2_v2 (q : R) : Fin 15 → R := ![((1) / q), ((-q^2 + 1) / q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_2_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_2_v1 q) = cGL_2_2_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_2_v1 cGL_2_2_v2; stepTac
def cGL_2_2_v3 (q : R) : Fin 15 → R := ![(1), ((-q^4 + 2*q^2 - 1) / q^3), ((-q^2 + 1) / q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_2_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_2_v2 q) = cGL_2_2_v3 q := by
  rw [bridge2_2]; unfold cGL_2_2_v2 cGL_2_2_v3; stepTac
def cGL_2_2_v4 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q^3), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), ((-q^2 + 1) / q^3), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_2_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_2_v3 q) = cGL_2_2_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_2_v3 cGL_2_2_v4; stepTac
def cGL_2_2_v5 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q^2), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_2_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_2_v4 q) = cGL_2_2_v5 q := by
  rw [bridge2_2]; unfold cGL_2_2_v4 cGL_2_2_v5; stepTac
def cGL_2_2_v6 (q : R) : Fin 15 → R := ![((q^4 - 2*q^2 + 1) / q^5), ((-q^4 + 2*q^2 - 1) / q^2), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_2_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_2_v5 q) = cGL_2_2_v6 q := by
  rw [bridge2_3]; unfold cGL_2_2_v5 cGL_2_2_v6; stepTac
def cGL_2_2_v7 (q : R) : Fin 15 → R := ![((q^4 - 2*q^2 + 1) / q^4), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^3), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_2_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_2_v6 q) = cGL_2_2_v7 q := by
  rw [bridge2_4]; unfold cGL_2_2_v6 cGL_2_2_v7; stepTac
def cGL_2_2_v8 (q : R) : Fin 15 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^3), 0, 0, ((-q^4 + 2*q^2 - 1) / q), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0, 0, 0]
theorem cGL_2_2_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_2_v7 q) = cGL_2_2_v8 q := by
  rw [bridge2_3]; unfold cGL_2_2_v7 cGL_2_2_v8; stepTac
def cGL_2_2_v9 (q : R) : Fin 15 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), 0, ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^3), 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0, 0]
theorem cGL_2_2_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_2_v8 q) = cGL_2_2_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_2_v8 cGL_2_2_v9; stepTac
def cGL_2_2_v10 (q : R) : Fin 15 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), 0, ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q), 0, ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), 0, ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0]
theorem cGL_2_2_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_2_v9 q) = cGL_2_2_v10 q := by
  rw [bridge2_0]; unfold cGL_2_2_v9 cGL_2_2_v10; stepTac
def cGL_2_2_v11 (q : R) : Fin 15 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^4), ((-q^12 + 5*q^10 - 12*q^8 + 17*q^6 - 14*q^4 + 6*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^2), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^5), ((-q^12 + 5*q^10 - 12*q^8 + 17*q^6 - 14*q^4 + 6*q^2 - 1) / q^6), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^5), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0]
theorem cGL_2_2_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_2_v10 q) = cGL_2_2_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_2_v10 cGL_2_2_v11; stepTac
def cGL_2_2_v12 (q : R) : Fin 15 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^3), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^6), ((-q^12 + 5*q^10 - 12*q^8 + 17*q^6 - 14*q^4 + 6*q^2 - 1) / q^5), ((-q^4 + 2*q^2 - 1) / q), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^4), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^7), ((-q^12 + 5*q^10 - 12*q^8 + 17*q^6 - 14*q^4 + 6*q^2 - 1) / q^6), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^3), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^5), 0, 0, 0]
theorem cGL_2_2_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_2_v11 q) = cGL_2_2_v12 q := by
  rw [bridge2_0]; unfold cGL_2_2_v11 cGL_2_2_v12; stepTac
def cGL_2_2_v13 (q : R) : Fin 15 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^6), ((q^16 - 6*q^14 + 18*q^12 - 34*q^10 + 43*q^8 - 37*q^6 + 21*q^4 - 7*q^2 + 1) / q^7), ((-q^12 + 5*q^10 - 12*q^8 + 17*q^6 - 14*q^4 + 6*q^2 - 1) / q^6), ((-q^4 + 2*q^2 - 1) / q^2), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^7), ((q^16 - 6*q^14 + 18*q^12 - 34*q^10 + 43*q^8 - 37*q^6 + 21*q^4 - 7*q^2 + 1) / q^8), ((-q^12 + 5*q^10 - 12*q^8 + 17*q^6 - 14*q^4 + 6*q^2 - 1) / q^7), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^7), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^6), 0, 0, 0]
theorem cGL_2_2_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_2_v12 q) = cGL_2_2_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_2_v12 cGL_2_2_v13; stepTac
def cGL_2_2_v14 (q : R) : Fin 15 → R := ![((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^5), ((q^18 - 7*q^16 + 23*q^14 - 47*q^12 + 65*q^10 - 63*q^8 + 44*q^6 - 22*q^4 + 7*q^2 - 1) / q^8), ((q^16 - 6*q^14 + 18*q^12 - 34*q^10 + 43*q^8 - 37*q^6 + 21*q^4 - 7*q^2 + 1) / q^7), ((-q^4 + 2*q^2 - 1) / q), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^6), ((q^18 - 7*q^16 + 23*q^14 - 47*q^12 + 65*q^10 - 63*q^8 + 44*q^6 - 22*q^4 + 7*q^2 - 1) / q^9), ((q^16 - 6*q^14 + 18*q^12 - 34*q^10 + 43*q^8 - 37*q^6 + 21*q^4 - 7*q^2 + 1) / q^8), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 35*q^8 - 28*q^6 + 16*q^4 - 6*q^2 + 1) / q^8), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^7), 0, 0, 0]
theorem cGL_2_2_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_2_v13 q) = cGL_2_2_v14 q := by
  rw [bridge2_0]; unfold cGL_2_2_v13 cGL_2_2_v14; stepTac
theorem cGL_2_2_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 2 1) = cGL_2_2_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_2_v0_step q hq, cGL_2_2_v1_step q hq, cGL_2_2_v2_step q hq, cGL_2_2_v3_step q hq, cGL_2_2_v4_step q hq, cGL_2_2_v5_step q hq, cGL_2_2_v6_step q hq, cGL_2_2_v7_step q hq, cGL_2_2_v8_step q hq, cGL_2_2_v9_step q hq, cGL_2_2_v10_step q hq, cGL_2_2_v11_step q hq, cGL_2_2_v12_step q hq, cGL_2_2_v13_step q hq, cGL_2_2_v14_step q hq]
theorem cGL_2_2_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 2 2 = ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 2 2, cGL_2_2_col q hq]; simp [cGL_2_2_v14]

def cGL_2_3_v0 (q : R) : Fin 15 → R := ![0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_3_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 3 1) = cGL_2_3_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_3_v0; stepTac
def cGL_2_3_v1 (q : R) : Fin 15 → R := ![0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_3_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_3_v0 q) = cGL_2_3_v1 q := by
  rw [bridge2_2]; unfold cGL_2_3_v0 cGL_2_3_v1; stepTac
def cGL_2_3_v2 (q : R) : Fin 15 → R := ![0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_3_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_3_v1 q) = cGL_2_3_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_3_v1 cGL_2_3_v2; stepTac
def cGL_2_3_v3 (q : R) : Fin 15 → R := ![0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_3_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_3_v2 q) = cGL_2_3_v3 q := by
  rw [bridge2_2]; unfold cGL_2_3_v2 cGL_2_3_v3; stepTac
def cGL_2_3_v4 (q : R) : Fin 15 → R := ![0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_3_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_3_v3 q) = cGL_2_3_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_3_v3 cGL_2_3_v4; stepTac
def cGL_2_3_v5 (q : R) : Fin 15 → R := ![0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_3_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_3_v4 q) = cGL_2_3_v5 q := by
  rw [bridge2_2]; unfold cGL_2_3_v4 cGL_2_3_v5; stepTac
def cGL_2_3_v6 (q : R) : Fin 15 → R := ![0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_3_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_3_v5 q) = cGL_2_3_v6 q := by
  rw [bridge2_3]; unfold cGL_2_3_v5 cGL_2_3_v6; stepTac
def cGL_2_3_v7 (q : R) : Fin 15 → R := ![0, 0, 0, (q^2 - 1), 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_3_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_3_v6 q) = cGL_2_3_v7 q := by
  rw [bridge2_4]; unfold cGL_2_3_v6 cGL_2_3_v7; stepTac
def cGL_2_3_v8 (q : R) : Fin 15 → R := ![0, 0, 0, (q^3 - q), 0, 0, 0, (q^2 - 1), 0, 0, (q), 0, 0, 0, 0]
theorem cGL_2_3_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_3_v7 q) = cGL_2_3_v8 q := by
  rw [bridge2_3]; unfold cGL_2_3_v7 cGL_2_3_v8; stepTac
def cGL_2_3_v9 (q : R) : Fin 15 → R := ![0, 0, (q^3 - q), (-q^4 + 2*q^2 - 1), 0, 0, (q^2 - 1), ((-q^4 + 2*q^2 - 1) / q), 0, (q), (-q^2 + 1), 0, 0, 0, 0]
theorem cGL_2_3_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_3_v8 q) = cGL_2_3_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_3_v8 cGL_2_3_v9; stepTac
def cGL_2_3_v10 (q : R) : Fin 15 → R := ![0, 0, (q^4 - q^2), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q), (-q^4 + 2*q^2 - 1), 0, (q^3 - q), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^2), ((-q^4 + 2*q^2 - 1) / q), (q^2), ((-q^4 + 2*q^2 - 1) / q), (-q^2 + 1), 0, 0, 0]
theorem cGL_2_3_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_3_v9 q) = cGL_2_3_v10 q := by
  rw [bridge2_0]; unfold cGL_2_3_v9 cGL_2_3_v10; stepTac
def cGL_2_3_v11 (q : R) : Fin 15 → R := ![0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^2), ((-q^4 + 2*q^2 - 1) / q), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^2), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), ((-q^4 + 2*q^2 - 1) / q), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^2), ((-q^2 + 1) / q), 0, 0, 0]
theorem cGL_2_3_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_3_v10 q) = cGL_2_3_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_3_v10 cGL_2_3_v11; stepTac
def cGL_2_3_v12 (q : R) : Fin 15 → R := ![0, 0, (-q^6 + 3*q^4 - 3*q^2 + 1), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^2), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^3), (-q^4 + 2*q^2 - 1), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^2), 0, 0, 0]
theorem cGL_2_3_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_3_v11 q) = cGL_2_3_v12 q := by
  rw [bridge2_0]; unfold cGL_2_3_v11 cGL_2_3_v12; stepTac
def cGL_2_3_v13 (q : R) : Fin 15 → R := ![0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^3), 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0]
theorem cGL_2_3_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_3_v12 q) = cGL_2_3_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_3_v12 cGL_2_3_v13; stepTac
def cGL_2_3_v14 (q : R) : Fin 15 → R := ![0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^2), ((-q^14 + 5*q^12 - 11*q^10 + 16*q^8 - 16*q^6 + 11*q^4 - 5*q^2 + 1) / q^5), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), ((-q^14 + 5*q^12 - 11*q^10 + 16*q^8 - 16*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0, 0]
theorem cGL_2_3_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_3_v13 q) = cGL_2_3_v14 q := by
  rw [bridge2_0]; unfold cGL_2_3_v13 cGL_2_3_v14; stepTac
theorem cGL_2_3_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 3 1) = cGL_2_3_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_3_v0_step q hq, cGL_2_3_v1_step q hq, cGL_2_3_v2_step q hq, cGL_2_3_v3_step q hq, cGL_2_3_v4_step q hq, cGL_2_3_v5_step q hq, cGL_2_3_v6_step q hq, cGL_2_3_v7_step q hq, cGL_2_3_v8_step q hq, cGL_2_3_v9_step q hq, cGL_2_3_v10_step q hq, cGL_2_3_v11_step q hq, cGL_2_3_v12_step q hq, cGL_2_3_v13_step q hq, cGL_2_3_v14_step q hq]
theorem cGL_2_3_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 3 3 = ((-q^14 + 5*q^12 - 11*q^10 + 16*q^8 - 16*q^6 + 11*q^4 - 5*q^2 + 1) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 3 3, cGL_2_3_col q hq]; simp [cGL_2_3_v14]

def cGL_2_4_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_4_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 4 1) = cGL_2_4_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_4_v0; stepTac
def cGL_2_4_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_4_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_4_v0 q) = cGL_2_4_v1 q := by
  rw [bridge2_2]; unfold cGL_2_4_v0 cGL_2_4_v1; stepTac
def cGL_2_4_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_4_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_4_v1 q) = cGL_2_4_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_4_v1 cGL_2_4_v2; stepTac
def cGL_2_4_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_4_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_4_v2 q) = cGL_2_4_v3 q := by
  rw [bridge2_2]; unfold cGL_2_4_v2 cGL_2_4_v3; stepTac
def cGL_2_4_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_4_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_4_v3 q) = cGL_2_4_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_4_v3 cGL_2_4_v4; stepTac
def cGL_2_4_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_4_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_4_v4 q) = cGL_2_4_v5 q := by
  rw [bridge2_2]; unfold cGL_2_4_v4 cGL_2_4_v5; stepTac
def cGL_2_4_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_4_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_4_v5 q) = cGL_2_4_v6 q := by
  rw [bridge2_3]; unfold cGL_2_4_v5 cGL_2_4_v6; stepTac
def cGL_2_4_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (q^2 - 1), 0, 0, 0, (q), 0, 0, 0, 0, 0, 0]
theorem cGL_2_4_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_4_v6 q) = cGL_2_4_v7 q := by
  rw [bridge2_4]; unfold cGL_2_4_v6 cGL_2_4_v7; stepTac
def cGL_2_4_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (q^3 - q), 0, 0, 0, (q^2 - 1), 0, 0, (q), 0, 0, 0]
theorem cGL_2_4_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_4_v7 q) = cGL_2_4_v8 q := by
  rw [bridge2_3]; unfold cGL_2_4_v7 cGL_2_4_v8; stepTac
def cGL_2_4_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (q^2 - 1), 0, 0, 0, ((q^2 - 1) / q), 0, 0, (1), 0, 0, 0]
theorem cGL_2_4_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_4_v8 q) = cGL_2_4_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_4_v8 cGL_2_4_v9; stepTac
def cGL_2_4_v10 (q : R) : Fin 15 → R := ![0, 0, 0, (q^2 - 1), 0, 0, 0, ((q^2 - 1) / q), 0, 0, (1), 0, 0, 0, 0]
theorem cGL_2_4_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_4_v9 q) = cGL_2_4_v10 q := by
  rw [bridge2_0]; unfold cGL_2_4_v9 cGL_2_4_v10; stepTac
def cGL_2_4_v11 (q : R) : Fin 15 → R := ![0, 0, (q^2 - 1), ((-q^4 + 2*q^2 - 1) / q), 0, 0, ((q^2 - 1) / q), ((-q^4 + 2*q^2 - 1) / q^2), 0, (1), ((-q^2 + 1) / q), 0, 0, 0, 0]
theorem cGL_2_4_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_4_v10 q) = cGL_2_4_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_4_v10 cGL_2_4_v11; stepTac
def cGL_2_4_v12 (q : R) : Fin 15 → R := ![0, 0, (q^3 - q), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^2), ((-q^4 + 2*q^2 - 1) / q), 0, (q^2 - 1), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), (q), ((-q^4 + 2*q^2 - 1) / q^2), ((-q^2 + 1) / q), 0, 0, 0]
theorem cGL_2_4_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_4_v11 q) = cGL_2_4_v12 q := by
  rw [bridge2_0]; unfold cGL_2_4_v11 cGL_2_4_v12; stepTac
def cGL_2_4_v13 (q : R) : Fin 15 → R := ![0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^2), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^3), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), ((-q^2 + 1) / q^2), 0, 0, 0]
theorem cGL_2_4_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_4_v12 q) = cGL_2_4_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_4_v12 cGL_2_4_v13; stepTac
def cGL_2_4_v14 (q : R) : Fin 15 → R := ![0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^3), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^2), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0]
theorem cGL_2_4_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_4_v13 q) = cGL_2_4_v14 q := by
  rw [bridge2_0]; unfold cGL_2_4_v13 cGL_2_4_v14; stepTac
theorem cGL_2_4_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 4 1) = cGL_2_4_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_4_v0_step q hq, cGL_2_4_v1_step q hq, cGL_2_4_v2_step q hq, cGL_2_4_v3_step q hq, cGL_2_4_v4_step q hq, cGL_2_4_v5_step q hq, cGL_2_4_v6_step q hq, cGL_2_4_v7_step q hq, cGL_2_4_v8_step q hq, cGL_2_4_v9_step q hq, cGL_2_4_v10_step q hq, cGL_2_4_v11_step q hq, cGL_2_4_v12_step q hq, cGL_2_4_v13_step q hq, cGL_2_4_v14_step q hq]
theorem cGL_2_4_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 4 4 = ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 4 4, cGL_2_4_col q hq]; simp [cGL_2_4_v14]

def cGL_2_6_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0, 0]
theorem cGL_2_6_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 6 1) = cGL_2_6_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_6_v0; stepTac
def cGL_2_6_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, (q), 0, 0, 0, 0, 0]
theorem cGL_2_6_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_6_v0 q) = cGL_2_6_v1 q := by
  rw [bridge2_2]; unfold cGL_2_6_v0 cGL_2_6_v1; stepTac
def cGL_2_6_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, (q), 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0]
theorem cGL_2_6_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_6_v1 q) = cGL_2_6_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_6_v1 cGL_2_6_v2; stepTac
def cGL_2_6_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (q), 0, 0, 0, (-q^3 + q), 0, 0, 0, 0, 0]
theorem cGL_2_6_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_6_v2 q) = cGL_2_6_v3 q := by
  rw [bridge2_2]; unfold cGL_2_6_v2 cGL_2_6_v3; stepTac
def cGL_2_6_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (1), (-q^3 + q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0]
theorem cGL_2_6_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_6_v3 q) = cGL_2_6_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_6_v3 cGL_2_6_v4; stepTac
def cGL_2_6_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), (1), 0, 0, (q^5 - 2*q^3 + q), 0, 0, 0, 0, 0]
theorem cGL_2_6_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_6_v4 q) = cGL_2_6_v5 q := by
  rw [bridge2_2]; unfold cGL_2_6_v4 cGL_2_6_v5; stepTac
def cGL_2_6_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (-q^4 + 2*q^2 - 1), ((q^6 - 2*q^4 + 2*q^2 - 1) / q), 0, 0, (1), 0, 0, 0, 0, 0]
theorem cGL_2_6_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_6_v5 q) = cGL_2_6_v6 q := by
  rw [bridge2_3]; unfold cGL_2_6_v5 cGL_2_6_v6; stepTac
def cGL_2_6_v7 (q : R) : Fin 15 → R := ![0, (-q^4 + 2*q^2 - 1), ((q^6 - 2*q^4 + 2*q^2 - 1) / q), 0, 0, 0, 0, 0, 0, (q), 0, 0, 0, 0, 0]
theorem cGL_2_6_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_6_v6 q) = cGL_2_6_v7 q := by
  rw [bridge2_4]; unfold cGL_2_6_v6 cGL_2_6_v7; stepTac
def cGL_2_6_v8 (q : R) : Fin 15 → R := ![(-q^4 + 2*q^2 - 1), 0, (q^6 - 2*q^4 + 2*q^2 - 1), 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_6_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_6_v7 q) = cGL_2_6_v8 q := by
  rw [bridge2_3]; unfold cGL_2_6_v7 cGL_2_6_v8; stepTac
def cGL_2_6_v9 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q), 0, 0, (q^6 - 2*q^4 + 2*q^2 - 1), 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_6_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_6_v8 q) = cGL_2_6_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_6_v8 cGL_2_6_v9; stepTac
def cGL_2_6_v10 (q : R) : Fin 15 → R := ![(-q^4 + 2*q^2 - 1), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), (q^6 - 2*q^4 + 2*q^2 - 1), 0, 0, (q^2 - 1), (q), 0, 0, 0, 0, 0, 0]
theorem cGL_2_6_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_6_v9 q) = cGL_2_6_v10 q := by
  rw [bridge2_0]; unfold cGL_2_6_v9 cGL_2_6_v10; stepTac
def cGL_2_6_v11 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^2), ((q^6 - 2*q^4 + 2*q^2 - 1) / q), 0, (q^2 - 1), ((-q^4 + 2*q^2 - 1) / q), (1), 0, 0, 0, 0, 0, 0]
theorem cGL_2_6_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_6_v10 q) = cGL_2_6_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_6_v10 cGL_2_6_v11; stepTac
def cGL_2_6_v12 (q : R) : Fin 15 → R := ![(-q^4 + 2*q^2 - 1), 0, (q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1), ((-q^12 + 5*q^10 - 10*q^8 + 12*q^6 - 9*q^4 + 4*q^2 - 1) / q^3), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^2), 0, (q^3 - q), ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), ((-q^4 + 2*q^2 - 1) / q), 0, 0, 0, 0, 0, 0]
theorem cGL_2_6_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_6_v11 q) = cGL_2_6_v12 q := by
  rw [bridge2_0]; unfold cGL_2_6_v11 cGL_2_6_v12; stepTac
def cGL_2_6_v13 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q), 0, ((-q^12 + 5*q^10 - 10*q^8 + 12*q^6 - 9*q^4 + 4*q^2 - 1) / q^3), ((q^14 - 5*q^12 + 12*q^10 - 18*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^4), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^3), 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0, 0]
theorem cGL_2_6_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_6_v12 q) = cGL_2_6_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_6_v12 cGL_2_6_v13; stepTac
def cGL_2_6_v14 (q : R) : Fin 15 → R := ![(-q^4 + 2*q^2 - 1), 0, ((-q^12 + 5*q^10 - 10*q^8 + 12*q^6 - 9*q^4 + 4*q^2 - 1) / q^2), ((q^16 - 6*q^14 + 16*q^12 - 26*q^10 + 29*q^8 - 23*q^6 + 13*q^4 - 5*q^2 + 1) / q^5), ((q^14 - 5*q^12 + 12*q^10 - 18*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^4), 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, 0, 0, 0]
theorem cGL_2_6_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_6_v13 q) = cGL_2_6_v14 q := by
  rw [bridge2_0]; unfold cGL_2_6_v13 cGL_2_6_v14; stepTac
theorem cGL_2_6_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 6 1) = cGL_2_6_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_6_v0_step q hq, cGL_2_6_v1_step q hq, cGL_2_6_v2_step q hq, cGL_2_6_v3_step q hq, cGL_2_6_v4_step q hq, cGL_2_6_v5_step q hq, cGL_2_6_v6_step q hq, cGL_2_6_v7_step q hq, cGL_2_6_v8_step q hq, cGL_2_6_v9_step q hq, cGL_2_6_v10_step q hq, cGL_2_6_v11_step q hq, cGL_2_6_v12_step q hq, cGL_2_6_v13_step q hq, cGL_2_6_v14_step q hq]
theorem cGL_2_6_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 6 6 = ((-q^6 + 3*q^4 - 2*q^2 + 1) / q) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 6 6, cGL_2_6_col q hq]; simp [cGL_2_6_v14]

def cGL_2_7_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0]
theorem cGL_2_7_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 7 1) = cGL_2_7_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_7_v0; stepTac
def cGL_2_7_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, (1), 0, 0]
theorem cGL_2_7_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_7_v0 q) = cGL_2_7_v1 q := by
  rw [bridge2_2]; unfold cGL_2_7_v0 cGL_2_7_v1; stepTac
def cGL_2_7_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((1) / q), 0, 0]
theorem cGL_2_7_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_7_v1 q) = cGL_2_7_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_7_v1 cGL_2_7_v2; stepTac
def cGL_2_7_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (q^2 - 1), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0]
theorem cGL_2_7_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_7_v2 q) = cGL_2_7_v3 q := by
  rw [bridge2_2]; unfold cGL_2_7_v2 cGL_2_7_v3; stepTac
def cGL_2_7_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0]
theorem cGL_2_7_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_7_v3 q) = cGL_2_7_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_7_v3 cGL_2_7_v4; stepTac
def cGL_2_7_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0]
theorem cGL_2_7_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_7_v4 q) = cGL_2_7_v5 q := by
  rw [bridge2_2]; unfold cGL_2_7_v4 cGL_2_7_v5; stepTac
def cGL_2_7_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^5), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0]
theorem cGL_2_7_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_7_v5 q) = cGL_2_7_v6 q := by
  rw [bridge2_3]; unfold cGL_2_7_v5 cGL_2_7_v6; stepTac
def cGL_2_7_v7 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^5), 0, 0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, 0]
theorem cGL_2_7_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_7_v6 q) = cGL_2_7_v7 q := by
  rw [bridge2_4]; unfold cGL_2_7_v6 cGL_2_7_v7; stepTac
def cGL_2_7_v8 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^4), 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), 0, 0]
theorem cGL_2_7_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_7_v7 q) = cGL_2_7_v8 q := by
  rw [bridge2_3]; unfold cGL_2_7_v7 cGL_2_7_v8; stepTac
def cGL_2_7_v9 (q : R) : Fin 15 → R := ![0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^4), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^2), 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, 0]
theorem cGL_2_7_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_7_v8 q) = cGL_2_7_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_7_v8 cGL_2_7_v9; stepTac
def cGL_2_7_v10 (q : R) : Fin 15 → R := ![0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^3), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^6), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^5), 0, (-q^6 + 3*q^4 - 2*q^2 + 1), ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^3), ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^2), 0, 0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0]
theorem cGL_2_7_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_7_v9 q) = cGL_2_7_v10 q := by
  rw [bridge2_0]; unfold cGL_2_7_v9 cGL_2_7_v10; stepTac
def cGL_2_7_v11 (q : R) : Fin 15 → R := ![0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^6), ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^3), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2)]
theorem cGL_2_7_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_7_v10 q) = cGL_2_7_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_7_v10 cGL_2_7_v11; stepTac
def cGL_2_7_v12 (q : R) : Fin 15 → R := ![0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^5), ((q^14 - 5*q^12 + 12*q^10 - 18*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^8), ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), 0, ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^2), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^5), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), 0, 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^5), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q)]
theorem cGL_2_7_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_7_v11 q) = cGL_2_7_v12 q := by
  rw [bridge2_0]; unfold cGL_2_7_v11 cGL_2_7_v12; stepTac
def cGL_2_7_v13 (q : R) : Fin 15 → R := ![0, 0, ((q^14 - 5*q^12 + 12*q^10 - 18*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^8), ((-q^16 + 5*q^14 - 13*q^12 + 23*q^10 - 29*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^9), ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^5), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), 0, 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4)]
theorem cGL_2_7_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_7_v12 q) = cGL_2_7_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_7_v12 cGL_2_7_v13; stepTac
def cGL_2_7_v14 (q : R) : Fin 15 → R := ![0, 0, ((q^14 - 5*q^12 + 12*q^10 - 18*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^7), ((-q^18 + 6*q^16 - 17*q^14 + 32*q^12 - 43*q^10 + 43*q^8 - 32*q^6 + 17*q^4 - 6*q^2 + 1) / q^10), ((-q^16 + 5*q^14 - 13*q^12 + 23*q^10 - 29*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^9), 0, ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^4), ((q^18 - 7*q^16 + 21*q^14 - 39*q^12 + 52*q^10 - 50*q^8 + 36*q^6 - 18*q^4 + 6*q^2 - 1) / q^7), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), 0, 0, 0, ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^7), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^3)]
theorem cGL_2_7_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_7_v13 q) = cGL_2_7_v14 q := by
  rw [bridge2_0]; unfold cGL_2_7_v13 cGL_2_7_v14; stepTac
theorem cGL_2_7_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 7 1) = cGL_2_7_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_7_v0_step q hq, cGL_2_7_v1_step q hq, cGL_2_7_v2_step q hq, cGL_2_7_v3_step q hq, cGL_2_7_v4_step q hq, cGL_2_7_v5_step q hq, cGL_2_7_v6_step q hq, cGL_2_7_v7_step q hq, cGL_2_7_v8_step q hq, cGL_2_7_v9_step q hq, cGL_2_7_v10_step q hq, cGL_2_7_v11_step q hq, cGL_2_7_v12_step q hq, cGL_2_7_v13_step q hq, cGL_2_7_v14_step q hq]
theorem cGL_2_7_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 7 7 = ((q^18 - 7*q^16 + 21*q^14 - 39*q^12 + 52*q^10 - 50*q^8 + 36*q^6 - 18*q^4 + 6*q^2 - 1) / q^7) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 7 7, cGL_2_7_col q hq]; simp [cGL_2_7_v14]

def cGL_2_8_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0]
theorem cGL_2_8_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 8 1) = cGL_2_8_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_8_v0; stepTac
def cGL_2_8_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, (1), 0]
theorem cGL_2_8_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_8_v0 q) = cGL_2_8_v1 q := by
  rw [bridge2_2]; unfold cGL_2_8_v0 cGL_2_8_v1; stepTac
def cGL_2_8_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((1) / q), 0]
theorem cGL_2_8_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_8_v1 q) = cGL_2_8_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_8_v1 cGL_2_8_v2; stepTac
def cGL_2_8_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, (q^2 - 1), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, ((-q^4 + 2*q^2 - 1) / q^2), 0]
theorem cGL_2_8_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_8_v2 q) = cGL_2_8_v3 q := by
  rw [bridge2_2]; unfold cGL_2_8_v2 cGL_2_8_v3; stepTac
def cGL_2_8_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^4 + 2*q^2 - 1) / q^3), 0]
theorem cGL_2_8_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_8_v3 q) = cGL_2_8_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_8_v3 cGL_2_8_v4; stepTac
def cGL_2_8_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0]
theorem cGL_2_8_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_8_v4 q) = cGL_2_8_v5 q := by
  rw [bridge2_2]; unfold cGL_2_8_v4 cGL_2_8_v5; stepTac
def cGL_2_8_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^5), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0]
theorem cGL_2_8_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_8_v5 q) = cGL_2_8_v6 q := by
  rw [bridge2_3]; unfold cGL_2_8_v5 cGL_2_8_v6; stepTac
def cGL_2_8_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^5), 0, 0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0]
theorem cGL_2_8_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_8_v6 q) = cGL_2_8_v7 q := by
  rw [bridge2_4]; unfold cGL_2_8_v6 cGL_2_8_v7; stepTac
def cGL_2_8_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^4), 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), 0]
theorem cGL_2_8_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_8_v7 q) = cGL_2_8_v8 q := by
  rw [bridge2_3]; unfold cGL_2_8_v7 cGL_2_8_v8; stepTac
def cGL_2_8_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^5), 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q)]
theorem cGL_2_8_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_8_v8 q) = cGL_2_8_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_8_v8 cGL_2_8_v9; stepTac
def cGL_2_8_v10 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^5), 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, 0, 0, 0, 0, (q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1)]
theorem cGL_2_8_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_8_v9 q) = cGL_2_8_v10 q := by
  rw [bridge2_0]; unfold cGL_2_8_v9 cGL_2_8_v10; stepTac
def cGL_2_8_v11 (q : R) : Fin 15 → R := ![0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^5), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, 0, 0, (q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q)]
theorem cGL_2_8_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_8_v10 q) = cGL_2_8_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_8_v10 cGL_2_8_v11; stepTac
def cGL_2_8_v12 (q : R) : Fin 15 → R := ![0, 0, ((q^6 - 2*q^4 + 2*q^2 - 1) / q^4), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^7), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^6), 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, (q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1), 0, (-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1)]
theorem cGL_2_8_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_8_v11 q) = cGL_2_8_v12 q := by
  rw [bridge2_0]; unfold cGL_2_8_v11 cGL_2_8_v12; stepTac
def cGL_2_8_v13 (q : R) : Fin 15 → R := ![0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^7), ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((-q^8 + 3*q^6 - 4*q^4 + 3*q^2 - 1) / q^7), 0, ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^4), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), (-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q)]
theorem cGL_2_8_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_8_v12 q) = cGL_2_8_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_8_v12 cGL_2_8_v13; stepTac
def cGL_2_8_v14 (q : R) : Fin 15 → R := ![0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^6), ((q^14 - 5*q^12 + 12*q^10 - 18*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^9), ((q^12 - 4*q^10 + 9*q^8 - 12*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^3), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^6), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), 0, 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^2), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), (q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1)]
theorem cGL_2_8_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_8_v13 q) = cGL_2_8_v14 q := by
  rw [bridge2_0]; unfold cGL_2_8_v13 cGL_2_8_v14; stepTac
theorem cGL_2_8_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 8 1) = cGL_2_8_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_8_v0_step q hq, cGL_2_8_v1_step q hq, cGL_2_8_v2_step q hq, cGL_2_8_v3_step q hq, cGL_2_8_v4_step q hq, cGL_2_8_v5_step q hq, cGL_2_8_v6_step q hq, cGL_2_8_v7_step q hq, cGL_2_8_v8_step q hq, cGL_2_8_v9_step q hq, cGL_2_8_v10_step q hq, cGL_2_8_v11_step q hq, cGL_2_8_v12_step q hq, cGL_2_8_v13_step q hq, cGL_2_8_v14_step q hq]
theorem cGL_2_8_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 8 8 = ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 8 8, cGL_2_8_col q hq]; simp [cGL_2_8_v14]

def cGL_2_9_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0, 0]
theorem cGL_2_9_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 9 1) = cGL_2_9_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_9_v0; stepTac
def cGL_2_9_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (1), 0, 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0]
theorem cGL_2_9_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_9_v0 q) = cGL_2_9_v1 q := by
  rw [bridge2_2]; unfold cGL_2_9_v0 cGL_2_9_v1; stepTac
def cGL_2_9_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((1) / q), (-q^2 + 1), 0, 0, ((q^4 - 2*q^2 + 1) / q), 0, 0, 0, 0, 0]
theorem cGL_2_9_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_9_v1 q) = cGL_2_9_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_9_v1 cGL_2_9_v2; stepTac
def cGL_2_9_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((1) / q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0]
theorem cGL_2_9_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_9_v2 q) = cGL_2_9_v3 q := by
  rw [bridge2_2]; unfold cGL_2_9_v2 cGL_2_9_v3; stepTac
def cGL_2_9_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), (q^4 - 2*q^2 + 1), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 2) / q), 0, 0, 0, 0, 0]
theorem cGL_2_9_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_9_v3 q) = cGL_2_9_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_9_v3 cGL_2_9_v4; stepTac
def cGL_2_9_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0, 0, 0]
theorem cGL_2_9_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_9_v4 q) = cGL_2_9_v5 q := by
  rw [bridge2_2]; unfold cGL_2_9_v4 cGL_2_9_v5; stepTac
def cGL_2_9_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0]
theorem cGL_2_9_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_9_v5 q) = cGL_2_9_v6 q := by
  rw [bridge2_3]; unfold cGL_2_9_v5 cGL_2_9_v6; stepTac
def cGL_2_9_v7 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0]
theorem cGL_2_9_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_9_v6 q) = cGL_2_9_v7 q := by
  rw [bridge2_4]; unfold cGL_2_9_v6 cGL_2_9_v7; stepTac
def cGL_2_9_v8 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_9_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_9_v7 q) = cGL_2_9_v8 q := by
  rw [bridge2_3]; unfold cGL_2_9_v7 cGL_2_9_v8; stepTac
def cGL_2_9_v9 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0, 0, 0]
theorem cGL_2_9_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_9_v8 q) = cGL_2_9_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_9_v8 cGL_2_9_v9; stepTac
def cGL_2_9_v10 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^4), ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0, 0]
theorem cGL_2_9_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_9_v9 q) = cGL_2_9_v10 q := by
  rw [bridge2_0]; unfold cGL_2_9_v9 cGL_2_9_v10; stepTac
def cGL_2_9_v11 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^4), ((q^14 - 5*q^12 + 11*q^10 - 16*q^8 + 17*q^6 - 12*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^3), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0, 0]
theorem cGL_2_9_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_9_v10 q) = cGL_2_9_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_9_v10 cGL_2_9_v11; stepTac
def cGL_2_9_v12 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^3), ((q^16 - 6*q^14 + 15*q^12 - 24*q^10 + 29*q^8 - 24*q^6 + 14*q^4 - 5*q^2 + 1) / q^6), ((q^14 - 5*q^12 + 11*q^10 - 16*q^8 + 17*q^6 - 12*q^4 + 5*q^2 - 1) / q^5), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^2), ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0, 0, 0, 0, 0]
theorem cGL_2_9_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_9_v11 q) = cGL_2_9_v12 q := by
  rw [bridge2_0]; unfold cGL_2_9_v11 cGL_2_9_v12; stepTac
def cGL_2_9_v13 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((q^16 - 6*q^14 + 15*q^12 - 24*q^10 + 29*q^8 - 24*q^6 + 14*q^4 - 5*q^2 + 1) / q^6), ((-q^18 + 6*q^16 - 17*q^14 + 32*q^12 - 44*q^10 + 45*q^8 - 34*q^6 + 18*q^4 - 6*q^2 + 1) / q^7), ((q^14 - 5*q^12 + 11*q^10 - 16*q^8 + 17*q^6 - 12*q^4 + 5*q^2 - 1) / q^6), 0, ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^5), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0, 0, 0, 0, 0]
theorem cGL_2_9_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_9_v12 q) = cGL_2_9_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_9_v12 cGL_2_9_v13; stepTac
def cGL_2_9_v14 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, ((q^16 - 6*q^14 + 15*q^12 - 24*q^10 + 29*q^8 - 24*q^6 + 14*q^4 - 5*q^2 + 1) / q^5), ((-q^20 + 7*q^18 - 22*q^16 + 44*q^14 - 65*q^12 + 73*q^10 - 62*q^8 + 40*q^6 - 19*q^4 + 6*q^2 - 1) / q^8), ((-q^18 + 6*q^16 - 17*q^14 + 32*q^12 - 44*q^10 + 45*q^8 - 34*q^6 + 18*q^4 - 6*q^2 + 1) / q^7), 0, ((q^10 - 5*q^8 + 9*q^6 - 8*q^4 + 4*q^2 - 1) / q^4), ((-q^14 + 6*q^12 - 15*q^10 + 21*q^8 - 19*q^6 + 12*q^4 - 5*q^2 + 1) / q^7), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), 0, 0, 0, 0, 0, 0]
theorem cGL_2_9_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_9_v13 q) = cGL_2_9_v14 q := by
  rw [bridge2_0]; unfold cGL_2_9_v13 cGL_2_9_v14; stepTac
theorem cGL_2_9_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 9 1) = cGL_2_9_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_9_v0_step q hq, cGL_2_9_v1_step q hq, cGL_2_9_v2_step q hq, cGL_2_9_v3_step q hq, cGL_2_9_v4_step q hq, cGL_2_9_v5_step q hq, cGL_2_9_v6_step q hq, cGL_2_9_v7_step q hq, cGL_2_9_v8_step q hq, cGL_2_9_v9_step q hq, cGL_2_9_v10_step q hq, cGL_2_9_v11_step q hq, cGL_2_9_v12_step q hq, cGL_2_9_v13_step q hq, cGL_2_9_v14_step q hq]
theorem cGL_2_9_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 9 9 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 9 9, cGL_2_9_col q hq]; simp [cGL_2_9_v14]

def cGL_2_10_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0]
theorem cGL_2_10_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 10 1) = cGL_2_10_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_10_v0; stepTac
def cGL_2_10_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((-q^2 + 1) / q), 0, 0]
theorem cGL_2_10_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_10_v0 q) = cGL_2_10_v1 q := by
  rw [bridge2_2]; unfold cGL_2_10_v0 cGL_2_10_v1; stepTac
def cGL_2_10_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, ((-q^2 + 1) / q^2), 0, 0]
theorem cGL_2_10_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_10_v1 q) = cGL_2_10_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_10_v1 cGL_2_10_v2; stepTac
def cGL_2_10_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0]
theorem cGL_2_10_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_10_v2 q) = cGL_2_10_v3 q := by
  rw [bridge2_2]; unfold cGL_2_10_v2 cGL_2_10_v3; stepTac
def cGL_2_10_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0]
theorem cGL_2_10_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_10_v3 q) = cGL_2_10_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_10_v3 cGL_2_10_v4; stepTac
def cGL_2_10_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGL_2_10_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_10_v4 q) = cGL_2_10_v5 q := by
  rw [bridge2_2]; unfold cGL_2_10_v4 cGL_2_10_v5; stepTac
def cGL_2_10_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0]
theorem cGL_2_10_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_10_v5 q) = cGL_2_10_v6 q := by
  rw [bridge2_3]; unfold cGL_2_10_v5 cGL_2_10_v6; stepTac
def cGL_2_10_v7 (q : R) : Fin 15 → R := ![0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), 0, 0]
theorem cGL_2_10_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_10_v6 q) = cGL_2_10_v7 q := by
  rw [bridge2_4]; unfold cGL_2_10_v6 cGL_2_10_v7; stepTac
def cGL_2_10_v8 (q : R) : Fin 15 → R := ![0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, 0, 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^2), 0, 0]
theorem cGL_2_10_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_10_v7 q) = cGL_2_10_v8 q := by
  rw [bridge2_3]; unfold cGL_2_10_v7 cGL_2_10_v8; stepTac
def cGL_2_10_v9 (q : R) : Fin 15 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^3), 0, 0, 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), 0, 0]
theorem cGL_2_10_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_10_v8 q) = cGL_2_10_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_10_v8 cGL_2_10_v9; stepTac
def cGL_2_10_v10 (q : R) : Fin 15 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^4), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^3), 0, 0, 0, ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), 0]
theorem cGL_2_10_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_10_v9 q) = cGL_2_10_v10 q := by
  rw [bridge2_0]; unfold cGL_2_10_v9 cGL_2_10_v10; stepTac
def cGL_2_10_v11 (q : R) : Fin 15 → R := ![0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^8), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^5), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), 0, 0, 0, ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^3)]
theorem cGL_2_10_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_10_v10 q) = cGL_2_10_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_10_v10 cGL_2_10_v11; stepTac
def cGL_2_10_v12 (q : R) : Fin 15 → R := ![0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^9), ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^8), 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^3), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^5), 0, 0, 0, ((-q^14 + 5*q^12 - 12*q^10 + 19*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^6), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^2)]
theorem cGL_2_10_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_10_v11 q) = cGL_2_10_v12 q := by
  rw [bridge2_0]; unfold cGL_2_10_v11 cGL_2_10_v12; stepTac
def cGL_2_10_v13 (q : R) : Fin 15 → R := ![0, 0, ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^9), ((-2*q^16 + 9*q^14 - 22*q^12 + 37*q^10 - 44*q^8 + 37*q^6 - 21*q^4 + 7*q^2 - 1) / q^10), ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^9), 0, ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^7), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^6), 0, 0, 0, ((-q^14 + 5*q^12 - 12*q^10 + 19*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^2), ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^5)]
theorem cGL_2_10_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_10_v12 q) = cGL_2_10_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_10_v12 cGL_2_10_v13; stepTac
def cGL_2_10_v14 (q : R) : Fin 15 → R := ![0, 0, ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^8), ((-2*q^18 + 11*q^16 - 29*q^14 + 52*q^12 - 66*q^10 + 63*q^8 - 44*q^6 + 22*q^4 - 7*q^2 + 1) / q^11), ((-2*q^16 + 9*q^14 - 22*q^12 + 37*q^10 - 44*q^8 + 37*q^6 - 21*q^4 + 7*q^2 - 1) / q^10), 0, ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^5), ((-q^20 + 7*q^18 - 23*q^16 + 49*q^14 - 75*q^12 + 86*q^10 - 75*q^8 + 49*q^6 - 23*q^4 + 7*q^2 - 1) / q^8), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^7), 0, 0, 0, ((-2*q^16 + 9*q^14 - 22*q^12 + 37*q^10 - 44*q^8 + 37*q^6 - 21*q^4 + 7*q^2 - 1) / q^8), ((-q^14 + 5*q^12 - 12*q^10 + 19*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^4)]
theorem cGL_2_10_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_10_v13 q) = cGL_2_10_v14 q := by
  rw [bridge2_0]; unfold cGL_2_10_v13 cGL_2_10_v14; stepTac
theorem cGL_2_10_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 10 1) = cGL_2_10_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_10_v0_step q hq, cGL_2_10_v1_step q hq, cGL_2_10_v2_step q hq, cGL_2_10_v3_step q hq, cGL_2_10_v4_step q hq, cGL_2_10_v5_step q hq, cGL_2_10_v6_step q hq, cGL_2_10_v7_step q hq, cGL_2_10_v8_step q hq, cGL_2_10_v9_step q hq, cGL_2_10_v10_step q hq, cGL_2_10_v11_step q hq, cGL_2_10_v12_step q hq, cGL_2_10_v13_step q hq, cGL_2_10_v14_step q hq]
theorem cGL_2_10_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 10 10 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 10 10, cGL_2_10_col q hq]; simp [cGL_2_10_v14]

def cGL_2_11_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0]
theorem cGL_2_11_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 11 1) = cGL_2_11_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_11_v0; stepTac
def cGL_2_11_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, (q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((-q^2 + 1) / q), 0]
theorem cGL_2_11_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_11_v0 q) = cGL_2_11_v1 q := by
  rw [bridge2_2]; unfold cGL_2_11_v0 cGL_2_11_v1; stepTac
def cGL_2_11_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, ((-q^2 + 1) / q^2), 0]
theorem cGL_2_11_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_11_v1 q) = cGL_2_11_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_11_v1 cGL_2_11_v2; stepTac
def cGL_2_11_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0]
theorem cGL_2_11_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_11_v2 q) = cGL_2_11_v3 q := by
  rw [bridge2_2]; unfold cGL_2_11_v2 cGL_2_11_v3; stepTac
def cGL_2_11_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0]
theorem cGL_2_11_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGL_2_11_v3 q) = cGL_2_11_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGL_2_11_v3 cGL_2_11_v4; stepTac
def cGL_2_11_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0]
theorem cGL_2_11_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGL_2_11_v4 q) = cGL_2_11_v5 q := by
  rw [bridge2_2]; unfold cGL_2_11_v4 cGL_2_11_v5; stepTac
def cGL_2_11_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0]
theorem cGL_2_11_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_11_v5 q) = cGL_2_11_v6 q := by
  rw [bridge2_3]; unfold cGL_2_11_v5 cGL_2_11_v6; stepTac
def cGL_2_11_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), 0]
theorem cGL_2_11_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, false)).mulVec (cGL_2_11_v6 q) = cGL_2_11_v7 q := by
  rw [bridge2_4]; unfold cGL_2_11_v6 cGL_2_11_v7; stepTac
def cGL_2_11_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, 0, 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^2), 0]
theorem cGL_2_11_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGL_2_11_v7 q) = cGL_2_11_v8 q := by
  rw [bridge2_3]; unfold cGL_2_11_v7 cGL_2_11_v8; stepTac
def cGL_2_11_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^2)]
theorem cGL_2_11_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_11_v8 q) = cGL_2_11_v9 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_11_v8 cGL_2_11_v9; stepTac
def cGL_2_11_v10 (q : R) : Fin 15 → R := ![0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, 0, 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q)]
theorem cGL_2_11_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_11_v9 q) = cGL_2_11_v10 q := by
  rw [bridge2_0]; unfold cGL_2_11_v9 cGL_2_11_v10; stepTac
def cGL_2_11_v11 (q : R) : Fin 15 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), 0, 0, 0, 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q), ((q^12 - 4*q^10 + 8*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^2)]
theorem cGL_2_11_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_11_v10 q) = cGL_2_11_v11 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_11_v10 cGL_2_11_v11; stepTac
def cGL_2_11_v12 (q : R) : Fin 15 → R := ![0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), 0, 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q), 0, ((q^12 - 4*q^10 + 8*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q)]
theorem cGL_2_11_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_11_v11 q) = cGL_2_11_v12 q := by
  rw [bridge2_0]; unfold cGL_2_11_v11 cGL_2_11_v12; stepTac
def cGL_2_11_v13 (q : R) : Fin 15 → R := ![0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^9), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^8), 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^6), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^5), 0, 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^2), ((q^12 - 4*q^10 + 8*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q), ((-q^14 + 5*q^12 - 12*q^10 + 19*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^2)]
theorem cGL_2_11_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, true)).mulVec (cGL_2_11_v12 q) = cGL_2_11_v13 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_1]; unfold cGL_2_11_v12 cGL_2_11_v13; stepTac
def cGL_2_11_v14 (q : R) : Fin 15 → R := ![0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^10), ((2*q^12 - 7*q^10 + 15*q^8 - 18*q^6 + 14*q^4 - 6*q^2 + 1) / q^9), 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^7), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^6), 0, 0, 0, ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^3), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^2), ((-q^14 + 5*q^12 - 12*q^10 + 19*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q)]
theorem cGL_2_11_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGL_2_11_v13 q) = cGL_2_11_v14 q := by
  rw [bridge2_0]; unfold cGL_2_11_v13 cGL_2_11_v14; stepTac
theorem cGL_2_11_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGL).mulVec (Pi.single 11 1) = cGL_2_11_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_2_11_v0_step q hq, cGL_2_11_v1_step q hq, cGL_2_11_v2_step q hq, cGL_2_11_v3_step q hq, cGL_2_11_v4_step q hq, cGL_2_11_v5_step q hq, cGL_2_11_v6_step q hq, cGL_2_11_v7_step q hq, cGL_2_11_v8_step q hq, cGL_2_11_v9_step q hq, cGL_2_11_v10_step q hq, cGL_2_11_v11_step q hq, cGL_2_11_v12_step q hq, cGL_2_11_v13_step q hq, cGL_2_11_v14_step q hq]
theorem cGL_2_11_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGL 11 11 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGL) 11 11, cGL_2_11_col q hq]; simp [cGL_2_11_v14]

def cGL_1_3_v0 (q : R) : Fin 6 → R := ![0, 0, 0, ((1) / q), 0, 0]
theorem cGL_1_3_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (Pi.single 3 1) = cGL_1_3_v0 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGL_1_3_v0; stepTac
def cGL_1_3_v1 (q : R) : Fin 6 → R := ![0, 0, ((1) / q), 0, 0, 0]
theorem cGL_1_3_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGL_1_3_v0 q) = cGL_1_3_v1 q := by
  rw [bridge1_2]; unfold cGL_1_3_v0 cGL_1_3_v1; stepTac
def cGL_1_3_v2 (q : R) : Fin 6 → R := ![0, ((1) / q), ((-q^2 + 1) / q^2), 0, 0, 0]
theorem cGL_1_3_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGL_1_3_v1 q) = cGL_1_3_v2 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGL_1_3_v1 cGL_1_3_v2; stepTac
def cGL_1_3_v3 (q : R) : Fin 6 → R := ![0, (1), ((-q^4 + 2*q^2 - 1) / q^3), ((-q^2 + 1) / q^2), 0, 0]
theorem cGL_1_3_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGL_1_3_v2 q) = cGL_1_3_v3 q := by
  rw [bridge1_2]; unfold cGL_1_3_v2 cGL_1_3_v3; stepTac
def cGL_1_3_v4 (q : R) : Fin 6 → R := ![0, ((-q^4 + 2*q^2 - 1) / q^3), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), ((-q^2 + 1) / q^3), 0, 0]
theorem cGL_1_3_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGL_1_3_v3 q) = cGL_1_3_v4 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGL_1_3_v3 cGL_1_3_v4; stepTac
def cGL_1_3_v5 (q : R) : Fin 6 → R := ![0, ((-q^4 + 2*q^2 - 1) / q^2), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0]
theorem cGL_1_3_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGL_1_3_v4 q) = cGL_1_3_v5 q := by
  rw [bridge1_2]; unfold cGL_1_3_v4 cGL_1_3_v5; stepTac
def cGL_1_3_v6 (q : R) : Fin 6 → R := ![0, ((q^4 - 2*q^2 + 1) / q^5), ((-q^4 + 2*q^2 - 1) / q^2), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0]
theorem cGL_1_3_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGL_1_3_v5 q) = cGL_1_3_v6 q := by
  rw [bridge1_3]; unfold cGL_1_3_v5 cGL_1_3_v6; stepTac
def cGL_1_3_v7 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / q^5), 0, ((-q^4 + 2*q^2 - 1) / q), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^2), 0, 0]
theorem cGL_1_3_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, false)).mulVec (cGL_1_3_v6 q) = cGL_1_3_v7 q := by
  rw [bridge1_4]; unfold cGL_1_3_v6 cGL_1_3_v7; stepTac
def cGL_1_3_v8 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q), 0, 0]
theorem cGL_1_3_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGL_1_3_v7 q) = cGL_1_3_v8 q := by
  rw [bridge1_3]; unfold cGL_1_3_v7 cGL_1_3_v8; stepTac
def cGL_1_3_v9 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / q^5), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q), 0]
theorem cGL_1_3_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, true)).mulVec (cGL_1_3_v8 q) = cGL_1_3_v9 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_1]; unfold cGL_1_3_v8 cGL_1_3_v9; stepTac
def cGL_1_3_v10 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q), 0, 0, ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^2), ((q^6 - 2*q^4 + 3*q^2 - 1) / q)]
theorem cGL_1_3_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGL_1_3_v9 q) = cGL_1_3_v10 q := by
  rw [bridge1_0]; unfold cGL_1_3_v9 cGL_1_3_v10; stepTac
def cGL_1_3_v11 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / q^5), ((-q^4 + 2*q^2 - 1) / q^2), 0, ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^2), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^3), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^2)]
theorem cGL_1_3_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, true)).mulVec (cGL_1_3_v10 q) = cGL_1_3_v11 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_1]; unfold cGL_1_3_v10 cGL_1_3_v11; stepTac
def cGL_1_3_v12 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q), 0, ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^3)]
theorem cGL_1_3_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGL_1_3_v11 q) = cGL_1_3_v12 q := by
  rw [bridge1_0]; unfold cGL_1_3_v11 cGL_1_3_v12; stepTac
def cGL_1_3_v13 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / q^5), ((-q^4 + 2*q^2 - 1) / q^2), 0, ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^5), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^4)]
theorem cGL_1_3_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, true)).mulVec (cGL_1_3_v12 q) = cGL_1_3_v13 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_1]; unfold cGL_1_3_v12 cGL_1_3_v13; stepTac
def cGL_1_3_v14 (q : R) : Fin 6 → R := ![((q^4 - 2*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q), 0, ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^3), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 35*q^8 - 28*q^6 + 16*q^4 - 6*q^2 + 1) / q^6), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^5)]
theorem cGL_1_3_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGL_1_3_v13 q) = cGL_1_3_v14 q := by
  rw [bridge1_0]; unfold cGL_1_3_v13 cGL_1_3_v14; stepTac
theorem cGL_1_3_col (q : R) (hq : q ≠ 0) :
    (wordW q idx1 wGL).mulVec (Pi.single 3 1) = cGL_1_3_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_1_3_v0_step q hq, cGL_1_3_v1_step q hq, cGL_1_3_v2_step q hq, cGL_1_3_v3_step q hq, cGL_1_3_v4_step q hq, cGL_1_3_v5_step q hq, cGL_1_3_v6_step q hq, cGL_1_3_v7_step q hq, cGL_1_3_v8_step q hq, cGL_1_3_v9_step q hq, cGL_1_3_v10_step q hq, cGL_1_3_v11_step q hq, cGL_1_3_v12_step q hq, cGL_1_3_v13_step q hq, cGL_1_3_v14_step q hq]
theorem cGL_1_3_entry (q : R) (hq : q ≠ 0) :
    wordW q idx1 wGL 3 3 = ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx1 wGL) 3 3, cGL_1_3_col q hq]; simp [cGL_1_3_v14]

def cGL_1_4_v0 (q : R) : Fin 6 → R := ![0, 0, 0, 0, ((1) / q), 0]
theorem cGL_1_4_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (Pi.single 4 1) = cGL_1_4_v0 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGL_1_4_v0; stepTac
def cGL_1_4_v1 (q : R) : Fin 6 → R := ![0, 0, 0, 0, (1), 0]
theorem cGL_1_4_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGL_1_4_v0 q) = cGL_1_4_v1 q := by
  rw [bridge1_2]; unfold cGL_1_4_v0 cGL_1_4_v1; stepTac
def cGL_1_4_v2 (q : R) : Fin 6 → R := ![0, 0, 0, 0, ((1) / q), 0]
theorem cGL_1_4_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGL_1_4_v1 q) = cGL_1_4_v2 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGL_1_4_v1 cGL_1_4_v2; stepTac
def cGL_1_4_v3 (q : R) : Fin 6 → R := ![0, 0, 0, 0, (1), 0]
theorem cGL_1_4_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGL_1_4_v2 q) = cGL_1_4_v3 q := by
  rw [bridge1_2]; unfold cGL_1_4_v2 cGL_1_4_v3; stepTac
def cGL_1_4_v4 (q : R) : Fin 6 → R := ![0, 0, 0, 0, ((1) / q), 0]
theorem cGL_1_4_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGL_1_4_v3 q) = cGL_1_4_v4 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGL_1_4_v3 cGL_1_4_v4; stepTac
def cGL_1_4_v5 (q : R) : Fin 6 → R := ![0, 0, 0, 0, (1), 0]
theorem cGL_1_4_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGL_1_4_v4 q) = cGL_1_4_v5 q := by
  rw [bridge1_2]; unfold cGL_1_4_v4 cGL_1_4_v5; stepTac
def cGL_1_4_v6 (q : R) : Fin 6 → R := ![0, 0, 0, 0, (q), 0]
theorem cGL_1_4_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGL_1_4_v5 q) = cGL_1_4_v6 q := by
  rw [bridge1_3]; unfold cGL_1_4_v5 cGL_1_4_v6; stepTac
def cGL_1_4_v7 (q : R) : Fin 6 → R := ![0, 0, 0, 0, (q^2), 0]
theorem cGL_1_4_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, false)).mulVec (cGL_1_4_v6 q) = cGL_1_4_v7 q := by
  rw [bridge1_4]; unfold cGL_1_4_v6 cGL_1_4_v7; stepTac
def cGL_1_4_v8 (q : R) : Fin 6 → R := ![0, 0, 0, 0, (q^3), 0]
theorem cGL_1_4_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGL_1_4_v7 q) = cGL_1_4_v8 q := by
  rw [bridge1_3]; unfold cGL_1_4_v7 cGL_1_4_v8; stepTac
def cGL_1_4_v9 (q : R) : Fin 6 → R := ![0, 0, 0, (q^3), (-q^4 + q^2), 0]
theorem cGL_1_4_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, true)).mulVec (cGL_1_4_v8 q) = cGL_1_4_v9 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_1]; unfold cGL_1_4_v8 cGL_1_4_v9; stepTac
def cGL_1_4_v10 (q : R) : Fin 6 → R := ![0, 0, 0, (q^4), (-q^5 + 2*q^3 - q), (-q^4 + q^2)]
theorem cGL_1_4_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGL_1_4_v9 q) = cGL_1_4_v10 q := by
  rw [bridge1_0]; unfold cGL_1_4_v9 cGL_1_4_v10; stepTac
def cGL_1_4_v11 (q : R) : Fin 6 → R := ![0, 0, 0, (-q^5 + 2*q^3 - q), (q^6 - 2*q^4 + 3*q^2 - 1), (-q^3 + q)]
theorem cGL_1_4_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, true)).mulVec (cGL_1_4_v10 q) = cGL_1_4_v11 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_1]; unfold cGL_1_4_v10 cGL_1_4_v11; stepTac
def cGL_1_4_v12 (q : R) : Fin 6 → R := ![0, 0, 0, (-q^6 + 2*q^4 - q^2), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), (q^6 - 2*q^4 + 3*q^2 - 1)]
theorem cGL_1_4_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGL_1_4_v11 q) = cGL_1_4_v12 q := by
  rw [bridge1_0]; unfold cGL_1_4_v11 cGL_1_4_v12; stepTac
def cGL_1_4_v13 (q : R) : Fin 6 → R := ![0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^2), ((q^6 - 2*q^4 + 3*q^2 - 1) / q)]
theorem cGL_1_4_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, true)).mulVec (cGL_1_4_v12 q) = cGL_1_4_v13 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_1]; unfold cGL_1_4_v12 cGL_1_4_v13; stepTac
def cGL_1_4_v14 (q : R) : Fin 6 → R := ![0, 0, 0, (q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1), ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^2)]
theorem cGL_1_4_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGL_1_4_v13 q) = cGL_1_4_v14 q := by
  rw [bridge1_0]; unfold cGL_1_4_v13 cGL_1_4_v14; stepTac
theorem cGL_1_4_col (q : R) (hq : q ≠ 0) :
    (wordW q idx1 wGL).mulVec (Pi.single 4 1) = cGL_1_4_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_1_4_v0_step q hq, cGL_1_4_v1_step q hq, cGL_1_4_v2_step q hq, cGL_1_4_v3_step q hq, cGL_1_4_v4_step q hq, cGL_1_4_v5_step q hq, cGL_1_4_v6_step q hq, cGL_1_4_v7_step q hq, cGL_1_4_v8_step q hq, cGL_1_4_v9_step q hq, cGL_1_4_v10_step q hq, cGL_1_4_v11_step q hq, cGL_1_4_v12_step q hq, cGL_1_4_v13_step q hq, cGL_1_4_v14_step q hq]
theorem cGL_1_4_entry (q : R) (hq : q ≠ 0) :
    wordW q idx1 wGL 4 4 = ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx1 wGL) 4 4, cGL_1_4_col q hq]; simp [cGL_1_4_v14]

def cGL_1_5_v0 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, ((1) / q)]
theorem cGL_1_5_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (Pi.single 5 1) = cGL_1_5_v0 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGL_1_5_v0; stepTac
def cGL_1_5_v1 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, (1)]
theorem cGL_1_5_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGL_1_5_v0 q) = cGL_1_5_v1 q := by
  rw [bridge1_2]; unfold cGL_1_5_v0 cGL_1_5_v1; stepTac
def cGL_1_5_v2 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, ((1) / q)]
theorem cGL_1_5_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGL_1_5_v1 q) = cGL_1_5_v2 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGL_1_5_v1 cGL_1_5_v2; stepTac
def cGL_1_5_v3 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, (1)]
theorem cGL_1_5_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGL_1_5_v2 q) = cGL_1_5_v3 q := by
  rw [bridge1_2]; unfold cGL_1_5_v2 cGL_1_5_v3; stepTac
def cGL_1_5_v4 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, ((1) / q)]
theorem cGL_1_5_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGL_1_5_v3 q) = cGL_1_5_v4 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGL_1_5_v3 cGL_1_5_v4; stepTac
def cGL_1_5_v5 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, (1)]
theorem cGL_1_5_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGL_1_5_v4 q) = cGL_1_5_v5 q := by
  rw [bridge1_2]; unfold cGL_1_5_v4 cGL_1_5_v5; stepTac
def cGL_1_5_v6 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, (q)]
theorem cGL_1_5_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGL_1_5_v5 q) = cGL_1_5_v6 q := by
  rw [bridge1_3]; unfold cGL_1_5_v5 cGL_1_5_v6; stepTac
def cGL_1_5_v7 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, (q^2)]
theorem cGL_1_5_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, false)).mulVec (cGL_1_5_v6 q) = cGL_1_5_v7 q := by
  rw [bridge1_4]; unfold cGL_1_5_v6 cGL_1_5_v7; stepTac
def cGL_1_5_v8 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, (q^3)]
theorem cGL_1_5_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGL_1_5_v7 q) = cGL_1_5_v8 q := by
  rw [bridge1_3]; unfold cGL_1_5_v7 cGL_1_5_v8; stepTac
def cGL_1_5_v9 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, (q^2)]
theorem cGL_1_5_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, true)).mulVec (cGL_1_5_v8 q) = cGL_1_5_v9 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_1]; unfold cGL_1_5_v8 cGL_1_5_v9; stepTac
def cGL_1_5_v10 (q : R) : Fin 6 → R := ![0, 0, 0, 0, (q^2), 0]
theorem cGL_1_5_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGL_1_5_v9 q) = cGL_1_5_v10 q := by
  rw [bridge1_0]; unfold cGL_1_5_v9 cGL_1_5_v10; stepTac
def cGL_1_5_v11 (q : R) : Fin 6 → R := ![0, 0, 0, (q^2), (-q^3 + q), 0]
theorem cGL_1_5_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, true)).mulVec (cGL_1_5_v10 q) = cGL_1_5_v11 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_1]; unfold cGL_1_5_v10 cGL_1_5_v11; stepTac
def cGL_1_5_v12 (q : R) : Fin 6 → R := ![0, 0, 0, (q^3), (-q^4 + 2*q^2 - 1), (-q^3 + q)]
theorem cGL_1_5_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGL_1_5_v11 q) = cGL_1_5_v12 q := by
  rw [bridge1_0]; unfold cGL_1_5_v11 cGL_1_5_v12; stepTac
def cGL_1_5_v13 (q : R) : Fin 6 → R := ![0, 0, 0, (-q^4 + 2*q^2 - 1), ((q^6 - 2*q^4 + 3*q^2 - 1) / q), (-q^2 + 1)]
theorem cGL_1_5_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, true)).mulVec (cGL_1_5_v12 q) = cGL_1_5_v13 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_1]; unfold cGL_1_5_v12 cGL_1_5_v13; stepTac
def cGL_1_5_v14 (q : R) : Fin 6 → R := ![0, 0, 0, (-q^5 + 2*q^3 - q), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), ((q^6 - 2*q^4 + 3*q^2 - 1) / q)]
theorem cGL_1_5_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGL_1_5_v13 q) = cGL_1_5_v14 q := by
  rw [bridge1_0]; unfold cGL_1_5_v13 cGL_1_5_v14; stepTac
theorem cGL_1_5_col (q : R) (hq : q ≠ 0) :
    (wordW q idx1 wGL).mulVec (Pi.single 5 1) = cGL_1_5_v14 q := by
  simp only [wGL, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGL_1_5_v0_step q hq, cGL_1_5_v1_step q hq, cGL_1_5_v2_step q hq, cGL_1_5_v3_step q hq, cGL_1_5_v4_step q hq, cGL_1_5_v5_step q hq, cGL_1_5_v6_step q hq, cGL_1_5_v7_step q hq, cGL_1_5_v8_step q hq, cGL_1_5_v9_step q hq, cGL_1_5_v10_step q hq, cGL_1_5_v11_step q hq, cGL_1_5_v12_step q hq, cGL_1_5_v13_step q hq, cGL_1_5_v14_step q hq]
theorem cGL_1_5_entry (q : R) (hq : q ≠ 0) :
    wordW q idx1 wGL 5 5 = ((q^6 - 2*q^4 + 3*q^2 - 1) / q) := by
  rw [entry_eq_mulVec_single (wordW q idx1 wGL) 5 5, cGL_1_5_col q hq]; simp [cGL_1_5_v14]

/-- **`S` for `(σ₀σ₁⁻¹)³ · σ₃σ₄σ₃ · (σ₂σ₃⁻¹)³`, proton on strands `0–2` (bond `G`, ruled form).** -/
theorem S_GL (q : R) (hq : q ≠ 0) :
    Fp64 [0, 1, 2] (word64 q wGL) + Fm64 [0, 1, 2] (word64 q wGL) = -(4 * q * (q - q⁻¹) ^ 4) := by
  rw [Fp_L_reduction, Fm_L_reduction, cGL_5_0_entry q hq, cGL_5_1_entry q hq, cGL_5_2_entry q hq, cGL_4_3_entry q hq, cGL_4_4_entry q hq, cGL_4_5_entry q hq, cGL_4_6_entry q hq, cGL_4_7_entry q hq, cGL_4_8_entry q hq, cGL_4_10_entry q hq, cGL_4_11_entry q hq, cGL_4_12_entry q hq, cGL_2_12_entry q hq, cGL_2_13_entry q hq, cGL_2_14_entry q hq, cGL_4_0_entry q hq, cGL_4_1_entry q hq, cGL_4_2_entry q hq, cGL_2_2_entry q hq, cGL_2_3_entry q hq, cGL_2_4_entry q hq, cGL_2_6_entry q hq, cGL_2_7_entry q hq, cGL_2_8_entry q hq, cGL_2_9_entry q hq, cGL_2_10_entry q hq, cGL_2_11_entry q hq, cGL_1_3_entry q hq, cGL_1_4_entry q hq, cGL_1_5_entry q hq]
  field_simp; ring

theorem Fp_GL_at_one : Fp64 [0, 1, 2] (word64 (1 : R) wGL) = 6 := by
  rw [Fp_L_reduction, cGL_5_0_entry 1 one_ne_zero, cGL_5_1_entry 1 one_ne_zero, cGL_5_2_entry 1 one_ne_zero, cGL_4_3_entry 1 one_ne_zero, cGL_4_4_entry 1 one_ne_zero, cGL_4_5_entry 1 one_ne_zero, cGL_4_6_entry 1 one_ne_zero, cGL_4_7_entry 1 one_ne_zero, cGL_4_8_entry 1 one_ne_zero, cGL_4_10_entry 1 one_ne_zero, cGL_4_11_entry 1 one_ne_zero, cGL_4_12_entry 1 one_ne_zero, cGL_2_12_entry 1 one_ne_zero, cGL_2_13_entry 1 one_ne_zero, cGL_2_14_entry 1 one_ne_zero]; norm_num

theorem Fm_GL_at_one : Fm64 [0, 1, 2] (word64 (1 : R) wGL) = -6 := by
  rw [Fm_L_reduction, cGL_4_0_entry 1 one_ne_zero, cGL_4_1_entry 1 one_ne_zero, cGL_4_2_entry 1 one_ne_zero, cGL_2_2_entry 1 one_ne_zero, cGL_2_3_entry 1 one_ne_zero, cGL_2_4_entry 1 one_ne_zero, cGL_2_6_entry 1 one_ne_zero, cGL_2_7_entry 1 one_ne_zero, cGL_2_8_entry 1 one_ne_zero, cGL_2_9_entry 1 one_ne_zero, cGL_2_10_entry 1 one_ne_zero, cGL_2_11_entry 1 one_ne_zero, cGL_1_3_entry 1 one_ne_zero, cGL_1_4_entry 1 one_ne_zero, cGL_1_5_entry 1 one_ne_zero]; norm_num

end QOU.BraidsAndKnots.BondChiralitySixStrand
