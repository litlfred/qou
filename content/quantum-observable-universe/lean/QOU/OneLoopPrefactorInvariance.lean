/-
  Why the 1-loop FORM transports across normalisations and the CONSTANT does not.

  WHAT THIS IS FOR.  The `c_σ` arc carries a prefactor law

      c_σ  =  k · |τ|^p          with  p = −1/2  and  k = 2^{−1/2}

  and the corpus spent a long time unsure which half of that was assumed.  Two
  session-level findings settled it, and both are pure algebra that was argued
  in prose and in `mpmath`.  They are proved here so the argument stops being a
  numerical coincidence and starts being a fact.

  1. `exponent_normalisation_invariant` — rescaling `c ↦ A·c` by ANY positive
     constant leaves the two-point exponent unchanged.

     This is the precise reason the FORM survives a change of convention while
     the PREFACTOR does not.  Dimofte–Gukov–Lenells–Zagier (arXiv:0903.2472)
     carry at least three additive offsets between conventions — a `/2` in eq
     (2.3), a `+log 2` in eq (4.5) between `S₁` and the colored-Jones
     coefficient `s₁`, and a `log π` shift against Gukov–Murakami (fn 24) — and
     fix their integration constants against colored-Jones asymptotics.  Every
     one of those is an `A` in the statement below, so every one of them leaves
     `p` alone and moves `k`.  An earlier draft of the audit claimed DGLZ's `/2`
     simply IS this corpus's `k`; that was retracted, and this theorem is the
     reason the retraction was forced rather than merely prudent.

  2. `k_const_iff_exponent_neg_half` — for two manifolds,

         c₁·√τ₁ = c₂·√τ₂     ↔     p₁₂ = −1/2 .

     The corpus validated the law by checking that `k_c := c_σ·|τ|^{1/2}` is the
     same across manifolds, and recorded the exponent as ASSUMED.  The two
     statements are the same statement.  Every `k`-constancy check was already
     an exponent measurement, so `p = −1/2` was pinned to 17 digits by data the
     corpus already had and the assumption ledger named the wrong thing.

  3. `normalisation_step_trivial_of_k_agree` — if a missing `c`-dependent
     dictionary step `g` satisfies `k_meas c = k_true * g c`, then agreement of
     the measured `k` at two cusp numbers forces `g` to agree there too.

     Trivial as algebra, and that is the point: it is what licences reading the
     17-digit `k₁ = k₂` agreement as a BOUND on the missing normalisation step
     rather than as evidence for a particular value of `k`.

  SCOPE.  Nothing here is about torsion, Chern–Simons, or the volume
  conjecture.  These are statements about a two-parameter power law and the
  logarithm, stated over `ℝ`, and they carry no geometric content whatsoever.
  What they do is fix which half of the empirical work was load-bearing.

  -- Ref: [dimofte-gukov-lenells-zagier-2009] arXiv:0903.2472, eq (2.1)-(2.3), (4.5)
  -- Ref: [manuscript] docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt

namespace QOU.OneLoopPrefactorInvariance

open Real

/-- The two-point exponent of a power law through `(t₁, c₁)` and `(t₂, c₂)`:
the unique `p` with `cᵢ = k·tᵢ^p` for some `k`, read off in logarithms. -/
noncomputable def twoPointExponent (t₁ c₁ t₂ c₂ : ℝ) : ℝ :=
  (Real.log c₁ - Real.log c₂) / (Real.log t₁ - Real.log t₂)

/-- **The exponent is invariant under an overall rescaling of `c`.**

Rescaling `c ↦ A·c` is exactly what a change of normalisation convention does
to the observable, and it cancels in the numerator: `log (A·c₁) − log (A·c₂) =
log c₁ − log c₂`.  So a convention offset can move the prefactor `k` freely and
can never move `p`.  No positivity is needed on `t₁, t₂` — the denominator is
untouched. -/
theorem exponent_normalisation_invariant
    {t₁ t₂ c₁ c₂ A : ℝ} (hc₁ : c₁ ≠ 0) (hc₂ : c₂ ≠ 0) (hA : A ≠ 0) :
    twoPointExponent t₁ (A * c₁) t₂ (A * c₂) = twoPointExponent t₁ c₁ t₂ c₂ := by
  unfold twoPointExponent
  rw [Real.log_mul hA hc₁, Real.log_mul hA hc₂]
  ring_nf

/-- **`k`-constancy and `p = −1/2` are the same statement.**

