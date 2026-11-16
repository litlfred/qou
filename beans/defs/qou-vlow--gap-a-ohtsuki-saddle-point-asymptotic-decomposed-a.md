---
# qou-vlow
title: 'GAP (A): Ohtsuki saddle-point asymptotic -- decomposed, and NOT out of reach'
status: in-progress
pr: 8220
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-31T04:01:44Z
updated_at: 2026-10-04T15:19:27Z
parent: qou-r9ih
---


## ROAST of my own claim: "(A) is Ohtsuki's steepest descent, out of reach"

I ended the previous turn recommending we stop on the `5₂` lane because `(A)` was
"out of reach". **I did not check before saying it.** Measured now, the claim is
wrong in three separate ways, and one of them is embarrassing: the corpus
already contains pieces of Ohtsuki's own argument.

### What "out of reach" should have meant, and what is actually true

**1. "Mathlib has no saddle-point method" — TRUE, and this is the only part
that survived.** At the pinned rev `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`,
`grep -rl "Laplace method|stationary phase|steepest descent|saddle point"` over
all of `Mathlib/` returns **zero files**. `Mathlib/Analysis/SpecialFunctions/Stirling.lean`
exists but proves Stirling by the **Wallis product**, not by Laplace's method —
so it is not the seed either. `Mathlib/Analysis/Asymptotics/` supplies the
*language* (`IsBigO`, `IsLittleO`, `IsTheta`, `AsymptoticEquivalent`) and none
of the *methods*.

**2. "Therefore out of reach" — DOES NOT FOLLOW.** Ohtsuki's §3 toolkit rests on
things Mathlib *does* have. Proposition 3.1 — the one everything else is built
on — is:

> for `a ≠ 0` complex and `C` a path between the two components of
> `{Re(az²) < 0}`,  `∫_C e^{Naz²} dz = √π/(√a·√N) + O(e^{−εN})`.

Its proof, in the paper, is: rescale `z ↦ z/√a` to reduce to `a = −1`, quote
`∫_ℝ e^{−Nz²} = √π/√N`, and bound two tails by `O(e^{−εN})`. Mathlib has the
Gaussian (`integral_gaussian`, `integral_gaussian_complex` for `0 < re b`,
`integral_gaussian_complex_Ioi`) and it has contour deformation. **Prop 3.1 is a
formalizable, self-contained Mathlib-gap contribution**, and it is the seed of
the whole missing subject area. Saying "out of reach" skipped over a brick I
could have named.

**3. "The corpus has nothing on this" — FALSE. It has two substantial pieces.**

* `QOU/QBeta/FiveTwoOhtsukiCriticalPoint.lean` (bean `qou-thmb`) **proves**
  that Ohtsuki's critical-point system `(1−x)y = 1`, `x(y−1)² = 1` eliminates to
  `x³ = (1−x)²`, which is the corpus's own `5₂` saddle cubic under `x = 1−y`.
  Polynomial, over any `CommRing`, no analysis. That is §5's critical point,
  done.
* `QOU/MathlibExt/GaussianThetaSum.lean` (bean `qou-mlgp` (B)) proves
  `∑_{n∈ℤ} e^{−a(n−c)²} = √(π/a)·θ₂(−c, iπ/a)` from the Jacobi theta functional
  equation, hence **sum = integral × (1 + O(e^{−π²/a}))** — the discrete-to-
  continuum replacement with *exponentially* small error, uniformly in the
  lattice offset `c`. That is the content §4's Poisson summation is used for.
* Faddeev's quantum dilogarithm has its own cluster:
  `MathlibExt/FaddeevQuantumDilogarithm.lean`, `FaddeevPhiBRealIntegral.lean`,
  `QuantumDilogarithmInfinite.lean`, `PhiBProd.lean`, `PhiBFibreExtension.lean`.

And as of today the analytic identity at the critical point is also a theorem:
`FiveTwoOhtsukiBridge.ohtsuki_sum_im_eq_three_blochWigner` proves
`Im V̂(critical point) = 3·D(y₀)` sorry-free, instantiated at the corpus's own
`cLiTwoExt`.

### The honest verdict

Not "out of reach". **Out of budget, for a reason that is scale plus one missing
Mathlib subject area** — and it is decomposable, which "out of reach" hid.

### What is actually hard, measured

Of the 5058 extracted lines of `library/ki52`, **1412 (28 %)** are §5.3 and §5.4
— *verifying the hypotheses* of the saddle-point method and of Poisson summation
for the specific two-variable potential `V̂(t,s)`. §5.3 says outright that its
arguments are due to Yokota [44]. This is concrete real-analytic estimate work
on a specific function, which is the single most expensive kind of Lean
formalization per page. Plus Appendix B (uniform convergence `V → V̂`), which is
where Faddeev-quantum-dilogarithm asymptotics enters.

### Two real limitations, so the decomposition is not flattered

* `GaussianThetaSum` is stated for **real** `a > 0` (`(a c : ℝ) (ha : 0 < a)`).
  Ohtsuki's saddle is **complex**, with a rotated contour. So the corpus has the
  `4₁`-flavoured real-Laplace case, not the complex-saddle case that §3 needs.
  Bridging that is real work, not a restatement.
* Props 3.2, 3.4, 3.5 — the perturbative Gaussian carrying the *full* asymptotic
  expansion, and its multi-variable form — are what produce the `N^{3/2}` and the
  `ω` prefactor in `OhtsukiAsymptotic`. Nothing in the corpus touches them.

### Suggested first brick, if this is ever picked up

Proposition 3.1 in `QOU/MathlibExt/`, stated for complex `a`, off
`integral_gaussian_complex` plus two `O(e^{−εN})` tail bounds. It is the only
piece that is (i) self-contained, (ii) a genuine Mathlib gap, and (iii) needed by
every later proposition. Do **not** start from §5.3.


## Progress Update (2026-11-16T22:11:55Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/DilogPartBJointAndOhtsukiSaddleBrick.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/dilog-part-b-joint-and-ohtsuki-saddle-brick.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8220 (`4fed1eb1d2c9f99be67799649865fd4f3ddd3d6a`); keeping `status: in-progress` until PR merges.
