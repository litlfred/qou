# Pre-registration — Faddeev–Niemi $|Q_H|^{3/4}$ against the QOU binding gap

**Date:** 2026-08-26 · **Bean:** `qou-thtm` · **PR:** [#5799](https://github.com/litlfred/qou/pull/5799)
**Status when committed: NO NUMBERS HAVE BEEN COMPUTED.** This file is committed
*before* the probe is written or run. The verdict is reported against the criteria
below whatever it turns out to be, including a boring one.

## Why a pre-registration

A one-parameter power law fitted against ~19 isotopes will find *something*. The
hazard is specific and named in AGENTS.md: passing a fit off as a derivation. This
document fixes, in advance, the quantity, the support criterion, the refutation
criterion, the total number of functional forms that will be tried, and the
disqualifying degrees of freedom. Trying more forms afterwards and reporting the
best is the exact fraud this guards against.

## The claim under test

Faddeev–Niemi (`library/arxiv-hep-th-9610193v1`, *Knots and Particles*) record the
Vakulenko–Kapitanski lower bound on the Faddeev-model Hamiltonian
$H = E_2 + E_4 = \int d^3x\,\tfrac{g}{2}(\partial_\mu \vec n)^2 + e^2 F^2$:

> $H \geq c\,|Q_H|^{3/4}$

with $Q_H$ the Hopf invariant. The QOU binding gap is that the per-block / pairwise
form **saturates**: `B_sym/A` tops out at 2.998 MeV/nucleon against nature's 8.790,
and ⁴He exceeds the complete-graph pairwise ceiling by 11.12 MeV
([`2026-08-25-low-isotope-binding-error-staleness-vs-gap.md`](2026-08-25-low-isotope-binding-error-staleness-vs-gap.md)).
$|Q_H|^{3/4}$ is neither per-block nor pairwise — a single non-linear functional of
one global topological charge — which is the *class* the missing term must be in.

**Hypothesis H:** the missing binding term is of the form $B = c\,|Q_H|^{3/4}$ with
$c$ a single global constant and $Q_H$ a topological charge of the nuclear
configuration fixed independently of the binding data.

## (a) Exact quantity, and the corpus source

Primary target — **total nuclear binding energy** $B_{\mathrm{AME}}(Z,A)$ in MeV, read
from `codata_constants.ame_binding_mev(Z, A)`, the public accessor for the **vendored
AME2020 publication table**, i.e. the same route the canonical witness producer
[`computations/ame_2020_binding_energies.py`](../../computations/ame_2020_binding_energies.py)
uses. No hand-typed literals. Returns `mp.mpf` inside `workdps(>=50)`.

Secondary target — the **residual** $R(A) = B_{\mathrm{AME}}(A) - B_{\mathrm{sym}}(A)$,
using the six $B_{\mathrm{sym}}$ values **as recorded in §4 of the audit cited above**
(²H 1.416·A, ⁴He 2.170·A, ¹²C 2.673·A, ⁵⁶Fe 2.898·A, ²⁰⁸Pb 2.991·A, ²³⁸U 2.998·A —
i.e. `B_sym = (B_sym/A)·A` from that table). These are **read from a committed audit,
not recomputed**, and will be labelled as such in the report.

Isotope set, fixed now (19 nuclides, $(Z,A)$):

    (1,2) (1,3) (2,3) (2,4) (3,6) (3,7) (4,9) (5,11) (6,12) (7,14)
    (8,16) (12,24) (14,28) (20,40) (26,56) (28,58) (50,120) (82,208) (92,238)

## (b) What COUNTS AS SUPPORT — fixed numeric criteria

H is supported **only if both** hold:

- **S-i.** With the exponent held at the literal Faddeev–Niemi value and a
  topologically-fixed charge — $Q_H \propto A^{d}$ with $d \in \{1, 2\}$ (see (d)) —
  and **one single global constant $c$** fitted across all 19 nuclides, the maximum
  relative residual $\max_i |B_i^{\text{model}}/B_i^{\mathrm{AME}} - 1| \le 0.10$.
- **S-ii.** In the deliberately-over-permissive free-exponent form $B = c\,A^{p}$
  (two free parameters), the fitted exponent satisfies $p \in [0.70, 0.80]$ **and**
  the maximum relative residual $\le 0.10$.

The same two criteria, applied to the secondary target $R(A)$ over the six recorded
rows, constitute support for the weaker reading that the class supplies only the
*missing* term.

## (c) What REFUTES it — fixed numeric criteria

H is refuted (scope to be classified per AGENTS.md (a)/(b)) if **either** holds:

- **R-i.** The free-exponent fit $B = c\,A^{p}$ — which has strictly *more* freedom
  than H allows — has maximum relative residual $> 0.25$ across the 19 nuclides.
  A form that cannot fit with an extra free parameter cannot fit with $p$ pinned.
- **R-ii.** The fitted exponent $p$ falls outside $[0.70, 0.80]$.

Either alone refutes. Both are evaluated on the primary and secondary targets
separately and reported separately.

## (c-bis) Pre-registered structural prediction — falsifiable

Before running anything, a structural argument is asserted and is itself put at risk:

> **S1.** For any real $p$, $B = c\,A^{p}$ implies $B/A = c\,A^{p-1}$, which is
> **strictly monotone** in $A$ for $p \neq 1$ and **constant** for $p = 1$. The
> empirical $B_{\mathrm{AME}}/A$ is **non-monotone** with an interior maximum near
> $A = 56$. Therefore **no** pure power law in $A$ — $p = 3/4$ included — reproduces
> the measured $A$-dependence, and criterion S-ii cannot be met by any $p$.

**S1 is falsified if the free-exponent fit achieves $\le 0.10$ max relative
residual.** If that happens S1 is retracted in the report. S1 makes the numerical
step a confirmation rather than a search, which is the point.

## (d) Total number of functional forms tried — **THREE**, per target

Fixed now. No fourth form will be tried, and no form will be added after seeing a
result. Any later exploration is a *new* pre-registration, reported as such.

| # | form | free params | topological reading of $Q_H$ |
|---|---|---|---|
| **F1** | $B = c\,A^{3/4}$ | 1 ($c$) | $Q_H \propto A$ — chain-like linking, degree 1 in strand count |
| **F2** | $B = c\,A^{3/2}$ | 1 ($c$) | $Q_H \propto A^{2}$ — the natural quadratic self-linking / flux scaling of a Hopf invariant |
| **F3** | $B = c\,A^{p}$ | 2 ($c$, $p$) | over-permissive superset; bounds the best the class could possibly do |

Applied to two targets (primary $B_{\mathrm{AME}}$, secondary $R$) that is
**six fits in total**. Nothing else.

**Fit rule, fixed now:** least squares in log space, minimising
$\sum_i (\ln B_i^{\text{model}} - \ln B_i^{\mathrm{AME}})^2$. For F1/F2 this is
$\ln c = \mathrm{mean}_i(\ln B_i^{\mathrm{AME}} - p \ln A_i)$; for F3 it is the
closed-form linear regression of $\ln B$ on $\ln A$. Closed form, deterministic, no
optimiser, no seed, no stopping rule to tune. Computed in `mpmath.mpf` end to end.

## (e) What is explicitly NOT support

Stated in advance so it cannot be argued afterwards:

1. **A per-isotope constant is not support.** Any $c_i$ varying with $(Z,A)$ makes
   the form a reparametrisation of the data and carries zero information. If a
   per-isotope constant is needed, that is a **refutation**, reported as one.
2. **A free $Q_H(A)$ is not support — it is unfalsifiable.** If $Q_H$ is not pinned
   independently, then for any target one may set $Q_H = (B/c)^{4/3}$ and the
   exponent $3/4$ constrains nothing whatsoever. Only a $Q_H$ fixed by topology
   ahead of the data (F1, F2) makes H a claim at all.
3. **Matching the single ⁴He excess is not support.** One constant against one
   number is not a test. It will not be reported as evidence in either direction.
4. **$p \approx 0.75$ with large residuals is not support.** S-ii requires *both*
   the exponent window and the residual bound. An exponent landing in the window
   while the fit misses the shape is a coincidence of the log-space regression, and
   will be reported as a refutation under R-i.
5. **"Suggestive" is not support.** That $3/4$ sits between the SEMF surface
   exponent $2/3$ and volume exponent $1$ is a remark about two other numbers.
6. **Corroboration by a second construct landing near the same value is not
   support** — that is the numerology signature already recorded at §7 of the
   binding audit ($a_V = 7.5836$ vs $2 m_e \cdot 8G \approx 7.49$).

## Prior expectations, recorded so they cannot be revised

- The direction is expected wrong: $Q^{3/4}$ is sub-linear, so with $Q_H \propto A$
  the binding *per nucleon* falls like $A^{-1/4}$ where the corpus needs it to rise.
- The corpus's own `rem:hopf-link-non-magic` records $\mathrm{Vol}(\mathrm{Hopf}) = 0$
  (Seifert-fibered, not hyperbolic) and places the Hopf link entirely in
  $E_\infty^{0,*}$ — the *descended Markov-trace* slot, which is exactly the piece
  that contributes $\lesssim 0.5\%$ of magic-shell binding. The Hopf object is
  already **degenerate** in this setting, which cuts against a naive transfer before
  any number is computed.
- Corpus-grep run before writing this file: `Niemi` / `Vakulenko` / `hopfion` /
  `knot-soliton` / `Hopf invariant` across `docs/audits/`, `docs/coordination/`,
  `content/`, `computations/`, and `library/INDEX.md`. The energy-bound reading
  appears **only** in
  [`2026-08-25-recent-knot-particle-uploads-vs-our-identifications.md`](2026-08-25-recent-knot-particle-uploads-vs-our-identifications.md) §3
  and in bean `qou-thtm`. No prior derivation, no prior refutation. The item is
  genuinely untested in this corpus — this is not a re-declaration of a closed one.

## Reporting commitment

The report will state the verdict against (b)/(c) verbatim, name the scope (a) or
(b) per AGENTS.md, cite the invariant if (b), and say plainly if the honest answer is
"this does not bear on the gap". No float64 anywhere; no agreement reported as
"exact" or "to N digits".