The corpus checked that `k_c := c_σ·|τ|^{1/2}` agrees across manifolds and
listed the exponent as assumed.  Given two distinct positive `τ` values, the
agreement holds exactly when the two-point exponent is `−1/2`; the check was an
exponent measurement all along. -/
theorem k_const_iff_exponent_neg_half
    {t₁ t₂ c₁ c₂ : ℝ} (ht₁ : 0 < t₁) (ht₂ : 0 < t₂)
    (hc₁ : 0 < c₁) (hc₂ : 0 < c₂) (hlog : Real.log t₁ ≠ Real.log t₂) :
    c₁ * Real.sqrt t₁ = c₂ * Real.sqrt t₂ ↔
      twoPointExponent t₁ c₁ t₂ c₂ = -(1 / 2) := by
  have hsub : Real.log t₁ - Real.log t₂ ≠ 0 := sub_ne_zero.mpr hlog
  have hs₁ : Real.log (Real.sqrt t₁) = Real.log t₁ / 2 := Real.log_sqrt ht₁.le
  have hs₂ : Real.log (Real.sqrt t₂) = Real.log t₂ / 2 := Real.log_sqrt ht₂.le
  have hst₁ : (0:ℝ) < Real.sqrt t₁ := Real.sqrt_pos.mpr ht₁
  have hst₂ : (0:ℝ) < Real.sqrt t₂ := Real.sqrt_pos.mpr ht₂
  constructor
  · intro h
    -- take logarithms of the (positive) equal quantities
    have hlogeq : Real.log (c₁ * Real.sqrt t₁) = Real.log (c₂ * Real.sqrt t₂) := by
      rw [h]
    rw [Real.log_mul (ne_of_gt hc₁) (ne_of_gt hst₁),
        Real.log_mul (ne_of_gt hc₂) (ne_of_gt hst₂), hs₁, hs₂] at hlogeq
    unfold twoPointExponent
    field_simp
    linarith [hlogeq]
  · intro h
    unfold twoPointExponent at h
    have hnum : Real.log c₁ - Real.log c₂ = -(1 / 2) * (Real.log t₁ - Real.log t₂) := by
      field_simp at h
      linarith [h]
    -- rebuild the product equality from equal logarithms
    have hlogeq : Real.log (c₁ * Real.sqrt t₁) = Real.log (c₂ * Real.sqrt t₂) := by
      rw [Real.log_mul (ne_of_gt hc₁) (ne_of_gt hst₁),
          Real.log_mul (ne_of_gt hc₂) (ne_of_gt hst₂), hs₁, hs₂]
      linarith [hnum]
    have hp₁ : (0:ℝ) < c₁ * Real.sqrt t₁ := mul_pos hc₁ hst₁
    have hp₂ : (0:ℝ) < c₂ * Real.sqrt t₂ := mul_pos hc₂ hst₂
    exact Real.log_injOn_pos (Set.mem_Ioi.mpr hp₁) (Set.mem_Ioi.mpr hp₂) hlogeq

/-- **What a `k`-agreement bounds.**

If the measured constant differs from the true one by an unknown `c`-dependent
dictionary step, `k_meas c = k_true * g c` with `k_true ≠ 0`, then agreement of
the MEASURED constants at two cusp numbers forces the step to agree there.

This is what licences reading the 17-digit `k₁ = k₂` agreement as a constraint
on the missing normalisation — it excludes every candidate `g` with
`g 1 ≠ g 2`, which is how `2^{(c-1)/2}`, `2^{c-1}`, `c`, `√c` and `c^{1/4}` were
ruled out. -/
theorem normalisation_step_trivial_of_k_agree
    {k_meas g : ℕ → ℝ} {k_true : ℝ} (hk : k_true ≠ 0)
    (hfac : ∀ c, k_meas c = k_true * g c) {c₁ c₂ : ℕ}
    (hagree : k_meas c₁ = k_meas c₂) :
    g c₁ = g c₂ := by
  have h : k_true * g c₁ = k_true * g c₂ := by
    rw [← hfac c₁, ← hfac c₂]; exact hagree
  exact mul_left_cancel₀ hk h

/-! ### The van der Veen constant, and what the law turns it into

The three statements above are about the SHAPE of the law.  The two below are
about the specific constant the `c_σ` arc now carries.  Van der Veen's
asymptotic for a Whitehead chain `W_{a,1,c,d}`, once the signs in his Lemma 2a
and his Step-3 coefficient are corrected, gives in closed form

    c_σ  =  2^{1/2−n} (n² + m²)^{−1/4},    n := c+d,  m := 4a−c+d

