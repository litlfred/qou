import QOU.QBeta.FiveTwoBranchPinned
import QOU.MathlibExt.ComplexDilogarithmDeriv

/-!
# The envelope, wired: `d/dφ V(x φ, y φ) = ∂V/∂x · x′` along the curve

Bean `qou-trns`. `FiveTwoEnvelopeAssembly` proved the envelope theorem
abstractly — if `∂F/∂y = 0` the total derivative collapses to the `x`-part — and
`FiveTwoEnvelopeSum` proved what the surviving terms sum to. What was never
written is the instantiation at the actual potential

    V(x,y) = Li₂(y) + Li₂(x·y) + Li₂(y/x) + log(−y)² .

This file writes it.

## Route

The abstract theorem is stated for a Fréchet derivative on `ℂ × ℂ`. Getting one
for `V` means assembling four two-variable derivatives and then doing continuous
-linear-map algebra. Differentiating **along the path** instead needs only the
one-variable chain rule, four times, and produces the same statement:

    d/dφ V(x φ, y φ) = ∂V/∂x · x′ + ∂V/∂y · y′       (`hasDerivAt_deformedV_path`)

with `∂V/∂y = 0` then killing the second term (`hasDerivAt_deformedV_envelope`).
The abstract theorem remains the conceptual statement — and it is *not* used
here, which is worth saying plainly rather than implying a dependency that does
not exist.

## The collection step, and a trap it avoids

Adding the four chain-rule outputs is a rational identity, but the terms contain
logarithms and `field_simp` will happily rewrite `1 − y/x` to `(x−y)/x`
*inside* one — changing the branch and silently breaking the whole argument.
That happened once already in this lane. `dV_collect` therefore takes the four
logarithms as **opaque variables**, so no tactic ever sees a `log` while
denominators are cleared. Same discipline as `sum_div_of_pinned`.

## ⚠ The envelope hypothesis is NOT free on the curve

`dVdy x y = 0` unfolds to `(1−y)(1−x·y)(1−y/x) = y²`, which after clearing `x`
is `x·y² = (1−y)(1−x·y)(x−y)` — the deformed saddle, and by
`deformed_saddle_iff_curve` that **is** the curve (`dVdy_eq_zero_iff_exp`,
`exp_saddle_iff_curve`). An earlier draft of this docstring concluded from that
"so the envelope hypothesis is free on the curve". **That is false**, and
Route 30 G2 caught it:

| root | `dVdy` |
|---|---|
| the two roots other than the positive real one | `0` |
| the positive **real** root `t` | `2πi/t` — measured to `2e-40`, not `0` |

The exponentiated saddle holds at all three roots (to `1e-41`); what fails at
`t` is the *logarithmic* identity, because `−t` is a **negative real** and sits
on `log`'s cut, so `log(−t) = log t + iπ` and the `2·log(−y)` term contributes a
bare `2πi`. Exponentiating is necessary, not sufficient: the branch integers
have to line up too.

**The transport survives, and for a reason worth stating.** `S(φ) = Σⱼ Re Vⱼ`
takes real parts, and the leak is `2πi·t′/t` with `t` and `t′` **real**, hence
purely imaginary, hence killed by `Re`. Route 30 measures
`Re(dV/dφ) = Re(∂V/∂x·x′)` at **all** roots to `4.6e-41`, while the unreduced
difference reaches `2.47`. So `hasDerivAt_deformedV_envelope` below is a true
theorem whose hypothesis fails at one of the three roots, and
`hasDerivAt_re_deformedV_envelope` is the one that actually applies.

## Side conditions

The `Li₂` derivative needs each argument off the cut `[1,∞)` and nonzero. These
are stated as hypotheses, not assumed: they are what `FiveTwoCutAvoidance` is
for, and pretending otherwise is how a gap gets buried.

The `log(−y)` derivative is taken as a **hypothesis**, not derived from
`−y ∈ slitPlane`. An earlier draft did derive it that way, and Route 31 G4
showed the result: on this arc one of the three roots is real and positive at
*every* `φ`, so `−y` is a negative real, so `slitPlane` fails, so the theorem
was **vacuous at that root** — at all 199 sampled points. Two routes now supply
the hypothesis, with the same value `Y′/Y`:
`hasDerivAt_log_neg_of_slitPlane` off the cut, and `hasDerivAt_log_neg_ofReal`
on it via `log(−t) = log t + iπ`.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Complex QOU.MathlibExt

