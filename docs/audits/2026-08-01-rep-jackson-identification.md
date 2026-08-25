# (REP) Attack 1 — constructive Jackson-integral identification: the corpus performs NO binding-side integral; (REP) is a canonical-choice premise, and the choice is not pinned by moments + symmetry

**Date:** 2026-08-01 · **Bean:** qou-u5p0
**Tier:** AUDIT — scope-(a), NO FIT, nothing wired; the target conjecture
stays a conjecture. No content block touched; no Lean file touched (the
`BalancedMomentConfluence` / `BalancedKernelConfluence` / `QOU.lean` files
are owned by a parallel verification agent this session; tightness/
Prokhorov (REP-2) is owned by a parallel agent — neither is touched here).

**Target.** **(REP)**, the last substantive hypothesis of
[`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md):
*the corpus's actual binding resummation is integration against a positive
kernel whose $ds/s$-moments are the balanced normalizer*
$N^{\mathrm{bal}}_q(n) = q^{-(n-1)(n-2)/4}\,[n-1]_q!$. Post-Attack-A/B/E
state: the conjecture is reduced to (POS) + (REP)
([`2026-07-25-borel-propertime-attack-a-e.md`](2026-07-25-borel-propertime-attack-a-e.md)
§1.3); an explicit positive kernel with exactly the balanced moments
exists (Jackson $\circledast$ theta, Jackson $\circledast$ log-normal),
but at $q \ne 1$ the moments do not pin the kernel
([`2026-07-25-qborel-confluence-pos-attack.md`](2026-07-25-qborel-confluence-pos-attack.md)
§3, §3.1).

**Probe:** [`computations/probes/rep_jackson_identification_probe.py`](../../computations/probes/rep_jackson_identification_probe.py)
→ [`rep-jackson-identification.witness.json`](../../computations/probes/rep-jackson-identification.witness.json)
— 6/6 assertions, exit 0 (sympy exact + mpmath 60 dps, tol $10^{-30}$;
audit-only; both q₀ pins).

## 1. The determination (the key deliverable): the corpus performs NO integral resummation of the binding OGF — the operation is formal

Survey of every place the binding OGF / C1 carrier is produced or
consumed:

| Site | What it actually does | Integral? |
|---|---|---|
| [`computations/mass_binding_dashboard.py`](../../computations/mass_binding_dashboard.py) (lines 2–9, production presentation of the binding forms) | "every binding form is evaluated from the ONE canonical Jones–Markov transfer trace (`tr_m_atom_zn` …) … α = E₀"; `B_sym` via the closed-form linear-chain factorization. A **finite algebraic trace evaluation**. The only grep hits for involution/Borel vocabulary (lines 350, 391, 708) are the *bar-involution entanglement split* of the atom trace — unrelated to resummation. | **No** |
| [`computations/canonical_mass.py`](../../computations/canonical_mass.py) (the absolute-mass facade) | muon-anchored Hecke energy `2·(m_μ·F_Bor − 6·m_e)` — algebraic | **No** |
| [`KeystoneBridgeC1Binding.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean) + [`2026-07-20-keystone-bridge-c1-binding.md`](2026-07-20-keystone-bridge-c1-binding.md) | the normalizer **strip** $b_n = B_n/N(n)$, $N(n) = (n-1)!$ forced by $n \cdot N(n) = n!$, and the depth-2 recurrence — **coefficient-level algebra** (Lean, exact) | **No** |
| [`2026-07-20-qlift-routeD-qborel-transform.md`](2026-07-20-qlift-routeD-qborel-transform.md) | the corpus's only q-Borel *application* to the C1 carrier is the **formal** coefficient map (RSZ Def 2.3.3 diagonal weight $f_n \mapsto f_n q^{-n(n-1)/2}$), used to test kernel gauge-equivalence — and that formal route was **closed negatively** (diagonal-gauge invariant $I_m$) | **No** (explicitly "formal") |
| [`computations/lever1_gevrey_order_pin.py`](../../computations/lever1_gevrey_order_pin.py), [`computations/lever1_borel_half_singularity_probe.py`](../../computations/lever1_borel_half_singularity_probe.py), [`computations/sw_period_growth_probe.py`](../../computations/sw_period_growth_probe.py) | growth-class pin and Borel–Padé **singularity location** of the level-1/2 Borel transform — diagnostics, EXPLORATORY; no resummed value is produced, and nothing consumes one | **No** (analysis of the Borel plane, not a Laplace evaluation) |
| Confluent-narrowing §6 residue ([`2026-07-20-qdifference-kernel-confluent-narrowing.md`](2026-07-20-qdifference-kernel-confluent-narrowing.md)) | the once-landed `B_precur` dashboard recurrence was an anchored depth-2 **recurrence** (and flagged as an effective fit), not an integral | **No** |

