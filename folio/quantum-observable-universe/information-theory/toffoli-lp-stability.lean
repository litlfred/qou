/-
  The golden-ratio threshold and the convention-C Toffoli diagonal.

  SCOPE CORRECTED 2026-08-30 (bean qou-3j5m).  This file used to be
  titled "LP-dual stability of the q-Toffoli braid" and to state that
  the q-Toffoli diagonal numerator is P₇₇(q) = q + q^(1/2) - 1, whose
  zero q⋆ = 1/φ² = (3 - √5)/2 is the stability threshold.  That
  numerator belongs to the EXCISED convention C (z_C = √q/(q+1)).
  Under the canonical convention D (z_D = q³/(q²+1)) the diagonal is

      P₇₇(q) = q³(q⁴+1)/(q²+1)²,

  strictly positive on q > 0 with NO positive zero — so the golden
  threshold is a property of the excised frame, not of the gate, and
  LP-stability is not equivalent to the positivity below.  See
  folio/quantum-observable-universe/information-theory/
  toffoli-lp-stability.md items 1-2 and the derivation probe
  computations/probes/toffoli_trio_rederivation.py.

  What survives, and is what this file actually proves, is the real
  analysis:      q > q⋆   ↔   q + √q - 1 > 0.
  It is a true and self-contained fact about f(q) = q + √q - 1; only
  the identification of f with a live Toffoli amplitude is withdrawn.

  Proof structure:
    1. Golden-ratio identity: (√5 - 1)/2 squared equals q⋆, so
       √q⋆ = (√5 - 1)/2 and q⋆ + √q⋆ - 1 = 0.
    2. Monotonicity: f(q) := q + √q - 1 is strictly increasing on
       [0, ∞) since both q ↦ q and q ↦ √q are monotone.
    3. Combine: f(q) > 0 ↔ q > q⋆ (via strict monotonicity and
       evaluation at q⋆).
    4. For q ≤ 0, Real.sqrt returns 0, so f(q) = q - 1 ≤ -1 < 0,
       and q⋆ > 0 > q, so both sides false.

**Ground ring**: R_q = ℤ[q, q⁻¹]. Under convention D the diagonal
numerator is q³(q⁴+1) = q⁷ + q³, an honest element of R_q — no
q^(1/2) and hence no extension is needed. The convention-C numerator
q + q^(1/2) - 1 was what required R_q[q^(1/2)].
-/
import QOU.QuantumObservableUniverse
import QOU.GroundRingCore
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt

namespace QOU.Information

noncomputable section

/-- The Toffoli diagonal numerator in the base ring `R_q`, under the
    canonical convention D: `P₇₇(q) = q³(q⁴+1)/(q²+1)²` has numerator
    `q³(q⁴+1) = q⁷ + q³`.  This is exact, not a stub — the convention-D
    diagonal is a Laurent polynomial over a positive denominator, so
    unlike its convention-C predecessor `q + q^(1/2) - 1` it needs no
    square-root extension of `R_q`. -/
def toffoli_diag_numerator : QOU.GroundRing.R_q :=
  QOU.GroundRing.q_param ^ 7 + QOU.GroundRing.q_param ^ 3

/-- The golden ratio `φ = (1 + √5) / 2`. -/
noncomputable def phi_golden : ℝ := (1 + Real.sqrt 5) / 2

/-- The golden-ratio threshold `q⋆ = (3 - √5) / 2 = 1 / φ²`. -/
noncomputable def q_star_threshold : ℝ := (3 - Real.sqrt 5) / 2

/-- **Golden-ratio threshold identity.** `q⋆ · φ² = 1`.
    Closed-form identity underpinning `prop:toffoli-lp-stability`. -/
theorem q_star_golden_square :
    q_star_threshold * phi_golden ^ 2 = 1 := by
  unfold q_star_threshold phi_golden
  have h5 : Real.sqrt 5 * Real.sqrt 5 = 5 :=
    Real.mul_self_sqrt (by norm_num : (0 : ℝ) ≤ 5)
  nlinarith [h5, Real.sqrt_nonneg 5]

/-- `0 < q⋆`: the golden-ratio threshold is strictly positive. -/
theorem q_star_pos : 0 < q_star_threshold := by
  unfold q_star_threshold
  have h5_lt_9 : Real.sqrt 5 < 3 := by
    have h : Real.sqrt 5 < Real.sqrt 9 := by
      apply Real.sqrt_lt_sqrt <;> norm_num
    simpa [show Real.sqrt 9 = 3 from by
      rw [show (9 : ℝ) = 3 ^ 2 from by norm_num, Real.sqrt_sq (by norm_num : (0 : ℝ) ≤ 3)]] using h
  linarith

/-- `√q⋆ = (√5 - 1) / 2`.  Equivalently, `q⋆ = ((√5 - 1)/2)²`. -/
theorem sqrt_q_star :
    Real.sqrt q_star_threshold = (Real.sqrt 5 - 1) / 2 := by
  have h5_ge_1 : (1 : ℝ) ≤ Real.sqrt 5 := by
    have : Real.sqrt 1 ≤ Real.sqrt 5 := Real.sqrt_le_sqrt (by norm_num)
    simpa [Real.sqrt_one] using this
  have h_nn : 0 ≤ (Real.sqrt 5 - 1) / 2 := by linarith
  have h_sq : ((Real.sqrt 5 - 1) / 2) ^ 2 = q_star_threshold := by
    unfold q_star_threshold
    have h5 : Real.sqrt 5 * Real.sqrt 5 = 5 :=
      Real.mul_self_sqrt (by norm_num : (0 : ℝ) ≤ 5)
    nlinarith [h5]
  calc Real.sqrt q_star_threshold
      = Real.sqrt (((Real.sqrt 5 - 1) / 2) ^ 2) := by rw [h_sq]
    _ = (Real.sqrt 5 - 1) / 2 := Real.sqrt_sq h_nn

/-- **Value at the threshold**: `q⋆ + √q⋆ - 1 = 0`. -/
theorem f_at_q_star :
    q_star_threshold + Real.sqrt q_star_threshold - 1 = 0 := by
  rw [sqrt_q_star]
  unfold q_star_threshold
  ring

/-- **Monotonicity of `f(q) = q + √q - 1` on `[0, ∞)`.** Strict. -/
theorem f_strict_mono {a b : ℝ} (ha : 0 ≤ a) (hab : a < b) :
    a + Real.sqrt a - 1 < b + Real.sqrt b - 1 := by
  have hsqrt_le : Real.sqrt a ≤ Real.sqrt b :=
    Real.sqrt_le_sqrt (le_of_lt hab)
  linarith

