import BraidKnotOctonion.BondChiralitySixStrand.Core

/-!
# Bond chirality on six strands: `σ₀σ₁σ₀ · (σ₃σ₄⁻¹)³ · (σ₂σ₃⁻¹)³`, proton on strands `3–5` (bond `G`, ruled form)

The weight-space columns needed by `F(O₊)` and `F(O₋)` (mulVec chains, one step per letter),
then `S = F(O₊) + F(O₋)` on the full 64-dimensional space and `F(O±)` at `q = 1`.
Setup and conventions: `BondChiralitySixStrand.Core`.
-/

namespace QOU.BraidsAndKnots.BondChiralitySixStrand

open Matrix

variable {R : Type*} [Field R]

set_option linter.unusedVariables false
set_option maxHeartbeats 1000000

/-- `σ₀σ₁σ₀ · (σ₃σ₄⁻¹)³ · (σ₂σ₃⁻¹)³`, proton on strands `3–5` (bond `G`, ruled form). -/
def wGR : List Letter := [(0, false), (1, false), (0, false), (3, false), (4, true), (3, false), (4, true), (3, false), (4, true), (2, false), (3, true), (2, false), (3, true), (2, false), (3, true)]

def cGR_5_3_v0 (q : R) : Fin 6 → R := ![0, 0, 0, 0, (1), 0]
theorem cGR_5_3_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (Pi.single 3 1) = cGR_5_3_v0 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGR_5_3_v0; stepTac
def cGR_5_3_v1 (q : R) : Fin 6 → R := ![0, 0, 0, 0, (q), 0]
theorem cGR_5_3_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGR_5_3_v0 q) = cGR_5_3_v1 q := by
  rw [bridge5_2]; unfold cGR_5_3_v0 cGR_5_3_v1; stepTac
def cGR_5_3_v2 (q : R) : Fin 6 → R := ![0, 0, 0, (q), (-q^2 + 1), 0]
theorem cGR_5_3_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGR_5_3_v1 q) = cGR_5_3_v2 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGR_5_3_v1 cGR_5_3_v2; stepTac
def cGR_5_3_v3 (q : R) : Fin 6 → R := ![0, 0, (q), 0, (-q^3 + q), 0]
theorem cGR_5_3_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGR_5_3_v2 q) = cGR_5_3_v3 q := by
  rw [bridge5_2]; unfold cGR_5_3_v2 cGR_5_3_v3; stepTac
def cGR_5_3_v4 (q : R) : Fin 6 → R := ![0, 0, (1), (-q^3 + q), (q^4 - 2*q^2 + 1), 0]
theorem cGR_5_3_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGR_5_3_v3 q) = cGR_5_3_v4 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGR_5_3_v3 cGR_5_3_v4; stepTac
def cGR_5_3_v5 (q : R) : Fin 6 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q), (1), (q^5 - 2*q^3 + q), 0]
theorem cGR_5_3_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGR_5_3_v4 q) = cGR_5_3_v5 q := by
  rw [bridge5_2]; unfold cGR_5_3_v4 cGR_5_3_v5; stepTac
def cGR_5_3_v6 (q : R) : Fin 6 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((1) / q), 0, (q^5 - 2*q^3 + q)]
theorem cGR_5_3_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, true)).mulVec (cGR_5_3_v5 q) = cGR_5_3_v6 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_4]; unfold cGR_5_3_v5 cGR_5_3_v6; stepTac
def cGR_5_3_v7 (q : R) : Fin 6 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q), ((q^2 - 1) / q^2), ((1) / q), (q^6 - 2*q^4 + q^2)]
theorem cGR_5_3_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGR_5_3_v6 q) = cGR_5_3_v7 q := by
  rw [bridge5_3]; unfold cGR_5_3_v6 cGR_5_3_v7; stepTac
def cGR_5_3_v8 (q : R) : Fin 6 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((q^2 - 1) / q^3), (q^6 - 2*q^4 + q^2), ((-q^8 + 3*q^6 - 3*q^4 + q^2 + 1) / q)]
theorem cGR_5_3_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, true)).mulVec (cGR_5_3_v7 q) = cGR_5_3_v8 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_4]; unfold cGR_5_3_v7 cGR_5_3_v8; stepTac
def cGR_5_3_v9 (q : R) : Fin 6 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q), ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^4), ((q^2 - 1) / q^3), (-q^8 + 3*q^6 - 3*q^4 + q^2 + 1)]
theorem cGR_5_3_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGR_5_3_v8 q) = cGR_5_3_v9 q := by
  rw [bridge5_3]; unfold cGR_5_3_v8 cGR_5_3_v9; stepTac
def cGR_5_3_v10 (q : R) : Fin 6 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^5), (-q^8 + 3*q^6 - 3*q^4 + q^2 + 1), ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q^3)]
theorem cGR_5_3_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, true)).mulVec (cGR_5_3_v9 q) = cGR_5_3_v10 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_4]; unfold cGR_5_3_v9 cGR_5_3_v10; stepTac
def cGR_5_3_v11 (q : R) : Fin 6 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q), ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^5), ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q^2)]
theorem cGR_5_3_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGR_5_3_v10 q) = cGR_5_3_v11 q := by
  rw [bridge5_3]; unfold cGR_5_3_v10 cGR_5_3_v11; stepTac
def cGR_5_3_v12 (q : R) : Fin 6 → R := ![0, 0, (-q^4 + 2*q^2 - 1), ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^4), ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q)]
theorem cGR_5_3_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGR_5_3_v11 q) = cGR_5_3_v12 q := by
  rw [bridge5_0]; unfold cGR_5_3_v11 cGR_5_3_v12; stepTac
def cGR_5_3_v13 (q : R) : Fin 6 → R := ![0, (-q^4 + 2*q^2 - 1), 0, ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^4), ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^3), (q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1)]
theorem cGR_5_3_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, false)).mulVec (cGR_5_3_v12 q) = cGR_5_3_v13 q := by
  rw [bridge5_1]; unfold cGR_5_3_v12 cGR_5_3_v13; stepTac
def cGR_5_3_v14 (q : R) : Fin 6 → R := ![(-q^4 + 2*q^2 - 1), 0, 0, ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^3), ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^2), (q^13 - 4*q^11 + 6*q^9 - 4*q^7 + 2*q^3 - q)]
theorem cGR_5_3_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGR_5_3_v13 q) = cGR_5_3_v14 q := by
  rw [bridge5_0]; unfold cGR_5_3_v13 cGR_5_3_v14; stepTac
theorem cGR_5_3_col (q : R) (hq : q ≠ 0) :
    (wordW q idx5 wGR).mulVec (Pi.single 3 1) = cGR_5_3_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_5_3_v0_step q hq, cGR_5_3_v1_step q hq, cGR_5_3_v2_step q hq, cGR_5_3_v3_step q hq, cGR_5_3_v4_step q hq, cGR_5_3_v5_step q hq, cGR_5_3_v6_step q hq, cGR_5_3_v7_step q hq, cGR_5_3_v8_step q hq, cGR_5_3_v9_step q hq, cGR_5_3_v10_step q hq, cGR_5_3_v11_step q hq, cGR_5_3_v12_step q hq, cGR_5_3_v13_step q hq, cGR_5_3_v14_step q hq]
theorem cGR_5_3_entry (q : R) (hq : q ≠ 0) :
    wordW q idx5 wGR 3 3 = ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx5 wGR) 3 3, cGR_5_3_col q hq]; simp [cGR_5_3_v14]

def cGR_4_3_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_3_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 3 1) = cGR_4_3_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_3_v0; stepTac
def cGR_4_3_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_3_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_3_v0 q) = cGR_4_3_v1 q := by
  rw [bridge4_2]; unfold cGR_4_3_v0 cGR_4_3_v1; stepTac
def cGR_4_3_v2 (q : R) : Fin 15 → R := ![0, 0, 0, (q), 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_3_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_3_v1 q) = cGR_4_3_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_3_v1 cGR_4_3_v2; stepTac
def cGR_4_3_v3 (q : R) : Fin 15 → R := ![0, (q), 0, 0, 0, 0, (-q^3 + q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_3_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_3_v2 q) = cGR_4_3_v3 q := by
  rw [bridge4_2]; unfold cGR_4_3_v2 cGR_4_3_v3; stepTac
def cGR_4_3_v4 (q : R) : Fin 15 → R := ![0, (1), 0, (-q^3 + q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_3_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_3_v3 q) = cGR_4_3_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_3_v3 cGR_4_3_v4; stepTac
def cGR_4_3_v5 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q), 0, (1), 0, 0, (q^5 - 2*q^3 + q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_3_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_3_v4 q) = cGR_4_3_v5 q := by
  rw [bridge4_2]; unfold cGR_4_3_v4 cGR_4_3_v5; stepTac
def cGR_4_3_v6 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((1) / q), 0, 0, 0, 0, 0, 0, (q^5 - 2*q^3 + q), 0, 0, 0, 0]
theorem cGR_4_3_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_3_v5 q) = cGR_4_3_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_3_v5 cGR_4_3_v6; stepTac
def cGR_4_3_v7 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q), 0, ((q^2 - 1) / q^2), 0, 0, ((1) / q), 0, 0, 0, (q^6 - 2*q^4 + q^2), 0, 0, 0, 0]
theorem cGR_4_3_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_3_v6 q) = cGR_4_3_v7 q := by
  rw [bridge4_3]; unfold cGR_4_3_v6 cGR_4_3_v7; stepTac
def cGR_4_3_v8 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((q^2 - 1) / q^3), 0, 0, (q^6 - 2*q^4 + q^2), 0, 0, 0, ((-q^8 + 3*q^6 - 3*q^4 + q^2 + 1) / q), 0, 0, 0, 0]
theorem cGR_4_3_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_3_v7 q) = cGR_4_3_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_3_v7 cGR_4_3_v8; stepTac
def cGR_4_3_v9 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q), 0, ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^4), 0, 0, ((q^2 - 1) / q^3), 0, 0, 0, (-q^8 + 3*q^6 - 3*q^4 + q^2 + 1), 0, 0, 0, 0]
theorem cGR_4_3_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_3_v8 q) = cGR_4_3_v9 q := by
  rw [bridge4_3]; unfold cGR_4_3_v8 cGR_4_3_v9; stepTac
def cGR_4_3_v10 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^5), 0, 0, (-q^8 + 3*q^6 - 3*q^4 + q^2 + 1), 0, 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q^3), 0, 0, 0, 0]
theorem cGR_4_3_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_3_v9 q) = cGR_4_3_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_3_v9 cGR_4_3_v10; stepTac
def cGR_4_3_v11 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q), 0, ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^5), 0, 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q^2), 0, 0, 0, 0]
theorem cGR_4_3_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_3_v10 q) = cGR_4_3_v11 q := by
  rw [bridge4_3]; unfold cGR_4_3_v10 cGR_4_3_v11; stepTac
def cGR_4_3_v12 (q : R) : Fin 15 → R := ![0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^2), ((-q^4 + 2*q^2 - 1) / q), ((-q^16 + 5*q^14 - 10*q^12 + 10*q^10 - 3*q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^7), ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, ((q^12 - 3*q^10 + 3*q^8 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^5), 0, 0, ((q^14 - 5*q^12 + 10*q^10 - 10*q^8 + 4*q^6 + 2*q^4 - 3*q^2 + 1) / q^3), ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q^2), 0, 0, 0]
theorem cGR_4_3_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_3_v11 q) = cGR_4_3_v12 q := by
  rw [bridge4_0]; unfold cGR_4_3_v11 cGR_4_3_v12; stepTac
def cGR_4_3_v13 (q : R) : Fin 15 → R := ![((-q^6 + 3*q^4 - 3*q^2 + 1) / q^2), 0, (-q^4 + 2*q^2 - 1), ((-q^16 + 5*q^14 - 10*q^12 + 10*q^10 - 3*q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), ((-q^16 + 5*q^14 - 10*q^12 + 10*q^10 - 3*q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^7), ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^12 - 3*q^10 + 3*q^8 - 3*q^4 + 3*q^2 - 1) / q^5), ((q^12 - 3*q^10 + 3*q^8 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^5), 0, ((q^14 - 5*q^12 + 10*q^10 - 10*q^8 + 4*q^6 + 2*q^4 - 3*q^2 + 1) / q^2), ((q^14 - 5*q^12 + 10*q^10 - 10*q^8 + 4*q^6 + 2*q^4 - 3*q^2 + 1) / q^3), ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q^2), 0, 0]
theorem cGR_4_3_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_3_v12 q) = cGR_4_3_v13 q := by
  rw [bridge4_1]; unfold cGR_4_3_v12 cGR_4_3_v13; stepTac
def cGR_4_3_v14 (q : R) : Fin 15 → R := ![((-q^6 + 3*q^4 - 3*q^2 + 1) / q), (-q^4 + 2*q^2 - 1), 0, ((-q^16 + 5*q^14 - 10*q^12 + 10*q^10 - 3*q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), ((-q^16 + 5*q^14 - 10*q^12 + 10*q^10 - 3*q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^5), ((q^12 - 3*q^10 + 3*q^8 - 3*q^4 + 3*q^2 - 1) / q^4), ((q^12 - 3*q^10 + 3*q^8 - 3*q^4 + 3*q^2 - 1) / q^5), ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^4), 0, ((q^14 - 5*q^12 + 10*q^10 - 10*q^8 + 4*q^6 + 2*q^4 - 3*q^2 + 1) / q), ((q^14 - 5*q^12 + 10*q^10 - 10*q^8 + 4*q^6 + 2*q^4 - 3*q^2 + 1) / q^2), ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q), 0, 0]
theorem cGR_4_3_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_3_v13 q) = cGR_4_3_v14 q := by
  rw [bridge4_0]; unfold cGR_4_3_v13 cGR_4_3_v14; stepTac
theorem cGR_4_3_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 3 1) = cGR_4_3_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_3_v0_step q hq, cGR_4_3_v1_step q hq, cGR_4_3_v2_step q hq, cGR_4_3_v3_step q hq, cGR_4_3_v4_step q hq, cGR_4_3_v5_step q hq, cGR_4_3_v6_step q hq, cGR_4_3_v7_step q hq, cGR_4_3_v8_step q hq, cGR_4_3_v9_step q hq, cGR_4_3_v10_step q hq, cGR_4_3_v11_step q hq, cGR_4_3_v12_step q hq, cGR_4_3_v13_step q hq, cGR_4_3_v14_step q hq]
theorem cGR_4_3_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 3 3 = ((-q^16 + 5*q^14 - 10*q^12 + 10*q^10 - 3*q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 3 3, cGR_4_3_col q hq]; simp [cGR_4_3_v14]

def cGR_4_4_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_4_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 4 1) = cGR_4_4_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_4_v0; stepTac
def cGR_4_4_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (q), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_4_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_4_v0 q) = cGR_4_4_v1 q := by
  rw [bridge4_2]; unfold cGR_4_4_v0 cGR_4_4_v1; stepTac
def cGR_4_4_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (q), 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_4_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_4_v1 q) = cGR_4_4_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_4_v1 cGR_4_4_v2; stepTac
def cGR_4_4_v3 (q : R) : Fin 15 → R := ![0, 0, (q), 0, 0, 0, 0, (-q^3 + q), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_4_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_4_v2 q) = cGR_4_4_v3 q := by
  rw [bridge4_2]; unfold cGR_4_4_v2 cGR_4_4_v3; stepTac
def cGR_4_4_v4 (q : R) : Fin 15 → R := ![0, 0, (1), 0, (-q^3 + q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_4_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_4_v3 q) = cGR_4_4_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_4_v3 cGR_4_4_v4; stepTac
def cGR_4_4_v5 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, (1), 0, 0, (q^5 - 2*q^3 + q), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_4_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_4_v4 q) = cGR_4_4_v5 q := by
  rw [bridge4_2]; unfold cGR_4_4_v4 cGR_4_4_v5; stepTac
def cGR_4_4_v6 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((1) / q), 0, 0, 0, 0, 0, 0, (q^5 - 2*q^3 + q), 0, 0, 0]
theorem cGR_4_4_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_4_v5 q) = cGR_4_4_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_4_v5 cGR_4_4_v6; stepTac
def cGR_4_4_v7 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, ((q^2 - 1) / q^2), 0, 0, ((1) / q), 0, 0, 0, (q^6 - 2*q^4 + q^2), 0, 0, 0]
theorem cGR_4_4_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_4_v6 q) = cGR_4_4_v7 q := by
  rw [bridge4_3]; unfold cGR_4_4_v6 cGR_4_4_v7; stepTac
def cGR_4_4_v8 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((q^2 - 1) / q^3), 0, 0, (q^6 - 2*q^4 + q^2), 0, 0, 0, ((-q^8 + 3*q^6 - 3*q^4 + q^2 + 1) / q), 0, 0, 0]
theorem cGR_4_4_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_4_v7 q) = cGR_4_4_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_4_v7 cGR_4_4_v8; stepTac
def cGR_4_4_v9 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^4), 0, 0, ((q^2 - 1) / q^3), 0, 0, 0, (-q^8 + 3*q^6 - 3*q^4 + q^2 + 1), 0, 0, 0]
theorem cGR_4_4_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_4_v8 q) = cGR_4_4_v9 q := by
  rw [bridge4_3]; unfold cGR_4_4_v8 cGR_4_4_v9; stepTac
def cGR_4_4_v10 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^5), 0, 0, (-q^8 + 3*q^6 - 3*q^4 + q^2 + 1), 0, 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q^3), 0, 0, 0]
theorem cGR_4_4_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_4_v9 q) = cGR_4_4_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_4_v9 cGR_4_4_v10; stepTac
def cGR_4_4_v11 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^5), 0, 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q^2), 0, 0, 0]
theorem cGR_4_4_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_4_v10 q) = cGR_4_4_v11 q := by
  rw [bridge4_3]; unfold cGR_4_4_v10 cGR_4_4_v11; stepTac
def cGR_4_4_v12 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q), 0, ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^5), 0, 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q^2), 0, 0, 0, 0]
theorem cGR_4_4_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_4_v11 q) = cGR_4_4_v12 q := by
  rw [bridge4_0]; unfold cGR_4_4_v11 cGR_4_4_v12; stepTac
def cGR_4_4_v13 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q), 0, 0, ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^5), 0, 0, ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^4), 0, 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q), 0, 0, 0, 0]
theorem cGR_4_4_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_4_v12 q) = cGR_4_4_v13 q := by
  rw [bridge4_1]; unfold cGR_4_4_v12 cGR_4_4_v13; stepTac
def cGR_4_4_v14 (q : R) : Fin 15 → R := ![(-q^4 + 2*q^2 - 1), 0, 0, ((-q^16 + 5*q^14 - 10*q^12 + 10*q^10 - 3*q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^5), 0, ((q^12 - 3*q^10 + 3*q^8 - 3*q^4 + 3*q^2 - 1) / q^5), ((q^10 - 2*q^8 + q^6 + q^4 - 2*q^2 + 1) / q^4), 0, 0, ((q^14 - 5*q^12 + 10*q^10 - 10*q^8 + 4*q^6 + 2*q^4 - 3*q^2 + 1) / q^2), ((q^12 - 4*q^10 + 6*q^8 - 4*q^6 + 2*q^2 - 1) / q), 0, 0, 0]
theorem cGR_4_4_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_4_v13 q) = cGR_4_4_v14 q := by
  rw [bridge4_0]; unfold cGR_4_4_v13 cGR_4_4_v14; stepTac
theorem cGR_4_4_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 4 1) = cGR_4_4_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_4_v0_step q hq, cGR_4_4_v1_step q hq, cGR_4_4_v2_step q hq, cGR_4_4_v3_step q hq, cGR_4_4_v4_step q hq, cGR_4_4_v5_step q hq, cGR_4_4_v6_step q hq, cGR_4_4_v7_step q hq, cGR_4_4_v8_step q hq, cGR_4_4_v9_step q hq, cGR_4_4_v10_step q hq, cGR_4_4_v11_step q hq, cGR_4_4_v12_step q hq, cGR_4_4_v13_step q hq, cGR_4_4_v14_step q hq]
theorem cGR_4_4_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 4 4 = ((-q^14 + 4*q^12 - 6*q^10 + 4*q^8 + q^6 - 3*q^4 + 3*q^2 - 1) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 4 4, cGR_4_4_col q hq]; simp [cGR_4_4_v14]

def cGR_4_5_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0]
theorem cGR_4_5_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 5 1) = cGR_4_5_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_5_v0; stepTac
def cGR_4_5_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), (1), 0, 0, 0, 0, 0]
theorem cGR_4_5_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_5_v0 q) = cGR_4_5_v1 q := by
  rw [bridge4_2]; unfold cGR_4_5_v0 cGR_4_5_v1; stepTac
def cGR_4_5_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((1) / q), 0, 0, 0, 0, 0]
theorem cGR_4_5_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_5_v1 q) = cGR_4_5_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_5_v1 cGR_4_5_v2; stepTac
def cGR_4_5_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (q^2 - 1), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0]
theorem cGR_4_5_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_5_v2 q) = cGR_4_5_v3 q := by
  rw [bridge4_2]; unfold cGR_4_5_v2 cGR_4_5_v3; stepTac
def cGR_4_5_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0]
theorem cGR_4_5_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_5_v3 q) = cGR_4_5_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_5_v3 cGR_4_5_v4; stepTac
def cGR_4_5_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, 0, 0]
theorem cGR_4_5_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_5_v4 q) = cGR_4_5_v5 q := by
  rw [bridge4_2]; unfold cGR_4_5_v4 cGR_4_5_v5; stepTac
def cGR_4_5_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, 0, 0, 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0]
theorem cGR_4_5_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_5_v5 q) = cGR_4_5_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_5_v5 cGR_4_5_v6; stepTac
def cGR_4_5_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^8 + 4*q^6 - 5*q^4 + 3*q^2 - 1) / q^4), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4)]
theorem cGR_4_5_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_5_v6 q) = cGR_4_5_v7 q := by
  rw [bridge4_3]; unfold cGR_4_5_v6 cGR_4_5_v7; stepTac
def cGR_4_5_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^8 + 4*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5)]
theorem cGR_4_5_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_5_v7 q) = cGR_4_5_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_5_v7 cGR_4_5_v8; stepTac
def cGR_4_5_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), 0, 0, ((-q^8 + 4*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^7), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6)]
theorem cGR_4_5_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_5_v8 q) = cGR_4_5_v9 q := by
  rw [bridge4_3]; unfold cGR_4_5_v8 cGR_4_5_v9; stepTac
def cGR_4_5_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^7), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^7), 0, 0, ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 20*q^4 + 9*q^2 - 2) / q^5), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^8), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^7)]
theorem cGR_4_5_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_5_v9 q) = cGR_4_5_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_5_v9 cGR_4_5_v10; stepTac
def cGR_4_5_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^8), 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^7), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^6), 0, 0, ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 20*q^4 + 9*q^2 - 2) / q^4), ((q^18 - 7*q^16 + 22*q^14 - 42*q^12 + 55*q^10 - 52*q^8 + 36*q^6 - 18*q^4 + 6*q^2 - 1) / q^9), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^8)]
theorem cGR_4_5_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_5_v10 q) = cGR_4_5_v11 q := by
  rw [bridge4_3]; unfold cGR_4_5_v10 cGR_4_5_v11; stepTac
def cGR_4_5_v12 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^7), 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^5), 0, 0, ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 20*q^4 + 9*q^2 - 2) / q^3), ((q^18 - 7*q^16 + 22*q^14 - 42*q^12 + 55*q^10 - 52*q^8 + 36*q^6 - 18*q^4 + 6*q^2 - 1) / q^8), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^7)]
theorem cGR_4_5_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_5_v11 q) = cGR_4_5_v12 q := by
  rw [bridge4_0]; unfold cGR_4_5_v11 cGR_4_5_v12; stepTac
def cGR_4_5_v13 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^7), 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), 0, ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^4), 0, ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 20*q^4 + 9*q^2 - 2) / q^3), 0, ((q^18 - 7*q^16 + 22*q^14 - 42*q^12 + 55*q^10 - 52*q^8 + 36*q^6 - 18*q^4 + 6*q^2 - 1) / q^7), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6)]
theorem cGR_4_5_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_5_v12 q) = cGR_4_5_v13 q := by
  rw [bridge4_1]; unfold cGR_4_5_v12 cGR_4_5_v13; stepTac
def cGR_4_5_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^7), 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), 0, 0, ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^3), ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 20*q^4 + 9*q^2 - 2) / q^3), 0, 0, ((q^18 - 7*q^16 + 22*q^14 - 42*q^12 + 55*q^10 - 52*q^8 + 36*q^6 - 18*q^4 + 6*q^2 - 1) / q^6), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^5)]
theorem cGR_4_5_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_5_v13 q) = cGR_4_5_v14 q := by
  rw [bridge4_0]; unfold cGR_4_5_v13 cGR_4_5_v14; stepTac