The nearest *actual* numerical integral/resummation machinery in the
corpus lives in the **Q_β sector**, over *different series* (the D-ladder
$d_k$; the Masbaum bar-side Habiro series), all probe-tier, none
production-wired:
[`qbeta_dladder_jackson_qborel_acceleration_probe.py`](../../computations/qbeta/qbeta_dladder_jackson_qborel_acceleration_probe.py)
(fixed-base Jackson q-Borel — refuted as mis-classed for that series),
[`qbeta_dladder_ecalle_phib_resummation.py`](../../computations/qbeta/qbeta_dladder_ecalle_phib_resummation.py)
(Écalle / $\Phi_b$ state integral, measurement-only),
[`qbeta_g3_5two_qborel_theta_laplace.py`](../../computations/probes/qbeta_g3_5two_qborel_theta_laplace.py)
(θ-kernel bilateral Laplace). None touches the binding OGF.

> **Determination (deliverable 1).** The corpus **never performs** an
> integral resummation of the binding series — no q-Laplace/Jackson
> integral, no numerically evaluated Borel sum, feeds any binding number.
> The binding OGF is used **purely formally/algebraically**: the proved
> keystone strip, the proved depth-2 recurrence, formal diagonal q-Borel
> weights, and growth diagnostics. Production binding is the finite
> Markov-trace evaluation. Consequently **(REP) is a claim about a
> canonical CHOICE of integral representation for a formally-performed
> operation — not a matching to an existing corpus operation.** (This is
> the prompt's branch 3; branch 2's "rewrite the existing resummation"
> has no referent.)

## 2. The identification that (REP) asserts, made exact — and the Attack-5 falsifier outcome: MATCH

Although no corpus integral exists, the *formal* operation the corpus
does perform can be compared exactly against the Jackson-kernel
integral. The probe verifies (all exact or $10^{-30}$):

1. **The corpus operation (R1, exact).** $I(n+2) = I(n+1) + (n+1)I(n)$;
   periods $B_n = I(n)/n$; strip $N(n) = (n-1)!$ forced by
   $n \cdot N(n) = n!$; carrier $b_n = I(n)/n!$; recurrence
   $(n+2)\,b_{n+2} = b_{n+1} + b_n$ — all exact, $n \le 14$.
2. **Archimedean falsifier (R2, sympy exact).** Per order,
   $\int_0^\infty s^n e^{-s}\,\frac{ds}{s} = (n-1)!$; and the
   finite-order polynomial identity ($N = 8$, exact in $x$):

   $$
   \int_0^\infty \Bigl[\sum_{n=1}^{N} b_n\,(x s)^n\Bigr] e^{-s}\,\frac{ds}{s}
   \;=\; \sum_{n=1}^{N} B_n\, x^n .
   $$

   The strip **is** order-by-order integration against the unit
   Schwinger kernel. MATCH (a mismatch would have killed the option).
