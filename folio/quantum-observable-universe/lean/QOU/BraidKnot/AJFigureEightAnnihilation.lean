import QOU.BraidKnot.AJFigureEight
import QOU.BraidKnot.AJFigureEightTelescope

/-!
# QOU.BraidKnot.AJFigureEightAnnihilation

**The general-`N` annihilation, proved — `StrongAJFigureEight` is now
sorry-free** (bean `udmw`, assembly tranche).

This file discharges the one remaining `sorry` of the AJ-in-QOU tranche:
the explicit order-2 operator (`figureEightOperator`) annihilates the
colored Jones tower of `4₁` at **every** `q ≠ 0` — including roots of
unity.  The proof is the qZeilberger certificate telescope
(`computations/aj_figure_eight_certificate.py`), reassembled
**division-free**: the rational certificate's `(q^k − q^N)(q^k − q^{N+1})`
denominators vanish at the tower boundary and at roots of unity, so the
telescoping sequence `certW` is defined through the split products of
`AJFigureEightTelescope` with divisions only by powers of `q`, `x = q^N`
and the nonvanishing clearing product `clearD`.  The B-side shift
denominators are consumed exactly by factors the operator itself supplies
(`a₂ ∋ (xq²−1)`, `a₁ ∋ (xq−1)²`, the A-shift `∋ (qx−1)`) — the structural
reason the telescope closes without genericity hypotheses.

Every identity transcribed here is pre-verified exactly in
`computations/aj_figure_eight_telescope_assembly_check.py`
(master local identity [K3], boundary `W(0) = −rhs` [W0], the `N = 0`
instance [N0], and a full simulation of this file's `certW` telescope for
`N = 1..6` [SIM]).

## Structure

* `clearD` — the clearing product `∏_{j<k} x·q^{j+1}` (nonzero for `q ≠ 0`).
* `certW` — the division-free telescoping sequence (`k = 0, 1` boundary
  values; `k ≥ 2` the pole-cleared certificate form).
* `certW_local_step_zero/_one/certW_local_step` — the local identity
  `a₂F(N+2,k) + a₁F(N+1,k) + a₀F(N,k) = certW(k+1) − certW(k)` at
  `k = 0`, `k = 1`, `k ≥ 2`.
* `certW_top_eq_zero` — `certW(N+2) = 0` (the `risingA` termination zero).
* `figureEightOperator_annihilates` — the summed telescope, all `N`, all
  `q ≠ 0`.
* The **sorry-free instance** `StrongAJFigureEight K` (superseding the
  cited-sorry instance formerly in `AJFigureEight.lean`).

## Base ring (§7c)

`{K : Type*} [Field K]` (the tower needs `q⁻¹`); `[CharZero K]` only on
the instance, inherited from its nontriviality witness.  No `ℝ`, no
ordering, no archimedean constructs.
-/

namespace QOU.BraidKnot.AJFigureEight

open Finset
open QOU.BraidKnot.HabiroNewtonLadder

variable {K : Type*} [Field K]

/-! ## The clearing product -/

/-- `clearD q x k = ∏_{j<k} x·q^{j+1}` — the per-factor denominators of the
    Newton ladder at `x + x⁻¹`, as one product (nonzero for `q, x ≠ 0`). -/
def clearD (q x : K) (k : ℕ) : K :=
  ∏ j ∈ Finset.range k, (x * q ^ (j + 1))

theorem clearD_succ (q x : K) (k : ℕ) :
    clearD q x (k + 1) = clearD q x k * (x * q ^ (k + 1)) := by
  unfold clearD; rw [Finset.prod_range_succ]

theorem clearD_ne_zero {q x : K} (hq : q ≠ 0) (hx : x ≠ 0) (k : ℕ) :
    clearD q x k ≠ 0 :=
  Finset.prod_ne_zero_iff.mpr fun _ _ => mul_ne_zero hx (pow_ne_zero _ hq)

/-- Color shift of the clearing product: `clearD_{qx}(k) = q^k · clearD_x(k)`. -/
theorem clearD_shift (q x : K) (k : ℕ) :
    clearD q (q * x) k = q ^ k * clearD q x k := by
  unfold clearD
  have h : ∀ j ∈ Finset.range k,
      q * x * q ^ (j + 1) = q * (x * q ^ (j + 1)) := by
    intro j _; ring
  rw [Finset.prod_congr rfl h, Finset.prod_mul_distrib, Finset.prod_const,
    Finset.card_range]