theorem cGR_4_5_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 5 1) = cGR_4_5_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_5_v0_step q hq, cGR_4_5_v1_step q hq, cGR_4_5_v2_step q hq, cGR_4_5_v3_step q hq, cGR_4_5_v4_step q hq, cGR_4_5_v5_step q hq, cGR_4_5_v6_step q hq, cGR_4_5_v7_step q hq, cGR_4_5_v8_step q hq, cGR_4_5_v9_step q hq, cGR_4_5_v10_step q hq, cGR_4_5_v11_step q hq, cGR_4_5_v12_step q hq, cGR_4_5_v13_step q hq, cGR_4_5_v14_step q hq]
theorem cGR_4_5_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 5 5 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 5 5, cGR_4_5_col q hq]; simp [cGR_4_5_v14]

def cGR_2_0_v0 (q : R) : Fin 15 → R := ![0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_0_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 0 1) = cGR_2_0_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_0_v0; stepTac
def cGR_2_0_v1 (q : R) : Fin 15 → R := ![0, ((q^2 - 1) / q), (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_0_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_0_v0 q) = cGR_2_0_v1 q := by
  rw [bridge2_2]; unfold cGR_2_0_v0 cGR_2_0_v1; stepTac
def cGR_2_0_v2 (q : R) : Fin 15 → R := ![((q^2 - 1) / q), ((-q^4 + 2*q^2 - 1) / q^2), ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_0_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_0_v1 q) = cGR_2_0_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_0_v1 cGR_2_0_v2; stepTac
def cGR_2_0_v3 (q : R) : Fin 15 → R := ![(q^2 - 1), ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_0_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_0_v2 q) = cGR_2_0_v3 q := by
  rw [bridge2_2]; unfold cGR_2_0_v2 cGR_2_0_v3; stepTac
def cGR_2_0_v4 (q : R) : Fin 15 → R := ![((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_0_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_0_v3 q) = cGR_2_0_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_0_v3 cGR_2_0_v4; stepTac
def cGR_2_0_v5 (q : R) : Fin 15 → R := ![((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_0_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_0_v4 q) = cGR_2_0_v5 q := by
  rw [bridge2_2]; unfold cGR_2_0_v4 cGR_2_0_v5; stepTac
def cGR_2_0_v6 (q : R) : Fin 15 → R := ![((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_0_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_0_v5 q) = cGR_2_0_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_0_v5 cGR_2_0_v6; stepTac
def cGR_2_0_v7 (q : R) : Fin 15 → R := ![((-q^8 + 4*q^6 - 5*q^4 + 3*q^2 - 1) / q^4), ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, 0, 0]
theorem cGR_2_0_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_0_v6 q) = cGR_2_0_v7 q := by
  rw [bridge2_3]; unfold cGR_2_0_v6 cGR_2_0_v7; stepTac
def cGR_2_0_v8 (q : R) : Fin 15 → R := ![((-q^8 + 4*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, 0, 0, 0, 0]
theorem cGR_2_0_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_0_v7 q) = cGR_2_0_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_0_v7 cGR_2_0_v8; stepTac
def cGR_2_0_v9 (q : R) : Fin 15 → R := ![((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), ((-q^8 + 4*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^7), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), 0, 0, 0, 0, 0]
theorem cGR_2_0_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_0_v8 q) = cGR_2_0_v9 q := by
  rw [bridge2_3]; unfold cGR_2_0_v8 cGR_2_0_v9; stepTac
def cGR_2_0_v10 (q : R) : Fin 15 → R := ![((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^7), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^7), 0, 0, ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 20*q^4 + 9*q^2 - 2) / q^5), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^8), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^7), 0, 0, 0, 0, 0]
theorem cGR_2_0_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_0_v9 q) = cGR_2_0_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_0_v9 cGR_2_0_v10; stepTac
def cGR_2_0_v11 (q : R) : Fin 15 → R := ![((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^8), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^7), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^6), 0, 0, ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 20*q^4 + 9*q^2 - 2) / q^4), ((q^18 - 7*q^16 + 22*q^14 - 42*q^12 + 55*q^10 - 52*q^8 + 36*q^6 - 18*q^4 + 6*q^2 - 1) / q^9), 0, 0, ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^8), 0, 0, 0, 0, 0]
theorem cGR_2_0_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_0_v10 q) = cGR_2_0_v11 q := by
  rw [bridge2_3]; unfold cGR_2_0_v10 cGR_2_0_v11; stepTac
def cGR_2_0_v12 (q : R) : Fin 15 → R := ![((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^7), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^5), 0, 0, ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 20*q^4 + 9*q^2 - 2) / q^3), ((q^18 - 7*q^16 + 22*q^14 - 42*q^12 + 55*q^10 - 52*q^8 + 36*q^6 - 18*q^4 + 6*q^2 - 1) / q^8), 0, 0, ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^7), 0, 0, 0, 0, 0]
theorem cGR_2_0_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_0_v11 q) = cGR_2_0_v12 q := by
  rw [bridge2_0]; unfold cGR_2_0_v11 cGR_2_0_v12; stepTac
def cGR_2_0_v13 (q : R) : Fin 15 → R := ![((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^6), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^5), ((-q^16 + 7*q^14 - 21*q^12 + 37*q^10 - 43*q^8 + 34*q^6 - 18*q^4 + 6*q^2 - 1) / q^6), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^5), 0, ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 20*q^4 + 9*q^2 - 2) / q^2), ((q^20 - 8*q^18 + 29*q^16 - 64*q^14 + 97*q^12 - 107*q^10 + 88*q^8 - 54*q^6 + 24*q^4 - 7*q^2 + 1) / q^9), ((q^18 - 7*q^16 + 22*q^14 - 42*q^12 + 55*q^10 - 52*q^8 + 36*q^6 - 18*q^4 + 6*q^2 - 1) / q^8), 0, ((q^18 - 7*q^16 + 23*q^14 - 47*q^12 + 66*q^10 - 66*q^8 + 47*q^6 - 23*q^4 + 7*q^2 - 1) / q^8), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^7), 0, 0, 0, 0]
theorem cGR_2_0_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_0_v12 q) = cGR_2_0_v13 q := by
  rw [bridge2_1]; unfold cGR_2_0_v12 cGR_2_0_v13; stepTac
def cGR_2_0_v14 (q : R) : Fin 15 → R := ![((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^5), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^4), ((-q^16 + 7*q^14 - 21*q^12 + 37*q^10 - 43*q^8 + 34*q^6 - 18*q^4 + 6*q^2 - 1) / q^5), ((-q^16 + 7*q^14 - 21*q^12 + 37*q^10 - 43*q^8 + 34*q^6 - 18*q^4 + 6*q^2 - 1) / q^6), ((-q^14 + 6*q^12 - 15*q^10 + 22*q^8 - 21*q^6 + 13*q^4 - 5*q^2 + 1) / q^5), ((q^14 - 6*q^12 + 16*q^10 - 26*q^8 + 28*q^6 - 20*q^4 + 9*q^2 - 2) / q), ((q^20 - 8*q^18 + 29*q^16 - 64*q^14 + 97*q^12 - 107*q^10 + 88*q^8 - 54*q^6 + 24*q^4 - 7*q^2 + 1) / q^8), ((q^20 - 8*q^18 + 29*q^16 - 64*q^14 + 97*q^12 - 107*q^10 + 88*q^8 - 54*q^6 + 24*q^4 - 7*q^2 + 1) / q^9), ((q^18 - 7*q^16 + 22*q^14 - 42*q^12 + 55*q^10 - 52*q^8 + 36*q^6 - 18*q^4 + 6*q^2 - 1) / q^8), ((q^18 - 7*q^16 + 23*q^14 - 47*q^12 + 66*q^10 - 66*q^8 + 47*q^6 - 23*q^4 + 7*q^2 - 1) / q^7), ((q^18 - 7*q^16 + 23*q^14 - 47*q^12 + 66*q^10 - 66*q^8 + 47*q^6 - 23*q^4 + 7*q^2 - 1) / q^8), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^7), 0, 0, 0]
theorem cGR_2_0_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_0_v13 q) = cGR_2_0_v14 q := by
  rw [bridge2_0]; unfold cGR_2_0_v13 cGR_2_0_v14; stepTac
theorem cGR_2_0_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 0 1) = cGR_2_0_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_0_v0_step q hq, cGR_2_0_v1_step q hq, cGR_2_0_v2_step q hq, cGR_2_0_v3_step q hq, cGR_2_0_v4_step q hq, cGR_2_0_v5_step q hq, cGR_2_0_v6_step q hq, cGR_2_0_v7_step q hq, cGR_2_0_v8_step q hq, cGR_2_0_v9_step q hq, cGR_2_0_v10_step q hq, cGR_2_0_v11_step q hq, cGR_2_0_v12_step q hq, cGR_2_0_v13_step q hq, cGR_2_0_v14_step q hq]
theorem cGR_2_0_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 0 0 = ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 0 0, cGR_2_0_col q hq]; simp [cGR_2_0_v14]

def cGR_5_4_v0 (q : R) : Fin 6 → R := ![0, 0, 0, (1), ((-q^2 + 1) / q), 0]
theorem cGR_5_4_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (Pi.single 4 1) = cGR_5_4_v0 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGR_5_4_v0; stepTac
def cGR_5_4_v1 (q : R) : Fin 6 → R := ![0, 0, (1), 0, (-q^2 + 1), 0]
theorem cGR_5_4_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGR_5_4_v0 q) = cGR_5_4_v1 q := by
  rw [bridge5_2]; unfold cGR_5_4_v0 cGR_5_4_v1; stepTac
def cGR_5_4_v2 (q : R) : Fin 6 → R := ![0, 0, ((1) / q), (-q^2 + 1), ((q^4 - 2*q^2 + 1) / q), 0]
theorem cGR_5_4_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGR_5_4_v1 q) = cGR_5_4_v2 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGR_5_4_v1 cGR_5_4_v2; stepTac
def cGR_5_4_v3 (q : R) : Fin 6 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((1) / q), (q^4 - 2*q^2 + 1), 0]
theorem cGR_5_4_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGR_5_4_v2 q) = cGR_5_4_v3 q := by
  rw [bridge5_2]; unfold cGR_5_4_v2 cGR_5_4_v3; stepTac
def cGR_5_4_v4 (q : R) : Fin 6 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^3), (q^4 - 2*q^2 + 1), ((-q^6 + 3*q^4 - 3*q^2 + 2) / q), 0]
theorem cGR_5_4_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGR_5_4_v3 q) = cGR_5_4_v4 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGR_5_4_v3 cGR_5_4_v4; stepTac
def cGR_5_4_v5 (q : R) : Fin 6 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), (-q^6 + 3*q^4 - 3*q^2 + 2), 0]
theorem cGR_5_4_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGR_5_4_v4 q) = cGR_5_4_v5 q := by
  rw [bridge5_2]; unfold cGR_5_4_v4 cGR_5_4_v5; stepTac
def cGR_5_4_v6 (q : R) : Fin 6 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((-q^4 + 2*q^2 - 1) / q^4), 0, (-q^6 + 3*q^4 - 3*q^2 + 2)]
theorem cGR_5_4_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, true)).mulVec (cGR_5_4_v5 q) = cGR_5_4_v6 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_4]; unfold cGR_5_4_v5 cGR_5_4_v6; stepTac
def cGR_5_4_v7 (q : R) : Fin 6 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^5), ((-q^4 + 2*q^2 - 1) / q^4), (-q^7 + 3*q^5 - 3*q^3 + 2*q)]
theorem cGR_5_4_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGR_5_4_v6 q) = cGR_5_4_v7 q := by
  rw [bridge5_3]; unfold cGR_5_4_v6 cGR_5_4_v7; stepTac
def cGR_5_4_v8 (q : R) : Fin 6 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), (-q^7 + 3*q^5 - 3*q^3 + 2*q), ((q^12 - 4*q^10 + 6*q^8 - 5*q^6 + q^4 + 2*q^2 - 1) / q^4)]
theorem cGR_5_4_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, true)).mulVec (cGR_5_4_v7 q) = cGR_5_4_v8 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_4]; unfold cGR_5_4_v7 cGR_5_4_v8; stepTac
def cGR_5_4_v9 (q : R) : Fin 6 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), ((q^12 - 4*q^10 + 6*q^8 - 5*q^6 + q^4 + 2*q^2 - 1) / q^3)]
theorem cGR_5_4_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGR_5_4_v8 q) = cGR_5_4_v9 q := by
  rw [bridge5_3]; unfold cGR_5_4_v8 cGR_5_4_v9; stepTac
def cGR_5_4_v10 (q : R) : Fin 6 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^8), ((q^12 - 4*q^10 + 6*q^8 - 5*q^6 + q^4 + 2*q^2 - 1) / q^3), ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^6)]
theorem cGR_5_4_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, true)).mulVec (cGR_5_4_v9 q) = cGR_5_4_v10 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_4]; unfold cGR_5_4_v9 cGR_5_4_v10; stepTac
def cGR_5_4_v11 (q : R) : Fin 6 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^8), ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^5)]
theorem cGR_5_4_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGR_5_4_v10 q) = cGR_5_4_v11 q := by
  rw [bridge5_3]; unfold cGR_5_4_v10 cGR_5_4_v11; stepTac
def cGR_5_4_v12 (q : R) : Fin 6 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^4)]
theorem cGR_5_4_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGR_5_4_v11 q) = cGR_5_4_v12 q := by
  rw [bridge5_0]; unfold cGR_5_4_v11 cGR_5_4_v12; stepTac
def cGR_5_4_v13 (q : R) : Fin 6 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^3)]
theorem cGR_5_4_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, false)).mulVec (cGR_5_4_v12 q) = cGR_5_4_v13 q := by
  rw [bridge5_1]; unfold cGR_5_4_v12 cGR_5_4_v13; stepTac
def cGR_5_4_v14 (q : R) : Fin 6 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5), ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^2)]
theorem cGR_5_4_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGR_5_4_v13 q) = cGR_5_4_v14 q := by
  rw [bridge5_0]; unfold cGR_5_4_v13 cGR_5_4_v14; stepTac
theorem cGR_5_4_col (q : R) (hq : q ≠ 0) :
    (wordW q idx5 wGR).mulVec (Pi.single 4 1) = cGR_5_4_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_5_4_v0_step q hq, cGR_5_4_v1_step q hq, cGR_5_4_v2_step q hq, cGR_5_4_v3_step q hq, cGR_5_4_v4_step q hq, cGR_5_4_v5_step q hq, cGR_5_4_v6_step q hq, cGR_5_4_v7_step q hq, cGR_5_4_v8_step q hq, cGR_5_4_v9_step q hq, cGR_5_4_v10_step q hq, cGR_5_4_v11_step q hq, cGR_5_4_v12_step q hq, cGR_5_4_v13_step q hq, cGR_5_4_v14_step q hq]
theorem cGR_5_4_entry (q : R) (hq : q ≠ 0) :
    wordW q idx5 wGR 4 4 = ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx5 wGR) 4 4, cGR_5_4_col q hq]; simp [cGR_5_4_v14]

def cGR_4_6_v0 (q : R) : Fin 15 → R := ![0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_6_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 6 1) = cGR_4_6_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_6_v0; stepTac
def cGR_4_6_v1 (q : R) : Fin 15 → R := ![0, (1), 0, 0, 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_6_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_6_v0 q) = cGR_4_6_v1 q := by
  rw [bridge4_2]; unfold cGR_4_6_v0 cGR_4_6_v1; stepTac
def cGR_4_6_v2 (q : R) : Fin 15 → R := ![0, ((1) / q), 0, (-q^2 + 1), 0, 0, ((q^4 - 2*q^2 + 1) / q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_6_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_6_v1 q) = cGR_4_6_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_6_v1 cGR_4_6_v2; stepTac
def cGR_4_6_v3 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((1) / q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_6_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_6_v2 q) = cGR_4_6_v3 q := by
  rw [bridge4_2]; unfold cGR_4_6_v2 cGR_4_6_v3; stepTac
def cGR_4_6_v4 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q^3), 0, (q^4 - 2*q^2 + 1), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 2) / q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_6_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_6_v3 q) = cGR_4_6_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_6_v3 cGR_4_6_v4; stepTac
def cGR_4_6_v5 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_6_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_6_v4 q) = cGR_4_6_v5 q := by
  rw [bridge4_2]; unfold cGR_4_6_v4 cGR_4_6_v5; stepTac
def cGR_4_6_v6 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, ((-q^4 + 2*q^2 - 1) / q^4), 0, 0, 0, 0, 0, 0, (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0, 0]
theorem cGR_4_6_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_6_v5 q) = cGR_4_6_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_6_v5 cGR_4_6_v6; stepTac
def cGR_4_6_v7 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^5), 0, 0, ((-q^4 + 2*q^2 - 1) / q^4), 0, 0, 0, (-q^7 + 3*q^5 - 3*q^3 + 2*q), 0, 0, 0, 0]
theorem cGR_4_6_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_6_v6 q) = cGR_4_6_v7 q := by
  rw [bridge4_3]; unfold cGR_4_6_v6 cGR_4_6_v7; stepTac
def cGR_4_6_v8 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), 0, 0, (-q^7 + 3*q^5 - 3*q^3 + 2*q), 0, 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 5*q^6 + q^4 + 2*q^2 - 1) / q^4), 0, 0, 0, 0]
theorem cGR_4_6_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_6_v7 q) = cGR_4_6_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_6_v7 cGR_4_6_v8; stepTac
def cGR_4_6_v9 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), 0, 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 5*q^6 + q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0]
theorem cGR_4_6_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_6_v8 q) = cGR_4_6_v9 q := by
  rw [bridge4_3]; unfold cGR_4_6_v8 cGR_4_6_v9; stepTac
def cGR_4_6_v10 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^8), 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 5*q^6 + q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0, 0, 0, 0]
theorem cGR_4_6_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_6_v9 q) = cGR_4_6_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_6_v9 cGR_4_6_v10; stepTac
def cGR_4_6_v11 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^8), 0, 0, 0, ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0, 0, 0]
theorem cGR_4_6_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_6_v10 q) = cGR_4_6_v11 q := by
  rw [bridge4_3]; unfold cGR_4_6_v10 cGR_4_6_v11; stepTac
def cGR_4_6_v12 (q : R) : Fin 15 → R := ![0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((q^20 - 6*q^18 + 15*q^16 - 21*q^14 + 16*q^12 - 16*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^10), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, ((-q^16 + 4*q^14 - 6*q^12 + 4*q^10 + 3*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^8), 0, 0, ((-q^18 + 6*q^16 - 15*q^14 + 21*q^12 - 17*q^10 + 4*q^8 + 8*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0, 0]
theorem cGR_4_6_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_6_v11 q) = cGR_4_6_v12 q := by
  rw [bridge4_0]; unfold cGR_4_6_v11 cGR_4_6_v12; stepTac
def cGR_4_6_v13 (q : R) : Fin 15 → R := ![((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((q^20 - 6*q^18 + 15*q^16 - 21*q^14 + 16*q^12 - 16*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^9), ((q^20 - 6*q^18 + 15*q^16 - 21*q^14 + 16*q^12 - 16*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^10), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((-q^16 + 4*q^14 - 6*q^12 + 4*q^10 + 3*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((-q^16 + 4*q^14 - 6*q^12 + 4*q^10 + 3*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^8), 0, ((-q^18 + 6*q^16 - 15*q^14 + 21*q^12 - 17*q^10 + 4*q^8 + 8*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^18 + 6*q^16 - 15*q^14 + 21*q^12 - 17*q^10 + 4*q^8 + 8*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGR_4_6_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_6_v12 q) = cGR_4_6_v13 q := by
  rw [bridge4_1]; unfold cGR_4_6_v12 cGR_4_6_v13; stepTac
def cGR_4_6_v14 (q : R) : Fin 15 → R := ![((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, ((q^20 - 6*q^18 + 15*q^16 - 21*q^14 + 16*q^12 - 16*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^8), ((q^20 - 6*q^18 + 15*q^16 - 21*q^14 + 16*q^12 - 16*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^9), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((-q^16 + 4*q^14 - 6*q^12 + 4*q^10 + 3*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((-q^16 + 4*q^14 - 6*q^12 + 4*q^10 + 3*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), 0, ((-q^18 + 6*q^16 - 15*q^14 + 21*q^12 - 17*q^10 + 4*q^8 + 8*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((-q^18 + 6*q^16 - 15*q^14 + 21*q^12 - 17*q^10 + 4*q^8 + 8*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0]
theorem cGR_4_6_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_6_v13 q) = cGR_4_6_v14 q := by
  rw [bridge4_0]; unfold cGR_4_6_v13 cGR_4_6_v14; stepTac
theorem cGR_4_6_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 6 1) = cGR_4_6_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_6_v0_step q hq, cGR_4_6_v1_step q hq, cGR_4_6_v2_step q hq, cGR_4_6_v3_step q hq, cGR_4_6_v4_step q hq, cGR_4_6_v5_step q hq, cGR_4_6_v6_step q hq, cGR_4_6_v7_step q hq, cGR_4_6_v8_step q hq, cGR_4_6_v9_step q hq, cGR_4_6_v10_step q hq, cGR_4_6_v11_step q hq, cGR_4_6_v12_step q hq, cGR_4_6_v13_step q hq, cGR_4_6_v14_step q hq]
theorem cGR_4_6_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 6 6 = ((-q^16 + 4*q^14 - 6*q^12 + 4*q^10 + 3*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^7) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 6 6, cGR_4_6_col q hq]; simp [cGR_4_6_v14]

def cGR_4_7_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_7_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 7 1) = cGR_4_7_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_7_v0; stepTac
def cGR_4_7_v1 (q : R) : Fin 15 → R := ![0, 0, (1), 0, 0, 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_7_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_7_v0 q) = cGR_4_7_v1 q := by
  rw [bridge4_2]; unfold cGR_4_7_v0 cGR_4_7_v1; stepTac
def cGR_4_7_v2 (q : R) : Fin 15 → R := ![0, 0, ((1) / q), 0, (-q^2 + 1), 0, 0, ((q^4 - 2*q^2 + 1) / q), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_7_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_7_v1 q) = cGR_4_7_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_7_v1 cGR_4_7_v2; stepTac
def cGR_4_7_v3 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((1) / q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_7_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_7_v2 q) = cGR_4_7_v3 q := by
  rw [bridge4_2]; unfold cGR_4_7_v2 cGR_4_7_v3; stepTac
def cGR_4_7_v4 (q : R) : Fin 15 → R := ![0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, (q^4 - 2*q^2 + 1), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 2) / q), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_7_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_7_v3 q) = cGR_4_7_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_7_v3 cGR_4_7_v4; stepTac
def cGR_4_7_v5 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_4_7_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_7_v4 q) = cGR_4_7_v5 q := by
  rw [bridge4_2]; unfold cGR_4_7_v4 cGR_4_7_v5; stepTac
def cGR_4_7_v6 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, ((-q^4 + 2*q^2 - 1) / q^4), 0, 0, 0, 0, 0, 0, (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0]
theorem cGR_4_7_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_7_v5 q) = cGR_4_7_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_7_v5 cGR_4_7_v6; stepTac
def cGR_4_7_v7 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^5), 0, 0, ((-q^4 + 2*q^2 - 1) / q^4), 0, 0, 0, (-q^7 + 3*q^5 - 3*q^3 + 2*q), 0, 0, 0]
theorem cGR_4_7_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_7_v6 q) = cGR_4_7_v7 q := by
  rw [bridge4_3]; unfold cGR_4_7_v6 cGR_4_7_v7; stepTac
def cGR_4_7_v8 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), 0, 0, (-q^7 + 3*q^5 - 3*q^3 + 2*q), 0, 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 5*q^6 + q^4 + 2*q^2 - 1) / q^4), 0, 0, 0]
theorem cGR_4_7_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_7_v7 q) = cGR_4_7_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_7_v7 cGR_4_7_v8; stepTac
def cGR_4_7_v9 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), 0, 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 5*q^6 + q^4 + 2*q^2 - 1) / q^3), 0, 0, 0]
theorem cGR_4_7_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_7_v8 q) = cGR_4_7_v9 q := by
  rw [bridge4_3]; unfold cGR_4_7_v8 cGR_4_7_v9; stepTac
def cGR_4_7_v10 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^8), 0, 0, ((q^12 - 4*q^10 + 6*q^8 - 5*q^6 + q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0, 0, 0]
theorem cGR_4_7_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_7_v9 q) = cGR_4_7_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_7_v9 cGR_4_7_v10; stepTac
def cGR_4_7_v11 (q : R) : Fin 15 → R := ![0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^8), 0, 0, 0, ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0, 0]
theorem cGR_4_7_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_7_v10 q) = cGR_4_7_v11 q := by
  rw [bridge4_3]; unfold cGR_4_7_v10 cGR_4_7_v11; stepTac
def cGR_4_7_v12 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^8), 0, 0, 0, ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0, 0, 0]
theorem cGR_4_7_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_7_v11 q) = cGR_4_7_v12 q := by
  rw [bridge4_0]; unfold cGR_4_7_v11 cGR_4_7_v12; stepTac
