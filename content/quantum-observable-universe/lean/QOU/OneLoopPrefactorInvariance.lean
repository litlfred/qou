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
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Data.Complex.Basic

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

/-! ### The `Σ(2,3,5)` keystone dimension tower is exact `φ`-algebra

Separate arc, same file because it is the same question asked on the other side
of the hyperbolic/Seifert divide. At `r = 5` the quantum dimensions are
`[1] = [4] = 1`, `[2] = [3] = φ`, `[5] = 0`, `[6] = −1`, and the corpus's
`Σ(2,3,5)` keystone (`lr_modulus_identification_sigma235.py`) builds a tower of
global dimensions on them. The ratios in that tower are **not** numerical
coincidences — they are forced by the affine `Ê₈` McKay marks, and that is what
is proved here.

`golden_quantum_dimension` grounds it: `[2] = 2cos(π/5) = φ`, from Mathlib's
`Real.cos_pi_div_five`, so the tower's input is a theorem rather than a table.

The payoff is that the cinquefoil — the `brings-surface` chapter's `ζ₅` carrier —
has `|V(T_{2,5})(ζ₁₀)|² = 1 + φ² = D²_Fib`, and hence sits exactly at the bottom
of that tower.

WHAT THIS DOES NOT SAY. This is *not* the `c_σ` law. `c_σ` is the asymptotic
constant of the colored Jones of a **cusped** complement with `Vol > 0`, power
`N^{3/2}`, growth `e^{Vol·N/2π}`; the keystone's `S_ℓ` is a flat-connection
amplitude in the WRT invariant of a **closed** manifold with `Vol = 0`, power
`√N`, exponential a pure phase. Both carry a forced constant, by different
mechanisms — `k = 2^{−1/2}` by the Gaussian saddle above, the keystone's `√2` by
the 2:1 fold `D²_{Ê₈} = 2 D²_MTC` proved below. They share `ℚ(√5)` by cyclotomy,
not by mechanism.

-- Ref: [hikami2005brieskorn] math-ph/0405028, library/arxiv-math-ph-0405028v2/0405028v2.pdf
-- Ref: [manuscript] computations/lr_modulus_identification_sigma235.py
-- Ref: [manuscript] computations/probes/bring_golden_jones_probe.py
-/

/-- Quantum dimensions at `r = 5`, on the affine `Ê₈` McKay marks. -/
noncomputable def qdim5 (φ : ℝ) : ℕ → ℝ
  | 1 => 1
  | 2 => φ
  | 3 => φ
  | 4 => 1
  | 5 => 0
  | 6 => -1
  | _ => 0

/-- **`[2] = 2cos(π/5) = φ`.**  The tower's input is a theorem, not a table. -/
theorem golden_quantum_dimension :
    2 * Real.cos (π / 5) = (1 + Real.sqrt 5) / 2 := by
  rw [Real.cos_pi_div_five]; ring

/-- **The keystone tower.**  `D²_{SU(2)₃} = 2 D²_Fib` and `D²_{Ê₈} = 4 D²_Fib`,
for every `φ` — the ratios come from the mark multiset, not from `√5`. -/
theorem keystone_dimension_tower (φ : ℝ) :
    (qdim5 φ 1 ^ 2 + qdim5 φ 2 ^ 2 + qdim5 φ 3 ^ 2 + qdim5 φ 4 ^ 2)
        = 2 * (1 + φ ^ 2)
      ∧ (([1, 2, 3, 4, 5, 6, 4, 2, 3] : List ℕ).map (fun m => qdim5 φ m ^ 2)).sum
        = 4 * (1 + φ ^ 2) := by
  constructor <;> · simp [qdim5]; ring

/-- **`Σ marks² = 120 = |2I|`** — the binary icosahedral group's order, and
`|S₅|`, and `|Aut(Bring)|`. -/
theorem marks_sq_sum_eq_120 :
    (([1, 2, 3, 4, 5, 6, 4, 2, 3] : List ℕ).map (fun m => m ^ 2)).sum = 120 := by
  decide

