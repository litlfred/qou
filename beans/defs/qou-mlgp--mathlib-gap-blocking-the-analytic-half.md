---
# qou-mlgp
title: The Mathlib gap that blocks formalising the analytic half of the c_sigma derivation
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
updated_at: 2026-09-26T11:03:28Z
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

## Mathlib infra added: the trapezoid rule (gap 1, first tranche)

`QOU/MathlibExt/TrapezoidRule.lean`, six declarations, all sorry-free on
`[propext, Classical.choice, Quot.sound]`, wired at `QOU.lean:341`:

    integral_weight                            int_a^b (x-a)(b-x) = (b-a)^3/6
    integral_eq_trapezoid_sub                  the EXACT error identity
    abs_trapezoid_sub_integral_le              |trap - int| <= (b-a)^3 M/12
    hasDerivAt_log_two_sin                     (log(2 sin))' = cos/sin
    hasDerivAt_cos_div_sin                     (cos/sin)' = -1/sin^2
    abs_trapezoid_sub_integral_log_two_sin_le  the instance (A) needs

**MATHLIB HAS NO QUADRATURE AT ALL.** Grepping the whole library for
`trapezoid`, `trapezium`, `quadrature`, Simpson: nothing. It has the FTC,
integration by parts and `Polynomial.bernoulli`, but no rule for approximating
an integral by samples and no error estimate for one. This is the first.

The identity:

    int_a^b f = ((b-a)/2)(f a + f b) - (1/2) int_a^b (x-a)(b-x) f''(x) dx

exact for every `f` in `C^2`. Peano-kernel form, kernel `(x-a)(b-x) >= 0`.

**PROVED WITH ONE FTC APPLICATION, not two integrations by parts.** With
`w = (x-a)(b-x)` (so `w(a) = w(b) = 0`, `w'' = -2`), the function `F := w f' - w' f`
has `F' = w f'' + 2f` because the two `w' f'` terms cancel. So
`int (w f'' + 2f) = F(b) - F(a) = (b-a)(f a + f b)`. Rearrange. That is the whole
proof — much shorter than the textbook route.

**WHAT IT CLOSES IN THIS BEAN.** `KashaevReflectionTrapezoid.lean` proved that
the reflection collapses `eps_k + eps_{N-1-k}` to exactly the trapezoid remainder
of `log(2 sin)` on one cell. The resulting `O(h^2)` BOUND was asserted in that
file's docstring and NOT proved, because nothing in Mathlib bounded a trapezoid
remainder. It is proved now. So the symmetric half of (A) is complete: identity
AND bound.

`(log(2 sin))'` and `(cos/sin)'` are also absent from Mathlib in this form;
both are proved here from the chain and quotient rules.

