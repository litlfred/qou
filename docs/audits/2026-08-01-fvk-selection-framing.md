# Friedrichs versus Krein: a survey of candidate selection principles, and what each one actually implies — the F/K choice is the $ds$-versus-$s\,ds$ level choice, no principle tested selects Friedrichs, and one excludes Krein

**Date:** 2026-08-01 · **Bean:** `qou-f6sm`
**Tier:** AUDIT + Lean. NO FIT, nothing wired. The target conjecture
([`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md))
is unchanged in kind; no content block was touched.

**Probe:** [`fvk_selection_probe.py`](../../computations/probes/fvk_selection_probe.py)
→ [`fvk-selection.witness.json`](../../computations/probes/fvk-selection.witness.json)
— 6 assertion blocks, exit 0, wall $\approx 19$ s (sympy exact + mpmath;
qd at 400–500 dps, eigen at 120 dps, continued fractions at 160 dps).
**Lean:** [`FvkSMapRigidity.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/FvkSMapRigidity.lean),
four theorems, sorry-free, `lean`-direct exit 0, axioms `[propext]` only
(negative control run: a deliberately corrupted statement fails to elaborate,
so the exit 0 is real checking).

Notation as in the parent audits: $q > 1$, $p = 1/q$, $\tilde q = \sqrt q$,
$\tilde p = 1/\tilde q$, $L = \ln\tilde q$, $E = q/(q-1)$; balanced moments
$m_k = q^{-k(k-1)/4}[k]_q!$; SW core moments $G_k = \tilde q^{\,k(k-1)/2}$;
$J(q)$ the canonical Jacobi operator of the balanced functional; $\mu_F,
\mu_K$ the spectral measures of its Friedrichs and Krein extensions;
and $\lambda_F = \min\mathrm{supp}\,\mu_F$ the smallest Friedrichs support
point.

## 0. Verdict summary

| # | Principle | Verdict tier | One-line reason |
|---|---|---|---|
| P1 | Friedrichs as the minimal-form / form-domain-distinguished extension | **conventional-default** | the polynomials are a form core of $J_F$ *by construction*, but the same datum determines $J_K$ just as canonically; and the three apparently independent arguments for $F$ are one fact in three costumes (§2) |
| P2 | Krein excluded — no mass at $s = 0$ (P2 computational time) | **conditional-derivation for the EXCLUSION; does not select $F$** | exact core: $\mu = s\cdot\nu$ has a solution $\nu$ on $(0,\infty)$ iff $\mu(\{0\}) = 0$, which fails at exactly one point of the arc. Every other member passes (§3) |
| P3 | Dual-mode positivity / modular criteria (KSel-3) | **orthogonal** (not merely inconclusive) | the criteria are defined on a Gaussian sampled at step $=$ variance; the F/K supports have step $2L$ against variance $L$, and their masses are Nevanlinna masses, not Gaussian samplings — no domain of definition (§4) |
| P4 | Non-selection: the ambiguity is physical | **live, and currently the best-supported answer** | no corpus consumer touches a non-moment functional, and every arc member reproduces every moment (measured $3.8\times10^{-60}$, §5) |
| P5 | *(added here)* The S-map level identity | **derivation — of a reduction, not of a selection** | $F = S(K)$ **exactly** at every truncation order on the SW core ($1.6\times10^{-116}$): the F/K choice *is* the $ds$-versus-$s\,ds$ choice, i.e. the conjecture's own $\varsigma\,ds/s$ normalization one level down (§6) |

**Headline.** No principle tested selects Friedrichs. One (P2) excludes
Krein, conditionally on the conjecture's own premise. The structural gain is
P5: the question "which extension?" is not an independent degree of freedom
at all — it is the same normalization question the conjecture already carries,
displaced by one power of $s$.

## 1. Why no lattice or class result can decide this

The parent tranche established that $\mu_F$ and $\mu_K$ occupy the two
complementary $q$-sublattices of the **one** $u \equiv 1$ theta grid
([`ksel2id-u1-promotion`](2026-08-01-ksel2id-u1-promotion.md) A-4), that
$\mathrm{supp}\,\mu_K = \mathrm{zeros}(A_{\tilde p})$ and
$\mathrm{supp}\,\mu_F = \mathrm{zeros}(A_{\tilde p})/\tilde q$
([`awzero-asymptotics`](2026-08-01-awzero-asymptotics.md)), and that the bar
reflection does not act on the extension circle by pushforward at all
([`ksel2id-friedrichs-sw-identification`](2026-08-01-ksel2id-friedrichs-sw-identification.md) §3).

So $F$ and $K$ agree on every invariant the class machinery computes: same
class $\varphi_1$, same grid, exactly one $\tilde q$-step apart. **A
selection must be operator-level or substrate-level.** That is what this
survey tests.

## 2. P1 — Friedrichs as the form-distinguished extension

### 2.1 What is true

The Friedrichs extension is the one whose form domain is the closure of the
given dense domain in the form norm. In the GNS/Favard presentation that
domain is the polynomials, so the polynomials are a form core of $J_F$ **by
construction** — which is exactly why the plain truncation eigenvalues
decrease to $\mathrm{spec}\,J_F$ by min–max, the machinery the parent audit
used to compute $\mu_F$ at all.

Three further facts point the same way, and it is tempting to read them as
three independent arguments:

1. $J_F$ is the **largest** nonnegative extension in the form order.
2. $\mu_F$ has the **largest** smallest support point ($\lambda_F \approx
   0.3367$ at $q = 2.0736$; Pedersen).
3. $\mu_F$ **minimizes** the total mass of the computational-time measure,
   $I(\mu) := \int s^{-1}\,d\mu$ (§3.2 below).

### 2.2 Why it is a conventional default, not a derivation

**The three facts are one fact.** By the Krein–Ando ordering of nonnegative
self-adjoint extensions, $J_K \le J_t \le J_F$ in the form order for every
member $t$ of the arc; the form order reverses under inversion, so
$J_F^{-1} \le J_t^{-1}$, and $(J^{-1})_{00}$ *is* $I(\mu)$. Item 3 is item 1
inverted; item 2 is item 1 read at the bottom of the spectrum. Reporting them
as mutually corroborating would be exactly the "convention dressed as
derivation" failure mode this survey was asked to catch, so it is named here
and recorded in the probe's own witness (`V3.honest_caveat`).

**The given datum determines $J_K$ just as canonically.** Both $J_F$ and
$J_K$ are functorial in the pair (symmetric operator, dense domain): $J_F$ is
the largest nonnegative extension, $J_K$ the smallest. "The extension that
respects the algebra and adds no information" describes both — the Krein–von
Neumann extension is precisely the *soft* / minimal-energy choice, and calling
$F$ "GNS-internal" (the phrasing floated in
[`ksel2-gns-favard-canonicity`](2026-08-01-ksel2-gns-favard-canonicity.md) §5
item 3, which this section is evaluating) does not exclude $K$: nothing in the
GNS data prefers a hard boundary condition to a soft one.

**What would promote it.** P1 becomes a derivation exactly when the substrate
supplies a **form** — an energy functional whose closure is the primitive
datum — rather than an operator with a domain. Corpus-grep over
`docs/audits/`, `docs/coordination/`, `content/`, `computations/` for
`form domain` / `Dirichlet form` / `quadratic form` / `form core`: the only
hits tying a *form* to this operator are the parent audits themselves; the
Dirichlet-form hits are the $w_\lambda$-covariance tranche (a different
object), and the quadratic-form hits are Epstein/Bring lattice sums. **The
substrate does not currently present $J(q)$ as a form.** Until it does, P1 is
the operator theorist's default convention.

> **Verdict: conventional-default.** Promotion requires a corpus derivation in
> which the energy form, not the moment functional, is primitive.

## 3. P2 — the Krein atom at $s = 0$ and computational time

### 3.1 The exact mathematical core (this part is not interpretive)

The corpus's own frame identity is $m_k = N^{\mathrm{bal}}_q(k{+}1)$
([`ksel2-gns-favard-canonicity`](2026-08-01-ksel2-gns-favard-canonicity.md)
§3): the balanced moment sequence is the normalizer sequence shifted by one.
The conjecture displays its object as the scale-invariant measure
$\varsigma\,ds/s$, i.e. as a measure $\nu$ with

$$
N(n) \;=\; \int_0^\infty s^{\,n}\,d\nu(s), \qquad \nu = s^{-1}\mu .
$$

So the representing measure $\mu$ of the balanced moments and the
computational-time measure $\nu$ are related by $\mu = s\cdot\nu$, and the
question "does the extension admit the conjecture's own shape?" is the
question "is $\mu$ in the image of $\nu \mapsto s\,\nu$?" That has an exact
answer:

> $\mu = s\cdot\nu$ for some Borel measure $\nu$ on $(0,\infty)$ **iff**
> $\mu(\{0\}) = 0$.

Multiplication by $s$ annihilates any atom at $0$, so an atom at $0$ cannot be
in the image; conversely, if $\mu(\{0\}) = 0$ then $\nu := s^{-1}\mu$ works.
Among the extensions of $J(q)$ exactly one has an atom at $0$ — the Krein
extension, by definition. Every other member of the arc is discrete with
$\min\mathrm{supp} > 0$, so $\nu$ exists *and is finite*.

The probe realizes this as a computable dichotomy: $I(\mu) = (J^{-1})_{00}$ is
the total $\nu$-mass, and at the Krein boundary condition the truncated matrix
is **exactly singular** — the continued-fraction denominator is
$2.2\times10^{-154}$ at $N = 44$, against $0.4834$ at Friedrichs (V3). The
identity $I = \sum_j w_j/\lambda_j$ cross-checks to $9.9\times10^{-121}$.

### 3.2 What it does and does not buy

- It **excludes Krein**, conditionally on reading the conjecture's displayed
  $\varsigma\,ds/s$ shape as a requirement on the fibre-level object.
- It does **not select Friedrichs.** Every non-Krein member passes. Adding
  "and minimize $I$" selects $F$, but that is P1 in disguise (§2.2).

### 3.3 The critique that must be recorded

The interpretive reading — an atom at $s = 0$ means a finite probability of
**zero** computation steps, which P2 forbids — has a level problem that cuts
against it:

- **P2's interpretive force lives at the archimedean point**, where $s$ is
  real proper time. But at $q = 1$ the moment problem is Carleman-determinate:
  there is no ambiguity to resolve.
- **The ambiguity lives at the fibre level** ($q \ne 1$), where $s$ is a
  formal $q$-Borel variable and the corpus has *not* established that it
  counts anything. Reading "zero computation steps" off a fibre-level atom is
  a transport of meaning across exactly the wall the corpus is careful about
  elsewhere.
- **The archimedean object itself has infinite $ds/s$ mass.** $N(0) = \int_0^\infty
  e^{-s}\,ds/s$ diverges logarithmically at $s \to 0$ — the loop's UV end, the
  reason $\zeta$-regularization is there at all. So "the computational-time
  measure must have finite total mass" is *false* of the archimedean object,
  and cannot be imposed at the fibre level on archimedean grounds. What
  survives is only the sharper statement of §3.1, which is about the *shape*
  $\mu = s\nu$, not about finiteness.

There is a genuinely attractive reading in the other direction, recorded but
not endorsed: at $q \ne 1$ every non-Krein extension has a spectral gap
$\lambda > 0$, so the $ds/s$ mass is finite — the $q$-deformation supplies a
UV cutoff, with the minimal computation step as the regulator, and the
archimedean divergence is restored as $\lambda_F \to 0$. This is physics
prose, not a derivation, and §8 shows that its most obvious quantitative
consequence fails.

> **Verdict: conditional-derivation for the exclusion of Krein
> (interpretive-only for anything more).** The exclusion's mathematical core
> is exact; its premise — that the fibre object must literally carry the
> $\varsigma\,ds/s$ shape — is the conjecture's own, so within the conjecture
> the exclusion is legitimate and outside it, it is not available.

## 4. P3 — the modular / dual-mode criteria are orthogonal

KSel-3's criteria (dual-mode positivity, i.e. the $\theta_3$-characteristic
point; and modular inertness, i.e. the a.c. zero mode) are defined through the
Poisson dual coefficients of a **Gaussian sampled on a lattice**, and their
whole mechanism is the coincidence $\sigma^2 = \text{lattice step}$: the
$k$-th moment shifts the sampling by $k\sigma^2$, which is a lattice vector
precisely when $\sigma^2$ is the step, which is why the dual modes are
moment-blind.

