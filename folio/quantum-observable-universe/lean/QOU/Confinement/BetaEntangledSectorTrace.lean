/-
# The two-strand kernel of the entangled β-decay sector trace

Bean `qou-99qc` (P4 of the 2026-11-20 β-decay programme). Owner (Carl), 2026-11-20: *"A beta decay
is not standalone. It is a particle interaction … it is a Gröbner basis calculation at the end of the
day."* Pre-registered in
`computations/probes/beta_gs_reduction_n_gammagamma/PREREGISTRATION.md`.

The probe `beta_gs_reduction_probe.py` reads an entangled six-strand word (nucleon `β_Bor` on strands
0–2, photon pair on 3–5, bridge letters between them) in the Jimbo representation and compares the
`K`-weighted trace over the sector `n ⊗ ν` (nucleon `T³ = −½`, lepton `= u`) with the sector
`p ⊗ e⁻` (nucleon `T³ = +½`, lepton `= d`). For the split word the two agree; one bridge crossing
separates them. This file proves the mechanism on the smallest space where it lives: one quark
strand and one lepton strand, `V ⊗ V`, basis `uu, ud, du, dd` (indices `0, 1, 2, 3`).

* `Rc` is the Jimbo crossing of `ChargedCurrentW.Rc` (columns are images): `uu ↦ q uu`,
  `ud ↦ du`, `du ↦ ud + h du`, `dd ↦ q dd`, with `h = q − q⁻¹`. Restated so this file depends on
  Mathlib only.
* `qtr X = Σᵢ wᵢ Xᵢᵢ`, `w = (q², 1, 1, q⁻²)` (the weight `q^{2T³}`).
* `qtr_markov` : for every element `a + b·Rc` of `H₂`, `qtr / [2]² = a + b·z_D`, `z_D = q³/(q²+1)`
  — the `K`-weighted trace IS the convention-D Ocneanu trace (the calibration the probe checks on
  `H₃` words).
* `secDiff X = X_{du,du} − X_{ud,ud}` : the `n⊗ν` sector (quark `d`, lepton `ν = u`) minus the
  `p⊗e⁻` sector (quark `u`, lepton `e⁻ = d`); both have `K`-weight 1.
* `secDiff_one` : the uncrossed (factorised) pair gives `0`.
* `secDiff_Rc`, `secDiff_Rcinv` : one crossing of either sign gives `h`.
* `secDiff_H2` : on all of `H₂`, `secDiff (a + b·Rc) = b·h` — the sector separation is carried
  entirely by the `h` term of the crossing, which `ChargedCurrentW.Rc_strand` identifies as the
  strand-tracked `W` exchange `h·E⊗F`.

What this does NOT establish: that the lepton strand is a second copy of `V` (assumption carried
from #8638); any energy scale (the probe's `S_N = m_μ[N]!/q^N` gives GeV-sized `Q₄`, far from
`Q_β`); anything about `n` versus `p` as Hecke ELEMENTS (they are one element, #8636 — the
separation here is a sector/state statement).

Base ring (§7c): generic `[Field K]`, hypotheses `q ≠ 0` and `q² + 1 ≠ 0` only where dividing.

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §VIII
-/
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

namespace QOU.QuarkState.BetaEntangledSectorTrace

open Matrix

variable {K : Type*} [Field K]

/-- `h = q − q⁻¹`. -/
def hh (q : K) : K := q - q⁻¹

/-- The Jimbo crossing on `V ⊗ V`, basis `uu, ud, du, dd`; column `j` is the image of basis `j`. -/
def Rc (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0;
     0, 0, 1, 0;
     0, 1, hh q, 0;
     0, 0, 0, q]

/-- `Rc⁻¹ = Rc − h`. -/
def Rcinv (q : K) : Matrix (Fin 4) (Fin 4) K := Rc q - hh q • (1 : Matrix (Fin 4) (Fin 4) K)