## (A) — where it stands

    (i)   the exact reflection                       PROVED
    (ii)  symmetric half = trapezoid remainder       PROVED (identity)
    (ii') symmetric half is O(h^2)                   PROVED (bound)  <- this commit
    (iii) the j=0 singularity                        REMOVED (exact split)
    (iv)  Stirling upper, Robbins 1/(12n)            PROVED
    (v)   Stirling lower, Robbins 1/(12n+1)          PROVED
    (vi)  Euler-Maclaurin, order 2, for logSinc      OPEN

(vi) is what remains. The trapezoid rule is the order-1 case of exactly that
machinery; the order-2 case adds the `(h/12)(f'(b) - f'(a))` correction with an
`O(h^5)` per-cell remainder, and the natural next step is the same Peano-kernel
argument one degree higher (kernel `(x-a)^2(b-x)^2`, four integrations by parts
or one FTC against a quartic `F`).

## Gap 1 CLOSED at the level (A) needs: the CORRECTED trapezoid rule

`QOU/MathlibExt/CorrectedTrapezoid.lean`, three declarations, all sorry-free on
`[propext, Classical.choice, Quot.sound]`, wired at `QOU.lean:342`:

    integral_weight_sq                        int (x-a)^2(b-x)^2 = (b-a)^5/30
    integral_eq_corrected_trapezoid_sub       the EXACT order-2 identity
    abs_corrected_trapezoid_sub_integral_le   |.| <= h^5 M/720 for |f''''| <= M

    int_a^b f = (h/2)(f a + f b) - (h^2/12)(f' b - f' a)
                  + (1/24) int_a^b (x-a)^2(b-x)^2 f''''(x) dx

exact for every `f` in `C^4`. The `-(h^2/12)(f' b - f' a)` term IS the
Euler-Maclaurin `B_2` correction, and it TELESCOPES on summing the cells — which
is precisely why (A)'s expansion has a `-(pi/12N) cot theta` term and nothing
else below `O(1/N^3)`.

**SAME ONE-FTC TRICK, ONE DEGREE UP.** Kernel `w = u^2(u-h)^2` (double roots at
both ends kill the first two boundary terms), and

    F := w f''' - w' f'' + w'' f' - w''' f     satisfies     F' = w f'''' - 24 f

every cross term cancelling against its neighbour. One FTC application gives
`F(b) - F(a) = 2h^2(f' b - f' a) - 12h(f a + f b)`; divide by 24. NO integration
by parts is performed, let alone four times. The textbook route is four
integrations by parts; this is one line of cancellation.

Verified numerically: identity to 1e-33 on `log(2 sin)` cells; the bound holds
with the right constant at three cells; `int (x-a)^2(b-x)^2 = h^5/30` exact.

**LEAN GOTCHA WORTH RECORDING.** `HasDerivAt.pow` returns a `Pi`-power
(`(fun y => y - a) ^ 2`), not a lambda, and `ring` cannot beta-reduce it —
`convert` then fails with an unsolved goal full of `((fun y => b - y) ^ 2) x`.
The fix is to ascribe each power to its lambda form in an intermediate `have`
before combining with `.mul`. Same trap will hit any future Peano-kernel work.

## (A) — every named analytic ingredient is now built

    (i)   the exact reflection                       PROVED
    (ii)  symmetric half = trapezoid remainder       PROVED (identity)
    (ii') symmetric half is O(h^2)                   PROVED (bound)
    (iii) the j=0 singularity                        REMOVED (exact split)
    (iv)  Stirling upper, Robbins 1/(12n)            PROVED
    (v)   Stirling lower, Robbins 1/(12n+1)          PROVED
    (vi)  order-2 Euler-Maclaurin cell rule          PROVED  <- this commit

What is left is ASSEMBLY, not analysis: sum the order-2 rule over the `k` cells
of `logSinc` (the `B_2` terms telescope), combine with `sum_log_two_sin_split`
and the Robbins bounds, and read off

    s_k = (N/pi) Lambda(th) - (1/2) log(2N sin th) - (pi/12N) cot(th) + O(1/N^3)

Every piece that assembly needs now exists in this corpus. That is a different
statement from "(A) is closed" — the assembly is real work and is not done — but
no missing lemma stands in front of it.

## Composite order-2 Euler-Maclaurin BUILT — and the one real gap left, named

`QOU/MathlibExt/CompositeEulerMaclaurin.lean`, sorry-free on
`[propext, Classical.choice, Quot.sound]`, wired at `QOU.lean:343`:

    abs_integral_sub_composite_le
      | int_a^{a+kh} g - [ h sum_{j=0}^{k} g(a+jh) - (h/2)(g a + g(a+kh))
                           - (h^2/12)(g'(a+kh) - g' a) ] |  <=  k h^5 M/720

Induction on `k`: the one-cell rule on `[a+kh, a+(k+1)h]` plus
`integral_add_adjacent_intervals`, with the residual at `k+1` splitting as
(inductive residual) + (cell residual) by a `ring` identity.

**THE POINT IS WHAT TELESCOPES.** `k` cells contribute `k` remainders but only
ONE correction term: the interior `B_2` terms cancel in pairs and only the two
endpoints survive. That is exactly why (A)'s expansion carries a lone
`-(pi/12N) cot theta` and nothing else below `O(1/N^3)`.

Verified numerically on `logSinc` over a uniform grid away from 0: residual
inside the bound at `k = 4, 8, 16, 32`, decaying like `h^4` (divides by 16 per
doubling).

## THE ONE REMAINING GAP, NAMED PRECISELY

Applying the composite rule to `logSinc x = log(sin x) - log x` on `[0, theta]`
needs `logSinc` to be `C^4` AT `x = 0`, and **it is not, as literally defined**.
Each of `log(sin x)` and `log x` is separately non-differentiable at `0`, even
though the difference extends analytically (`logSinc x = -x^2/6 + O(x^4)`).
Mathlib's convention `log 0 = 0` gives the right VALUE at `0`
(`logSinc_zero`) but NOT differentiability.

So the remaining step is: exhibit the analytic extension of `logSinc` at `0`,
and prove it agrees with `logSinc` on `(0, theta]`. Concretely one wants
`log (sin x / x)` with `sin x / x` extended by `1` at `0` — i.e. Mathlib's
`Real.sinc`-style construction, or a power-series argument.

That is a real piece of work and it is NOT done. It is, as far as this bean can
determine, the only thing left between this corpus and (A).

## (A) — the full ledger

    (i)   the exact reflection                       PROVED
    (ii)  symmetric half = trapezoid remainder       PROVED (identity)
    (ii') symmetric half is O(h^2)                   PROVED (bound)
    (iii) the j=0 singularity, subtracted            PROVED (exact split)
    (iv)  Stirling upper, Robbins 1/(12n)            PROVED
    (v)   Stirling lower, Robbins 1/(12n+1)          PROVED
    (vi)  order-2 Euler-Maclaurin, one cell          PROVED
    (vii) order-2 Euler-Maclaurin, composite         PROVED  <- this commit
    (viii) logSinc is C^4 at 0 (analytic extension)  OPEN    <- the only one

Note (viii) is a REGULARITY fact about one explicit function, not a missing
piece of general analysis. Every general tool the argument needs now exists.

## CORRECTION: (A) never needed `logSinc` to be C^4 at 0

The previous entry named "logSinc is C^4 at 0 (analytic extension)" as the ONLY
thing left. That was wrong — not about the mathematics, but about what (A)
needs. The requirement was an artefact of applying the composite rule on
`[0, theta]`. It disappears on `[h, theta]`.

**WHY.** The Kashaev sum is `sum_{j=1}^{k} logSinc(j h)` — it STARTS AT j = 1.
So `[h, theta]` with `k-1` cells is the natural interval and it never touches 0.
The cost is three left-endpoint terms:

    (1/h) int_0^h logSinc,     (1/2) logSinc(h),     (h/12) logSinc'(h)

and all three are `O(h^2) = O(1/N^2)` — one order BELOW the `O(1/N)` term being
chased. Measured at N = 100..800: about `-0.55/N^2`, `-0.82/N^2`, `-0.27/N^2`.
They do not enter the answer.

(Their leading parts also cancel exactly: with `logSinc x = -x^2/6 + O(x^4)` they
contribute `-h^2/18 + h^2/12 - h^2/36 = 0`, which is why the `[0,theta]` and
`[h,theta]` forms agree to `O(h^4)`.)

**WHAT IS ACTUALLY NEEDED** is two elementary bounds near 0, not regularity at 0.
`QOU/Knot/LogSincNearZero.lean`, sorry-free on
`[propext, Classical.choice, Quot.sound]`, wired at `QOU.lean:122`, proves the
first:

    logSinc_nonpos                 logSinc x <= 0            on (0, pi)
    neg_sq_div_three_le_logSinc    -(x^2/3) <= logSinc x     on (0, 1]
    abs_logSinc_le                 |logSinc x| <= x^2/3      on (0, 1]

from `Real.sin_lt`, `Real.sin_gt_sub_cube` and `Real.log_le_sub_one_of_pos`.
No analytic extension, no power series, no removable-singularity machinery.
The stale header on `CompositeEulerMaclaurin.lean` has been corrected in place
rather than left to mislead.

**STILL NEEDED:** `|logSinc' x| <= x` on `(0,1]`, equivalently
`|x cos x - sin x| <= x^2 sin x`. Both halves are one-line monotonicity
arguments — `u = sin x - x cos x` has `u(0) = 0`, `u' = x sin x > 0`;
`v = x^2 sin x - sin x + x cos x` has `v(0) = 0`, `v' = x(sin x + x cos x) > 0`
on `(0,1]` — via `strictMonoOn_of_deriv_pos`. Not formalised yet.

Note this bound is needed only to make `(h/12) logSinc'(h)` provably `o(h)`.
Mere boundedness of `logSinc'` is NOT enough (it would give `O(h)`, the same
order as the answer); what is needed is `logSinc'(x) -> 0` as `x -> 0+`, and
`|logSinc' x| <= x` is the cheapest clean way to say it.

## (A) — the ledger, corrected

    (i)-(vii)  as before                            PROVED
    (viii)     logSinc is C^4 at 0                  NOT NEEDED — retracted
    (ix)       |logSinc x| <= x^2/3 near 0          PROVED  <- this commit
    (x)        |logSinc' x| <= x near 0             OPEN — elementary, 2 monotonicities

## The derivative bound BUILT — (A)'s named ingredient list is now empty

`QOU/Knot/LogSincNearZero.lean` gained four more, all sorry-free on
`[propext, Classical.choice, Quot.sound]`:

    sin_sub_mul_cos_pos     0 < sin x - x cos x            on (0,1]
    sin_sub_mul_cos_lt      sin x - x cos x < x^2 sin x    on (0,1]
    hasDerivAt_logSinc      logSinc' x = cos x/sin x - 1/x on (0,pi)
    abs_logSinc_deriv_le    |logSinc' x| <= x              on (0,1]

Both monotonicity facts are `f(0) = 0` plus `f' > 0` via
`strictMonoOn_of_deriv_pos` on `Icc 0 1`:

    u = sin x - x cos x               u' = x sin x > 0
    v = x^2 sin x - sin x + x cos x   v' = x(sin x + x cos x) > 0

the second using `cos > 0` on `(0,1] subset (0, pi/2)`. Then
`logSinc' x = (x cos x - sin x)/(x sin x)`, `u > 0` opens the absolute value as
`sin x - x cos x`, and `v > 0` bounds it by `x^2 sin x`, so the quotient is
`< x`. Verified numerically at five `x` down to `0.01`.

**LEAN NOTES.** (i) `hasDerivAt_id` composes into `id`-wrapped forms that `ring`
treats as atoms — `simp only [id_eq]` before `ring`. Same species as the
`HasDerivAt.pow` Pi-power trap recorded earlier. (ii) `positivity` cannot use
hypotheses about variables: `0 < y * sin y` needs `mul_pos hy.1 hs`, not
`positivity`.

## (A) — the ledger, and what "assembly" now means

    (i)-(vii)  reflection, trapezoid identity + bound, the j=0 split,
               Robbins both sides, order-2 EM one-cell and composite   PROVED
    (viii)     logSinc is C^4 at 0                            RETRACTED, not needed
    (ix)       |logSinc x| <= x^2/3 near 0                             PROVED
    (x)        |logSinc' x| <= x near 0                                PROVED

Every analytic ingredient this bean ever named for (A) is now built and
sorry-free. What is left is the ASSEMBLY: instantiate the composite rule at
`g = logSinc`, `a = h`, `k-1` cells; add `sum_log_two_sin_split`; add the
Robbins bounds for `log(k!)`; collect the `h`-endpoint terms with (ix) and (x);
and read off

    s_k = (N/pi) Lambda(th) - (1/2) log(2N sin th) - (pi/12N) cot(th) + O(1/N^3)

That is bookkeeping over a dozen existing lemmas, plus `C^4` bounds on `logSinc`
in the INTERIOR `[h, theta]` (where it is manifestly smooth — no singularity —
but the fourth derivative still has to be exhibited and bounded, which is real
if unglamorous work). No missing idea remains.

## CORRECTION: the interior C^4 bound is NOT bookkeeping

The previous entry said the remaining assembly needs "`C^4` bounds on `logSinc`
in the INTERIOR `[h, theta]` (where it is manifestly smooth — no singularity —
but the fourth derivative still has to be exhibited and bounded, which is real
if unglamorous work)". The "unglamorous" understated it. Measured:

    logSinc''   = 1/x^2 - 1/sin^2 x                ->  -1/3    as x -> 0
    logSinc'''  = 2 cos x/sin^3 x - 2/x^3          ->   0
    logSinc'''' = 6/x^4 - (4cos^2 x + 2)/sin^4 x   ->  -2/15

(all three checked against numerical differentiation). Each is a DIFFERENCE OF
TWO TERMS THAT INDIVIDUALLY BLOW UP. At `N = 100` the crude `6/h^4` is `6.2e6`
while the true `|logSinc''''(h)|` is `0.1335` — a factor of **5e7**.

Why that matters: the composite EM error on the SUM is `k h^4 M/720 ~ M/N^3`,
so `M = O(1)` gives `O(1/N^3)` (fine) but the crude `M ~ 6/h^4 ~ N^4` gives
`O(N)` — no theorem at all. The bound therefore DEPENDS on the cancellation, and
proving it needs `sin`/`cos` expansions to eighth order with explicit
remainders. That is genuine analysis, not bookkeeping.

Checked that no cheaper route dodges it:
  * order-1 (plain trapezoid) composite: error on the sum is `k h^2 M''/12 =
    O(1/N)` — the SAME order as the `-(pi/12N) cot` term being extracted, so it
    cannot see the answer. Order 2 is genuinely required.
  * expressing the order-2 remainder via `g'''` instead of `g''''` lowers the
    requirement to `sup|logSinc'''|`, which is also bounded (-> 0) but needs a
    seventh-order cancellation. Cheaper, not cheap.
  * applying EM to `log(2 sin)` directly instead of `logSinc` makes it worse:
    there `M ~ 6/h^4` with NO cancellation, and the error diverges like `N`.

## What IS elementary, and is now proved

`QOU/Knot/LogSincNearZero.lean`, sorry-free on
`[propext, Classical.choice, Quot.sound]`:

    hasDerivAt_logSinc_deriv   logSinc'' x = 1/x^2 - 1/sin^2 x   on (0,pi)
    abs_logSinc_deriv2_le      |logSinc'' x| <= 1                on (0,1]

The bound is `logSinc'' = (sin^2 x - x^2)/(x^2 sin^2 x)` with
`x^2 - sin^2 x <= x^4/2` (from `sin x < x` and `sin x > x - x^3/4`) and
`x^2 sin^2 x >= 9x^4/16` (from `sin x >= 3x/4` on `(0,1]`), giving `<= 8/9`.
Same two `sin` bounds as the earlier results — no new machinery.

This is the second-derivative case of exactly the cancellation the fourth
derivative needs, done at the order where the algebra is still manageable. It is
the right template for the harder ones; it is not a substitute for them.

## (A) — honest ledger

    every previously named ingredient                          PROVED
    |logSinc''| <= 1 on (0,1]                                  PROVED <- this commit
    sup|logSinc''''| = O(1) on (0,theta]  (or |logSinc'''|)     OPEN, and it is
                                                               ANALYSIS, not
                                                               bookkeeping
    the final assembly, given that bound                       OPEN, bookkeeping

