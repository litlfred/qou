/-
# The symmetry energy's sign is locked by AM–GM

A bond sum is additive in `L = -log b`, so the whole composition dependence of
the binding law collapses to one slope. For any graph and any proton/neutron
assignment, with `E = E_pp + E_pn + E_nn`,

```
Σ = (L_pp+L_nn)/2 · E  +  (L_pp-L_nn)/2 · (E_pp - E_nn)  +  δ · E_pn
δ = L_pn - (L_pp+L_nn)/2
```

Holding `E` and the imbalance `E_pp - E_nn` fixed, `Σ` is affine in `E_pn` with
slope `δ`. A symmetric nucleus maximises `E_pn`, an asymmetric one minimises it,
so the law binds symmetric nuclei more — the SEMF sign — exactly when `δ > 0`.
No layout, graph or scale enters that statement.

`δ` compares `b_pn` against the **geometric** mean of `b_pp` and `b_nn`, because
the sum is additive in the logs. The corpus builds `b_pn` as an **arithmetic**
(convex) combination of them: `pn-bond-cannot-be-extremal.md`, merged
2026-09-04, shows `b_pn = w·b_pp + (1-w)·b_nn` with `w = 1/2 + δ_flavour/4`.
Arithmetic beats geometric. So the sign comes out backwards, and it does so
structurally rather than numerically.

## What is proved here

* `delta_nonpos_iff` — the sign question *is* the AM-vs-GM question.
* `sqrt_mul_le_midpoint` and `delta_midpoint_nonpos` — an equal-weight p-n bond
  is wrong-signed for any positive `b_pp`, `b_nn`.
* `crossing_weight` — with the pinned `b_pp = q²/[2]_q`, `b_nn = q⁻²/[2]_q`, the
  weight landing exactly on the geometric mean is `w = 1/(q²+1)`.
* `convex_strictMono` — above that weight the combination exceeds the mean, so
  by `delta_nonpos_iff` it is on the wrong side.
* `crossing_lt_half` — `1/(q²+1) < 1/2` for every `q > 1`, so no re-derivation
  of `q` rescues an equal-weight construction.
* `am_sub_gm_eq` — the gap is `h²/(2[2]_q)` with `h = q - 1/q`, the Hecke
  parameter itself. The deformation *is* the gap.

## The numbers this instantiates

`computations/qbeta/qbeta_symmetry_sign_is_am_gm_locked_probe.py`, at `q₀`:
GM `= 1/[2]_q = 0.497290545605`, AM `= 0.508155…`, the corpus `b_pn =
0.508229789377`, recovered `w = 0.500343927702` against a threshold
`1/(q₀²+1) = 0.448018144974` — **11.7 % above it**. The endpoints `δ(w=0) =
+2 log q₀` and `δ(w=1) = -2 log q₀` are exactly bean `qou-y2np`'s bar branch, so
that "one bit" is two points of this continuum and the crossing between them is
derived.

## What is NOT proved

The POWER. Turning `E_pn` into the SEMF's `(N-Z)²/A` needs a well-mixed
assignment (`E_pn ≈ 2E·ZN/A²`), which is a mean-field model rather than a
theorem — and the corpus's canonical layout is segregated, with `E_pn = 1` and
no symmetry term at all. Everything below is about the SIGN, which needs none
of that.

Bean `qou-i01a`; unifies `qou-q7ga`, `qou-y2np` and the sibling's convexity
result.
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

namespace QOU.Hecke.SymmetrySignAmGm

open Real

/-- The p–n slope: how the bond sum changes when one like-species pair of bonds
is traded for a p–n bond, in the corpus's `L = -log b` letters. Positive means
mixing binds more — the SEMF sign. -/
noncomputable def delta (bpp bpn bnn : ℝ) : ℝ :=
  (Real.log bpp + Real.log bnn) / 2 - Real.log bpn

/-- **The sign question is the AM-vs-GM question.** `δ ≤ 0` — the wrong sign —
exactly when `b_pn` is at least the geometric mean of the like-species bonds.
Everything else in this file is about which side of that mean the construction
puts `b_pn` on. -/
theorem delta_nonpos_iff {bpp bpn bnn : ℝ} (hpp : 0 < bpp) (hpn : 0 < bpn)
    (hnn : 0 < bnn) :
    delta bpp bpn bnn ≤ 0 ↔ Real.sqrt (bpp * bnn) ≤ bpn := by
  have hprod : (0 : ℝ) < bpp * bnn := mul_pos hpp hnn
  have hlog : Real.log (Real.sqrt (bpp * bnn)) = (Real.log bpp + Real.log bnn) / 2 := by
    rw [Real.log_sqrt hprod.le, Real.log_mul hpp.ne' hnn.ne']
  have hs : (0 : ℝ) < Real.sqrt (bpp * bnn) := Real.sqrt_pos.mpr hprod
  rw [delta, sub_nonpos, ← hlog, Real.log_le_log_iff hs hpn]