def cGR_4_7_v13 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, 0, ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), 0, 0, 0, ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0, 0, 0]
theorem cGR_4_7_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_7_v12 q) = cGR_4_7_v13 q := by
  rw [bridge4_1]; unfold cGR_4_7_v12 cGR_4_7_v13; stepTac
def cGR_4_7_v14 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((q^20 - 6*q^18 + 15*q^16 - 21*q^14 + 16*q^12 - 16*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^9), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, ((-q^16 + 4*q^14 - 6*q^12 + 4*q^10 + 3*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), 0, 0, ((-q^18 + 6*q^16 - 15*q^14 + 21*q^12 - 17*q^10 + 4*q^8 + 8*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^16 + 5*q^14 - 10*q^12 + 11*q^10 - 6*q^8 - 2*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0, 0]
theorem cGR_4_7_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_7_v13 q) = cGR_4_7_v14 q := by
  rw [bridge4_0]; unfold cGR_4_7_v13 cGR_4_7_v14; stepTac
theorem cGR_4_7_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 7 1) = cGR_4_7_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_7_v0_step q hq, cGR_4_7_v1_step q hq, cGR_4_7_v2_step q hq, cGR_4_7_v3_step q hq, cGR_4_7_v4_step q hq, cGR_4_7_v5_step q hq, cGR_4_7_v6_step q hq, cGR_4_7_v7_step q hq, cGR_4_7_v8_step q hq, cGR_4_7_v9_step q hq, cGR_4_7_v10_step q hq, cGR_4_7_v11_step q hq, cGR_4_7_v12_step q hq, cGR_4_7_v13_step q hq, cGR_4_7_v14_step q hq]
theorem cGR_4_7_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 7 7 = ((-q^14 + 3*q^12 - 3*q^10 + q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^7) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 7 7, cGR_4_7_col q hq]; simp [cGR_4_7_v14]

def cGR_4_8_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0, 0, 0]
theorem cGR_4_8_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 8 1) = cGR_4_8_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_8_v0; stepTac
def cGR_4_8_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((-q^2 + 1) / q), 0, 0, 0, 0, 0]
theorem cGR_4_8_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_8_v0 q) = cGR_4_8_v1 q := by
  rw [bridge4_2]; unfold cGR_4_8_v0 cGR_4_8_v1; stepTac
def cGR_4_8_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), ((-q^2 + 1) / q^2), 0, 0, 0, 0, 0]
theorem cGR_4_8_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_8_v1 q) = cGR_4_8_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_8_v1 cGR_4_8_v2; stepTac
def cGR_4_8_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0, 0, 0]
theorem cGR_4_8_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_8_v2 q) = cGR_4_8_v3 q := by
  rw [bridge4_2]; unfold cGR_4_8_v2 cGR_4_8_v3; stepTac
def cGR_4_8_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, 0, 0]
theorem cGR_4_8_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_8_v3 q) = cGR_4_8_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_8_v3 cGR_4_8_v4; stepTac
def cGR_4_8_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0, 0, 0, 0]
theorem cGR_4_8_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_8_v4 q) = cGR_4_8_v5 q := by
  rw [bridge4_2]; unfold cGR_4_8_v4 cGR_4_8_v5; stepTac
def cGR_4_8_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, 0, 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0]
theorem cGR_4_8_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_8_v5 q) = cGR_4_8_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_8_v5 cGR_4_8_v6; stepTac
def cGR_4_8_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5)]
theorem cGR_4_8_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_8_v6 q) = cGR_4_8_v7 q := by
  rw [bridge4_3]; unfold cGR_4_8_v6 cGR_4_8_v7; stepTac
def cGR_4_8_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 20*q^6 - 14*q^4 + 6*q^2 - 1) / q^6), ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^7), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^6)]
theorem cGR_4_8_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_8_v7 q) = cGR_4_8_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_8_v7 cGR_4_8_v8; stepTac
def cGR_4_8_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), 0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), 0, 0, ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 20*q^6 - 14*q^4 + 6*q^2 - 1) / q^5), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^8), ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^7)]
theorem cGR_4_8_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_8_v8 q) = cGR_4_8_v9 q := by
  rw [bridge4_3]; unfold cGR_4_8_v8 cGR_4_8_v9; stepTac
def cGR_4_8_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^8), 0, 0, ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 20*q^6 - 14*q^4 + 6*q^2 - 1) / q^5), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^8), 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 32*q^10 - 43*q^8 + 41*q^6 - 27*q^4 + 11*q^2 - 2) / q^6), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^9), ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^8)]
theorem cGR_4_8_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_8_v9 q) = cGR_4_8_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_8_v9 cGR_4_8_v10; stepTac
def cGR_4_8_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^18 - 6*q^16 + 18*q^14 - 36*q^12 + 52*q^10 - 55*q^8 + 42*q^6 - 22*q^4 + 7*q^2 - 1) / q^9), 0, 0, ((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^8), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^7), 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 32*q^10 - 43*q^8 + 41*q^6 - 27*q^4 + 11*q^2 - 2) / q^5), ((-q^20 + 7*q^18 - 23*q^16 + 49*q^14 - 76*q^12 + 88*q^10 - 76*q^8 + 49*q^6 - 23*q^4 + 7*q^2 - 1) / q^10), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^9)]
theorem cGR_4_8_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_8_v10 q) = cGR_4_8_v11 q := by
  rw [bridge4_3]; unfold cGR_4_8_v10 cGR_4_8_v11; stepTac
def cGR_4_8_v12 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^18 - 6*q^16 + 18*q^14 - 36*q^12 + 52*q^10 - 55*q^8 + 42*q^6 - 22*q^4 + 7*q^2 - 1) / q^8), 0, 0, ((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 32*q^10 - 43*q^8 + 41*q^6 - 27*q^4 + 11*q^2 - 2) / q^4), ((-q^20 + 7*q^18 - 23*q^16 + 49*q^14 - 76*q^12 + 88*q^10 - 76*q^8 + 49*q^6 - 23*q^4 + 7*q^2 - 1) / q^9), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^8)]
theorem cGR_4_8_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_8_v11 q) = cGR_4_8_v12 q := by
  rw [bridge4_0]; unfold cGR_4_8_v11 cGR_4_8_v12; stepTac
def cGR_4_8_v13 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^18 - 6*q^16 + 18*q^14 - 36*q^12 + 52*q^10 - 55*q^8 + 42*q^6 - 22*q^4 + 7*q^2 - 1) / q^8), 0, 0, ((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), 0, ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^5), 0, ((-q^16 + 6*q^14 - 17*q^12 + 32*q^10 - 43*q^8 + 41*q^6 - 27*q^4 + 11*q^2 - 2) / q^4), 0, ((-q^20 + 7*q^18 - 23*q^16 + 49*q^14 - 76*q^12 + 88*q^10 - 76*q^8 + 49*q^6 - 23*q^4 + 7*q^2 - 1) / q^8), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^7)]
theorem cGR_4_8_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_8_v12 q) = cGR_4_8_v13 q := by
  rw [bridge4_1]; unfold cGR_4_8_v12 cGR_4_8_v13; stepTac
def cGR_4_8_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^18 - 6*q^16 + 18*q^14 - 36*q^12 + 52*q^10 - 55*q^8 + 42*q^6 - 22*q^4 + 7*q^2 - 1) / q^8), 0, 0, ((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), 0, 0, ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^4), ((-q^16 + 6*q^14 - 17*q^12 + 32*q^10 - 43*q^8 + 41*q^6 - 27*q^4 + 11*q^2 - 2) / q^4), 0, 0, ((-q^20 + 7*q^18 - 23*q^16 + 49*q^14 - 76*q^12 + 88*q^10 - 76*q^8 + 49*q^6 - 23*q^4 + 7*q^2 - 1) / q^7), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^6)]
theorem cGR_4_8_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_8_v13 q) = cGR_4_8_v14 q := by
  rw [bridge4_0]; unfold cGR_4_8_v13 cGR_4_8_v14; stepTac
theorem cGR_4_8_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 8 1) = cGR_4_8_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_8_v0_step q hq, cGR_4_8_v1_step q hq, cGR_4_8_v2_step q hq, cGR_4_8_v3_step q hq, cGR_4_8_v4_step q hq, cGR_4_8_v5_step q hq, cGR_4_8_v6_step q hq, cGR_4_8_v7_step q hq, cGR_4_8_v8_step q hq, cGR_4_8_v9_step q hq, cGR_4_8_v10_step q hq, cGR_4_8_v11_step q hq, cGR_4_8_v12_step q hq, cGR_4_8_v13_step q hq, cGR_4_8_v14_step q hq]
theorem cGR_4_8_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 8 8 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 8 8, cGR_4_8_col q hq]; simp [cGR_4_8_v14]

def cGR_2_1_v0 (q : R) : Fin 15 → R := ![(1), ((-q^2 + 1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_1_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 1 1) = cGR_2_1_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_1_v0; stepTac
def cGR_2_1_v1 (q : R) : Fin 15 → R := ![(q), ((-q^4 + 2*q^2 - 1) / q^2), ((-q^2 + 1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_1_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_1_v0 q) = cGR_2_1_v1 q := by
  rw [bridge2_2]; unfold cGR_2_1_v0 cGR_2_1_v1; stepTac
def cGR_2_1_v2 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q^2), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), ((-q^2 + 1) / q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_1_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_1_v1 q) = cGR_2_1_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_1_v1 cGR_2_1_v2; stepTac
def cGR_2_1_v3 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_1_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_1_v2 q) = cGR_2_1_v3 q := by
  rw [bridge2_2]; unfold cGR_2_1_v2 cGR_2_1_v3; stepTac
def cGR_2_1_v4 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_1_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_1_v3 q) = cGR_2_1_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_1_v3 cGR_2_1_v4; stepTac
def cGR_2_1_v5 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_1_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_1_v4 q) = cGR_2_1_v5 q := by
  rw [bridge2_2]; unfold cGR_2_1_v4 cGR_2_1_v5; stepTac
def cGR_2_1_v6 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_1_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_1_v5 q) = cGR_2_1_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_1_v5 cGR_2_1_v6; stepTac
def cGR_2_1_v7 (q : R) : Fin 15 → R := ![((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0, 0, 0, 0]
theorem cGR_2_1_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_1_v6 q) = cGR_2_1_v7 q := by
  rw [bridge2_3]; unfold cGR_2_1_v6 cGR_2_1_v7; stepTac
def cGR_2_1_v8 (q : R) : Fin 15 → R := ![((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 20*q^6 - 14*q^4 + 6*q^2 - 1) / q^6), ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^7), 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0, 0, 0, 0, 0]
theorem cGR_2_1_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_1_v7 q) = cGR_2_1_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_1_v7 cGR_2_1_v8; stepTac
def cGR_2_1_v9 (q : R) : Fin 15 → R := ![((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), 0, 0, ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 20*q^6 - 14*q^4 + 6*q^2 - 1) / q^5), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^8), 0, 0, ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^7), 0, 0, 0, 0, 0]
theorem cGR_2_1_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_1_v8 q) = cGR_2_1_v9 q := by
  rw [bridge2_3]; unfold cGR_2_1_v8 cGR_2_1_v9; stepTac
def cGR_2_1_v10 (q : R) : Fin 15 → R := ![((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^8), ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 20*q^6 - 14*q^4 + 6*q^2 - 1) / q^5), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^8), 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 32*q^10 - 43*q^8 + 41*q^6 - 27*q^4 + 11*q^2 - 2) / q^6), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^9), 0, 0, ((q^14 - 5*q^12 + 12*q^10 - 19*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^8), 0, 0, 0, 0, 0]
theorem cGR_2_1_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_1_v9 q) = cGR_2_1_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_1_v9 cGR_2_1_v10; stepTac
def cGR_2_1_v11 (q : R) : Fin 15 → R := ![((q^18 - 6*q^16 + 18*q^14 - 36*q^12 + 52*q^10 - 55*q^8 + 42*q^6 - 22*q^4 + 7*q^2 - 1) / q^9), ((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^8), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^7), 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 32*q^10 - 43*q^8 + 41*q^6 - 27*q^4 + 11*q^2 - 2) / q^5), ((-q^20 + 7*q^18 - 23*q^16 + 49*q^14 - 76*q^12 + 88*q^10 - 76*q^8 + 49*q^6 - 23*q^4 + 7*q^2 - 1) / q^10), 0, 0, ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^9), 0, 0, 0, 0, 0]
theorem cGR_2_1_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_1_v10 q) = cGR_2_1_v11 q := by
  rw [bridge2_3]; unfold cGR_2_1_v10 cGR_2_1_v11; stepTac
def cGR_2_1_v12 (q : R) : Fin 15 → R := ![((q^18 - 6*q^16 + 18*q^14 - 36*q^12 + 52*q^10 - 55*q^8 + 42*q^6 - 22*q^4 + 7*q^2 - 1) / q^8), ((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 32*q^10 - 43*q^8 + 41*q^6 - 27*q^4 + 11*q^2 - 2) / q^4), ((-q^20 + 7*q^18 - 23*q^16 + 49*q^14 - 76*q^12 + 88*q^10 - 76*q^8 + 49*q^6 - 23*q^4 + 7*q^2 - 1) / q^9), 0, 0, ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^8), 0, 0, 0, 0, 0]
theorem cGR_2_1_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_1_v11 q) = cGR_2_1_v12 q := by
  rw [bridge2_0]; unfold cGR_2_1_v11 cGR_2_1_v12; stepTac
def cGR_2_1_v13 (q : R) : Fin 15 → R := ![((q^18 - 6*q^16 + 18*q^14 - 36*q^12 + 52*q^10 - 55*q^8 + 42*q^6 - 22*q^4 + 7*q^2 - 1) / q^7), ((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^6), ((q^18 - 7*q^16 + 22*q^14 - 44*q^12 + 63*q^10 - 65*q^8 + 47*q^6 - 23*q^4 + 7*q^2 - 1) / q^7), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), 0, ((-q^16 + 6*q^14 - 17*q^12 + 32*q^10 - 43*q^8 + 41*q^6 - 27*q^4 + 11*q^2 - 2) / q^3), ((-q^22 + 8*q^20 - 30*q^18 + 72*q^16 - 125*q^14 + 164*q^12 - 164*q^10 + 125*q^8 - 72*q^6 + 30*q^4 - 8*q^2 + 1) / q^10), ((-q^20 + 7*q^18 - 23*q^16 + 49*q^14 - 76*q^12 + 88*q^10 - 76*q^8 + 49*q^6 - 23*q^4 + 7*q^2 - 1) / q^9), 0, ((-q^20 + 7*q^18 - 24*q^16 + 54*q^14 - 88*q^12 + 107*q^10 - 97*q^8 + 64*q^6 - 29*q^4 + 8*q^2 - 1) / q^9), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^8), 0, 0, 0, 0]
theorem cGR_2_1_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_1_v12 q) = cGR_2_1_v13 q := by
  rw [bridge2_1]; unfold cGR_2_1_v12 cGR_2_1_v13; stepTac
def cGR_2_1_v14 (q : R) : Fin 15 → R := ![((q^18 - 6*q^16 + 18*q^14 - 36*q^12 + 52*q^10 - 55*q^8 + 42*q^6 - 22*q^4 + 7*q^2 - 1) / q^6), ((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^5), ((q^18 - 7*q^16 + 22*q^14 - 44*q^12 + 63*q^10 - 65*q^8 + 47*q^6 - 23*q^4 + 7*q^2 - 1) / q^6), ((q^18 - 7*q^16 + 22*q^14 - 44*q^12 + 63*q^10 - 65*q^8 + 47*q^6 - 23*q^4 + 7*q^2 - 1) / q^7), ((q^16 - 6*q^14 + 16*q^12 - 28*q^10 + 35*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), ((-q^16 + 6*q^14 - 17*q^12 + 32*q^10 - 43*q^8 + 41*q^6 - 27*q^4 + 11*q^2 - 2) / q^2), ((-q^22 + 8*q^20 - 30*q^18 + 72*q^16 - 125*q^14 + 164*q^12 - 164*q^10 + 125*q^8 - 72*q^6 + 30*q^4 - 8*q^2 + 1) / q^9), ((-q^22 + 8*q^20 - 30*q^18 + 72*q^16 - 125*q^14 + 164*q^12 - 164*q^10 + 125*q^8 - 72*q^6 + 30*q^4 - 8*q^2 + 1) / q^10), ((-q^20 + 7*q^18 - 23*q^16 + 49*q^14 - 76*q^12 + 88*q^10 - 76*q^8 + 49*q^6 - 23*q^4 + 7*q^2 - 1) / q^9), ((-q^20 + 7*q^18 - 24*q^16 + 54*q^14 - 88*q^12 + 107*q^10 - 97*q^8 + 64*q^6 - 29*q^4 + 8*q^2 - 1) / q^8), ((-q^20 + 7*q^18 - 24*q^16 + 54*q^14 - 88*q^12 + 107*q^10 - 97*q^8 + 64*q^6 - 29*q^4 + 8*q^2 - 1) / q^9), ((-q^18 + 6*q^16 - 18*q^14 + 36*q^12 - 52*q^10 + 55*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^8), 0, 0, 0]
theorem cGR_2_1_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_1_v13 q) = cGR_2_1_v14 q := by
  rw [bridge2_0]; unfold cGR_2_1_v13 cGR_2_1_v14; stepTac
theorem cGR_2_1_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 1 1) = cGR_2_1_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_1_v0_step q hq, cGR_2_1_v1_step q hq, cGR_2_1_v2_step q hq, cGR_2_1_v3_step q hq, cGR_2_1_v4_step q hq, cGR_2_1_v5_step q hq, cGR_2_1_v6_step q hq, cGR_2_1_v7_step q hq, cGR_2_1_v8_step q hq, cGR_2_1_v9_step q hq, cGR_2_1_v10_step q hq, cGR_2_1_v11_step q hq, cGR_2_1_v12_step q hq, cGR_2_1_v13_step q hq, cGR_2_1_v14_step q hq]
theorem cGR_2_1_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 1 1 = ((-q^14 + 5*q^12 - 12*q^10 + 20*q^8 - 21*q^6 + 15*q^4 - 6*q^2 + 1) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 1 1, cGR_2_1_col q hq]; simp [cGR_2_1_v14]

def cGR_5_5_v0 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, ((1) / q)]
theorem cGR_5_5_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (Pi.single 5 1) = cGR_5_5_v0 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGR_5_5_v0; stepTac
def cGR_5_5_v1 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, (1)]
theorem cGR_5_5_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGR_5_5_v0 q) = cGR_5_5_v1 q := by
  rw [bridge5_2]; unfold cGR_5_5_v0 cGR_5_5_v1; stepTac
def cGR_5_5_v2 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, ((1) / q)]
theorem cGR_5_5_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGR_5_5_v1 q) = cGR_5_5_v2 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGR_5_5_v1 cGR_5_5_v2; stepTac
def cGR_5_5_v3 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, (1)]
theorem cGR_5_5_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGR_5_5_v2 q) = cGR_5_5_v3 q := by
  rw [bridge5_2]; unfold cGR_5_5_v2 cGR_5_5_v3; stepTac
def cGR_5_5_v4 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, ((1) / q)]
theorem cGR_5_5_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, true)).mulVec (cGR_5_5_v3 q) = cGR_5_5_v4 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_3]; unfold cGR_5_5_v3 cGR_5_5_v4; stepTac
def cGR_5_5_v5 (q : R) : Fin 6 → R := ![0, 0, 0, 0, 0, (1)]
theorem cGR_5_5_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (2, false)).mulVec (cGR_5_5_v4 q) = cGR_5_5_v5 q := by
  rw [bridge5_2]; unfold cGR_5_5_v4 cGR_5_5_v5; stepTac
def cGR_5_5_v6 (q : R) : Fin 6 → R := ![0, 0, 0, 0, (1), ((-q^2 + 1) / q)]
theorem cGR_5_5_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, true)).mulVec (cGR_5_5_v5 q) = cGR_5_5_v6 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_4]; unfold cGR_5_5_v5 cGR_5_5_v6; stepTac
def cGR_5_5_v7 (q : R) : Fin 6 → R := ![0, 0, 0, (1), 0, (-q^2 + 1)]
theorem cGR_5_5_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGR_5_5_v6 q) = cGR_5_5_v7 q := by
  rw [bridge5_3]; unfold cGR_5_5_v6 cGR_5_5_v7; stepTac
def cGR_5_5_v8 (q : R) : Fin 6 → R := ![0, 0, 0, ((1) / q), (-q^2 + 1), ((q^4 - 2*q^2 + 1) / q)]
theorem cGR_5_5_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, true)).mulVec (cGR_5_5_v7 q) = cGR_5_5_v8 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_4]; unfold cGR_5_5_v7 cGR_5_5_v8; stepTac
def cGR_5_5_v9 (q : R) : Fin 6 → R := ![0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((1) / q), (q^4 - 2*q^2 + 1)]
theorem cGR_5_5_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGR_5_5_v8 q) = cGR_5_5_v9 q := by
  rw [bridge5_3]; unfold cGR_5_5_v8 cGR_5_5_v9; stepTac
def cGR_5_5_v10 (q : R) : Fin 6 → R := ![0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), (q^4 - 2*q^2 + 1), ((-q^6 + 3*q^4 - 3*q^2 + 2) / q)]
theorem cGR_5_5_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (4, true)).mulVec (cGR_5_5_v9 q) = cGR_5_5_v10 q := by
  rw [gW_inv_mulVec q idx5 idx5_inj, bridge5_4]; unfold cGR_5_5_v9 cGR_5_5_v10; stepTac
def cGR_5_5_v11 (q : R) : Fin 6 → R := ![0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), (-q^6 + 3*q^4 - 3*q^2 + 2)]
theorem cGR_5_5_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (3, false)).mulVec (cGR_5_5_v10 q) = cGR_5_5_v11 q := by
  rw [bridge5_3]; unfold cGR_5_5_v10 cGR_5_5_v11; stepTac
def cGR_5_5_v12 (q : R) : Fin 6 → R := ![0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), (-q^7 + 3*q^5 - 3*q^3 + 2*q)]
theorem cGR_5_5_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGR_5_5_v11 q) = cGR_5_5_v12 q := by
  rw [bridge5_0]; unfold cGR_5_5_v11 cGR_5_5_v12; stepTac
def cGR_5_5_v13 (q : R) : Fin 6 → R := ![0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), ((-q^4 + 2*q^2 - 1) / q), (-q^8 + 3*q^6 - 3*q^4 + 2*q^2)]
theorem cGR_5_5_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (1, false)).mulVec (cGR_5_5_v12 q) = cGR_5_5_v13 q := by
  rw [bridge5_1]; unfold cGR_5_5_v12 cGR_5_5_v13; stepTac
def cGR_5_5_v14 (q : R) : Fin 6 → R := ![0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), (-q^4 + 2*q^2 - 1), (-q^9 + 3*q^7 - 3*q^5 + 2*q^3)]
theorem cGR_5_5_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx5 (0, false)).mulVec (cGR_5_5_v13 q) = cGR_5_5_v14 q := by
  rw [bridge5_0]; unfold cGR_5_5_v13 cGR_5_5_v14; stepTac
theorem cGR_5_5_col (q : R) (hq : q ≠ 0) :
    (wordW q idx5 wGR).mulVec (Pi.single 5 1) = cGR_5_5_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_5_5_v0_step q hq, cGR_5_5_v1_step q hq, cGR_5_5_v2_step q hq, cGR_5_5_v3_step q hq, cGR_5_5_v4_step q hq, cGR_5_5_v5_step q hq, cGR_5_5_v6_step q hq, cGR_5_5_v7_step q hq, cGR_5_5_v8_step q hq, cGR_5_5_v9_step q hq, cGR_5_5_v10_step q hq, cGR_5_5_v11_step q hq, cGR_5_5_v12_step q hq, cGR_5_5_v13_step q hq, cGR_5_5_v14_step q hq]
theorem cGR_5_5_entry (q : R) (hq : q ≠ 0) :
    wordW q idx5 wGR 5 5 = (-q^9 + 3*q^7 - 3*q^5 + 2*q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx5 wGR) 5 5, cGR_5_5_col q hq]; simp [cGR_5_5_v14]

def cGR_4_10_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0]
theorem cGR_4_10_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 10 1) = cGR_4_10_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_10_v0; stepTac
def cGR_4_10_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0]
theorem cGR_4_10_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_10_v0 q) = cGR_4_10_v1 q := by
  rw [bridge4_2]; unfold cGR_4_10_v0 cGR_4_10_v1; stepTac
def cGR_4_10_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0]
theorem cGR_4_10_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_10_v1 q) = cGR_4_10_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_10_v1 cGR_4_10_v2; stepTac
def cGR_4_10_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0]
theorem cGR_4_10_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_10_v2 q) = cGR_4_10_v3 q := by
  rw [bridge4_2]; unfold cGR_4_10_v2 cGR_4_10_v3; stepTac