/-- The keystone's core `ℚ(√5)` identity, `(10 − 2√5)(10 + 2√5) = 80`. -/
theorem keystone_core_identity :
    (10 - 2 * Real.sqrt 5) * (10 + 2 * Real.sqrt 5) = 80 := by
  have h : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  nlinarith [h]

/-- **The cinquefoil sits at the bottom of the tower.**  With `φ² = φ + 1`, the
Bring `ζ₅` carrier's Jones value `2 + φ` is `1 + φ² = D²_Fib`. -/
theorem cinquefoil_value_is_fib_dimension {φ : ℝ} (hφ : φ ^ 2 = φ + 1) :
    1 + φ ^ 2 = 2 + φ := by rw [hφ]; ring

/-! ### `τ²` is an integer, and it is a Gaussian norm

The closed form `|τ_DG| = 2^{2n−2}√(n²+m²)` (`n = c+d`, `m = 4a−c+d`) squares to
something with no square root left in it:

    τ²  =  16^{n−1} · (n² + m²)

so **every `b = 1` Whitehead chain has integer `τ²`** — and `n² + m²` is exactly
`Complex.normSq (n − mi)`, the norm of a Gaussian integer. That is the arithmetic
content of the closed form, made formal: `τ_DG` lives in `Q(i)`, the trace field
of the regular ideal octahedron, and the radical is a norm rather than an
accident.

It is also what the twisted-framing test measured. Reframing the `a = 0`
complement by `μ − aλ` on one cusp gives, exactly,

    Whitehead  n=1, m=4a−1 :  τ² =  1 + (4a−1)²  =  2, 10, 26, 50, 82
    Borromean  n=2, m=4a   :  τ² = 64 (1 + 4a²)  =  64, 320, 320, 1088, 1088

on 25 framings with no mismatch — see `one_loop_twisted_framing_probe.py`. The
integrality below is why those came out as integers rather than as numerical
near-misses, and the `m²` is why the Borromean row is symmetric under `a ↦ −a`.

-- Ref: [vanderveen2008] arXiv:math/0611181
-- Ref: [manuscript] computations/probes/one_loop_twisted_framing_probe.py
-/

/-- **`τ² = 16^{n−1}(n² + m²)`** — no radical survives the squaring. -/
theorem vdv_tau_sq (n : ℕ) (hn : 1 ≤ n) (m : ℝ) :
    (4 ^ n * Real.sqrt ((n : ℝ) ^ 2 + m ^ 2) / 4) ^ 2
      = 16 ^ (n - 1) * ((n : ℝ) ^ 2 + m ^ 2) := by
  have hS : (0:ℝ) ≤ (n : ℝ) ^ 2 + m ^ 2 := by positivity
  have h16 : (16:ℝ) ^ n = 16 ^ (n - 1) * 16 := by
    conv_lhs => rw [← Nat.sub_add_cancel hn]
    rw [pow_succ]
  have h4 : ((4:ℝ) ^ n) ^ 2 = 16 ^ n := by
    rw [← pow_mul, mul_comm, pow_mul]; norm_num
  rw [div_pow, mul_pow, Real.sq_sqrt hS, h4, h16]
  ring

/-- **The radical is a Gaussian norm.**  `n² + m²` is `normSq (n − mi)`, so
`τ²` is `16^{n−1}` times the norm of an element of `ℤ[i]` — the ring of integers
of `ℚ(i)`, the trace field of the regular ideal octahedron. -/
theorem vdv_radical_is_gaussian_norm (n : ℕ) (m : ℝ) :
    Complex.normSq (⟨(n : ℝ), -m⟩ : ℂ) = (n : ℝ) ^ 2 + m ^ 2 := by
  simp [Complex.normSq_apply]; ring

/-! ### The saddle condition, and what it forces

The knot-side derivation runs Laplace's method on Kashaev's one-variable sum
`⟨4₁⟩_N = Σ_k |(q;q)_k|²`, whose logarithm expands as

    log g_k = −(2N/π)·Λ(θ) + log(2N sin θ) + O(1/N),      θ = kπ/N

