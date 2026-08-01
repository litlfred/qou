# Kernel selection principle 3 — Faddeev modular-double covariance: the atomic and a.c. (REP) realizations are ONE Gaussian in dual frames; covariance organizes the family but does not pin a unique kernel

**Date:** 2026-08-01 · **Bean:** qou-q5zq
**Tier:** AUDIT — scope-(a), NO FIT, nothing wired; the target conjecture
stays a conjecture. No content block touched; no Lean file touched.
Namespace `ksel3_*` (parallel selection-principle agents own
`ksel1*`/`ksel2*`; neither is touched here).

**Target.** Within the (REP) kernel family — the $u$-translate continuum
of positive balanced-moment kernels
([`2026-08-01-rep-jackson-identification.md`](2026-08-01-rep-jackson-identification.md)
§3 item 3) built on the Attack-B atomic (Jackson $\circledast$ theta) and
a.c. (Jackson $\circledast$ log-normal) realizations
([`2026-07-25-qborel-confluence-pos-attack.md`](2026-07-25-qborel-confluence-pos-attack.md)
§3) — which kernels are covariant under the Faddeev modular double
($b \leftrightarrow 1/b$, $q \leftrightarrow \tilde q$), and does that
covariance pin a unique one?

**Probe:** [`computations/probes/ksel3_modular_double_probe.py`](../../computations/probes/ksel3_modular_double_probe.py)
→ [`ksel3-modular-double.witness.json`](../../computations/probes/ksel3-modular-double.witness.json)
— 7/7 assertions, exit 0 (sympy exact + mpmath 80 dps, tol $10^{-40}$/
$10^{-45}$; audit-only; both q₀ pins).

## 1. Regime map — where the modular double lives at real substrate $q_0 > 1$

The Faddeev modular double is $q = e^{2\pi i b^2}$,
$\tilde q = e^{-2\pi i/b^2}$, with the exact pairing
$\ln q \cdot \ln \tilde q = 4\pi^2$ and the covariant special function
$\Phi_b = \Phi_{1/b}$. The honest chart at the corpus's real substrate
(all verified in probe M6, rel $< 10^{-45}$, both pins; the $b$-map is
the corpus's own —
[`computations/qbeta/phi_b_substrate_regime.py`](../../computations/qbeta/phi_b_substrate_regime.py),
cited not re-derived):

| Chart | $b$ | $q$ | Modular dual |
|---|---|---|---|
| Unitary / $\Phi_b$ standard | $b$ real | $\lvert q\rvert = 1$ | $\lvert\tilde q\rvert = 1$ |
| **Substrate** (real $q_0 > 1$, $t = \ln q_0$) | $b^2 = \pm i\,t/2\pi$, i.e. $b$ on the $e^{\mp i\pi/4}$ rays | $b_+$: $q = 1/q_0$ ($\lvert q\rvert < 1$, convergent double); $b_-$: $q = q_0$ | $b_+$: $\tilde q_F = e^{-4\pi^2/t}$ (real, $\approx 10^{-164.3}$ at the pins); $b_-$: $e^{+4\pi^2/t}$ (divergent product) |

So at real $q_0$ the substrate is **not** in the unitary real-$b$ regime;
the modular double acts there as the **real involution
$\ln q \mapsto 4\pi^2/\ln q$** on the nome logarithm — precisely the
Fricke-like pairing the corpus has already met (§4 below). This matches
the compact-vs-$\Phi_b$ finding of
[`2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md`](2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md)
(the corpus's compact $\Phi_q$ has the $b$-product only; the dual factor
is a $10^{-164}$ correction at the anchors, per
`phi_b_substrate_regime.py`).

## 2. The dual-pair verdict (deliverable 1): EXACT — the atomic and a.c. realizations are one Gaussian seen in dual frames

Write $t = \ln s$, $L := \ln\tilde q = \tfrac12\ln q$ (kernel base
$\tilde q = \sqrt q$). Probe M1 (sympy exact): the $u$-translate atomic
B-factor mass exponent satisfies, with $t_j = \ln u + jL$ and
$\hat\mu = -L/2$,

$$
-\,L\,\frac{j(j+1)}{2} - j\ln u \;=\; -\frac{(t_j - \hat\mu)^2}{2L} + C(u),
$$

with $C(u)$ independent of $j$ — i.e. **every member of the atomic
continuum is the lattice sampling, on $\ln u + L\mathbb{Z}$, of the one
Gaussian $g(t) = e^{-(t-\hat\mu)^2/(2\sigma^2)}$ with $\sigma^2 = L$,
$\hat\mu = -L/2$ — and that Gaussian is exactly the Attack-B log-normal
a.c. B-factor** ($\sigma^2 = \tfrac{\ln q}{2} = L$,
$\hat\mu = -\tfrac{\ln q}{4} = -L/2$). The "two known realizations" are
one object; the striking possibility named in the task brief holds in
this refined, exact form.