/-- **The golden-ratio threshold of `f(q) = q + √q - 1`.**
    `f` is positive exactly above q⋆ = (3 - √5) / 2 = 1 / φ².

    SCOPE (2026-08-30): this is a statement about the real function `f`
    and nothing else.  `f` is the numerator of the **convention-C**
    Toffoli diagonal, which is excised; the canonical convention-D
    diagonal `q³(q⁴+1)/(q²+1)²` is positive for every `q > 0` and has
    no threshold.  So this theorem no longer establishes LP-stability
    of the q-Toffoli, and must not be cited for it — see the file
    header.  The proof below is unchanged and remains correct.
    Label: prop:toffoli-lp-stability
    Ref: [leitner2026] Chapter 8, prop:toffoli-transfer-matrix
    Ref: [leitner2026] Chapter 4, prop:lp-dual-stability -/
theorem toffoli_lp_stable (q : ℝ) :
    q_star_threshold < q ↔ 0 < q + Real.sqrt q - 1 := by
  constructor
  · -- Forward: q > q⋆ ⇒ f(q) > 0.
    intro hq
    have hqstar_nn : 0 ≤ q_star_threshold := le_of_lt q_star_pos
    have := f_strict_mono hqstar_nn hq
    linarith [f_at_q_star]
  · -- Reverse: f(q) > 0 ⇒ q > q⋆. Contrapositive on q ≤ q⋆.
    intro hf
    by_contra hle
    push_neg at hle
    rcases lt_or_eq_of_le hle with hlt | heq
    · -- q < q⋆.
      by_cases hq_nn : 0 ≤ q
      · have := f_strict_mono hq_nn hlt
        linarith [f_at_q_star]
      · -- q < 0: √q = 0 by Real.sqrt convention.
        push_neg at hq_nn
        have hsqrt_zero : Real.sqrt q = 0 :=
          Real.sqrt_eq_zero'.mpr (le_of_lt hq_nn)
        rw [hsqrt_zero] at hf
        linarith
    · -- q = q⋆: f = 0, contradicts hf.
      rw [heq] at hf
      linarith [f_at_q_star]

/-  REMOVED 2026-08-30 (bean qou-3j5m): `toffoli_shadow_bounded`.

    It read `∃ κ : ℝ, 0 < κ ∧ κ < 10`, discharged by `⟨303/100, …⟩`.
    Two independent reasons it had to go.

    (1) It was vacuous in the sense of AGENTS.md §"No trivial trues":
        the statement mentions no Toffoli, no Gram matrix and no q, so
        it is provable without any hypothesis about the objects it
        claims to be about.  Exhibiting 3.03 proves that 3.03 lies in
        (0, 10), nothing more.

    (2) The number itself is withdrawn.  κ(G(q₀)) ≈ 3.03 came from a
        Gram matrix built with the retracted naive length rule
        tr_M(T_w) = z^ℓ(w) under the excised convention C, in float64,
        at a superseded q₀; under convention D the Markov–Gram form is
        singular, so λ_max/|λ_min| is not a condition number at all.
        The content block withdrew the figure on 2026-08-09
        (toffoli-lp-stability.md item 3); this file kept it.

    There is nothing to restate here: a real shadow-price bound needs
    the radical-quotient ruling first.
-/

/-!
## The flip amplitude and the LP cone coordinate carry opposite signs

Settles the open item of bean `qou-0pnj`.  `prop:toffoli-lp-stability`'s proof
reduces feasibility of `G·t ≥ 0` to "the positivity of `P₇₇ · W_std` with the
appropriate sign from" the flip amplitude.  The two quantities that step
relates carry **exactly opposite** signs of the same factor `ħ = q - q⁻¹`,
identically in `q` — so the reduction cannot inherit the amplitude's sign.

* the derived flip amplitude is `P₇₆ = -(q-1)(q+1)·S / (2q(q²+1)²)`,
* the q-Toffoli, all-proton ordering, is `T_q = σ₁ + ħ·σ₀σ₁`, so its NF
  coordinate on the word `(0,1)` is `+ħ`.

Since `ħ = (q-1)(q+1)/q`, the amplitude is `-ħ` times a strictly positive
cofactor, giving `P₇₆ · ħ ≤ 0` on `q > 0`.  Scope (b): this excludes any
reduction in which the cone condition inherits the amplitude's sign.  It does
**not** exclude one carrying a negative proportionality.

Symbolic cross-check: `computations/probes/toffoli_sign_inversion_is_structural.py`, 7/7.
-/

/-- The sextic cofactor `S(q) = q⁶ + q⁴ + 2q² + 1`. -/
noncomputable def toffoliSextic (q : ℝ) : ℝ := q ^ 6 + q ^ 4 + 2 * q ^ 2 + 1

/-- The derived convention-D target-flip amplitude `P₇₆`. -/
noncomputable def toffoliFlipAmplitude (q : ℝ) : ℝ :=
  -((q - 1) * (q + 1) * toffoliSextic q) / (2 * q * (q ^ 2 + 1) ^ 2)

/-- The NF coordinate of `T_q` on the word `(0,1)`, namely `ħ = q - q⁻¹`. -/
noncomputable def toffoliConeCoord (q : ℝ) : ℝ := q - 1 / q

/-- `S(q) > 0` for every real `q`: every exponent is even, every coefficient
    positive, and the constant term is `1`. -/
theorem toffoliSextic_pos (q : ℝ) : 0 < toffoliSextic q := by
  unfold toffoliSextic; positivity

/-- **The factorisation.** `P₇₆ = -ħ · S / (2(q²+1)²)`. -/
theorem toffoliFlipAmplitude_eq (q : ℝ) (hq : q ≠ 0) :
    toffoliFlipAmplitude q
      = -(toffoliConeCoord q) * (toffoliSextic q / (2 * (q ^ 2 + 1) ^ 2)) := by
  unfold toffoliFlipAmplitude toffoliConeCoord
  have h1 : (q ^ 2 + 1) ≠ 0 := by positivity
  field_simp
  ring

/-- **Opposite signs, identically.** On `q > 0` the flip amplitude and the LP
    cone coordinate never share a sign: their product is non-positive.  This is
    the invariant that excludes a sign-inheriting reduction. -/
theorem toffoliFlip_mul_coneCoord_nonpos (q : ℝ) (hq : 0 < q) :
    toffoliFlipAmplitude q * toffoliConeCoord q ≤ 0 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  rw [toffoliFlipAmplitude_eq q hq0]
  have hS : 0 < toffoliSextic q / (2 * (q ^ 2 + 1) ^ 2) := by
    have := toffoliSextic_pos q
    positivity
  nlinarith [sq_nonneg (toffoliConeCoord q), hS,
             mul_nonneg (le_of_lt hS) (sq_nonneg (toffoliConeCoord q))]

/-!
## Every sign and zero claim of the convention-D Toffoli arc, proved