/-- **AM–GM in the two-variable form the bond letters need.** -/
theorem sqrt_mul_le_midpoint {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) :
    Real.sqrt (a * b) ≤ (a + b) / 2 := by
  have h1 : a * b ≤ ((a + b) / 2) ^ 2 := by nlinarith [sq_nonneg (a - b)]
  calc Real.sqrt (a * b) ≤ Real.sqrt (((a + b) / 2) ^ 2) := Real.sqrt_le_sqrt h1
    _ = (a + b) / 2 := Real.sqrt_sq (by linarith)

/-- **An equal-weight p–n bond is always wrong-signed.** Nothing about `q`, the
graph or the scale enters: the midpoint of two positives is never below their
geometric mean, so `δ ≤ 0` however the letters come out. -/
theorem delta_midpoint_nonpos {bpp bnn : ℝ} (hpp : 0 < bpp) (hnn : 0 < bnn) :
    delta bpp ((bpp + bnn) / 2) bnn ≤ 0 :=
  (delta_nonpos_iff hpp (by linarith) hnn).mpr (sqrt_mul_le_midpoint hpp.le hnn.le)

/-- **The crossing weight, in the pinned case.** With `b_pp = q²/[2]_q` and
`b_nn = q⁻²/[2]_q` the geometric mean is `1/[2]_q`, and the convex weight that
lands exactly on it is `w = 1/(q²+1)`. Stated as the identity rather than as an
inequality, because the identity is what a reader checks. -/
theorem crossing_weight {q : ℝ} (hq : 0 < q) :
    (1 / (q ^ 2 + 1)) * (q ^ 2 / (q + 1 / q))
      + (1 - 1 / (q ^ 2 + 1)) * ((q ^ 2)⁻¹ / (q + 1 / q))
      = 1 / (q + 1 / q) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : q + 1 / q ≠ 0 := by positivity
  field_simp
  ring

/-- The convex combination is strictly increasing in the weight when the p–p
bond is the larger. So a weight ABOVE the crossing puts `b_pn` above the
geometric mean, which by `delta_nonpos_iff` is the wrong side. -/
theorem convex_strictMono {bpp bnn w w' : ℝ} (h : bnn < bpp) (hw : w < w') :
    w * bpp + (1 - w) * bnn < w' * bpp + (1 - w') * bnn := by nlinarith

/-- **No `q > 1` rescues an equal-weight construction.** The crossing `1/(q²+1)`
is `1/2` only at `q = 1` and strictly below it thereafter, while the corpus holds
the weight at `1/2 + δ_flavour/4`. This is `qou-q7ga`'s "the q-deformation is
net-negative on binding", with a mechanism: the deformation moves the threshold
down, the construction does not follow it. -/
theorem crossing_lt_half {q : ℝ} (hq : 1 < q) : 1 / (q ^ 2 + 1) < 1 / 2 := by
  have hq2 : (1 : ℝ) < q ^ 2 := by nlinarith
  have hpos : (0 : ℝ) < q ^ 2 + 1 := by linarith
  rw [div_lt_div_iff₀ hpos (by norm_num : (0:ℝ) < 2)]
  linarith

/-- **The AM–GM gap IS the Hecke parameter, squared.**
`(b_pp+b_nn)/2 - 1/[2]_q = h²/(2[2]_q)` with `h = q - 1/q`, because
`[2]_q² - 4 = h²`. The size of the wrong-signed term is not incidental to the
deformation — it is the deformation. -/
theorem am_sub_gm_eq {q : ℝ} (hq : 0 < q) :
    (q ^ 2 / (q + 1 / q) + (q ^ 2)⁻¹ / (q + 1 / q)) / 2 - 1 / (q + 1 / q)
      = (q - 1 / q) ^ 2 / (2 * (q + 1 / q)) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hsum : q + 1 / q ≠ 0 := by positivity
  field_simp
  ring

/-! ## Deriving the convex weight `w`

`w` is not a free parameter. The corpus's three interface factors are
`f_pp = z` (positive crossing, the Markov axiom `tr(ασ) = z·tr(α)`),
`f_nn = z - h` (negative crossing, via the Hecke skein `σ⁻¹ = σ - h`), and
`f_pn = z - h·(1/2 - δ/4)` (`bring_color_weighted`, the default since
2026-06-01). `weight_of_convention` shows the convex weight is then **forced**:
`w = 1/2 + δ/4`, identically, for any `z`, `h`, `δ`.

So "derive `w`" reduces entirely to deriving the flat `1/2` in
`σ_avg = (σ + σ⁻¹)/2` — and `weight_miss` shows that flat half is the whole
story: the miss against the crossing splits as `(q²-1)/(2(q²+1)) + δ/4`, whose
two parts stand at `0.0519819` and `0.000344`, a ratio of **151**. The only
derived ingredient in `w` is 151× too small to matter. -/

/-- **The convex weight is forced by the averaging convention.** Given the three
interface factors, `w = 1/2 + δ/4` is an identity, not a choice. -/
theorem weight_of_convention (z h d : ℝ) :
    z - h * (1 / 2 - d / 4)
      = (1 / 2 + d / 4) * z + (1 - (1 / 2 + d / 4)) * (z - h) := by ring

