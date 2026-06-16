# `conj:dilogarithm-archimedean-limit` — the convergence-regime half is elementary

**Date:** 2026-06-07
**Block:** [`conj:dilogarithm-archimedean-limit`](../../content/quantum-observable-universe/mass-theory/dilogarithm-archimedean-limit.md)
**Keystone:** root of the dilog cluster (unblocks `borromean-bloch-group-element`, `phi-q-wkb-greens-function`, `algebraic-geometric-dilog-equivalence`).

## Result

The conjecture
$$
\lim_{\substack{q\to 1^-,\; n\to\infty\\ n|1-q|\to\infty}} (1-q)\log\Phi_n(x;q) = \mathrm{Li}_2(x)
$$
splits cleanly into two halves of very different difficulty:

- **Part A — the convergence regime $q\to 1^-$, fixed $x\in(0,1)$ — is
  ELEMENTARY.** It is a monotone left-Riemann-sum limit plus an
  exponential tail bound and the factor $(1-q)/\hbar\to 1$. It needs
  **no Tauberian theorem and no branch-cut analysis** — the poles of
  $\Phi_n$ are never approached, because $1-xq^k \ge 1-x > 0$ for every
  $k$ when $0<x<1$ and $0<q<1$. It is moreover **uniform on compact
  subsets of $(0,1)$**, which is exactly the conjecture's gap (1).

- **Part B — the substrate continuation $q\to 1^+$ (to $q_0\approx 1.11$)
  and uniformity as $x\to 1^-$ — is the genuine open content.** Here the
  factors $1-xq^k$ can vanish (the algebraic poles of $\Phi_n$ approach
  the $\mathrm{Li}_2$ branch cut $[1,\infty)$), and the Riemann-sum error
  bound $\le \hbar f(0)=\hbar\,(-\log(1-x))$ degrades as $x\to 1^-$.
  This is the conjecture's gap (2) (branch-cut compatibility) and is
  where the Frobenius-pairing pole cancellation against a fixed $T_w$
  must do real work.

This **resolves gap (1)** of the block's "Why it is conjectural" list
and isolates the open content to gaps (2)–(3).

## Proof of Part A

Fix $x\in(0,1)$. Write $q=e^{-\hbar}$, $\hbar>0$, so $q\in(0,1)$, and put
$$
f(s) := -\log\bigl(1-x e^{-s}\bigr),\qquad s\in[0,\infty).
$$

**(i) $f$ is positive, bounded, continuous, decreasing, with
$\int_0^\infty f = \mathrm{Li}_2(x)$.**
For $s\ge 0$ we have $xe^{-s}\in(0,x]\subset(0,1)$, hence
$1-xe^{-s}\in[1-x,1)$ and $f(s)\in\bigl(0,\,-\log(1-x)\bigr]$. As $s$
increases $xe^{-s}$ decreases, so $1-xe^{-s}$ increases to $1$ and $f$
decreases to $0$. Substituting $t=xe^{-s}$ ($\mathrm{d}s=-\mathrm{d}t/t$,
$s{:}0\to\infty \Leftrightarrow t{:}x\to 0^+$),
$$
\int_0^\infty f(s)\,\mathrm{d}s
= \int_0^x \frac{-\log(1-t)}{t}\,\mathrm{d}t
= \mathrm{Li}_2(x).
$$

**(ii) The Riemann sum converges to the truncated integral.**
Because $\log\Phi_n(x;q) = -\sum_{k=0}^{n-1}\log(1-xq^k)
= \sum_{k=0}^{n-1} f(\hbar k)$, the quantity $\hbar\sum_{k=0}^{n-1}f(\hbar k)$
is the **left** Riemann sum of $\int_0^{n\hbar} f$ on the uniform
partition of mesh $\hbar$. For a non-negative decreasing $f$ the left sum
dominates the integral, which dominates the right sum, and
$$
0 \le \hbar\!\sum_{k=0}^{n-1} f(\hbar k) - \int_0^{n\hbar} f
\le \hbar\bigl(f(0)-f(n\hbar)\bigr) \le \hbar\,f(0)
= \hbar\,(-\log(1-x)) \xrightarrow[\hbar\to 0]{} 0 .
$$

**(iii) The tail vanishes as $n\hbar\to\infty$.**
Using $-\log(1-u)\le u/(1-u)\le u/(1-x)$ for $u=xe^{-s}\le x$,
$$
0 \le \int_{n\hbar}^\infty f
\le \frac{1}{1-x}\int_{n\hbar}^\infty x e^{-s}\,\mathrm{d}s
= \frac{x}{1-x}\,e^{-n\hbar} \xrightarrow[n\hbar\to\infty]{} 0 .
$$

