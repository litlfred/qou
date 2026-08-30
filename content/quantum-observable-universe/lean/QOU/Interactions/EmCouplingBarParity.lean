import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# Bar parity of the electromagnetic coupling object

The EM coupling object is `α_EM⁻¹ = q·[9]_q·[10]_q` (bare; CS-tower dressed
downstream). This file proves, over any field and sorry-free, the exact bar
(`q ↦ q⁻¹`) decomposition that fills the coupling-level cell of the
interaction-sector taxonomy (`def:interaction-sector-taxonomy`):

* the quantum integer `[n]_q` is **bar-even** (invariant), with no
  nondegeneracy hypotheses — numerator and denominator flip sign together,
  and the degenerate cases agree on both sides under the `x/0 = 0`
  convention;
* therefore the bare coupling `C(q) = q·[9]_q·[10]_q` satisfies
  `C(q) ± C(q⁻¹) = (q ± q⁻¹)·[9]_q·[10]_q` — its bar-even part is the
  **cosh channel** (strong side) and its bar-odd part the **sinh channel**
  (weak side) of the same invariant factor `B = [9]_q·[10]_q`. The EM
  coupling is the full exponential mix `e^λ·B`, not a pure channel.

Observable level (added same day, bean qou-z2xz): `α = C⁻¹` carries the
conjugate exponential `e^{−λ}` and the Hartree scale `α²` the doubled
`e^{−2λ}`; and under nondegeneracy (`q² ≠ ±1`, `B ≠ 0` — true at the real
anchor) the coupling is provably NEITHER bar-even NOR bar-odd. So the
electromagnetic taxonomy cell is not merely unassigned — no pure-parity
assignment exists. Numeric twin (proton pin, 60 dps):
`computations/probes/alpha_em_bar_parity_probe.py`.
-/

namespace QOU.Interactions

variable {K : Type*} [Field K]

/-- The quantum integer `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`. -/
def qint (n : ℕ) (q : K) : K := (q ^ n - q⁻¹ ^ n) / (q - q⁻¹)

/-- `[n]_q` is bar-even: invariant under `q ↦ q⁻¹`. No hypotheses — the
degenerate denominators agree on both sides under the field convention. -/
theorem qint_bar_even (n : ℕ) (q : K) : qint n q⁻¹ = qint n q := by
  unfold qint
  rw [inv_inv, ← neg_sub (q ^ n), ← neg_sub q, neg_div_neg_eq]

/-- The bare electromagnetic coupling object `C(q) = q·[9]_q·[10]_q`. -/
def emCouplingBare (q : K) : K := q * (qint 9 q * qint 10 q)

/-- Bar image of the coupling: only the exponential prefactor moves. -/
theorem emCouplingBare_bar (q : K) :
    emCouplingBare q⁻¹ = q⁻¹ * (qint 9 q * qint 10 q) := by
  unfold emCouplingBare
  rw [qint_bar_even 9 q, qint_bar_even 10 q]

/-- **Exact bar decomposition of the EM coupling**: its even part is the
cosh-channel multiple of the bar-invariant `B = [9]_q·[10]_q` and its odd
part the sinh-channel multiple — the EM coupling is the full exponential
mix, not a pure bar channel. -/
theorem emCouplingBare_even_odd (q : K) :
    emCouplingBare q + emCouplingBare q⁻¹
        = (q + q⁻¹) * (qint 9 q * qint 10 q) ∧
    emCouplingBare q - emCouplingBare q⁻¹
        = (q - q⁻¹) * (qint 9 q * qint 10 q) := by
  constructor <;> · rw [emCouplingBare_bar]; unfold emCouplingBare; ring