/-! ## The division-free telescoping sequence -/

/-- The certificate telescoping sequence, division-free.  `certW q x k` is
    the pole-cleared value of `Cert(q, x, q^k) · F(N, k)`:

    * `k = 0`: `−rhs(q,x)` (the boundary value `−Cert(x,1)` — the content
      of `feCert_boundary`);
    * `k = 1`: the explicit cleared value;
    * `k ≥ 2`: `−C·(1−x)(1−qx)·q^k·A(k−2)·B(k) / (q²x⁷·clearD(k))` with
      `C = (qx+1)(qx²−1)(q³x²−1)` — divisions only by powers and `clearD`,
      all nonzero for `q, x ≠ 0`. -/
def certW (q x : K) : ℕ → K
  | 0 => -feRhs q x
  | 1 => -((q * x - 1) ^ 2 * (q * x + 1) * (q * x ^ 2 - 1)
      * (q ^ 3 * x ^ 2 - 1)) / (q ^ 2 * x ^ 8)
  | (m + 2) =>
      -((q * x + 1) * (q * x ^ 2 - 1) * (q ^ 3 * x ^ 2 - 1)
          * (1 - x) * (1 - q * x) * q ^ (m + 2)
          * risingA q x m * risingB q x (m + 2))
        / (q ^ 2 * x ^ 7 * clearD q x (m + 2))

/-- **Top of the tower**: at `x = q^N` with `N ≥ 1` the telescoping
    sequence vanishes at `k = N + 2` — the `j = N − 1` factor of
    `risingA q (q^N) N` is `q^N − q^N = 0`.  Division-free, so no
    genericity hypothesis is needed. -/
theorem certW_top_eq_zero (q : K) {N : ℕ} (hN : 1 ≤ N) :
    certW q (q ^ N) (N + 2) = 0 := by
  have hA : risingA q (q ^ N) N = 0 := by
    refine Finset.prod_eq_zero (i := N - 1)
      (Finset.mem_range.mpr (by omega)) ?_
    have h1 : N - 1 + 1 = N := by omega
    rw [h1, sub_self]
  show -((q * q ^ N + 1) * (q * (q ^ N) ^ 2 - 1) * (q ^ 3 * (q ^ N) ^ 2 - 1)
      * (1 - q ^ N) * (1 - q * q ^ N) * q ^ (N + 2)
      * risingA q (q ^ N) N * risingB q (q ^ N) (N + 2))
    / (q ^ 2 * (q ^ N) ^ 7 * clearD q (q ^ N) (N + 2)) = 0
  rw [hA]
  simp

/-! ## The local telescope steps -/

section LocalSteps
set_option maxHeartbeats 1600000
set_option maxRecDepth 16384

/-- Local step at `k = 0` (all three ladder values are `1`):
    `a₂ + a₁ + a₀ = certW(1) − certW(0)` — the boundary identity
    `W(0) = −rhs` in step form ([W0] in the pre-verification). -/
theorem certW_local_step_zero {q x : K} (hq : q ≠ 0) (hx : x ≠ 0) :
    feCoeff 2 q x + feCoeff 1 q x + feCoeff 0 q x
      = certW q x 1 - certW q x 0 := by
  show feCoeff 2 q x + feCoeff 1 q x + feCoeff 0 q x
      = -((q * x - 1) ^ 2 * (q * x + 1) * (q * x ^ 2 - 1)
          * (q ^ 3 * x ^ 2 - 1)) / (q ^ 2 * x ^ 8) - -feRhs q x
  simp only [feCoeff, feRhs]
  field_simp
  ring

/-- Local step at `k = 1`: the three ladder factors are the explicit
    `Λ_M − λ₁`, and `certW 2` is the explicit cleared form. -/
