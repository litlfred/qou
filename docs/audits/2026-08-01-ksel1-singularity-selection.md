# KSel-1 (singularity matching) on the (REP) kernel continuum: the map $u \mapsto$ pole set is exact and uniquely selective in form, but the QOU binding data satisfy neither hypothesis — the $u$-continuum survives

**Date:** 2026-08-01 · **Bean:** qou-334t
**Tier:** AUDIT — scope-(a), NO FIT, nothing wired; the target conjecture
stays a conjecture. No content block touched; no Lean file touched.
Machinery reused with attribution from the (REP) Attack-1 probe
([`rep_jackson_identification_probe.py`](../../computations/probes/rep_jackson_identification_probe.py),
bean qou-u5p0). The parallel selection principles KSel-2 (GNS/spectral
measure) and KSel-3 (Faddeev modular double) are owned by sibling
agents and are not touched here; the single KSel-3-adjacent item below
(§4, the self-dual half-step offset) is recorded, not interpreted.

**Target.** The canonical-choice residue of **(REP)**, the last
substantive hypothesis of
[`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md):
per [`2026-08-01-rep-jackson-identification.md`](2026-08-01-rep-jackson-identification.md)
§3, the $\sigma$-symmetric atomic class of positive kernels with the
balanced moments $N^{\mathrm{bal}}_q(n) = q^{-(n-1)(n-2)/4}[n-1]_q!$ is
a **continuum** — the $u$-translate circle $\mu_u$ (atoms
$u\,\tilde q^{\,j}$, $\tilde q = \sqrt q$, masses
$\propto \tilde q^{-j(j+1)/2}u^{-j}$), Jackson-convolved. That audit's
§3 item 5 names RSZ's *output-regularity* ("optimality") remark as the
plausible pinning axis. **KSel-1 makes it concrete:** each $u$-translate
shifts where the q-Laplace *output* can be singular, and the corpus
independently knows binding-side singularity data — so ask whether a
unique $u$ places the output singularities at the known location.

**Probe:** [`computations/probes/ksel1_singularity_selection_probe.py`](../../computations/probes/ksel1_singularity_selection_probe.py)
→ [`ksel1-singularity-selection.witness.json`](../../computations/probes/ksel1-singularity-selection.witness.json)
— 8/8 assertions, exit 0 (sympy exact + mpmath 60 dps, tol $10^{-30}$
for kernel identities; audit-only; both q₀ pins).

## 1. The corpus's singularity data, pinned with tiers (task 1)

Sources: [`lever1_borel_half_singularity_probe.py`](../../computations/lever1_borel_half_singularity_probe.py),
[`lever1_gevrey_order_pin.py`](../../computations/lever1_gevrey_order_pin.py),
their witnesses, and the alien-calculus audit
[`2026-07-12-alien-calculus-review-binding-gevrey-half.md`](2026-07-12-alien-calculus-review-binding-gevrey-half.md).

| Datum | Value | Convention / variable | Tier |
|---|---|---|---|
| Growth class at $q = 1$ | Gevrey-1/2 (sandwich $n! \le 4^n I(n)^2 \le 8^n n!$) | classical coefficients $a_D^{(n)} = I(n)/n$ | **proved-lean** (`QOU/Mass/BindingGevreyHalf.lean`, sorry-free; mirrored exactly to $n \le 60$ in K1) |
| Singularity location at $q = 1$ | $\xi^* = 1/\sqrt 2 \approx 0.7071$, **positive real axis**, non-polar (branch/essential) | the **level-1/2** Borel plane, $b_n = a_D^{(n)}/\Gamma(n/2+1)$ | axis: **exact** (Pringsheim from $b_n > 0$, re-asserted); radius: classical-asymptote-derived + **measured scope-(a)** (root test → $\sqrt 2$; Padé pole $0.688$, 2.6%) |
| Local model / Stokes datum at $q=1$ | $\gamma = 3/2$, second-level action $1/4$, $A_\omega = 4\sqrt2\,e^{-3/8}$ | co-equational, level-1/2 plane | **measured scope-(a)** (derived-before-measurement; `lever1-bridge-alien-datum`) |
| $q_0$ classical plane | **no singularity** — the level-1/2 radius collapses; class change to q-Gevrey | any classical Borel level at $q_0$ | **measured scope-(a)** (gevrey-order pin + Borel-half probe, $q_0$ legs) |

The critical scoping fact: the only *located* singularity
($\xi^* = 1/\sqrt 2$) is a **$q = 1$, classical-plane** datum. At
$q = 1$ the kernel class $\mathcal K_1$ is the Carleman singleton
$\{e^{-s}ds\}$ (REP audit §3 item 1) — $u$ is not a parameter there, so
this datum cannot discriminate on the $u$-circle. Any fibre-level
selection must use fibre-level singularity data, which §3 below shows
do not (currently, and in one direction cannot) exist.

## 2. The exact map $u \mapsto$ pole set (task 2, model leg — probe K2)

Let the input (q-Borel-side) function carry a pole at $\xi^*$ (model:
$\hat f(\xi) = (\xi/\xi^*)/(1 - \xi/\xi^*)$). The atomic-kernel
q-Laplace output is $L_u(x) = \sum_a (c_a/t_a)\,\hat f(x\,t_a)$ over
the kernel atoms $t_a$. Then, exactly:

- **Support lattice.** The Attack-B kernel $K_u = \mu_{\mathrm{Jackson}}
  \circledast \mu_{\theta,u}$ has atoms
  $t = \dfrac{p^m}{1-p}\,u\,\tilde q^{\,j} = \dfrac{u}{1-p}\,
  \tilde q^{\,j-2m}$ ($p = 1/q = \tilde q^{-2}$), and the exponent set
  $\{j - 2m\}$ covers $\mathbb Z$ (constructive). So
  $\mathrm{supp}\, K_u = \dfrac{u}{1-p}\,\tilde q^{\mathbb Z}$.
- **Pole set.** $L_u$ has poles exactly at

  $$
  x \in \frac{\xi^*(1-p)}{u}\,\tilde q^{\mathbb Z},
  $$

  the identity $\xi^*/t = \xi^*(1-p)u^{-1}\tilde q^{\,2m-j}$ being
  exact (sympy) and residue cancellation impossible — all masses are
  positive, so coincident atoms *add*. Verified: every computed pole
  lands on the lattice to rel $< 10^{-30}$ at $u \in \{1,\ 1.3,\
  \tilde q^{1/2}\}$ ($q = 1.2$).
- **Free transitive circle action.** The class map $u \mapsto
  [\xi^*(1-p)/u] \in \mathbb R_{>0}/\tilde q^{\mathbb Z}$ shifts by
  exactly $-\log_{\tilde q} u$: translating $u$ moves the whole pole
  lattice by $u^{-1}$, and $\mu_{\tilde q u} = \mu_u$ (the family is a
  genuine circle, §4). Hence **one** independently-known output pole
  location $x^{\mathrm{tgt}}$ selects a **unique**
  $u \equiv \xi^*(1-p)/x^{\mathrm{tgt}} \bmod \tilde q^{\mathbb Z}$ —
  verified: the solved $u$ places a pole on $x^{\mathrm{tgt}} = 0.53$
  to $< 10^{-30}$, while a $\tilde q^{0.37}$-detuned $u$ misses by
  0.37 of a step.

So **KSel-1 is well-formed and uniquely selective *in form***: given
(i) a fibre input-side singularity $\xi^*$ and (ii) an output-side pole
datum, the kernel is pinned — a derivation input, not a fit. (The
continuous-theta variant of the same statement: the RSZ kernel
$1/\theta$ puts the output poles on the theta zero lattice
$-u\,\tilde q^{\mathbb Z}$; the position-class map mod
$\tilde q^{\mathbb Z}$ is the same circle bijection.)

## 3. The QOU binding data fail both hypotheses (probe K3 — the new measurements)

Carrier: the REP-R3 q-lift object, computed to $n \le 400$ via the
exact q-telephone recurrence $S(n{+}2) = S(n{+}1) + [n{+}1]_q S(n)$
(checked $\equiv$ involution numbers at $q = 1$, exact), with
$b^q_n = S(n)/[n]_q!$ and balanced periods
$B^{\mathrm{bal}}_n = b^q_n\,N^{\mathrm{bal}}_q(n)$.

**(a) The fibre q-Borel side is *entire* — no input singularity
exists.** The normalized ratio $g(n) = (b^q_{n+1}/b^q_n)\,
q^{(2n+1)/4}$ converges (a persistent parity two-cycle, each parity
Cauchy $< 10^{-8}$, actually $\sim 10^{-11}$), so

$$
b^q_n \sim q^{-n^2/4}\,\rho_\varphi^{-n}\cdot(\text{two-cycle factor}),
\qquad \rho_\varphi \approx 2.4495\ (q{=}1.2),\quad
\rho_\varphi \approx 3.1772\ (q_0).
$$

Hence $\varphi(\xi) = \sum b^q_n \xi^n$ has infinite radius (theta
growth class, log-order 2): **there is no finite q-Borel-plane
singularity at the fibre for input-side matching to target.** This
sharpens the corpus's class-change finding (which said: no *classical*
plane carries the period at $q_0$) — in the balanced q-Borel
normalization the transform is entire outright.

**(b) The balanced period series is geometric class — the output-side
singularity is the positive-axis wall $x^* = r^*$ (new measured
datum).** With the exact per-$n$ identity
$B^{\mathrm{bal}}_{n+1}/B^{\mathrm{bal}}_n = g(n)\,q^{1/4-n}[n]_q$
(asserted $< 10^{-40}$), the ratio converges to a two-cycle whose
geometric mean pins the radius:

| $q$ | $r^*$ (two-cycle geometric mean, $n = 400$) | parity pair | Cauchy ($n{=}300$ vs $400$) |
|---|---|---|---|
| $1.2$ | $0.46806946386$ | $0.467675038,\ 0.468464222$ | $2.7\times10^{-13}$ |
| $q_0$ muon pin | $0.34039465785$ | $0.340364706,\ 0.340424612$ | $2.5\times10^{-8}$ |
| $q_0$ proton pin | $0.34039463705$ | $0.340364685,\ 0.340424591$ | $2.5\times10^{-8}$ |

All $B^{\mathrm{bal}}_n > 0$, so by Pringsheim the singularity of
$\sum B^{\mathrm{bal}}_n x^n$ sits **on the positive real axis at
$x^* = r^*$** — an output-plane datum, computable from the corpus
carrier alone. (In the limit form the two-cycle satisfies
$r^* = (q-1)\,q^{-1/4}\rho_\varphi$, parity-resolved — the finite-$n$
identity above.) Confluence consistency: at $q = 1$ the same
recurrence gives $B_n = I(n)/n$ with radius 0 (the known Gevrey-1/2
divergence); the finite radius is a purely fibre-level phenomenon. The
two q₀ pins differ in $r^*$ by $6\times10^{-8}$ relative — the pin
difference propagated, as expected.

## 4. The selection verdict (probe K4–K5) — continuum survives, exactly

**The output wall is exactly $u$-invariant.** For $x > 0$ every term of
$L_u(x) = \sum_a (c_a/t_a)\varphi(x t_a)$ is positive, so by Tonelli
rearrangement the output equals the $u$-independent series
$\sum_n b^q_n N^{\mathrm{bal}}_q(n)\,x^n$ wherever it converges, and
diverges to $+\infty$ beyond $r^*$ — **for every $u$** (verified
numerically: windowed atomic double sum $=$ truncated series to
$< 10^{-25}$ at $u \in \{1, 1.3, \tilde q^{1/2}\}$). The positive-axis
output singularity is a moment-determined functional, and the moments
are $u$-invariant by the REP-R4a reindex identity — **the same exact
mechanism that created the continuum makes the singularity-matching
axis degenerate on the positive axis.**

> **Verdict (scope-(a)): CONTINUUM SURVIVES.** KSel-1 selects no $u$:
> (i) *input side* — the fibre q-Borel transform is entire (§3a), so
> the matching hypothesis has no referent; (ii) *output side* — the
> only corpus-computable output singularity, the positive-axis wall
> $x^* = r^*$ (§3b), is exactly $u$-invariant (Tonelli + moment
> invariance); (iii) the only independently-known located singularity,
> $\xi^* = 1/\sqrt 2$, is a $q = 1$ classical-plane datum living where
> the kernel class is the Carleman singleton (§1). The principle is
> uniquely selective *in form* (§2) — what is missing is data, in a
> specific direction: an **off-positive-axis** output datum (the pole
> lattice of the analytic continuation past $r^*$, which *is*
> $u$-dependent by §2's mechanism) or a genuine fibre input
> singularity. Neither is currently in the corpus. Nothing here proves
> or refutes the conjecture; the (REP) canonicity stays open.

**Cross-checks (task 3).**

- **Balanced moments at every tested $u$, including the self-dual
  points.** The full kernel's $ds/s$-moments equal
  $N^{\mathrm{bal}}_q(k{+}1)$ at $u = 1$, $u = 1.3$, **and**
  $u = \tilde q^{1/2}$, rel $< 10^{-30}$ — $u$-invariance holds by
  construction (reindex identity); asserted, as required.
- **Circle + reflection structure.** $\mu_{\tilde q u} = \mu_u$ as
  normalized measures ($< 10^{-25}$); the bar-reflection
  $\sigma\colon s \mapsto \tilde q^{-1}/s$ maps
  $\mu_u \mapsto \mu_{1/u}$ and fixes exactly the classes $u \equiv 1$
  and $u \equiv \tilde q^{1/2}$ (measure equalities $< 10^{-25}$).
- **Self-dual coincidence check (KSel-3 adjacency) — recorded, not
  interpreted.** Since KSel-1 selects no $u$, there is no selected-$u$
  vs maximal-symmetry coincidence to evaluate. What *is* exact: the
  two $\sigma$-self-dual points' model pole-lattice classes differ by
  **exactly half a $\tilde q$-step**
  ($|\mathrm{frac} - \tfrac12| < 10^{-25}$). If a future output-lattice
  measurement lands on either class, it discriminates the two
  symmetry-maximal candidates sharply — the two principles' answers
  are cleanly comparable, not confounded.

## 5. Discipline

- **Corpus-grep (all four paths).**
  `borel.*half|borel.*singular|gevrey` over `docs/audits/`;
  `singularity.selection|output.regularity|balanced.*radius|ksel` over
  `docs/`, `content/`, `computations/`: the singularity data inventory
  of §1 is the complete prior state (lever1 probes + witnesses + the
  alien-calculus audit); no prior statement of the balanced-series
  finite radius $r^*$, the entire-transform finding, or any KSel-1
  computation exists (nearest: the REP audit's §3 item 5 naming the
  output-regularity axis as future work — executed here).
  The Q_β-sector resummation scripts
  (`qbeta_dladder_*`, `qbeta_g3_5two_qborel_theta_laplace`) act on
  different series and are out of scope per the REP audit §1.
- **NO FIT.** Every scored check is an exact symbolic identity, an
  exact-integer statement, or a convergence/cross-check at stated
  tolerance; the q₀ pin strings enter only as evaluation points; no
  CODATA read; nothing wired; no content block or Lean file touched;
  no conjecture-class instance created. The new numbers ($r^*$,
  $\rho_\varphi$) are *measurements of corpus-defined series*, tier
  measured scope-(a), consumed by nothing.
- **Scope-(a) throughout.** "Continuum survives" is a statement about
  *this selection principle on the current corpus data* — not a (b)
  exclusion of output-regularity selection in general; §4 states
  exactly which future datum would make KSel-1 land, and §2 proves it
  would then select uniquely.
- **Formalize-first.** The pole-lattice identity, the exponent-set
  coverage, the class-shift law, and the Tonelli rearrangement
  argument were derived by hand and asserted symbolically/exactly
  *before* the 60-dps numeric layer; the wall-bracketing and radius
  numerics only cross-check displayed structure. (The prototype run
  that discovered the parity two-cycle and the $u$-cancellation
  preceded assertion-setting, per compute-author §3.1.)
- **Long-compute:** total runtime ≈ 40 s (under the 5-min logging
  threshold; run with `-u` regardless).
- **Render-QA:** the preflight grep battery was run by hand (balanced
  `$`/`$$`/braces; no `\operatorname` outside math-safe context — the
  single `\operatorname{supp}` was checked and replaced; no
  markdown-list lines opening with `+`/`-`/`*` inside display math; no
  inline align-family environments; display `$$` on its own lines).
  The pipeline render was not run in this sandbox — stated explicitly
  per the render-QA gate: this doc was **not machine-validated**.

## 6. Cross-references

- The continuum being tested: [`2026-08-01-rep-jackson-identification.md`](2026-08-01-rep-jackson-identification.md) (§3 item 3; §3 item 5 names the axis)
- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
- Corpus singularity data: [`2026-07-12-alien-calculus-review-binding-gevrey-half.md`](2026-07-12-alien-calculus-review-binding-gevrey-half.md); witnesses `lever1-borel-half-singularity-probe`, `lever1-gevrey-order-pin`, `lever1-bridge-alien-datum`
- Lean class pin: [`QOU/Mass/BindingGevreyHalf.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/BindingGevreyHalf.lean)
- RSZ source: `library/arxiv-0903.0853v3/0903.0853v3.pdf` (§1.2.1 — the output-regularity "optimality" remark made concrete here)
- Probe + witness: [`ksel1_singularity_selection_probe.py`](../../computations/probes/ksel1_singularity_selection_probe.py), [`ksel1-singularity-selection.witness.json`](../../computations/probes/ksel1-singularity-selection.witness.json)