**(iv) Assemble.** Combining (i)–(iii),
$\hbar\sum_{k=0}^{n-1} f(\hbar k)\to \mathrm{Li}_2(x)$ along $\hbar\to 0$,
$n\hbar\to\infty$. Finally
$$
(1-q)\log\Phi_n(x;q)
= \frac{1-e^{-\hbar}}{\hbar}\cdot\hbar\!\sum_{k=0}^{n-1} f(\hbar k),
\qquad \frac{1-e^{-\hbar}}{\hbar}\xrightarrow[\hbar\to0]{}1,
$$
and the second factor is bounded and converges to $\mathrm{Li}_2(x)$, so
the product converges to $\mathrm{Li}_2(x)$. $\qquad\blacksquare$

**Numerical confirmation.** The witness
[`computations/dilog-archimedean-limit-partA.witness.json`](../../computations/dilog-archimedean-limit-partA.witness.json)
(producer `dilog_archimedean_partA_witness.py`) evaluates
$(1-q)\log\Phi_n(x;q)$ at $x\in\{0.2,0.5,0.8\}$ along $\varepsilon\in\{10^{-2},10^{-3},10^{-4}\}$
with $n=\lceil 30/\varepsilon\rceil$. The absolute error falls by exactly
one decade per decade of $\varepsilon$ (e.g. $x=0.2$:
$6.07\!\times\!10^{-5}\to 6.07\!\times\!10^{-6}\to 6.07\!\times\!10^{-7}$),
confirming the predicted $O(\varepsilon\,(-\log(1-x)))$ rate, and stays
within the monotone Riemann-sum bound at every step.

**Uniformity (gap (1)).** On a compact $[a,b]\subset(0,1)$ the bounds in
(ii)–(iii) are uniform: $f(0)=-\log(1-x)\le-\log(1-b)$ and the tail
constant $x/(1-x)\le b/(1-b)$. Hence the convergence is uniform on
$[a,b]$, which is precisely the uniform-on-compacts statement the block
listed as gap (1).

## What remains open (Part B)

1. **Substrate side $q\to 1^+$.** At $q_0\approx 1.11$ the factors
   $1-xq^k$ change sign as $k$ grows (the poles of $\Phi_n$), so the
   monotone-Riemann-sum argument fails and the analytic continuation past
   the branch cut is required. This is gap (2), tied to the
   Frobenius-pairing pole cancellation above GB-depth $k_\star(T_w)$
   (`prop:quantum-dilogarithm-stratified`) and to
   `conj:shared-denominator-cusp-holonomy`.
2. **Uniformity as $x\to 1^-$.** The error bound $\hbar(-\log(1-x))$ blows
   up at the edge $x=1$; controlling the limit there (where $\mathrm{Li}_2$
   meets its branch point) is genuinely delicate.
3. **Lean/Mathlib.** A sorry-free Lean proof of even Part A needs Mathlib
   Riemann-sum-to-integral convergence and the identity
   $\int_0^x -\log(1-t)/t = \sum_{k\ge1}x^k/k^2$. This is the bottleneck
   correctly identified in the prior audit (below); the present note does
   not remove it.

## Relationship to the 2026-05-30 assessment (not a contradiction)

[`docs/audits/2026-05-30-conjecture-closure-session-audit.md`](2026-05-30-conjecture-closure-session-audit.md)
(row 3) demoted this conjecture to **Tier B** — "needs Mathlib analysis
infra: q-Pochhammer + Riemann-sum convergence + Li₂ series … not
single-session work." That assessment is about **Lean closure** and
remains correct: the Mathlib infrastructure is still the blocker, and
this note does not author it.

The refinement here is at the **mathematical** level: the *convergence
regime* ($q\to 1^-$, fixed $x$) is elementary (difficulty A), and the
genuine difficulty — the part that justifies a Tier-B Lean rating — lives
entirely in the $q\to 1^+$ substrate continuation and the $x\to 1^-$ edge
(Part B). The block's gap (1) ("uniform Riemann-sum error … the
conjecture asserts uniform") was over-stated: it is a theorem, proved
above, not a conjectural assertion. Gaps (2)–(3) are the real open
content. The block stays `kind: "conjecture"` (Part B is open).

The [`2026-05-09-conjecture-closure-tractability.md`](2026-05-09-conjecture-closure-tractability.md)
row (`dilogarithm-archimedean-limit | B | Same as algebraic-geometric-dilog`)
should likewise be read as "B for the substrate-side Lean closure"; the
convergence half is A.
