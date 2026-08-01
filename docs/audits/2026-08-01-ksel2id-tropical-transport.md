# KSel-2-ID transport: the `E`-shift of the lattice class is exact algebra — the perturbation-lemma gap is dissolved, not proved

**Date:** 2026-08-01 · **Bean:** `qou-uazz`
**Tier:** AUDIT + Lean. NO FIT, nothing wired; the target conjecture
([`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md))
is unchanged in kind. Parent:
[`2026-08-01-ksel2id-u1-promotion.md`](2026-08-01-ksel2id-u1-promotion.md)
(this closes its §4 gap 1 by *removing the need for it*, not by proving it).

**Probe:** [`ksel2id_tropical_transport_probe.py`](../../computations/probes/ksel2id_tropical_transport_probe.py)
→ [`ksel2id-tropical-transport.witness.json`](../../computations/probes/ksel2id-tropical-transport.witness.json)
— 3 assertion blocks, exit 0 (sympy exact + mpmath 60 dps).
**Lean:** [`TropicalClassTransport.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/TropicalClassTransport.lean),
sorry-free, `lean`-direct exit 0.

Notation as in the parent: $q > 1$, $p = 1/q$, $\tilde q = \sqrt q$
(the Lean half-variable $v$), $E = 1/(1-p) = q/(q-1)$; balanced moments
$m_k$, SW core moments $G_k = \tilde q^{\,k(k-1)/2}$; the $u \equiv 1$
class $\varphi_1 = \mathrm{frac}(\log_{\tilde q} E)$.

## 1. The problem, and why it did not need the lemma it was blocked on

The parent audit derived the balanced family's class from the SW core's
by comparing **Jacobi data**: the balanced $(\alpha_n, \beta_n)$
converge geometrically to the $E$-scaled SW ones, so *if* geometric
convergence of Jacobi data implied equality of asymptotic extremal-support
class, the balanced class would be $\varphi_1$. That implication — the
**perturbation lemma** — was unproved, and it is not a soft statement:
extremal supports are global spectral data, not continuous functionals of
finitely many coefficients.

The observation here is that the comparison does not have to be made on
the Jacobi data at all. Run it on the **moment ratios** — the tropical
(Newton-polygon) roots — and the transport is exact:

$$
m_k = G_k\, E^k\,(p;p)_k
\quad\Longrightarrow\quad
\frac{m_{k+1}}{m_k}
= \underbrace{\frac{G_{k+1}}{G_k}}_{=\ \tilde q^{\,k}\ \text{(exact)}}
\cdot\, E \,\cdot\, \bigl(1 - p^{\,k+1}\bigr).
$$

The factorization is the merged exact one
([`SWJacksonMomentFactorization.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SWJacksonMomentFactorization.lean));
the two ratio identities are proved here. Taking $\log_{\tilde q}$,

$$
\log_{\tilde q}\!\frac{m_{k+1}}{m_k}
= k \;+\; \log_{\tilde q} E \;+\; \log_{\tilde q}\bigl(1 - p^{\,k+1}\bigr),
$$

so the integer part is irrelevant to the class, the shift is exactly
$\log_{\tilde q} E$, and the entire error is the single explicit term
$\log_{\tilde q}(1 - p^{k+1})$, which is bounded in closed form and dies
geometrically at rate $p$.

## 2. Results

| # | Statement | Tier |
|---|---|---|
| T1 | $m_{k+1}/m_k = \tilde q^{\,k} E (1 - p^{k+1})$ | **exact** (sympy $k \le 12$; **Lean** `balancedNormalizer_ratio`, division-free, generic field) |
| T2 | $G_{k+1}/G_k = \tilde q^{\,k}$, so the SW core's tropical class is $0$ at **every** $k$ | **exact** (sympy; **Lean** `swMoment_ratio`) — no asymptotics at all |
| T3 | $\lvert \mathrm{class}(k) - \varphi_1 \rvert \le \lvert\log_{\tilde q}(1 - p^{k+1})\rvert$, decaying at rate exactly $p$ | **exact bound + verified** (8-rung $q$-ladder incl. both pins; the bound dominates at every $k$; measured rate matches $p$ within the *predicted* $O(p^{k+1})$ correction) |
| T4 | $\log_{\tilde q}$-error $\to 0$, hence the balanced tropical class $\to \varphi_1$ | **Lean** `tendsto_jacksonLogCorrection` (wall side, `ℝ`) |

Effect on the gap list. The chain

  (SW class) $\xrightarrow{\ \text{perturbation lemma (unproved)}\ }$ (balanced class)

is replaced by

  (SW class $= 0$, exact) $\xrightarrow{\ \text{exact algebra}\ +\ \text{explicit geometric limit}\ }$ (balanced class $= \varphi_1$).

**The perturbation lemma is no longer on the critical path.** It is
neither proved nor refuted here; it is simply not needed for the class
statement, because the route that needed it has been replaced by one
that does not.

## 3. What still remains (unchanged in kind)

One analytic statement: **extremal support class = tropical class**
(that the $N$-extremal support points are asymptotic to the successive
moment/coefficient ratios). This is precisely the input the **pure SW
core already required** — the $A_w$ zero asymptotics
$\zeta_n = \tilde q^{\,2n-1}(1 + O(\tilde p^{\,n}))$, the parent audit's
§4 gap 2, classical for $q$-series of this type but not imported as a
proved theorem. So the transport adds **no new analytic debt**; it
removes one of the two gaps and leaves the other exactly where it was.

Not claimed: that the Friedrichs/Krein measures *are* the tropical
lattice (that is the residual above); any statement about the finer
odd/even sublattice split (ratios see the class, not the sublattice);
anything about the conjecture's own content.

## 4. Honest correction recorded

The probe's first draft asserted that the tropical route "certifies at
the pins at tiny $k$" — the run **refuted this**: reaching $10^{-12}$ at
the muon pin takes $k \approx 293$, comparable to the truncation route's
$N \approx 375$. The claim was corrected in place before commit. The
tropical route's advantage is of **kind, not speed**: its error carries a
closed-form bound, so the class limit is a theorem rather than an
extrapolation, and no computation at any depth is needed to establish
it — the reported $k$ values are illustrative only. The inverse pin is
evaluated through its $>1$ representative, so its row duplicates the
muon pin by construction (bar-invariance) and is not an independent
datum; this too is recorded in the witness.

## 5. Discipline

- **Corpus-grep (all four paths).** `multiplicative convolution |
  Mellin convolution | perturbation lemma | N-extremal | lattice class`
  over `docs/audits/`, `docs/coordination/`, `content/`,
  `computations/`: the parent/grandparent KSel-2 audits and
  [`rep_jackson_identification_probe.py`](../../computations/probes/rep_jackson_identification_probe.py)
  (Mellin structure of the Jackson factor — cited, not re-derived). No
  prior statement of the moment-ratio transport; no prior closure.
- **NO FIT.** Every scored item is an exact symbolic identity or a
  numeric check of a *displayed* bound. The one tolerance in the probe
  is **derived from the displayed expansion** ($O(p^{k+1})$ relative
  correction to the ratio), not tuned: the first attempt used an
  arbitrary $10^{-20}$, which the data failed, and the fix was to
  replace it with the predicted bound — not to loosen it.
- **Refutation hygiene.** No scope-(b) claims. The perturbation lemma is
  recorded as *not needed*, explicitly **not** as refuted.
- **Formalize-first.** The ratio identities were derived by hand,
  checked symbolically, and proved in Lean before any numeric layer; the
  numerics only exercise the displayed bound.
- **Render-QA:** preflight grep battery run by hand (balanced `$`/`$$`
  and braces; no `\operatorname`; no line inside `$$…$$` opening with
  `+`/`-`/`*`; no inline align-family environments). The pipeline render
  was **not** run for this doc — **not machine-validated**, stated per
  the render-QA gate.

## 6. Cross-references

- Parent (the gap this dissolves): [`2026-08-01-ksel2id-u1-promotion.md`](2026-08-01-ksel2id-u1-promotion.md)
- The factorization it rests on: [`2026-08-01-ksel2id-friedrichs-sw-identification.md`](2026-08-01-ksel2id-friedrichs-sw-identification.md), Lean [`SWJacksonMomentFactorization.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SWJacksonMomentFactorization.lean)
- SW core Jacobi data (Lean): [`SWCoreJacobi.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SWCoreJacobi.lean)
- The two bar-fixed candidate classes: [`2026-08-01-bar-reflection-grid-selection-lean.md`](2026-08-01-bar-reflection-grid-selection-lean.md)
- Target conjecture: [`schwinger-measure-computational-time.md`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md)