theorem certW_local_step_one {q : K} (hq : q ≠ 0) (N : ℕ) :
    feCoeff 2 q (q ^ N) * (lam q (N + 2) - lam q 1)
        + feCoeff 1 q (q ^ N) * (lam q (N + 1) - lam q 1)
        + feCoeff 0 q (q ^ N) * (lam q N - lam q 1)
      = certW q (q ^ N) 2 - certW q (q ^ N) 1 := by
  have hx : (q : K) ^ N ≠ 0 := pow_ne_zero _ hq
  have hxq1 : (q : K) ^ (N + 1) = q * q ^ N := by rw [pow_succ]; ring
  have hxq2 : (q : K) ^ (N + 2) = q * (q * q ^ N) := by
    rw [pow_succ, pow_succ]; ring
  have hl0 : lam q N - lam q 1
      = (q ^ N - q) * (q ^ N * q - 1) / (q ^ N * q) := by
    unfold lam
    rw [pow_one]
    field_simp
    ring
  have hl1 : lam q (N + 1) - lam q 1
      = (q * q ^ N - q) * (q * q ^ N * q - 1) / (q * q ^ N * q) := by
    unfold lam
    rw [pow_one, hxq1]
    field_simp
    ring
  have hl2 : lam q (N + 2) - lam q 1
      = (q * (q * q ^ N) - q) * (q * (q * q ^ N) * q - 1)
          / (q * (q * q ^ N) * q) := by
    unfold lam
    rw [pow_one, hxq2]
    field_simp
    ring
  rw [hl0, hl1, hl2]
  show feCoeff 2 q (q ^ N)
        * ((q * (q * q ^ N) - q) * (q * (q * q ^ N) * q - 1)
            / (q * (q * q ^ N) * q))
      + feCoeff 1 q (q ^ N)
        * ((q * q ^ N - q) * (q * q ^ N * q - 1) / (q * q ^ N * q))
      + feCoeff 0 q (q ^ N)
        * ((q ^ N - q) * (q ^ N * q - 1) / (q ^ N * q))
    = -((q * q ^ N + 1) * (q * (q ^ N) ^ 2 - 1) * (q ^ 3 * (q ^ N) ^ 2 - 1)
          * (1 - q ^ N) * (1 - q * q ^ N) * q ^ (0 + 2)
          * risingA q (q ^ N) 0 * risingB q (q ^ N) (0 + 2))
        / (q ^ 2 * (q ^ N) ^ 7 * clearD q (q ^ N) (0 + 2))
      - -((q * q ^ N - 1) ^ 2 * (q * q ^ N + 1) * (q * (q ^ N) ^ 2 - 1)
          * (q ^ 3 * (q ^ N) ^ 2 - 1)) / (q ^ 2 * (q ^ N) ^ 8)
  simp only [feCoeff, risingA, risingB, clearD,
    Finset.prod_range_succ, Finset.prod_range_zero]
  norm_num
  field_simp
  ring

/-- **Local step at `k = m + 2` — the master identity.**  All divisions are
    by powers of `q`, `x` and by `clearD` (nonzero); the B-side shift
    denominators `(xq−1)`, `(xq²−1)` are consumed exactly by the factors
    the operator supplies, so the identity holds for every `q ≠ 0` —
    roots of unity included ([K3] + [SIM] in the pre-verification). -/
