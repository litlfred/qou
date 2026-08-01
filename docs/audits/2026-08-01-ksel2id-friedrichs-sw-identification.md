# KSel-2-ID — Stieltjes–Wigert / q-Laguerre identification and the Friedrichs–Krein selection: the balanced family is q-Laguerre up to one explicit SW-Gaussian; the extremal extensions are q-lattice measures aligned with the u ≡ 1 class; the bar reflection does NOT act on the extension circle

**Date:** 2026-08-01 · **Bean:** qou-0ms0 (KSel-2 follow-up, extension-identification route)
**Tier:** AUDIT — NO FIT, nothing wired; no content block or Lean file
touched. Namespace `ksel2id_*`. Parent audit:
[`2026-08-01-ksel2-gns-favard-canonicity.md`](2026-08-01-ksel2-gns-favard-canonicity.md)
(its §5 items 2–3 are executed here). Sibling selection audits KSel-1 /
KSel-3 untouched; their discriminator questions are answered below at
measured tier.

**Probes** (both exit 0, all assertions passed):

- [`computations/probes/ksel2id_sw_identification_probe.py`](../../computations/probes/ksel2id_sw_identification_probe.py)
  → [`ksel2id-sw-identification.witness.json`](../../computations/probes/ksel2id-sw-identification.witness.json)
  — 5 assertions (sympy exact + mpmath; quadrature cross-checks
  $10^{-20}$, Euler/Jackson sums $10^{-30}$; both q₀ pins).
- [`computations/probes/ksel2id_friedrichs_selection_probe.py`](../../computations/probes/ksel2id_friedrichs_selection_probe.py)
  → [`ksel2id-friedrichs-selection.witness.json`](../../computations/probes/ksel2id-friedrichs-selection.witness.json)
  — 8 assertions (exact-ℚ qd algorithm + mpf qd certified by moment
  reproduction $< 10^{-300}$; truncation eigen-study; both q₀ pins).

Notation: $p = 1/q \in (0,1)$, $\tilde q = \sqrt q$,
$L = \ln \tilde q$, $(p;p)_k = \prod_{j \le k}(1 - p^j)$; balanced
moments $m_k = q^{-k(k-1)/4}[k]_q!$ (one-sided $[k]_q$).

## 1. Literature identification (Task 1): SW-proper NO-MATCH; SW an exact factor; q-Laguerre EXACT for the one-sided convention

Exact base-$p$ rewrite (probe S1, symbolic $k \le 12$):

$$
[k]_q! \;=\; p^{-k(k-1)/2}\,\frac{(p;p)_k}{(1-p)^k},
\qquad
m_k \;=\; \tilde p^{\,-k(k-1)/2}\,\frac{(p;p)_k}{(1-p)^k},
\quad \tilde p = \sqrt p .
$$

The balanced family is a Gaussian (log-quadratic) part at base
$\tilde q$ times a q-Pochhammer part at base $q$ — mixed bases; the
balanced convention is exactly the half-step (bar-symmetric) point.

