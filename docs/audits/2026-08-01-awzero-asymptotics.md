# The `A_w` zero asymptotics are proved: a theta-limit Rouché localization with an explicit constant, valid for every `0 < w < 1` from an explicit index `n₀(w)`

**Date:** 2026-08-01 · **Bean:** `qou-k16h`
**Tier:** AUDIT + Lean. NO FIT, nothing wired. The target conjecture
([`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md))
is unchanged in kind.
Parents: [`2026-08-01-ksel2id-tropical-transport.md`](2026-08-01-ksel2id-tropical-transport.md) §3
(the residual this closes) and
[`2026-08-01-ksel2id-u1-promotion.md`](2026-08-01-ksel2id-u1-promotion.md) §4 gap 2
(where the statement was recorded as *measured, no proved theorem imported*).

**Probe:** [`awzero_asymptotics_probe.py`](../../computations/probes/awzero_asymptotics_probe.py)
→ [`awzero-asymptotics.witness.json`](../../computations/probes/awzero-asymptotics.witness.json)
— 5 assertion blocks, exit 0 (mpmath; 60 dps for the identities, per-case
`n²·log₁₀(1/w) + 120` dps for the zeros).
**Lean:** [`AwZeroLocalization.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/AwZeroLocalization.lean),
sorry-free, `lean`-direct exit 0.

Notation. $0 < w < 1$; $(a;q)_n$, $(a;q)_\infty$ the q-Pochhammer symbols;

$$
A_w(z) \;=\; \sum_{m \ge 0} \frac{w^{m^2}(-z)^m}{(w;w)_m}
$$

the Ramanujan entire function (q-Airy function), entire of order $0$ with
$A_w(0) = 1$. In the KSel-2-ID chain $w = \tilde q^{-1}$, so the target
$\zeta_n = w^{1-2n}(1 + O(w^n))$ reads $\zeta_n = \tilde q^{\,2n-1}(1 + O(\tilde q^{\,-n}))$.

## 0. Verdict summary

| # | Statement | Tier |
|---|---|---|
| Z1 | **Localization + counting.** For every $0 < w < 1$ and every $n \ge n_0(w)$: $A_w$ has exactly one (necessarily simple) zero in the disc $\lvert z - w^{1-2n}\rvert < \varepsilon_n\,w^{1-2n}$, $\varepsilon_n = 2\kappa(w)w^n$, and exactly $n$ zeros in $\lvert z\rvert < w^{-2n}$. Consequently, for every $n > n_0(w)$ that zero **is the $n$-th**: $\zeta_n = w^{1-2n}(1+\theta_n)$ with $\lvert\theta_n\rvert \le 2\kappa(w)w^n$. | **proved** (§1; $n_0$ explicit, §1.5) |
| Z2 | **The constant.** $\kappa(w) = (w;w^2)_\infty^{2}\big/\big[(1-w)(w^2;w^2)_\infty^{2}\big]$, an eta quotient, with $\kappa(0^+) = 1$ and $\kappa(1^-) = 2/\pi$; in particular $\kappa$ is bounded on $(0,1)$, so the $O(w^n)$ is uniform in $w$ with an $O(1)$ constant. | **proved** (limit values **measured**, §1.5) |
| Z3 | **Refinement.** $\theta_n = -\kappa(w)\,w^n + O(w^{3n})$. | **derived + measured** (leading term derived in §1.5, remainder order measured) |
| Z4 | **Exact algebra.** The recentring identity, the Jacobi-triple-product theta limit, the defect expansion, and the telescoping q-shift cancellation. | **exact** (probe A1, 9 samples, to working precision; **Lean** for the four algebraic cores) |
| Z5 | **The master bound** $\lvert D_n(u)\rvert \le B_n(u)\lvert G(u)\rvert$ with $B_n$ in closed form. | **proved**; verified to dominate at 72 samples, tightest slack $0.9998$ |
| Z6 | **Certified $n_0(w)$.** From closed-form, grid-free majorants M1/M2. $n_0 = 2, 4, 10, 19, 54, 109, 267$ at $w = 0.3, 0.5, 0.7, 0.8, 0.9, 0.94, 0.97$; at the muon pin $w = \tilde q^{-1} \approx 0.949167$, $n_0 = $ **135** (bound $1.13\times10^{-3}$). | **proved + computed** |
| Z7 | The naive single-term Rouché at the geometric-mean radius closes **only** for $w < w_0 \approx 0.4559$ and never improves with $n$. | **scope-(a)** statement about *that argument* (§4) |

**The residual named in `TropicalClassTransport` §3 and `u1-promotion` §4 gap 2
is closed** — with the honest qualification of Z1: the theorem is a statement
about $n \ge n_0(w)$, and $n_0$ grows as $w \to 1$.

## 1. The argument

### 1.1 Recentring — why index $n$ owns the point $w^{1-2n}$

Substituting $z = w^{1-2n}u$ and writing $m = n + k$,

$$
m^2 + (1-2n)m \;=\; (n - n^2) \;+\; k(k+1),
$$

so, exactly,

$$
A_w\!\left(w^{1-2n}u\right) \;=\; (-1)^n\,w^{\,n-n^2}\,u^n\,\Phi_n(u),
\qquad
\Phi_n(u) \;=\; \sum_{k \ge -n} \frac{(-1)^k w^{k(k+1)} u^k}{(w;w)_{n+k}} .
$$

The exponent is a constant plus a Gaussian **centred at $k = 0$**, i.e. at
$m = n$: this is the precise sense in which the $n$-th coefficient owns that
argument. Lean: `recentring_exponent`, `recentring_zpow`.

### 1.2 The theta limit

As $n \to \infty$ the lower limit recedes and $(w;w)_{n+k} \to (w;w)_\infty$
for each fixed $k$, so $\Phi_n \to G$ with

$$
G(u) \;=\; \frac{1}{(w;w)_\infty}\sum_{k \in \mathbb Z} (-1)^k w^{k(k+1)} u^k
      \;=\; \frac{(w^2;w^2)_\infty\,(w^2u;w^2)_\infty\,(u^{-1};w^2)_\infty}{(w;w)_\infty},
$$

the second equality by the Jacobi triple product at base $w^2$ (the exponent
$k(k+1) = 2\binom{k}{2} + 2k$). Hence **$G$'s zero set is exactly the lattice
$u \in w^{2\mathbb Z}$**, $u = 1$ is a simple zero, and the nearest other zeros
sit at $u = w^{\pm 2}$, at distance $1 - w^2$.

This is the whole mechanism: *the tropical lattice is the zero set of the
theta limit of the recentred series.* The claim "extremal support class =
tropical class" is not an accident of the numerics; it is the statement that
$A_w$, recentred at index $n$, converges to a theta function.

### 1.3 The exact defect, and the cancellation that survives $w \to 1$

Write $D_n := \Phi_n - G$ and $\eta_m := 1 - (w^{m+1};w)_\infty$, so that
$(w;w)_m^{-1} - (w;w)_\infty^{-1} = -(w;w)_\infty^{-1}\eta_m$.
Using Euler's expansion of $\eta_m$ (valid for all $m \in \mathbb Z$), the double sum
converges absolutely — the exponent $k^2 + kj + j^2/2$ is positive definite —
and one gets the **exact** expansion

$$
D_n(u) \;=\; -\frac{1}{(w;w)_\infty}\sum_{j \ge 1} (-1)^{j+1}\,
   \frac{w^{\,j(j+1)/2 + nj}}{(w;w)_j}\, S_j(u),
\qquad
S_j(u) = (w^{j+2}u;w^2)_\infty (w^{-j}u^{-1};w^2)_\infty (w^2;w^2)_\infty .
$$

Every $S_j$ is again a theta product. Dividing by the theta product inside
$G$ and using the reflection identity $1 - x^{-1} = -x^{-1}(1-x)$ repeatedly,
the q-shifts **telescope exactly**:

$$
\frac{\lvert S_{2s}(u)\rvert}
     {\lvert (w^2u;w^2)_\infty (u^{-1};w^2)_\infty (w^2;w^2)_\infty\rvert}
 = w^{-s(s+1)}\lvert u\rvert^{-s},
$$

$$
\frac{\lvert S_{2s+1}(u)\rvert}
     {\lvert (w^2u;w^2)_\infty (u^{-1};w^2)_\infty (w^2;w^2)_\infty\rvert}
 = w^{-(s+1)^2}\lvert u\rvert^{-(s+1)}\,\Omega(u),
\qquad
\Omega(u) := \frac{\lvert (wu;w^2)_\infty (wu^{-1};w^2)_\infty\rvert}
                  {\lvert (w^2u;w^2)_\infty (u^{-1};w^2)_\infty\rvert}.
$$

**This is the load-bearing step.** The comparison is against $\lvert G(u)\rvert$
*pointwise*, not against $\sum_m \lvert\text{term}_m\rvert$: the theta
cancellation that makes $\lvert G\rvert$ exponentially small near $w \to 1$ is
present on *both* sides and cancels. A bound that discards it pays a factor
$(w^2;w^2)_\infty^{3}$ — about $10^{-22}$ at the muon pin — and is useless
there. Lean: `one_sub_inv`, `prod_one_sub_inv`.

Collecting terms gives the **master bound**

$$
\lvert D_n(u)\rvert \le B_n(u)\,\lvert G(u)\rvert,
\qquad
B_n(u) = \Omega(u)\!\!\sum_{s \ge 0}\!\frac{w^{s(s+1)+(2s+1)n}\lvert u\rvert^{-(s+1)}}{(w;w)_{2s+1}}
 \;+\; \sum_{s \ge 1}\frac{w^{s^2+2sn}\lvert u\rvert^{-s}}{(w;w)_{2s}} .
$$

Both series are Gaussian in $s$; the leading term is $\Omega(u)\,w^n\lvert u\rvert^{-1}/(1-w)$.
Probe A2: the bound dominates at all 72 sampled $(w,n,u)$, with a tightest
slack of $0.9998$ — it is essentially attained, not loose.

### 1.4 The two Rouché conditions

**Counting.** On $\lvert u\rvert = w^{-1}$ (i.e. $\lvert z\rvert = w^{-2n}$), if
$\sup B_n < 1$ then $u^n\Phi_n$ and $u^nG$ have the same winding number. The
factor $(w^2u;w^2)_\infty$ is zero-free in $\lvert u\rvert < w^{-2}$, and each
factor $1 - w^{2i}/u$ of $(u^{-1};w^2)_\infty$ contributes winding
$(+1) + (-1) = 0$ (zero at $w^{2i}$ inside, pole at $0$). So the winding is
$n$: **$A_w$ has exactly $n$ zeros in $\lvert z\rvert < w^{-2n}$.** This is what
fixes the *index*, not merely the location.

(Care: $u^nG(u)$ has an essential singularity at $u = 0$, so its winding number
is computed directly from the product expansion above — it is *not* a
zero-minus-pole count. The argument principle is applied only to $u^n\Phi_n$,
which is entire.)

**Localization.** On $\lvert u - 1\rvert = \varepsilon$ with $\varepsilon < 1-w^2$,
if $\sup B_n < 1$ then $\Phi_n$ has exactly as many zeros inside as $G$ — namely
one, counted with multiplicity, hence simple.

**Indexing.** For $n > n_0$ both counting statements — at $n$ and at $n-1$ —
are available ($B_n$ is decreasing in $n$, so the condition, once true at $n_0$,
stays true), giving exactly one zero in the annulus
$w^{-2(n-1)} < \lvert z\rvert < w^{-2n}$; the localized zero lies in that annulus,
so it is the $n$-th. At the boundary index $n = n_0$ the count at $n_0-1$ is not
available, so only the disc statement is claimed there. This one-index caveat is
recorded rather than papered over.

**Choosing $\varepsilon$.** Factor $G$ exactly: with $u = 1+s$,

$$
\lvert G(u)\rvert = \frac{(w^2;w^2)_\infty}{(w;w)_\infty}\,
  \lvert (w^2u;w^2)_\infty\rvert\,\lvert (w^2u^{-1};w^2)_\infty\rvert\,
  \frac{\lvert s\rvert}{\lvert u\rvert},
$$

so $\lvert G\rvert$ grows linearly out of its simple zero and the leading part of
$B_n$ on that circle is $\kappa(w)w^n/\varepsilon$ up to a factor $1+O(\varepsilon)$.
Taking $\varepsilon_n = 2\kappa(w)w^n$ makes it $\tfrac12(1+O(\varepsilon_n))$,
hence $< 1$ once $\varepsilon_n$ is small enough. **That is the theorem.**

### 1.5 The constant $\kappa$, the explicit $n_0$, and the refinement

The derivative of the theta limit at its simple zero is
$G'(1) = (w^2;w^2)_\infty^{3}/(w;w)_\infty$.
Evaluating the leading ($j=1$) defect term at $u = 1$ against it gives the
first-order shift in closed form:

$$
\theta_n \;=\; -\kappa(w)\,w^n + O(w^{3n}),
\qquad
\kappa(w) \;=\; \frac{(w;w^2)_\infty^{2}}{(1-w)\,(w^2;w^2)_\infty^{2}} .
$$

$\kappa$ is an eta quotient and, crucially, **bounded**: the exponentially small
factors cancel, leaving $(w;w^2)_\infty/(w^2;w^2)_\infty \sim \sqrt{2t/\pi}$ with
$t = \ln(1/w)$, so $\kappa \to 2/\pi$ as $w \to 1^-$, and $\kappa \to 1$ as
$w \to 0^+$. Measured (probe A3):

| $w$ | 0.3 | 0.5 | 0.7 | 0.8 | 0.9 | 0.94 | pin | 0.97 | $2/\pi$ |
|---|---|---|---|---|---|---|---|---|---|
| $\kappa(w)$ | 0.810362 | 0.742127 | 0.692319 | 0.671749 | 0.653309 | 0.646441 | **0.644904** | 0.641461 | 0.636620 |

**$n_0(w)$ is grid-free.** Two closed-form majorants replace any numerical
supremum:

- **M1 (counting).** On $\lvert u\rvert = w^{-1}$, each factor of $\Omega$ is
  $\big[(1-w^{2i+2})^2 + 4w^{2i+2}S\big]\big/\big[(1-w^{2i+1})^2 + 4w^{2i+1}S\big]$
  with $S = \sin^2(\theta/2)$, and is **antitone in $S$**, because
  $w(1-x)^2 - (1-wx)^2 = -(1-w)(1-wx^2) < 0$. Evaluating at $S = 0$ and
  bounding $2\lvert\sin(\theta/2)\rvert \le 2$,

  $$
  \Omega \;\le\; \frac{2\,(w^2;w^2)_\infty^{2}}{(w;w^2)_\infty^{2}} .
  $$

  Lean: `omega_factor_key`, `omegaFactor_antitone`.
- **M2 (localization).** On $\lvert u-1\rvert = \varepsilon < \tfrac12$ with
  $\Lambda_{\text{even}}\varepsilon' \le \tfrac12$, $\varepsilon' = \varepsilon/(1-\varepsilon)$,
  factorwise perturbation around $u = 1$ gives

  $$
  \Omega \;\le\; \frac{1+\varepsilon}{\varepsilon}\,\kappa(w)(1-w)\,
    \exp\!\big[(\Lambda_{\text{odd}} + 2\Lambda_{\text{even}})(\varepsilon+\varepsilon')\big],
  $$

  $\Lambda_{\text{odd}} = \sum_i w^{2i+1}/(1-w^{2i+1})$, $\Lambda_{\text{even}}$ likewise.

$n_0(w)$ is then the least $n$ making both closed-form conditions hold. Probe A3
checks that M1 and M2 do dominate the evaluated suprema (they do); probe A5
tabulates the transition, showing the condition failing at indices just below
$n_0$ and holding at $n_0$.

**Where the remaining looseness is.** M2 is nearly tight (slack $1.97$ at the
pin), M1 is not: at the pin $\Omega \le 61.0$ from M1 against an evaluated
supremum of $1.013$, a slack of $60$. That single factor is what makes the
counting condition, not the localization condition, the binding one there
($n_0^{\text{count}} = 135$ versus $n_0^{\text{loc}} = 113$); with the evaluated
supremum the counting condition would already hold at $n = 64$. So a sharper
majorant for $\Omega$ on the counting circle — keeping more than the first
$\lvert\sin(\theta/2)\rvert \le 1$ factor exact — would roughly halve $n_0$ at the
pin. That is a known, quantified improvement, not claimed here.

| $w$ | 0.3 | 0.5 | 0.7 | 0.8 | 0.9 | 0.94 | pin | 0.97 |
|---|---|---|---|---|---|---|---|---|
| $n_0(w)$ | 2 | 4 | 10 | 19 | 54 | 109 | **135** | 267 |
| bound $2\kappa w^{n_0}$ | 0.146 | 0.093 | 0.039 | 0.019 | 0.0044 | 0.0015 | **0.00113** | 0.000377 |

**So the argument does cover the substrate pins.** It is not a "$w$ bounded away
from $1$" result: it holds for every $w < 1$, and what degrades as $w \to 1$ is
the *index* from which it bites, not the validity.

Two readings of that table are worth recording.

- **The threshold is where the bound becomes meaningful, not an artefact.**
  Across the whole ladder the relative bound at the threshold index sits in the
  narrow band $3.8\times10^{-4}$ to $1.5\times10^{-1}$, and it improves by a
  factor $w$ per index thereafter. Equivalently $n_0(w)\ln(1/w)$ drifts only
  from $2.4$ to $8.1$ across $w \in [0.3, 0.97]$. That is the growth M2
  predicts: its binding constraint is
  $(\Lambda_{\text{odd}} + 2\Lambda_{\text{even}})\varepsilon_{n} = O(1)$ with
  $\Lambda \sim \ln(1/t)/(2t)$, $t = \ln(1/w)$, giving
  $w^{n_0} \lesssim t/\ln(1/t)$ and hence
  $n_0 \approx \big[\ln(1/t) + \ln\ln(1/t)\big]/t$ — logarithmic in $1/t$, not
  any power of $1/(1-w)$.
- **The two pins are not independent.** The muon and proton pins differ in
  $q_0$ at the $10^{-8}$ level, hence in $w$ at the ninth digit; the probe
  reports identical $\kappa$, $n_0$ and bound for both, as it must. The proton
  row is a consistency check, not a second datum.

## 2. What is proved, and what is not

**Proved (Z1, Z2, Z5, Z6, and the Z4 algebra).** The localization, the counting,
the explicit constant $2\kappa(w)$, and the explicit $n_0(w)$.

**Not proved here, and not claimed:**

1. **Below $n_0$.** The theorem is *silent* for $n < n_0(w)$. It is a
   sufficient condition, not a necessary one — numerically the asymptotic is
   already excellent well below $n_0$ (probe A4 tabulates this). This is a
   scope-(a) limitation of the argument, **not** a scope-(b) claim that the
   asymptotic fails there.
2. **Z3's remainder.** The leading term $-\kappa(w)w^n$ is derived; the
   $O(w^{3n})$ order is **measured** (the ratio
   $(\theta_n + \kappa w^n)/w^{2n}$ decays at rate $w$ per index, matching the
   prediction). A second-order Rouché would upgrade it; not executed.
3. **Reality of the zeros.** Not used, and not proved here. (Simplicity *is*
   a by-product: Rouché counts with multiplicity, so the single zero it places
   in each disc is simple. Reality is classical via the Nevanlinna-matrix route
   — [`christiansen2003sw`], [`berg1995`] — and is not re-derived.) The
   localization and counting statements are about zeros in discs in $\mathbb C$
   and do not presuppose reality.
4. **Nothing about the target conjecture.** No wiring, no production change.
   The KSel-2-ID class statement now rests on a proved analytic input instead of
   a measured one; that is the whole delta.

## 3. Numerical verification (probe A4)

Zeros were located by bracketed bisection inside the theorem's **own** interval
$[w^{1-2n}(1-\varepsilon_n),\,w^{1-2n}(1+\varepsilon_n)]$ for $n \ge n_0$ — so a
sign change there is itself a check of the theorem — with a certified truncation
bound on the series tail

$$
\Big\lvert \sum_{m > M} a_m z^m \Big\rvert \le
  \frac{w^{(M+1)^2}\lvert z\rvert^{M+1}}{(w;w)_\infty\,(1-r)},
  \qquad r = w^{2M+3}\lvert z\rvert < 1 .
$$

**Endpoint certification against the tail (added after Copilot review on
PR #4507).** The bisection sees only the truncation $\sum_{m \le M} a_m z^m$,
so a sign change *there* certifies a sign change of the **true** series only
if the truncation's magnitude exceeds the tail bound at each bracket
endpoint. The probe now asserts exactly that — $\lvert\sum_{m \le M} a_m z^m
\rvert >$ (the displayed tail bound) at both endpoints, for every
$n \ge n_0$ — and records both bound values per row. Previously the bound was
computed but only *reported*, never applied to the endpoints, so the word
"certified" claimed more than the code did. The assertion passes at every
rung including the pin: 69 certified rows, zero failures, at dps 583 for
$n \approx 135$.

The probe **asserts** $\lvert\theta_n\rvert \le 2\kappa(w)w^n$ at every certified
index. Where $n_0 \le 12$ every index $1..n_0+8$ is enumerated, which also
verifies the *ordering* independently of the counting argument; above that, the
certified window $n_0-2 \ldots n_0+8$ is probed.

| $w$ | 0.5 | 0.7 | 0.85 | 0.9 | pin |
|---|---|---|---|---|---|
| $n_0$ | 4 | 10 | 30 | 54 | 135 |
| dps | 163 | 170 | 221 | 295 | 583 |
| worst $\lvert\theta_n\rvert/(2\kappa w^{n})$, $n \ge n_0$ | 0.500067 | 0.500014 | 0.500001 | 0.500000 | 0.500000 |
| measured next-order rate | 0.499788 | 0.699495 | 0.849754 | 0.899894 | 0.949147 |
| predicted rate ($=w$) | 0.5 | 0.7 | 0.85 | 0.9 | 0.949167 |

Two things to read off. The worst ratio is $\tfrac12$ to five or six figures —
exactly what Z3 predicts ($\theta_n \simeq -\kappa w^n$, so
$\lvert\theta_n\rvert/(2\kappa w^n) \to \tfrac12$): the theorem's constant is
sharp to a factor of two, and that factor is the deliberate safety margin in
$\varepsilon_n = 2\kappa w^n$, not slack in the analysis. And the residual
$(\theta_n + \kappa w^n)/w^{2n}$ decays at a measured per-index rate matching $w$
to $4$–$5$ figures at every rung, confirming the $O(w^{3n})$ order of Z3's
remainder.

## 4. Why the obvious route fails, and why this one does not

The textbook approach — single-term Rouché at the geometric-mean radius
$\rho_n = \sqrt{r_{n-1}r_n}$ of consecutive tropical roots — works only for
small $w$. Log-concavity of the terms with curvature at least $2\ln(1/w)$ gives
$T_{n\pm k} \le T_n w^{k^2}$ at that radius, so the criterion is
$2\sum_{k\ge1}w^{k^2} < 1$, i.e. $w < w_0 \approx 0.4559$ (probe A5, computed by
bisection). Worse, the dominance ratio tends to $w$ as $n \to \infty$: **it never
improves with $n$**, so no amount of depth rescues it. At the muon pin
$w \approx 0.9492$ the criterion's left-hand side is
$2\sum_{k\ge1}w^{k^2} \approx 6.76$: the "rest" outweighs the dominant term
almost sevenfold.

This is a **scope-(a)** statement about that argument. It is *not* a claim that
single-term methods are excluded in principle; it is the measured reason the
theta-limit route was taken instead.

The theta route works precisely because §1.3's telescoping keeps the
cancellation on both sides of the inequality. The tropical roots themselves are
strictly increasing — $r_n/r_{n-1} = w^{-2}(1-w^{n+1})/(1-w^n) > 1$ reduces to
$w^{n+1} < 1+w$ — so the Newton polygon is strictly convex and every corner is
genuine (Lean: `tropRoot_lt_succ`, stated with a shifted index); but convexity
alone is not dominance, and
that gap is exactly what §1.3 fills.

## 5. Literature (Leg 2) — what could and could not be verified

**Network reality.** In this sandbox `WebFetch` returned HTTP 403 on every
publisher and on arXiv; the `paper-search` MCP tools returned empty result sets;
only `WebSearch` (titles, URLs, snippet summaries) functioned. **No abstract or
full text was read.** Everything below is at search-index metadata level and is
labelled accordingly. Nothing from the literature is used to support any claim
in §1 — the proof above is self-contained.

**Registered** in [`content/schema/references.ts`](../../content/schema/references.ts)
at metadata-verification level, with the verification level recorded in each
`note` (no theorem statement is imported from either):

- `bergweiler-hayman2003` — W. Bergweiler, W. K. Hayman, *Zeros of Solutions of
  a Functional Equation*, Comput. Methods Funct. Theory **3** (2003) 55–78,
  DOI `10.1007/BF03321025`. Index snippets describe geometric-progression zero
  asymptotics for entire solutions of q-functional equations under a
  Newton–Puiseux hypothesis — the classical home of the *shape* proved here.
  (Springer renders the online year as 2004 for CMFT vol. 3.)
- `ismail2005qairy` — M. E. H. Ismail, *Asymptotics of q-orthogonal polynomials
  and a q-Airy function*, IMRN **2005**(18) 1063–1088, DOI
  `10.1155/IMRN.2005.1063`. The paper that *names* the q-Airy function. Index
  evidence indicates it proves Plancherel–Rotach asymptotics, **not** a
  zero-asymptotics theorem; do not cite it for the latter.

**Deliberately NOT registered** — the single most relevant lead, because its
metadata could not be pinned down:

- Ismail and Zhang, *Zeros of entire functions and a problem of Ramanujan*,
  Adv. Math. **209**(1) (2007) 363–380, ScienceDirect PII `S0001870806001605`.
  Snippets report that the large zeros of the Ramanujan entire function admit a
  **convergent** asymptotic series — specifically that $q^{2n-1}z_n$ is analytic
  in $q^n$, with the shape $z_n = q^{1-2n}\big[1 - \sum_{j\ge1} y_j q^{jn}\big]$.
  If that is correct it is *stronger* than Z1 and is consistent with Z3
  ($y_1 = \kappa$ in the present notation). **Two things block registration:**
  the second author's given name is rendered "C. Zhang" by the search index
  (Changgui Zhang is already in `references.ts` under other keys; the $A_q$
  literature is dominated by Ruiming Zhang), and no DOI could be verified.
  Guessing either would be fabrication. Registering it is a clean follow-up from
  an unblocked environment.
- Also unverified leads, recorded for the next agent: W. K. Hayman, *On the
  zeros of a q-Bessel function*, Contemp. Math. **382** (2005) 205–216;
  R. Zhang, *Zeros of Ramanujan type entire functions*, arXiv:1603.04694;
  *On a Ramanujan type entire function and its zeros*, JMAA (2020), PII
  `S0022247X20300184` — reportedly the best single literature review of the
  question.

**Assessment.** The result proved in §1 is very likely known — the shape
certainly is. What §1 supplies that the literature (as far as could be seen) does
not, and what the corpus actually needed, is a **self-contained proof with fully
explicit constants and an explicit $n_0(w)$ evaluated at the substrate pins**, so
the KSel-2-ID chain does not have to import an unread theorem. Corpus discipline
("sorry-free ≠ derived", and its literature analogue) makes an unverifiable
citation a worse dependency than a proof.

## 6. Discipline

- **Corpus-grep (all four paths).** `q-Airy | Ramanujan entire | zero
  asymptotics | Rouché | Newton polygon | tropical root` over `docs/audits/`,
  `docs/coordination/`, `content/`, `computations/`. Prior state: the statement
  is declared **open** in exactly three places — `ksel2id-u1-promotion.md` §4
  gap 2, `ksel2id-tropical-transport.md` §3, and the content block
  [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md).
  The only implementation is `ksel2id_u1_promotion_probe.py`'s numerical
  zero-finder (`a_ramanujan`, `a_zeros`), which *measures* the asymptotic. No
  prior proof, no prior Rouché argument, no prior closed-form constant. `Newton
  polygon` hits are the unrelated qlift tranche.
- **NO FIT.** Every scored item is an exact identity or a check of a *displayed*
  bound. $\kappa$ and $n_0$ are **derived**, not fitted: $\kappa$ is the
  evaluation of the $j=1$ defect term at $u=1$ divided by $G'(1)$, and $n_0$ is
  the least index satisfying a closed-form inequality. The zero-finding
  tolerances are working precision. When the first draft's defect-expansion
  truncation ($J = 40$) failed the working-precision tolerance at $w = 0.85$, the
  fix was to make the truncation adaptive — **not** to loosen the tolerance.
- **Refutation hygiene.** One negative is recorded: the naive single-term Rouché
  closes only below $w_0 \approx 0.4559$ and does not improve with $n$. It is
  stated as **scope-(a)** — a limitation of that argument at those radii — with
  the supporting log-concavity computation displayed. No scope-(b) exclusion is
  asserted anywhere in this audit.
- **Conditional-proved ≠ premise-established.** Z1 is unconditional for
  $n \ge n_0(w)$; it is not conditional on any class or conjecture. The Lean
  module contains no conjecture carrier and no `sorry` — it formalises only the
  algebra it claims to (the analytic steps are explicitly excluded in its
  docstring, not silently axiomatised).
- **Formalize-first.** The three exact identities and the two order facts
  (strict convexity of the Newton polygon; the antitone Ω-factor) were derived by
  hand and proved in Lean before the numeric layer; the probe only exercises
  displayed bounds.
- **Grid honesty.** The certified $n_0$ uses **no grid**: M1 and M2 are
  closed-form. A grid supremum of $\Omega$ is computed only to *report the
  slack* in those majorants, and the probe asserts `grid sup ≤ majorant`. For
  $w > 0.95$ that illustrative grid is coarsened from 720 to 120 samples,
  because each q-product needs $10^3$–$10^4$ factors there; a coarser grid can
  only under-estimate a supremum, so the assertion stays sound and merely gets
  weaker. A first run of this probe also carried a $w = 0.99$ rung; it was
  dropped for runtime, not because it failed — the certified $n_0$ machinery is
  $w$-uniform and would simply report a larger index.
- **Long-compute discipline.** `python3 -u … > /tmp/awzero.log 2>&1` (run
  detached; same capture as the `| tee` form), with
  progress + elapsed lines at every block and per-$w$ boundary. Bottleneck:
  block A3's evaluated-supremum cross-checks at $w \ge 0.94$ (the q-products need
  $\sim 10^3$ factors) and block A4's pin case (zero-finding at
  $\sim 6\times10^2$ dps). Reported in the witness.
- **Render-QA.** The preflight grep battery was run **by hand** on this file:
  balanced `$`/`$$` and `{}`; no `\operatorname`; no line inside `$$…$$` opening
  with `+`/`-`/`*`; no inline align-family environments; every symbol introduced
  before use ($t$, $\Lambda_{\text{odd/even}}$, $S$, $\varepsilon'$, $r_n$).
  **The pipeline render was NOT run** (the `folio-assistant` clone is not present
  in this sandbox) — this document is **not machine-validated**.
- **Nothing wired.** Audit-only; no content block, no production script, no
  dashboard touched.

## 7. Cross-references

- Residual this closes: [`2026-08-01-ksel2id-tropical-transport.md`](2026-08-01-ksel2id-tropical-transport.md) §3;
  [`2026-08-01-ksel2id-u1-promotion.md`](2026-08-01-ksel2id-u1-promotion.md) §4 gap 2
- Identification of the extremal supports with zeros($A_{\tilde q^{-1}}$):
  [`2026-08-01-ksel2id-friedrichs-sw-identification.md`](2026-08-01-ksel2id-friedrichs-sw-identification.md)
- SW core Jacobi data (Lean): [`SWCoreJacobi.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SWCoreJacobi.lean);
  factorization: [`SWJacksonMomentFactorization.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SWJacksonMomentFactorization.lean)
- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