## The eighth-order cancellation is DODGEABLE: reduce the remainder to g''

`QOU/MathlibExt/CorrectedTrapezoid.lean` gained two, sorry-free on
`[propext, Classical.choice, Quot.sound]`:

    integral_weight_sq_deriv2        int_a^b w'' = 0
    integral_weight_sq_mul_deriv4_eq int_a^b w g4 = int_a^b w'' g2

with `w = (x-a)^2(b-x)^2` and `w'' = 12(x-a)^2 - 12(b-a)(x-a) + 2(b-a)^2`.

**WHY IT WORKS.** `w` has DOUBLE roots at both endpoints, so
`w(a)=w(b)=w'(a)=w'(b)=0` and two integrations by parts leave NO boundary terms
— one FTC application against `F := w g3 - w' g2`, the same trick as everywhere
else in this file. And `int w'' = 0` because `w'` vanishes at both ends.

**WHAT IT BUYS.** The `g4` form needs `sup|logSinc''''|`, whose finiteness rests
on an eighth-order cancellation (crude bound overshoots by 5e7 — see the
previous entry). The `g2` form needs only `logSinc''`, which is ALREADY PROVED
bounded here (`|logSinc''| <= 1` on `(0,1]`).

The zero mean is what makes it sharp enough. Writing the remainder as
`int w''(g'' - c)` with `c = g''(a)`:

    |remainder| <= (int|w''|) osc_cell(g'') <= 2h^3 osc_cell(g'')