/-- The Hecke relation `Rc² = h·Rc + 1` (so `Rc · Rcinv = 1`), for `q ≠ 0`. -/
theorem Rc_sq (q : K) (hq : q ≠ 0) : Rc q * Rc q = hh q • Rc q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Rc, hh, Matrix.mul_apply, Fin.sum_univ_four] <;> field_simp <;> ring

theorem Rc_mul_Rcinv (q : K) (hq : q ≠ 0) : Rc q * Rcinv q = 1 := by
  rw [Rcinv, Matrix.mul_sub, Rc_sq q hq, Matrix.mul_smul, Matrix.mul_one, add_sub_cancel_left]

/-- The weight `q^{2T³}` on `uu, ud, du, dd`. -/
def wt (q : K) : Fin 4 → K := ![q ^ 2, 1, 1, q⁻¹ ^ 2]

/-- `K`-weighted trace. -/
def qtr (q : K) (X : Matrix (Fin 4) (Fin 4) K) : K := ∑ i, wt q i * X i i

theorem qtr_one (q : K) (hq : q ≠ 0) : qtr q 1 = (q + q⁻¹) ^ 2 := by
  simp [qtr, wt, Fin.sum_univ_four]; field_simp; ring

theorem qtr_Rc (q : K) (hq : q ≠ 0) : qtr q (Rc q) = q ^ 3 + q := by
  simp [qtr, wt, Rc, hh, Fin.sum_univ_four]; field_simp; ring

/-- **The `K`-weighted trace is the convention-D Markov trace on all of `H₂`.** -/
theorem qtr_markov (q a b : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    qtr q (a • (1 : Matrix (Fin 4) (Fin 4) K) + b • Rc q) / (q + q⁻¹) ^ 2
      = a + b * (q ^ 3 / (q ^ 2 + 1)) := by
  have hsum : q + q⁻¹ ≠ 0 := by
    intro h0
    apply h2
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h0, mul_zero]
  have hlin : qtr q (a • (1 : Matrix (Fin 4) (Fin 4) K) + b • Rc q)
      = a * qtr q 1 + b * qtr q (Rc q) := by
    simp only [qtr, Matrix.add_apply, Matrix.smul_apply, smul_eq_mul, Finset.mul_sum]
    rw [← Finset.sum_add_distrib]; congr 1; funext i; ring
  rw [hlin, qtr_one q hq, qtr_Rc q hq]
  field_simp

/-- `n⊗ν` sector (`du`) minus `p⊗e⁻` sector (`ud`); both carry `K`-weight 1. -/
def secDiff (X : Matrix (Fin 4) (Fin 4) K) : K := X 2 2 - X 1 1

theorem wt_sectors_equal (q : K) : wt q 2 = wt q 1 := rfl

/-- **Factorised (uncrossed) pair: no sector separation.** -/
theorem secDiff_one : secDiff (1 : Matrix (Fin 4) (Fin 4) K) = 0 := by
  simp [secDiff]

/-- **One positive crossing separates the sectors by exactly `h`.** -/
theorem secDiff_Rc (q : K) : secDiff (Rc q) = hh q := by
  simp [secDiff, Rc]

/-- **One negative crossing separates them by the same `h`.** -/
theorem secDiff_Rcinv (q : K) : secDiff (Rcinv q) = hh q := by
  simp [secDiff, Rcinv, Rc, Matrix.sub_apply]

/-- **On all of `H₂` the separation is the `σ`-coefficient times `h`.** -/
theorem secDiff_H2 (q a b : K) :
    secDiff (a • (1 : Matrix (Fin 4) (Fin 4) K) + b • Rc q) = b * hh q := by
  simp [secDiff, Rc]

/-- At `q = 1` (`h = 0`) the separation vanishes: it is a first-order effect in `h`. -/
theorem secDiff_Rc_at_one : secDiff (Rc (1 : K)) = 0 := by
  simp [secDiff_Rc, hh]

end QOU.QuarkState.BetaEntangledSectorTrace