theorem certW_local_step {q : K} (hq : q ≠ 0) (N m : ℕ) :
    feCoeff 2 q (q ^ N) * newtonLadder (lam q) (lam q (N + 2)) (m + 2)
        + feCoeff 1 q (q ^ N) * newtonLadder (lam q) (lam q (N + 1)) (m + 2)
        + feCoeff 0 q (q ^ N) * newtonLadder (lam q) (lam q N) (m + 2)
      = certW q (q ^ N) (m + 3) - certW q (q ^ N) (m + 2) := by
  have hx : (q : K) ^ N ≠ 0 := pow_ne_zero _ hq
  have hD : clearD q (q ^ N) (m + 2) ≠ 0 := clearD_ne_zero hq hx _
  have hqp : ∀ a : ℕ, (q : K) ^ a ≠ 0 := fun a => pow_ne_zero _ hq
  have hxq1 : (q : K) ^ (N + 1) = q * q ^ N := by rw [pow_succ]; ring
  have hxq2 : (q : K) ^ (N + 2) = q * (q * q ^ N) := by
    rw [pow_succ, pow_succ]; ring
  -- B-side constraints (division-free)
  have hc1 : (q ^ N * q - 1) * risingB q (q * q ^ N) (m + 2)
      = risingB q (q ^ N) (m + 2) * (q ^ N * q ^ (m + 2 + 1) - 1) := by
    rw [risingB_shift, risingB_succ]
  have hc2 : (q * q ^ N * q - 1) * risingB q (q * (q * q ^ N)) (m + 2)
      = risingB q (q * q ^ N) (m + 2) * (q * q ^ N * q ^ (m + 2 + 1) - 1) := by
    rw [risingB_shift, risingB_succ]
  -- ladder value at color N
  have hF0 : newtonLadder (lam q) (lam q N) (m + 2)
      = risingA q (q ^ N) m * (q ^ N - q ^ (m + 1)) * (q ^ N - q ^ (m + 2))
          * risingB q (q ^ N) (m + 2) / clearD q (q ^ N) (m + 2) := by
    rw [eq_div_iff hD]
    calc newtonLadder (lam q) (lam q N) (m + 2) * clearD q (q ^ N) (m + 2)
        = risingA q (q ^ N) (m + 2) * risingB q (q ^ N) (m + 2) :=
          newtonLadder_lam_split hq N (m + 2)
      _ = risingA q (q ^ N) m * (q ^ N - q ^ (m + 1)) * (q ^ N - q ^ (m + 2))
            * risingB q (q ^ N) (m + 2) := by
          rw [risingA_succ, risingA_succ]
  -- ladder value at color N + 1
  have hF1 : newtonLadder (lam q) (lam q (N + 1)) (m + 2)
      = (q ^ N - 1) * risingA q (q ^ N) m * (q ^ N - q ^ (m + 1))
          * risingB q (q * q ^ N) (m + 2) / clearD q (q ^ N) (m + 2) := by
    rw [eq_div_iff hD]
    refine mul_left_cancel₀ (hqp (m + 2)) ?_
    have hsplit := newtonLadder_lam_split hq (N + 1) (m + 2)
    rw [hxq1] at hsplit
    have hfold : (∏ j ∈ Finset.range (m + 2), (q * q ^ N * q ^ (j + 1)))
        = clearD q (q * q ^ N) (m + 2) := rfl
    rw [hfold] at hsplit
    calc q ^ (m + 2)
            * (newtonLadder (lam q) (lam q (N + 1)) (m + 2)
                * clearD q (q ^ N) (m + 2))
        = newtonLadder (lam q) (lam q (N + 1)) (m + 2)
            * (q ^ (m + 2) * clearD q (q ^ N) (m + 2)) := by ring
      _ = newtonLadder (lam q) (lam q (N + 1)) (m + 2)
            * clearD q (q * q ^ N) (m + 2) := by rw [← clearD_shift]
      _ = risingA q (q * q ^ N) (m + 2) * risingB q (q * q ^ N) (m + 2) :=
          hsplit
      _ = q ^ (m + 2) * (q ^ N - 1) * risingA q (q ^ N) (m + 1)
            * risingB q (q * q ^ N) (m + 2) := by rw [risingA_shift]
      _ = q ^ (m + 2) * (q ^ N - 1)
            * (risingA q (q ^ N) m * (q ^ N - q ^ (m + 1)))
            * risingB q (q * q ^ N) (m + 2) := by rw [risingA_succ]
      _ = q ^ (m + 2)
            * ((q ^ N - 1) * risingA q (q ^ N) m * (q ^ N - q ^ (m + 1))
                * risingB q (q * q ^ N) (m + 2)) := by ring
  -- ladder value at color N + 2
  have hF2 : newtonLadder (lam q) (lam q (N + 2)) (m + 2)
      = (q * q ^ N - 1) * (q ^ N - 1) * risingA q (q ^ N) m
          * risingB q (q * (q * q ^ N)) (m + 2)
          / (q * clearD q (q ^ N) (m + 2)) := by
    rw [eq_div_iff (mul_ne_zero hq hD)]
    refine mul_left_cancel₀ (mul_ne_zero (hqp (m + 2)) (hqp (m + 1))) ?_
    have hsplit := newtonLadder_lam_split hq (N + 2) (m + 2)
    rw [hxq2] at hsplit
    have hfold : (∏ j ∈ Finset.range (m + 2), (q * (q * q ^ N) * q ^ (j + 1)))
        = clearD q (q * (q * q ^ N)) (m + 2) := rfl
    rw [hfold] at hsplit
    calc q ^ (m + 2) * q ^ (m + 1)
            * (newtonLadder (lam q) (lam q (N + 2)) (m + 2)
                * (q * clearD q (q ^ N) (m + 2)))
        = newtonLadder (lam q) (lam q (N + 2)) (m + 2)
            * (q ^ (m + 2) * (q ^ (m + 1) * q * clearD q (q ^ N) (m + 2))) := by
          ring
      _ = newtonLadder (lam q) (lam q (N + 2)) (m + 2)
            * (q ^ (m + 2) * (q ^ (m + 2) * clearD q (q ^ N) (m + 2))) := by
          rw [pow_succ]
      _ = newtonLadder (lam q) (lam q (N + 2)) (m + 2)
            * (q ^ (m + 2) * clearD q (q * q ^ N) (m + 2)) := by
          rw [← clearD_shift]
      _ = newtonLadder (lam q) (lam q (N + 2)) (m + 2)
            * clearD q (q * (q * q ^ N)) (m + 2) := by
          rw [← clearD_shift q (q * q ^ N)]
      _ = risingA q (q * (q * q ^ N)) (m + 2)
            * risingB q (q * (q * q ^ N)) (m + 2) := hsplit
      _ = q ^ (m + 2) * (q * q ^ N - 1) * risingA q (q * q ^ N) (m + 1)
            * risingB q (q * (q * q ^ N)) (m + 2) := by rw [risingA_shift]
      _ = q ^ (m + 2) * (q * q ^ N - 1)
            * (q ^ (m + 1) * (q ^ N - 1) * risingA q (q ^ N) m)
            * risingB q (q * (q * q ^ N)) (m + 2) := by rw [risingA_shift]
      _ = q ^ (m + 2) * q ^ (m + 1)
            * ((q * q ^ N - 1) * (q ^ N - 1) * risingA q (q ^ N) m
                * risingB q (q * (q * q ^ N)) (m + 2)) := by ring
  -- eliminate B2 (the a2-factor (xq^2-1) and the A-shift factor (qx-1)
  -- exactly consume both shift denominators)
  have hB2elim : (q ^ N * q ^ 2 - 1)
        * ((q * q ^ N - 1) * risingB q (q * (q * q ^ N)) (m + 2))
      = risingB q (q ^ N) (m + 2) * (q ^ N * q ^ (m + 2 + 1) - 1)
          * (q * q ^ N * q ^ (m + 2 + 1) - 1) := by
    calc (q ^ N * q ^ 2 - 1)
            * ((q * q ^ N - 1) * risingB q (q * (q * q ^ N)) (m + 2))
        = (q * q ^ N * q - 1) * risingB q (q * (q * q ^ N)) (m + 2)
            * (q ^ N * q - 1) := by ring
      _ = risingB q (q * q ^ N) (m + 2) * (q * q ^ N * q ^ (m + 2 + 1) - 1)
            * (q ^ N * q - 1) := by rw [hc2]
      _ = (q ^ N * q - 1) * risingB q (q * q ^ N) (m + 2)
            * (q * q ^ N * q ^ (m + 2 + 1) - 1) := by ring
      _ = risingB q (q ^ N) (m + 2) * (q ^ N * q ^ (m + 2 + 1) - 1)
            * (q * q ^ N * q ^ (m + 2 + 1) - 1) := by rw [hc1]
  -- assemble
  rw [hF0, hF1, hF2]
  show feCoeff 2 q (q ^ N)
        * ((q * q ^ N - 1) * (q ^ N - 1) * risingA q (q ^ N) m
            * risingB q (q * (q * q ^ N)) (m + 2)
            / (q * clearD q (q ^ N) (m + 2)))
      + feCoeff 1 q (q ^ N)
        * ((q ^ N - 1) * risingA q (q ^ N) m * (q ^ N - q ^ (m + 1))
            * risingB q (q * q ^ N) (m + 2) / clearD q (q ^ N) (m + 2))
      + feCoeff 0 q (q ^ N)
        * (risingA q (q ^ N) m * (q ^ N - q ^ (m + 1)) * (q ^ N - q ^ (m + 2))
            * risingB q (q ^ N) (m + 2) / clearD q (q ^ N) (m + 2))
    = -((q * q ^ N + 1) * (q * (q ^ N) ^ 2 - 1) * (q ^ 3 * (q ^ N) ^ 2 - 1)
          * (1 - q ^ N) * (1 - q * q ^ N) * q ^ (m + 3)
          * risingA q (q ^ N) (m + 1) * risingB q (q ^ N) (m + 2 + 1))
        / (q ^ 2 * (q ^ N) ^ 7 * clearD q (q ^ N) (m + 2 + 1))
      - -((q * q ^ N + 1) * (q * (q ^ N) ^ 2 - 1) * (q ^ 3 * (q ^ N) ^ 2 - 1)
          * (1 - q ^ N) * (1 - q * q ^ N) * q ^ (m + 2)
          * risingA q (q ^ N) m * risingB q (q ^ N) (m + 2))
        / (q ^ 2 * (q ^ N) ^ 7 * clearD q (q ^ N) (m + 2))
  rw [show risingA q (q ^ N) (m + 1)
        = risingA q (q ^ N) m * (q ^ N - q ^ (m + 1)) from
      risingA_succ q (q ^ N) m,
    show risingB q (q ^ N) (m + 2 + 1)
        = risingB q (q ^ N) (m + 2) * (q ^ N * q ^ (m + 2 + 1) - 1) from
      risingB_succ q (q ^ N) (m + 2),
    show clearD q (q ^ N) (m + 2 + 1)
        = clearD q (q ^ N) (m + 2) * (q ^ N * q ^ (m + 2 + 1)) from
      clearD_succ q (q ^ N) (m + 2)]
  -- expose the eliminations inside the a2 and a1 terms
  have ha2 : feCoeff 2 q (q ^ N)
        * ((q * q ^ N - 1) * (q ^ N - 1) * risingA q (q ^ N) m
            * risingB q (q * (q * q ^ N)) (m + 2)
            / (q * clearD q (q ^ N) (m + 2)))
      = ((q ^ N) ^ 2 * q - 1) * (q ^ N - 1) * risingA q (q ^ N) m
          * (risingB q (q ^ N) (m + 2) * (q ^ N * q ^ (m + 2 + 1) - 1)
              * (q * q ^ N * q ^ (m + 2 + 1) - 1))
        / ((q ^ N) ^ 6 * (q * clearD q (q ^ N) (m + 2))) := by
    show (q ^ N * q ^ 2 - 1) * ((q ^ N) ^ 2 * q - 1) / (q ^ N) ^ 6
        * ((q * q ^ N - 1) * (q ^ N - 1) * risingA q (q ^ N) m
            * risingB q (q * (q * q ^ N)) (m + 2)
            / (q * clearD q (q ^ N) (m + 2)))
      = ((q ^ N) ^ 2 * q - 1) * (q ^ N - 1) * risingA q (q ^ N) m
          * (risingB q (q ^ N) (m + 2) * (q ^ N * q ^ (m + 2 + 1) - 1)
              * (q * q ^ N * q ^ (m + 2 + 1) - 1))
        / ((q ^ N) ^ 6 * (q * clearD q (q ^ N) (m + 2)))
    rw [← hB2elim]
    ring
  have ha1 : feCoeff 1 q (q ^ N)
        * ((q ^ N - 1) * risingA q (q ^ N) m * (q ^ N - q ^ (m + 1))
            * risingB q (q * q ^ N) (m + 2) / clearD q (q ^ N) (m + 2))
      = -((q ^ N * q - 1) * (q ^ N * q + 1)
          * ((q ^ N) ^ 4 * q ^ 4 - (q ^ N) ^ 3 * q ^ 3 - (q ^ N) ^ 2 * q ^ 3
              - (q ^ N) ^ 2 * q - q ^ N * q + 1)
          * (q ^ N - 1) * risingA q (q ^ N) m * (q ^ N - q ^ (m + 1))
          * (risingB q (q ^ N) (m + 2) * (q ^ N * q ^ (m + 2 + 1) - 1)))
        / ((q ^ N) ^ 8 * q ^ 2 * clearD q (q ^ N) (m + 2)) := by
    show -((q ^ N * q - 1) ^ 2 * (q ^ N * q + 1)
          * ((q ^ N) ^ 4 * q ^ 4 - (q ^ N) ^ 3 * q ^ 3 - (q ^ N) ^ 2 * q ^ 3
              - (q ^ N) ^ 2 * q - q ^ N * q + 1)) / ((q ^ N) ^ 8 * q ^ 2)
        * ((q ^ N - 1) * risingA q (q ^ N) m * (q ^ N - q ^ (m + 1))
            * risingB q (q * q ^ N) (m + 2) / clearD q (q ^ N) (m + 2))
      = -((q ^ N * q - 1) * (q ^ N * q + 1)
          * ((q ^ N) ^ 4 * q ^ 4 - (q ^ N) ^ 3 * q ^ 3 - (q ^ N) ^ 2 * q ^ 3
              - (q ^ N) ^ 2 * q - q ^ N * q + 1)
          * (q ^ N - 1) * risingA q (q ^ N) m * (q ^ N - q ^ (m + 1))
          * (risingB q (q ^ N) (m + 2) * (q ^ N * q ^ (m + 2 + 1) - 1)))
        / ((q ^ N) ^ 8 * q ^ 2 * clearD q (q ^ N) (m + 2))
    rw [← hc1]
    ring
  rw [ha2, ha1]
  simp only [feCoeff]
  have e1 : (q : K) ^ (m + 2) = q ^ (m + 1) * q := by ring
  have e2 : (q : K) ^ (m + 3) = q ^ (m + 1) * q ^ 2 := by ring
  rw [e1, e2]
  field_simp
  ring