def cGR_4_10_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0]
theorem cGR_4_10_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_10_v3 q) = cGR_4_10_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_10_v3 cGR_4_10_v4; stepTac
def cGR_4_10_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0]
theorem cGR_4_10_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_10_v4 q) = cGR_4_10_v5 q := by
  rw [bridge4_2]; unfold cGR_4_10_v4 cGR_4_10_v5; stepTac
def cGR_4_10_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, (1), 0, 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0]
theorem cGR_4_10_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_10_v5 q) = cGR_4_10_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_10_v5 cGR_4_10_v6; stepTac
def cGR_4_10_v7 (q : R) : Fin 15 → R := ![0, 0, 0, (1), 0, 0, 0, 0, 0, 0, (-q^2 + 1), 0, 0, 0, 0]
theorem cGR_4_10_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_10_v6 q) = cGR_4_10_v7 q := by
  rw [bridge4_3]; unfold cGR_4_10_v6 cGR_4_10_v7; stepTac
def cGR_4_10_v8 (q : R) : Fin 15 → R := ![0, 0, 0, ((1) / q), 0, 0, (-q^2 + 1), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q), 0, 0, 0, 0]
theorem cGR_4_10_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_10_v7 q) = cGR_4_10_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_10_v7 cGR_4_10_v8; stepTac
def cGR_4_10_v9 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((1) / q), 0, 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0]
theorem cGR_4_10_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_10_v8 q) = cGR_4_10_v9 q := by
  rw [bridge4_3]; unfold cGR_4_10_v8 cGR_4_10_v9; stepTac
def cGR_4_10_v10 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 2) / q), 0, 0, 0, 0]
theorem cGR_4_10_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_10_v9 q) = cGR_4_10_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_10_v9 cGR_4_10_v10; stepTac
def cGR_4_10_v11 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0, 0]
theorem cGR_4_10_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_10_v10 q) = cGR_4_10_v11 q := by
  rw [bridge4_3]; unfold cGR_4_10_v10 cGR_4_10_v11; stepTac
def cGR_4_10_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 5*q^2 - 2) / q), (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0]
theorem cGR_4_10_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_10_v11 q) = cGR_4_10_v12 q := by
  rw [bridge4_0]; unfold cGR_4_10_v11 cGR_4_10_v12; stepTac
def cGR_4_10_v13 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^3), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, (-q^8 + 4*q^6 - 6*q^4 + 5*q^2 - 2), ((-q^8 + 4*q^6 - 6*q^4 + 5*q^2 - 2) / q), (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0]
theorem cGR_4_10_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_10_v12 q) = cGR_4_10_v13 q := by
  rw [bridge4_1]; unfold cGR_4_10_v12 cGR_4_10_v13; stepTac
def cGR_4_10_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^2), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), 0, (-q^9 + 4*q^7 - 6*q^5 + 5*q^3 - 2*q), (-q^8 + 4*q^6 - 6*q^4 + 5*q^2 - 2), (-q^7 + 3*q^5 - 3*q^3 + 2*q), 0, 0]
theorem cGR_4_10_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_10_v13 q) = cGR_4_10_v14 q := by
  rw [bridge4_0]; unfold cGR_4_10_v13 cGR_4_10_v14; stepTac
theorem cGR_4_10_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 10 1) = cGR_4_10_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_10_v0_step q hq, cGR_4_10_v1_step q hq, cGR_4_10_v2_step q hq, cGR_4_10_v3_step q hq, cGR_4_10_v4_step q hq, cGR_4_10_v5_step q hq, cGR_4_10_v6_step q hq, cGR_4_10_v7_step q hq, cGR_4_10_v8_step q hq, cGR_4_10_v9_step q hq, cGR_4_10_v10_step q hq, cGR_4_10_v11_step q hq, cGR_4_10_v12_step q hq, cGR_4_10_v13_step q hq, cGR_4_10_v14_step q hq]
theorem cGR_4_10_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 10 10 = (-q^9 + 4*q^7 - 6*q^5 + 5*q^3 - 2*q) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 10 10, cGR_4_10_col q hq]; simp [cGR_4_10_v14]

def cGR_4_11_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0]
theorem cGR_4_11_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 11 1) = cGR_4_11_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_11_v0; stepTac
def cGR_4_11_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0]
theorem cGR_4_11_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_11_v0 q) = cGR_4_11_v1 q := by
  rw [bridge4_2]; unfold cGR_4_11_v0 cGR_4_11_v1; stepTac
def cGR_4_11_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0]
theorem cGR_4_11_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_11_v1 q) = cGR_4_11_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_11_v1 cGR_4_11_v2; stepTac
def cGR_4_11_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0]
theorem cGR_4_11_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_11_v2 q) = cGR_4_11_v3 q := by
  rw [bridge4_2]; unfold cGR_4_11_v2 cGR_4_11_v3; stepTac
def cGR_4_11_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0]
theorem cGR_4_11_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_11_v3 q) = cGR_4_11_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_11_v3 cGR_4_11_v4; stepTac
def cGR_4_11_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0]
theorem cGR_4_11_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_11_v4 q) = cGR_4_11_v5 q := by
  rw [bridge4_2]; unfold cGR_4_11_v4 cGR_4_11_v5; stepTac
def cGR_4_11_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, ((-q^2 + 1) / q), 0, 0, 0]
theorem cGR_4_11_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_11_v5 q) = cGR_4_11_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_11_v5 cGR_4_11_v6; stepTac
def cGR_4_11_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, (-q^2 + 1), 0, 0, 0]
theorem cGR_4_11_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_11_v6 q) = cGR_4_11_v7 q := by
  rw [bridge4_3]; unfold cGR_4_11_v6 cGR_4_11_v7; stepTac
def cGR_4_11_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((1) / q), 0, 0, (-q^2 + 1), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q), 0, 0, 0]
theorem cGR_4_11_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_11_v7 q) = cGR_4_11_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_11_v7 cGR_4_11_v8; stepTac
def cGR_4_11_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((1) / q), 0, 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0]
theorem cGR_4_11_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_11_v8 q) = cGR_4_11_v9 q := by
  rw [bridge4_3]; unfold cGR_4_11_v8 cGR_4_11_v9; stepTac
def cGR_4_11_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 2) / q), 0, 0, 0]
theorem cGR_4_11_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_11_v9 q) = cGR_4_11_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_11_v9 cGR_4_11_v10; stepTac
def cGR_4_11_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0]
theorem cGR_4_11_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_11_v10 q) = cGR_4_11_v11 q := by
  rw [bridge4_3]; unfold cGR_4_11_v10 cGR_4_11_v11; stepTac
def cGR_4_11_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0, 0]
theorem cGR_4_11_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_11_v11 q) = cGR_4_11_v12 q := by
  rw [bridge4_0]; unfold cGR_4_11_v11 cGR_4_11_v12; stepTac
def cGR_4_11_v13 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, (-q^7 + 3*q^5 - 3*q^3 + 2*q), 0, 0, 0, 0]
theorem cGR_4_11_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_11_v12 q) = cGR_4_11_v13 q := by
  rw [bridge4_1]; unfold cGR_4_11_v12 cGR_4_11_v13; stepTac
def cGR_4_11_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, (-q^8 + 4*q^6 - 6*q^4 + 5*q^2 - 2), (-q^7 + 3*q^5 - 3*q^3 + 2*q), 0, 0, 0]
theorem cGR_4_11_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_11_v13 q) = cGR_4_11_v14 q := by
  rw [bridge4_0]; unfold cGR_4_11_v13 cGR_4_11_v14; stepTac
theorem cGR_4_11_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 11 1) = cGR_4_11_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_11_v0_step q hq, cGR_4_11_v1_step q hq, cGR_4_11_v2_step q hq, cGR_4_11_v3_step q hq, cGR_4_11_v4_step q hq, cGR_4_11_v5_step q hq, cGR_4_11_v6_step q hq, cGR_4_11_v7_step q hq, cGR_4_11_v8_step q hq, cGR_4_11_v9_step q hq, cGR_4_11_v10_step q hq, cGR_4_11_v11_step q hq, cGR_4_11_v12_step q hq, cGR_4_11_v13_step q hq, cGR_4_11_v14_step q hq]
theorem cGR_4_11_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 11 11 = (-q^7 + 3*q^5 - 3*q^3 + 2*q) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 11 11, cGR_4_11_col q hq]; simp [cGR_4_11_v14]

def cGR_4_12_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0]
theorem cGR_4_12_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 12 1) = cGR_4_12_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_12_v0; stepTac
def cGR_4_12_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q^2), ((1) / q), 0]
theorem cGR_4_12_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_12_v0 q) = cGR_4_12_v1 q := by
  rw [bridge4_2]; unfold cGR_4_12_v0 cGR_4_12_v1; stepTac
def cGR_4_12_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q^3), 0, ((1) / q)]
theorem cGR_4_12_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_12_v1 q) = cGR_4_12_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_12_v1 cGR_4_12_v2; stepTac
def cGR_4_12_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), ((q^2 - 1) / q^3), (1)]
theorem cGR_4_12_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_12_v2 q) = cGR_4_12_v3 q := by
  rw [bridge4_2]; unfold cGR_4_12_v2 cGR_4_12_v3; stepTac
def cGR_4_12_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), (1), ((-q^4 + 2*q^2 - 1) / q^3)]
theorem cGR_4_12_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_12_v3 q) = cGR_4_12_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_12_v3 cGR_4_12_v4; stepTac
def cGR_4_12_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), ((-q^4 + 2*q^2 - 1) / q^2)]
theorem cGR_4_12_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_12_v4 q) = cGR_4_12_v5 q := by
  rw [bridge4_2]; unfold cGR_4_12_v4 cGR_4_12_v5; stepTac
def cGR_4_12_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), 0, 0, ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), ((-q^4 + 2*q^2 - 1) / q^3)]
theorem cGR_4_12_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_12_v5 q) = cGR_4_12_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_12_v5 cGR_4_12_v6; stepTac
def cGR_4_12_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), 0, 0, ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((-2*q^8 + 6*q^6 - 7*q^4 + 4*q^2 - 1) / q^7), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6)]
theorem cGR_4_12_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_12_v6 q) = cGR_4_12_v7 q := by
  rw [bridge4_3]; unfold cGR_4_12_v6 cGR_4_12_v7; stepTac
def cGR_4_12_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^7), 0, 0, ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((-2*q^8 + 6*q^6 - 7*q^4 + 4*q^2 - 1) / q^7), 0, 0, ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^7), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^8), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^7)]
theorem cGR_4_12_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_12_v7 q) = cGR_4_12_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_12_v7 cGR_4_12_v8; stepTac
def cGR_4_12_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^7), ((-2*q^8 + 6*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), 0, 0, ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^9), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^8)]
theorem cGR_4_12_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_12_v8 q) = cGR_4_12_v9 q := by
  rw [bridge4_3]; unfold cGR_4_12_v8 cGR_4_12_v9; stepTac
def cGR_4_12_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^7), ((-2*q^14 + 9*q^12 - 20*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^10), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^9)]
theorem cGR_4_12_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_12_v9 q) = cGR_4_12_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_12_v9 cGR_4_12_v10; stepTac
def cGR_4_12_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^10), 0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^8), 0, 0, ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^6), ((-2*q^16 + 11*q^14 - 27*q^12 + 41*q^10 - 43*q^8 + 32*q^6 - 17*q^4 + 6*q^2 - 1) / q^11), ((-2*q^14 + 9*q^12 - 20*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^10)]
theorem cGR_4_12_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_12_v10 q) = cGR_4_12_v11 q := by
  rw [bridge4_3]; unfold cGR_4_12_v10 cGR_4_12_v11; stepTac
def cGR_4_12_v12 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^9), 0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^7), 0, 0, ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^5), ((-2*q^16 + 11*q^14 - 27*q^12 + 41*q^10 - 43*q^8 + 32*q^6 - 17*q^4 + 6*q^2 - 1) / q^10), ((-2*q^14 + 9*q^12 - 20*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^9)]
theorem cGR_4_12_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_12_v11 q) = cGR_4_12_v12 q := by
  rw [bridge4_0]; unfold cGR_4_12_v11 cGR_4_12_v12; stepTac
def cGR_4_12_v13 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^9), 0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^6), 0, ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^5), 0, ((-2*q^16 + 11*q^14 - 27*q^12 + 41*q^10 - 43*q^8 + 32*q^6 - 17*q^4 + 6*q^2 - 1) / q^9), ((-2*q^14 + 9*q^12 - 20*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^8)]
theorem cGR_4_12_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_12_v12 q) = cGR_4_12_v13 q := by
  rw [bridge4_1]; unfold cGR_4_12_v12 cGR_4_12_v13; stepTac
def cGR_4_12_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^9), 0, 0, ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, 0, ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^5), ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^5), 0, 0, ((-2*q^16 + 11*q^14 - 27*q^12 + 41*q^10 - 43*q^8 + 32*q^6 - 17*q^4 + 6*q^2 - 1) / q^8), ((-2*q^14 + 9*q^12 - 20*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^7)]
theorem cGR_4_12_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_12_v13 q) = cGR_4_12_v14 q := by
  rw [bridge4_0]; unfold cGR_4_12_v13 cGR_4_12_v14; stepTac
theorem cGR_4_12_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 12 1) = cGR_4_12_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_12_v0_step q hq, cGR_4_12_v1_step q hq, cGR_4_12_v2_step q hq, cGR_4_12_v3_step q hq, cGR_4_12_v4_step q hq, cGR_4_12_v5_step q hq, cGR_4_12_v6_step q hq, cGR_4_12_v7_step q hq, cGR_4_12_v8_step q hq, cGR_4_12_v9_step q hq, cGR_4_12_v10_step q hq, cGR_4_12_v11_step q hq, cGR_4_12_v12_step q hq, cGR_4_12_v13_step q hq, cGR_4_12_v14_step q hq]
theorem cGR_4_12_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 12 12 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 12 12, cGR_4_12_col q hq]; simp [cGR_4_12_v14]

def cGR_2_5_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_5_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 5 1) = cGR_2_5_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_5_v0; stepTac
def cGR_2_5_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^2 - 1) / q^2), ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_5_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_5_v0 q) = cGR_2_5_v1 q := by
  rw [bridge2_2]; unfold cGR_2_5_v0 cGR_2_5_v1; stepTac
def cGR_2_5_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^2 - 1) / q^3), 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0]
theorem cGR_2_5_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_5_v1 q) = cGR_2_5_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_5_v1 cGR_2_5_v2; stepTac
def cGR_2_5_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^4), ((q^2 - 1) / q^3), 0, 0, (1), 0, 0, 0, 0, 0]
theorem cGR_2_5_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_5_v2 q) = cGR_2_5_v3 q := by
  rw [bridge2_2]; unfold cGR_2_5_v2 cGR_2_5_v3; stepTac
def cGR_2_5_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^4 - 2*q^2 + 1) / q^5), (1), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0]
theorem cGR_2_5_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_5_v3 q) = cGR_2_5_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_5_v3 cGR_2_5_v4; stepTac
def cGR_2_5_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0, 0]
theorem cGR_2_5_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_5_v4 q) = cGR_2_5_v5 q := by
  rw [bridge2_2]; unfold cGR_2_5_v4 cGR_2_5_v5; stepTac
def cGR_2_5_v6 (q : R) : Fin 15 → R := ![0, ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), 0, 0, ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^7), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0]
theorem cGR_2_5_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_5_v5 q) = cGR_2_5_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_5_v5 cGR_2_5_v6; stepTac
def cGR_2_5_v7 (q : R) : Fin 15 → R := ![((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^6), 0, ((q^4 - 2*q^2 + 1) / q^4), 0, 0, ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((-2*q^8 + 6*q^6 - 7*q^4 + 4*q^2 - 1) / q^7), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^6), 0, 0, 0, 0, 0]
theorem cGR_2_5_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_5_v6 q) = cGR_2_5_v7 q := by
  rw [bridge2_3]; unfold cGR_2_5_v6 cGR_2_5_v7; stepTac
def cGR_2_5_v8 (q : R) : Fin 15 → R := ![((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^7), ((-2*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 1) / q^6), ((-2*q^8 + 6*q^6 - 7*q^4 + 4*q^2 - 1) / q^7), 0, 0, ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^7), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^8), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^7), 0, 0, 0, 0, 0]
theorem cGR_2_5_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_5_v7 q) = cGR_2_5_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_5_v7 cGR_2_5_v8; stepTac
def cGR_2_5_v9 (q : R) : Fin 15 → R := ![((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((2*q^6 - 3*q^4 + 3*q^2 - 1) / q^7), ((-2*q^8 + 6*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), 0, 0, ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^8), 0, 0, 0, 0, 0]
theorem cGR_2_5_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_5_v8 q) = cGR_2_5_v9 q := by
  rw [bridge2_3]; unfold cGR_2_5_v8 cGR_2_5_v9; stepTac
def cGR_2_5_v10 (q : R) : Fin 15 → R := ![((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^7), ((-2*q^14 + 9*q^12 - 20*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^10), 0, 0, ((2*q^10 - 7*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^9), 0, 0, 0, 0, 0]
theorem cGR_2_5_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_5_v9 q) = cGR_2_5_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_5_v9 cGR_2_5_v10; stepTac
def cGR_2_5_v11 (q : R) : Fin 15 → R := ![((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^10), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^8), 0, 0, ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^6), ((-2*q^16 + 11*q^14 - 27*q^12 + 41*q^10 - 43*q^8 + 32*q^6 - 17*q^4 + 6*q^2 - 1) / q^11), 0, 0, ((-2*q^14 + 9*q^12 - 20*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^10), 0, 0, 0, 0, 0]
theorem cGR_2_5_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_5_v10 q) = cGR_2_5_v11 q := by
  rw [bridge2_3]; unfold cGR_2_5_v10 cGR_2_5_v11; stepTac
def cGR_2_5_v12 (q : R) : Fin 15 → R := ![((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^9), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^7), 0, 0, ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^5), ((-2*q^16 + 11*q^14 - 27*q^12 + 41*q^10 - 43*q^8 + 32*q^6 - 17*q^4 + 6*q^2 - 1) / q^10), 0, 0, ((-2*q^14 + 9*q^12 - 20*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^9), 0, 0, 0, 0, 0]
theorem cGR_2_5_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_5_v11 q) = cGR_2_5_v12 q := by
  rw [bridge2_0]; unfold cGR_2_5_v11 cGR_2_5_v12; stepTac
def cGR_2_5_v13 (q : R) : Fin 15 → R := ![((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^8), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((2*q^14 - 11*q^12 + 26*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^8), ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^7), 0, ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^4), ((-2*q^18 + 13*q^16 - 38*q^14 + 68*q^12 - 84*q^10 + 75*q^8 - 49*q^6 + 23*q^4 - 7*q^2 + 1) / q^11), ((-2*q^16 + 11*q^14 - 27*q^12 + 41*q^10 - 43*q^8 + 32*q^6 - 17*q^4 + 6*q^2 - 1) / q^10), 0, ((-2*q^16 + 11*q^14 - 29*q^12 + 48*q^10 - 54*q^8 + 42*q^6 - 22*q^4 + 7*q^2 - 1) / q^10), ((-2*q^14 + 9*q^12 - 20*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^9), 0, 0, 0, 0]
theorem cGR_2_5_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_5_v12 q) = cGR_2_5_v13 q := by
  rw [bridge2_1]; unfold cGR_2_5_v12 cGR_2_5_v13; stepTac
def cGR_2_5_v14 (q : R) : Fin 15 → R := ![((2*q^14 - 9*q^12 + 20*q^10 - 28*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^7), ((-2*q^10 + 7*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), ((2*q^14 - 11*q^12 + 26*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^7), ((2*q^14 - 11*q^12 + 26*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^8), ((2*q^12 - 9*q^10 + 17*q^8 - 18*q^6 + 12*q^4 - 5*q^2 + 1) / q^7), ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^3), ((-2*q^18 + 13*q^16 - 38*q^14 + 68*q^12 - 84*q^10 + 75*q^8 - 49*q^6 + 23*q^4 - 7*q^2 + 1) / q^10), ((-2*q^18 + 13*q^16 - 38*q^14 + 68*q^12 - 84*q^10 + 75*q^8 - 49*q^6 + 23*q^4 - 7*q^2 + 1) / q^11), ((-2*q^16 + 11*q^14 - 27*q^12 + 41*q^10 - 43*q^8 + 32*q^6 - 17*q^4 + 6*q^2 - 1) / q^10), ((-2*q^16 + 11*q^14 - 29*q^12 + 48*q^10 - 54*q^8 + 42*q^6 - 22*q^4 + 7*q^2 - 1) / q^9), ((-2*q^16 + 11*q^14 - 29*q^12 + 48*q^10 - 54*q^8 + 42*q^6 - 22*q^4 + 7*q^2 - 1) / q^10), ((-2*q^14 + 9*q^12 - 20*q^10 + 28*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^9), 0, 0, 0]
theorem cGR_2_5_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_5_v13 q) = cGR_2_5_v14 q := by
  rw [bridge2_0]; unfold cGR_2_5_v13 cGR_2_5_v14; stepTac
theorem cGR_2_5_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 5 1) = cGR_2_5_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_5_v0_step q hq, cGR_2_5_v1_step q hq, cGR_2_5_v2_step q hq, cGR_2_5_v3_step q hq, cGR_2_5_v4_step q hq, cGR_2_5_v5_step q hq, cGR_2_5_v6_step q hq, cGR_2_5_v7_step q hq, cGR_2_5_v8_step q hq, cGR_2_5_v9_step q hq, cGR_2_5_v10_step q hq, cGR_2_5_v11_step q hq, cGR_2_5_v12_step q hq, cGR_2_5_v13_step q hq, cGR_2_5_v14_step q hq]
theorem cGR_2_5_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 5 5 = ((-2*q^12 + 9*q^10 - 18*q^8 + 23*q^6 - 18*q^4 + 9*q^2 - 2) / q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 5 5, cGR_2_5_col q hq]; simp [cGR_2_5_v14]

def cGR_4_9_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0]
theorem cGR_4_9_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 9 1) = cGR_4_9_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_9_v0; stepTac
def cGR_4_9_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0]
theorem cGR_4_9_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_9_v0 q) = cGR_4_9_v1 q := by
  rw [bridge4_2]; unfold cGR_4_9_v0 cGR_4_9_v1; stepTac
def cGR_4_9_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((1) / q), 0, 0, ((-q^2 + 1) / q^2), 0, 0, 0, 0, 0, 0]
theorem cGR_4_9_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_9_v1 q) = cGR_4_9_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_9_v1 cGR_4_9_v2; stepTac
def cGR_4_9_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (1), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), ((-q^2 + 1) / q^2), 0, 0, 0, 0, 0]
theorem cGR_4_9_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_9_v2 q) = cGR_4_9_v3 q := by
  rw [bridge4_2]; unfold cGR_4_9_v2 cGR_4_9_v3; stepTac
def cGR_4_9_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), ((-q^2 + 1) / q^3), 0, 0, 0, 0, 0]
theorem cGR_4_9_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_9_v3 q) = cGR_4_9_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_9_v3 cGR_4_9_v4; stepTac
def cGR_4_9_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, 0, 0]
theorem cGR_4_9_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_9_v4 q) = cGR_4_9_v5 q := by
  rw [bridge4_2]; unfold cGR_4_9_v4 cGR_4_9_v5; stepTac
def cGR_4_9_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0]
theorem cGR_4_9_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_9_v5 q) = cGR_4_9_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_9_v5 cGR_4_9_v6; stepTac
def cGR_4_9_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4)]
theorem cGR_4_9_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_9_v6 q) = cGR_4_9_v7 q := by
  rw [bridge4_3]; unfold cGR_4_9_v6 cGR_4_9_v7; stepTac
def cGR_4_9_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^5), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^5), 0, 0, ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^5), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^6), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^5)]
theorem cGR_4_9_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_9_v7 q) = cGR_4_9_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_9_v7 cGR_4_9_v8; stepTac
def cGR_4_9_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^5), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^4), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^7), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^6)]
theorem cGR_4_9_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_9_v8 q) = cGR_4_9_v9 q := by
  rw [bridge4_3]; unfold cGR_4_9_v8 cGR_4_9_v9; stepTac
def cGR_4_9_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^7), 0, 0, ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^4), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^7), 0, 0, ((q^12 - 5*q^10 + 12*q^8 - 18*q^6 + 17*q^4 - 9*q^2 + 2) / q^5), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^8), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^7)]
theorem cGR_4_9_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_9_v9 q) = cGR_4_9_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_9_v9 cGR_4_9_v10; stepTac
def cGR_4_9_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^14 + 5*q^12 - 13*q^10 + 21*q^8 - 22*q^6 + 15*q^4 - 6*q^2 + 1) / q^8), 0, 0, ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^7), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((q^12 - 5*q^10 + 12*q^8 - 18*q^6 + 17*q^4 - 9*q^2 + 2) / q^4), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 35*q^8 - 28*q^6 + 16*q^4 - 6*q^2 + 1) / q^9), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^8)]
theorem cGR_4_9_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_9_v10 q) = cGR_4_9_v11 q := by
  rw [bridge4_3]; unfold cGR_4_9_v10 cGR_4_9_v11; stepTac
