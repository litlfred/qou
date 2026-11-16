/-
# Extensivity decides the binding law

The `Delta_bind` arc ended on a refutation and a replacement, and both are
statements about **growth class**, not about nuclear data. This file proves them
with no data in it.

The closed form derived in `computations/qbeta/qbeta_bond_factors_derived_probe.py`
makes the Markov trace of the atom word a **product** along the chain:

```
tr_M(beta_free) = t_p^Z . t_n^N
tr_M(beta_atom) = t_p^Z . t_n^N . b_pp^(Z-1) . b_pn . b_nn^(N-1)
```

Binding energy is **extensive** — a sum over bonds, so `Theta(A)` in the nucleon
count. Two consequences, and they are the whole argument:

1. **`B = s . (tr_free - tr_atom)` cannot hold at any scale.** The difference
   carries the factor `t_p^Z` with `t_p > 1`, and no constant multiple of an
   exponential is bounded by a line. `exists_pow_gt_linear`.

2. **`B = E_0 . log(tr_free / tr_atom)` is extensive by construction.** The
   `t_p^Z t_n^N` factor cancels in the ratio and the log of the remaining
   product is the bond sum, which is pinned between two lines through the
   origin. `linear_le_bondSum`, `bondSum_le_linear`.

`log` is the unique map carrying multiplicative to additive, so the second law is
*forced* rather than chosen — and it consumes exactly the same derived bond
factors as the first. Measured consequence, over the 2548 AME2020 nuclides with
measured binding energies: p5-p95 residual spread `1592x` for law 1 against
`1.225x` for law 2.

## What is proved here, and what is measurement

**Proved:** everything above, for an arbitrary base `t` with `1 < t` and
arbitrary bond energies. The growth-class separation is pure ordered-field
algebra and needs no substrate constant.

**Measurement, and NOT proved here:** that `t_p = 1.1457596925 > 1`, and that the
three bond energies `-ln b_pp = 0.4899`, `-ln b_pn = 0.6768`, `-ln b_nn = 0.9073`
are positive. Those are the hypotheses this file's theorems take. They are
established numerically at 30 dps by
`computations/qbeta/qbeta_binding_law_options_probe.py`, whose witness is
`qbeta-binding-law-options.witness.json`. Stating which side of that line each
claim sits on is the point of formalising at all.

Decision frame, options and open avenues:
`docs/audits/2026-09-04-binding-law-options-decision-frame.md`.
-/

import Mathlib.Algebra.Order.Ring.Pow
import Mathlib.Tactic

namespace QOU.Hecke.BindingExtensivity

/-! ## 1. A multiplicative observable is not bounded by any line

The one lemma with content is Bernoulli applied twice: once to get `t^m` above a
line, once more by squaring to get `t^(2m)` above a *parabola*. A parabola beats
a line, and that is the entire obstruction. -/

/-- Bernoulli, squared: for `1 ≤ t` and any `m`, `t^(2m) ≥ (m(t-1))²`.

One application of `one_add_mul_le_pow` gives `1 + m(t-1) ≤ t^m`; squaring turns
the linear lower bound into a quadratic one, which is what outruns `C·n`. -/
lemma sq_mul_sub_one_le_pow_two_mul {t : ℝ} (ht : 1 ≤ t) (m : ℕ) :
    ((m : ℝ) * (t - 1)) ^ 2 ≤ t ^ (2 * m) := by
  have hd : (0 : ℝ) ≤ t - 1 := by linarith
  have hb : 1 + (m : ℝ) * (t - 1) ≤ t ^ m := by
    have h := one_add_mul_le_pow (a := t - 1) (by linarith) m
    simpa using h
  have h1 : (m : ℝ) * (t - 1) ≤ t ^ m := by linarith
  have h0 : (0 : ℝ) ≤ (m : ℝ) * (t - 1) := by positivity
  have hsq : ((m : ℝ) * (t - 1)) ^ 2 ≤ (t ^ m) ^ 2 := by
    gcongr
  calc ((m : ℝ) * (t - 1)) ^ 2 ≤ (t ^ m) ^ 2 := hsq
    _ = t ^ (2 * m) := by rw [← pow_mul, Nat.mul_comm]

/-- **No constant scale makes an exponential linear.**

For any base `t > 1`, any scale `s > 0` and any linear coefficient `C`, there is
an `n` with `C·n < s·t^n`.

