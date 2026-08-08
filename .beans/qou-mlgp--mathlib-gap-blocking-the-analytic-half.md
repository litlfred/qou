---
# qou-mlgp
title: 'The Mathlib gap that blocks formalising the analytic half of the c_sigma derivation'
status: todo
type: task
priority: normal
tags:
    - lean
    - mathlib
    - c-sigma
    - one-loop
    - formalization-gap
created_at: 2026-08-08T22:20:00Z
updated_at: 2026-08-08T22:20:00Z
---

## What is and is not formalised

`QOU.OneLoopPrefactorInvariance` proves the ALGEBRA of the `c_sigma`
derivation sorry-free: `k_sq_eq_half_of_saddle`, `c_pow_four_eq_third`,
`saddle_forces_cot`, `vdv_c_sigma_iff_tau`, `vdv_tau_sq`,
`vdv_radical_is_gaussian_norm`, plus the `Sigma(2,3,5)` keystone tower.

The ANALYTIC input is assumed, as hypotheses `hc` and `hτ`, and is the whole of
what remains open on this arc:

  (A) the Euler-Maclaurin expansion
      `s_n = (N/pi) Lambda(n pi/N) - (1/2) log(2 N sin(r pi)) + O(1/N)`
      with the CONSTANT, not merely the leading order;
  (B) Laplace's method for a SUM,
      `sum_k e^{phi(k)} ~ e^{phi(k*)} sqrt(2 pi / |phi''(k*)|)`;
  (C) the Lobachevsky function `Lambda(theta) = -int_0^theta log|2 sin x| dx`
      with `Lambda' = -log|2 sin|` and `Lambda'' = -cot`;
  (D) the multivariate Gaussian with complex covariance,
      `int_{R^{n+1}} exp(-pi[A u^2/2 + 2 sum (v_j + u/2)^2]) = 2^{-n/2} sqrt(2/A)`.

## CORRECTION — I checked Mathlib and not the corpus. (C) is DONE, in-repo.

The gap analysis below is right about *Mathlib* and wrong about *qou*, and the
error is the same one this session made three times before it: asking "does the
library have it?" without asking "do we already have it?"