def cGR_4_9_v12 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^14 + 5*q^12 - 13*q^10 + 21*q^8 - 22*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), 0, 0, ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^6), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), 0, 0, ((q^12 - 5*q^10 + 12*q^8 - 18*q^6 + 17*q^4 - 9*q^2 + 2) / q^3), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 35*q^8 - 28*q^6 + 16*q^4 - 6*q^2 + 1) / q^8), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^7)]
theorem cGR_4_9_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_9_v11 q) = cGR_4_9_v12 q := by
  rw [bridge4_0]; unfold cGR_4_9_v11 cGR_4_9_v12; stepTac
def cGR_4_9_v13 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^14 + 5*q^12 - 13*q^10 + 21*q^8 - 22*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), 0, 0, ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^6), 0, ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), 0, ((q^12 - 5*q^10 + 12*q^8 - 18*q^6 + 17*q^4 - 9*q^2 + 2) / q^3), 0, ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 35*q^8 - 28*q^6 + 16*q^4 - 6*q^2 + 1) / q^7), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^6)]
theorem cGR_4_9_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_9_v12 q) = cGR_4_9_v13 q := by
  rw [bridge4_1]; unfold cGR_4_9_v12 cGR_4_9_v13; stepTac
def cGR_4_9_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^14 + 5*q^12 - 13*q^10 + 21*q^8 - 22*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), 0, 0, ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^3), ((q^12 - 5*q^10 + 12*q^8 - 18*q^6 + 17*q^4 - 9*q^2 + 2) / q^3), 0, 0, ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 35*q^8 - 28*q^6 + 16*q^4 - 6*q^2 + 1) / q^6), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^5)]
theorem cGR_4_9_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_9_v13 q) = cGR_4_9_v14 q := by
  rw [bridge4_0]; unfold cGR_4_9_v13 cGR_4_9_v14; stepTac
theorem cGR_4_9_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 9 1) = cGR_4_9_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_9_v0_step q hq, cGR_4_9_v1_step q hq, cGR_4_9_v2_step q hq, cGR_4_9_v3_step q hq, cGR_4_9_v4_step q hq, cGR_4_9_v5_step q hq, cGR_4_9_v6_step q hq, cGR_4_9_v7_step q hq, cGR_4_9_v8_step q hq, cGR_4_9_v9_step q hq, cGR_4_9_v10_step q hq, cGR_4_9_v11_step q hq, cGR_4_9_v12_step q hq, cGR_4_9_v13_step q hq, cGR_4_9_v14_step q hq]
theorem cGR_4_9_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 9 9 = ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 9 9, cGR_4_9_col q hq]; simp [cGR_4_9_v14]

def cGR_2_2_v0 (q : R) : Fin 15 → R := ![0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_2_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 2 1) = cGR_2_2_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_2_v0; stepTac
def cGR_2_2_v1 (q : R) : Fin 15 → R := ![0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_2_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_2_v0 q) = cGR_2_2_v1 q := by
  rw [bridge2_2]; unfold cGR_2_2_v0 cGR_2_2_v1; stepTac
def cGR_2_2_v2 (q : R) : Fin 15 → R := ![((1) / q), ((-q^2 + 1) / q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_2_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_2_v1 q) = cGR_2_2_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_2_v1 cGR_2_2_v2; stepTac
def cGR_2_2_v3 (q : R) : Fin 15 → R := ![(1), ((-q^4 + 2*q^2 - 1) / q^3), ((-q^2 + 1) / q^2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_2_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_2_v2 q) = cGR_2_2_v3 q := by
  rw [bridge2_2]; unfold cGR_2_2_v2 cGR_2_2_v3; stepTac
def cGR_2_2_v4 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q^3), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), ((-q^2 + 1) / q^3), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_2_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_2_v3 q) = cGR_2_2_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_2_v3 cGR_2_2_v4; stepTac
def cGR_2_2_v5 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q^2), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_2_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_2_v4 q) = cGR_2_2_v5 q := by
  rw [bridge2_2]; unfold cGR_2_2_v4 cGR_2_2_v5; stepTac
def cGR_2_2_v6 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_2_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_2_v5 q) = cGR_2_2_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_2_v5 cGR_2_2_v6; stepTac
def cGR_2_2_v7 (q : R) : Fin 15 → R := ![((-q^6 + 3*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^5), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, 0, 0]
theorem cGR_2_2_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_2_v6 q) = cGR_2_2_v7 q := by
  rw [bridge2_3]; unfold cGR_2_2_v6 cGR_2_2_v7; stepTac
def cGR_2_2_v8 (q : R) : Fin 15 → R := ![((-q^6 + 3*q^4 - 3*q^2 + 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^5), 0, 0, ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^5), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^6), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, 0, 0]
theorem cGR_2_2_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_2_v7 q) = cGR_2_2_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_2_v7 cGR_2_2_v8; stepTac
def cGR_2_2_v9 (q : R) : Fin 15 → R := ![((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^6), ((-q^6 + 3*q^4 - 3*q^2 + 1) / q^5), ((q^8 - 3*q^6 + 5*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^4), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^7), 0, 0, ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^6), 0, 0, 0, 0, 0]
theorem cGR_2_2_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_2_v8 q) = cGR_2_2_v9 q := by
  rw [bridge2_3]; unfold cGR_2_2_v8 cGR_2_2_v9; stepTac
def cGR_2_2_v10 (q : R) : Fin 15 → R := ![((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^7), ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^4), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^7), 0, 0, ((q^12 - 5*q^10 + 12*q^8 - 18*q^6 + 17*q^4 - 9*q^2 + 2) / q^5), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^8), 0, 0, ((-q^10 + 4*q^8 - 8*q^6 + 9*q^4 - 5*q^2 + 1) / q^7), 0, 0, 0, 0, 0]
theorem cGR_2_2_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_2_v9 q) = cGR_2_2_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_2_v9 cGR_2_2_v10; stepTac
def cGR_2_2_v11 (q : R) : Fin 15 → R := ![((-q^14 + 5*q^12 - 13*q^10 + 21*q^8 - 22*q^6 + 15*q^4 - 6*q^2 + 1) / q^8), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^7), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((q^12 - 5*q^10 + 12*q^8 - 18*q^6 + 17*q^4 - 9*q^2 + 2) / q^4), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 35*q^8 - 28*q^6 + 16*q^4 - 6*q^2 + 1) / q^9), 0, 0, ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^8), 0, 0, 0, 0, 0]
theorem cGR_2_2_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_2_v10 q) = cGR_2_2_v11 q := by
  rw [bridge2_3]; unfold cGR_2_2_v10 cGR_2_2_v11; stepTac
def cGR_2_2_v12 (q : R) : Fin 15 → R := ![((-q^14 + 5*q^12 - 13*q^10 + 21*q^8 - 22*q^6 + 15*q^4 - 6*q^2 + 1) / q^7), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^6), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), 0, 0, ((q^12 - 5*q^10 + 12*q^8 - 18*q^6 + 17*q^4 - 9*q^2 + 2) / q^3), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 35*q^8 - 28*q^6 + 16*q^4 - 6*q^2 + 1) / q^8), 0, 0, ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^7), 0, 0, 0, 0, 0]
theorem cGR_2_2_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_2_v11 q) = cGR_2_2_v12 q := by
  rw [bridge2_0]; unfold cGR_2_2_v11 cGR_2_2_v12; stepTac
def cGR_2_2_v13 (q : R) : Fin 15 → R := ![((-q^14 + 5*q^12 - 13*q^10 + 21*q^8 - 22*q^6 + 15*q^4 - 6*q^2 + 1) / q^6), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^5), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^6), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), 0, ((q^12 - 5*q^10 + 12*q^8 - 18*q^6 + 17*q^4 - 9*q^2 + 2) / q^2), ((q^18 - 7*q^16 + 23*q^14 - 47*q^12 + 65*q^10 - 63*q^8 + 44*q^6 - 22*q^4 + 7*q^2 - 1) / q^9), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 35*q^8 - 28*q^6 + 16*q^4 - 6*q^2 + 1) / q^8), 0, ((q^16 - 6*q^14 + 18*q^12 - 34*q^10 + 43*q^8 - 37*q^6 + 21*q^4 - 7*q^2 + 1) / q^8), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^7), 0, 0, 0, 0]
theorem cGR_2_2_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_2_v12 q) = cGR_2_2_v13 q := by
  rw [bridge2_1]; unfold cGR_2_2_v12 cGR_2_2_v13; stepTac
def cGR_2_2_v14 (q : R) : Fin 15 → R := ![((-q^14 + 5*q^12 - 13*q^10 + 21*q^8 - 22*q^6 + 15*q^4 - 6*q^2 + 1) / q^5), ((q^10 - 4*q^8 + 8*q^6 - 9*q^4 + 5*q^2 - 1) / q^4), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^5), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^6), ((-q^12 + 5*q^10 - 11*q^8 + 15*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), ((q^12 - 5*q^10 + 12*q^8 - 18*q^6 + 17*q^4 - 9*q^2 + 2) / q), ((q^18 - 7*q^16 + 23*q^14 - 47*q^12 + 65*q^10 - 63*q^8 + 44*q^6 - 22*q^4 + 7*q^2 - 1) / q^8), ((q^18 - 7*q^16 + 23*q^14 - 47*q^12 + 65*q^10 - 63*q^8 + 44*q^6 - 22*q^4 + 7*q^2 - 1) / q^9), ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 35*q^8 - 28*q^6 + 16*q^4 - 6*q^2 + 1) / q^8), ((q^16 - 6*q^14 + 18*q^12 - 34*q^10 + 43*q^8 - 37*q^6 + 21*q^4 - 7*q^2 + 1) / q^7), ((q^16 - 6*q^14 + 18*q^12 - 34*q^10 + 43*q^8 - 37*q^6 + 21*q^4 - 7*q^2 + 1) / q^8), ((q^14 - 5*q^12 + 13*q^10 - 21*q^8 + 22*q^6 - 15*q^4 + 6*q^2 - 1) / q^7), 0, 0, 0]
theorem cGR_2_2_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_2_v13 q) = cGR_2_2_v14 q := by
  rw [bridge2_0]; unfold cGR_2_2_v13 cGR_2_2_v14; stepTac
theorem cGR_2_2_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 2 1) = cGR_2_2_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_2_v0_step q hq, cGR_2_2_v1_step q hq, cGR_2_2_v2_step q hq, cGR_2_2_v3_step q hq, cGR_2_2_v4_step q hq, cGR_2_2_v5_step q hq, cGR_2_2_v6_step q hq, cGR_2_2_v7_step q hq, cGR_2_2_v8_step q hq, cGR_2_2_v9_step q hq, cGR_2_2_v10_step q hq, cGR_2_2_v11_step q hq, cGR_2_2_v12_step q hq, cGR_2_2_v13_step q hq, cGR_2_2_v14_step q hq]
theorem cGR_2_2_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 2 2 = ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 26*q^6 + 16*q^4 - 6*q^2 + 1) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 2 2, cGR_2_2_col q hq]; simp [cGR_2_2_v14]

def cGR_2_3_v0 (q : R) : Fin 15 → R := ![0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_3_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 3 1) = cGR_2_3_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_3_v0; stepTac
def cGR_2_3_v1 (q : R) : Fin 15 → R := ![0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_3_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_3_v0 q) = cGR_2_3_v1 q := by
  rw [bridge2_2]; unfold cGR_2_3_v0 cGR_2_3_v1; stepTac
def cGR_2_3_v2 (q : R) : Fin 15 → R := ![0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_3_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_3_v1 q) = cGR_2_3_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_3_v1 cGR_2_3_v2; stepTac
def cGR_2_3_v3 (q : R) : Fin 15 → R := ![0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_3_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_3_v2 q) = cGR_2_3_v3 q := by
  rw [bridge2_2]; unfold cGR_2_3_v2 cGR_2_3_v3; stepTac
def cGR_2_3_v4 (q : R) : Fin 15 → R := ![0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_3_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_3_v3 q) = cGR_2_3_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_3_v3 cGR_2_3_v4; stepTac
def cGR_2_3_v5 (q : R) : Fin 15 → R := ![0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_3_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_3_v4 q) = cGR_2_3_v5 q := by
  rw [bridge2_2]; unfold cGR_2_3_v4 cGR_2_3_v5; stepTac
def cGR_2_3_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_3_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_3_v5 q) = cGR_2_3_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_3_v5 cGR_2_3_v6; stepTac
def cGR_2_3_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, 0, (1), 0, 0, 0, 0]
theorem cGR_2_3_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_3_v6 q) = cGR_2_3_v7 q := by
  rw [bridge2_3]; unfold cGR_2_3_v6 cGR_2_3_v7; stepTac
def cGR_2_3_v8 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^2 - 1) / q), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((1) / q), 0, 0, 0, 0]
theorem cGR_2_3_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_3_v7 q) = cGR_2_3_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_3_v7 cGR_2_3_v8; stepTac
def cGR_2_3_v9 (q : R) : Fin 15 → R := ![0, 0, 0, (q^2 - 1), 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0, 0]
theorem cGR_2_3_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_3_v8 q) = cGR_2_3_v9 q := by
  rw [bridge2_3]; unfold cGR_2_3_v8 cGR_2_3_v9; stepTac
def cGR_2_3_v10 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0, 0]
theorem cGR_2_3_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_3_v9 q) = cGR_2_3_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_3_v9 cGR_2_3_v10; stepTac
def cGR_2_3_v11 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, 0]
theorem cGR_2_3_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_3_v10 q) = cGR_2_3_v11 q := by
  rw [bridge2_3]; unfold cGR_2_3_v10 cGR_2_3_v11; stepTac
def cGR_2_3_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^8 + 4*q^6 - 5*q^4 + 3*q^2 - 1) / q^3), ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, ((q^12 - 5*q^10 + 10*q^8 - 11*q^6 + 8*q^4 - 4*q^2 + 1) / q^6), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0]
theorem cGR_2_3_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_3_v11 q) = cGR_2_3_v12 q := by
  rw [bridge2_0]; unfold cGR_2_3_v11 cGR_2_3_v12; stepTac
def cGR_2_3_v13 (q : R) : Fin 15 → R := ![0, 0, ((-q^8 + 4*q^6 - 5*q^4 + 3*q^2 - 1) / q^3), 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), 0, ((q^12 - 5*q^10 + 10*q^8 - 11*q^6 + 8*q^4 - 4*q^2 + 1) / q^6), 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0]
theorem cGR_2_3_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_3_v12 q) = cGR_2_3_v13 q := by
  rw [bridge2_1]; unfold cGR_2_3_v12 cGR_2_3_v13; stepTac
def cGR_2_3_v14 (q : R) : Fin 15 → R := ![0, 0, ((-q^8 + 4*q^6 - 5*q^4 + 3*q^2 - 1) / q^2), ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), 0, 0, ((q^12 - 5*q^10 + 10*q^8 - 11*q^6 + 8*q^4 - 4*q^2 + 1) / q^5), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^4), 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, 0]
theorem cGR_2_3_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_3_v13 q) = cGR_2_3_v14 q := by
  rw [bridge2_0]; unfold cGR_2_3_v13 cGR_2_3_v14; stepTac
theorem cGR_2_3_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 3 1) = cGR_2_3_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_3_v0_step q hq, cGR_2_3_v1_step q hq, cGR_2_3_v2_step q hq, cGR_2_3_v3_step q hq, cGR_2_3_v4_step q hq, cGR_2_3_v5_step q hq, cGR_2_3_v6_step q hq, cGR_2_3_v7_step q hq, cGR_2_3_v8_step q hq, cGR_2_3_v9_step q hq, cGR_2_3_v10_step q hq, cGR_2_3_v11_step q hq, cGR_2_3_v12_step q hq, cGR_2_3_v13_step q hq, cGR_2_3_v14_step q hq]
theorem cGR_2_3_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 3 3 = ((-q^6 + 3*q^4 - 2*q^2 + 1) / q) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 3 3, cGR_2_3_col q hq]; simp [cGR_2_3_v14]

def cGR_2_4_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_4_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 4 1) = cGR_2_4_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_4_v0; stepTac
def cGR_2_4_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_4_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_4_v0 q) = cGR_2_4_v1 q := by
  rw [bridge2_2]; unfold cGR_2_4_v0 cGR_2_4_v1; stepTac
def cGR_2_4_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_4_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_4_v1 q) = cGR_2_4_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_4_v1 cGR_2_4_v2; stepTac
def cGR_2_4_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_4_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_4_v2 q) = cGR_2_4_v3 q := by
  rw [bridge2_2]; unfold cGR_2_4_v2 cGR_2_4_v3; stepTac
def cGR_2_4_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((1) / q), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_4_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_4_v3 q) = cGR_2_4_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_4_v3 cGR_2_4_v4; stepTac
def cGR_2_4_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
theorem cGR_2_4_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_4_v4 q) = cGR_2_4_v5 q := by
  rw [bridge2_2]; unfold cGR_2_4_v4 cGR_2_4_v5; stepTac
def cGR_2_4_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0, 0, 0]
theorem cGR_2_4_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_4_v5 q) = cGR_2_4_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_4_v5 cGR_2_4_v6; stepTac
def cGR_2_4_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, 0, (1), 0, 0, 0]
theorem cGR_2_4_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_4_v6 q) = cGR_2_4_v7 q := by
  rw [bridge2_3]; unfold cGR_2_4_v6 cGR_2_4_v7; stepTac
def cGR_2_4_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^2 - 1) / q), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((1) / q), 0, 0, 0]
theorem cGR_2_4_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_4_v7 q) = cGR_2_4_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_4_v7 cGR_2_4_v8; stepTac
def cGR_2_4_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, (q^2 - 1), 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0]
theorem cGR_2_4_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_4_v8 q) = cGR_2_4_v9 q := by
  rw [bridge2_3]; unfold cGR_2_4_v8 cGR_2_4_v9; stepTac
def cGR_2_4_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0]
theorem cGR_2_4_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_4_v9 q) = cGR_2_4_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_4_v9 cGR_2_4_v10; stepTac
def cGR_2_4_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0]
theorem cGR_2_4_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_4_v10 q) = cGR_2_4_v11 q := by
  rw [bridge2_3]; unfold cGR_2_4_v10 cGR_2_4_v11; stepTac
def cGR_2_4_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, 0]
theorem cGR_2_4_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_4_v11 q) = cGR_2_4_v12 q := by
  rw [bridge2_0]; unfold cGR_2_4_v11 cGR_2_4_v12; stepTac
def cGR_2_4_v13 (q : R) : Fin 15 → R := ![0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, 0, 0]
theorem cGR_2_4_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_4_v12 q) = cGR_2_4_v13 q := by
  rw [bridge2_1]; unfold cGR_2_4_v12 cGR_2_4_v13; stepTac
def cGR_2_4_v14 (q : R) : Fin 15 → R := ![0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), 0, 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^4), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, 0, 0]
theorem cGR_2_4_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_4_v13 q) = cGR_2_4_v14 q := by
  rw [bridge2_0]; unfold cGR_2_4_v13 cGR_2_4_v14; stepTac
theorem cGR_2_4_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 4 1) = cGR_2_4_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_4_v0_step q hq, cGR_2_4_v1_step q hq, cGR_2_4_v2_step q hq, cGR_2_4_v3_step q hq, cGR_2_4_v4_step q hq, cGR_2_4_v5_step q hq, cGR_2_4_v6_step q hq, cGR_2_4_v7_step q hq, cGR_2_4_v8_step q hq, cGR_2_4_v9_step q hq, cGR_2_4_v10_step q hq, cGR_2_4_v11_step q hq, cGR_2_4_v12_step q hq, cGR_2_4_v13_step q hq, cGR_2_4_v14_step q hq]
theorem cGR_2_4_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 4 4 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 4 4, cGR_2_4_col q hq]; simp [cGR_2_4_v14]

def cGR_1_0_v0 (q : R) : Fin 6 → R := ![((1) / q), 0, 0, 0, 0, 0]
theorem cGR_1_0_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (Pi.single 0 1) = cGR_1_0_v0 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGR_1_0_v0; stepTac
def cGR_1_0_v1 (q : R) : Fin 6 → R := ![(1), 0, 0, 0, 0, 0]
theorem cGR_1_0_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGR_1_0_v0 q) = cGR_1_0_v1 q := by
  rw [bridge1_2]; unfold cGR_1_0_v0 cGR_1_0_v1; stepTac
def cGR_1_0_v2 (q : R) : Fin 6 → R := ![((1) / q), 0, 0, 0, 0, 0]
theorem cGR_1_0_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGR_1_0_v1 q) = cGR_1_0_v2 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGR_1_0_v1 cGR_1_0_v2; stepTac
def cGR_1_0_v3 (q : R) : Fin 6 → R := ![(1), 0, 0, 0, 0, 0]
theorem cGR_1_0_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGR_1_0_v2 q) = cGR_1_0_v3 q := by
  rw [bridge1_2]; unfold cGR_1_0_v2 cGR_1_0_v3; stepTac
def cGR_1_0_v4 (q : R) : Fin 6 → R := ![((1) / q), 0, 0, 0, 0, 0]
theorem cGR_1_0_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGR_1_0_v3 q) = cGR_1_0_v4 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGR_1_0_v3 cGR_1_0_v4; stepTac
def cGR_1_0_v5 (q : R) : Fin 6 → R := ![(1), 0, 0, 0, 0, 0]
theorem cGR_1_0_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGR_1_0_v4 q) = cGR_1_0_v5 q := by
  rw [bridge1_2]; unfold cGR_1_0_v4 cGR_1_0_v5; stepTac
def cGR_1_0_v6 (q : R) : Fin 6 → R := ![0, (1), 0, 0, 0, 0]
theorem cGR_1_0_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, true)).mulVec (cGR_1_0_v5 q) = cGR_1_0_v6 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_4]; unfold cGR_1_0_v5 cGR_1_0_v6; stepTac
def cGR_1_0_v7 (q : R) : Fin 6 → R := ![0, ((q^2 - 1) / q), (1), 0, 0, 0]
theorem cGR_1_0_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGR_1_0_v6 q) = cGR_1_0_v7 q := by
  rw [bridge1_3]; unfold cGR_1_0_v6 cGR_1_0_v7; stepTac
def cGR_1_0_v8 (q : R) : Fin 6 → R := ![((q^2 - 1) / q), ((-q^4 + 2*q^2 - 1) / q^2), ((1) / q), 0, 0, 0]
theorem cGR_1_0_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, true)).mulVec (cGR_1_0_v7 q) = cGR_1_0_v8 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_4]; unfold cGR_1_0_v7 cGR_1_0_v8; stepTac
def cGR_1_0_v9 (q : R) : Fin 6 → R := ![(q^2 - 1), ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, 0]
theorem cGR_1_0_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGR_1_0_v8 q) = cGR_1_0_v9 q := by
  rw [bridge1_3]; unfold cGR_1_0_v8 cGR_1_0_v9; stepTac
def cGR_1_0_v10 (q : R) : Fin 6 → R := ![((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, 0]
theorem cGR_1_0_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, true)).mulVec (cGR_1_0_v9 q) = cGR_1_0_v10 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_4]; unfold cGR_1_0_v9 cGR_1_0_v10; stepTac
def cGR_1_0_v11 (q : R) : Fin 6 → R := ![((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0]
theorem cGR_1_0_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGR_1_0_v10 q) = cGR_1_0_v11 q := by
  rw [bridge1_3]; unfold cGR_1_0_v10 cGR_1_0_v11; stepTac
def cGR_1_0_v12 (q : R) : Fin 6 → R := ![((-q^6 + 3*q^4 - 2*q^2 + 1) / q), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0]
theorem cGR_1_0_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGR_1_0_v11 q) = cGR_1_0_v12 q := by
  rw [bridge1_0]; unfold cGR_1_0_v11 cGR_1_0_v12; stepTac
def cGR_1_0_v13 (q : R) : Fin 6 → R := ![(-q^6 + 3*q^4 - 2*q^2 + 1), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^3), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, 0, 0]
theorem cGR_1_0_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, false)).mulVec (cGR_1_0_v12 q) = cGR_1_0_v13 q := by
  rw [bridge1_1]; unfold cGR_1_0_v12 cGR_1_0_v13; stepTac
def cGR_1_0_v14 (q : R) : Fin 6 → R := ![(-q^7 + 3*q^5 - 2*q^3 + q), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^2), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q), 0, 0, 0]
theorem cGR_1_0_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGR_1_0_v13 q) = cGR_1_0_v14 q := by
  rw [bridge1_0]; unfold cGR_1_0_v13 cGR_1_0_v14; stepTac
theorem cGR_1_0_col (q : R) (hq : q ≠ 0) :
    (wordW q idx1 wGR).mulVec (Pi.single 0 1) = cGR_1_0_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_1_0_v0_step q hq, cGR_1_0_v1_step q hq, cGR_1_0_v2_step q hq, cGR_1_0_v3_step q hq, cGR_1_0_v4_step q hq, cGR_1_0_v5_step q hq, cGR_1_0_v6_step q hq, cGR_1_0_v7_step q hq, cGR_1_0_v8_step q hq, cGR_1_0_v9_step q hq, cGR_1_0_v10_step q hq, cGR_1_0_v11_step q hq, cGR_1_0_v12_step q hq, cGR_1_0_v13_step q hq, cGR_1_0_v14_step q hq]