This is the refutation of `B = s·Δtr` in its entirety: `Δtr` carries `t_p^Z` with
`t_p > 1` (measured 1.1458), binding energy is `Θ(A)`, and no choice of `s`
closes that gap. Measured counterpart: at the law's own optimal scale the
residual still spans 4.21 decades over the AME2020 table. -/
theorem exists_pow_gt_linear {t : ℝ} (ht : 1 < t) {s : ℝ} (hs : 0 < s) (C : ℝ) :
    ∃ n : ℕ, C * (n : ℝ) < s * t ^ n := by
  have hd0 : (0 : ℝ) < t - 1 := by linarith
  have hr : (0 : ℝ) < s * (t - 1) ^ 2 := by positivity
  -- Archimedean, division-free: `2C ≤ k · (s(t-1)²)` for some `k`.
  obtain ⟨k, hk⟩ := Archimedean.arch (2 * C) hr
  rw [nsmul_eq_mul] at hk
  refine ⟨2 * (k + 1), ?_⟩
  have hkm : ((k : ℝ)) < ((k : ℝ) + 1) := by linarith
  have hmpos : (0 : ℝ) < (k : ℝ) + 1 := by positivity
  -- strict at `m = k+1`, because the Archimedean bound was only `≤` at `k`
  have hkey : 2 * C < ((k : ℝ) + 1) * (s * (t - 1) ^ 2) := by
    nlinarith [hk, hr, hkm]
  have hstep : 2 * C * ((k : ℝ) + 1)
      < (((k : ℝ) + 1) * (s * (t - 1) ^ 2)) * ((k : ℝ) + 1) :=
    mul_lt_mul_of_pos_right hkey hmpos
  have hpow : (((k : ℝ) + 1) * (t - 1)) ^ 2 ≤ t ^ (2 * (k + 1)) := by
    have h := sq_mul_sub_one_le_pow_two_mul ht.le (k + 1)
    push_cast at h
    exact h
  have hcast : C * ((2 * (k + 1) : ℕ) : ℝ) = 2 * C * ((k : ℝ) + 1) := by
    push_cast; ring
  rw [hcast]
  calc 2 * C * ((k : ℝ) + 1)
      < (((k : ℝ) + 1) * (s * (t - 1) ^ 2)) * ((k : ℝ) + 1) := hstep
    _ = s * ((((k : ℝ) + 1) * (t - 1)) ^ 2) := by ring
    _ ≤ s * t ^ (2 * (k + 1)) := by
        exact mul_le_mul_of_nonneg_left hpow hs.le

/-! ## 2. The additive observable is extensive by construction

`log(tr_free / tr_atom)` is the bond sum of the canonical `A−1` chain. Its
growth class is settled by nothing more than the bond energies being bounded. -/

/-- The bond-energy sum of the canonical `A−1` chain, for `Z = p+1` protons and
`N = q+1` neutrons: `p` proton-proton bonds, one proton-neutron interface, and
`q` neutron-neutron bonds. Equals `log(tr_M(β_free) / tr_M(β_atom))` with
`epp = -ln b_pp`, `epn = -ln b_pn`, `enn = -ln b_nn`. -/
def bondSum (epp epn enn : ℝ) (p q : ℕ) : ℝ := p * epp + epn + q * enn

/-- The bond sum is bounded **above** by a line through the origin in `A−1`. -/
theorem bondSum_le_linear {epp epn enn M : ℝ} (hpp : epp ≤ M) (hpn : epn ≤ M)
    (hnn : enn ≤ M) (p q : ℕ) :
    bondSum epp epn enn p q ≤ M * ((p : ℝ) + q + 1) := by
  have h1 : (p : ℝ) * epp ≤ (p : ℝ) * M :=
    mul_le_mul_of_nonneg_left hpp (by positivity)
  have h2 : (q : ℝ) * enn ≤ (q : ℝ) * M :=
    mul_le_mul_of_nonneg_left hnn (by positivity)
  unfold bondSum
  nlinarith [h1, h2, hpn]

/-- The bond sum is bounded **below** by a line through the origin in `A−1`. -/
theorem linear_le_bondSum {epp epn enn m : ℝ} (hpp : m ≤ epp) (hpn : m ≤ epn)
    (hnn : m ≤ enn) (p q : ℕ) :
    m * ((p : ℝ) + q + 1) ≤ bondSum epp epn enn p q := by
  have h1 : (p : ℝ) * m ≤ (p : ℝ) * epp :=
    mul_le_mul_of_nonneg_left hpp (by positivity)
  have h2 : (q : ℝ) * m ≤ (q : ℝ) * enn :=
    mul_le_mul_of_nonneg_left hnn (by positivity)
  unfold bondSum
  nlinarith [h1, h2, hpn]