| Hypothesis | Verdict | Mechanism |
|---|---|---|
| balanced = SW-proper (pure log-normal / Stieltjes 1894) under some $s \mapsto c\,s^a$ | **NO-MATCH — scope-(b), cited invariant** | log-normal moment sequences are log-QUADRATIC in $k$, and log-quadraticity is invariant under every affine-in-log map (probe S2, exact). The balanced family is exactly not log-quadratic: $m_{k+2}m_k/m_{k+1}^2 = \tilde q\,\frac{1-p^{k+2}}{1-p^{k+1}}$ (exact symbolic), the second factor $> 1$ and strictly decreasing — so $\Delta^2 \ln m_k$ is non-constant. Residual vs the quadratic through $k = 0,1,2$ at the pins: $-0.29$ nats at $k=3$, $-25.6$ at $k=12$ (O(1) at accessible orders; $\Delta^2$ deviation decays only as $p^k$) |
| SW as an exact **factor** | **EXACT** | $m_k = G_k J_k$ with $G_k = e^{Lk^2/2 - Lk/2}$ = the moments of $\mathrm{LN}(-L/2, L)$ = the classical SW weight at $t_{\rm sw} = 1/\tilde q$ pushed by $s \mapsto s\,\tilde q^{-3/2}$ (exact parameter match; this is precisely the KSel-3 "one Gaussian"), and $J_k = (p;p)_k/(1-p)^k$ = the moments of the Jackson atomic measure $(p;p)_\infty \sum_m \frac{p^m}{(p;p)_m}\delta_{p^m/(1-p)}$ (Euler sum, rel $< 10^{-30}$ at $q = 1.2$ + both pins) — compactly supported in $(0, 1/(1-p)]$, hence **determinate**. So **balanced = SW(base $\tilde q$) ⊛ Jackson**: the indeterminacy core of the binding-kernel family IS Stieltjes' 1894 log-normal example at base $\sqrt q$ ([`christiansen2003sw`], [`berg1995`]) |
| one-sided = q-Laguerre ($\alpha = 0$, [`moak1981`]) | **EXACT** | the weight $w(x) = 1/(-x;p)_\infty$ satisfies $w(px) = (1+x)w(x)$, giving the exact moment recurrence $\nu_{k+1} = p^{-(k+1)}(1-p^{k+1})\nu_k$ (quadrature cross-check rel $< 10^{-20}$ at $p = 5/6$ + both pins), hence normalized moments $\rho_k = p^{-k(k+1)/2}(p;p)_k$; symbolically exact for $k \le 12$: $[k]_q! = \rho_k\,(p/(1-p))^k$ — i.e. the one-sided normalizer family is the $\alpha = 0$ q-Laguerre (generalized SW) family **under the pure scaling $s \mapsto \frac{p}{1-p}\,s$** |
| balanced = q-Laguerre under affine-in-log | **NO** (same scope-(b) invariant), but with an **exact one-Gaussian bridge** | $m_k \cdot p^{-k(k-1)/4} = [k]_q!$ exactly: one extra copy of the same SW Gaussian $\mathrm{LN}(-L/2,L)$ carries balanced → one-sided → q-Laguerre. The balanced member is the "half-dressed" bar-symmetric midpoint |

**Answer to the working hypothesis:** *yes for the one-sided
convention* — it is exactly the classical q-Laguerre/generalized-SW
indeterminate family after an explicit scaling; *structurally yes,
literally no for the balanced convention* — its indeterminacy core is
exactly the classical SW measure at base $\tilde q$, but the balanced
sequence itself is not any SW/log-normal family's affine-in-log image
(exact obstruction), sitting instead exactly one SW-Gaussian
convolution away from q-Laguerre.

## 2. Friedrichs / Krein selection (Task 2): none of the named candidates; the extremal pair are q-lattice measures on the u ≡ 1 class