end LocalSteps

/-! ## The summed telescope -/

section Summed
set_option maxHeartbeats 800000

/-- **General-`N` annihilation, proved for every `q ≠ 0`** (roots of unity
    included): the explicit operator annihilates the colored Jones tower
    of the figure-eight.  `N = 0` is a direct computation; `N ≥ 1` is the
    division-free certificate telescope. -/
theorem figureEightOperator_annihilates {q : K} (hq : q ≠ 0) :
    Annihilates (figureEightOperator (K := K)) q (coloredJones41 q) := by
  intro N
  show ∑ j ∈ Finset.range (2 + 1),
      feCoeff j q (q ^ N) * coloredJones41 q (N + j) = feRhs q (q ^ N)
  match N with
  | 0 =>
      have h2 : q ^ 2 ≠ 0 := pow_ne_zero _ hq
      have h3 : q ^ 3 ≠ 0 := pow_ne_zero _ hq
      have hJ0 : coloredJones41 q 0 = 0 := by simp [coloredJones41]
      have hJ1 : coloredJones41 q 1 = 1 := by
        simp [coloredJones41, habiroTerm]
      rw [Finset.sum_range_succ, Finset.sum_range_succ,
        Finset.sum_range_one]
      show feCoeff 0 q (q ^ 0) * coloredJones41 q (0 + 0)
          + feCoeff 1 q (q ^ 0) * coloredJones41 q (0 + 1)
          + feCoeff 2 q (q ^ 0) * coloredJones41 q (0 + 2)
        = feRhs q (q ^ 0)
      rw [show (0 + 0 : ℕ) = 0 from rfl, show (0 + 1 : ℕ) = 1 from rfl,
        show (0 + 2 : ℕ) = 2 from rfl, hJ0, hJ1, coloredJones41_two hq,
        pow_zero]
      simp only [feCoeff, feRhs]
      field_simp
      ring
  | (M + 1) =>
      have hN : 1 ≤ M + 1 := by omega
      have hx : (q : K) ^ (M + 1) ≠ 0 := pow_ne_zero _ hq
      have hJ0 : coloredJones41 q (M + 1)
          = ∑ k ∈ Finset.range (M + 1 + 2),
              newtonLadder (lam q) (lam q (M + 1)) k :=
        coloredJones41_sum_stable hq hN (by omega)
      have hJ1 : coloredJones41 q (M + 1 + 1)
          = ∑ k ∈ Finset.range (M + 1 + 2),
              newtonLadder (lam q) (lam q (M + 1 + 1)) k :=
        coloredJones41_sum_stable hq (by omega) (by omega)
      have hJ2 : coloredJones41 q (M + 1 + 2)
          = ∑ k ∈ Finset.range (M + 1 + 2),
              newtonLadder (lam q) (lam q (M + 1 + 2)) k :=
        coloredJones41_eq_newton_sum hq (M + 1 + 2)
      rw [Finset.sum_range_succ, Finset.sum_range_succ,
        Finset.sum_range_one]
      show feCoeff 0 q (q ^ (M + 1)) * coloredJones41 q (M + 1 + 0)
          + feCoeff 1 q (q ^ (M + 1)) * coloredJones41 q (M + 1 + 1)
          + feCoeff 2 q (q ^ (M + 1)) * coloredJones41 q (M + 1 + 2)
        = feRhs q (q ^ (M + 1))
      rw [show (M + 1 + 0 : ℕ) = M + 1 from rfl, hJ0, hJ1, hJ2,
        Finset.mul_sum, Finset.mul_sum, Finset.mul_sum,
        ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
      have hstep : ∀ k ∈ Finset.range (M + 1 + 2),
          feCoeff 0 q (q ^ (M + 1))
              * newtonLadder (lam q) (lam q (M + 1)) k
            + feCoeff 1 q (q ^ (M + 1))
              * newtonLadder (lam q) (lam q (M + 1 + 1)) k
            + feCoeff 2 q (q ^ (M + 1))
              * newtonLadder (lam q) (lam q (M + 1 + 2)) k
          = certW q (q ^ (M + 1)) (k + 1) - certW q (q ^ (M + 1)) k := by
        intro k _
        match k with
        | 0 =>
            simp only [newtonLadder_zero, mul_one]
            rw [show (0 + 1 : ℕ) = 1 from rfl]
            linear_combination certW_local_step_zero (q := q)
              (x := q ^ (M + 1)) hq hx
        | 1 =>
            have hL : ∀ M' : ℕ, newtonLadder (lam q) (lam q M') 1
                = lam q M' - lam q 1 := by
              intro M'
              show ∏ j ∈ Finset.range 1, (lam q M' - lam q (j + 1))
                  = lam q M' - lam q 1
              rw [Finset.prod_range_one]
            rw [hL (M + 1), hL (M + 1 + 1), hL (M + 1 + 2),
              show (1 + 1 : ℕ) = 2 from rfl]
            linear_combination certW_local_step_one hq (M + 1)
        | (m + 2) =>
            rw [show m + 2 + 1 = m + 3 from rfl]
            linear_combination certW_local_step hq (M + 1) m
      rw [Finset.sum_congr rfl hstep,
        Finset.sum_range_sub (f := fun k => certW q (q ^ (M + 1)) k)]
      show certW q (q ^ (M + 1)) (M + 1 + 2) - certW q (q ^ (M + 1)) 0
          = feRhs q (q ^ (M + 1))
      rw [certW_top_eq_zero q hN]
      show 0 - -feRhs q (q ^ (M + 1)) = feRhs q (q ^ (M + 1))
      ring

end Summed

/-! ## The sorry-free instance -/

/-- **Strong AJ for the figure-eight — every field is machine-checked.**
    Supersedes the cited-sorry instance formerly in `AJFigureEight.lean`:
    the general-`N` annihilation is the proved
    `figureEightOperator_annihilates` (division-free certificate
    telescope, valid at every `q ≠ 0` including roots of unity). -/
instance [CharZero K] : StrongAJFigureEight K where
  op := figureEightOperator
  order_eq := rfl
  nontrivial := fun _ hq => figureEightOperator_nontrivial hq
  annihilates := fun _ hq => figureEightOperator_annihilates hq
  unit := feUnit
  unit_nondegenerate := feUnit_nondegenerate
  specializes := figureEightOperator_specializes

end QOU.BraidKnot.AJFigureEight