The Jacobi imaginary transform (Poisson summation) is then the frame
change (probe M3, direct-vs-dual rel $< 10^{-40}$ at the exercised base
$L = 1$, where the first dual correction $\sim 5\times10^{-9}$ makes the
check two-sided; classical tie-in via `mpmath.jtheta`, rel
$< 10^{-45}$):

$$
Z(u) \;=\; \sqrt{\tfrac{2\pi}{L}}\sum_{m\in\mathbb{Z}}
e^{-2\pi^2 m^2/L}\, e^{2\pi i m \varphi_u},
\qquad \varphi_u = \frac{\ln u - \hat\mu}{L},
$$

with **dual nome $Q_d = e^{-4\pi^2/L}$** (pairing
$L\cdot\ln(1/Q_d) = 4\pi^2$ — the modular-double involution of §1 at the
kernel base). Three exact structural consequences:

1. **Dual-mode moment covariance (M2, sympy exact).** With the complex
   shift $z = k + 2\pi i m/L$,

   $$
   z\hat\mu + \tfrac{z^2 L}{2}
   \;=\; L\,\tfrac{k(k-1)}{2} \;+\;
   \Bigl(\tfrac{2\pi i m \hat\mu}{L} - \tfrac{2\pi^2 m^2}{L}\Bigr)
   \;+\; 2\pi i\,mk,
   \qquad e^{2\pi i mk} = 1,
   $$

   so the $m$-th dual mode contributes to the $k$-th moment exactly (its
   own mass) $\times\, q^{k(k-1)/4}$: **every dual mode carries the same
   normalized moment ladder.** The mechanism is $\sigma^2 = L$ (variance
   $=$ lattice step): the $k$-th exponential moment shifts the sampling
   by the *lattice vector* $kL$. The balanced moment functional is blind
   to the entire dual-mode sector — **the (REP) indeterminacy continuum
   of the rep-jackson audit §3 *is* the nonzero-dual-mode sector,
   exactly.** (M4a quantifies: the $u=1$ and $u=1.3$ members share all
   normalized moments to $10^{-40}$ yet have total-variation distance 1.)
2. **The a.c. realization is the zero mode = the circle average (M4b,
   rel $< 10^{-35}$).** The Haar average of the unnormalized atomic
   family over the translate circle $\ln u \in [0, L)$ equals the
   continuum Gaussian object — verified moment-by-moment and against a
   non-moment test function. So "atomic $\leftrightarrow$ a.c." is not a
   coincidence of moments: the a.c. kernel is the frame-invariant
   ($m = 0$) component of every atomic member.
3. **Substrate degeneracy (M6).** At both q₀ pins the dual corrections
   have magnitude $2\,\tilde q_F\lvert\cos 2\pi\varphi_u\rvert \sim
   10^{-164.3}$ — verified as $\lvert Z(u)\sqrt{L/2\pi} - 1\rvert
   < 10^{-55}$ (the analytic size is below any resolvable precision).
   The whole $u$-continuum is **doubly-exponentially degenerate at the
   substrate**: atomic and a.c. realizations are numerically
   indistinguishable there at any corpus precision floor.

## 3. The selection verdict (deliverable 2): covariance organizes, but does not pin — distinct covariance notions pick distinct objects

Probe M5 classifies the translate circle by the dual coefficients
$c_m(u) \propto e^{-2\pi^2 m^2/L}\, e^{2\pi i m\varphi_u}$:

| Covariance notion | Cut on the family | Selected object |
|---|---|---|
| **Measure-level self-duality** (transform fixes the kernel) | $L' = 4\pi^2/L = L \iff L = 2\pi \iff q_0 = e^{4\pi} \approx 2.87\times10^5$ | **EMPTY at the substrate** ($L'/L \approx 1.45\times10^4$ at the pins) |
| **Reality of all $c_m$** | $2\varphi_u \in \mathbb{Z} \iff 2\ln u \in L\mathbb{Z}$ | **exactly the bar-reflection $\sigma$-invariant pair** $\{u \equiv 1,\ u \equiv \tilde q^{1/2}\}$ of rep-jackson R4 — the modular frame *re-derives* $\sigma$, adds **no** new cut; the $\sigma$-symmetrized continuum has $\cos$-real duals for **every** $u$ and survives |
| **Positivity of all $c_m$** ($\iff$ $\theta_3$ shape-self-duality) | $\varphi_u \in \mathbb{Z}$ | **unique atomic member $u \equiv \tilde q^{\pm 1/2}$** ($c_m \propto +1$; $\theta_3$-characteristic, and Jacobi maps $\theta_3 \mapsto \theta_3$ — verified rel $< 10^{-45}$). Note: this is **not** the Attack-B presentation $u = 1$, which has $c_m \propto (-1)^m$ ($\theta_2$-characteristic; Jacobi maps $\theta_2 \mapsto \theta_4$, not shape-fixed) |
| **Modular inertness** (no dual modes at all) | $c_m = 0$ for $m \ne 0$ | **unique a.c. member** — the log-normal B-factor (the zero mode itself) |

