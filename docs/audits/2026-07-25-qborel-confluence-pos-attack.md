# Binding Borel variable = loop proper time — Attack B (balanced-kernel q→1 confluence + the (POS) hypothesis)

**Date:** 2026-07-25 · **Bean:** qou-xa89 (Attack B), epic qou-q04o
**Tier:** AUDIT — scope-(a), NO FIT, nothing wired; the target conjecture
stays a conjecture. No content block touched.

**Target.** [`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md),
read in the **balanced** q-Borel convention
$N^{\mathrm{bal}}_q(n) = q^{-(n-1)(n-2)/4}\,[n-1]_q!$ (the fibre-level
refinement forced by Attack E's bar-covariance falsifier). Post-Attack-A/E
state ([`2026-07-25-borel-propertime-attack-a-e.md`](2026-07-25-borel-propertime-attack-a-e.md)):
the conjecture reduces to **(POS)** kernel positivity + **(REP)**
$(n-1)!$-moment representability; Stieltjes determinacy of $\{k!\}$ is
settled (Carleman, Lean-proved divergence); the balanced reading survives
with vanishing first-order $q$-correction; the named next-order falsifier
target is the $h^2$-coefficient $\sum_{k=1}^{n-1}(k^2-1)/24$.

**Probe:** [`computations/probes/qborel_confluence_pos_probe.py`](../../computations/probes/qborel_confluence_pos_probe.py)
→ [`qborel-confluence-pos.witness.json`](../../computations/probes/qborel-confluence-pos.witness.json)
— 9/9 assertions, exit 0 (sympy exact + mpmath 60 dps, tol $10^{-30}$;
audit-only; both q₀ pins).

## 0. What was read from Ramis–Sauloy–Zhang (Astérisque 355, `library/arxiv-0903.0853v3/0903.0853v3.pdf`)

| Cite | Content used |
|---|---|
| **Definition 2.3.3** (p. 23) | level-1 formal q-Borel $\mathcal{B}_{q,1}f(\xi) = \sum_n f_n\, q^{-n(n-1)/2}\xi^n$, standing convention $\lvert q\rvert > 1$ |
| **Remark 2.3.4** (p. 23) | level-1 label; image space $\mathbb{C}(\{\xi\})_{q,1}$ (entire, growth $\prec q^{-n(n-1)/2}$) |
| **§3.3.1** (p. 39) | level-$d$ q-Borel via a weight family $t_n$ with $t_n = q^{n-d}t_{n-d}$; natural level-1 choice $t_n = q^{n(n-1)/2}$; theta-built families |
| **eq. (1.2)** (p. 9) | $\theta(z;q) = \sum_{n\in\mathbb{Z}} q^{-n(n-1)/2}z^n = \prod_{n\ge 0}(1-q^{-n-1})(1+q^{-n}z)(1+q^{-n-1}/z)$ (Jacobi triple product), $\theta(qz) = qz\,\theta(z)$; zeros only on the negative spiral $-q^{\mathbb{Z}}$ |
| **§1.2.1** (p. 7) | the q-Borel/q-Laplace **kernels are not canonical**: several q-exponential kernel choices and **continuous or discrete (Jackson-style) contours**; no closed integral formula for the ch. 5 summation "except for some particular cases" |
| **§1.1.3** (p. 2) | RSZ **explicitly does not treat $q \to 1$ confluence** — "we do not study problems of confluence of our invariants towards invariants of differential equations" — deferring to Di Vizio–Zhang, *On q-summation and confluence*, Ann. Inst. Fourier **59**(1):347–392 (2009) (their ref [21]) |

Corpus qlift-doors extractions re-used, not re-derived: Route A
([`2026-07-20-qlift-routeA-rsz-invariants.md`](2026-07-20-qlift-routeA-rsz-invariants.md))
for Newton-polygon/slope invariants; Route D
([`2026-07-20-qlift-routeD-qborel-transform.md`](2026-07-20-qlift-routeD-qborel-transform.md))
for the Def-2.3.3 convention and the kernel-menu remark; Door-i
([`2026-07-20-qlift-doorI-analytic-summation.md`](2026-07-20-qlift-doorI-analytic-summation.md))
for ch. 5's functorial content. **RSZ contains no q→1 confluence theorem**
— the honest citation for the kernel-convergence step is Di Vizio–Zhang
2009, and that theorem is the named remaining gap (§4).

Index convention: as in Attack A's A2 shift, every kernel below is stated
as a finite (probability) measure $K$ with Stieltjes moments
$\int_0^\infty s^k\,K(ds) = N^{\mathrm{bal}}(k+1)$, $k \ge 0$; the
conjecture's $ds/s$-moment shape $\int s^n\,K(ds)/s = N^{\mathrm{bal}}(n)$
is the same statement.

## 1. Structural identities (exact, sympy)

1. **Theta-measure mechanism.** The reindex $m = j + k$ gives the exact
   polynomial identity

   $$
   mk - \frac{m(m+1)}{2} \;=\; \frac{k(k-1)}{2} - \frac{j(j+1)}{2},
   $$

   so the discrete measure with atoms $q^m$ ($m \in \mathbb{Z}$) and
   weights $\propto q^{-m(m+1)/2}$ — equivalently $1/\theta(q^m; q)$ up to
   $\theta(1)$, by the RSZ eq-(1.2) functional equation — has $k$-th
   moments $\propto q^{k(k-1)/2}$ for **all** $k$. The RSZ level-1 q-Borel
   weight is realized by a positive Jackson-style discrete kernel (the
   §1.2.1 discrete-contour menu made concrete).
2. **Balanced = bar-geometric mean.** Exactly, $n = 1..8$:

   $$
   N^{\mathrm{bal}}(n)^2 = N_q(n)\,N_{q^{-1}}(n),
   \qquad
   N^{\mathrm{bal}}(n) = q^{+(n-1)(n-2)/4}\,[n-1]_{q^{-1}}! .
   $$

   The balanced normalizer is the geometric mean of the bar pair — the
   bar-symmetrized q-Borel weight. The second form is the split the
   positive kernel construction (§3) uses.

## 2. The $h^2$-coefficient test (the decisive check) — MATCH

Exact sympy series, $q = e^h$, per moment order $n = 1..8$:

$$
\log\frac{N^{\mathrm{bal}}_{e^h}(n)}{(n-1)!}
\;=\; 0\cdot h \;+\; c_2(n)\,h^2 \;+\; 0\cdot h^3 \;+\; O(h^4),
\qquad
c_2(n) \;=\; \sum_{k=1}^{n-1}\frac{k^2-1}{24}
\;=\; \frac{(n-1)(n-2)(2n+3)}{144},
$$

with the $c_2(n)$ compared against Attack E's predicted target **as exact
rationals** — equality holds for every $n$ (e.g. $c_2(3) = 1/8$,
$c_2(4) = 11/24$, $c_2(5) = 13/12$), and the closed form is proved
symbolically (`sympy.summation`). The $h^1$ **and** $h^3$ coefficients
vanish exactly — bar-invariance forces the expansion even in $h$.

> **Verdict (scope-(a)):** the balanced confluence structure is verified
> **through second order** — the fibre kernel's deviation from the
> classical moments is exactly the Attack-E target, at every tested order.
> Strong support for the balanced reading; **not a proof** of the
> identification.

**Ladder confirmation (numerically exact, 60 dps).** Over
$q = 1 + 10^{-k}$, $k = 1..6$: the $n = 1, 2$ deviations are exactly $0$;
for $n = 3..8$ the log-log slope of $|N^{\mathrm{bal}}_q(n)/(n-1)! - 1|$
vs $h = \ln q$ is $2.0000..2.0014$ (bracket $[1.9, 2.1]$), and the
extracted $\mathrm{dev}/h^2$ at $k = 6$ matches the exact rational
$c_2(n)$ to $\le 2\times 10^{-14}$ relative. The fitted **exponent** is a
diagnostic read-off of the exactly-proved series structure above — not a
fitted physics constant.

## 3. (POS) at the fibre — an explicit manifestly positive balanced kernel EXISTS

The §1.2 split factors the balanced moments exactly:

$$
N^{\mathrm{bal}}(k+1) \;=\; \underbrace{[k]_{q^{-1}}!}_{A(k)} \cdot
\underbrace{q^{+k(k-1)/4}}_{B(k)},
$$

and **both factors are moment sequences of manifestly positive measures**
(real $q > 1$, $s > 0$; verified at $q = 1.2$ and both q₀ pins, rel
$< 10^{-30}$, $k = 0..8$):

| Factor | Positive kernel | Manifest positivity | Moments |
|---|---|---|---|
| $A(k)$ | **Jackson q-Gamma kernel** at $p = q^{-1} < 1$: atoms $t_m = p^m/(1-p)$, masses $c_m = p^m\,(p^{m+1};p)_\infty$ | every factor $1 - p^j \in (0,1)$ | $\sum_m c_m t_m^k = [k]_p!$ (the Jackson-integral representation of $\Gamma_p$; RSZ §1.2.1's "Jackson style" contour) |
| $B(k)$, discrete | **theta kernel** at $\tilde q = q^{1/2}$: atoms $\tilde q^{\,j}$ ($j \in \mathbb{Z}$), masses $\tilde q^{-j(j+1)/2}/\Theta_0 = (\theta(1;\tilde q)/\theta(\tilde q^{\,j};\tilde q))/\Theta_0$ | RSZ eq. (1.2): $\theta(z;\tilde q) = \prod_{n\ge 0}(1-\tilde q^{-n-1})(1+\tilde q^{-n}z)(1+\tilde q^{-n-1}/z)$ — for real $\tilde q > 1$, $z > 0$ **every factor is positive** (zeros live only on $-\tilde q^{\mathbb{Z}}$); factor-by-factor positivity checked on a grid, and the mass identity vs the triple product verified to $10^{-28}$ | $= q^{k(k-1)/4}$ exactly (§1.1 mechanism at base $\tilde q$) |
| $B(k)$, continuous | **log-normal kernel**: $ds/s$-density $\exp(-(\ln s - \hat\mu)^2/(2\sigma^2))/\sqrt{2\pi\sigma^2}$, $\sigma^2 = \tfrac{\ln q}{2}$, $\hat\mu = -\tfrac{\ln q}{4}$ | Gaussian density $> 0$ | $e^{k\hat\mu + k^2\sigma^2/2} = q^{k(k-1)/4}$ (verified by tanh-sinh quadrature, rel $< 10^{-28}$) |

Mellin (multiplicative) convolution of positive measures is positive and
multiplies moment sequences, so

$$
K^{\mathrm{at}}_q := \mu_{\mathrm{Jackson}} \circledast \mu_\theta
\qquad\text{and}\qquad
K^{\mathrm{ac}}_q := \mu_{\mathrm{Jackson}} \circledast \mu_{\mathrm{logn}}
$$

are **explicit positive probability measures on $(0,\infty)$ whose
Stieltjes moments are exactly $\{N^{\mathrm{bal}}(k+1)\}$** (assembly
identity verified to $10^{-30}$ at all three $q$ values, both
realizations).

> **Verdict on (POS), scope-(a):** at the fibre (real $q > 1$),
> **(POS) ∧ (REP-balanced) is satisfiable** — a manifestly positive kernel
> with exactly the balanced moments exists, built from the very
> ingredients RSZ names (theta weight = Def 2.3.3 / §3.3.1 level-1 family;
> Jackson-style discrete contour = §1.2.1). The positivity is *manifest*
> (a product of positive factors, stated exactly from eq. (1.2)), not a
> numerical accident. This does **not** prove the conjecture's (POS): what
> remains open is that the **substrate's own** resummation kernel is one
> of these positive realizations (see the indeterminacy point below —
> at $q \ne 1$ "the" kernel is not even pinned by the moments).

### 3.1 The honest converse — fibre indeterminacy

$K^{\mathrm{at}}_q$ is purely atomic (positive point masses on a
geometric-type grid); $K^{\mathrm{ac}}_q$ is absolutely continuous
(countable sum of scaled log-normals). They are **distinct positive
measures sharing all balanced moments** (the factor identities are exact
for every $k$ — the theta reindex, the Gaussian integral, the Jackson
q-Gamma sum). Hence:

- **At $q \ne 1$ the balanced moment problem is INDETERMINATE.**
  Consistently, the Carleman terms $N^{\mathrm{bal}}(k+1)^{-1/(2k)}$ decay
  geometrically (ratio $< q^{-1/16}$, verified $k = 100..200$ at
  $q = 1.2$), so $\sum_k N^{\mathrm{bal}}(k+1)^{-1/(2k)} < \infty$ —
  Carleman's sufficient condition fails at the fibre. (This is the
  log-normal/Krein regime: the balanced weight's Gaussian half-factor
  $q^{k(k-1)/4}$ is exactly the growth class of the classic indeterminate
  example.)
- **Attack A's determinacy forcing ("positive + right moments ⇒ the
  kernel IS $e^{-s}ds$") is an archimedean-only feature.** It becomes
  available exactly in the $q \to 1$ limit, where the moment sequence
  degenerates to the determinate $\{k!\}$. At the fibre, (POS) + (REP)
  constrain but do not pin the kernel; the identification carries genuine
  convention/derivation content beyond moments there.
- Corpus-grep: no prior fibre-indeterminacy statement for this kernel
  (nearest, already cited in Attack A: the channel-rotation-askey block's
  indeterminate non-compact q-Hermite problem — a different object).

## 4. Kernel-level confluence $q \to 1$ — verdict and the remaining named gap

**Numerics (diagnostic).** The CDF of $K^{\mathrm{ac}}_q$ at
$s \in \{1/2, 1, 2\}$ vs the classical $1 - e^{-s}$ along
$q = 1 + 10^{-k}$, $k = 1..3$ (float64, lossy, diagnostic only):
deviations shrink $\times\!\sim\!100$ per decade
($1.6\times 10^{-4} \to 1.8\times 10^{-6} \to 1.8\times 10^{-8}$ at
$s = 1$) — the **kernel-level (CDF) confluence is empirically $O(h^2)$ as
well**, matching the balanced moment rate, not just $O(h)$.

**Verdict (scope-(a)).** The balanced q-Borel kernel does confluesce to
the classical Schwinger kernel $e^{-s}\,ds$ as $q \to 1^+$, at the moment
level **exactly** ($h^1 \equiv 0$; $h^2$ = the Attack-E target, §2) and at
the kernel (CDF) level empirically at the same $O(h^2)$ rate. Under the
balanced reading, the conjecture's identification is consistent with being
the **confluence map** of the RSZ-style fibre kernel — supported through
second order, with an explicit positive fibre realization. Not proved.

**The remaining named gap** (what a theorem — and Lean — needs):

1. **The rigorous kernel-convergence theorem** $K_q \Rightarrow e^{-s}ds$
   (weak convergence). The clean classical route: per-$n$ moment
   convergence (§2 — exact series statements, Lean-formalizable per $n$ as
   $\sinh$-product bounds) **+** the **Fréchet–Shohat moment-convergence
   theorem** **+** **Carleman determinacy of the limit sequence**
   $\{k!\}$ (Attack A's leg). Neither classical theorem is in Mathlib
   (Attack A already flagged Carleman); RSZ explicitly does not contain
   the confluence step (§1.1.3) — the literature route is Di Vizio–Zhang,
   Ann. Inst. Fourier 59 (2009) 347–392. Positivity survives the limit
   for free (a weak limit of positive measures is positive), so the
   archimedean (POS) follows from the same package.
2. **(POS)/(REP) for the substrate's kernel.** §3 shows a positive
   balanced kernel *exists*; that the substrate's resummation weight *is*
   such a kernel remains the open content of the conjecture — sharpened
   here by §3.1: at $q \ne 1$ the moments do not pin the kernel, so the
   substrate identification requires a derivation input beyond moment
   matching (e.g. the SDP-positivity transfer route named in Attack A
   §1.4, or a categorical derivation of the Jackson/theta contour).
3. **Balanced restatement of the q-lift bridge** (Attack A gap 4) —
   unchanged, still queued.

## 5. Discipline

- **Corpus-grep (all four paths).** `qlift|0903.0853|Ramis|Sauloy` over
  docs/audits + coordination: RSZ facts already extracted (Routes A/D,
  Door-i, GGM prune) were **re-used, not re-derived**; none covers the
  confluence/positivity questions attacked here.
  `indeterminate|Shohat|Fréchet|lognormal` over docs/audits, content,
  computations, coordination: no prior statement of fibre indeterminacy or
  the Fréchet–Shohat route for this kernel.
- **NO FIT.** Every scored check is an exact symbolic identity or an
  exact-value cross-check at $10^{-30}$; the only fitted quantity is the
  log-log **rate exponent** (a diagnostic of an exactly-proved series
  structure, stated as such); the two q₀ pin strings enter only as
  evaluation points of exact identities; no CODATA read; nothing wired; no
  content block touched; no Lean instance created.
- **Scope-(a) throughout.** Both verdicts (confluence MATCH; (POS)
  satisfiable) are support-level, not proofs; the indeterminacy finding is
  stated with its exact mechanism (two explicit realizations) and scoped
  to real $q > 1$.
- **Formalize-first.** The theta reindex identity, the geometric-mean
  split, and the $h^2$ closed form were derived by hand and verified
  symbolically **before** the numeric ladder; the mpmath layers only
  cross-check displayed identities (algebraic preflight run on the Jackson
  and theta moment identities before the probe was written).
- **Float64 appears only in C5**, marked LOSSY/diagnostic per
  compute-author §1.1; all production-precision claims are sympy-exact or
  60 dps with $10^{-30}$ tolerance.
- **Render-QA:** the preflight grep battery was run by hand (balanced
  `$`/`$$`/braces; no `\operatorname`; no markdown-list lines opening with
  `+`/`-`/`*` inside display math; no inline align-family environments;
  the pipeline render was not run in this sandbox — stated explicitly per
  the render-QA gate: this doc was **not machine-validated**).

## 6. Cross-references

- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
- Attacks A + E (the reduction + the balanced refinement): [`2026-07-25-borel-propertime-attack-a-e.md`](2026-07-25-borel-propertime-attack-a-e.md); Lean [`BorelProperTimeMoment.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorelProperTimeMoment.lean)
- RSZ source: `library/arxiv-0903.0853v3/0903.0853v3.pdf` (Def 2.3.3; §3.3.1; eq. (1.2); §1.2.1; §1.1.3); prior corpus extractions [`2026-07-20-qlift-routeA-rsz-invariants.md`](2026-07-20-qlift-routeA-rsz-invariants.md), [`2026-07-20-qlift-routeD-qborel-transform.md`](2026-07-20-qlift-routeD-qborel-transform.md), [`2026-07-20-qlift-doorI-analytic-summation.md`](2026-07-20-qlift-doorI-analytic-summation.md)
- Confluence literature route (outside RSZ): Di Vizio–Zhang, *On q-summation and confluence*, Ann. Inst. Fourier 59(1):347–392 (2009)
- Balanced convention: [`BalancedQuantumTwist.lean`](../../content/quantum-observable-universe/lean/QOU/Common/BalancedQuantumTwist.lean)
- Probe + witness: [`qborel_confluence_pos_probe.py`](../../computations/probes/qborel_confluence_pos_probe.py), [`qborel-confluence-pos.witness.json`](../../computations/probes/qborel-confluence-pos.witness.json)
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