with `Λ` the Lobachevsky function.  Three quantities come out of the saddle:

  * the SADDLE CONDITION `Λ'(θ) = −log(2 sin θ) = 0`, i.e. `2 sin θ* = 1`;
  * the STIRLING factor `2 sin θ*`, from the subleading term;
  * the HESSIAN `|Λ''(θ*)| = |cot θ*|`, from the Gaussian integral,

giving `c_σ = 2 sin θ* · |cot θ*|^{−1/2}` and `|τ_DG| = |cot θ*| / 2`.

WHAT IS AND IS NOT PROVED HERE.  The algebra downstream of the saddle is proved
here; the saddle itself still enters as hypotheses `hc` and `hτ`.  The two
analytic inputs those hypotheses stand for are now BOTH formalised elsewhere in
this corpus (bean `qou-mlgp`), so the reading "not formalised, Mathlib has no
usable form" — which this header carried until 2026-08-09 — is out of date:

  * the expansion, `QOU.Knot.FigureEightVolume.kashaev_log_sum_asymptotic`.
    With `kashaev_factor_eq_sin_sq` giving `log g_k = 2·∑_{j≤k} log(2 sin jπ/N)`,
    it says exactly the display above with the `O(1/N)` made explicit:
    `log g_k = −(2N/π)Λ(θ) + log(2N sin θ) + (π/6N)cot θ + O(1/N²)`;
  * Laplace's method for the sum,
    `QOU.MathlibExt.hasSum_gaussian_theta` and `…_tilt` — an EXACT Jacobi-theta
    identity for the Gaussian sum, so sum/integral `= 1 + O(e^{−π²/a})`.

WHAT IS STILL ASSUMED, as of 2026-08-09, is `hτ` ONLY.  `hc` is now DERIVED,
in `QOU.Knot.FigureEightVolume.cSigma_sq_mul_abs_cot`: the asymptotics produce
the constant in the shape `c_σ(θ) = (2 sin θ)·|cot θ|^{−1/2}` — Stirling factor
over square-rooted Hessian — and squaring that and multiplying by `|cot θ|` is
`hc`.  `cSigma_saddle_pow_four` and `k_sq_eq_half` below are re-proved there
with `hc` supplied rather than assumed, so the chain from the Kashaev sum to
`c_σ = 3^{−1/4}` no longer passes through an assumption.

The text here read "nobody has yet derived `hc` and `hτ`" until that date; that
was true when written and is now half out of date.  `hτ` remains open.

What is proved here is the algebra, which is where the whole surprise lives:

  * `saddle_forces_cot` — the saddle condition plus `θ ∈ (π/2, π)` pins
    `cot θ* = −√3`.  Nothing about `4₁` is used; one summation variable is the
    only input.
  * `c_sq_sqrt_three_of_saddle` and `c_pow_four_eq_third` — hence `c_σ⁴ = 1/3`.
    In one variable the saddle condition IS `2 sin θ* = 1`, so the Stirling
    factor is forced to `1` and `c_σ = 3^{−1/4}` with no freedom at all.
    `3^{−1/4}` is a property of "one summation variable", not of `4₁`.
  * `k_sq_eq_half_of_saddle` — the sharpest of the three, and the reason this
    section exists.  `k := c_σ·|τ|^{1/2}` satisfies `k² = 1/2` **using only the
    saddle condition**: the Hessian cancels between `c_σ` and `τ` before it is
    ever evaluated, so `k = 2^{−1/2}` never depended on `cot θ* = −√3`, on the
    trace field, or on which manifold this is.  The corpus calibrated `k` on
    `4₁` for a long time; it was forced by the shape of the saddle.

-- Ref: [manuscript] computations/probes/one_loop_c_sigma_tetrahedral_probe.py
-- Ref: [manuscript] docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md
-/