For the extension circle that coincidence fails, exactly (probe V4, sympy):
the SW core Gaussian has $\sigma^2 = L$, while the F and K supports are
lattices of step $2L$ (spacing exactly one $q$-step — two $\tilde q$-steps,
the parent's measured $2.0012$). So

$$
\frac{k\,\sigma^2}{\text{step}} \;=\; \frac{k}{2},
$$

a lattice vector only for **even** $k$: the moment-blindness mechanism breaks
at every odd order, and a step-$2L$ sampled Gaussian is not a solution of the
moment problem at all. Consistently, the extension masses are Nevanlinna
masses $1/\sum_n p_n(x)^2$, not Gaussian samplings.

An honest surprise here, recorded rather than buried: the probe's first draft
asserted that the Friedrichs masses would differ from the Gaussian samplings
by orders of magnitude. **The run refuted that** — the ratio spread over the
first ten atoms is only $1.534$. Exact proportionality is excluded (so the
conclusion stands), but the masses are *near*-proportional, and that near-miss
is plausibly the quantitative mechanism behind the parent audits' asymptotic
$u \equiv 1$ alignment. The assertion was rewritten to test what is true, not
what was expected.

> **Verdict: orthogonal.** Not "inconclusive": the KSel-3 criteria have no
> domain of definition on the extension circle. They cut the $u$-circle, which
> the parent audit already proved (scope-(b), discreteness) is a *different*
> circle.

## 5. P4 — non-selection, taken seriously

### 5.1 The case for it

Every representing measure of the balanced sequence has, by definition, every
balanced moment. The probe verifies this across the arc: four members
reproduce $m_k$ for $k \le 30$ to a worst relative deviation of
$3.8\times10^{-60}$ (V5). And the corpus's binding sector consumes the kernel
**only formally** — the proved keystone strip, the proved depth-2 recurrence,
and formal $q$-Borel coefficient maps; no binding number is produced by an
integral resummation
([`rep-jackson-identification`](2026-08-01-rep-jackson-identification.md), as
restated in the conjecture block's "Structure of the open content").

Putting those together: **every functional of the kernel that the corpus
currently evaluates is a moment, and no moment distinguishes the extensions.**
The F/K ambiguity is, today, unobservable.

### 5.2 What would make it a positive result rather than a shrug

Non-selection becomes a *result* — rather than an absence of one — if the
corpus can establish a **determinacy-of-consumption** statement:

> every functional of the binding kernel that enters a corpus prediction is
> determined by the moment sequence,

in which case the extension choice is provably physically vacuous and the
conjecture's open content collapses from "which extension?" to "none of them
individually — the object is the moment functional." The corpus fact that
would have to hold is exactly the one currently true but *unproved as a
closure*: that the binding chain never leaves the formal / moment layer.

The moment it fails — the first time a lateral Borel–Laplace resummation at a
non-integer point, a Stokes constant, or a regularized $N(0)$ enters a
prediction — non-selection is refuted and the choice becomes physical. That is
the decisive test, and §7 states it operationally.

> **Verdict: live.** On current corpus facts, P4 is the best-supported answer.
> It is not yet a theorem, because "the corpus consumes only moments" is an
> observation about the present state, not a proved property of the chain.

## 6. P5 — the S-map level identity (added here)

The one genuinely new structural result of this survey.

### 6.1 The algebra (exact, and Lean-proved)

Define the **S-map** on representing measures: $S(\mu) := (s \mapsto
s/\tilde q)_*\bigl(s\,d\mu/m_1\bigr)$ — multiply by $s$, rescale one
$\tilde q$-step. On the Jacobi side this is $J \mapsto \tilde q^{-1}\cdot
\mathrm{LR}(J)$, with $\mathrm{LR}$ the square-root-free Christoffel step at
shift $0$:

$$
e_k = \frac{\beta_{k+1}}{\ell_k}, \quad
\ell_{k+1} = \alpha_{k+1} - e_k, \quad
\alpha'_k = \ell_k + e_k, \quad
\beta'_k = \ell_k\,e_{k-1} .
$$

Probe V1 (sympy, symbolic in $\tilde q$): applied to the closed-form SW data
$\alpha_k = \tilde q^{\,k-1}(\tilde q^{\,k}(1+\tilde q) - 1)$,
$\beta_{k+1} = \tilde q^{\,3k}(\tilde q^{\,k+1}-1)$, the LR step returns the
**same** matrix rescaled:

$$
\alpha'_k = \tilde q\,\alpha_k, \qquad \beta'_k = \tilde q^{\,2}\beta_k .
$$

The SW core is an exact fixed point of $S$. The Lean file proves the rigidity
behind this: a normalized moment sequence is S-fixed
($m_{k+1} = c^k\,m_1\,m_k$) **iff** it is log-quadratic
($m_k = m_1^k\,c^{\binom{k}{2}}$), together with the division-free detector
$c\,m_{k+1}^2 = m_{k+2}\,m_k$ and its contrapositive. So *S-fixedness is
exactly the Stieltjes–Wigert property* — it is not a feature this particular
family happens to have.

### 6.2 The consequence: $F = S(K)$, exactly, at every order

Gauss–Radau at $0$ on $N$ points and plain Gauss on $N-1$ points are related
by the Christoffel transform; combined with the fixed-point property, the
probe verifies for the SW core (V2, $q = 2.0736$, $N = 34$, dps 120):

$$
\lambda^K_j = \tilde q\,\lambda^F_{j-1}, \qquad
\lambda^K_j\,w^K_j = w^F_{j-1},
$$

to worst relative deviations $1.6\times10^{-116}$ (nodes) and
$2.4\times10^{-116}$ (masses) — an **exact finite-$N$ identity**, not an
asymptotic one. The $s$ factor kills the Krein atom at $0$ and the rescaling
shifts the support one $\tilde q$-step: this is the parent audit's
support-level observation upgraded to a measure-level identity with a proved
algebraic cause.

For the balanced family $S$ is not exact — the obstruction is precisely the
Jackson factor $(1 - p^{k+1})$, and the Jacobi-data deviation decays at rate
$\tilde p$ (measured $0.694318$ against $\tilde p = 0.694444$; V2b).

*Honest run-history note.* The first draft predicted the moment-ratio rate $p$
here, which the run missed by a square root. The fix was to state the correct
prediction — the corpus's own documented Jacobi-layer rate $\tilde p$
([`ksel2id-u1-promotion`](2026-08-01-ksel2id-u1-promotion.md) A-6) — and to
*tighten* the tolerance from $5\times10^{-2}$ to $10^{-2}$, not to loosen it.

### 6.3 Why this reframes the question

$F = S(K)$ means the two extremal extensions are **not two independent
candidates**: they are the same object read at two levels of the
$s$-multiplication tower. Choosing between them is choosing whether the
substrate's measure carries $s^0$ or $s^1$ — which is the conjecture's own
$\varsigma\,ds/s$ normalization question, displaced by one power of $s$.

This is a derivation **of a reduction**, not of a selection: it says the
closing question is not new content, and that a principle fixing the
$s$-power fixes the extension. It does not itself fix the $s$-power.

## 7. Recommendation, and the decisive test

**Recommendation: attack P4 (non-selection), not P1.**

P1 is the tempting target and it is the one to avoid: every route into it
terminates in the same form-order fact, and dressing that fact in three
costumes will read as three arguments while being one. P2 is already
harvested — its exclusion of Krein is exact, and it provably cannot do more.
P3 is closed as orthogonal. P5 says a selection principle must be a principle
about the $s$-power, which is a *smaller* target than "which extension".

The decisive test has two halves, and they are cheap relative to the parent
tranche's compute:

1. **Sweep the corpus for a non-moment consumer.** Enumerate every place the
   binding kernel or the Schwinger measure is evaluated and classify each
   functional as moment-determined or not. If the sweep comes back empty, the
   determinacy-of-consumption statement of §5.2 is within reach and
   non-selection becomes a positive result. If it finds one, that functional
   is the discriminator, and the F/K question becomes physical and answerable
   by evaluating it on $\mu_F$ and $\mu_K$ — which this probe's machinery
   already computes.
2. **Test any candidate discriminator against the arc interior, not just
   against $F$ and $K$.** §8 is the cautionary instance: a natural candidate
   separated Krein from everything else and could not tell $F$ from a mid-arc
   member at seven digits. A discriminator that only excludes Krein is P2
   again.

## 8. The decisive-test dry run: an honest negative

The most attractive candidate discriminator available today is the
$\zeta$-regularized finite part of $N(0)$. If $\mu_F$ behaved like $e^{-s}ds$
truncated below its gap, then since
$\int_\lambda^\infty e^{-s}\,ds/s = E_1(\lambda) = -\gamma - \ln\lambda +
O(\lambda)$, one would predict the parameter-free limit

$$
I_F(q) + \ln\lambda_F(q) \;\longrightarrow\; -\gamma = -0.5772\ldots
\qquad (q \to 1^+).
$$

Probe V6 tests it. The quantity turns out to be **remarkably $N$-stable** —
$0.9505901,\ 0.9505896,\ 0.9505966,\ 0.9506010$ at $N = 20, 28, 36, 44$ for
$q \approx 1.2155$, even though $I_F$ moves from $3.094$ to $3.254$ and
$\lambda_{\min}$ from $0.1172$ to $0.0999$ over the same ladder: the two badly
pre-asymptotic legs cancel. So the values are converged in $N$, and they are:

| $q$ | 2.0736 | 1.4641 | 1.2155 | pins ($\approx 1.10998$) |
|---|---|---|---|---|
| $I_F + \ln\lambda_F$ | 0.98021 | 0.95959 | 0.95060 | 0.94758 |
| $I_F/E_1(\lambda_F)$ | 2.5176 | 2.0616 | 1.7842 | — |
| $I_F - E_1(\lambda_F)$ | 1.2471 | 1.3585 | 1.4304 | — |

Two readings, pointing opposite ways, and the verdict needs both. The
**ratio** $I_F/E_1$ does fall toward $1$, so the leading behaviour of the
truncated-exponential model is right. But the **additive residual**
$I_F - E_1$ *grows*, and the $-\gamma$ test is an additive finite-part test.
The measured quantity sits $\approx 1.53$ above $-\gamma$ and drifts by
$\approx 0.003$ per major $q$ step. **The test as posed fails** — scope-(a):
this is a statement about the studied range with $N$-converged evaluation, not
a proved exclusion of any $q \to 1$ behaviour. The mechanism is clear enough:
$\mu_F$ is a $q$-lattice measure whose harmonic moment is dominated by its
single lowest atom, not a truncated density.

And it would not have discriminated anyway: the mid-arc column agrees with the
Friedrichs column to seven digits at every rung.

One regularity is recorded with **no interpretation and no fit**: the quantity
sits near $0.95$ across the whole studied range. It is not claimed to converge
to anything, and it should not be chased without a structural reason to expect
a particular constant.

## 9. Honest gaps and scope

1. **Nothing here selects Friedrichs.** The survey's positive content is one
   exclusion (P2, conditional), one orthogonality (P3), and one reduction
   (P5). If a reader wants "the answer is Friedrichs", this document does not
   supply it, and §2.2 explains why the obvious argument for it is circular.
2. **Krein–Ando ordering is cited, not re-proved.** The claim that $I$ is
   minimized at $F$ over the *whole* arc rests on $J_K \le J_t \le J_F$; the
   probe's sweep only corroborates it at sampled points.
3. **The finite-$N$ boundary-shift family does not resolve the arc interior.**
   At $N = 44$ both $I$ and $\lambda_{\min}$ are nearly constant across
   $s \in [0, 0.99]$ and collapse only between $s = 0.9999$ and $s = 1$. So
   "strict monotonicity along the arc" is verified as stated but is *not*
   evidence about interior members; that parametrization is extremely
   non-uniform. Recorded in the witness (`V3.resolution_caveat`).
4. **§8 is scope-(a).** No claim is made about the $q \to 1$ limit beyond the
   observed, $N$-converged trend. The $q$-ladder stops at $q \approx 1.2155$
   plus the pins; the pin rows are $N = 22$ lower bounds and are labelled
   pre-asymptotic.
5. **The Lean covers the algebra only.** It formalises S-map rigidity, not the
   identification of truncation limits with the Friedrichs and Krein
   extensions (literature: [`pedersen1995`], [`simon1998`]), and not any
   measure theory. No conjecture carrier is declared; nothing is assumed.
6. **No scope-(b) exclusion is asserted anywhere in this audit.** P2's
   exclusion of Krein is exact *given a stated premise*, which makes it
   conditional, not structural; it is labelled as such throughout.

## 10. Discipline

- **Corpus-grep (all four paths).** `Friedrichs | Krein | form domain |
  Dirichlet form | quadratic form | form core | harmonic moment | Christoffel
  | LR step | Krein–Ando | resolvent order` over `docs/audits/`,
  `docs/coordination/`, `content/`, `computations/`. Prior state: the KSel-2 /
  KSel-2-ID / awzero tranche (which *names* Friedrichs-minimality as a
  candidate — [`ksel2-gns-favard-canonicity`](2026-08-01-ksel2-gns-favard-canonicity.md)
  §5 item 3 — and evaluates it nowhere), plus `form domain` appearing in that
  one sentence. No prior corpus occurrence of the harmonic moment
  $(J^{-1})_{00}$, the Christoffel/LR route, the Krein–Ando ordering, or the
  S-map rigidity. No prior closure of the selection question. Coordination
  ledgers walked; nothing recorded.
- **NO FIT.** Every scored item is an exact symbolic identity or a check of a
  *displayed* relation at a stated tolerance. The one prediction that missed
  (§6.2) was corrected to the corpus's own documented rate and its tolerance
  *tightened*; the one expectation that was refuted (§4, mass spread) was
  rewritten to test what is true and the surprise recorded. No constant is
  fitted; the $0.95$ regularity of §8 is explicitly not interpreted.
- **Refutation hygiene.** No scope-(b) claims. §8's negative is scope-(a) and
  says so. P2's exclusion is labelled conditional on a named premise. P3's
  "orthogonal" is a statement about the criteria's domain of definition, with
  the exact variance-versus-step computation displayed.
- **Anti-laundering.** The central finding of §2.2 is that three apparently
  independent arguments for Friedrichs are one fact; naming that was the
  point of the exercise, and it is recorded in the machine witness as well as
  here.
- **Formalize-first.** The S-map rigidity was derived by hand, proved in Lean,
  and only then exercised numerically; the numerics check displayed identities.
- **Long-compute discipline.** `python3 -u … 2>&1 | tee /tmp/fvk_selection.log`,
  per-block progress lines. Wall $\approx 19$ s — no bottleneck worth
  reporting; the expensive legs (eigen at $N = 44$, dps 120) are seconds.
- **Lean verification.** `lean`-direct exit 0 against restored oleans;
  `#print axioms` gives `[propext]` for all four theorems; a negative control
  (corrupted exponent) fails to elaborate, so the exit 0 is genuine checking.
- **Render-QA.** The preflight grep battery was run **by hand** on this file:
  balanced `$`/`$$` and braces; no `\operatorname` (the one natural use, the
  support operator, is written `\mathrm{supp}` throughout); no line
  inside `$$…$$` opening with `+`, `-` or `*`; no inline align-family
  environments; display `$$` on their own lines; every symbol introduced
  before use. **The pipeline render was NOT run** (no `folio-assistant` clone
  in this sandbox) — this document is **not machine-validated**.
- **Nothing wired.** Audit-only; no content block, production script, or
  dashboard touched.

## 11. Cross-references

- The closing question: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
- F/K computed; bar-pushforward closed: [`2026-08-01-ksel2id-friedrichs-sw-identification.md`](2026-08-01-ksel2id-friedrichs-sw-identification.md)
- Complementary sublattices of one $u \equiv 1$ class: [`2026-08-01-ksel2id-u1-promotion.md`](2026-08-01-ksel2id-u1-promotion.md)
- Exact class transport: [`2026-08-01-ksel2id-tropical-transport.md`](2026-08-01-ksel2id-tropical-transport.md)
- Supports as $A_w$ zeros: [`2026-08-01-awzero-asymptotics.md`](2026-08-01-awzero-asymptotics.md)
- The non-selection precedent this survey generalizes: [`2026-08-01-ksel3-modular-double-covariance.md`](2026-08-01-ksel3-modular-double-covariance.md)
- The candidate named and here evaluated: [`2026-08-01-ksel2-gns-favard-canonicity.md`](2026-08-01-ksel2-gns-favard-canonicity.md) §5 item 3
- Probe + witness: [`fvk_selection_probe.py`](../../computations/probes/fvk_selection_probe.py), [`fvk-selection.witness.json`](../../computations/probes/fvk-selection.witness.json)
- Lean: [`FvkSMapRigidity.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/FvkSMapRigidity.lean)
- Bibliography (already registered): [`pedersen1995`], [`simon1998`], [`christiansen2003sw`], [`berg1995`], [`moak1981`]
