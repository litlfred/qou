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