/-- **The saddle condition pins the cotangent.**  On `(π/2, π)`, the only
solution of `2 sin θ = 1` has `cot θ = −√3`. -/
theorem saddle_forces_cot {θ : ℝ} (hθ : θ ∈ Set.Ioo (π / 2) π)
    (hsad : 2 * Real.sin θ = 1) :
    Real.cos θ / Real.sin θ = -Real.sqrt 3 := by
  have hs : Real.sin θ = 1 / 2 := by linarith
  have hcneg : Real.cos θ < 0 :=
    Real.cos_neg_of_pi_div_two_lt_of_lt hθ.1 (by linarith [hθ.2, Real.pi_pos])
  have hpy : Real.sin θ ^ 2 + Real.cos θ ^ 2 = 1 := Real.sin_sq_add_cos_sq θ
  have hsq : Real.cos θ ^ 2 = 3 / 4 := by rw [hs] at hpy; nlinarith [hpy]
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hpos : 0 < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hfac : (2 * Real.cos θ - Real.sqrt 3) * (2 * Real.cos θ + Real.sqrt 3) = 0 := by
    nlinarith [hsq, h3]
  have hne : 2 * Real.cos θ - Real.sqrt 3 ≠ 0 := by nlinarith [hcneg, hpos]
  have hzero : 2 * Real.cos θ + Real.sqrt 3 = 0 := by
    rcases mul_eq_zero.mp hfac with h | h
    · exact absurd h hne
    · exact h
  have hcos : Real.cos θ = -(Real.sqrt 3 / 2) := by linarith
  rw [hcos, hs]; ring

/-- `c_σ² · √3 = 1`, from the saddle. -/
theorem c_sq_sqrt_three_of_saddle {θ c : ℝ} (hθ : θ ∈ Set.Ioo (π / 2) π)
    (hsad : 2 * Real.sin θ = 1)
    (hc : c ^ 2 * |Real.cos θ / Real.sin θ| = (2 * Real.sin θ) ^ 2) :
    c ^ 2 * Real.sqrt 3 = 1 := by
  rw [saddle_forces_cot hθ hsad, abs_neg, abs_of_nonneg (Real.sqrt_nonneg 3),
      hsad] at hc
  linarith [hc]

/-- **`c_σ = 3^{−1/4}`, with no freedom.**  Stated as `c_σ⁴ = 1/3` to stay
inside `npow`. -/
theorem c_pow_four_eq_third {θ c : ℝ} (hθ : θ ∈ Set.Ioo (π / 2) π)
    (hsad : 2 * Real.sin θ = 1)
    (hc : c ^ 2 * |Real.cos θ / Real.sin θ| = (2 * Real.sin θ) ^ 2) :
    c ^ 4 = 1 / 3 := by
  have h := c_sq_sqrt_three_of_saddle hθ hsad hc
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  nlinarith [h, h3]

/-- **`k = 2^{−1/2}` is forced by the saddle condition alone.**

`c_σ = 2 sin θ*·|cot θ*|^{−1/2}` and `|τ| = |cot θ*|/2`, so in `k := c_σ·√|τ|`
the Hessian cancels *before it is evaluated*.  No `θ ∈ (π/2, π)`, no `cot θ* =
−√3`, no trace field, no manifold — only `2 sin θ* = 1`.

This is why the `4₁` calibration was never carrying information. -/
theorem k_sq_eq_half_of_saddle {θ c k : ℝ} (hsad : 2 * Real.sin θ = 1)
    (hc : c ^ 2 * |Real.cos θ / Real.sin θ| = (2 * Real.sin θ) ^ 2)
    (hk : k = c * Real.sqrt (|Real.cos θ / Real.sin θ| / 2)) :
    k ^ 2 = 1 / 2 := by
  have hnn : (0:ℝ) ≤ |Real.cos θ / Real.sin θ| / 2 := by positivity
  rw [hk, mul_pow, Real.sq_sqrt hnn]
  have hsplit : c ^ 2 * (|Real.cos θ / Real.sin θ| / 2)
      = c ^ 2 * |Real.cos θ / Real.sin θ| / 2 := by ring
  rw [hsplit, hc, hsad]
  norm_num

end QOU.OneLoopPrefactorInvariance