theorem cGR_1_0_entry (q : R) (hq : q ≠ 0) :
    wordW q idx1 wGR 0 0 = (-q^7 + 3*q^5 - 2*q^3 + q) := by
  rw [entry_eq_mulVec_single (wordW q idx1 wGR) 0 0, cGR_1_0_col q hq]; simp [cGR_1_0_v14]

def cGR_4_13_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1)]
theorem cGR_4_13_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 13 1) = cGR_4_13_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_13_v0; stepTac
def cGR_4_13_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (q)]
theorem cGR_4_13_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_13_v0 q) = cGR_4_13_v1 q := by
  rw [bridge4_2]; unfold cGR_4_13_v0 cGR_4_13_v1; stepTac
def cGR_4_13_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (q), (-q^2 + 1)]
theorem cGR_4_13_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_13_v1 q) = cGR_4_13_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_13_v1 cGR_4_13_v2; stepTac
def cGR_4_13_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (q), 0, (-q^3 + q)]
theorem cGR_4_13_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_13_v2 q) = cGR_4_13_v3 q := by
  rw [bridge4_2]; unfold cGR_4_13_v2 cGR_4_13_v3; stepTac
def cGR_4_13_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), (-q^3 + q), (q^4 - 2*q^2 + 1)]
theorem cGR_4_13_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_13_v3 q) = cGR_4_13_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_13_v3 cGR_4_13_v4; stepTac
def cGR_4_13_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), (1), (q^5 - 2*q^3 + q)]
theorem cGR_4_13_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_13_v4 q) = cGR_4_13_v5 q := by
  rw [bridge4_2]; unfold cGR_4_13_v4 cGR_4_13_v5; stepTac
def cGR_4_13_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), (1), 0, 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q^2), ((-q^2 + 1) / q), (q^4 - 2*q^2 + 1)]
theorem cGR_4_13_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_13_v5 q) = cGR_4_13_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_13_v5 cGR_4_13_v6; stepTac
def cGR_4_13_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, 0, 0, (q), 0, 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^2), ((-q^2 + 1) / q)]
theorem cGR_4_13_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_13_v6 q) = cGR_4_13_v7 q := by
  rw [bridge4_3]; unfold cGR_4_13_v6 cGR_4_13_v7; stepTac
def cGR_4_13_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^2), 0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^2), ((-q^8 + 4*q^6 - 5*q^4 + 4*q^2 - 1) / q^3), ((-q^2 + 1) / q^2)]
theorem cGR_4_13_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_13_v7 q) = cGR_4_13_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_13_v7 cGR_4_13_v8; stepTac
def cGR_4_13_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((q^6 - 3*q^4 + 3*q^2 - 1) / q), 0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^4), ((-q^8 + 4*q^6 - 5*q^4 + 4*q^2 - 1) / q^3)]
theorem cGR_4_13_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_13_v8 q) = cGR_4_13_v9 q := by
  rw [bridge4_3]; unfold cGR_4_13_v8 cGR_4_13_v9; stepTac
def cGR_4_13_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((q^10 - 5*q^8 + 10*q^6 - 11*q^4 + 7*q^2 - 2) / q^2), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^5), ((-q^8 + 4*q^6 - 5*q^4 + 4*q^2 - 1) / q^4)]
theorem cGR_4_13_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_13_v9 q) = cGR_4_13_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_13_v9 cGR_4_13_v10; stepTac
def cGR_4_13_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), 0, 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^3), 0, 0, ((q^10 - 5*q^8 + 10*q^6 - 11*q^4 + 7*q^2 - 2) / q), ((q^14 - 6*q^12 + 15*q^10 - 21*q^8 + 20*q^6 - 12*q^4 + 5*q^2 - 1) / q^6), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^5)]
theorem cGR_4_13_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_13_v10 q) = cGR_4_13_v11 q := by
  rw [bridge4_3]; unfold cGR_4_13_v10 cGR_4_13_v11; stepTac
def cGR_4_13_v12 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), 0, 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^2), 0, 0, (q^10 - 5*q^8 + 10*q^6 - 11*q^4 + 7*q^2 - 2), ((q^14 - 6*q^12 + 15*q^10 - 21*q^8 + 20*q^6 - 12*q^4 + 5*q^2 - 1) / q^5), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^4)]
theorem cGR_4_13_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_13_v11 q) = cGR_4_13_v12 q := by
  rw [bridge4_0]; unfold cGR_4_13_v11 cGR_4_13_v12; stepTac
def cGR_4_13_v13 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), 0, 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), 0, ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q), 0, (q^10 - 5*q^8 + 10*q^6 - 11*q^4 + 7*q^2 - 2), 0, ((q^14 - 6*q^12 + 15*q^10 - 21*q^8 + 20*q^6 - 12*q^4 + 5*q^2 - 1) / q^4), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^3)]
theorem cGR_4_13_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_13_v12 q) = cGR_4_13_v13 q := by
  rw [bridge4_1]; unfold cGR_4_13_v12 cGR_4_13_v13; stepTac
def cGR_4_13_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), 0, 0, ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), 0, 0, (-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1), (q^10 - 5*q^8 + 10*q^6 - 11*q^4 + 7*q^2 - 2), 0, 0, ((q^14 - 6*q^12 + 15*q^10 - 21*q^8 + 20*q^6 - 12*q^4 + 5*q^2 - 1) / q^3), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^2)]
theorem cGR_4_13_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_13_v13 q) = cGR_4_13_v14 q := by
  rw [bridge4_0]; unfold cGR_4_13_v13 cGR_4_13_v14; stepTac
theorem cGR_4_13_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 13 1) = cGR_4_13_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_13_v0_step q hq, cGR_4_13_v1_step q hq, cGR_4_13_v2_step q hq, cGR_4_13_v3_step q hq, cGR_4_13_v4_step q hq, cGR_4_13_v5_step q hq, cGR_4_13_v6_step q hq, cGR_4_13_v7_step q hq, cGR_4_13_v8_step q hq, cGR_4_13_v9_step q hq, cGR_4_13_v10_step q hq, cGR_4_13_v11_step q hq, cGR_4_13_v12_step q hq, cGR_4_13_v13_step q hq, cGR_4_13_v14_step q hq]
theorem cGR_4_13_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 13 13 = ((q^14 - 6*q^12 + 15*q^10 - 21*q^8 + 20*q^6 - 12*q^4 + 5*q^2 - 1) / q^3) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 13 13, cGR_4_13_col q hq]; simp [cGR_4_13_v14]

def cGR_2_6_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0, 0]
theorem cGR_2_6_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 6 1) = cGR_2_6_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_6_v0; stepTac
def cGR_2_6_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, (q), 0, 0, 0, 0, 0]
theorem cGR_2_6_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_6_v0 q) = cGR_2_6_v1 q := by
  rw [bridge2_2]; unfold cGR_2_6_v0 cGR_2_6_v1; stepTac
def cGR_2_6_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, (q), 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0]
theorem cGR_2_6_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_6_v1 q) = cGR_2_6_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_6_v1 cGR_2_6_v2; stepTac
def cGR_2_6_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (q), 0, 0, 0, (-q^3 + q), 0, 0, 0, 0, 0]
theorem cGR_2_6_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_6_v2 q) = cGR_2_6_v3 q := by
  rw [bridge2_2]; unfold cGR_2_6_v2 cGR_2_6_v3; stepTac
def cGR_2_6_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (1), (-q^3 + q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0]
theorem cGR_2_6_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_6_v3 q) = cGR_2_6_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_6_v3 cGR_2_6_v4; stepTac
def cGR_2_6_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), (1), 0, 0, (q^5 - 2*q^3 + q), 0, 0, 0, 0, 0]
theorem cGR_2_6_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_6_v4 q) = cGR_2_6_v5 q := by
  rw [bridge2_2]; unfold cGR_2_6_v4 cGR_2_6_v5; stepTac
def cGR_2_6_v6 (q : R) : Fin 15 → R := ![0, ((-q^4 + 2*q^2 - 1) / q), (1), 0, 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q^2), ((-q^2 + 1) / q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0]
theorem cGR_2_6_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_6_v5 q) = cGR_2_6_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_6_v5 cGR_2_6_v6; stepTac
def cGR_2_6_v7 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q), 0, (q), 0, 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^2), 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0, 0]
theorem cGR_2_6_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_6_v6 q) = cGR_2_6_v7 q := by
  rw [bridge2_3]; unfold cGR_2_6_v6 cGR_2_6_v7; stepTac
def cGR_2_6_v8 (q : R) : Fin 15 → R := ![((-q^4 + 2*q^2 - 1) / q^2), ((q^6 - 3*q^4 + 3*q^2 - 1) / q), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^2), 0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q^2), ((-q^8 + 4*q^6 - 5*q^4 + 4*q^2 - 1) / q^3), 0, 0, ((-q^2 + 1) / q^2), 0, 0, 0, 0, 0]
theorem cGR_2_6_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_6_v7 q) = cGR_2_6_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_6_v7 cGR_2_6_v8; stepTac
def cGR_2_6_v9 (q : R) : Fin 15 → R := ![((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), ((q^6 - 3*q^4 + 3*q^2 - 1) / q), 0, 0, ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((-q^8 + 4*q^6 - 5*q^4 + 4*q^2 - 1) / q^3), 0, 0, 0, 0, 0]
theorem cGR_2_6_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_6_v8 q) = cGR_2_6_v9 q := by
  rw [bridge2_3]; unfold cGR_2_6_v8 cGR_2_6_v9; stepTac
def cGR_2_6_v10 (q : R) : Fin 15 → R := ![((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), ((-q^8 + 4*q^6 - 6*q^4 + 4*q^2 - 1) / q), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((q^10 - 5*q^8 + 10*q^6 - 11*q^4 + 7*q^2 - 2) / q^2), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^5), 0, 0, ((-q^8 + 4*q^6 - 5*q^4 + 4*q^2 - 1) / q^4), 0, 0, 0, 0, 0]
theorem cGR_2_6_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_6_v9 q) = cGR_2_6_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_6_v9 cGR_2_6_v10; stepTac
def cGR_2_6_v11 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^3), 0, 0, ((q^10 - 5*q^8 + 10*q^6 - 11*q^4 + 7*q^2 - 2) / q), ((q^14 - 6*q^12 + 15*q^10 - 21*q^8 + 20*q^6 - 12*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^5), 0, 0, 0, 0, 0]
theorem cGR_2_6_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_6_v10 q) = cGR_2_6_v11 q := by
  rw [bridge2_3]; unfold cGR_2_6_v10 cGR_2_6_v11; stepTac
def cGR_2_6_v12 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^3), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^2), 0, 0, (q^10 - 5*q^8 + 10*q^6 - 11*q^4 + 7*q^2 - 2), ((q^14 - 6*q^12 + 15*q^10 - 21*q^8 + 20*q^6 - 12*q^4 + 5*q^2 - 1) / q^5), 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^4), 0, 0, 0, 0, 0]
theorem cGR_2_6_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_6_v11 q) = cGR_2_6_v12 q := by
  rw [bridge2_0]; unfold cGR_2_6_v11 cGR_2_6_v12; stepTac
def cGR_2_6_v13 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^3), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q^2), ((-q^12 + 6*q^10 - 14*q^8 + 17*q^6 - 12*q^4 + 5*q^2 - 1) / q^3), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^2), 0, (q^11 - 5*q^9 + 10*q^7 - 11*q^5 + 7*q^3 - 2*q), ((q^16 - 7*q^14 + 21*q^12 - 36*q^10 + 41*q^8 - 32*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), ((q^14 - 6*q^12 + 15*q^10 - 21*q^8 + 20*q^6 - 12*q^4 + 5*q^2 - 1) / q^5), 0, ((q^14 - 6*q^12 + 16*q^10 - 25*q^8 + 25*q^6 - 16*q^4 + 6*q^2 - 1) / q^5), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^4), 0, 0, 0, 0]
theorem cGR_2_6_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_6_v12 q) = cGR_2_6_v13 q := by
  rw [bridge2_1]; unfold cGR_2_6_v12 cGR_2_6_v13; stepTac
def cGR_2_6_v14 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^2), ((q^8 - 4*q^6 + 6*q^4 - 4*q^2 + 1) / q), ((-q^12 + 6*q^10 - 14*q^8 + 17*q^6 - 12*q^4 + 5*q^2 - 1) / q^2), ((-q^12 + 6*q^10 - 14*q^8 + 17*q^6 - 12*q^4 + 5*q^2 - 1) / q^3), ((-q^10 + 5*q^8 - 9*q^6 + 8*q^4 - 4*q^2 + 1) / q^2), (q^12 - 5*q^10 + 10*q^8 - 11*q^6 + 7*q^4 - 2*q^2), ((q^16 - 7*q^14 + 21*q^12 - 36*q^10 + 41*q^8 - 32*q^6 + 17*q^4 - 6*q^2 + 1) / q^5), ((q^16 - 7*q^14 + 21*q^12 - 36*q^10 + 41*q^8 - 32*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), ((q^14 - 6*q^12 + 15*q^10 - 21*q^8 + 20*q^6 - 12*q^4 + 5*q^2 - 1) / q^5), ((q^14 - 6*q^12 + 16*q^10 - 25*q^8 + 25*q^6 - 16*q^4 + 6*q^2 - 1) / q^4), ((q^14 - 6*q^12 + 16*q^10 - 25*q^8 + 25*q^6 - 16*q^4 + 6*q^2 - 1) / q^5), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^4), 0, 0, 0]
theorem cGR_2_6_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_6_v13 q) = cGR_2_6_v14 q := by
  rw [bridge2_0]; unfold cGR_2_6_v13 cGR_2_6_v14; stepTac
theorem cGR_2_6_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 6 1) = cGR_2_6_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_6_v0_step q hq, cGR_2_6_v1_step q hq, cGR_2_6_v2_step q hq, cGR_2_6_v3_step q hq, cGR_2_6_v4_step q hq, cGR_2_6_v5_step q hq, cGR_2_6_v6_step q hq, cGR_2_6_v7_step q hq, cGR_2_6_v8_step q hq, cGR_2_6_v9_step q hq, cGR_2_6_v10_step q hq, cGR_2_6_v11_step q hq, cGR_2_6_v12_step q hq, cGR_2_6_v13_step q hq, cGR_2_6_v14_step q hq]
theorem cGR_2_6_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 6 6 = ((q^16 - 7*q^14 + 21*q^12 - 36*q^10 + 41*q^8 - 32*q^6 + 17*q^4 - 6*q^2 + 1) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 6 6, cGR_2_6_col q hq]; simp [cGR_2_6_v14]

def cGR_2_7_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0, 0]
theorem cGR_2_7_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 7 1) = cGR_2_7_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_7_v0; stepTac
def cGR_2_7_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, (1), 0, 0]
theorem cGR_2_7_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_7_v0 q) = cGR_2_7_v1 q := by
  rw [bridge2_2]; unfold cGR_2_7_v0 cGR_2_7_v1; stepTac
def cGR_2_7_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((1) / q), 0, 0]
theorem cGR_2_7_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_7_v1 q) = cGR_2_7_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_7_v1 cGR_2_7_v2; stepTac
def cGR_2_7_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (q^2 - 1), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0]
theorem cGR_2_7_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_7_v2 q) = cGR_2_7_v3 q := by
  rw [bridge2_2]; unfold cGR_2_7_v2 cGR_2_7_v3; stepTac
def cGR_2_7_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^4 + 2*q^2 - 1) / q^3), 0, 0]
theorem cGR_2_7_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_7_v3 q) = cGR_2_7_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_7_v3 cGR_2_7_v4; stepTac
def cGR_2_7_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0]
theorem cGR_2_7_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_7_v4 q) = cGR_2_7_v5 q := by
  rw [bridge2_2]; unfold cGR_2_7_v4 cGR_2_7_v5; stepTac
def cGR_2_7_v6 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, 0, ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^6), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, 0]
theorem cGR_2_7_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_7_v5 q) = cGR_2_7_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_7_v5 cGR_2_7_v6; stepTac
def cGR_2_7_v7 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), 0, 0, 0, ((q^12 - 4*q^10 + 5*q^8 - 2*q^6 - q^4 + 2*q^2 - 1) / q^6), 0, 0, ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0]
theorem cGR_2_7_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_7_v6 q) = cGR_2_7_v7 q := by
  rw [bridge2_3]; unfold cGR_2_7_v6 cGR_2_7_v7; stepTac
def cGR_2_7_v8 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^12 - 4*q^10 + 5*q^8 - 2*q^6 - q^4 + 2*q^2 - 1) / q^6), 0, 0, 0, ((-q^14 + 4*q^12 - 6*q^10 + 5*q^8 - 3*q^4 + 3*q^2 - 1) / q^7), 0, 0, ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, 0]
theorem cGR_2_7_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_7_v7 q) = cGR_2_7_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_7_v7 cGR_2_7_v8; stepTac
def cGR_2_7_v9 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^12 - 4*q^10 + 5*q^8 - 2*q^6 - q^4 + 2*q^2 - 1) / q^5), 0, 0, 0, ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^8), 0, 0, ((-q^14 + 4*q^12 - 6*q^10 + 5*q^8 - 3*q^4 + 3*q^2 - 1) / q^7), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0]
theorem cGR_2_7_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_7_v8 q) = cGR_2_7_v9 q := by
  rw [bridge2_3]; unfold cGR_2_7_v8 cGR_2_7_v9; stepTac
def cGR_2_7_v10 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^8), 0, 0, 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((-q^14 + 4*q^12 - 6*q^10 + 5*q^8 - 3*q^4 + 3*q^2 - 1) / q^8), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, 0]
theorem cGR_2_7_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_7_v9 q) = cGR_2_7_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_7_v9 cGR_2_7_v10; stepTac
def cGR_2_7_v11 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^7), 0, 0, 0, ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^10), 0, 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0]
theorem cGR_2_7_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_7_v10 q) = cGR_2_7_v11 q := by
  rw [bridge2_3]; unfold cGR_2_7_v10 cGR_2_7_v11; stepTac
def cGR_2_7_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^18 + 6*q^16 - 14*q^14 + 16*q^12 - 7*q^10 - 6*q^8 + 13*q^6 - 11*q^4 + 5*q^2 - 1) / q^8), ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^7), 0, 0, ((q^22 - 7*q^20 + 20*q^18 - 31*q^16 + 27*q^14 - 5*q^12 - 21*q^10 + 34*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^11), ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^10), 0, ((q^20 - 6*q^18 + 15*q^16 - 21*q^14 + 16*q^12 - 16*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^10), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0]
theorem cGR_2_7_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_7_v11 q) = cGR_2_7_v12 q := by
  rw [bridge2_0]; unfold cGR_2_7_v11 cGR_2_7_v12; stepTac
def cGR_2_7_v13 (q : R) : Fin 15 → R := ![0, 0, ((-q^18 + 6*q^16 - 14*q^14 + 16*q^12 - 7*q^10 - 6*q^8 + 13*q^6 - 11*q^4 + 5*q^2 - 1) / q^8), 0, ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^6), 0, ((q^22 - 7*q^20 + 20*q^18 - 31*q^16 + 27*q^14 - 5*q^12 - 21*q^10 + 34*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^11), 0, ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^9), ((q^20 - 6*q^18 + 15*q^16 - 21*q^14 + 16*q^12 - 16*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^10), 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4)]
theorem cGR_2_7_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_7_v12 q) = cGR_2_7_v13 q := by
  rw [bridge2_1]; unfold cGR_2_7_v12 cGR_2_7_v13; stepTac
def cGR_2_7_v14 (q : R) : Fin 15 → R := ![0, 0, ((-q^18 + 6*q^16 - 14*q^14 + 16*q^12 - 7*q^10 - 6*q^8 + 13*q^6 - 11*q^4 + 5*q^2 - 1) / q^7), ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^6), 0, 0, ((q^22 - 7*q^20 + 20*q^18 - 31*q^16 + 27*q^14 - 5*q^12 - 21*q^10 + 34*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^10), ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^9), 0, ((q^20 - 6*q^18 + 15*q^16 - 21*q^14 + 16*q^12 - 16*q^8 + 21*q^6 - 15*q^4 + 6*q^2 - 1) / q^9), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3)]
theorem cGR_2_7_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_7_v13 q) = cGR_2_7_v14 q := by
  rw [bridge2_0]; unfold cGR_2_7_v13 cGR_2_7_v14; stepTac
theorem cGR_2_7_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 7 1) = cGR_2_7_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_7_v0_step q hq, cGR_2_7_v1_step q hq, cGR_2_7_v2_step q hq, cGR_2_7_v3_step q hq, cGR_2_7_v4_step q hq, cGR_2_7_v5_step q hq, cGR_2_7_v6_step q hq, cGR_2_7_v7_step q hq, cGR_2_7_v8_step q hq, cGR_2_7_v9_step q hq, cGR_2_7_v10_step q hq, cGR_2_7_v11_step q hq, cGR_2_7_v12_step q hq, cGR_2_7_v13_step q hq, cGR_2_7_v14_step q hq]
theorem cGR_2_7_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 7 7 = ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^9) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 7 7, cGR_2_7_col q hq]; simp [cGR_2_7_v14]

def cGR_2_8_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, 0]
theorem cGR_2_8_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 8 1) = cGR_2_8_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_8_v0; stepTac
def cGR_2_8_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, (1), 0]
theorem cGR_2_8_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_8_v0 q) = cGR_2_8_v1 q := by
  rw [bridge2_2]; unfold cGR_2_8_v0 cGR_2_8_v1; stepTac
def cGR_2_8_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^2 - 1) / q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((1) / q), 0]
theorem cGR_2_8_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_8_v1 q) = cGR_2_8_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_8_v1 cGR_2_8_v2; stepTac
def cGR_2_8_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, (q^2 - 1), 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, ((-q^4 + 2*q^2 - 1) / q^2), 0]
theorem cGR_2_8_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_8_v2 q) = cGR_2_8_v3 q := by
  rw [bridge2_2]; unfold cGR_2_8_v2 cGR_2_8_v3; stepTac
def cGR_2_8_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^4 + 2*q^2 - 1) / q^3), 0]
theorem cGR_2_8_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_8_v3 q) = cGR_2_8_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_8_v3 cGR_2_8_v4; stepTac
def cGR_2_8_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0]
theorem cGR_2_8_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_8_v4 q) = cGR_2_8_v5 q := by
  rw [bridge2_2]; unfold cGR_2_8_v4 cGR_2_8_v5; stepTac
def cGR_2_8_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), 0, 0, 0, ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^6), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0]
theorem cGR_2_8_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_8_v5 q) = cGR_2_8_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_8_v5 cGR_2_8_v6; stepTac
def cGR_2_8_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q), 0, 0, 0, ((q^12 - 4*q^10 + 5*q^8 - 2*q^6 - q^4 + 2*q^2 - 1) / q^6), 0, 0, ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0]
theorem cGR_2_8_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_8_v6 q) = cGR_2_8_v7 q := by
  rw [bridge2_3]; unfold cGR_2_8_v6 cGR_2_8_v7; stepTac
def cGR_2_8_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^12 - 4*q^10 + 5*q^8 - 2*q^6 - q^4 + 2*q^2 - 1) / q^6), 0, 0, 0, ((-q^14 + 4*q^12 - 6*q^10 + 5*q^8 - 3*q^4 + 3*q^2 - 1) / q^7), 0, 0, ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0]
theorem cGR_2_8_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_8_v7 q) = cGR_2_8_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_8_v7 cGR_2_8_v8; stepTac
def cGR_2_8_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^12 - 4*q^10 + 5*q^8 - 2*q^6 - q^4 + 2*q^2 - 1) / q^5), 0, 0, 0, ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^8), 0, 0, ((-q^14 + 4*q^12 - 6*q^10 + 5*q^8 - 3*q^4 + 3*q^2 - 1) / q^7), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0]
theorem cGR_2_8_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_8_v8 q) = cGR_2_8_v9 q := by
  rw [bridge2_3]; unfold cGR_2_8_v8 cGR_2_8_v9; stepTac
def cGR_2_8_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^8), 0, 0, 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((-q^14 + 4*q^12 - 6*q^10 + 5*q^8 - 3*q^4 + 3*q^2 - 1) / q^8), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0]
theorem cGR_2_8_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_8_v9 q) = cGR_2_8_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_8_v9 cGR_2_8_v10; stepTac
def cGR_2_8_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^7), 0, 0, 0, ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^10), 0, 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0]
theorem cGR_2_8_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_8_v10 q) = cGR_2_8_v11 q := by
  rw [bridge2_3]; unfold cGR_2_8_v10 cGR_2_8_v11; stepTac
def cGR_2_8_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^7), 0, 0, 0, ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^10), 0, 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0]
theorem cGR_2_8_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_8_v11 q) = cGR_2_8_v12 q := by
  rw [bridge2_0]; unfold cGR_2_8_v11 cGR_2_8_v12; stepTac