3. **Fibre falsifier (R3, 60 dps, $q \in \{1.2,\ q_0^{\mu},\ q_0^{p}\}$).**
   The Attack-B atomic kernel $K^{\mathrm{at}}_q = \mu_{\mathrm{Jackson}}
   \circledast \mu_\theta$ — built from exactly the RSZ ingredients
   (Def 2.3.3 weight; eq. (1.2) theta; the §1.2.1 "discrete in Jackson
   style" contour) — satisfies

   $$
   \int_0^\infty s^{\,n}\, K^{\mathrm{at}}_q(ds)\,/\,s \;=\; N^{\mathrm{bal}}_q(n),
   \qquad n = 1..9,\ \text{rel} < 10^{-30},
   $$

   and the q-lift C1 carrier $b^q_n = S_q(n)/[n]_q!$ (with
   $S_q(n+2) = S_q(n+1) + [n+1]_q S_q(n)$) resums through the kernel
   correctly at finite order (coefficient-wise and at a spot value).
   The **exact discrepancy** against the corpus's *proved one-sided*
   strip $[n-1]_q!$ is the bar-covariant weight $q^{-(n-1)(n-2)/4}$
   per $n$ (Attack E's finding, re-verified as the control): the
   identification holds **only** in the balanced convention, exactly as
   the conjecture's fibre-level refinement demands.

**On "RSZ's q-Laplace is a Jackson integral by definition":** the honest
citation is narrower. RSZ §1.2.1 (p. 7) offers a *menu* — "several
choices for Borel and Laplace kernels … and several choices of the
integration contours (**continuous or discrete in Jackson style**)" — and
for RSZ's *own* preferred ch. 5 summation states "we did not obtain
explicit integral formulae for this summation (except for some particular
cases)". So the Jackson-style discrete contour is an RSZ-named *option*
realized here concretely (as in Attack B), not RSZ's unique definition.

## 3. The canonical-choice formulation (deliverable 2) — and what fails to pin the kernel

Since branch 3 holds, (REP) must be stated as a canonicity claim:

> **(REP-canonical).** Let $\mathcal{K}_q$ be the set of positive
> measures $K$ on $(0,\infty)$ with
> $\int s^n\,K(ds)/s = N^{\mathrm{bal}}_q(n)$ for all $n \ge 1$. The
> conjecture's (REP) content is: the substrate's resummation weight is a
> **canonical** element of $\mathcal{K}_q$, distinguished by structural
> properties, whose $q \to 1$ confluence is $e^{-s}\,ds$.

Status of the candidate pinning properties (probe R4, at $q = 1.2$;
mechanisms exact, cross-checks $10^{-30}$):

1. **At $q = 1$: no choice content.** $\mathcal{K}_1 = \{e^{-s}ds\}$ —
   Carleman determinacy of $\{k!\}$ (Attack A, Lean-carried divergence
   hypothesis). (REP) archimedean-side is pure representability, and it
   holds (§2, R2).
2. **Positivity + moments do not pin (known, Attack B §3.1).**
   $K^{\mathrm{at}}$ vs $K^{\mathrm{ac}}$.
3. **NEW — a continuum, even inside the bar-symmetric atomic class.**
   The $u$-translate family of the theta factor — atoms
   $u\,\tilde q^{\,j}$ ($j \in \mathbb{Z}$, $\tilde q = \sqrt q$), masses
   $\propto \tilde q^{-j(j+1)/2} u^{-j}$ — has $u$-**independent**
   moments $q^{k(k-1)/4}$: the exact reindex mechanism is
   $jk - j(j+1)/2 = k(k-1)/2 - i(i+1)/2$ at $j = i + k$, so the
   $u$-dependence collapses to the normalization (the family is
   effectively parametrized by $u \in \mathbb{R}_{>0}/\tilde q^{\mathbb{Z}}$,
   a circle). Generic $u$ gives a **distinct support** (grid offset
   $\approx 0.87$ of a $\tilde q$-step at $u = 1.3$). The natural
   bar-reflection $\sigma\colon s \mapsto \tilde q^{-1}/s$ — the unique
   reflection fixing *both* Attack-B B-factor realizations (theta $u=1$
   via the exact index map $j \mapsto -1-j$; log-normal via Gaussian
   symmetry about $\hat\mu = -\tfrac12 \ln \tilde q$) — maps
   $\mu_u \mapsto \mu_{1/u}$ (verified as measure equality), so
   $\sigma$-invariance alone cuts the circle only to two points
   ($u \equiv 1$, $u \equiv \tilde q^{1/2}$); but the **symmetrization**
   $\tfrac12(\mu_u + \mu_{1/u})$ is positive, $\sigma$-invariant,
   atomic, and carries the same moments for **every** $u$. Convolving
   with the fixed Jackson factor yields a $u$-continuum of positive
   kernels with exactly the balanced moments (verified $10^{-30}$).
   **Consequence:** positivity + balanced moments + bar-reflection
   invariance + atomicity do **not** pin the fibre kernel.
4. **Confluence-compatibility adds nothing.** Any family in
   $\mathcal{K}_{q_j}$ along $q_j \to 1$ has moments converging to
   $\{(n-1)!\}$, and (conditional on the classical Fréchet–Shohat +
   Carleman package — the named Mathlib gap,
   [`2026-07-25-kernel-convergence-mathlib-gap.md`](2026-07-25-kernel-convergence-mathlib-gap.md))
   converges weakly to $e^{-s}ds$. So "confluence-compatible" is implied
   by membership in $\mathcal{K}_q$ and distinguishes nothing.
5. **"Unique bar-invariant kernel in the RSZ classification" — not
   available.** RSZ contains **no classification of admissible kernels**;
   §1.2.1 asserts the opposite (non-canonicity, a menu of kernels and
   contours). What RSZ *does* single out about its ch. 5 summation is a
   different property — "our choice of summation here seems quite
   'optimal': the entries of our Stokes matrices are elliptic functions …
   moreover Stokes matrices are meromorphic in the parameter of
   'q-direction of summation'" (§1.2.1) — an *output-regularity*
   criterion, with no general explicit integral formula. That criterion
   (ellipticity/meromorphy of the resulting Stokes data, not
   bar-symmetry of the kernel) is the plausible future pinning axis, and
   it is a **derivation-input** question, not a moment/symmetry question.

> **Verdict (scope-(a)).** (REP) splits cleanly: **archimedean (REP)** is
> settled representability (the corpus's formal strip is exactly
> integration against the determinate $e^{-s}ds$ — §2); **fibre (REP)**
> is a canonical-choice premise whose canonicity is **not derivable from
> the named structural properties** — the $\sigma$-symmetric atomic
> class of $\mathcal{K}_q$ is a continuum (item 3). Pinning the
> substrate's kernel requires a derivation input beyond moments +
> symmetry: the SDP-positivity transfer route (Attack A §1.4), a
> categorical derivation of the Jackson/theta contour, or an RSZ-style
> output-regularity ("optimality") criterion. This *sharpens* Attack B
> §3.1 (two realizations → a continuum inside the symmetric atomic
> class) and is consistent with the balanced-confluence audit's gap 2
> ("`hrep` … cannot be reduced to moment data at $q \ne 1$",
> [`2026-07-25-balanced-moment-confluence-lean.md`](2026-07-25-balanced-moment-confluence-lean.md)
> §3). Nothing here proves or refutes the conjecture.

## 4. Falsifier outcome and honest gap list

- **Falsifier outcome: MATCH, both legs** (R2 exact; R3 at $q = 1.2$ and
  both q₀ pins, rel $< 10^{-30}$). The option **survives**: the corpus's
  formal operation *is* representable, order by order, as the Jackson
  q-integral against the Attack-B atomic kernel in the balanced
  convention. No discrepancy to report; the one-sided convention's exact
  gap ($q^{-(n-1)(n-2)/4}$) is the already-known Attack-E weight,
  recorded per $n$ in the witness.
- **What survives ≠ what is proved.** Representability + falsifier-MATCH
  do not make the kernel *the substrate's*: at $q \ne 1$ infinitely many
  positive symmetric kernels represent the same operation (§3 item 3).
  (REP) remains open; its open content is now precisely located in the
  canonicity, not the existence.
- **The reflection $\sigma$ is a candidate bar-realization, not derived.**
  $\sigma\colon s \mapsto \tilde q^{-1}/s$ is *natural* (fixes both
  B-factor realizations) but the claim "bar acts on proper time by
  $\sigma$" is itself convention-level; the non-uniqueness conclusion is
  robust to this (it only *adds* an invariance constraint, and the
  continuum survives it).
- **Not attempted:** the SDP-positivity transfer (Attack A §1.4); the
  RSZ ch. 5 output-regularity criterion as a pinning axiom; any Lean
  (the relevant Lean files are owned by parallel agents this session).

## 5. Discipline

- **Corpus-grep (all four paths).** `Jackson|q-Laplace|laplace|borel|resum`
  over `computations/` + `content/` (the §1 inventory);
  `Stieltjes-Wigert|N-extremal|Nevanlinna|translate` over `docs/`,
  `content/`, `computations/`: no prior statement of the translate-family
  continuum or the canonical-choice split (nearest: Attack B §3.1's
  two-realization indeterminacy; the balanced-confluence audit's `hrep`
  irreducibility note — both cited, both strictly weaker);
  `docs/coordination/alpha-em.md` walked (the R2/R2-core thread; no
  (REP) closure recorded).
- **NO FIT.** Every scored check is an exact symbolic identity or an
  exact-value cross-check at $10^{-30}$; the q₀ pin strings enter only
  as evaluation points; no CODATA read; nothing wired; no content block
  or Lean file touched; no instance of any conjecture class created.
- **Scope-(a) throughout.** The determination is a corpus-survey fact
  (cited file-by-file); the falsifier outcome is support, not proof; the
  non-uniqueness is stated with its exact mechanism and scoped to real
  $q > 1$.
- **Formalize-first.** The reindex identity, the $u$-power bookkeeping,
  the reflection index map $j \mapsto -1-j$, and the Gaussian symmetry
  were derived by hand and asserted symbolically (sympy) **before** the
  60-dps numeric layer; the numerics only cross-check displayed
  identities.
- **Render-QA:** the preflight grep battery was run by hand (balanced
  `$`/`$$`/braces; no `\operatorname`; no markdown-list lines opening
  with `+`/`-`/`*` inside display math; no inline align-family
  environments; the pipeline render was not run in this sandbox — stated
  explicitly per the render-QA gate: this doc was **not
  machine-validated**).

## 6. Cross-references

- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
- The reduction to (POS)+(REP): [`2026-07-25-borel-propertime-attack-a-e.md`](2026-07-25-borel-propertime-attack-a-e.md)
- The positive kernels + fibre indeterminacy (sharpened here): [`2026-07-25-qborel-confluence-pos-attack.md`](2026-07-25-qborel-confluence-pos-attack.md)
- The `hmom` discharge + `hrep` remainder: [`2026-07-25-balanced-moment-confluence-lean.md`](2026-07-25-balanced-moment-confluence-lean.md)
- The corpus operation being represented: [`2026-07-20-keystone-bridge-c1-binding.md`](2026-07-20-keystone-bridge-c1-binding.md), [`KeystoneBridgeC1Binding.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/KeystoneBridgeC1Binding.lean)
- The formal-q-Borel closure (why "formal" is not an integral): [`2026-07-20-qlift-routeD-qborel-transform.md`](2026-07-20-qlift-routeD-qborel-transform.md)
- Kernel-convergence Mathlib gap (Fréchet–Shohat / Carleman): [`2026-07-25-kernel-convergence-mathlib-gap.md`](2026-07-25-kernel-convergence-mathlib-gap.md)
- RSZ source: `library/arxiv-0903.0853v3/0903.0853v3.pdf` (§1.2.1 pp. 7–8 — kernel menu, Jackson-style contours, no general explicit integral formula, the "optimal" output-regularity remark; Def 2.3.3; eq. (1.2))
- Probe + witness: [`rep_jackson_identification_probe.py`](../../computations/probes/rep_jackson_identification_probe.py), [`rep-jackson-identification.witness.json`](../../computations/probes/rep-jackson-identification.witness.json)