/-- **The two observables sit in different growth classes.**

With `A = p + q + 2` nucleons the additive observable is pinned between two lines
through the origin, for *every* `(p, q)` — that is what "extensive" means. The
multiplicative one is bounded by no line at all, at any scale.

This is §1.2 and §2 of the decision frame, with no nuclear data in it. The two
sides are not competing fits of the same shape; they are different shapes, and
only one of them can be a binding energy. -/
theorem additive_is_linear_multiplicative_is_not
    {epp epn enn m M t s : ℝ}
    (hmpp : m ≤ epp) (hmpn : m ≤ epn) (hmnn : m ≤ enn)
    (hMpp : epp ≤ M) (hMpn : epn ≤ M) (hMnn : enn ≤ M)
    (ht : 1 < t) (hs : 0 < s) (C : ℝ) :
    (∀ p q : ℕ, m * ((p : ℝ) + q + 1) ≤ bondSum epp epn enn p q ∧
                bondSum epp epn enn p q ≤ M * ((p : ℝ) + q + 1))
    ∧ ∃ n : ℕ, C * (n : ℝ) < s * t ^ n :=
  ⟨fun p q => ⟨linear_le_bondSum hmpp hmpn hmnn p q,
               bondSum_le_linear hMpp hMpn hMnn p q⟩,
   exists_pow_gt_linear ht hs C⟩

/-- The bond sum is **positive and unbounded** once every bond energy is, which
is the measured case (`0.4899`, `0.6768`, `0.9073`). Together with
`bondSum_le_linear` this says the additive law grows like `A` and not faster. -/
theorem bondSum_pos {epp epn enn m : ℝ} (hm : 0 < m) (hpp : m ≤ epp)
    (hpn : m ≤ epn) (hnn : m ≤ enn) (p q : ℕ) :
    0 < bondSum epp epn enn p q := by
  have h := linear_le_bondSum hpp hpn hnn p q
  have : (0 : ℝ) < m * ((p : ℝ) + q + 1) := by positivity
  linarith

/-! ## 3. Prefactor ratio identity and scale cancellation in binding ratios (`qou-2pnv`) -/

/-- **Exact algebraic identity for the `12.4347` prefactor ratio (`qou-2pnv`).**
The ratio of the deprecated volume-density prefactor `m_e / ℏ_q² = m_e / ((q - 1) / q)²`
to the canonical binding scale `E₀ = m_e / (q (q - 1))` equals `q³ / (q - 1)` identically
for every `q ≠ 0, 1` and `m_e ≠ 0`. -/
theorem deprecated_vs_canonical_prefactor_ratio {R : Type*} [Field R]
    (m_e q : R) (hm : m_e ≠ 0) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    (m_e / ((q - 1) / q) ^ 2) / (m_e / (q * (q - 1))) = q ^ 3 / (q - 1) := by
  field_simp
  ring

/-- **Identity `q³ / (q - 1) = 1 / (c_q² ℏ_q³)` (`qou-2pnv`).**
With `c_q = 1 / (q - 1)` and `ℏ_q = (q - 1) / q`, the prefactor ratio `q³ / (q - 1)`
equals `1 / (c_q² ℏ_q³)` identically. -/
theorem prefactor_ratio_eq_inv_cq_sq_hbar_cu {R : Type*} [Field R]
    (q : R) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    q ^ 3 / (q - 1) = 1 / ((1 / (q - 1)) ^ 2 * ((q - 1) / q) ^ 3) := by
  field_simp
  ring

/-- **Scale cancellation in binding-energy ratios (`qou-2pnv`).**
Any nonzero rescaling `E₀ ↦ c · E₀` of the overall energy scale cancels identically
in the ratio of two binding energies `((c · E₀) · b₁) / ((c · E₀) · b₂) = b₁ / b₂`. -/
theorem binding_ratio_scale_invariant {R : Type*} [Field R]
    (E₀ c b₁ b₂ : R) (hE : E₀ ≠ 0) (hc : c ≠ 0) :
    ((c * E₀) * b₁) / ((c * E₀) * b₂) = b₁ / b₂ := by
  have hcE : c * E₀ ≠ 0 := mul_ne_zero hc hE
  exact mul_div_mul_left b₁ b₂ hcE

end QOU.Hecke.BindingExtensivity