> **Verdict (scope-(a)).** Modular-double covariance is a genuine
> organizing symmetry of the (REP) family — the family *is* the
> dual-frame decomposition of one Gaussian — but it is **not by itself a
> selection principle**: the strict fixed-point notion is empty at the
> substrate; the reality notion reproduces the already-known $\sigma$ cut
> (fixing a sub-locus of two points, with the symmetrized continuum
> surviving); and the two strengthened notions (dual-positivity /
> $\theta_3$ self-dual characteristic vs modular inertness) each pin a
> *unique* kernel — **but different ones** (the centered atomic member
> $u \equiv \tilde q^{\pm1/2}$ vs the a.c. log-normal). Choosing among
> these covariance notions is itself convention, so the outcome is a
> symmetry-normalization, not a derivation. This is the same shape as the
> rep-jackson conclusion (pinning needs a derivation input beyond
> moments + symmetry), now with the input precisely located: **what
> would promote it** is an independent corpus derivation that the
> substrate machinery uses the self-dual object — e.g. if the $\Phi_b$
> state integrals the corpus *does* compute
> ([`qbeta_dladder_ecalle_phib_resummation.py`](../../computations/qbeta/qbeta_dladder_ecalle_phib_resummation.py),
> [`phi_b_evaluator.py`](../../computations/qbeta/phi_b_evaluator.py))
> were shown to enter the **binding** resummation chain with the
> $\theta_3$/self-dual characteristic. Today they live in the Q_β sector
> only, measurement-tier
> ([`2026-08-01-rep-jackson-identification.md`](2026-08-01-rep-jackson-identification.md)
> §1), so no such promotion is available. Nothing here proves or refutes
> the conjecture.

An honest caveat on the "unique $\theta_3$ member": dual-positivity is a
*natural* normalization (the centered lattice, self-dual characteristic,
all-positive dual masses) but the corpus's own Attack-B convention chose
$u = 1$ (the $\theta_2$ point, whose duals alternate in sign, the
half-period-twist / odd-chart pattern) — the same two-characteristic
tension seen in the W8 odd-nome finding
([`2026-07-24-tau-dictionary-fricke-cusp-spin.md`](2026-07-24-tau-dictionary-fricke-cusp-spin.md):
$t_5 = -10$ requires the odd-nome chart). Recorded as structure, not
interpreted.

## 4. The W8b resonance note — recorded, with the exact part stated exactly

The cusp-factorization audit's W8b variable is
$\tilde q_{\mathrm{W8b}} = e^{-4\pi^2/(5\ln q_0)}$ with
$t_5(iy) = 125\,\tilde q_{\mathrm{W8b}}(1 + O(\tilde q_{\mathrm{W8b}}))$
and the Fricke functional equation $t_5(\tau)\,t_5(-1/(5\tau)) = 125$.
Probe M6 verifies (rel $< 10^{-45}$, both pins) the **exact**
definitional identities

$$
\tilde q_F := e^{-4\pi^2/\ln q_0} = \bigl(\tilde q_{\mathrm{W8b}}\bigr)^5,
\qquad
e^{-2\pi^2/L} = \tilde q_F,
\qquad
Q_d = e^{-4\pi^2/L} = \tilde q_F^{\,2}
\quad (L = \tfrac{\ln q_0}{2}),
$$