and if `g''` is MONOTONE the per-cell oscillations TELESCOPE over the k cells to
`|g''(b) - g''(a)|` instead of accumulating as `k h sup|g'''|`. Composite error
on the sum becomes `(h^2/12) TV(g'') = O(1/N^2)`.

Verified: with `TV(logSinc'')` on `[h, 5pi/6]`, the bound / the `-(pi/12N)cot`
term is 0.064, 0.032, 0.016, 0.008 at N = 100, 200, 400, 800 — falling like
`1/N`, i.e. strictly below the answer, as required.

**THE REMAINING REQUIREMENT, REDUCED.** From "bound `logSinc''''`" (an
eighth-order cancellation of two blowing-up terms) to "`logSinc''` is monotone",
i.e. the SIGN condition `logSinc''' < 0`, i.e.

    x^3 cos x  <  sin^3 x      on (0, pi)

a single clean inequality (Adamovic-Mitrinovic type), verified numerically
across `(0, 5pi/6]`. For `x >= pi/2` it is trivial (LHS <= 0 < RHS). For
`x < pi/2` it needs `sin x > x - x^3/6`; Mathlib's `sin_gt_sub_cube` gives only
`x - x^3/4`, which is too weak — that is the concrete missing lemma.

## (A) — ledger

    every previously named ingredient                    PROVED
    |logSinc''| <= 1 on (0,1]                            PROVED
    int w g4 = int w'' g2,  int w'' = 0                  PROVED  <- this commit
    x^3 cos x < sin^3 x on (0,pi)   (monotonicity)       OPEN — one inequality,
                                                         needs sin x > x - x^3/6
    the final assembly                                   OPEN — bookkeeping