/-- The odd and even parts differ by the sinh/cosh factor pair: twice the
even part is `(q+q⁻¹)·B`, twice the odd part is `(q−q⁻¹)·B`, whose ratio is
the `tanh` of the substrate rapidity (numerically ≈ 0.104 at the proton
pin — the probe's measured value). Stated multiplicatively to avoid a
division hypothesis. -/
theorem emCoupling_channel_ratio (q : K) :
    (q - q⁻¹) * (emCouplingBare q + emCouplingBare q⁻¹)
      = (q + q⁻¹) * (emCouplingBare q - emCouplingBare q⁻¹) := by
  obtain ⟨he, ho⟩ := emCouplingBare_even_odd q
  rw [he, ho]; ring

/-! ## Observable level: `α` and the Hartree scale `α²` -/

/-- The fine-structure object itself, `α = C(q)⁻¹`. The EM sector's
comparison observables (Coulomb energy, Hartree/Rydberg scale) carry their
`q`-dependence through `α` and `α²`; the remaining factors are
`q`-independent calibration constants. -/
def emAlpha (q : K) : K := (emCouplingBare q)⁻¹

theorem emAlpha_bar (q : K) :
    emAlpha q⁻¹ = q * (qint 9 q * qint 10 q)⁻¹ := by
  unfold emAlpha
  rw [emCouplingBare_bar, mul_inv, inv_inv]

/-- `α` carries the **conjugate** exponential `e^{−λ}`: its bar-even part
is the cosh multiple and its bar-odd part the *negative* sinh multiple of
the bar-invariant `B⁻¹` — opposite odd-part sign to the coupling. -/
theorem emAlpha_even_odd (q : K) :
    emAlpha q + emAlpha q⁻¹ = (q + q⁻¹) * (qint 9 q * qint 10 q)⁻¹ ∧
    emAlpha q - emAlpha q⁻¹ = (q⁻¹ - q) * (qint 9 q * qint 10 q)⁻¹ := by
  constructor <;>
    · rw [emAlpha_bar]; unfold emAlpha emCouplingBare; rw [mul_inv]; ring

/-- The observable scale `α²` (the Hartree/Rydberg `q`-dependence)
decomposes with the doubled conjugate exponential `e^{−2λ}`. -/
theorem emAlphaSq_even_odd (q : K) :
    emAlpha q ^ 2 + emAlpha q⁻¹ ^ 2
        = (q ^ 2 + q⁻¹ ^ 2) * ((qint 9 q * qint 10 q)⁻¹) ^ 2 ∧
    emAlpha q ^ 2 - emAlpha q⁻¹ ^ 2
        = (q⁻¹ ^ 2 - q ^ 2) * ((qint 9 q * qint 10 q)⁻¹) ^ 2 := by
  constructor <;>
    · rw [emAlpha_bar]; unfold emAlpha emCouplingBare; rw [mul_inv]; ring

/-! ## The electromagnetic objects are provably NOT pure-parity

Under nondegeneracy — `q² ≠ 1`, `q² ≠ −1`, `B ≠ 0`, all of which hold at
the real substrate anchor `q₀ ≈ 1.11` — the coupling is neither bar-even
nor bar-odd. So the electromagnetic cell of the taxonomy is not merely
unassigned: **no pure-parity assignment exists**, unlike binding (pure
even) and `Q_β` (pure odd). -/

theorem emCouplingBare_not_bar_even (q : K) (hq : q ≠ 0) (h2 : q ^ 2 ≠ 1)
    (hB : qint 9 q * qint 10 q ≠ 0) :
    emCouplingBare q⁻¹ ≠ emCouplingBare q := by
  rw [emCouplingBare_bar]
  unfold emCouplingBare
  intro h
  have hqq : (q⁻¹ : K) = q := mul_right_cancel₀ hB h
  have h1 : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  rw [hqq] at h1
  exact h2 (by rw [sq]; exact h1)

theorem emCouplingBare_not_bar_odd (q : K) (hq : q ≠ 0) (h2 : q ^ 2 ≠ -1)
    (hB : qint 9 q * qint 10 q ≠ 0) :
    emCouplingBare q⁻¹ ≠ -emCouplingBare q := by
  rw [emCouplingBare_bar]
  unfold emCouplingBare
  intro h
  have h' : q⁻¹ * (qint 9 q * qint 10 q) = -q * (qint 9 q * qint 10 q) := by
    rw [neg_mul]; exact h
  have hqq : (q⁻¹ : K) = -q := mul_right_cancel₀ hB h'
  have h1 : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  rw [hqq] at h1
  exact h2 (by rw [sq]; linear_combination -h1)

end QOU.Interactions