The blocks of this arc assert a family of sign and zero facts about the four
derived convention-D amplitudes.  Each is discharged below, so nothing in the
arc rests on a numerical evaluation at a single anchor.

| claim | theorem |
|---|---|
| `P₇₇` strictly positive on `q > 0`, no positive root | `toffoliDiagonal_pos` |
| `P₆₆` strictly positive on `q > 0` | `toffoliP66_pos` |
| `P₇₆`'s only positive zero is `q = 1` | `toffoliFlip_eq_zero_iff` |
| `P₇₆ < 0` on `q > 1` (the substrate side) | `toffoliFlip_neg_of_one_lt` |
| `P₇₆ > 0` on `0 < q < 1` | `toffoliFlip_pos_of_lt_one` |
| the flip channel is **not** antisymmetric | `toffoli_not_antisymmetric` |
| `W_std > 0`, and `P₇₇·W_std > 0` | `wStd_pos`, `toffoliDiagonal_mul_wStd_pos` |

Symbolic cross-check of the same seven:
`computations/probes/toffoli_amplitude_sign_claims.py`.
-/

/-- The convention-D diagonal `P₇₇ = q³(q⁴+1)/(q²+1)²`. -/
noncomputable def toffoliDiagonal (q : ℝ) : ℝ :=
  q ^ 3 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- The convention-D even-channel diagonal `P₆₆`. -/
noncomputable def toffoliP66 (q : ℝ) : ℝ :=
  (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 2) / (4 * q * (q ^ 2 + 1) ^ 2)

/-- The convention-D reverse-flip amplitude `P₆₇`. -/
noncomputable def toffoliReverseFlip (q : ℝ) : ℝ :=
  (q - 1) * (q + 1) * (2 * q ^ 6 + q ^ 4 + q ^ 2 + 1) / (2 * q * (q ^ 2 + 1) ^ 2)

/-- The Wedderburn weight of the 2-dimensional standard representation. -/
noncomputable def wStd (q : ℝ) : ℝ := (q ^ 2 + 1) ^ 2 / (q ^ 4 + 4 * q ^ 2 + 1)

/-- **`P₇₇` has no positive root.** Strictly positive for every `q > 0`, so the
    golden-ratio threshold `q⋆` of the excised convention C has no analogue. -/
theorem toffoliDiagonal_pos {q : ℝ} (hq : 0 < q) : 0 < toffoliDiagonal q := by
  unfold toffoliDiagonal; positivity

/-- **`P₆₆` is strictly positive** for every `q > 0`. -/
theorem toffoliP66_pos {q : ℝ} (hq : 0 < q) : 0 < toffoliP66 q := by
  unfold toffoliP66; positivity

/-- The cone coordinate `ħ = q - q⁻¹` is positive exactly above `1`. -/
theorem toffoliConeCoord_pos_iff {q : ℝ} (hq : 0 < q) :
    0 < toffoliConeCoord q ↔ 1 < q := by
  unfold toffoliConeCoord
  rw [sub_pos]
  have hinv : 0 < 1 / q := by positivity
  constructor
  · intro h
    -- multiply `1/q < q` through by `q > 0`
    have h2 := mul_lt_mul_of_pos_right h hq
    rw [one_div, inv_mul_cancel₀ (ne_of_gt hq)] at h2
    nlinarith
  · intro h
    -- multiply `1 < q*q` through by `1/q > 0`
    have h1 : (1 : ℝ) < q * q := by nlinarith
    have h2 := mul_lt_mul_of_pos_left h1 hinv
    rw [mul_one] at h2
    calc 1 / q < 1 / q * (q * q) := h2
      _ = q := by field_simp

/-- `ħ = 0` exactly at `q = 1`, on `q > 0`. -/
theorem toffoliConeCoord_eq_zero_iff {q : ℝ} (hq : 0 < q) :
    toffoliConeCoord q = 0 ↔ q = 1 := by
  unfold toffoliConeCoord
  rw [sub_eq_zero, eq_div_iff (ne_of_gt hq)]
  constructor
  · intro h; nlinarith
  · intro h; rw [h]; ring

/-- **The only positive zero of `P₇₆` is `q = 1`** — the classical limit. -/
theorem toffoliFlip_eq_zero_iff {q : ℝ} (hq : 0 < q) :
    toffoliFlipAmplitude q = 0 ↔ q = 1 := by
  rw [toffoliFlipAmplitude_eq q (ne_of_gt hq)]
  have hC : 0 < toffoliSextic q / (2 * (q ^ 2 + 1) ^ 2) := by
    have := toffoliSextic_pos q; positivity
  rw [← toffoliConeCoord_eq_zero_iff hq]
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | h2
    · linarith [neg_eq_zero.mp h1]
    · exact absurd h2 (ne_of_gt hC)
  · intro h; rw [h]; ring

/-- **`P₇₆ < 0` on `q > 1`** — including the substrate anchor. -/
theorem toffoliFlip_neg_of_one_lt {q : ℝ} (hq : 1 < q) :
    toffoliFlipAmplitude q < 0 := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  rw [toffoliFlipAmplitude_eq q (ne_of_gt hq0)]
  have hC : 0 < toffoliSextic q / (2 * (q ^ 2 + 1) ^ 2) := by
    have := toffoliSextic_pos q; positivity
  have hh : 0 < toffoliConeCoord q := (toffoliConeCoord_pos_iff hq0).mpr hq
  nlinarith

/-- **`P₇₆ > 0` on `0 < q < 1`.** The sign structure is the mirror of the
    amplitude's, which is what makes the excised convention's regime wrong. -/
theorem toffoliFlip_pos_of_lt_one {q : ℝ} (h0 : 0 < q) (h1 : q < 1) :
    0 < toffoliFlipAmplitude q := by
  rw [toffoliFlipAmplitude_eq q (ne_of_gt h0)]
  have hC : 0 < toffoliSextic q / (2 * (q ^ 2 + 1) ^ 2) := by
    have := toffoliSextic_pos q; positivity
  have hh : toffoliConeCoord q < 0 := by
    by_contra hcon
    push_neg at hcon
    rcases lt_or_eq_of_le hcon with h | h
    · exact absurd ((toffoliConeCoord_pos_iff h0).mp h) (not_lt.mpr (le_of_lt h1))
    · exact absurd ((toffoliConeCoord_eq_zero_iff h0).mp h.symm) (ne_of_lt h1)
  nlinarith

/-- **The antisymmetry defect, exactly.** `P₆₇ + P₇₆ = q(q-1)²(q+1)²/(2(q²+1))`,
    which is `0` only at `q = 1`. -/
theorem toffoli_antisymmetry_defect {q : ℝ} (hq : 0 < q) :
    toffoliReverseFlip q + toffoliFlipAmplitude q
      = q * (q - 1) ^ 2 * (q + 1) ^ 2 / (2 * (q ^ 2 + 1)) := by
  unfold toffoliReverseFlip toffoliFlipAmplitude toffoliSextic
  have h1 : (q ^ 2 + 1) ≠ 0 := by positivity
  field_simp
  ring