## The last inequality is PROVED — x^3 cos x < sin^3 x

`QOU/MathlibExt/SinCubeBounds.lean`, three declarations, all sorry-free on
`[propext, Classical.choice, Quot.sound]`, wired at `QOU.lean:345`:

    sub_cube_div_six_lt_sin                        x - x^3/6 < sin x      all x > 0
    cos_lt_one_sub_sq_div_two_add_pow_four_div_24  cos x < 1 - x^2/2 + x^4/24
    mul_cube_cos_lt_sin_cube                       x^3 cos x < sin^3 x    on (0, pi)

**ANOTHER GAP MATHLIB DOCUMENTS AND DOES NOT FILL.** `Trigonometric/Bounds.lean`
proves `sin_gt_sub_cube : x - x^3/4 < sin x` on `(0,1]`, and the comment right
above it says "the tighter inequality is `sin x > x - x^3/6` for all `x > 0`,
but this inequality has [a simpler proof]". The tighter form is supplied here,
for ALL `x > 0` with no upper restriction. Same species as the Robbins gap:
Mathlib names the sharper statement in prose and leaves it unformalised.

**THE LADDER** — three monotonicity steps, each `f(0) = 0` plus `f' > 0`, each
feeding the next:

    1. f = sin x - x + x^3/6         f' = cos x - 1 + x^2/2 > 0
       straight from Mathlib's one_sub_sq_div_two_lt_cos
    2. g = 1 - x^2/2 + x^4/24 - cos x   g' = sin x - x + x^3/6 = f > 0
       step 1 IS step 2's derivative positivity
    3. (1 - x^2/6)^3 = 1 - x^2/2 + x^4/12 - x^6/216 exceeds 1 - x^2/2 + x^4/24
       exactly when x^2 <= 9, so on (0, pi/2) step 2 gives cos x < (1-x^2/6)^3,
       hence x^3 cos x < (x - x^3/6)^3 < sin^3 x by step 1.
       For x >= pi/2 it is trivial: cos x <= 0 < sin^3 x.

Note step 1 needed no upper bound on `x` at all — `one_sub_sq_div_two_lt_cos`
holds for every `x != 0`, so `StrictMonoOn` on `Set.Ici 0` does the whole job.
That is why the result is stronger than Mathlib's on both counts (constant AND
range).

## (A) — every analytic requirement is now discharged

    reflection, trapezoid identity + bound, j=0 split, Robbins both sides,
    order-2 EM one-cell + composite, |logSinc| <= x^2/3, |logSinc'| <= x,
    |logSinc''| <= 1, int w g4 = int w'' g2, int w'' = 0,
    x^3 cos x < sin^3 x  (logSinc'' monotone)                        ALL PROVED

What remains is the ASSEMBLY and nothing else:
  * instantiate the composite rule at `g = logSinc`, `a = h`, `k-1` cells,
    with the `int w'' g''` remainder form and the telescoping oscillation bound;
  * add `sum_log_two_sin_split` and the Robbins bounds for `log(k!)`;
  * collect the three `h`-endpoint terms with `|logSinc| <= x^2/3` and
    `|logSinc'| <= x`;
  * read off `s_k = (N/pi)Lambda(th) - (1/2)log(2N sin th) - (pi/12N)cot(th)
    + O(1/N^2)`.

Two caveats worth keeping honest: the composite rule as proved takes the
remainder in `g4` form, so the assembly must route through
`integral_weight_sq_mul_deriv4_eq` by hand (a composite version with the `g''`
remainder and the telescoping bound is NOT yet stated as one theorem); and the
telescoping step itself — `sum of per-cell oscillations = TV` for a monotone
function — is not formalised either. Both are bookkeeping over existing pieces,
but they are bookkeeping that has not been done.

## The oscillation-driven cell bound: first of the two named bookkeeping pieces

`QOU/MathlibExt/CorrectedTrapezoid.lean` gained three more, all sorry-free on
`[propext, Classical.choice, Quot.sound]`:

    abs_weight_sq_deriv2_le                     |w''| <= 2(b-a)^2 on [a,b]
    abs_integral_weight_sq_deriv2_mul_le        |int w'' g''| <= 2(b-a)^3 D
                                                when |g'' - g''(a)| <= D
    abs_corrected_trapezoid_sub_integral_le_osc |trap - B2 - int| <= (b-a)^3 D/12

The last is the counterpart of `abs_corrected_trapezoid_sub_integral_le`, which
needs `sup|g''''|`. This one needs only how much `g''` MOVES across the cell —
an OSCILLATION, not a supremum — which is exactly what telescopes when `g''` is
monotone.

`|w''| <= 2(b-a)^2` because `w'' = 12u^2 - 12hu + 2h^2 = 12(u - h/2)^2 - h^2`
ranges over `[-h^2, 2h^2]` on `u in [0,h]`. And `int w'' = 0` is what lets `g''`
be replaced by `g'' - g''(a)` for free — the substitution that converts a sup
bound into an oscillation bound.

**LEAN NOTE.** `have hWint := hWc.intervalIntegrable` leaves the MEASURE a
metavariable (no expected type), and the failure surfaces far away as
"typeclass instance problem is stuck: IsLocallyFiniteMeasure ?m". Pin it with
`(mu := volume)` at the `have`. Three rounds were spent patching the wrong line
before reading the reported line number properly.

## (A) — what is left

    every analytic requirement                                       PROVED
    the oscillation-driven cell bound                                PROVED <- this commit
    composite version carrying the oscillation bound + telescoping   OPEN
    the final assembly                                               OPEN