written below as `√2 / (2ⁿ · √√(n²+m²))` to stay inside `Monoid.npow` and
`Real.sqrt`.  The corpus's law is `c_σ = k·|τ|^{−1/2}` with `k = 2^{−1/2}`, i.e.
`c_σ = √(1/(2τ))`.  `vdv_c_sigma_iff_tau` says those two statements together
pin `τ` to `2^{2n−2}√(n²+m²)` and nothing else.

That is what makes the pre-registered `τ_DG` predictions at `L8n5`, `L10n100`
and `L10n103` a CONSEQUENCE of the closed form rather than a second fit: given
the closed form and the law, the value of `τ` is forced, so computing it in
SnapPy is a genuine test that could have failed.

-- Ref: [vanderveen2008] arXiv:math/0611181, Lemma 1-4 and Main theorem
-- Ref: [manuscript] docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md
-/

/-- The corpus's 1-loop law in the form it is actually used: `c = √(1/(2τ))`. -/
noncomputable def vdvCSigma (n : ℕ) (m : ℝ) : ℝ :=
  Real.sqrt 2 / (2 ^ n * Real.sqrt (Real.sqrt ((n : ℝ) ^ 2 + m ^ 2)))

/-- **The law inverts.**  For positive `τ` and `c`, `c = √(1/(2τ))` and
`τ = 1/(2c²)` say the same thing.  Stated separately because it is the only
step in `vdv_c_sigma_iff_tau` that is about the law rather than the constant. -/
theorem law_inverts {t c : ℝ} (ht : 0 < t) (hc : 0 < c) :
    c = Real.sqrt (1 / (2 * t)) ↔ t = 1 / (2 * c ^ 2) := by
  have h2t : (0:ℝ) < 2 * t := by linarith
  constructor
  · intro h
    have hsq : c ^ 2 = 1 / (2 * t) := by
      rw [h]; exact Real.sq_sqrt (le_of_lt (by positivity))
    rw [hsq]
    field_simp
  · intro h
    have hc2 : (0:ℝ) < c ^ 2 := by positivity
    have : 1 / (2 * t) = c ^ 2 := by
      rw [h]; field_simp
    rw [this, Real.sqrt_sq hc.le]

/-- **The derived constant forces the torsion.**

`c_σ = 2^{1/2−n}(n²+m²)^{−1/4}` together with the law `c_σ = √(1/(2τ))` holds
exactly when `τ = 2^{2n−2}√(n²+m²)`, written here as `4ⁿ√(n²+m²)/4`. -/
theorem vdv_c_sigma_iff_tau {t : ℝ} (ht : 0 < t) (n : ℕ) (m : ℝ)
    (hnm : 0 < (n : ℝ) ^ 2 + m ^ 2) :
    vdvCSigma n m = Real.sqrt (1 / (2 * t)) ↔
      t = 4 ^ n * Real.sqrt ((n : ℝ) ^ 2 + m ^ 2) / 4 := by
  have hS : (0:ℝ) < Real.sqrt ((n : ℝ) ^ 2 + m ^ 2) := Real.sqrt_pos.mpr hnm
  have hSS : (0:ℝ) < Real.sqrt (Real.sqrt ((n : ℝ) ^ 2 + m ^ 2)) :=
    Real.sqrt_pos.mpr hS
  have hpow : (0:ℝ) < (2:ℝ) ^ n := by positivity
  have hc : 0 < vdvCSigma n m := by
    unfold vdvCSigma; positivity
  -- `(c_σ)² = 2 / (4ⁿ · √(n²+m²))`
  have hsq : vdvCSigma n m ^ 2 = 2 / (4 ^ n * Real.sqrt ((n : ℝ) ^ 2 + m ^ 2)) := by
    unfold vdvCSigma
    rw [div_pow, mul_pow, Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2),
        Real.sq_sqrt hS.le]
    congr 1
    rw [← pow_mul, mul_comm n 2, pow_mul]
    norm_num
  have hden : (4:ℝ) ^ n * Real.sqrt ((n : ℝ) ^ 2 + m ^ 2) ≠ 0 := by positivity
  have hval : 1 / (2 * (2 / (4 ^ n * Real.sqrt ((n : ℝ) ^ 2 + m ^ 2))))
      = 4 ^ n * Real.sqrt ((n : ℝ) ^ 2 + m ^ 2) / 4 := by
    field_simp
    norm_num
  rw [law_inverts ht hc, hsq, hval]

end QOU.OneLoopPrefactorInvariance