/-! ### 1. The potential and its two partials -/

/-- The deformed potential. -/
noncomputable def deformedV (p : ℂ × ℂ) : ℂ :=
  cLiTwoExt p.2 + cLiTwoExt (p.1 * p.2) + cLiTwoExt (p.2 / p.1) + Complex.log (-p.2) ^ 2

/-- `∂V/∂x = [−log(1 − x·y) + log(1 − y/x)] / x`. -/
noncomputable def dVdx (x y : ℂ) : ℂ :=
  (-Complex.log (1 - x * y) + Complex.log (1 - y / x)) / x

/-- `∂V/∂y = [−log(1−y) − log(1 − x·y) − log(1 − y/x) + 2·log(−y)] / y`. -/
noncomputable def dVdy (x y : ℂ) : ℂ :=
  (-Complex.log (1 - y) - Complex.log (1 - x * y) - Complex.log (1 - y / x)
    + 2 * Complex.log (-y)) / y

/-! ### 2. Collecting the four chain-rule terms -/

/-- **The collection step, with the logarithms held opaque.**

`L₁, L₂, L₃, M` stand for `log(1−y)`, `log(1 − x·y)`, `log(1 − y/x)`, `log(−y)`.
Keeping them as variables is not stylistic: `field_simp` rewrites `1 − y/x` to
`(x−y)/x`, and inside a logarithm that changes the branch. -/
theorem dV_collect {x y x' y' L₁ L₂ L₃ M : ℂ} (hx : x ≠ 0) (hy : y ≠ 0) :
    -(L₁ / y) * y' + -(L₂ / (x * y)) * (x' * y + x * y')
        + -(L₃ / (y / x)) * ((y' * x - y * x') / x ^ 2) + 2 * M * (y' / y)
      = ((-L₂ + L₃) / x) * x' + ((-L₁ - L₂ - L₃ + 2 * M) / y) * y' := by
  field_simp
  ring

/-! ### 2b. The `log(−y)` derivative — two routes, because one is not enough -/

/-- `log(−r) = log r + iπ` for real `r > 0`. -/
theorem log_neg_ofReal {r : ℝ} (hr : 0 < r) :
    Complex.log (-(r : ℂ)) = ((Real.log r : ℝ) : ℂ) + (Real.pi : ℂ) * Complex.I := by
  have hneg : -(r : ℂ) = ((-r : ℝ) : ℂ) := by push_cast; ring
  rw [hneg, Complex.log, Complex.arg_ofReal_of_neg (by linarith : -r < 0)]
  simp [abs_of_pos hr]

/-- Route 1: `−y` off the cut. The generic case. -/
theorem hasDerivAt_log_neg_of_slitPlane {Y : ℝ → ℂ} {Y' : ℂ} {s : ℝ}
    (hY : HasDerivAt Y Y' s) (hy0 : Y s ≠ 0) (hslit : -Y s ∈ Complex.slitPlane) :
    HasDerivAt (fun u => Complex.log (-Y u)) (Y' / Y s) s := by
  have := (Complex.hasDerivAt_log hslit).comp s hY.neg
  have heq : (-Y s)⁻¹ * -Y' = Y' / Y s := by field_simp
  rwa [heq] at this

/-- **Route 2: `Y` real and positive — where route 1 is impossible.**

At `y = t > 0` the point `−t` is a *negative real*, so it lies on `log`'s cut and
`hslit` can never hold. Route 30 G2 already showed the consequence for
`∂V/∂y`; Route 31 G4 showed the sharper one — a statement carrying `hslit` is
**vacuous** at the positive real root, which on this arc is one of the three
roots at every single `φ`.

The derivative still exists along a *real* path, because `log(−t) = log t + iπ`
is smooth in `t`, and it has the same value `Y′/Y`, so the path theorem below
does not care which route supplied it. -/
theorem hasDerivAt_log_neg_ofReal {t : ℝ → ℝ} {t' : ℝ} {s : ℝ}
    (ht : HasDerivAt t t' s) (hpos : 0 < t s) :
    HasDerivAt (fun u => Complex.log (-((t u : ℝ) : ℂ))) (((t' : ℝ) : ℂ) / ((t s : ℝ) : ℂ)) s := by
  have hev : ∀ᶠ u in nhds s, 0 < t u :=
    ht.continuousAt.eventually (eventually_gt_nhds hpos)
  have hrw : (fun u => ((Real.log (t u) : ℝ) : ℂ) + (Real.pi : ℂ) * Complex.I)
      =ᶠ[nhds s] fun u => Complex.log (-((t u : ℝ) : ℂ)) :=
    hev.mono fun u hu => (log_neg_ofReal hu).symm
  have hlog : HasDerivAt (fun u => Real.log (t u)) (t' / t s) s := ht.log hpos.ne'
  have hc : HasDerivAt (fun u => ((Real.log (t u) : ℝ) : ℂ) + (Real.pi : ℂ) * Complex.I)
      (((t' / t s : ℝ) : ℂ)) s := by
    simpa using (Complex.ofRealCLM.hasFDerivAt.comp_hasDerivAt s hlog).add_const
      ((Real.pi : ℂ) * Complex.I)
  have hval : ((t' / t s : ℝ) : ℂ) = ((t' : ℝ) : ℂ) / ((t s : ℝ) : ℂ) := by push_cast; ring
  rw [hval] at hc
  exact hc.congr_of_eventuallyEq hrw.symm

/-! ### 3. The derivative along a path -/

/-- **The total derivative along any differentiable path.**

Four applications of the one-variable chain rule, collected by `dV_collect`. -/
theorem hasDerivAt_deformedV_path {X Y : ℝ → ℂ} {X' Y' : ℂ} {s : ℝ}
    (hX : HasDerivAt X X' s) (hY : HasDerivAt Y Y' s)
    (hx0 : X s ≠ 0) (hy0 : Y s ≠ 0)
    (hc₁ : Y s ∈ notCut) (hc₂ : X s * Y s ∈ notCut) (hc₃ : Y s / X s ∈ notCut)
    (hn₂ : X s * Y s ≠ 0) (hn₃ : Y s / X s ≠ 0)
    (hlogd : HasDerivAt (fun u => Complex.log (-Y u)) (Y' / Y s) s) :
    HasDerivAt (fun u => deformedV (X u, Y u))
      (dVdx (X s) (Y s) * X' + dVdy (X s) (Y s) * Y') s := by
  -- the four inner paths
  have hprod : HasDerivAt (fun u => X u * Y u) (X' * Y s + X s * Y') s := hX.mul hY
  have hquot : HasDerivAt (fun u => Y u / X u) ((Y' * X s - Y s * X') / X s ^ 2) s :=
    hY.div hX hx0
  -- the four outer derivatives
  have h1 : HasDerivAt (fun u => cLiTwoExt (Y u))
      (-(Complex.log (1 - Y s) / Y s) * Y') s :=
    (hasDerivAt_cLiTwoExt' hc₁ hy0).comp s hY
  have h2raw := (hasDerivAt_cLiTwoExt' hc₂ hn₂).comp s hprod
  have h2 : HasDerivAt (fun u => cLiTwoExt (X u * Y u))
      (-(Complex.log (1 - X s * Y s) / (X s * Y s)) * (X' * Y s + X s * Y')) s := h2raw
  have h3raw := (hasDerivAt_cLiTwoExt' hc₃ hn₃).comp s hquot
  have h3 : HasDerivAt (fun u => cLiTwoExt (Y u / X u))
      (-(Complex.log (1 - Y s / X s) / (Y s / X s)) * ((Y' * X s - Y s * X') / X s ^ 2)) s := h3raw
  have hlog := hlogd
  have h4 : HasDerivAt (fun u => Complex.log (-Y u) ^ 2)
      (2 * Complex.log (-Y s) * (Y' / Y s)) s := by
    have := hlog.pow 2
    simpa [pow_one, mul_comm, mul_assoc, mul_left_comm] using this
  -- add and collect
  have hsum := ((h1.add h2).add h3).add h4
  unfold deformedV dVdx dVdy
  convert hsum using 1
  exact (dV_collect (L₁ := Complex.log (1 - Y s)) (L₂ := Complex.log (1 - X s * Y s))
    (L₃ := Complex.log (1 - Y s / X s)) (M := Complex.log (-Y s)) hx0 hy0).symm

/-- **The envelope collapse.** With `∂V/∂y = 0`, the `Y′` term dies and the total
derivative is the `x`-part alone — whatever `Y′` happens to be. This is why the
argument needs only that the roots are *differentiable*. -/
theorem hasDerivAt_deformedV_envelope {X Y : ℝ → ℂ} {X' Y' : ℂ} {s : ℝ}
    (hX : HasDerivAt X X' s) (hY : HasDerivAt Y Y' s)
    (hx0 : X s ≠ 0) (hy0 : Y s ≠ 0)
    (hc₁ : Y s ∈ notCut) (hc₂ : X s * Y s ∈ notCut) (hc₃ : Y s / X s ∈ notCut)
    (hn₂ : X s * Y s ≠ 0) (hn₃ : Y s / X s ≠ 0)
    (hlogd : HasDerivAt (fun u => Complex.log (-Y u)) (Y' / Y s) s)
    (hsaddle : dVdy (X s) (Y s) = 0) :
    HasDerivAt (fun u => deformedV (X u, Y u)) (dVdx (X s) (Y s) * X') s := by
  have h := hasDerivAt_deformedV_path hX hY hx0 hy0 hc₁ hc₂ hc₃ hn₂ hn₃ hlogd
  rwa [hsaddle, zero_mul, add_zero] at h

/-! ### 3b. The version that actually applies: real parts -/

/-- Taking real parts of a `ℝ → ℂ` derivative. -/
theorem hasDerivAt_re {f : ℝ → ℂ} {f' : ℂ} {s : ℝ} (h : HasDerivAt f f' s) :
    HasDerivAt (fun u => (f u).re) f'.re s :=
  Complex.reCLM.hasFDerivAt.comp_hasDerivAt s h

/-- **The envelope collapse for `Re V` — the one the transport uses.**

The hypothesis is not `∂V/∂y = 0` but the weaker `Re(∂V/∂y · y′) = 0`, which is
what actually holds at all three roots: at the two non-real ones `∂V/∂y` is `0`
outright, and at the positive real root `t` it is `2πi/t`, so `∂V/∂y · t′` is
purely imaginary because `t` and `t′` are real. See the module docstring — the
stronger hypothesis is false at that root, and Route 30 G2 measures it. -/
theorem hasDerivAt_re_deformedV_envelope {X Y : ℝ → ℂ} {X' Y' : ℂ} {s : ℝ}
    (hX : HasDerivAt X X' s) (hY : HasDerivAt Y Y' s)
    (hx0 : X s ≠ 0) (hy0 : Y s ≠ 0)
    (hc₁ : Y s ∈ notCut) (hc₂ : X s * Y s ∈ notCut) (hc₃ : Y s / X s ∈ notCut)
    (hn₂ : X s * Y s ≠ 0) (hn₃ : Y s / X s ≠ 0)
    (hlogd : HasDerivAt (fun u => Complex.log (-Y u)) (Y' / Y s) s)
    (himag : (dVdy (X s) (Y s) * Y').re = 0) :
    HasDerivAt (fun u => (deformedV (X u, Y u)).re) ((dVdx (X s) (Y s) * X').re) s := by
  have h := hasDerivAt_re (hasDerivAt_deformedV_path hX hY hx0 hy0 hc₁ hc₂ hc₃ hn₂ hn₃ hlogd)
  rwa [Complex.add_re, himag, add_zero] at h

/-- **The mechanism, named.** A purely imaginary `∂V/∂y` against a real `y′`
leaves nothing in the real part — which is exactly the positive real root's
situation, where `∂V/∂y = 2πi/t`. -/
theorem re_mul_eq_zero_of_im_axis {z : ℂ} {r : ℝ} (hz : z.re = 0) :
    (z * (r : ℂ)).re = 0 := by
  simp [Complex.mul_re, hz]

/-! ### 4. The saddle condition is the curve -/

/-- **`∂V/∂y = 0` reduces to the deformed saddle equation.**

`dVdy = 0` says `log[(1−y)(1−x·y)(1−y/x)] = 2 log(−y)`; exponentiating and
clearing `x` gives `x·y² = (1−y)(1−x·y)(x−y)`, which
`deformed_saddle_iff_curve` identifies with the curve. Stated at the level of
the exponentiated identity, which is where the branch choice stops mattering. -/
theorem dVdy_eq_zero_iff_exp {x y : ℂ} (hy : y ≠ 0) :
    dVdy x y = 0 ↔
      Complex.log (1 - y) + Complex.log (1 - x * y) + Complex.log (1 - y / x)
        = 2 * Complex.log (-y) := by
  unfold dVdy
  rw [div_eq_zero_iff]
  constructor
  · rintro (h | h)
    · linear_combination -h
    · exact absurd h hy
  · intro h
    left
    linear_combination -h

/-- The exponentiated saddle condition **is** the curve. -/
theorem exp_saddle_iff_curve {x y : ℂ} (hx : x ≠ 0)
    (h : (1 - y) * (1 - x * y) * (1 - y / x) = y ^ 2) :
    curve x y = 0 := by
  rw [← deformed_saddle_iff_curve]
  field_simp at h
  linear_combination -h

/-! ### 5. `∂V/∂y` on the curve is `2πi·(integer)/y` — Route 30's correction, structurally

Route 30 G2 refuted "the envelope hypothesis is free on the curve": `∂V/∂y = 0`
holds at two of the three roots, but at the positive real root it is `2πi/t`,
because `−t` sits on `log`'s cut.

The general statement behind that is cleaner than either case. On the curve the
**exponentiated** saddle holds exactly, so the logarithmic one holds *up to*
`2πi`, and therefore

    ∂V/∂y · y  ∈  2πi·ℤ

at **every** point of the curve. `k = 0` recovers the two easy roots; `k = ∓1`
is the real root's leak. Nothing has to be known in advance about which root is
which. -/
theorem exists_int_dVdy_mul {x y : ℂ} (hx : x ≠ 0) (hy : y ≠ 0)
    (h1 : (1 : ℂ) - y ≠ 0) (h2 : (1 : ℂ) - x * y ≠ 0) (h3 : (1 : ℂ) - y / x ≠ 0)
    (hc : curve x y = 0) :
    ∃ k : ℤ, dVdy x y * y = -(k * (2 * Real.pi * Complex.I)) := by
  have hneg : (-y) ≠ 0 := neg_ne_zero.mpr hy
  set S : ℂ := Complex.log (1 - y) + Complex.log (1 - x * y) + Complex.log (1 - y / x)
    - 2 * Complex.log (-y) with hS
  -- the exponentiated saddle, from the curve
  have hsad : (1 - y) * (1 - x * y) * (1 - y / x) = y ^ 2 := by
    have := (deformed_saddle_iff_curve x y).mpr hc
    field_simp
    linear_combination -this
  -- so `exp S = 1`
  have hexp : Complex.exp S = 1 := by
    rw [hS]
    rw [Complex.exp_sub, Complex.exp_add, Complex.exp_add,
      Complex.exp_log h1, Complex.exp_log h2, Complex.exp_log h3]
    rw [show (2 : ℂ) * Complex.log (-y) = Complex.log (-y) + Complex.log (-y) by ring,
      Complex.exp_add, Complex.exp_log hneg]
    rw [hsad]
    field_simp
  obtain ⟨k, hk⟩ := Complex.exp_eq_one_iff.mp hexp
  refine ⟨k, ?_⟩
  have hdv : dVdy x y * y = -S := by
    unfold dVdy
    rw [hS]
    field_simp
    ring
  rw [hdv, hk]

/-- **Hence the envelope condition holds at any curve point with a REAL root and
a real derivative** — which is exactly the positive real root's situation.

`dVdy · y = 2πi·k` makes `dVdy` purely imaginary when `y` is real, and a real
`Y'` then leaves nothing in the real part. This is Route 30's leak, discharged
rather than assumed. -/
theorem re_dVdy_mul_eq_zero_of_real {x : ℂ} {t t' : ℝ} (hx : x ≠ 0) (ht : t ≠ 0)
    (h1 : (1 : ℂ) - (t : ℂ) ≠ 0) (h2 : (1 : ℂ) - x * (t : ℂ) ≠ 0)
    (h3 : (1 : ℂ) - (t : ℂ) / x ≠ 0) (hc : curve x (t : ℂ) = 0) :
    (dVdy x (t : ℂ) * (t' : ℂ)).re = 0 := by
  have htc : ((t : ℝ) : ℂ) ≠ 0 := by simpa using ht
  obtain ⟨k, hk⟩ := exists_int_dVdy_mul hx htc h1 h2 h3 hc
  -- `dVdy = −k·2πi / t`, purely imaginary since `t` is real
  have hre : (dVdy x (t : ℂ)).re = 0 := by
    have hval : dVdy x (t : ℂ) = -(k * (2 * Real.pi * Complex.I)) / ((t : ℝ) : ℂ) := by
      field_simp at hk ⊢
      linear_combination hk
    rw [hval]
    simp [Complex.div_re, Complex.ofReal_re, Complex.ofReal_im]
  exact re_mul_eq_zero_of_im_axis hre

end QOU.QBeta.FiveTwoDeformedSaddle