The remaining composite piece is: redo `abs_integral_sub_composite_le`'s
induction with `abs_corrected_trapezoid_sub_integral_le_osc` in place of the
`g''''` bound, and sum the per-cell oscillations of a monotone `g''` by
`Finset.sum_range_sub` telescoping to `|g''(b) - g''(a)|`. Structurally
identical to the induction already proved; not yet written.

## Both named bookkeeping pieces are now DONE

`QOU/MathlibExt/CompositeEulerMaclaurin.lean`:

    abs_integral_sub_composite_le_osc
      | int_a^{a+kh} g - [ h sum_{j=0}^{k} g(a+jh) - (h/2)(g a + g(a+kh))
                           - (h^2/12)(g1(a+kh) - g1 a) ] |
        <= (h^3/12) (g2 a - g2(a+kh))     for g2 = g'' ANTITONE

sorry-free on `[propext, Classical.choice, Quot.sound]`.

**THE RIGHT-HAND SIDE DOES NOT GROW WITH k.** Against the `g''''` version's
`k h^5 sup|g''''|/720`, this is `h^3 TV(g'')/12` with no factor of `k` at all.
On the sum (divide by `h`) that is `O(h^2) = O(1/N^2)`, below the `O(1/N)` term
(A) extracts — and it needs only `logSinc''`, which is bounded AND monotone
(`mul_cube_cos_lt_sin_cube`), instead of `logSinc''''`.

**THE TELESCOPING NEEDED NO SUMMATION LEMMA.** For antitone `g''` the per-cell
oscillation on `[A,B]` is exactly `g''(A) - g''(B)`, and the induction's
arithmetic does the rest: the inductive `h^3/12 (g'' a - g'' A)` plus the new
cell's `h^3/12 (g'' A - g'' B)` add to `h^3/12 (g'' a - g'' B)`. The
`Finset.sum_range_sub` step anticipated in the previous entry turned out to be
unnecessary.

## (A) — every general piece exists; what is left is the instantiation

    all analytic requirements                              PROVED
    oscillation cell bound                                 PROVED
    composite rule with oscillation + telescoping          PROVED  <- this commit

What remains is ONE instantiation, with no general lemma missing:

  * apply `abs_integral_sub_composite_le_osc` at `g = logSinc`, `a = h`,
    `k-1` cells, using `mul_cube_cos_lt_sin_cube` for `AntitoneOn logSinc''`
    and `hasDerivAt_logSinc` / `hasDerivAt_logSinc_deriv` for the derivative
    hypotheses (the `g3`, `g4` hypotheses are still required by the statement
    even though the BOUND no longer mentions them — supplying them for logSinc
    on the interior is routine but not yet written);
  * add `sum_log_two_sin_split` and the Robbins bounds for `log(k!)`;
  * collect the three `h`-endpoint terms via `abs_logSinc_le` and
    `abs_logSinc_deriv_le`;
  * conclude
    `s_k = (N/pi)Lambda(th) - (1/2)log(2N sin th) - (pi/12N)cot(th) + O(1/N^2)`.

One wrinkle worth naming: `abs_integral_sub_composite_le_osc` still takes `g3`
and `g4` derivative hypotheses, inherited from the cell rule's proof even though
its conclusion no longer mentions them. For `logSinc` those are
`logSinc'''` and `logSinc''''` — which exist and are smooth on the interior
`[h, theta]`, so this is not the eighth-order cancellation problem returning; it
is just more derivative bookkeeping than the statement suggests. A cleaner
version would weaken the hypotheses to `C^2` plus integrability.

## The g3/g4 wrinkle removed: order-2 is a REWRITING of order-1

The previous entry flagged that `abs_integral_sub_composite_le_osc` still
demanded `g3` and `g4` hypotheses inherited from the quartic-kernel proof, even
though its conclusion no longer mentioned them — meaning the instantiation at
`logSinc` would have needed `logSinc'''` and `logSinc''''` after all. That is
now gone.

`QOU/MathlibExt/CorrectedTrapezoid.lean`:

    integral_eq_corrected_trapezoid_sub_deriv2
      int_a^b g = (h/2)(g a + g b) - (h^2/12)(g1 b - g1 a) + (1/24) int w'' g2

sorry-free, with NO `g'''` or `g''''` hypotheses. The kernel identity

    w'' = 12(x-a)^2 - 12(b-a)(x-a) + 2(b-a)^2 = -12 (x-a)(b-x) + 2(b-a)^2

expresses `w''` through the ORDER-1 kernel, so

    (1/24) int w'' g2 = -(1/2) int (x-a)(b-x) g2 + ((b-a)^2/12)(g1 b - g1 a)

by the FTC on `g2`; substituting into `integral_eq_trapezoid_sub` the `B_2`
terms cancel exactly and the order-1 identity is recovered. **The order-2 rule
is a rewriting of the order-1 rule, not a deeper theorem** — and it inherits the
order-1 rule's `C^2` hypotheses.

Both `abs_corrected_trapezoid_sub_integral_le_osc` and
`abs_integral_sub_composite_le_osc` are re-proved on that basis. The composite
signature is now exactly:

    0 < h -> (k : N)
      -> (forall x in Icc a (a+kh), HasDerivAt g  (g1 x) x)
      -> (forall x in Icc a (a+kh), HasDerivAt g1 (g2 x) x)
      -> ContinuousOn g2 (Icc a (a+kh))
      -> AntitoneOn   g2 (Icc a (a+kh))
      -> |int - [composite trapezoid + B_2]| <= (h^3/12)(g2 a - g2 (a+kh))