i.e. the Faddeev modular-dual nome at the substrate, the kernel's first
Poisson dual amplitude at base $\sqrt{q_0}$, and the W8b cusp variable
are all instances of the one involution $L \mapsto 4\pi^2/L$ — at level
1 on $\ln q_0$, level 1 on $\ln\tilde q$, and Fricke level 5
respectively (level-5 pairing $\ln\hat q \cdot \ln\hat q' = 4\pi^2/5$).
Magnitudes at the pins: $\log_{10}\tilde q_F \approx -164.35$,
$\log_{10}\tilde q_{\mathrm{W8b}} \approx -32.87$. **Status: recorded,
not interpreted** — the exact content is the shared involution shape and
the displayed power identities; no physical identification between the
W8b cusp chart and the kernel dual frame is claimed.

## 5. Honest gap list / what was not done

- **No selection axiom adopted.** §3 exhibits two inequivalent unique
  normalizations; adopting either as "the" substrate kernel would be a
  convention masquerading as a derivation. Not done, per the
  anti-laundering rule.
- **The promotion fact is absent from the corpus.** The corpus's
  $\Phi_b$ machinery never touches the binding chain (rep-jackson §1
  determination); until it does, modular-double covariance stays
  normalization-tier for (REP).
- **Not attempted:** extending the analysis to the Jackson factor's own
  dual behavior (the $A(k) = [k]_{q^{-1}}!$ factor is a $q$-Gamma
  object with its own modular story — untouched); any Lean; the
  Fricke-level-5 vs level-1 bridge beyond the exact power identities.

## 6. Discipline

- **Corpus-grep (all four paths).** `modular double|modular-double` over
  `docs/`, `content/`, `computations/`: the Φ_b regime chart
  (`phi_b_substrate_regime.py`, the 2026-07-06 modular-double audit, the
  $10^{-164}$ suppression note) — **cited, not re-derived**; none states
  the kernel-family Poisson structure. `Poisson|Jacobi imaginary` over
  the same trees: nearest priors are the theta/Poisson **mass**
  resummation prune
  ([`theta_poisson_mass_resummation_prune.py`](../../computations/probes/theta_poisson_mass_resummation_prune.py)
  — a different object, Markov-trace mass support, negative verdict) and
  the $\Theta_{\mathbb{Z}^8}$ weight-4 reflection in the r2core audit —
  neither touches the (REP) B-factor. No prior statement of the
  atomic-equals-sampled-Gaussian identification, the dual-mode moment
  blindness, or the circle-average identity. Ledger
  `docs/coordination/alpha-em.md` walked (rep/attack threads; no
  (REP) closure recorded).
- **NO FIT.** Every scored check is a sympy-exact identity or an
  exact-value cross-check at $10^{-40}$/$10^{-45}$; the q₀ pin strings
  enter only as evaluation points; no CODATA read; nothing wired; no
  content block or Lean file touched; no conjecture-class instance
  created.
- **Scope-(a) throughout.** The dual-pair fact is exact and stated with
  its mechanism ($\sigma^2 = $ lattice step); every selection outcome is
  graded (empty / re-derived / unique-but-plural); the empty fixed-point
  result is a scope-limited statement about this family at real
  $q_0 > 1$, not a structural exclusion.
- **Formalize-first.** The lattice-Gaussian completion of the square,
  the dual-mode shift identity, and the characteristic/phase
  classification were derived by hand and asserted symbolically (sympy,
  probe M1/M2/M5) **before** the 80-dps numeric layer; the numerics only
  cross-check displayed identities (Poisson at an exercised base where
  the dual terms are resolvable, plus the substrate-flatness bound).
- **Render-QA:** the preflight grep battery was run by hand (balanced
  `$`/`$$`/braces; no `\operatorname`; no markdown-list lines opening
  with `+`/`-`/`*` inside display math; no inline align-family
  environments; the pipeline render was not run in this sandbox — stated
  explicitly per the render-QA gate: this doc was **not
  machine-validated**).

## 7. Cross-references

- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
- The (REP) family + $u$-continuum (re-organized here): [`2026-08-01-rep-jackson-identification.md`](2026-08-01-rep-jackson-identification.md)
- The two realizations (shown here to be one object): [`2026-07-25-qborel-confluence-pos-attack.md`](2026-07-25-qborel-confluence-pos-attack.md) §3
- Corpus Φ_b machinery / regime: [`phi_b_substrate_regime.py`](../../computations/qbeta/phi_b_substrate_regime.py), [`phi_b_evaluator.py`](../../computations/qbeta/phi_b_evaluator.py), [`2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md`](2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md)
- W8b cusp factorization (the resonance): [`2026-07-24-tau-dictionary-fricke-cusp-spin.md`](2026-07-24-tau-dictionary-fricke-cusp-spin.md)
- Nearest Poisson priors (different objects): [`theta_poisson_mass_resummation_prune.py`](../../computations/probes/theta_poisson_mass_resummation_prune.py), [`2026-07-25-r2core-schwinger-measure-exploration.md`](2026-07-25-r2core-schwinger-measure-exploration.md)
- Probe + witness: [`ksel3_modular_double_probe.py`](../../computations/probes/ksel3_modular_double_probe.py), [`ksel3-modular-double.witness.json`](../../computations/probes/ksel3-modular-double.witness.json)