/-- **The flip channel is not antisymmetric.** `P₆₇ ≠ -P₇₆` for every `q > 0`
    other than the classical limit, so "reversing the crossing negates it" is
    false — and it fails in convention C and D alike. -/
theorem toffoli_not_antisymmetric {q : ℝ} (hq : 0 < q) (h1 : q ≠ 1) :
    toffoliReverseFlip q ≠ -toffoliFlipAmplitude q := by
  intro hcon
  have hsum : toffoliReverseFlip q + toffoliFlipAmplitude q = 0 := by
    rw [hcon]; ring
  rw [toffoli_antisymmetry_defect hq] at hsum
  have hne : q - 1 ≠ 0 := sub_ne_zero.mpr h1
  have hpos : 0 < q * (q - 1) ^ 2 * (q + 1) ^ 2 / (2 * (q ^ 2 + 1)) := by
    have h2 : 0 < (q - 1) ^ 2 := by positivity
    positivity
  exact absurd hsum (ne_of_gt hpos)

/-- **`W_std > 0`** for every `q > 0`: the denominator has no real root. -/
theorem wStd_pos {q : ℝ} (hq : 0 < q) : 0 < wStd q := by
  unfold wStd; positivity

/-- **The surviving half of the LP reduction.** `P₇₇ · W_std > 0` on `q > 0`,
    so the first factor of the proof's reduction never obstructs feasibility;
    everything at issue sits in the off-diagonal sign. -/
theorem toffoliDiagonal_mul_wStd_pos {q : ℝ} (hq : 0 < q) :
    0 < toffoliDiagonal q * wStd q :=
  mul_pos (toffoliDiagonal_pos hq) (wStd_pos hq)

/-!
## The recorded "product of traced volumes" IS the trace of the element

Retracts a hazard raised in bean `qou-ahu3`.  The construction computes
`markov_trace(ordering)` as `∏ᵢ V̂ᵢ` — a *product of traces* — and `tr_M` is
not multiplicative in general, since `σ₀` and `σ₁` do not commute.  That looked
like it might be the arc's real defect.  It is not: the factorisation follows
from the **defining Markov property** `tr(x·σ_last) = z·tr(x)` alone, with no
convention, no anchor, and no extra assumption.

For the chain elements `x = a σ₀ + b` and `y = c σ₁ + d`,

    tr(x·y) = ac·tr(σ₀σ₁) + ad·tr(σ₀) + bc·tr(σ₁) + bd·tr(1)
            = ac z² + ad z + bc z + bd            [Markov, twice]
            = (za + b)(zc + d)  =  V̂₀ · V̂₁ .

Verified symbolically for all eight strand-type orderings, in `q` **and** `z`
simultaneously, in `computations/probes/toffoli_markov_factorisation.py`; the
word `(0,1,0)` never occurs in any `T_q`, so no unproven trace value enters.
-/

/-- **The traced-volume factorisation is the Markov property.**  Given only
    `tr(1) = 1` and the Markov rule `tr(x·σ_last) = z·tr(x)`, the trace of the
    chain product equals the product of the traced volumes.  Stated with the
    trace values as hypotheses, so it is a theorem about the Markov property
    rather than about any particular convention or anchor. -/
theorem tracedVolume_product_eq_trace_of_markov
    (z a b c d trOne trS0 trS1 trS0S1 : ℝ)
    (hone : trOne = 1)
    (hs0 : trS0 = z * trOne)
    (hs1 : trS1 = z * trOne)
    (hs01 : trS0S1 = z * trS0) :
    a * c * trS0S1 + a * d * trS0 + b * c * trS1 + b * d * trOne
      = (z * a + b) * (z * c + d) := by
  subst hone; subst hs0; subst hs1; subst hs01; ring

/-!
## The LP cone condition's own threshold, and why it is not the amplitude's

The cone condition `G·t ≥ 0` for the q-Toffoli reduces to a **single**
inequality: of the six components, five are strictly positive throughout and
only the one indexed by the longest word `σ₀σ₁σ₀` changes sign.  With the
symbolic Gram (validated against `pyhecke.gram.gram_matrix_mp` at five values
of `q`) that component is

    (G·t)₅  =  (q¹⁰ + q⁶ - q⁴ + q² - 1) / (q²+1)²

whose numerator is irreducible over `ℚ` and has exactly one positive real root,
`q_c ≈ 0.8944802929106147637790049841733`.

**The point of the theorems below.** `q_c < 1` strictly, while the flip
amplitude `P₇₆` vanishes exactly at `q = 1`.  The cone condition and the
amplitude therefore have *different* thresholds, which refutes the last
surviving form of the proof's reduction — the sign-inheriting form was already
excluded by `toffoliFlip_mul_coneCoord_nonpos`, and a negative proportionality
would require the thresholds to coincide.  They do not.

Substituting `u = q²` turns the numerator into `u⁵ + u³ - u² + u - 1`, whose
strict monotonicity on `u ≥ 0` is elementary because `3u² - 2u + 1` has
negative discriminant.

Probe: `computations/probes/toffoli_cone_threshold.py`.
-/

/-- The cone constraint's numerator after the substitution `u = q²`. -/
noncomputable def coneRow5Poly (u : ℝ) : ℝ := u ^ 5 + u ^ 3 - u ^ 2 + u - 1

/-- The numerator of `(G·t)₅`, the one constraint that governs the cone. -/
noncomputable def coneRow5Numerator (q : ℝ) : ℝ :=
  q ^ 10 + q ^ 6 - q ^ 4 + q ^ 2 - 1

/-- The substitution `u = q²`. -/
theorem coneRow5Numerator_eq (q : ℝ) :
    coneRow5Numerator q = coneRow5Poly (q ^ 2) := by
  unfold coneRow5Numerator coneRow5Poly; ring

/-- `3u² - 2u + 1 > 0` for every real `u` — negative discriminant. -/
theorem quad_pos (u : ℝ) : 0 < 3 * u ^ 2 - 2 * u + 1 := by nlinarith [sq_nonneg (3 * u - 1)]

