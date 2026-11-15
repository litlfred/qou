/-
# The SW ⊛ Jackson moment factorization — Lean-exact form of the
# KSel-2-ID literature identification

The KSel-2-ID audit
(`docs/audits/2026-08-01-ksel2id-friedrichs-sw-identification.md` §1)
identified the balanced kernel family's indeterminacy core in the
classical literature: at the moment level, with `p = q⁻¹` and
half-variable `v` (`v² = q`, `q̃ = v` in the audit's notation),

* the one-sided q-factorial rewrites exactly to base `p`:
  `[k]_q! · (1−p)^k = q^{C(k,2)} · (p;p)_k` — Moak's α = 0 q-Laguerre
  moment family under a pure scaling (`moak1981`);
* the balanced normalizer factors exactly as **SW-Gaussian ×
  Jackson**: `N^bal(k+1) · (1−p)^k = v^{C(k,2)} · (p;p)_k`, i.e.
  `m_k = G_k · J_k` with `G_k = v^{k(k−1)/2}` — the moment sequence of
  the log-normal `LN(−L/2, L)`, `L = ln v`, which is Stieltjes' 1894
  indeterminate example at base `√q` (`christiansen2003sw`,
  `berg1995`) — and `J_k = (p;p)_k/(1−p)^k` the moments of the
  determinate, compactly supported Jackson atomic measure.

This module proves both identities sorry-free over a generic field,
in division-free (cleared) form plus division corollaries. The
ANALYTIC halves of the identification — that `G_k` are the moments of
an actual log-normal measure, that the Jackson factor is determinate
with compact support, and the convolution reading — are wall-side
facts recorded in the audit and NOT formalized here; this file carries
the exact moment-level algebra that the identification rests on.

Reuses (compose-don't-restate): `qint`/`qfact`
(`QOU.Mass.QDifferenceConfluentObstruction`), `balancedNormalizer` and
the bar transform `pow_mul_qint_inv`
(`QOU.Archimedean.BalancedMomentConfluence`), `geom_sum_mul` (Mathlib).

-- Ref: [leitner2026] docs/audits/2026-08-01-ksel2id-friedrichs-sw-identification.md §1;
--      predicted-spectra, conj:schwinger-measure-computational-time;
--      [moak1981] q-Laguerre polynomials; [christiansen2003sw] SW moment
--      problem; [berg1995] indeterminate moment problems.
-/

import Mathlib.Algebra.Group.NatPowAssoc
import Mathlib.Algebra.Order.Field.GeomSum
import Mathlib.Algebra.Order.Ring.GeomSum
import Mathlib.Algebra.Ring.Regular
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Positivity.Basic
import QOU.Archimedean.BalancedMomentConfluence

namespace QOU.Archimedean.SWJacksonMomentFactorization

open QOU.Mass.QDifferenceConfluentObstruction (qint qfact)
open QOU.Archimedean.BalancedMomentConfluence (balancedNormalizer
  pow_mul_qint_inv)

variable {K : Type*} [Field K]

/-- The q-Pochhammer `(p;p)_k = ∏_{j=1}^k (1 − p^j)` — the numerator of
the Jackson moment sequence. -/
def pPoch (p : K) : ℕ → K
  | 0 => 1
  | k + 1 => pPoch p k * (1 - p ^ (k + 1))

@[simp] theorem pPoch_zero (p : K) : pPoch p 0 = 1 := rfl

theorem pPoch_succ (p : K) (k : ℕ) :
    pPoch p (k + 1) = pPoch p k * (1 - p ^ (k + 1)) := rfl

/-- Telescoped geometric sum: `[n]_p · (1−p) = 1 − p^n` (any `p`). -/
theorem qint_mul_one_sub (p : K) (n : ℕ) :
    qint p n * (1 - p) = 1 - p ^ n := by
  simp only [qint]
  linear_combination -geom_sum_mul p n

/-- Base-`p` rewrite of one quantum integer: `[k+1]_q · (1−q⁻¹) =
q^k · (1 − q^{−(k+1)})` — the single-index step behind Moak's
q-Laguerre scaling. -/
theorem qint_mul_one_sub_inv (q : K) (hq : q ≠ 0) (k : ℕ) :
    qint q (k + 1) * (1 - q⁻¹) = q ^ k * (1 - q⁻¹ ^ (k + 1)) := by
  rw [← pow_mul_qint_inv q hq k, mul_assoc, qint_mul_one_sub]

/-- **The q-Laguerre rewrite of the one-sided q-factorial**
(division-free): `[k]_q! · (1−p)^k = q^{C(k,2)} · (p;p)_k` at `p = q⁻¹`.
Equivalently `[k]_q! = p^{−C(k,2)}(p;p)_k/(1−p)^k` — the α = 0
q-Laguerre (generalized Stieltjes–Wigert) moment family under the pure
scaling `s ↦ (p/(1−p))·s` (`moak1981`; audit §1, EXACT verdict). -/
theorem qfact_mul_one_sub_pow (q : K) (hq : q ≠ 0) (k : ℕ) :
    qfact q k * (1 - q⁻¹) ^ k = q ^ (k.choose 2) * pPoch q⁻¹ k := by
  induction k with
  | zero => simp [qfact]
  | succ k ih =>
      have hchoose : (k + 1).choose 2 = k + k.choose 2 := by
        rw [Nat.choose_succ_succ, Nat.choose_one_right]
      calc qfact q (k + 1) * (1 - q⁻¹) ^ (k + 1)
          = (qint q (k + 1) * (1 - q⁻¹)) * (qfact q k * (1 - q⁻¹) ^ k) := by
            rw [show qfact q (k + 1) = qint q (k + 1) * qfact q k from rfl,
              pow_succ]
            ring
        _ = (q ^ k * (1 - q⁻¹ ^ (k + 1)))
              * (q ^ (k.choose 2) * pPoch q⁻¹ k) := by
            rw [qint_mul_one_sub_inv q hq k, ih]
        _ = q ^ ((k + 1).choose 2) * pPoch q⁻¹ (k + 1) := by
            rw [hchoose, pow_add, pPoch_succ]
            ring

/-- **The SW ⊛ Jackson factorization at moment level** (division-free):
`N^bal(k+1) · (1−p)^k = v^{C(k,2)} · (p;p)_k` with `p = (v²)⁻¹`. The
factor `v^{C(k,2)} = q̃^{k(k−1)/2}` is the moment sequence `G_k` of the
log-normal `LN(−L/2, L)` — Stieltjes' 1894 indeterminate example at
base `q̃ = √q`, the KSel-3 "one Gaussian" — and `(p;p)_k/(1−p)^k` is
the Jackson moment sequence `J_k`. So `m_k = G_k · J_k` exactly:
the balanced family's indeterminacy core IS the classical SW
log-normal. -/
theorem balancedNormalizer_mul_one_sub_pow (v : K) (hv : v ≠ 0) (k : ℕ) :
    balancedNormalizer v (k + 1) * (1 - (v ^ 2)⁻¹) ^ k
      = v ^ (k.choose 2) * pPoch (v ^ 2)⁻¹ k := by
  have hv2 : (v ^ 2 : K) ≠ 0 := pow_ne_zero _ hv
  have hA := qfact_mul_one_sub_pow (v ^ 2) hv2 k
  unfold balancedNormalizer
  simp only [Nat.add_sub_cancel]
  calc (v ^ (k.choose 2))⁻¹ * qfact (v ^ 2) k * (1 - (v ^ 2)⁻¹) ^ k
      = (v ^ (k.choose 2))⁻¹ * (qfact (v ^ 2) k * (1 - (v ^ 2)⁻¹) ^ k) := by
        ring
    _ = (v ^ (k.choose 2))⁻¹ * ((v ^ 2) ^ (k.choose 2) * pPoch (v ^ 2)⁻¹ k) := by
        rw [hA]
    _ = v ^ (k.choose 2) * pPoch (v ^ 2)⁻¹ k := by
        rw [← pow_mul, two_mul, pow_add]
        field_simp

/-- Division form of the factorization: `m_k = G_k · J_k` literally,
under the nondegeneracy `1 − p ≠ 0` (i.e. `q ≠ 1`). -/
theorem balancedNormalizer_eq_gauss_mul_jackson (v : K) (hv : v ≠ 0)
    (hp : (1 : K) - (v ^ 2)⁻¹ ≠ 0) (k : ℕ) :
    balancedNormalizer v (k + 1)
      = v ^ (k.choose 2) * (pPoch (v ^ 2)⁻¹ k / (1 - (v ^ 2)⁻¹) ^ k) := by
  have h := balancedNormalizer_mul_one_sub_pow v hv k
  have hpk : ((1 : K) - (v ^ 2)⁻¹) ^ k ≠ 0 := pow_ne_zero _ hp
  rw [← mul_div_assoc, eq_div_iff hpk]
  exact h

end QOU.Archimedean.SWJacksonMomentFactorization