/-- **The miss against the crossing, split.** The deformation term
`(q²-1)/(2(q²+1))` and the flavour term `δ/4` are the only two contributions,
and at `q₀` the first is 151× the second — so the flavour split, the one derived
ingredient in `w`, is irrelevant to the sign. -/
theorem weight_miss {q d : ℝ} (hq : 0 < q) :
    (1 / 2 + d / 4) - 1 / (q ^ 2 + 1)
      = (q ^ 2 - 1) / (2 * (q ^ 2 + 1)) + d / 4 := by
  have : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-! ## Which means can give the SEMF sign: exactly those below the geometric

`mean_mul_reciprocal_mean` is the two-variable identity `M_p · M_{-p} = ab`,
whose immediate consequence is that `δ` is **odd** under `p ↦ -p`. The
convention sits at `p = 1`; its mirror `p = -1` is the harmonic mean, which
therefore has exactly the opposite `δ` — same magnitude, SEMF sign. Since `M_p`
is increasing in `p` and `M_0` is the geometric mean, the sign is right exactly
when `p < 0`: strictly BELOW the geometric mean, which is where no average with
`p ≥ 0` can go.

Stated here for `p = ±1`, where it needs no `rpow` and is the case that matters;
the general statement is measured in
`computations/qbeta/qbeta_symmetry_sign_is_am_gm_locked_probe.py`. -/

/-- `HM · AM = a·b`, the `p = ±1` case of `M_p · M_{-p} = ab`. -/
theorem harmonic_mul_arithmetic {a b : ℝ} (hab : a + b ≠ 0) :
    (2 * a * b / (a + b)) * ((a + b) / 2) = a * b := by
  field_simp

/-- **The harmonic mean is the arithmetic mean's exact mirror.** `δ` flips sign
and keeps its magnitude, so the wrong-signed `-0.0216177…` at `p = 1` is
`+0.0216177…` at `p = -1`. -/
theorem delta_harmonic_eq_neg_delta_arithmetic {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    delta a (2 * a * b / (a + b)) b = -delta a ((a + b) / 2) b := by
  have hab : (0 : ℝ) < a + b := by linarith
  have hH : (0 : ℝ) < 2 * a * b / (a + b) := by positivity
  have hA : (0 : ℝ) < (a + b) / 2 := by linarith
  have hmul := harmonic_mul_arithmetic (ne_of_gt hab)
  have : Real.log (2 * a * b / (a + b)) + Real.log ((a + b) / 2)
      = Real.log a + Real.log b := by
    rw [← Real.log_mul (ne_of_gt hH) (ne_of_gt hA), hmul,
        Real.log_mul (ne_of_gt ha) (ne_of_gt hb)]
  simp only [delta]
  linarith

/-- **So the harmonic mean gives the SEMF sign**, for any positive bonds. It is
recorded as a TARGET a derivation may be checked against — never as a criterion
to search on, and nothing here adopts it. -/
theorem delta_harmonic_nonneg {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    0 ≤ delta a (2 * a * b / (a + b)) b := by
  rw [delta_harmonic_eq_neg_delta_arithmetic ha hb, neg_nonneg]
  exact delta_midpoint_nonpos ha hb

/-! ## The three means in `[2]` form

With `b_pp = q²/[2]_q` and `b_nn = q⁻²/[2]_q`, writing `[2]_x = x + 1/x`:

```
AM = [2]_{q²}/(2[2]_q)      GM = 1/[2]_q      HM = 2/([2]_q·[2]_{q²})
```

⚠ Their convex weights are `1/2`, `q⁻¹/[2]_q`, `q⁻²/[2]_{q²}`, which LOOK like a
ladder `q^{-k}/[2]_{q^k}`. **They are not.** At `p = 2` that formula predicts
`0.55198` against the true `0.55089`, and it fails at every non-classical `p`
tested. It is a coincidence of the three classical means and is recorded here so
nobody re-derives it as structure. -/

/-- `AM = [2]_{q²}/(2[2]_q)`. -/
theorem arithmetic_pinned {q : ℝ} (hq : 0 < q) :
    (q ^ 2 / (q + 1 / q) + (q ^ 2)⁻¹ / (q + 1 / q)) / 2
      = (q ^ 2 + 1 / q ^ 2) / (2 * (q + 1 / q)) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have : q + 1 / q ≠ 0 := by positivity
  field_simp

/-- `HM = 2/([2]_q·[2]_{q²})`, and with `arithmetic_pinned` and `GM = 1/[2]_q`
this completes `AM·HM = GM²`. -/
theorem harmonic_pinned {q : ℝ} (hq : 0 < q) :
    2 * (q ^ 2 / (q + 1 / q)) * ((q ^ 2)⁻¹ / (q + 1 / q))
        / (q ^ 2 / (q + 1 / q) + (q ^ 2)⁻¹ / (q + 1 / q))
      = 2 / ((q + 1 / q) * (q ^ 2 + 1 / q ^ 2)) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have h2 : q + 1 / q ≠ 0 := by positivity
  have h4 : q ^ 2 + 1 / q ^ 2 ≠ 0 := by positivity
  field_simp

end QOU.Hecke.SymmetrySignAmGm