/-- `coneRow5Poly` is strictly increasing on `u ≥ 0`. -/
theorem coneRow5Poly_strictMono {a b : ℝ} (ha : 0 ≤ a) (hab : a < b) :
    coneRow5Poly a < coneRow5Poly b := by
  unfold coneRow5Poly
  have hb : 0 < b := lt_of_le_of_lt ha hab
  have hd : 0 < b - a := sub_pos.mpr hab
  -- a² + ab + b² - a - b + 1 = ½[(a-1)² + (b-1)² + (a+b)²] > 0
  have hquad : 0 < a ^ 2 + a * b + b ^ 2 - a - b + 1 := by
    nlinarith [sq_nonneg (a - 1), sq_nonneg (b - 1), sq_nonneg (a + b)]
  have hquart : 0 ≤ b ^ 4 + b ^ 3 * a + b ^ 2 * a ^ 2 + b * a ^ 3 + a ^ 4 := by
    have hb' : (0 : ℝ) ≤ b := le_of_lt hb
    nlinarith [pow_nonneg ha 4, pow_nonneg hb' 4, mul_nonneg (pow_nonneg hb' 3) ha,
               mul_nonneg (pow_nonneg hb' 2) (pow_nonneg ha 2),
               mul_nonneg hb' (pow_nonneg ha 3)]
  have hbr : 0 < (b ^ 4 + b ^ 3 * a + b ^ 2 * a ^ 2 + b * a ^ 3 + a ^ 4)
      + (a ^ 2 + a * b + b ^ 2 - a - b + 1) := by linarith
  have key : (b ^ 5 + b ^ 3 - b ^ 2 + b - 1) - (a ^ 5 + a ^ 3 - a ^ 2 + a - 1)
      = (b - a) * ((b ^ 4 + b ^ 3 * a + b ^ 2 * a ^ 2 + b * a ^ 3 + a ^ 4)
        + (a ^ 2 + a * b + b ^ 2 - a - b + 1)) := by ring
  have hpos : 0 < (b ^ 5 + b ^ 3 - b ^ 2 + b - 1) - (a ^ 5 + a ^ 3 - a ^ 2 + a - 1) := by
    rw [key]; exact mul_pos hd hbr
  linarith

/-- **The cone constraint is strictly satisfied at the classical limit.**
    `(G·t)₅`'s numerator equals `1` at `q = 1`. -/
theorem coneRow5Numerator_one : coneRow5Numerator 1 = 1 := by
  unfold coneRow5Numerator; norm_num

/-- The constraint is violated at `q = 1/2`, so a threshold exists below `1`. -/
theorem coneRow5Numerator_half_neg : coneRow5Numerator (1 / 2) < 0 := by
  unfold coneRow5Numerator; norm_num

/-- **The cone threshold is strictly below the amplitude's.**  At `q = 1` the
    flip amplitude vanishes while the cone constraint is strictly positive, so
    the two do not change sign at the same place.  This refutes the negative-
    proportionality reduction, which would require them to coincide; together
    with `toffoliFlip_mul_coneCoord_nonpos` (which excludes the sign-inheriting
    form) the proof's reduction has no surviving form. -/
theorem cone_threshold_ne_amplitude_threshold :
    toffoliFlipAmplitude 1 = 0 ∧ 0 < coneRow5Numerator 1 := by
  refine ⟨?_, ?_⟩
  · exact (toffoliFlip_eq_zero_iff one_pos).mpr rfl
  · rw [coneRow5Numerator_one]; norm_num

/-!
## The reduction is refuted by a ZERO-SET argument, independent of signs

The strongest form of the arc's conclusion, and the one that needs no
precision, no anchor and no convention.  The proof reduces the cone condition
to `P₇₇ · W_std` "with the appropriate sign from" `P₇₆`.  A product vanishes
exactly where one of its factors does, so any such reduction forces the cone
condition's zero set to be contained in the union of the factors'.  It is not:

| quantity | zeros on `q > 0` |
|---|---|
| the cone constraint `(G·t)₅` | one, at `q_c ≈ 0.8945` |
| `P₇₇ · W_std` | **none** — strictly positive throughout |
| `P₇₆` | one, at `q = 1` |

`q_c ≠ 1`, so the cone's zero is accounted for by neither factor.

The theorem below states this **without** needing the intermediate value
theorem or the exact value of `q_c`: on the interval `[1/2, 9/10]` the cone
constraint changes sign, while both claimed factors keep a constant (positive)
sign at both endpoints.  A quantity that changes sign where every factor of its
alleged product does not cannot be that product.
-/

/-- The cone constraint is already positive at `q = 9/10`, below `1`. -/
theorem coneRow5Numerator_nineTenths_pos : 0 < coneRow5Numerator (9 / 10) := by
  unfold coneRow5Numerator; norm_num

/-- **The reduction is refuted, without appeal to signs or precision.**  Across
    `[1/2, 9/10]` the cone constraint changes sign, while `P₇₇·W_std` and `P₇₆`
    are both strictly positive at each endpoint.  No product of factors that do
    not change sign can change sign, so the cone condition is not
    `P₇₇·W_std` modulated by anything depending only on `P₇₆`. -/
theorem cone_sign_change_unexplained_by_factors :
    coneRow5Numerator (1 / 2) < 0 ∧ 0 < coneRow5Numerator (9 / 10)
      ∧ 0 < toffoliDiagonal (1 / 2) * wStd (1 / 2)
      ∧ 0 < toffoliDiagonal (9 / 10) * wStd (9 / 10)
      ∧ 0 < toffoliFlipAmplitude (1 / 2)
      ∧ 0 < toffoliFlipAmplitude (9 / 10) := by
  refine ⟨coneRow5Numerator_half_neg, coneRow5Numerator_nineTenths_pos,
          toffoliDiagonal_mul_wStd_pos (by norm_num),
          toffoliDiagonal_mul_wStd_pos (by norm_num),
          toffoliFlip_pos_of_lt_one (by norm_num) (by norm_num),
          toffoliFlip_pos_of_lt_one (by norm_num) (by norm_num)⟩

end

/-! ## The cone condition inside the degree-2 subring of the amplitudes

The 8×8 strand-type amplitudes generate the whole field `ℚ(q)` — four of them
reconstruct `q` itself — so "is the cone condition a rational expression in
them?" has no content.  The question with content restricts the **form**: is it
in the *subring*, reachable by additions and multiplications alone?

It is, at degree 2, and the identity below is the witness.  Measured alongside
it (`computations/probes/toffoli_cone_in_entry_subring.py`): over the common
denominator `q⁶(q²+1)⁴` the ambient space of numerators is 21-dimensional and
the degree-2 span of the eight amplitudes has rank 15 — a proper subspace of
**codimension 6** — so membership is a genuine coincidence rather than the
forced answer.  Squares alone span only rank 14 and do *not* contain it, so the
cross terms are load-bearing.

**This does not revive `prop:toffoli-lp-stability`.**  That reduction is a
*monomial* times a sign, excluded by `toffoliDiagonal_pos` /
`toffoliFlip_eq_zero_iff` together with the sign change proved in
`cone_sign_change_unexplained_by_factors`.  A degree-2 polynomial is a strictly
larger class: it can vanish where no factor does, which is exactly how the cone
acquires its extra root.  The identity therefore *explains* the refutation
rather than weakening it. -/

/-- The convention-D diagonal `M₀₀ = (q⁴+1)/(q³(q²+1)²)`. -/
noncomputable def toffoliM00 (q : ℝ) : ℝ := (q ^ 4 + 1) / (q ^ 3 * (q ^ 2 + 1) ^ 2)

/-- The convention-D diagonal `M₃₃ = q(q²+1)/4`. -/
noncomputable def toffoliM33 (q : ℝ) : ℝ := q * (q ^ 2 + 1) / 4

/-- The convention-D diagonal `M₄₄ = (q²+1)/(4q³)`. -/
noncomputable def toffoliM44 (q : ℝ) : ℝ := (q ^ 2 + 1) / (4 * q ^ 3)

/-- The LP cone coordinate itself — row 5 of `G·t`, indexed by the longest
    Hecke normal-form word `σ₀σ₁σ₀`.  This is the single constraint of the six
    that changes sign; `coneRow5Numerator` is its numerator. -/
noncomputable def coneCoordRow5 (q : ℝ) : ℝ :=
  coneRow5Numerator q / (q ^ 2 + 1) ^ 2

/-- **The cone coordinate's sign is its numerator's.**  The denominator
    `(q²+1)²` is strictly positive, so every threshold statement proved about
    `coneRow5Numerator` transfers verbatim to the constraint itself. -/
theorem coneCoordRow5_pos_iff (q : ℝ) :
    0 < coneCoordRow5 q ↔ 0 < coneRow5Numerator q := by
  have hd : (0:ℝ) < (q ^ 2 + 1) ^ 2 := by positivity
  unfold coneCoordRow5
  exact div_pos_iff_of_pos_right hd

/-- **The cone condition is a degree-2 polynomial in four of the amplitudes.**

    An exact identity over `ℚ(q)`, valid for every `q > 0`:

    `(G·t)₅ = -4/9 + 5/36·M₀₀² - 20/3·M₀₀M₃₃ - 10/9·M₀₀M₄₄ + 5/18·M₀₀P₇₇`
    `        - 28/9·M₃₃² + 20/3·M₃₃M₄₄ + 38/9·M₃₃P₇₇ + 20/9·M₄₄² + 5/36·P₇₇²`

    Only `+` and `×` appear on the right: no division by an amplitude, hence no
    reconstruction of `q`.  Note the *cross* terms — the identity is false
    without them (the span of `{1}` together with the amplitudes and their
    squares alone does not contain the cone coordinate).

    This is *a* solution, not *the* solution: the solution space carries one
    free parameter over this four-amplitude span.  Whether any member has a
    Hecke-theoretic reading is open. -/
theorem cone_eq_quadratic_in_amplitudes {q : ℝ} (hq : 0 < q) :
    coneCoordRow5 q =
      -4/9
        + (5/36) * toffoliM00 q ^ 2
        - (20/3) * (toffoliM00 q * toffoliM33 q)
        - (10/9) * (toffoliM00 q * toffoliM44 q)
        + (5/18) * (toffoliM00 q * toffoliDiagonal q)
        - (28/9) * toffoliM33 q ^ 2
        + (20/3) * (toffoliM33 q * toffoliM44 q)
        + (38/9) * (toffoliM33 q * toffoliDiagonal q)
        + (20/9) * toffoliM44 q ^ 2
        + (5/36) * toffoliDiagonal q ^ 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  unfold coneCoordRow5 coneRow5Numerator toffoliM00 toffoliM33 toffoliM44
    toffoliDiagonal
  field_simp
  ring

/-! ## The same constraint in the Markov and Hecke parameters

The degree-2 expression above is in the *amplitude* basis, and its coefficients
are rationals with no evident meaning.  That is a fact about the basis, not
about the constraint: in the natural coordinates the expression is integral,
low-degree, and **forced** rather than fitted.

Write `z = q³/(q²+1)` for the Markov parameter (convention D) and note that
`toffoliConeCoord q = q - 1/q` is exactly the Hecke deformation `ħ` of the
quadratic relation `σ² = ħσ + 1` — the same object, already named for its other
role in this file, so no second name is introduced for it.

Every Markov trace of a Hecke word lies in `ℤ[z, ħ]`: the Markov property
`tr(x·σ_last) = z·tr(x)` removes the highest generator and the quadratic
relation reduces the rest.  The corpus already carries that as a table —
`QOU.Machinery.MarkovTraceH4.TRM` lists all 24 `H₄` normal-form trace values as
polynomials in `z` and `h`, its entries 9 and 13 being `h*z^2 + z`.  Since the
`q`-Toffoli's normal-form coordinates are `t = (0, 0, 1, ħ, 0, 0)`, i.e.
`T_q = σ₁ + ħ·σ₀σ₁`, the constraint `(G·t)₅ = tr(Wσ₁) + ħ·tr(Wσ₀σ₁)` is in
`ℤ[z, ħ]` before any computation. -/

/-- The Markov parameter, convention D (`z = q³/(q²+1)`).  The bare name
    `markovZ` denotes convention D uniformly across the corpus. -/
noncomputable def markovZ (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- **`tr(σ₀σ₁σ₀) = ħz² + z`.**  Not a finding of this arc — the value is
    already tabulated at `QOU.Machinery.MarkovTraceH4.TRM` entries 9 and 13.
    Recorded here in the form the constraint below consumes. -/
theorem toffoliDiagonal_eq_markov {q : ℝ} (hq : 0 < q) :
    toffoliDiagonal q = toffoliConeCoord q * markovZ q ^ 2 + markovZ q := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  unfold toffoliDiagonal toffoliConeCoord markovZ
  field_simp
  ring

/-- **The cone constraint is a degree-6 integer polynomial in `(z, ħ)`.**

    `(G·t)₅ = z² + 2ħz + 3ħ²z² + ħ³z + ħ⁴z²`

    Coefficients `(1, 2, 3, 1, 1)`; no denominators.  **Degree 6 is minimal** —
    no polynomial in `(z, ħ)` of total degree ≤ 5 equals it — and minimal degree
    is a genuine invariant of the class.

    ⚠ **The coefficient string is NOT an invariant.**  `z` and `ħ` are
    algebraically dependent (`markov_hecke_relation` below), so a representative
    is unique only modulo that relation; the degree-6 representatives form a
    six-parameter family, and `-1 + 4z² - 3ħz + 4z⁴ + ħ²z⁴` is an equally
    integral one.  Do not read meaning into `(1, 2, 3, 1, 1)`.  A reproducible
    choice is the grevlex normal form modulo the relation,
    `ħ⁵z + 4ħ³z + ħ² - 2ħz + 5z² - 1`, and even that depends on the term order.
    (`computations/probes/toffoli_cone_in_markov_hecke_parameters.py`, 18/18.)

    Both parameters are needed: the minimal polynomial of the constraint over
    `ℚ(z)` has degree 3 and over `ℚ(ħ)` degree 2, so it is a function of
    neither alone.  `ℚ(z, ħ) = ℚ(q)` — those degrees are coprime — so the
    content here is the *subring* statement, not a field statement. -/
theorem cone_eq_markov_hecke_polynomial {q : ℝ} (hq : 0 < q) :
    coneCoordRow5 q =
      markovZ q ^ 2
        + 2 * (toffoliConeCoord q * markovZ q)
        + 3 * (toffoliConeCoord q ^ 2 * markovZ q ^ 2)
        + toffoliConeCoord q ^ 3 * markovZ q
        + toffoliConeCoord q ^ 4 * markovZ q ^ 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  unfold coneCoordRow5 coneRow5Numerator toffoliConeCoord markovZ
  field_simp
  ring

/-- **The Markov parameter and the Hecke deformation are algebraically
    dependent**, satisfying the degree-4 irreducible relation

    `ħ³z - ħ²z² + 4ħz - 4z² + 1 = 0`.

    Consequence, and the reason it is stated here: `ℚ[z, ħ]` is *not* a
    polynomial ring but the coordinate ring of an affine rational curve, so a
    polynomial representative of any element is unique only modulo this
    relation.  In particular the coefficient string of
    `cone_eq_markov_hecke_polynomial` carries no information — the degree-6
    representatives of that one constraint form a six-parameter family.  What
    *is* invariant is the minimal degree.

    This is a fact about `H_n(q)` and its Markov trace, not about the
    `q`-Toffoli. -/
theorem markov_hecke_relation {q : ℝ} (hq : 0 < q) :
    toffoliConeCoord q ^ 3 * markovZ q
        - toffoliConeCoord q ^ 2 * markovZ q ^ 2
        + 4 * (toffoliConeCoord q * markovZ q)
        - 4 * markovZ q ^ 2 + 1 = 0 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  unfold toffoliConeCoord markovZ
  field_simp
  ring

/-! ## What the relation says: it is a statement about crossing loop values

`markov_hecke_relation` looks like an obstruction — it is what makes the
coefficient string above meaningless.  In the vocabulary of
`prop:markov-z-reconciliation` it is not an obstruction at all.  That block
defines the **negative-crossing loop value** `z₋ = z - (q - q⁻¹) = z - ħ`,
forced by the Hecke quadratic relation from the one-sided stabilisation rule,
and calls `a² = z/z₋` the Ocneanu **framing ratio**.  So `z - ħ`, met here as
an algebraic accident, is a named object.

Written in those terms the relation factors, via `ħ² + 4 = [2]_q²`, into
`z₊ z₋ = 1/[2]_q²`: the two crossing loop values multiply to the inverse
square of the quantum dimension.  Convention C satisfies neither this nor a
monomial framing ratio
(`computations/probes/markov_loop_value_product_and_framing_ratio.py`, 13/13). -/

/-- The quantum dimension `[2]_q = q + q⁻¹`. -/
noncomputable def qDimTwo (q : ℝ) : ℝ := q + 1 / q

/-- The negative-crossing loop value `z₋ = z - ħ`, forced by the Hecke
    quadratic relation (`prop:markov-z-reconciliation`). -/
noncomputable def markovZNeg (q : ℝ) : ℝ := markovZ q - toffoliConeCoord q

/-- `[2]_q² - ħ² = 4` — the quantum dimension and the Hecke deformation are a
    hyperbolic pair. -/
theorem qDimTwo_sq_sub_hbar_sq {q : ℝ} (hq : 0 < q) :
    qDimTwo q ^ 2 - toffoliConeCoord q ^ 2 = 4 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  unfold qDimTwo toffoliConeCoord
  field_simp
  ring

/-- `z₋ = 1/(q(q²+1))` in convention D — the negative-crossing loop value in
    closed form. -/
theorem markovZNeg_eq {q : ℝ} (hq : 0 < q) :
    markovZNeg q = 1 / (q * (q ^ 2 + 1)) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  unfold markovZNeg markovZ toffoliConeCoord
  field_simp
  ring

/-- **The two crossing loop values multiply to `1/[2]_q²`** (convention D).

    Equivalently `[2]_q² · z₊ · z₋ = 1`, which is `markov_hecke_relation` in
    closed form.  Convention C satisfies no such identity: there `z₊z₋` has
    half-integer and integer powers of `q` mixed in one numerator and does not
    factor. -/
theorem markov_loop_value_product {q : ℝ} (hq : 0 < q) :
    qDimTwo q ^ 2 * (markovZ q * markovZNeg q) = 1 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  rw [markovZNeg_eq hq]
  unfold qDimTwo markovZ
  field_simp

/-- **The Ocneanu framing ratio is a monomial in convention D**: `a² = q⁴`,
    so `a = q²`.  This is a *structural* reason for the convention-D ruling,
    independent of the empirical one on record (195.8 ppm on `tr_M(β_Bor)`) —
    no anchor and no measurement enters.  Convention C's framing ratio is
    `-q^{3/2}/(-q^{3/2} + q³ + q² - q - 1)`, not a monomial. -/
theorem markov_framing_ratio_eq {q : ℝ} (hq : 0 < q) :
    markovZ q = q ^ 4 * markovZNeg q := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  rw [markovZNeg_eq hq]
  unfold markovZ
  field_simp

/-- **`z = q²/[2]_q` in convention D** — the exact analogue of the form
    `z = 1/[2]_{√q}` that `prop:markov-z-reconciliation` already gives for
    convention C, which makes the two conventions comparable at a glance. -/
theorem markovZ_eq_qsq_div_qDimTwo {q : ℝ} (hq : 0 < q) :
    markovZ q * qDimTwo q = q ^ 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  unfold markovZ qDimTwo
  field_simp

/-! ## The Ocneanu family `z_N = q^N/[N]_q`, and why convention D is `N = 2`

**Prior art, credited late (2026-09-03).** This family is Wenzl's level-`r` Markov parameter
in Hecke normalisation: `markovZAt N q = wenzlMarkovParam N (q²) / q`
(`QOU.SchurWeyl.WenzlWeightLevelR`), and "D is the `N = 2` member" is
`QOU.QBeta.WenzlWeight.level_eq_two_of_conventionD` (PR #5242) and the `k = 2` remark in
`QOU.SchurWeyl.OcneanuWeight` (PR #5575).  The theorems below are kept as the per-cell
*mechanism* (the monomial framing ratio collapsing each numerator) and are not the first
formalisation of the family.

The monomial framing ratio of `markov_framing_ratio_eq` is not an aesthetic
fact.  `rem:markov-z-reconciliation` gives the Wedderburn block weights by the
frame-general Ocneanu formula, a product over the cells of `λ` of
`(z q^c - z₋ q^{-c})/(q^h - q^{-h})`.  When `a = q^N` — that is, when
`z = q^{2N} z₋` — every numerator collapses:

`z q^c - z₋ q^{-c} = z₋(q^{2N+c} - q^{-c}) = z₋ q^N (q^{N+c} - q^{-(N+c)})`,

so with `z₋ q^N = 1/[N]_q` the whole product becomes the hook-content formula
for the `U_q(𝔰𝔩_N)` quantum dimension, `w_λ = dim_q(V_λ)/[N]_q^n`.  Solving
`a = q^N` for `z` gives the family `z_N = q^N/[N]_q`, and `z₂` is convention D
on the nose.

Two consequences worth naming.  The exact vanishing `y_(1³) = 0` that the
corpus records for the production trace is the `𝔰𝔩₂` **row bound** — a
partition with more than `N` rows has a cell of content `-N`, whose numerator
factor carries `[0]_q = 0`.  And convention C is in *no* member of this family:
its framing ratio's logarithmic derivative is not constant, so it is `q^N` for
no `N` at all, and its weights vanish on no partition.

⚠ **`w_λ` is overloaded in this corpus** (notation register §7aa: the three
partition-weight families are distinct at `q ≠ 1`).  The weight identified here
is the **Ocneanu/Markov** one — the `y_λ` of the production trace.  It is *not*
`wedderburn-weight-canonical`'s `w_λ(q) = dim_q(λ)²/[n]_q!`, which is built
from the Frame–Robinson–Thrall hook-*length* dimension rather than the
hook-*content* one; measured at `n = 3` the two differ on every partition, and
differ already at `q = 1` (`1/6, 2/3, 1/6` against `1/2, 1/4, 0`).

Measurement:
`computations/probes/ocneanu_weights_are_sl_n_quantum_dimensions.py`, 13/13. -/

/-- The symmetric quantum integer `[m]_q = (q^m - q^{-m})/(q - q^{-1})`. -/
noncomputable def qIntSym (m : ℕ) (q : ℝ) : ℝ := (q ^ m - (1 / q) ^ m) / (q - 1 / q)

/-- `[2]_q` agrees with the quantum dimension `q + q⁻¹`. -/
theorem qIntSym_two {q : ℝ} (hq : 0 < q) (h1 : q ≠ 1) :
    qIntSym 2 q = qDimTwo q := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hd : q - 1 / q ≠ 0 := by
    rw [sub_ne_zero]
    intro h
    rw [eq_div_iff hq0] at h
    have hfac : (q - 1) * (q + 1) = 0 := by nlinarith [h]
    rcases mul_eq_zero.mp hfac with h' | h'
    · exact h1 (by linarith)
    · linarith
  have h2 : q ^ 2 - 1 ≠ 0 := by
    intro hz
    have hfac : (q - 1) * (q + 1) = 0 := by nlinarith [hz]
    rcases mul_eq_zero.mp hfac with h' | h'
    · exact h1 (by linarith)
    · linarith
  unfold qIntSym qDimTwo
  field_simp
  ring

/-- The Ocneanu family member with framing ratio `a = q^N`, in the form
    `z_N = q^{2N}ħ/(q^{2N} - 1)`; equivalently `q^N/[N]_q`. -/
noncomputable def markovZAt (N : ℕ) (q : ℝ) : ℝ :=
  q ^ (2 * N) * (q - 1 / q) / (q ^ (2 * N) - 1)

/-- **The defining property of the family: the framing ratio is `q^{2N}`.**
    `z_N = q^{2N}·(z_N - ħ)`, for every `N` — this is what makes the Ocneanu
    numerator collapse into quantum integers. -/
theorem markovZAt_framing {q : ℝ} (N : ℕ) (h : q ^ (2 * N) - 1 ≠ 0) :
    markovZAt N q = q ^ (2 * N) * (markovZAt N q - (q - 1 / q)) := by
  unfold markovZAt
  field_simp
  ring

/-- **Convention D is the `N = 2` member.**  `z₂ = q⁴ħ/(q⁴-1) = q³/(q²+1)`. -/
theorem markovZAt_two_eq_markovZ {q : ℝ} (hq : 0 < q) (h1 : q ≠ 1) :
    markovZAt 2 q = markovZ q := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have h2 : q ^ 2 - 1 ≠ 0 := by
    rw [sub_ne_zero]
    intro h
    apply h1
    nlinarith [sq_nonneg (q - 1), sq_nonneg (q + 1)]
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  have h4 : q ^ 4 - 1 ≠ 0 := by
    intro h
    apply h2
    have : (q ^ 2 - 1) * (q ^ 2 + 1) = 0 := by nlinarith [h]
    rcases mul_eq_zero.mp this with h' | h'
    · exact h'
    · exact absurd h' hd
  unfold markovZAt markovZ
  norm_num
  field_simp
  ring

/-- **The Ocneanu numerator collapses at framing `a = q^N`.**  Stated at the
    cell content `c` as a natural-number offset, which is all the `n = 3`
    weights below need: `z q^c - z₋ q^{-c} = z₋ q^N (q^{N+c} - q^{-(N+c)})`. -/
theorem ocneanu_numerator_collapse {q z zm : ℝ} (hq : 0 < q) (N c : ℕ)
    (h : z = q ^ (2 * N) * zm) :
    z * q ^ c - zm * (1 / q) ^ c
      = zm * q ^ N * (q ^ (N + c) - (1 / q) ^ (N + c)) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  subst h
  simp only [two_mul, pow_add, div_pow, one_pow]
  field_simp

/-- **The row bound, formally.**  At a cell of content `-N`, the Ocneanu
    numerator vanishes identically whenever the framing ratio is `q^N`.

    Since a partition with more than `N` rows always contains such a cell, this
    is why `w_λ = 0` there — and at `N = 2` it is why the corpus's exact
    `y_(1³) = 0` holds.  It is also what refutes the Wenzl-bridge premise
    `y_λ = w̃_λ` on the `κ_λ = 0` stratum: at `(3,1,1)` and `(3,2,1)` the left
    side is `0` by this lemma while `w̃_λ` is a ratio of positive quantum
    integers, so the identity asserts `0 = positive` and no parameter can
    reconcile it
    (`computations/probes/wenzl_bridge_self_conjugate_premise_is_false.py`,
    10/10). -/
theorem ocneanu_numerator_vanishes_at_content_neg {q z zm : ℝ} (hq : 0 < q)
    (N : ℕ) (h : z = q ^ (2 * N) * zm) :
    z * (1 / q) ^ N - zm * q ^ N = 0 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  subst h
  simp only [two_mul, pow_add, div_pow, one_pow]
  field_simp
  ring

end QOU.Information