def cGR_2_8_v13 (q : R) : Fin 15 → R := ![0, 0, ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^7), 0, 0, 0, ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^10), 0, 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0]
theorem cGR_2_8_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_8_v12 q) = cGR_2_8_v13 q := by
  rw [bridge2_1]; unfold cGR_2_8_v12 cGR_2_8_v13; stepTac
def cGR_2_8_v14 (q : R) : Fin 15 → R := ![0, 0, ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^6), 0, 0, 0, ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^9), 0, 0, ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, 0, ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0]
theorem cGR_2_8_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_8_v13 q) = cGR_2_8_v14 q := by
  rw [bridge2_0]; unfold cGR_2_8_v13 cGR_2_8_v14; stepTac
theorem cGR_2_8_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 8 1) = cGR_2_8_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_8_v0_step q hq, cGR_2_8_v1_step q hq, cGR_2_8_v2_step q hq, cGR_2_8_v3_step q hq, cGR_2_8_v4_step q hq, cGR_2_8_v5_step q hq, cGR_2_8_v6_step q hq, cGR_2_8_v7_step q hq, cGR_2_8_v8_step q hq, cGR_2_8_v9_step q hq, cGR_2_8_v10_step q hq, cGR_2_8_v11_step q hq, cGR_2_8_v12_step q hq, cGR_2_8_v13_step q hq, cGR_2_8_v14_step q hq]
theorem cGR_2_8_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 8 8 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 8 8, cGR_2_8_col q hq]; simp [cGR_2_8_v14]

def cGR_1_1_v0 (q : R) : Fin 6 → R := ![0, 0, (1), 0, 0, 0]
theorem cGR_1_1_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (Pi.single 1 1) = cGR_1_1_v0 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGR_1_1_v0; stepTac
def cGR_1_1_v1 (q : R) : Fin 6 → R := ![0, 0, ((q^2 - 1) / q), (1), 0, 0]
theorem cGR_1_1_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGR_1_1_v0 q) = cGR_1_1_v1 q := by
  rw [bridge1_2]; unfold cGR_1_1_v0 cGR_1_1_v1; stepTac
def cGR_1_1_v2 (q : R) : Fin 6 → R := ![0, ((q^2 - 1) / q), ((-q^4 + 2*q^2 - 1) / q^2), ((1) / q), 0, 0]
theorem cGR_1_1_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGR_1_1_v1 q) = cGR_1_1_v2 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGR_1_1_v1 cGR_1_1_v2; stepTac
def cGR_1_1_v3 (q : R) : Fin 6 → R := ![0, (q^2 - 1), ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), ((-q^4 + 2*q^2 - 1) / q^2), 0, 0]
theorem cGR_1_1_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGR_1_1_v2 q) = cGR_1_1_v3 q := by
  rw [bridge1_2]; unfold cGR_1_1_v2 cGR_1_1_v3; stepTac
def cGR_1_1_v4 (q : R) : Fin 6 → R := ![0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^3), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0]
theorem cGR_1_1_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGR_1_1_v3 q) = cGR_1_1_v4 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGR_1_1_v3 cGR_1_1_v4; stepTac
def cGR_1_1_v5 (q : R) : Fin 6 → R := ![0, ((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^5), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0]
theorem cGR_1_1_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGR_1_1_v4 q) = cGR_1_1_v5 q := by
  rw [bridge1_2]; unfold cGR_1_1_v4 cGR_1_1_v5; stepTac
def cGR_1_1_v6 (q : R) : Fin 6 → R := ![((-q^6 + 3*q^4 - 2*q^2 + 1) / q^2), ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), ((q^10 - 4*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / q^6), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, 0]
theorem cGR_1_1_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, true)).mulVec (cGR_1_1_v5 q) = cGR_1_1_v6 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_4]; unfold cGR_1_1_v5 cGR_1_1_v6; stepTac
def cGR_1_1_v7 (q : R) : Fin 6 → R := ![((-q^6 + 3*q^4 - 2*q^2 + 1) / q), ((q^12 - 4*q^10 + 5*q^8 - 2*q^6 - q^4 + 2*q^2 - 1) / q^6), ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^3), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0]
theorem cGR_1_1_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGR_1_1_v6 q) = cGR_1_1_v7 q := by
  rw [bridge1_3]; unfold cGR_1_1_v6 cGR_1_1_v7; stepTac
def cGR_1_1_v8 (q : R) : Fin 6 → R := ![((q^12 - 4*q^10 + 5*q^8 - 2*q^6 - q^4 + 2*q^2 - 1) / q^6), ((-q^14 + 4*q^12 - 6*q^10 + 5*q^8 - 3*q^4 + 3*q^2 - 1) / q^7), ((q^8 - 4*q^6 + 5*q^4 - 3*q^2 + 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, 0]
theorem cGR_1_1_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, true)).mulVec (cGR_1_1_v7 q) = cGR_1_1_v8 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_4]; unfold cGR_1_1_v7 cGR_1_1_v8; stepTac
def cGR_1_1_v9 (q : R) : Fin 6 → R := ![((q^12 - 4*q^10 + 5*q^8 - 2*q^6 - q^4 + 2*q^2 - 1) / q^5), ((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^8), ((-q^14 + 4*q^12 - 6*q^10 + 5*q^8 - 3*q^4 + 3*q^2 - 1) / q^7), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0]
theorem cGR_1_1_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGR_1_1_v8 q) = cGR_1_1_v9 q := by
  rw [bridge1_3]; unfold cGR_1_1_v8 cGR_1_1_v9; stepTac
def cGR_1_1_v10 (q : R) : Fin 6 → R := ![((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^8), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((-q^14 + 4*q^12 - 6*q^10 + 5*q^8 - 3*q^4 + 3*q^2 - 1) / q^8), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, 0]
theorem cGR_1_1_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, true)).mulVec (cGR_1_1_v9 q) = cGR_1_1_v10 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_4]; unfold cGR_1_1_v9 cGR_1_1_v10; stepTac
def cGR_1_1_v11 (q : R) : Fin 6 → R := ![((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^7), ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^10), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0]
theorem cGR_1_1_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGR_1_1_v10 q) = cGR_1_1_v11 q := by
  rw [bridge1_3]; unfold cGR_1_1_v10 cGR_1_1_v11; stepTac
def cGR_1_1_v12 (q : R) : Fin 6 → R := ![((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^6), ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^9), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0]
theorem cGR_1_1_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGR_1_1_v11 q) = cGR_1_1_v12 q := by
  rw [bridge1_0]; unfold cGR_1_1_v11 cGR_1_1_v12; stepTac
def cGR_1_1_v13 (q : R) : Fin 6 → R := ![((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^5), ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^8), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0]
theorem cGR_1_1_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, false)).mulVec (cGR_1_1_v12 q) = cGR_1_1_v13 q := by
  rw [bridge1_1]; unfold cGR_1_1_v12 cGR_1_1_v13; stepTac
def cGR_1_1_v14 (q : R) : Fin 6 → R := ![((-q^16 + 5*q^14 - 9*q^12 + 7*q^10 - 6*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^7), ((q^18 - 5*q^16 + 10*q^14 - 11*q^12 + 5*q^10 + 5*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^3), ((q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / q^4), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3)]
theorem cGR_1_1_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGR_1_1_v13 q) = cGR_1_1_v14 q := by
  rw [bridge1_0]; unfold cGR_1_1_v13 cGR_1_1_v14; stepTac
theorem cGR_1_1_col (q : R) (hq : q ≠ 0) :
    (wordW q idx1 wGR).mulVec (Pi.single 1 1) = cGR_1_1_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_1_1_v0_step q hq, cGR_1_1_v1_step q hq, cGR_1_1_v2_step q hq, cGR_1_1_v3_step q hq, cGR_1_1_v4_step q hq, cGR_1_1_v5_step q hq, cGR_1_1_v6_step q hq, cGR_1_1_v7_step q hq, cGR_1_1_v8_step q hq, cGR_1_1_v9_step q hq, cGR_1_1_v10_step q hq, cGR_1_1_v11_step q hq, cGR_1_1_v12_step q hq, cGR_1_1_v13_step q hq, cGR_1_1_v14_step q hq]
theorem cGR_1_1_entry (q : R) (hq : q ≠ 0) :
    wordW q idx1 wGR 1 1 = ((q^20 - 6*q^18 + 14*q^16 - 17*q^14 + 10*q^12 + 5*q^10 - 16*q^8 + 18*q^6 - 12*q^4 + 5*q^2 - 1) / q^7) := by
  rw [entry_eq_mulVec_single (wordW q idx1 wGR) 1 1, cGR_1_1_col q hq]; simp [cGR_1_1_v14]

def cGR_4_14_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), ((-q^2 + 1) / q)]
theorem cGR_4_14_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (Pi.single 14 1) = cGR_4_14_v0 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_14_v0; stepTac
def cGR_4_14_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (1), 0, (-q^2 + 1)]
theorem cGR_4_14_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_14_v0 q) = cGR_4_14_v1 q := by
  rw [bridge4_2]; unfold cGR_4_14_v0 cGR_4_14_v1; stepTac
def cGR_4_14_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((1) / q), (-q^2 + 1), ((q^4 - 2*q^2 + 1) / q)]
theorem cGR_4_14_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_14_v1 q) = cGR_4_14_v2 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_14_v1 cGR_4_14_v2; stepTac
def cGR_4_14_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((1) / q), (q^4 - 2*q^2 + 1)]
theorem cGR_4_14_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_14_v2 q) = cGR_4_14_v3 q := by
  rw [bridge4_2]; unfold cGR_4_14_v2 cGR_4_14_v3; stepTac
def cGR_4_14_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), (q^4 - 2*q^2 + 1), ((-q^6 + 3*q^4 - 3*q^2 + 2) / q)]
theorem cGR_4_14_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, true)).mulVec (cGR_4_14_v3 q) = cGR_4_14_v4 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_3]; unfold cGR_4_14_v3 cGR_4_14_v4; stepTac
def cGR_4_14_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), (-q^6 + 3*q^4 - 3*q^2 + 2)]
theorem cGR_4_14_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (2, false)).mulVec (cGR_4_14_v4 q) = cGR_4_14_v5 q := by
  rw [bridge4_2]; unfold cGR_4_14_v4 cGR_4_14_v5; stepTac
def cGR_4_14_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^5), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^4), ((-q^6 + 3*q^4 - 3*q^2 + 2) / q)]
theorem cGR_4_14_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_14_v5 q) = cGR_4_14_v6 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_14_v5 cGR_4_14_v6; stepTac
def cGR_4_14_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 4*q^2 + 1) / q^5), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^4)]
theorem cGR_4_14_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_14_v6 q) = cGR_4_14_v7 q := by
  rw [bridge4_3]; unfold cGR_4_14_v6 cGR_4_14_v7; stepTac
def cGR_4_14_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 4*q^2 + 1) / q^5), 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^5), ((q^12 - 5*q^10 + 10*q^8 - 13*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^5)]
theorem cGR_4_14_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_14_v7 q) = cGR_4_14_v8 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_14_v7 cGR_4_14_v8; stepTac
def cGR_4_14_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^4), ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^7), ((q^12 - 5*q^10 + 10*q^8 - 13*q^6 + 11*q^4 - 5*q^2 + 1) / q^6)]
theorem cGR_4_14_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_14_v8 q) = cGR_4_14_v9 q := by
  rw [bridge4_3]; unfold cGR_4_14_v8 cGR_4_14_v9; stepTac
def cGR_4_14_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^7), 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^4), ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^7), 0, 0, ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q^5), ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^8), ((q^12 - 5*q^10 + 10*q^8 - 13*q^6 + 11*q^4 - 5*q^2 + 1) / q^7)]
theorem cGR_4_14_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (4, true)).mulVec (cGR_4_14_v9 q) = cGR_4_14_v10 q := by
  rw [gW_inv_mulVec q idx4 idx4_inj, bridge4_4]; unfold cGR_4_14_v9 cGR_4_14_v10; stepTac
def cGR_4_14_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^8), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^7), ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q^4), ((-q^18 + 7*q^16 - 22*q^14 + 42*q^12 - 55*q^10 + 52*q^8 - 36*q^6 + 18*q^4 - 6*q^2 + 1) / q^9), ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^8)]
theorem cGR_4_14_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (3, false)).mulVec (cGR_4_14_v10 q) = cGR_4_14_v11 q := by
  rw [bridge4_3]; unfold cGR_4_14_v10 cGR_4_14_v11; stepTac
def cGR_4_14_v12 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^7), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^5), 0, 0, ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q^3), ((-q^18 + 7*q^16 - 22*q^14 + 42*q^12 - 55*q^10 + 52*q^8 - 36*q^6 + 18*q^4 - 6*q^2 + 1) / q^8), ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^7)]
theorem cGR_4_14_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_14_v11 q) = cGR_4_14_v12 q := by
  rw [bridge4_0]; unfold cGR_4_14_v11 cGR_4_14_v12; stepTac
def cGR_4_14_v13 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^7), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), 0, ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^4), 0, ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q^3), 0, ((-q^18 + 7*q^16 - 22*q^14 + 42*q^12 - 55*q^10 + 52*q^8 - 36*q^6 + 18*q^4 - 6*q^2 + 1) / q^7), ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^6)]
theorem cGR_4_14_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (1, false)).mulVec (cGR_4_14_v12 q) = cGR_4_14_v13 q := by
  rw [bridge4_1]; unfold cGR_4_14_v12 cGR_4_14_v13; stepTac
def cGR_4_14_v14 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^7), 0, 0, ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^3), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q^3), 0, 0, ((-q^18 + 7*q^16 - 22*q^14 + 42*q^12 - 55*q^10 + 52*q^8 - 36*q^6 + 18*q^4 - 6*q^2 + 1) / q^6), ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^5)]
theorem cGR_4_14_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx4 (0, false)).mulVec (cGR_4_14_v13 q) = cGR_4_14_v14 q := by
  rw [bridge4_0]; unfold cGR_4_14_v13 cGR_4_14_v14; stepTac
theorem cGR_4_14_col (q : R) (hq : q ≠ 0) :
    (wordW q idx4 wGR).mulVec (Pi.single 14 1) = cGR_4_14_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_4_14_v0_step q hq, cGR_4_14_v1_step q hq, cGR_4_14_v2_step q hq, cGR_4_14_v3_step q hq, cGR_4_14_v4_step q hq, cGR_4_14_v5_step q hq, cGR_4_14_v6_step q hq, cGR_4_14_v7_step q hq, cGR_4_14_v8_step q hq, cGR_4_14_v9_step q hq, cGR_4_14_v10_step q hq, cGR_4_14_v11_step q hq, cGR_4_14_v12_step q hq, cGR_4_14_v13_step q hq, cGR_4_14_v14_step q hq]
theorem cGR_4_14_entry (q : R) (hq : q ≠ 0) :
    wordW q idx4 wGR 14 14 = ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^5) := by
  rw [entry_eq_mulVec_single (wordW q idx4 wGR) 14 14, cGR_4_14_col q hq]; simp [cGR_4_14_v14]

def cGR_2_9_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0, 0]
theorem cGR_2_9_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 9 1) = cGR_2_9_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_9_v0; stepTac
def cGR_2_9_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, (1), 0, 0, 0, (-q^2 + 1), 0, 0, 0, 0, 0]
theorem cGR_2_9_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_9_v0 q) = cGR_2_9_v1 q := by
  rw [bridge2_2]; unfold cGR_2_9_v0 cGR_2_9_v1; stepTac
def cGR_2_9_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((1) / q), (-q^2 + 1), 0, 0, ((q^4 - 2*q^2 + 1) / q), 0, 0, 0, 0, 0]
theorem cGR_2_9_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_9_v1 q) = cGR_2_9_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_9_v1 cGR_2_9_v2; stepTac
def cGR_2_9_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), ((1) / q), 0, 0, (q^4 - 2*q^2 + 1), 0, 0, 0, 0, 0]
theorem cGR_2_9_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_9_v2 q) = cGR_2_9_v3 q := by
  rw [bridge2_2]; unfold cGR_2_9_v2 cGR_2_9_v3; stepTac
def cGR_2_9_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^3), (q^4 - 2*q^2 + 1), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 2) / q), 0, 0, 0, 0, 0]
theorem cGR_2_9_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_9_v3 q) = cGR_2_9_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_9_v3 cGR_2_9_v4; stepTac
def cGR_2_9_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, (-q^6 + 3*q^4 - 3*q^2 + 2), 0, 0, 0, 0, 0]
theorem cGR_2_9_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_9_v4 q) = cGR_2_9_v5 q := by
  rw [bridge2_2]; unfold cGR_2_9_v4 cGR_2_9_v5; stepTac
def cGR_2_9_v6 (q : R) : Fin 15 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^4 + 2*q^2 - 1) / q^3), 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^5), ((q^6 - 3*q^4 + 3*q^2 - 1) / q^4), 0, 0, ((-q^6 + 3*q^4 - 3*q^2 + 2) / q), 0, 0, 0, 0, 0]
theorem cGR_2_9_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_9_v5 q) = cGR_2_9_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_9_v5 cGR_2_9_v6; stepTac
def cGR_2_9_v7 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 4*q^2 + 1) / q^5), 0, 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q^4), 0, 0, 0, 0, 0]
theorem cGR_2_9_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_9_v6 q) = cGR_2_9_v7 q := by
  rw [bridge2_3]; unfold cGR_2_9_v6 cGR_2_9_v7; stepTac
def cGR_2_9_v8 (q : R) : Fin 15 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 4*q^2 + 1) / q^5), 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^5), ((q^12 - 5*q^10 + 10*q^8 - 13*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), 0, 0, ((q^6 - 3*q^4 + 3*q^2 - 1) / q^5), 0, 0, 0, 0, 0]
theorem cGR_2_9_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_9_v7 q) = cGR_2_9_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_9_v7 cGR_2_9_v8; stepTac
def cGR_2_9_v9 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^5), ((-q^10 + 4*q^8 - 7*q^6 + 8*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^4), ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^7), 0, 0, ((q^12 - 5*q^10 + 10*q^8 - 13*q^6 + 11*q^4 - 5*q^2 + 1) / q^6), 0, 0, 0, 0, 0]
theorem cGR_2_9_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_9_v8 q) = cGR_2_9_v9 q := by
  rw [bridge2_3]; unfold cGR_2_9_v8 cGR_2_9_v9; stepTac
def cGR_2_9_v10 (q : R) : Fin 15 → R := ![((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^7), ((q^12 - 5*q^10 + 11*q^8 - 14*q^6 + 11*q^4 - 5*q^2 + 1) / q^4), ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^7), 0, 0, ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q^5), ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^8), 0, 0, ((q^12 - 5*q^10 + 10*q^8 - 13*q^6 + 11*q^4 - 5*q^2 + 1) / q^7), 0, 0, 0, 0, 0]
theorem cGR_2_9_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_9_v9 q) = cGR_2_9_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_9_v9 cGR_2_9_v10; stepTac
def cGR_2_9_v11 (q : R) : Fin 15 → R := ![((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^8), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^7), ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^6), 0, 0, ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q^4), ((-q^18 + 7*q^16 - 22*q^14 + 42*q^12 - 55*q^10 + 52*q^8 - 36*q^6 + 18*q^4 - 6*q^2 + 1) / q^9), 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^8), 0, 0, 0, 0, 0]
theorem cGR_2_9_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_9_v10 q) = cGR_2_9_v11 q := by
  rw [bridge2_3]; unfold cGR_2_9_v10 cGR_2_9_v11; stepTac
def cGR_2_9_v12 (q : R) : Fin 15 → R := ![((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^7), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^6), ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^5), 0, 0, ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q^3), ((-q^18 + 7*q^16 - 22*q^14 + 42*q^12 - 55*q^10 + 52*q^8 - 36*q^6 + 18*q^4 - 6*q^2 + 1) / q^8), 0, 0, ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^7), 0, 0, 0, 0, 0]
theorem cGR_2_9_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_9_v11 q) = cGR_2_9_v12 q := by
  rw [bridge2_0]; unfold cGR_2_9_v11 cGR_2_9_v12; stepTac
def cGR_2_9_v13 (q : R) : Fin 15 → R := ![((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^6), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^5), ((q^16 - 7*q^14 + 21*q^12 - 37*q^10 + 43*q^8 - 34*q^6 + 18*q^4 - 6*q^2 + 1) / q^6), ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^5), 0, ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q^2), ((-q^20 + 8*q^18 - 29*q^16 + 64*q^14 - 97*q^12 + 107*q^10 - 88*q^8 + 54*q^6 - 24*q^4 + 7*q^2 - 1) / q^9), ((-q^18 + 7*q^16 - 22*q^14 + 42*q^12 - 55*q^10 + 52*q^8 - 36*q^6 + 18*q^4 - 6*q^2 + 1) / q^8), 0, ((-q^18 + 7*q^16 - 23*q^14 + 47*q^12 - 65*q^10 + 65*q^8 - 47*q^6 + 23*q^4 - 7*q^2 + 1) / q^8), ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^7), 0, 0, 0, 0]
theorem cGR_2_9_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_9_v12 q) = cGR_2_9_v13 q := by
  rw [bridge2_1]; unfold cGR_2_9_v12 cGR_2_9_v13; stepTac
def cGR_2_9_v14 (q : R) : Fin 15 → R := ![((q^16 - 6*q^14 + 17*q^12 - 30*q^10 + 36*q^8 - 30*q^6 + 17*q^4 - 6*q^2 + 1) / q^5), ((-q^12 + 5*q^10 - 11*q^8 + 14*q^6 - 11*q^4 + 5*q^2 - 1) / q^4), ((q^16 - 7*q^14 + 21*q^12 - 37*q^10 + 43*q^8 - 34*q^6 + 18*q^4 - 6*q^2 + 1) / q^5), ((q^16 - 7*q^14 + 21*q^12 - 37*q^10 + 43*q^8 - 34*q^6 + 18*q^4 - 6*q^2 + 1) / q^6), ((q^14 - 6*q^12 + 15*q^10 - 22*q^8 + 21*q^6 - 13*q^4 + 5*q^2 - 1) / q^5), ((-q^14 + 6*q^12 - 16*q^10 + 26*q^8 - 28*q^6 + 20*q^4 - 9*q^2 + 2) / q), ((-q^20 + 8*q^18 - 29*q^16 + 64*q^14 - 97*q^12 + 107*q^10 - 88*q^8 + 54*q^6 - 24*q^4 + 7*q^2 - 1) / q^8), ((-q^20 + 8*q^18 - 29*q^16 + 64*q^14 - 97*q^12 + 107*q^10 - 88*q^8 + 54*q^6 - 24*q^4 + 7*q^2 - 1) / q^9), ((-q^18 + 7*q^16 - 22*q^14 + 42*q^12 - 55*q^10 + 52*q^8 - 36*q^6 + 18*q^4 - 6*q^2 + 1) / q^8), ((-q^18 + 7*q^16 - 23*q^14 + 47*q^12 - 65*q^10 + 65*q^8 - 47*q^6 + 23*q^4 - 7*q^2 + 1) / q^7), ((-q^18 + 7*q^16 - 23*q^14 + 47*q^12 - 65*q^10 + 65*q^8 - 47*q^6 + 23*q^4 - 7*q^2 + 1) / q^8), ((-q^16 + 6*q^14 - 17*q^12 + 30*q^10 - 35*q^8 + 30*q^6 - 17*q^4 + 6*q^2 - 1) / q^7), 0, 0, 0]
theorem cGR_2_9_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_9_v13 q) = cGR_2_9_v14 q := by
  rw [bridge2_0]; unfold cGR_2_9_v13 cGR_2_9_v14; stepTac
theorem cGR_2_9_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 9 1) = cGR_2_9_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_9_v0_step q hq, cGR_2_9_v1_step q hq, cGR_2_9_v2_step q hq, cGR_2_9_v3_step q hq, cGR_2_9_v4_step q hq, cGR_2_9_v5_step q hq, cGR_2_9_v6_step q hq, cGR_2_9_v7_step q hq, cGR_2_9_v8_step q hq, cGR_2_9_v9_step q hq, cGR_2_9_v10_step q hq, cGR_2_9_v11_step q hq, cGR_2_9_v12_step q hq, cGR_2_9_v13_step q hq, cGR_2_9_v14_step q hq]
theorem cGR_2_9_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 9 9 = ((-q^18 + 7*q^16 - 23*q^14 + 47*q^12 - 65*q^10 + 65*q^8 - 47*q^6 + 23*q^4 - 7*q^2 + 1) / q^7) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 9 9, cGR_2_9_col q hq]; simp [cGR_2_9_v14]

def cGR_2_10_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0, 0]
theorem cGR_2_10_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 10 1) = cGR_2_10_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_10_v0; stepTac
def cGR_2_10_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, (q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((-q^2 + 1) / q), 0, 0]
theorem cGR_2_10_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_10_v0 q) = cGR_2_10_v1 q := by
  rw [bridge2_2]; unfold cGR_2_10_v0 cGR_2_10_v1; stepTac