`C^2` plus monotonicity of `g''`. Nothing else.

## (A) — the instantiation is now exactly discharged by what exists

Every hypothesis of the composite rule is available for `logSinc` on `[h, theta]`:

    HasDerivAt logSinc  (logSinc' x)  x     hasDerivAt_logSinc
    HasDerivAt logSinc' (logSinc'' x) x     hasDerivAt_logSinc_deriv
    ContinuousOn logSinc''                  from the above
    AntitoneOn logSinc''                    mul_cube_cos_lt_sin_cube

Remaining: assemble — apply the composite rule, add `sum_log_two_sin_split` and
the Robbins bounds, collect the three `h`-endpoint terms with `abs_logSinc_le`
and `abs_logSinc_deriv_le`. The `AntitoneOn` instance still needs deriving from
the sign of `logSinc'''` via `antitoneOn_of_deriv_nonpos`, which requires
`HasDerivAt logSinc'' (logSinc''' x) x` — the ONE derivative statement still
unwritten, and it is a routine quotient-rule computation on `1/x^2 - 1/sin^2 x`,
not a cancellation estimate.

## `AntitoneOn logSinc''` — the composite rule's last hypothesis, discharged

`QOU/Knot/LogSincNearZero.lean`, two more, sorry-free on
`[propext, Classical.choice, Quot.sound]`:

    hasDerivAt_logSinc_deriv2   logSinc''' x = -2/x^3 + 2 cos x/sin^3 x   on (0,pi)
    antitoneOn_logSinc_deriv    AntitoneOn logSinc'' (Icc c d)  for 0 < c, d < pi

The derivative is the quotient rule twice (`(1/x^2)' = -2/x^3` and
`(1/sin^2 x)' = -2 cos x/sin^3 x`, both via `HasDerivAt.inv`). Antitonicity is
`antitoneOn_of_deriv_nonpos`, whose derivative condition
`2 cos x/sin^3 x <= 2/x^3` is exactly `x^3 cos x <= sin^3 x` after
`div_le_div_iff` — i.e. `mul_cube_cos_lt_sin_cube` from the previous round.

**EVERY HYPOTHESIS of `abs_integral_sub_composite_le_osc` is now available for
`logSinc` on any `[c,d]` inside `(0, pi)`:**

    HasDerivAt logSinc  (logSinc' x)  x    hasDerivAt_logSinc
    HasDerivAt logSinc' (logSinc'' x) x    hasDerivAt_logSinc_deriv
    ContinuousOn logSinc''                 from hasDerivAt_logSinc_deriv2
    AntitoneOn   logSinc''                 antitoneOn_logSinc_deriv

## (A) — what is genuinely left

Only the assembly, and it is now a matter of plugging in:

  1. `abs_integral_sub_composite_le_osc` at `g = logSinc`, `a = h`, `k-1` cells
     -> `sum_{j=1}^{k} logSinc(jh)` against `(1/h) int_h^theta logSinc` plus the
     `B_2` term, with error `<= (h^3/12)(logSinc''(h) - logSinc''(theta))`,
     which is `O(h^3)` and so `O(1/N^2)` on the sum;
  2. `sum_log_two_sin_split` to convert that into `s_k`;
  3. the Robbins bounds for `log(k!)`;
  4. `abs_logSinc_le` and `abs_logSinc_deriv_le` for the three `h`-endpoint
     terms, all `O(h^2)`;
  5. conclude
     `s_k = (N/pi)Lambda(th) - (1/2)log(2N sin th) - (pi/12N)cot(th) + O(1/N^2)`.

Steps 1-4 all cite theorems that exist and are sorry-free. Step 5 is arithmetic
over them. Nothing in the chain is now an open mathematical question -- which is
a different claim from "it is done", and the assembly is still unwritten.

## (A) IS CLOSED — the assembly, with an explicit `O(1/N^2)` constant

`QOU/Knot/KashaevAsymptotic.lean::kashaev_log_sum_asymptotic`, sorry-free on
`[propext, Classical.choice, Quot.sound]`. For `1 <= k < N`, `4 <= N`,
`h = pi/N`, `theta = k pi/N`:

    | sum_{j=1}^{k} log(2 sin(j pi/N))
        - ( -(N/pi) Lambda(theta) + (1/2) log(2 N sin theta)
            + (pi/12N) cot theta ) |
      <= 1/(144 k^2) + (7/12) h^2 + h^2/(12 sin^2 theta)

equivalently `s_k = (N/pi)Lambda(theta) - (1/2)log(2N sin theta)
- (pi/12N)cot(theta) + O(1/N^2)`. The bean asked for `O(log N) -> O(1)`; this
is `O(1/N^2)`, and the constant `-(1/2)log(2N sin theta)` is DERIVED.

### The one genuinely new ingredient: `Lambda` near zero WITH its constant

`QOU/Knot/LobNearZero.lean::abs_Lob_sub_near_zero`:

    |Lambda(b) - (b - b log(2b))| <= b^3/3      for 0 < b <= 1

Everything else in the chain was bookkeeping over pieces already built; this
is where `-(1/2)log(2N sin theta)` comes from, and it is what "(A) needs the
constant, not the rate" always meant. `(1/h)*Lambda(h)` is `O(1/h)`, so
anything short of the exact constant destroys the answer.

The proof does not assume any expansion of `Lambda`. For `0 < eps <= b < pi`,
`Lambda' = -log(2 sin)` gives

    Lambda(eps) - Lambda(b) = int_eps^b logSinc + int_eps^b log(2t)

splitting the integrand at its own singularity: `logSinc` is bounded
(`|logSinc t| <= t^2/3`) and `log(2t)` integrates in closed form. Letting
`eps -> 0+` kills the `eps` bracket. That limit needed two things the corpus
did not have:

  * `continuous_Cl_2` -- `Cl_2` is continuous, Weierstrass M-test on the
    Fourier series (`|sin(n th)/n^2| <= 1/n^2`, uniform in `th`). The corpus
    had `summable_clausen` but never continuity.
  * `Real.continuous_mul_log` for `eps log(2 eps) -> 0` (Mathlib had it).

### How the five error terms land

Exact decomposition (checked to 1e-59 in
`computations/probes/kashaev_assembly_bound_probe.py`):

    L_k - target = (rho - 1/12k) + delta/h + logSinc(h)/2
                   - (h/12)(cot h - 1/h) + E

    rho - 1/12k       Robbins BOTH sides       <= 1/(144 k^2)
    delta/h           Lambda near zero          <= h^2/3
    logSinc(h)/2      trapezoid h-endpoint      <= h^2/6
    (h/12)(cot h-1/h) B_2 h-endpoint            <= h^2/12
    E                 composite Euler-Maclaurin <= h^2/(12 sin^2 theta)

Two cancellations do the real work and neither is optional:

  1. `h log(2h)` from `Lambda(h)` against `h log(2h)` from `int log(2t)` --
     this is why the CONSTANT and not the rate is what (A) needed.
  2. `1/(12k)` from Robbins against `(h/12)*(1/theta)` from the `B_2` term at
     the `theta` end. This is why the one-sided Robbins bound is useless here:
     `1/(12k)` is exactly the size of the term it cancels, so only the
     two-sided bracket `1/(12k+1) <= rho <= 1/(12k)` leaves an `O(1/k^2)`
     residue. `le_log_factorial_stirling_robbins` earning its place.

### The singular `j = 0` endpoint is never approximated

`sum_log_two_sin_split` removes it EXACTLY -- `sum log(2 sin jh) = k log(2h) +
log k! + sum logSinc(jh)` -- handing the singular part to Stirling and leaving
Euler-Maclaurin a bounded smooth summand. Nothing is expanded through
`log(2 sin) -> -infty`. The earlier note in `KashaevReflectionTrapezoid.lean`
that "the antisymmetric half needs the singular endpoint" is superseded: the
split dodges it rather than solving it.

### Sharpness, stated honestly

The proved bound is `O(1/N^2)`; the true residual is `O(1/N^3)`
(residual*N^2 halves per doubling of N, probe part (ii)). The proof does not
exploit the parity that gives the extra order, and the constant is loose by
50x-20000x over the tested range. Both are fine for the use -- the point was
the constant term, not the remainder's sharpness -- but "O(1/N^2), explicit"
is the claim, not "sharp".

### Files added this round

    QOU/Knot/LobNearZero.lean         continuous_Cl_2, continuous_Lob,
                                      log_two_sin_eq_logSinc_add,
                                      integral_log_two_mul, continuousOn_logSinc,
                                      integral_logSinc_eq, abs_Lob_sub_near_zero
    QOU/Knot/KashaevAsymptotic.lean   abs_robbins_centred,
                                      kashaev_log_sum_asymptotic
    computations/probes/kashaev_assembly_bound_probe.py

### Lean gotchas recorded

  * `intervalIntegrable_log'` (unconditional, volume-only) lives in
    `Mathlib.Analysis.SpecialFunctions.Integrability.Basic` and is in the
    `intervalIntegral` namespace -- importing `Integrals.Basic` is not enough.
  * `Nat.cast (m+1)` and `(m:R)+1` are DIFFERENT ATOMS to `ring`. A single
    `simp only [hcast]` with `hcast : ((m+1:N):R) = (m:R)+1`, applied to the
    goal AND to every imported lemma instance, is what makes the final
    `field_simp; ring` go through. Without it `ring` fails on an identity that
    is numerically exact to 1e-59.
  * `abs_of_nonpos (by positivity : -(1/h) <= 0)` does not work -- `positivity`
    proves positivity, not nonpositivity. `abs_neg` then `abs_of_pos`.

## Bean status: (A) (B) (C) (D) all closed. What this bean does NOT close.

All four analytic gaps this bean opened with are now machine-checked in-repo:

    (A) Euler-Maclaurin for s_k WITH the constant   kashaev_log_sum_asymptotic
    (B) Laplace's method for a sum                  hasSum_gaussian_theta{,_tilt}
    (C) Lobachevsky function and derivatives        was already in-repo
    (D) multivariate Gaussian, complex covariance   integral_vdv_step4

The bean's own "Definition of done" asked for something weaker -- "(A) stated as
a Lean hypothesis with a citation" -- and also demanded, correctly, that the
Lean reading never cover more than it does. That clause now cuts the OTHER way:
`OneLoopPrefactorInvariance.lean` and `one-loop-prefactor-provenance.md` both
said the analytic input "is not formalised / Mathlib has no usable form", which
UNDERSTATES as of today. Both updated in the same commit.

**The gap that replaces it, stated exactly.** `hc` and `hτ` in
`OneLoopPrefactorInvariance` are still hypotheses. Nobody has derived them from
the four theorems above -- feeding the expansion into the theta identity,
extracting the saddle condition, the Stirling factor and the Hessian. That is a
different task from this bean's: it is assembly of formalised pieces, not a
search for missing analysis, and it should get its own bean rather than keeping
this one open. Do not read "the analytic gaps are closed" as "c_sigma(4_1) =
3^{-1/4} is formalised end to end". It is not.