Method (probe 2): Jacobi data $(\alpha_k, \beta_k)$ from the balanced
moments by the quotient-difference algorithm — exact ℚ at
$r = 21/20$ ($K = 26$; Favard positivity now **exact to depth 25**,
extending the parent audit's depth 9) and mpf at $r = 6/5$
($q = 2.0736$, $K = 48$, certified by moment reproduction
$< 10^{-300}$ + exact cross-check). Then:

- **Friedrichs by truncation:** the polynomials are by definition a
  form core of $J_F$, so by min–max every truncation eigenvalue
  $\lambda_j(N)$ decreases to $\lambda_j(J_F)$ (verified strictly
  monotone for all $j$; [`simon1998`], [`pedersen1995`]).
- **Krein by Gauss–Radau at 0:** boundary shift
  $t_N = P_N(0)/P_{N-1}(0)$ pins an eigenvalue at 0 ($< 10^{-80}$);
  the limit is the canonical solution with $0 \in \mathrm{supp}$ = the
  Krein extension measure ([`pedersen1995`]; numerically Cauchy,
  rel $< 10^{-4}$).

Measured results at $r = 6/5$ ($q = 2.0736$, $N = 48$; eigenvalues
Cauchy to $2\times10^{-7}$…$1.4\times10^{-4}$ over the used window):

| Quantity | Value |
|---|---|
| $\lambda_F = \inf \mathrm{spec}\, J_F$ | $0.336681762\ldots$ — **strictly positive** |
| low Friedrichs atoms | $0.33668,\ 1.86407,\ 5.36043,\ 13.0594,\ \ldots$ |
| Krein: atom at $0$ | mass $0.23641 = 1/\sum_{k<48} p_k(0)^2$ (Radau identity $< 10^{-25}$; $\sum p_k(0)^2 = 4.22990$, partials convergent — an independent indeterminacy corroboration) |
| low positive Krein atoms | $0.86770,\ 3.19731,\ 8.36713,\ \ldots$ — **interlacing** the Friedrichs atoms |
| atom spacing, in $\tilde q$-steps | strictly decreasing $2.259 \to 2.0012$ over $j \le 18$: asymptotically **2 steps = one $q$-step** — the extremal supports are $q$-lattices, not $\tilde q$-lattices |
| $\tilde q$-class of Friedrichs atoms | monotone drift $0.047 \to 0.8025$; Aitken limit $0.80534$ vs the $u{=}1$ class $\varphi_1 = \mathrm{frac}(\log_{\tilde q} \frac{q}{q-1}) = 0.80524$ — agreement $1.0\times10^{-4}$; the half-shifted $u = \tilde q^{1/2}$ class ($0.30524$) rejected by $0.5$ |
| $\tilde q$-class of Krein atoms | Aitken limit $0.80509$ — the **same** class ($1.6\times10^{-4}$) |
| extension-circle sweep ($N = 44$) | $\lambda_{\min}(s\,t_N)$ strictly decreasing along $s = 0, \tfrac14, \tfrac12, \tfrac34, 1$ from $0.33668$ to $2\times10^{-114}$; at $s = \tfrac32$ the smallest eigenvalue is negative — beyond-Krein boundary conditions leave the Stieltjes sector |
| q₀ pins (muon + proton, $K = 24$) | $\beta_k > 0$, reproduction $< 10^{-500}$, $\lambda_{\min}(N)$ strictly decreasing and positive ($0.1027, 0.0882, 0.0788$ at $N = 16/20/24$ — upper bounds for $\lambda_F$, not yet converged), Radau pin $< 10^{-40}$, mass-at-0 identity $< 10^{-20}$. The pins sit deep in the pre-asymptotic window ($\tilde q - 1 \approx 0.054$); grid-class asymptotics are read at the strong-deformation point, stated as such |

**Selection verdict.**

1. **NONE of the three named candidates is the Friedrichs or the Krein
   measure** — scope-(b) with cited invariant: in the indeterminate
   case every self-adjoint extension has compact resolvent, so its
   spectral measure is discrete with no finite accumulation point and
   (Friedrichs) $\lambda_F > 0$ ([`simon1998`], [`berg1995`]); the two
   atomic candidates (theta grids $\frac{u}{1-p}\tilde q^{\mathbb Z}$)
   accumulate at 0, and the a.c. log-normal candidate is continuous.
   Numerically: the lowest Friedrichs atom is off the $u = 1$ lattice
   by $0.21$ of a $\tilde q$-step. **The u-continuum members are
   interior (non-extremal) Nevanlinna solutions** — the parent audit's
   caution ("convolutions are generically not N-extremal") is
   confirmed, and the conjecture block's "three frames of one object"
   phrasing needs the refinement: the u-translate circle and the
   extension circle are two DIFFERENT circles inside the same solution
   set, meeting only asymptotically (next item).
2. **New structure (measured):** the Friedrichs and Krein supports are
   asymptotically the two **complementary $q$-sublattices of the one
   $u \equiv 1$ theta grid** — spacing exactly two $\tilde q$-steps,
   common class = $\varphi_1$ to $10^{-4}$, interlacing making
   $\mu_F \cup \mu_K$ asymptotically reconstruct the $u = 1$ support.
   The extension circle's canonical pair therefore *selects the
   $u \equiv 1$ class* (asymptotic-class sense, measured tier): the
   KSel-1 half-step discriminator between the two $\sigma$-fixed
   candidates $u \equiv 1$ vs $u \equiv \tilde q^{1/2}$ is answered
   **toward $u \equiv 1$** — the Attack-B presentation point, which is
   the $\theta_2$-characteristic point of KSel-3, *not* the
   $\theta_3$ self-dual point.
3. **Friedrichs maximizes the smallest support point** (consistent
   with [`pedersen1995`]): $\inf\mathrm{supp}\,\mu_F = \lambda_F
   \approx 0.3367 > 0$, while Krein has an atom at 0 and every
   u-translate/a.c. candidate has $\inf\mathrm{supp} = 0$.

## 3. Bar reflection (Task 3): σ fixes the SW factor and the u-classes {1, q̃^{1/2}} but does NOT act on the extension circle

$\sigma\colon s \mapsto \tilde q^{-1}/s$.

- **Exact (probe F8i):** $\sigma$ fixes the SW factor
  $\mathrm{LN}(-L/2, L)$ (pushforward invariance — completion of the
  square), and on $\tilde q$-grid classes acts as
  $\varphi \mapsto -\varphi \bmod 1$, whose fixed classes are exactly
  $\{0, \tfrac12\}$ = the $u \equiv 1$ and $u \equiv \tilde q^{1/2}$
  pair (re-derives the ksel1 R4 fixed points).
- **Obstruction (scope-(b), cited invariant — probe F8ii):** every
  extension measure has smallest positive support point $s_{\min} > 0$
  (discrete spectrum; the Krein measure additionally has an atom AT 0,
  whose $\sigma$-image is not a finite measure on $(0,\infty)$). Hence
  $\mathrm{supp}\,\sigma_*\mu \subset (0, 1/(\tilde q\, s_{\min})]$ is
  **bounded**, so its moments grow at most geometrically — while
  $m_{k+1}/m_k$ is strictly increasing and unbounded (exact). So
  $\sigma_*$ of an extension measure is **never** a representing
  measure: **the bar reflection does not map the extension circle to
  itself by pushforward, has no fixed points there, and does NOT
  exchange Friedrichs and Krein.** The closing question of
  [`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
  ("if the bar reflection exchanges the two extremal extensions, the
  symmetric points become canonical") has a **false premise in the
  pushforward reading**.
- **Numeric corroboration (F8iii):** $\sigma$-moments of the truncated
  Friedrichs measure vs $m_k$: ratio $1.4367$ at $k=1$ and
  $1.2\times10^{-4}$ at $k=8$ ($r = 6/5$); $2.8801$ at $k=1$
  ($r = 21/20$).
- **What survives (scope-(a), open):** a *non-pushforward* action of
  the bar involution on the Nevanlinna parameter (e.g. conjugation
  through the SW-factor deconvolution of §1) is not excluded and not
  constructed here. Note also the suggestive measured fact: the
  extremal pair's common asymptotic class is $u \equiv 1$ — one of
  $\sigma$'s two fixed classes — so a bar-compatible canonicity
  statement may yet exist at the *asymptotic-class* level; recorded,
  not interpreted.

## 4. What this changes for the (REP)/KSel campaign

1. The kernel-selection problem now has a **literature home**: the
   balanced family is the Jackson-dressed classical SW problem
   (equivalently, one SW-Gaussian away from Moak's q-Laguerre family);
   Christiansen's complete solution description applies to the SW core.
2. The (REP) "three frames" statement is refined: **u-circle ≠
   extension circle**. The u-translates are interior Nevanlinna
   solutions; the canonical (extension) solutions are new $q$-lattice
   measures computed here for the first time.
3. Two candidate closures of the extension choice died or moved:
   bar-reflection exchange of F/K — **refuted** (pushforward sense,
   scope-(b)); "distinguished extension = one of the named corpus
   kernels" — **refuted** (scope-(b), discreteness). What is *gained*
   is a measured selection datum: **both canonical extensions align
   asymptotically with the $u \equiv 1$ class**, sharpening what a
   derivation-tier selection principle must now produce (either a
   principle choosing Friedrichs vs Krein — e.g.
   Friedrichs-minimality/GNS-internality per the parent audit §5 — or
   a principle promoting the asymptotic $u \equiv 1$ alignment to a
   statement about the corpus kernel).

## 5. Honest gaps / tier statement

- The **Friedrichs identification of the truncation limit** is the
  variational/form-core argument (rigorous for eigenvalue limits); the
  **Krein identification of the Radau limit** is literature-cited
  ([`pedersen1995`]) + numerically Cauchy — not re-proved here.
- The **grid classes are asymptotic measurements** at the
  strong-deformation point $q = 2.0736$ (Aitken-extrapolated,
  agreement $10^{-4}$), scope-(a) measured; at the q₀ pins the
  pre-asymptotic window prevents any class readout (stated in the
  witness; no class claim is made at the pins).
- $\lambda_F$ at the pins is bracketed only from above
  ($\le 0.0788$, still decreasing at $N = 24$); positivity at the pins
  is structural (discreteness + F ≠ K), not yet numerically converged.
- No Lean was written; no conjecture-class instance created; the
  target conjecture is unchanged in kind.

## 6. Discipline

- **Corpus-grep (all four paths).** `Stieltjes-Wigert|Stieltjes–Wigert|
  q-Laguerre|Moak|Friedrichs|Krein|Radau|N-extremal` over
  `docs/audits/`, `docs/coordination/`, `content/`, `computations/`:
  prior state = the parent KSel-2 audit (names Friedrichs/Krein as
  candidates, computes nothing about them), the `simon1998` /
  `ismail-masson1994` bibliography entries, and the ksel1/ksel3
  sibling audits — no prior SW/q-Laguerre identification, no prior
  extension-measure computation, no prior bar-reflection-on-extensions
  result. Coordination ledgers (`option-e.md`, the 2026-07-24
  binding-mass workplan) show no closure of these items.
- **NO FIT.** Every scored check is an exact symbolic identity, an
  exact rational computation, or a numeric cross-check of a displayed
  identity at stated tolerance; the q₀ pin strings enter only as
  evaluation points; no CODATA read; nothing wired. The measured
  numbers ($\lambda_F$, grid classes, Aitken limits) are measurements
  of corpus-defined objects, consumed by nothing.
- **Refutation hygiene.** The three scope-(b) exclusions each carry a
  cited invariant: (i) log-quadraticity invariance under affine-in-log
  maps (SW-proper NO-MATCH); (ii) compact resolvent / discrete
  spectrum of extensions in the indeterminate case (named candidates
  are not extension measures); (iii) bounded support vs
  superexponential moment growth (no pushforward σ-action). Everything
  else is scope-(a) or measured tier.
- **Formalize-first.** The load-bearing identities (base-$p$ rewrite,
  $\Delta^2$ second-ratio identity, the q-Laguerre weight functional
  equation and its moment recurrence, the Radau mass-at-0 identity,
  the σ completion-of-the-square) were derived by hand and asserted
  symbolically/exactly before the numeric layers; the eigen-study
  numerics measure structure the theory does not supply
  (grid classes), labeled as measurements.
- **Long-compute:** probe 1 ≈ 2 min, probe 2 ≈ 4 min wall; both run
  with `python3 -u ... | tee` logs (`/tmp/ksel2id_sw.log`,
  `/tmp/ksel2id_friedrichs.log`); bottleneck is the exact-ℚ qd leg at
  $K = 26$ (~60 s).
- **Render-QA:** the preflight grep battery was run by hand (balanced
  `$`/`$$`/braces; no `\operatorname`; no markdown-list lines opening
  with `+`/`-`/`*` inside display math; no inline align-family
  environments; display `$$` on their own lines). The pipeline render
  was not run in this sandbox — **this doc was not machine-validated**,
  stated per the render-QA gate.

## 7. Cross-references

- Parent audit (executed §5 items): [`2026-08-01-ksel2-gns-favard-canonicity.md`](2026-08-01-ksel2-gns-favard-canonicity.md)
- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
- Sibling selection audits: [`2026-08-01-ksel1-singularity-selection.md`](2026-08-01-ksel1-singularity-selection.md) (half-step discriminator — answered §2), [`2026-08-01-ksel3-modular-double-covariance.md`](2026-08-01-ksel3-modular-double-covariance.md) (the "one Gaussian" = the SW factor, §1)
- The (REP) continuum: [`2026-08-01-rep-jackson-identification.md`](2026-08-01-rep-jackson-identification.md)
- Bibliography registered this tranche (all verified 2026-08-01;
  see notes in [`content/schema/references.ts`](../../content/schema/references.ts)):
  [`christiansen2003sw`] (JMAA 277 (2003) 218–245, DOI
  10.1016/S0022-247X(02)00534-6), [`berg1995`] (JCAM 65 (1995) 27–55,
  DOI 10.1016/0377-0427(95)00099-2), [`pedersen1995`] (JAT 83 (1995)
  289–307; DOI not resolvable from the sandbox, entry carries the
  verified ScienceDirect URL), [`moak1981`] (JMAA 81 (1981) 20–47,
  DOI 10.1016/0022-247X(81)90048-2). Already registered: [`simon1998`],
  [`ismail-masson1994`].
- Probes + witnesses: [`ksel2id_sw_identification_probe.py`](../../computations/probes/ksel2id_sw_identification_probe.py), [`ksel2id-sw-identification.witness.json`](../../computations/probes/ksel2id-sw-identification.witness.json), [`ksel2id_friedrichs_selection_probe.py`](../../computations/probes/ksel2id_friedrichs_selection_probe.py), [`ksel2id-friedrichs-selection.witness.json`](../../computations/probes/ksel2id-friedrichs-selection.witness.json)