def cGR_2_10_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, ((-q^2 + 1) / q^2), 0, 0]
theorem cGR_2_10_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_10_v1 q) = cGR_2_10_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_10_v1 cGR_2_10_v2; stepTac
def cGR_2_10_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0]
theorem cGR_2_10_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_10_v2 q) = cGR_2_10_v3 q := by
  rw [bridge2_2]; unfold cGR_2_10_v2 cGR_2_10_v3; stepTac
def cGR_2_10_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0]
theorem cGR_2_10_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_10_v3 q) = cGR_2_10_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_10_v3 cGR_2_10_v4; stepTac
def cGR_2_10_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGR_2_10_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_10_v4 q) = cGR_2_10_v5 q := by
  rw [bridge2_2]; unfold cGR_2_10_v4 cGR_2_10_v5; stepTac
def cGR_2_10_v6 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^7), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0, 0]
theorem cGR_2_10_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_10_v5 q) = cGR_2_10_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_10_v5 cGR_2_10_v6; stepTac
def cGR_2_10_v7 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, 0, 0, ((-q^14 + 4*q^12 - 7*q^10 + 7*q^8 - 2*q^6 - 2*q^4 + 3*q^2 - 1) / q^7), 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGR_2_10_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_10_v6 q) = cGR_2_10_v7 q := by
  rw [bridge2_3]; unfold cGR_2_10_v6 cGR_2_10_v7; stepTac
def cGR_2_10_v8 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^14 + 4*q^12 - 7*q^10 + 7*q^8 - 2*q^6 - 2*q^4 + 3*q^2 - 1) / q^7), 0, 0, 0, ((q^16 - 4*q^14 + 8*q^12 - 10*q^10 + 6*q^8 + q^6 - 5*q^4 + 4*q^2 - 1) / q^8), 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^5), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0, 0]
theorem cGR_2_10_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_10_v7 q) = cGR_2_10_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_10_v7 cGR_2_10_v8; stepTac
def cGR_2_10_v9 (q : R) : Fin 15 → R := ![0, 0, 0, ((-q^14 + 4*q^12 - 7*q^10 + 7*q^8 - 2*q^6 - 2*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((q^16 - 4*q^14 + 8*q^12 - 10*q^10 + 6*q^8 + q^6 - 5*q^4 + 4*q^2 - 1) / q^8), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGR_2_10_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_10_v8 q) = cGR_2_10_v9 q := by
  rw [bridge2_3]; unfold cGR_2_10_v8 cGR_2_10_v9; stepTac
def cGR_2_10_v10 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, 0, 0, ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^10), 0, 0, ((q^16 - 4*q^14 + 8*q^12 - 10*q^10 + 6*q^8 + q^6 - 5*q^4 + 4*q^2 - 1) / q^9), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0, 0]
theorem cGR_2_10_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_10_v9 q) = cGR_2_10_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_10_v9 cGR_2_10_v10; stepTac
def cGR_2_10_v11 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, 0, 0, ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^11), 0, 0, ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^10), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGR_2_10_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_10_v10 q) = cGR_2_10_v11 q := by
  rw [bridge2_3]; unfold cGR_2_10_v10 cGR_2_10_v11; stepTac
def cGR_2_10_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^20 - 6*q^18 + 16*q^16 - 25*q^14 + 23*q^12 - 7*q^10 - 12*q^8 + 20*q^6 - 15*q^4 + 6*q^2 - 1) / q^9), ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, 0, ((-q^24 + 7*q^22 - 22*q^20 + 42*q^18 - 52*q^16 + 37*q^14 - 37*q^10 + 52*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^12), ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^11), 0, ((-q^22 + 6*q^20 - 17*q^18 + 30*q^16 - 34*q^14 + 21*q^12 + 5*q^10 - 27*q^8 + 31*q^6 - 20*q^4 + 7*q^2 - 1) / q^11), ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^10), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0]
theorem cGR_2_10_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_10_v11 q) = cGR_2_10_v12 q := by
  rw [bridge2_0]; unfold cGR_2_10_v11 cGR_2_10_v12; stepTac
def cGR_2_10_v13 (q : R) : Fin 15 → R := ![0, 0, ((q^20 - 6*q^18 + 16*q^16 - 25*q^14 + 23*q^12 - 7*q^10 - 12*q^8 + 20*q^6 - 15*q^4 + 6*q^2 - 1) / q^9), 0, ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), 0, ((-q^24 + 7*q^22 - 22*q^20 + 42*q^18 - 52*q^16 + 37*q^14 - 37*q^10 + 52*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^12), 0, ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^10), ((-q^22 + 6*q^20 - 17*q^18 + 30*q^16 - 34*q^14 + 21*q^12 + 5*q^10 - 27*q^8 + 31*q^6 - 20*q^4 + 7*q^2 - 1) / q^11), 0, ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^9), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5)]
theorem cGR_2_10_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_10_v12 q) = cGR_2_10_v13 q := by
  rw [bridge2_1]; unfold cGR_2_10_v12 cGR_2_10_v13; stepTac
def cGR_2_10_v14 (q : R) : Fin 15 → R := ![0, 0, ((q^20 - 6*q^18 + 16*q^16 - 25*q^14 + 23*q^12 - 7*q^10 - 12*q^8 + 20*q^6 - 15*q^4 + 6*q^2 - 1) / q^8), ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), 0, 0, ((-q^24 + 7*q^22 - 22*q^20 + 42*q^18 - 52*q^16 + 37*q^14 - 37*q^10 + 52*q^8 - 42*q^6 + 22*q^4 - 7*q^2 + 1) / q^11), ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^10), 0, ((-q^22 + 6*q^20 - 17*q^18 + 30*q^16 - 34*q^14 + 21*q^12 + 5*q^10 - 27*q^8 + 31*q^6 - 20*q^4 + 7*q^2 - 1) / q^10), ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^9), 0, ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4)]
theorem cGR_2_10_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_10_v13 q) = cGR_2_10_v14 q := by
  rw [bridge2_0]; unfold cGR_2_10_v13 cGR_2_10_v14; stepTac
theorem cGR_2_10_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 10 1) = cGR_2_10_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_10_v0_step q hq, cGR_2_10_v1_step q hq, cGR_2_10_v2_step q hq, cGR_2_10_v3_step q hq, cGR_2_10_v4_step q hq, cGR_2_10_v5_step q hq, cGR_2_10_v6_step q hq, cGR_2_10_v7_step q hq, cGR_2_10_v8_step q hq, cGR_2_10_v9_step q hq, cGR_2_10_v10_step q hq, cGR_2_10_v11_step q hq, cGR_2_10_v12_step q hq, cGR_2_10_v13_step q hq, cGR_2_10_v14_step q hq]
theorem cGR_2_10_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 10 10 = ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^9) := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 10 10, cGR_2_10_col q hq]; simp [cGR_2_10_v14]

def cGR_2_11_v0 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, (1), 0, 0, ((-q^2 + 1) / q), 0, 0, 0]
theorem cGR_2_11_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (Pi.single 11 1) = cGR_2_11_v0 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_11_v0; stepTac
def cGR_2_11_v1 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, (q), 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, ((-q^2 + 1) / q), 0]
theorem cGR_2_11_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_11_v0 q) = cGR_2_11_v1 q := by
  rw [bridge2_2]; unfold cGR_2_11_v0 cGR_2_11_v1; stepTac
def cGR_2_11_v2 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q^2), 0, 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, ((-q^2 + 1) / q^2), 0]
theorem cGR_2_11_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_11_v1 q) = cGR_2_11_v2 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_11_v1 cGR_2_11_v2; stepTac
def cGR_2_11_v3 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((-q^4 + 2*q^2 - 1) / q), 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0]
theorem cGR_2_11_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_11_v2 q) = cGR_2_11_v3 q := by
  rw [bridge2_2]; unfold cGR_2_11_v2 cGR_2_11_v3; stepTac
def cGR_2_11_v4 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0]
theorem cGR_2_11_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, true)).mulVec (cGR_2_11_v3 q) = cGR_2_11_v4 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_3]; unfold cGR_2_11_v3 cGR_2_11_v4; stepTac
def cGR_2_11_v5 (q : R) : Fin 15 → R := ![0, 0, 0, 0, 0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0]
theorem cGR_2_11_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (2, false)).mulVec (cGR_2_11_v4 q) = cGR_2_11_v5 q := by
  rw [bridge2_2]; unfold cGR_2_11_v4 cGR_2_11_v5; stepTac
def cGR_2_11_v6 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), 0, 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), 0, 0, ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^7), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0]
theorem cGR_2_11_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_11_v5 q) = cGR_2_11_v6 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_11_v5 cGR_2_11_v6; stepTac
def cGR_2_11_v7 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), 0, 0, 0, ((-q^14 + 4*q^12 - 7*q^10 + 7*q^8 - 2*q^6 - 2*q^4 + 3*q^2 - 1) / q^7), 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0]
theorem cGR_2_11_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_11_v6 q) = cGR_2_11_v7 q := by
  rw [bridge2_3]; unfold cGR_2_11_v6 cGR_2_11_v7; stepTac
def cGR_2_11_v8 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^14 + 4*q^12 - 7*q^10 + 7*q^8 - 2*q^6 - 2*q^4 + 3*q^2 - 1) / q^7), 0, 0, 0, ((q^16 - 4*q^14 + 8*q^12 - 10*q^10 + 6*q^8 + q^6 - 5*q^4 + 4*q^2 - 1) / q^8), 0, 0, ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^5), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0]
theorem cGR_2_11_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_11_v7 q) = cGR_2_11_v8 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_11_v7 cGR_2_11_v8; stepTac
def cGR_2_11_v9 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((-q^14 + 4*q^12 - 7*q^10 + 7*q^8 - 2*q^6 - 2*q^4 + 3*q^2 - 1) / q^6), 0, 0, 0, ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, 0, ((q^16 - 4*q^14 + 8*q^12 - 10*q^10 + 6*q^8 + q^6 - 5*q^4 + 4*q^2 - 1) / q^8), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0]
theorem cGR_2_11_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_11_v8 q) = cGR_2_11_v9 q := by
  rw [bridge2_3]; unfold cGR_2_11_v8 cGR_2_11_v9; stepTac
def cGR_2_11_v10 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), 0, 0, 0, ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^10), 0, 0, ((q^16 - 4*q^14 + 8*q^12 - 10*q^10 + 6*q^8 + q^6 - 5*q^4 + 4*q^2 - 1) / q^9), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0]
theorem cGR_2_11_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (4, true)).mulVec (cGR_2_11_v9 q) = cGR_2_11_v10 q := by
  rw [gW_inv_mulVec q idx2 idx2_inj, bridge2_4]; unfold cGR_2_11_v9 cGR_2_11_v10; stepTac
def cGR_2_11_v11 (q : R) : Fin 15 → R := ![0, 0, 0, 0, ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, 0, 0, ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^11), 0, 0, ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^10), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0]
theorem cGR_2_11_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (3, false)).mulVec (cGR_2_11_v10 q) = cGR_2_11_v11 q := by
  rw [bridge2_3]; unfold cGR_2_11_v10 cGR_2_11_v11; stepTac
def cGR_2_11_v12 (q : R) : Fin 15 → R := ![0, 0, 0, ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, 0, 0, ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^11), 0, 0, ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^10), 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGR_2_11_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_11_v11 q) = cGR_2_11_v12 q := by
  rw [bridge2_0]; unfold cGR_2_11_v11 cGR_2_11_v12; stepTac
def cGR_2_11_v13 (q : R) : Fin 15 → R := ![0, 0, ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), 0, 0, 0, ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^11), 0, 0, ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^10), 0, 0, ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0]
theorem cGR_2_11_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (1, false)).mulVec (cGR_2_11_v12 q) = cGR_2_11_v13 q := by
  rw [bridge2_1]; unfold cGR_2_11_v12 cGR_2_11_v13; stepTac
def cGR_2_11_v14 (q : R) : Fin 15 → R := ![0, 0, ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), 0, 0, 0, ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^10), 0, 0, ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^9), 0, 0, ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0]
theorem cGR_2_11_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx2 (0, false)).mulVec (cGR_2_11_v13 q) = cGR_2_11_v14 q := by
  rw [bridge2_0]; unfold cGR_2_11_v13 cGR_2_11_v14; stepTac
theorem cGR_2_11_col (q : R) (hq : q ≠ 0) :
    (wordW q idx2 wGR).mulVec (Pi.single 11 1) = cGR_2_11_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_2_11_v0_step q hq, cGR_2_11_v1_step q hq, cGR_2_11_v2_step q hq, cGR_2_11_v3_step q hq, cGR_2_11_v4_step q hq, cGR_2_11_v5_step q hq, cGR_2_11_v6_step q hq, cGR_2_11_v7_step q hq, cGR_2_11_v8_step q hq, cGR_2_11_v9_step q hq, cGR_2_11_v10_step q hq, cGR_2_11_v11_step q hq, cGR_2_11_v12_step q hq, cGR_2_11_v13_step q hq, cGR_2_11_v14_step q hq]
theorem cGR_2_11_entry (q : R) (hq : q ≠ 0) :
    wordW q idx2 wGR 11 11 = 0 := by
  rw [entry_eq_mulVec_single (wordW q idx2 wGR) 11 11, cGR_2_11_col q hq]; simp [cGR_2_11_v14]

def cGR_1_2_v0 (q : R) : Fin 6 → R := ![0, (1), ((-q^2 + 1) / q), 0, 0, 0]
theorem cGR_1_2_v0_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (Pi.single 2 1) = cGR_1_2_v0 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGR_1_2_v0; stepTac
def cGR_1_2_v1 (q : R) : Fin 6 → R := ![0, (q), ((-q^4 + 2*q^2 - 1) / q^2), ((-q^2 + 1) / q), 0, 0]
theorem cGR_1_2_v1_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGR_1_2_v0 q) = cGR_1_2_v1 q := by
  rw [bridge1_2]; unfold cGR_1_2_v0 cGR_1_2_v1; stepTac
def cGR_1_2_v2 (q : R) : Fin 6 → R := ![0, ((-q^4 + 2*q^2 - 1) / q^2), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), ((-q^2 + 1) / q^2), 0, 0]
theorem cGR_1_2_v2_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGR_1_2_v1 q) = cGR_1_2_v2 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGR_1_2_v1 cGR_1_2_v2; stepTac
def cGR_1_2_v3 (q : R) : Fin 6 → R := ![0, ((-q^4 + 2*q^2 - 1) / q), ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^3), 0, 0]
theorem cGR_1_2_v3_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGR_1_2_v2 q) = cGR_1_2_v3 q := by
  rw [bridge1_2]; unfold cGR_1_2_v2 cGR_1_2_v3; stepTac
def cGR_1_2_v4 (q : R) : Fin 6 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^4), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), ((q^6 - 2*q^4 + 3*q^2 - 1) / q^4), 0, 0]
theorem cGR_1_2_v4_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, true)).mulVec (cGR_1_2_v3 q) = cGR_1_2_v4 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_3]; unfold cGR_1_2_v3 cGR_1_2_v4; stepTac
def cGR_1_2_v5 (q : R) : Fin 6 → R := ![0, ((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^6), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGR_1_2_v5_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (2, false)).mulVec (cGR_1_2_v4 q) = cGR_1_2_v5 q := by
  rw [bridge1_2]; unfold cGR_1_2_v4 cGR_1_2_v5; stepTac
def cGR_1_2_v6 (q : R) : Fin 6 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^3), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), ((-q^12 + 4*q^10 - 7*q^8 + 9*q^6 - 7*q^4 + 4*q^2 - 1) / q^7), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0, 0]
theorem cGR_1_2_v6_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, true)).mulVec (cGR_1_2_v5 q) = cGR_1_2_v6 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_4]; unfold cGR_1_2_v5 cGR_1_2_v6; stepTac
def cGR_1_2_v7 (q : R) : Fin 6 → R := ![((q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / q^2), ((-q^14 + 4*q^12 - 7*q^10 + 7*q^8 - 2*q^6 - 2*q^4 + 3*q^2 - 1) / q^7), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^4), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGR_1_2_v7_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGR_1_2_v6 q) = cGR_1_2_v7 q := by
  rw [bridge1_3]; unfold cGR_1_2_v6 cGR_1_2_v7; stepTac
def cGR_1_2_v8 (q : R) : Fin 6 → R := ![((-q^14 + 4*q^12 - 7*q^10 + 7*q^8 - 2*q^6 - 2*q^4 + 3*q^2 - 1) / q^7), ((q^16 - 4*q^14 + 8*q^12 - 10*q^10 + 6*q^8 + q^6 - 5*q^4 + 4*q^2 - 1) / q^8), ((-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / q^5), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0, 0]
theorem cGR_1_2_v8_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, true)).mulVec (cGR_1_2_v7 q) = cGR_1_2_v8 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_4]; unfold cGR_1_2_v7 cGR_1_2_v8; stepTac
def cGR_1_2_v9 (q : R) : Fin 6 → R := ![((-q^14 + 4*q^12 - 7*q^10 + 7*q^8 - 2*q^6 - 2*q^4 + 3*q^2 - 1) / q^6), ((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((q^16 - 4*q^14 + 8*q^12 - 10*q^10 + 6*q^8 + q^6 - 5*q^4 + 4*q^2 - 1) / q^8), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGR_1_2_v9_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGR_1_2_v8 q) = cGR_1_2_v9 q := by
  rw [bridge1_3]; unfold cGR_1_2_v8 cGR_1_2_v9; stepTac
def cGR_1_2_v10 (q : R) : Fin 6 → R := ![((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^9), ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^10), ((q^16 - 4*q^14 + 8*q^12 - 10*q^10 + 6*q^8 + q^6 - 5*q^4 + 4*q^2 - 1) / q^9), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^6), 0, 0]
theorem cGR_1_2_v10_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (4, true)).mulVec (cGR_1_2_v9 q) = cGR_1_2_v10 q := by
  rw [gW_inv_mulVec q idx1 idx1_inj, bridge1_4]; unfold cGR_1_2_v9 cGR_1_2_v10; stepTac
def cGR_1_2_v11 (q : R) : Fin 6 → R := ![((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^8), ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^11), ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^10), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^5), 0, 0]
theorem cGR_1_2_v11_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (3, false)).mulVec (cGR_1_2_v10 q) = cGR_1_2_v11 q := by
  rw [bridge1_3]; unfold cGR_1_2_v10 cGR_1_2_v11; stepTac
def cGR_1_2_v12 (q : R) : Fin 6 → R := ![((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^7), ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^10), ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^9), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0, 0]
theorem cGR_1_2_v12_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGR_1_2_v11 q) = cGR_1_2_v12 q := by
  rw [bridge1_0]; unfold cGR_1_2_v11 cGR_1_2_v12; stepTac
def cGR_1_2_v13 (q : R) : Fin 6 → R := ![((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^6), ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^9), ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^8), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4), 0]
theorem cGR_1_2_v13_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (1, false)).mulVec (cGR_1_2_v12 q) = cGR_1_2_v13 q := by
  rw [bridge1_1]; unfold cGR_1_2_v12 cGR_1_2_v13; stepTac
def cGR_1_2_v14 (q : R) : Fin 6 → R := ![((q^18 - 5*q^16 + 11*q^14 - 14*q^12 + 9*q^10 + 2*q^8 - 10*q^6 + 10*q^4 - 5*q^2 + 1) / q^5), ((-q^22 + 6*q^20 - 16*q^18 + 26*q^16 - 26*q^14 + 11*q^12 + 11*q^10 - 26*q^8 + 26*q^6 - 16*q^4 + 6*q^2 - 1) / q^8), ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^7), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^4), ((-q^12 + 4*q^10 - 8*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / q^5), ((-q^10 + 3*q^8 - 5*q^6 + 6*q^4 - 4*q^2 + 1) / q^4)]
theorem cGR_1_2_v14_step (q : R) (hq : q ≠ 0) :
    (gW q idx1 (0, false)).mulVec (cGR_1_2_v13 q) = cGR_1_2_v14 q := by
  rw [bridge1_0]; unfold cGR_1_2_v13 cGR_1_2_v14; stepTac
theorem cGR_1_2_col (q : R) (hq : q ≠ 0) :
    (wordW q idx1 wGR).mulVec (Pi.single 2 1) = cGR_1_2_v14 q := by
  simp only [wGR, wordW_mulVec_cons, wordW_nil, Matrix.one_mulVec]
  rw [cGR_1_2_v0_step q hq, cGR_1_2_v1_step q hq, cGR_1_2_v2_step q hq, cGR_1_2_v3_step q hq, cGR_1_2_v4_step q hq, cGR_1_2_v5_step q hq, cGR_1_2_v6_step q hq, cGR_1_2_v7_step q hq, cGR_1_2_v8_step q hq, cGR_1_2_v9_step q hq, cGR_1_2_v10_step q hq, cGR_1_2_v11_step q hq, cGR_1_2_v12_step q hq, cGR_1_2_v13_step q hq, cGR_1_2_v14_step q hq]
theorem cGR_1_2_entry (q : R) (hq : q ≠ 0) :
    wordW q idx1 wGR 2 2 = ((-q^20 + 5*q^18 - 12*q^16 + 18*q^14 - 16*q^12 + 5*q^10 + 10*q^8 - 17*q^6 + 14*q^4 - 6*q^2 + 1) / q^7) := by
  rw [entry_eq_mulVec_single (wordW q idx1 wGR) 2 2, cGR_1_2_col q hq]; simp [cGR_1_2_v14]

/-- **`S` for `σ₀σ₁σ₀ · (σ₃σ₄⁻¹)³ · (σ₂σ₃⁻¹)³`, proton on strands `3–5` (bond `G`, ruled form).** -/
theorem S_GR (q : R) (hq : q ≠ 0) :
    Fp64 [3, 4, 5] (word64 q wGR) + Fm64 [3, 4, 5] (word64 q wGR) = (3 * q ^ 2 + 1) * (q - q⁻¹) ^ 4 / q := by
  rw [Fp_R_reduction, Fm_R_reduction, cGR_5_3_entry q hq, cGR_4_3_entry q hq, cGR_4_4_entry q hq, cGR_4_5_entry q hq, cGR_2_0_entry q hq, cGR_5_4_entry q hq, cGR_4_6_entry q hq, cGR_4_7_entry q hq, cGR_4_8_entry q hq, cGR_2_1_entry q hq, cGR_5_5_entry q hq, cGR_4_10_entry q hq, cGR_4_11_entry q hq, cGR_4_12_entry q hq, cGR_2_5_entry q hq, cGR_4_9_entry q hq, cGR_2_2_entry q hq, cGR_2_3_entry q hq, cGR_2_4_entry q hq, cGR_1_0_entry q hq, cGR_4_13_entry q hq, cGR_2_6_entry q hq, cGR_2_7_entry q hq, cGR_2_8_entry q hq, cGR_1_1_entry q hq, cGR_4_14_entry q hq, cGR_2_9_entry q hq, cGR_2_10_entry q hq, cGR_2_11_entry q hq, cGR_1_2_entry q hq]
  field_simp; ring

theorem Fp_GR_at_one : Fp64 [3, 4, 5] (word64 (1 : R) wGR) = 6 := by
  rw [Fp_R_reduction, cGR_5_3_entry 1 one_ne_zero, cGR_4_3_entry 1 one_ne_zero, cGR_4_4_entry 1 one_ne_zero, cGR_4_5_entry 1 one_ne_zero, cGR_2_0_entry 1 one_ne_zero, cGR_5_4_entry 1 one_ne_zero, cGR_4_6_entry 1 one_ne_zero, cGR_4_7_entry 1 one_ne_zero, cGR_4_8_entry 1 one_ne_zero, cGR_2_1_entry 1 one_ne_zero, cGR_5_5_entry 1 one_ne_zero, cGR_4_10_entry 1 one_ne_zero, cGR_4_11_entry 1 one_ne_zero, cGR_4_12_entry 1 one_ne_zero, cGR_2_5_entry 1 one_ne_zero]; norm_num

theorem Fm_GR_at_one : Fm64 [3, 4, 5] (word64 (1 : R) wGR) = -6 := by
  rw [Fm_R_reduction, cGR_4_9_entry 1 one_ne_zero, cGR_2_2_entry 1 one_ne_zero, cGR_2_3_entry 1 one_ne_zero, cGR_2_4_entry 1 one_ne_zero, cGR_1_0_entry 1 one_ne_zero, cGR_4_13_entry 1 one_ne_zero, cGR_2_6_entry 1 one_ne_zero, cGR_2_7_entry 1 one_ne_zero, cGR_2_8_entry 1 one_ne_zero, cGR_1_1_entry 1 one_ne_zero, cGR_4_14_entry 1 one_ne_zero, cGR_2_9_entry 1 one_ne_zero, cGR_2_10_entry 1 one_ne_zero, cGR_2_11_entry 1 one_ne_zero, cGR_1_2_entry 1 one_ne_zero]; norm_num

end QOU.BraidsAndKnots.BondChiralitySixStrand