**(C) the Lobachevsky function and its derivatives: ALREADY BUILT.**

    QOU/Archimedean/BlochWignerLobachevsky.lean   Lob t = Cl_2 (2t)/2, values
    QOU/Knot/Clausen.lean                         hasDerivAt_clausen, and the
                                                  Riemann-sum machinery
    QOU/Archimedean/LobachevskyDerivative.lean    hasDerivAt_Lob   (Lambda' = -log(2 sin))
                                                  deriv_deriv_Lob  (Lambda'' = -cot)
                                                  deriv_deriv_Lob_neg / _pos
                                                  hasDerivAt_neg_log_two_sin
    QOU/Knot/FigureEightVolumeSqueeze.lean        tendsto_log_kashaev_vol --
                                                  the figure-eight volume
                                                  conjecture at LEADING order,
                                                  discharged

and `QOU/MathlibExt/` is a 54-file Mathlib-gap staging area that already holds
`ComplexDilogarithm`, `QuantumDilogarithm`, `FaddeevQuantumDilogarithm` and more.

I wrote a `LobachevskyDerivatives.lean` (plural) reproducing four of those
theorems — one of them, `hasDerivAt_neg_log_two_sin`, with the IDENTICAL name in
the IDENTICAL namespace, which would have collided on build. It compiled
sorry-free and was deleted unbuilt. `LobachevskyDerivative.lean`'s own header
even records the same lesson about a stale bean: "the bean's note that the
corpus has 'no Lobachevsky function' is stale."

**So the standing gap is narrower than stated below.** `kashaev N` is already
defined in Lean (`FigureEightVolume.lean`, as
`sum_k prod_j (2 - 2 cos(2 pi j/N))` = the same `prod 4 sin^2` the probe uses),
and `(2 pi/N) log(kashaev N) -> Vol(4_1)` is proved. What is missing is exactly
the NEXT ORDER: from

    log kashaev N = Vol N/(2 pi) + o(N)                     [PROVED in-repo]

to

    log kashaev N = Vol N/(2 pi) + (3/2) log N + log(3^{-1/4}) + o(1)   [OPEN]

which needs (A) Euler-Maclaurin for `s_n` WITH the constant and (B) Laplace's
method for a sum — and only those two. (C) is done and (D) Mathlib has.

## What Mathlib actually has — CHECKED, not assumed

The mathlib package in this repo is cache-only (build artifacts, no `.lean`
source), so this was determined by enumerating the compiled module tree:
`.lake/packages/mathlib/.lake/build/lib/lean/Mathlib`, 6990 modules.

  HAVE     Analysis/SpecialFunctions/Gaussian/GaussianIntegral.olean   -> (D) reachable
  HAVE     Real.cos_pi_div_five                                        -> used already,
           in `golden_quantum_dimension`
  MISSING  polylog / dilogarithm            0 modules
  MISSING  Lobachevsky                      0 modules      -> blocks (C)
  MISSING  Clausen                          0 modules      -> blocks (C)
  MISSING  Euler-Maclaurin                  0 modules      -> blocks (A)
  MISSING  Laplace method / stationary phase 0 modules     -> blocks (B)

So (D) is the only one of the four that Mathlib can currently support, and it is
the one the derivation needs least — it is a two-line change of variables. The
three that carry the actual content, (A), (B) and (C), have no Mathlib basis at
all.

## Why this is a real blocker and not laziness

(C) is the tractable entry point and is worth doing on its own merits:
`Lambda` is an elementary integral, `Lambda' = -log|2 sin|` is FTC, and
`Lambda'' = -cot` follows. It would also be reusable far beyond this corpus —
every hyperbolic-volume computation wants it.

(A) is the hard one. The `s_n` constant is what makes Lemma 3 true, what makes
`c_sigma(4_1) = 3^{-1/4}` come out rather than `3^{-1/4}` times an unknown, and
what the retracted van der Veen premise turned on. A leading-order
Euler-Maclaurin is not enough; the constant term is the entire content.

(B) is where the `sqrt(2 pi / |phi''|)` and hence the `|cot theta*|^{-1/2}` comes
from, i.e. the Hessian that cancels in `k`. Without it, `k_sq_eq_half_of_saddle`
is a theorem about a hypothesis rather than about the colored Jones polynomial.

## Mechanical guard — four duplicates in one session

Duplicated this session: `ohtsuki-takata-2015` (reference), `lawrence-zagier-1999`
(reference), the `[2]_zeta = phi` result (`bring_golden_jones_probe` rediscovering
`lr_modulus_identification_sigma235`), and this Lean file. Every one was
"I checked the external world and not the repo."

BEFORE adding anything, in this order:

    grep -n 'id: "<id>"' content/schema/references.ts     # and grep the TITLE too
    grep -rn "<concept>" --include=*.lean content/        # Lean already there?
    grep -rln "<concept>" computations/                   # probe already there?
    grep -n "<Module>" content/*/lean/QOU.lean            # already imported?

The last one is the cheapest and would have caught this file on its own:
`import QOU.Archimedean.LobachevskyDerivative` sits at line 289 of `QOU.lean`.

## Definition of done

Either (C) contributed upstream and (A) stated as a Lean hypothesis with a
citation rather than an inline assumption, or a written decision that the
analytic half stays informal — recorded here, with the reason. Do NOT quietly
leave the Lean reading as though it covers more than it does; the file header and
`prop:one-loop-prefactor-provenance` both say explicitly what is assumed, and
that must stay true.


## (A) DIAGNOSED — it is a structural change, not a tightening. 2026-08-08

Read `abs_deviation_le`'s actual construction before attempting it. It is built
from `sum_log_sin_le_integral_Icc` / `integral_le_sum_log_sin_Icc` — a
**rectangle-rule sandwich**: on each cell the monotonicity of `log(2 sin)`
brackets the sample by the integral. A rectangle rule has `O(h·Var)` error per
cell BY CONSTRUCTION; no sharpening of its constants reaches `O(h²)`.

So (A) is not "tighten `masterErr`". It needs:

  1. the TRAPEZOID / Euler-Maclaurin correction `(f(a)+f(b))/2` per cell — a
     different comparison, requiring `f''` control rather than monotonicity;
  2. separate treatment of the `j = 0` endpoint where `log(2 sin) -> -infinity`.
     That endpoint is where BOTH the `log N` and the `1/2` in the correction
     come from; it is the entire content, and it is why a leading-order EM is
     useless here.

Realistically a multi-day formalisation, not a sitting. Recorded so the next
attempt does not start by trying to improve constants.

## Landed toward (A): the exact endpoint constraint

`QOU/Knot/KashaevProdEndpoint.lean`, sorry-free, wired into `QOU.lean`:

    kashaev_factor_eq_sin_sq   2 - 2cos(2 pi j/N) = (2 sin(pi j/N))^2
    kashaevProd_endpoint       kashaevProd N (N-1) = N^2        EXACT, all N != 0
    sum_log_two_sin_endpoint   sum_{j=1}^{N-1} log(2 sin(j pi/N)) = log N

Numerically confirmed at N = 2,3,5,7,12,30. Built on
`QOU.MathlibExt.prod_two_sin_pi_div` (bean `qou-snpr`).

**Why it matters for (A).** Evaluate the target expansion at `k = N-1`:
`Lambda(pi) = 0` and `sin(pi(N-1)/N) = sin(pi/N)`, so it must return
`-(1/2) log(2 N sin(pi/N)) + O(1/N) = -log N + O(1/N)`. The theorem above says
that value EXACTLY, for every N, with no asymptotics. So it is a hard constraint
that pins the additive constant rather than evidence for it — and any candidate
refinement that fails it is wrong without further checking.

## (B) not started

Laplace's method for a sum. Mathlib has nothing (0 modules). Note it is needed
only through the specific `phi'' = -2 pi sqrt3 / N` at the figure-eight saddle,
so a bespoke version may be far cheaper than the general theorem — worth
scoping before attempting the general one.


## (B) SCOPED — Mathlib's Jacobi theta is the way in

(B) is needed only through one Gaussian sum. At the figure-eight saddle
`phi'' = -2 pi sqrt3 / N`, so what must be shown is

    sum_k exp(-a (k - c)^2) ~ sqrt(pi/a),      a = pi sqrt3 / N -> 0

Mathlib does NOT have this as such (`gaussianSum`, `tsum_exp_neg_mul_sq`:
absent from all 6990 oleans). But it HAS the object that gives it:

    NumberTheory/ModularForms/JacobiTheta/
      jacobiTheta              theta(tau) = sum_{n in Z} exp(pi i n^2 tau)
      jacobiTheta_S_smul       the S-transformation, theta(-1/tau) = sqrt(-i tau) theta(tau)
      jacobiTheta_eq_tsum_nat
      jacobiTheta_two_add

`jacobiTheta_S_smul` IS the Gaussian-sum asymptotic in disguise: along
`tau = i t`, `theta(i t) ~ 1/sqrt(t)` as `t -> 0+`, which is exactly
`sum_n exp(-pi n^2 t) ~ sqrt(pi/(pi t))`. So the `c = 0` (centred) case is
reachable from the modular transformation rather than from scratch.

**The offset is the open bit.** Our saddle sits at `k* = 5N/6`, not generally an
integer, so the sum is `sum_k exp(-a(k - c)^2)` with `c` non-integral — that is
the two-variable theta `theta_2(z, tau)`, and `jacobiTheta_two_add` suggests
some two-variable API exists. Scope that before writing anything: if the
characteristic version is present, (B) may be mostly assembly; if not, the
offset case has to be built.

This is materially cheaper than formalising general Laplace, which is what the
bean originally implied was needed. Nothing is built yet.


## (B) SOLVED ON PAPER — exact identity, Mathlib has every piece

The offset was NOT the open bit. `jacobiTheta₂_functional_equation` is stated
for ALL `z`, so the characteristic case is already there:

    jacobiTheta₂_functional_equation (z tau : C) :
      theta2 z tau = 1/(-I*tau)^(1/2) * exp(-pi*I*z^2/tau) * theta2 (z/tau) (-1/tau)

Instantiate at `tau = i a/pi` and `z = -i a c/pi`. Then `tau.im = a/pi > 0`,
`z/tau = -c`, `-1/tau = i pi/a`, `(-I tau)^(1/2) = (a/pi)^(1/2)`, and — the part
worth checking by hand — the exponential prefactor is `exp(a c^2)`, which
EXACTLY cancels the `exp(-a c^2)` produced by completing the square. Nothing is
left over. Result:

    sum_{k in Z} exp(-a (k-c)^2)  =  sqrt(pi/a) * theta2(-c, i pi/a)      EXACT

i.e. Poisson summation for the Gaussian, obtained from the theta functional
equation rather than from Poisson directly.

**Verified numerically to 1e-16** at (a,c) = (1,0), (1,0.3), (0.3,0.5),
(0.1,0.25), (0.02,0.8333), (0.005,0.8333) — including `c = 5/6`, the actual
figure-eight saddle offset.

**And the tail is exponentially small, not merely o(1).** `Im(i pi/a) = pi/a`,
so every `n != 0` term of `theta2(-c, i pi/a)` carries `exp(-pi^2 n^2/a)`:

    sum_k exp(-a(k-c)^2) = sqrt(pi/a) * (1 + O(exp(-pi^2/a)))

Numerically `sqrt(pi/a)` alone is already correct to 1e-16 at `a = 0.1`. At the
figure-eight saddle `a = pi sqrt3/N`, so the correction is
`O(exp(-pi N/sqrt3))` — utterly negligible, and far stronger than the `o(1)`
the Laplace step actually needs.

## What building (B) requires — concrete

  1. `Mathlib.NumberTheory.ModularForms.JacobiTheta.TwoVariable`:
     `jacobiTheta₂`, `jacobiTheta₂_functional_equation`,
     `hasSum_jacobiTheta₂_term`. `.../JacobiTheta/Bounds.olean` also exists and
     should supply the `n != 0` tail bound.
  2. Match the real sum `sum_k exp(-a(k-c)^2)` against
     `hasSum_jacobiTheta₂_term` — a real-to-complex tsum identification.
  3. Instantiate the functional equation and discharge the algebra above. The
     one fiddly part is the complex power `(-I*tau)^(1/2)` (`cpow`), which must
     be shown equal to `(a/pi)^(1/2)` on the positive imaginary axis.
  4. Bound the `n != 0` tail by `exp(-pi^2/a)` and conclude.

None of this is Laplace's method in general — it is one instantiation of an
existing Mathlib theorem plus bookkeeping. The bean's original framing ("no
Mathlib basis at all") was wrong for (B); it was right only for (A).

Not built. Step 3's `cpow` is the likely time sink.

## (B) BUILT — and a correction to this bean's own Mathlib claim

**CORRECTION FIRST.** The section "(B) SCOPED" above says

> Mathlib does NOT have this as such (`gaussianSum`, `tsum_exp_neg_mul_sq`:
> absent from all 6990 oleans).

That is wrong, and wrong in the way this bean has been wrong three times now: I
searched for two GUESSED NAMES and reported the absence of the names as the
absence of the theorem. Mathlib has it, under a name I did not guess:

    Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.lean
      Complex.tsum_exp_neg_quadratic (ha : 0 < a.re) (b : C) :
        sum' n:Z, cexp(-pi a n^2 + 2 pi b n)
          = 1/a^(1/2) * sum' n:Z, cexp(-pi/a (n + I b)^2)
      Complex.tsum_exp_neg_mul_int_sq
      Real.tsum_exp_neg_mul_int_sq

Specialising `a -> a/pi`, `b -> a c/pi` gives the identity below outright. So
(B) needed NO new analytic input from this repo — the correct statement is that
Mathlib had the transformation and lacked only the packaging.

**The mechanical guard, restated because it keeps earning its keep:** grep for
the STATEMENT SHAPE (`exp_neg`, `quadratic`, `PoissonSummation`), not for a
name you invented; and grep the directory, not the identifier.

**BUILT.** `QOU/MathlibExt/GaussianThetaSum.lean`, sorry-free, all seven
declarations on `[propext, Classical.choice, Quot.sound]`, wired at
`QOU.lean:336`:

    jacobiTheta2_term_gaussian                    the term identity
    im_I_mul_div_pi_pos                           i a/pi in the upper half plane
    hasSum_gaussian_theta_aux                     transported hasSum_jacobiTheta2_term
    jacobiTheta2_gaussian_functional_equation     the instantiation + the cpow
    hasSum_gaussian_theta                         <- the headline, in C
    tsum_gaussian_theta                           the tsum form
    hasSum_gaussian_theta_real                    the real form, over Z

        sum_{n in Z} e^{-a(n-c)^2} = sqrt(pi/a) . theta_2(-c, i pi/a)

exact, every `a > 0`, every real offset `c`. Step 3's `cpow` was indeed the
time sink, and went through `Complex.ofReal_cpow` + `Real.inv_rpow`.

Two things are better than a bare restatement of Mathlib's theorem:

  * it is a `HasSum`, not a `tsum`. Summability is carried rather than
    assumed, which is what the downstream tail-splitting needs.
  * it is in the theta normalisation, where `Im(i pi/a) = pi/a` makes the tail
    bound legible: `theta_2 = 1 + 2 sum_{n>=1} e^{-pi^2 n^2/a} cos(2 pi n c)`.

**WHAT IT CLOSES.** The sum -> integral step in the `c_sigma(4_1) = 3^{-1/4}`
derivation. `sqrt(pi/a)` IS the continuum integral, so
`sum/integral = 1 + O(e^{-pi^2/a})` uniformly in `c`. At the `4_1` saddle
`a = |phi''|/2 = pi sqrt3/N`, giving `sqrt(pi/a) = sqrt(N/sqrt3)` — exactly the
Laplace factor the tetrahedral probe uses — and error `e^{-pi N/sqrt3}`, about
`1e-79` at `N = 100`. The `O(1/N)` worry that would have sunk the constant is
off by an exponential. Measured `d log(deviation)/dN = -pi/sqrt3` to 18 digits.

Probe: `computations/probes/laplace_sum_theta_exactness_probe.py`, 4 assertions,
all pass.

**WHAT IT DOES NOT CLOSE.**

  * (A) is untouched, and is not reachable this way. `s_k`'s integrand is
    SINGULAR at the `j = 0` endpoint, Poisson summation does not apply, and
    the corrections there really are polynomial (`O(log N)`). The exact
    endpoint constraint is in `QOU/Knot/KashaevProdEndpoint.lean`.
  * The Gaussian APPROXIMATION of `phi` near the saddle. This file sums an
    exact Gaussian; the cubic-and-higher remainder of `phi` is a separate
    estimate and is still assumed.
  * (D), the multivariate complex-covariance Gaussian for the LINK side, is
    untouched. `hasSum_gaussian_theta` is one-dimensional and real-`a`.

Status: (B) done, (C) was already done in-repo, (A) and (D) open.

## (D) BUILT, and the higher remainder answered

**(D) — the multivariate complex-covariance Gaussian.**
`QOU/MathlibExt/GaussianShearIntegral.lean`, sorry-free on
`[propext, Classical.choice, Quot.sound]`, wired at `QOU.lean:337`:

    integral_cexp_two_pi_sq_shift     int_R e^{-2pi(v+s)^2} dv = 2^{-1/2}, any s
    integral_cexp_neg_pi_mul_div_two  int_R e^{-pi A u^2/2} du = (2/A)^{1/2}, Re A > 0
    integral_vdv_step4                2^{-n/2} (2/A)^{1/2}, every n

This was the last HYPOTHESIS under the link-side closed form. Everything in
`QOU/OneLoopPrefactorInvariance.lean` — `vdv_c_sigma_iff_tau`, `vdv_tau_sq`,
`vdv_radical_is_gaussian_norm` — is algebra downstream of this one integral,
and it is now proved rather than assumed.

Mathlib supplied both analytic inputs, so this was assembly:
`integral_gaussian_complex` (complex covariance, `0 < re b`) and
`integral_fintype_prod_volume_eq_pow`. The shift-independence of the transverse
integrals is the structural point — it is why the `n` transverse directions
contribute a bare `2^{-n/2}` and leave the `u`-integral one-dimensional.

**SCOPE, stated because the header does too.** The theorem is the ITERATED
integral `int_R du (int_{R^n} dv ...)`. Identifying it with the Bochner
integral over `R^{n+1}` is Fubini and needs joint integrability on the product
measure. NOT done. `volume_preserving_piFinSuccAbove` + `integral_prod` are the
pieces; the integrability proof is the work. Do not let a downstream header
claim the `R^{n+1}` form.

**THE HIGHER REMAINDER.** `GaussianThetaSum.lean` gained
`hasSum_gaussian_theta_tilt`:

    sum_k e^{-a(k-c)^2 + t(k-c)} = e^{t^2/4a} . sqrt(pi/a) . theta_2(-(c+t/2a), i pi/a)

Completing the square is a shift of `c`, so this is (B) with NO new analytic
input — and `e^{t^2/4a} sqrt(pi/a)` is exactly the continuum generating
function `int_R e^{-ax^2+tx} dx`. So the entire discrete-vs-continuum
discrepancy, at EVERY moment simultaneously, is the one factor
`theta_2 = 1 + O(e^{-pi^2/a})`, uniformly in `c` and `t`. Since the
cubic-and-higher remainder `R` enters only through moments (expand `e^R`), the
sum and the integral have the SAME asymptotic expansion at every order in
`1/N`. The worry that discretisation and the remainder could interact to make a
`1/N` term the continuum calculation misses is answered: they cannot.

**A NUMBER THAT MUST NOT BE MISQUOTED.** The `e^{-pi^2/a}` rate belongs to the
EXACT Gaussian. Measured on the real `4_1` cubic and quartic, the remainder
roughly HALVES the exponential rate:

    d(-log deviation)/dN  measured  0.8102     (model with real b3, b4)
    pure Gaussian pi/sqrt3          1.8138

still exponential — the only thing the one-loop constant needs — but not the
same constant. Recorded in the Lean header and in the probe.

Probe: `computations/probes/laplace_higher_remainder_probe.py`, 4 assertions,
all pass. Notable: `b3 sigma^3 ~ 0.04-0.11` and `b4 sigma^4 ~ 0.003-0.025` at
the tested `N`, so the remainder is NOT pointwise negligible and a `1/N`
sum-vs-integral difference was a live possibility a priori. On the real `4_1`
potential the residual is dominated by the ENDPOINT half-term, not the saddle:
`deviation / e^{-Vol N/2pi}` sits in `(1.60, 2.58)` across four doublings.

## Where the bean stands

  (A) OPEN. Euler-Maclaurin for `s_k` WITH its constant. Singular integrand at
      the `j = 0` endpoint, corrections genuinely polynomial (`O(log N)`).
      Exact endpoint constraint: `QOU/Knot/KashaevProdEndpoint.lean`.
  (B) DONE. `GaussianThetaSum.lean`.
  (C) was already done in-repo before this bean was written.
  (D) DONE. `GaussianShearIntegral.lean`, modulo the Fubini identification.

Still assumed downstream, and NOT covered by any of the above: a bound on the
actual sums rather than on their expansions (window + tail control), and the
integral's own `1/N` corrections.

## (A) HALVED — an exact reflection, and the 1/N term in closed form

Not closed. But it is no longer "a rectangle-rule sandwich one order too coarse,
multi-day, no handle". There is now an exact identity that constrains the whole
expansion, and the missing `1/N` term has been identified.

**THE REFLECTION.** `sin((N-j) pi/N) = sin(j pi/N)`, so for EVERY `k < N`

    L_k + L_{N-1-k} = log N,     L_k := -s_k = sum_{j=1}^k log(2 sin(j pi/N))

`QOU/Knot/FigureEightVolume.sum_log_two_sin_reflect`, sorry-free on
`[propext, Classical.choice, Quot.sound]`, together with the single-factor
`sin_pi_div_reflect`. Proof: split `Ico 1 N` at `k+1`, reflect the upper block
by `j -> N-j` (`Finset.sum_Ico_reflect`), and land on the endpoint value
`sum_log_two_sin_endpoint`. This is strictly stronger than the endpoint alone,
which only constrained `k = N-1`.

**WHAT IT BUYS — the symmetric half of (A) is a trapezoid remainder, exactly.**
Substituting `s_k = (N/pi) Lambda(th) - (1/2) log(2N sin th) + eps_k` with
`th = k pi/N`, `h = pi/N`, and using `Lambda(pi - x) = -Lambda(x)`, every term
cancels and the reflection collapses to

    eps_k + eps_{N-1-k} = (1/2)[f(th) + f(th+h)] - (1/h) int_th^{th+h} f

with `f = log(2 sin)` — the TRAPEZOID REMAINDER on one cell, as an IDENTITY, not
an estimate. Verified to working dps at 16 `(N,k)`; at `k = N/2` it quarters on
each doubling of `N` (ratio 4.0009, 4.0002, 4.0001), i.e. `O(1/N^2)` — already
sharper than the `O(1/N)` being claimed. So ALL of (A)'s difficulty is in the
antisymmetric half.

This also vindicates the earlier structural diagnosis in
`KashaevProdEndpoint.lean`: the missing ingredient really is the TRAPEZOID
correction `(f(a)+f(b))/2`, and the reflection exhibits it directly rather than
by analogy.

**AND THE ANTISYMMETRIC HALF HAS A CLOSED FORM.**

    eps_k = -(pi / 12 N) cot(theta) + O(1/N^3)

which is exactly the Euler-Maclaurin `B_2/2!` term `(h/12) f'`, `f' = cot`.
Measured at five `theta` over `N = 400, 800, 1600`: agreement to 7 digits, and
the residual of `N.eps` quarters on each doubling (so `eps`'s next correction is
`O(1/N^3)`, as even-order Euler-Maclaurin requires). It is odd about `pi/2` — as
the reflection forces — and at `theta = pi/2` it vanishes to `1e-69`.

So the refined expansion, measured but NOT proved, is

    s_k = (N/pi) Lambda(th) - (1/2) log(2 N sin th) - (pi/12N) cot(th) + O(1/N^3)

with NO leftover additive constant. That independently confirms the `2N` inside
the log — the correction to van der Veen's Lemma 3 recorded in
`docs/outreach/2026-08-08-van-der-veen-whitehead-chains-corrections.md`.

**WHAT IS STILL OPEN, PLAINLY.** Only the reflection is formalised. The
`-(pi/12N) cot` term is measured and is standard Euler-Maclaurin, but proving it
still needs the singular `j = 0` endpoint handled, and THAT is where the
`-(1/2) log N` and the additive constant come from — it needs Stirling, not
Euler-Maclaurin. The reflection does not reach it: it pairs `k` with `N-1-k`,
and both endpoints sit outside that pairing. Next concrete step is the endpoint,
not the interior.

Probe: `computations/probes/kashaev_reflection_probe.py`, 3 assertions, all pass.

## (A) — the trapezoid collapse PROVED, and the endpoint singularity removed

Two more pieces. (A) is still open, but the reason it is open has changed
completely: it is no longer blocked on a singularity.

**1. The trapezoid collapse is now a theorem, not a measurement.**
`QOU/Knot/KashaevReflectionTrapezoid.lean`:

    Lob_pi_sub               Lambda(pi - t) = -Lambda(t), from Cl_2_neg + Cl_2_add_two_pi
    integral_log_two_sin     int_a^b log(2 sin) = Lambda(a) - Lambda(b)   (FTC on hasDerivAt_Lob)
    kashaevLogSum / kashaevMainTerm / kashaevErr    the definitions
    kashaevErr_add_reflect   eps_k + eps_{N-1-k} = trapezoid remainder

The previous commit only MEASURED that the reflection collapses to a trapezoid
remainder. `kashaevErr_add_reflect` derives it: substitute the conjectured
expansion into `sum_log_two_sin_reflect`, apply `Lambda(pi-x) = -Lambda(x)` and
the fundamental theorem of calculus, and everything cancels. All three inputs
were already in this corpus — that is the point.

**2. The `j = 0` singularity is REMOVED, not estimated.**
`QOU/Knot/KashaevEndpointSplit.lean`:

    logSinc x := log(sin x) - log x
    logSinc_zero, logSinc_neg          regular at 0, and EVEN
    sum_log_two_sin_split
        sum_{j=1}^k log(2 sin(j pi/N)) = k log(2pi/N) + log(k!)
                                       + sum_{j=1}^k logSinc(j pi/N)

exact, every `N != 0`, every `k < N`. Subtract the singularity rather than
estimate it. The left side is singular termwise as `j/N -> 0`; the right side is
a closed form, a factorial, and a Riemann sum of a function continuous at `0`
and even (so no `h`-order endpoint term at the left end).

Measured (`kashaev_endpoint_split_probe.py`, 5 assertions, all pass):
the split is exact to 1e-68; the `logSinc` sum minus its Euler-Maclaurin
approximant is `O(h^3)` with `|.|.N^3 = 0.0222` flat to **1.0001x** across
`N = 100..800`; reassembly gives `s_k` to `O(1/N^3)` with `|.|.N^3 = 0.0669`
flat to 1.007x across `N = 400..1600`.

**THE CANCELLATION, and why Robbins is needed.** In the reassembly, Stirling's
`+1/(12k)` and the `-(h/12)(1/theta)` coming from `logSinc'(x) = cot x - 1/x`
cancel identically, leaving exactly the measured `-(pi/12N) cot theta`. Drop
either half and the residual is exactly `1/(12k)` — the probe exhibits this. So
the two halves are individually `O(1/N)` and only cancel together.

## The Mathlib gap for (A), now precisely two named items

  1. **Euler-Maclaurin summation** for a smooth function on a compact interval.
     Mathlib has `Polynomial.bernoulli` and `sum_range_pow_eq_bernoulli` but no
     summation formula.
  2. **Robbins' `1/(12n)` term of Stirling.** Mathlib's own docstring on
     `Real.Stirling.le_log_factorial_stirling` records the gap: "Sharper bounds
     due to Robbins are available, but are not yet formalised. These would add
     lower order terms (beginning with `(12 * n)^-1`)." Mathlib does have
     `le_log_factorial_stirling` (effective, one-sided) and
     `factorial_isEquivalent_stirling` (asymptotic).

With (1) alone the reassembly proves the `O(1/N)` form of (A). With (1)+(2) it
proves the `-(pi/12N) cot theta` refinement.

That is a materially different bean from the one written at the top of this
file, which said (A) needed "a structurally different comparison" and was
"multi-day, no handle". The comparison is identified, the singularity is gone,
and what is left is two standard library lemmas.

## Gap 2 of (A): Robbins' upper bound BUILT

`QOU/MathlibExt/StirlingRobbins.lean`, sorry-free on
`[propext, Classical.choice, Quot.sound]`, wired at `QOU.lean:340`:

    log_stirlingSeq_diff_le_robbins       log s(n+1) - log s(n+2) <= 1/(12(n+1)) - 1/(12(n+2))
    log_stirlingSeq_sub_le_robbins        the telescoped form, any n <= m
    log_stirlingSeq_sub_log_sqrt_pi_le    log s(n) - log sqrt(pi) <= 1/(12n)
    log_factorial_le_stirling_robbins     log n! <= n log n - n + (log n)/2
                                                    + log(2 pi)/2 + 1/(12n)

This is the term Mathlib's own docstring on `Stirling.le_log_factorial_stirling`
records as missing: "Sharper bounds due to Robbins are available, but are not
yet formalised. These would add lower order terms (beginning with `(12 * n)^-1`)
to the left hand side." The last theorem is the exact upper counterpart of that
lower bound.

**WHY IT COMES OUT WITH NO SLACK.** Mathlib already proves the series

    log s(n) - log s(n+1) = sum_{k>=0} (1/(2k+3)) x^{k+1},   x = 1/(2n+1)^2

Its existing consequence `log_stirlingSeq_diff_le_geo_sum` bounds every
coefficient by `1`. But the series starts at `k = 0` with coefficient `1/3`, so
every coefficient is `<= 1/3`, and

    (1/3) x/(1-x) = (1/3)/((2n+1)^2 - 1) = 1/(12n(n+1)) = 1/(12n) - 1/(12(n+1))

is an EQUALITY. The telescoping bound Robbins needs is not an estimate — it is
what the sharper coefficient bound gives directly. Then sum from `n` to infinity
against `tendsto_stirlingSeq_sqrt_pi`. Verified numerically: `(1/3)x/(1-x)`
against `1/(12n) - 1/(12(n+1))` agrees to |diff| = 0.0 at `n = 1`, and
`log n! - main` sits inside `(1/(12n+1), 1/(12n))` at every `n` tested.

**NOT A DUPLICATE** of `QOU/Mathlib/StirlingUpperBound.lean` (bean `el8w`),
which proves the CRUDE `n! <= e sqrt(n) (n/e)^n` by monotonicity from
`stirlingSeq 1`, for the Watson-uniqueness optimisation. Different constant,
different purpose; left in place, cross-referenced from the new file. Found by
grepping the repo before writing — the guard is working.

**WHAT IS STILL MISSING FROM GAP 2.** Robbins' matching LOWER refinement
`1/(12n+1) <= log s(n) - log sqrt(pi)`. Mathlib's `sqrt_pi_le_stirlingSeq` gives
only `0 <=`. Combined with the new upper bound that pins `log n!` to within
`1/(12n)` — enough for the `O(1/N)` form of (A), NOT enough for the
`-(pi/12N) cot theta` refinement, which needs both Robbins bounds (their gap is
`O(1/n^2) = o(1/N)`, which is why both are needed and neither alone suffices).

## (A) — where it stands now

    (i)   the exact reflection                       PROVED
    (ii)  symmetric half = trapezoid remainder       PROVED
    (iii) the j=0 singularity                        REMOVED (exact split)
    (iv)  Stirling, upper with Robbins' 1/(12n)      PROVED  <- this commit
    (v)   Stirling, lower with Robbins' 1/(12n+1)    open
    (vi)  Euler-Maclaurin for a smooth function      open

(vi) is the larger of the two remaining. (v) is a bounded follow-on to this
commit — the same series, minorised instead of majorised, which needs a
geometric lower bound on `1/(2k+3)` rather than the constant `1/3`.

## Gap 2 of (A): CLOSED — Robbins, both sides

`QOU/MathlibExt/StirlingRobbins.lean` now carries eight declarations, all
sorry-free on `[propext, Classical.choice, Quot.sound]`:

    log_stirlingSeq_diff_le_robbins / _ge_robbins     the telescoping steps
    log_stirlingSeq_sub_le_robbins  / _ge_robbins     telescoped over any range
    log_stirlingSeq_sub_log_sqrt_pi_le                <= 1/(12n)
    le_log_stirlingSeq_sub_log_sqrt_pi                >= 1/(12n+1)
    log_factorial_le_stirling_robbins                 log n! <= main + 1/(12n)
    le_log_factorial_stirling_robbins                 log n! >= main + 1/(12n+1)

with `main = n log n - n + (log n)/2 + log(2 pi)/2`. That is full Robbins.

**THE LOWER BOUND NEEDED NO SERIES ESTIMATE.** The terms are all nonnegative, so
the sum dominates its FIRST term `(1/3) x`, and that alone already beats the
telescoping gap:

    (1/3)/(2m+3)^2 >= 1/(12m+13) - 1/(12m+25)
      <=>  36(2m+3)^2 <= (12m+13)(12m+25)
      <=>  0 <= 24m + 1

true for every `m >= 0`, tight at `m = 0` where the sides differ by exactly `1`.
So `le_hasSum` plus polynomial algebra is the whole proof. The upper bound needed
the sharper coefficient bound `1/(2k+3) <= 1/3`; the lower needed only positivity.

The one genuinely new ingredient was the limit step: unlike the upper bound, the
telescoping here is not a constant bound on `log s`, so the argument shifts to
the antitone sequence `m -> log s(m+1) - 1/(12(m+1)+1)`, which has the same limit
`log sqrt(pi)` because the tail vanishes.

Verified independently at `n = 1..10000`: both bounds hold with the expected
slacks, and the gap `1/(12n) - 1/(12n+1)` is `O(1/n^2)` as needed.

## (A) — where it stands

    (i)   the exact reflection                       PROVED
    (ii)  symmetric half = trapezoid remainder       PROVED
    (iii) the j=0 singularity                        REMOVED (exact split)
    (iv)  Stirling upper, Robbins 1/(12n)            PROVED
    (v)   Stirling lower, Robbins 1/(12n+1)          PROVED
    (vi)  Euler-Maclaurin for a smooth function      OPEN  <- the only one left

(vi) is now the sole remaining blocker on (A), and it is not specific to this
problem: a general Euler-Maclaurin summation formula is simply absent from
Mathlib. What this corpus needs is the order-2 case for a `C^4` function on a
compact interval, applied to `logSinc`.
