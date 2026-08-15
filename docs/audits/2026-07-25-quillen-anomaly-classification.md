# Quillen's holomorphic anomaly as the organizing principle: exact gates vs magnitude legs

**Date:** 2026-07-25 · **Bean:** qou-2nm8 · **Axis:** Bring modulus / α_EM magnitude leg /
det′Δ lineage · **Tier:** scope-(a), audit-only · **Discipline:** NO FIT; nothing wired;
no new no-go claimed — this is a classification, the existing negatives stand on their own.

**Probe:** [`computations/probes/quillen_anomaly_classification_probe.py`](../../computations/probes/quillen_anomaly_classification_probe.py)
→ [`quillen-anomaly-classification-probe.witness.json`](../../computations/probes/quillen-anomaly-classification-probe.witness.json)
— 9/9 assertions passed, exit 0.

**The owner's question:** *"are we seeing Quillen's holomorphic anomaly?"* — asked against
the uploaded paper

> **AGMV**: L. Alvarez-Gaumé, G. Moore, C. Vafa, *Theta Functions, Modular Invariance,
> and Strings*, Commun. Math. Phys. **106**, 1–40 (1986). (`library/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invariance-and-strings.pdf`;
> © Springer-Verlag 1986. Sect. 2 *Fermions on a Torus*; Sect. 4 *Holomorphic
> Factorization*; Sect. 5 *Chiral Dirac Determinants*.)

**Answer (grounded below): yes, precisely.** The corpus's verified genus-1 identity
$\det{}'\Delta(E_\tau) = (\mathrm{Im}\,\tau)^2\,\lvert\eta(\tau)\rvert^4$ is an
anomaly-carrying Quillen-norm object (its Quillen curvature is computed exactly in §1);
the session's exact gates ($t_5(\tau_0) = -10$, the Fricke companion $-25/2$, the
$j$-values, the $a_p$ integers) live in the anomaly-free weight-0 holomorphic sector; and
every stuck magnitude leg (the polarized $\det{}'\Delta$ measure $1.38758$, the
product-period $1.4724\times 10^{12}$, the per-factor measures, the retracted $8.226$)
is an anomaly-carrying norm. The split the sessions kept rediscovering empirically — exact
rational gates on one side, no-distinguished-constant magnitudes on the other — is exactly
Quillen's holomorphic-anomaly dichotomy (AGMV Sect. 4).

## 1. The exact curvature (formalize-first anchor; symbolic + numeric)

**Theorem-level statement.** With $\tau = x + iy \in \mathbb{H}$ and the Wirtinger
operators $\partial_\tau = \tfrac12(\partial_x - i\partial_y)$,
$\partial_{\bar\tau} = \tfrac12(\partial_x + i\partial_y)$ (so
$\partial_\tau\partial_{\bar\tau} = \tfrac14(\partial_x^2 + \partial_y^2)$, verified
symbolically on a generic $C^2$ function):

$$
\partial_\tau\partial_{\bar\tau}\,
\log\bigl[(\mathrm{Im}\,\tau)^2\,\lvert\eta(\tau)\rvert^4\bigr]
\;=\;
\partial_\tau\partial_{\bar\tau}\,\bigl(2\log \mathrm{Im}\,\tau\bigr)
\;=\;
-\frac{1}{2\,(\mathrm{Im}\,\tau)^2}
\qquad \text{(exact)} .
$$

The $\lvert\eta\rvert^4 = \lvert\eta^2\rvert^2$ part contributes nothing: $\eta$ is
nonvanishing on $\mathbb{H}$, so
$\log\lvert\eta\rvert^4 = 2\log\eta(\tau) + 2\log\overline{\eta(\tau)}$ is
$\partial\bar\partial$-flat (mixed derivative of $f(u)+g(v)$ in independent variables is
identically zero — asserted in sympy). The entire curvature is carried by the metric factor
$2\log\mathrm{Im}\,\tau$, with the exact coefficient $-\tfrac12$ against the hyperbolic
form $1/(\mathrm{Im}\,\tau)^2$.

**Consequence (quantitative "not $\lvert f\rvert^2$").** The curvature is nonzero at every
$\tau \in \mathbb{H}$, so $\det{}'\Delta(E_\tau)$ is **not** $\lvert f(\tau)\rvert^2$ for
any holomorphic $f$ — the obstruction Quillen's theorem quantifies (AGMV Sect. 4,
Eqs. (4.1)–(4.2): $\det_\zeta = \lvert\mathrm{det}\,D\rvert^2 e^{-q}$ with the
non-holomorphic counterterm $q$ — AGMV's own symbol, quoted verbatim; it is their
Eq. (4.2) counterterm functional, unrelated to the substrate deformation parameter; determinant-line curvature
$\bar\partial\partial\log\lVert\sigma\rVert$, Eqs. (4.17)–(4.18), computed via
Bismut–Freed). The torus special case is already exhibited in AGMV Sect. 2: the twisted
determinant $\mathrm{Det}(\theta,\phi) = \vartheta{\genfrac{[}{]}{0pt}{1}{\theta}{\phi}}(0\,\vert\,\tau)/\eta(\tau)$
(their Eq. (2.3)) fails to be holomorphic in $u = \phi + \tau\theta$ *only* through the
quadratic exponent term — "*this is an example of a holomorphic anomaly which will be
discussed in detail in Sect. 4*".

**Numeric confirmation (mpmath finite differences).** Quarter-Laplacian of
$F(x,y) = \log(y^2\lvert\eta(x+iy)\rvert^4)$ vs $-1/(2y^2)$:

| point | quarter-Laplacian | rel. deviation |
|---|---|---|
| Bring $\tau_0 = -0.5 + 0.186676i$ | $-14.34805495455277\ldots$ | $< 10^{-100}$ (0 at working precision) |
| generic $\tau = 0.31 + 1.17i$ | $-0.36525677551318\ldots$ | $1.1\times 10^{-111}$ |

Anchored by the closed form $\lvert\eta(i)\rvert = \Gamma(\tfrac14)/(2\pi^{3/4})$
(asserted $< 10^{-40}$) — which is itself instructive: at CM points a Quillen norm takes
*period-type* (Chowla–Selberg $\Gamma$-factor) values, not the rational/algebraic values
of the holomorphic sector.

## 2. The anomaly-cancellation identity in $t_5$ (exact bookkeeping)

$\eta$ has weight $\tfrac12$, so its Petersson-invariant norm is
$N(\tau) = (\mathrm{Im}\,\tau)^{1/4}\lvert\eta(\tau)\rvert$ ($\mathrm{SL}(2,\mathbb{Z})$-invariance
asserted numerically for $T$ and $S$ to $< 10^{-40}$). Writing
$t_5 = (\eta(\tau)/\eta(5\tau))^6$ in these terms and using the exact bookkeeping
$\mathrm{Im}(5\tau) = 5\,\mathrm{Im}\,\tau$:

$$
\lvert t_5(\tau)\rvert
\;=\;
\left(\frac{\mathrm{Im}\,5\tau}{\mathrm{Im}\,\tau}\right)^{\!6/4}
\left(\frac{N(\tau)}{N(5\tau)}\right)^{\!6}
\;=\;
5^{3/2}\,\Bigl(\tfrac{N(\tau)}{N(5\tau)}\Bigr)^{6}.
$$

The per-factor anomaly weights $(\mathrm{Im}\,\tau)^{1/4}$ cancel in the ratio **up to the
exact constant** $5^{6/4} = 5^{3/2} = 5\sqrt5$ (sympy-exact; numerically $< 10^{-71}$ at
$\tau_0$ and a generic point). This is *why* $t_5$ is a weight-0 holomorphic modular
function — anomaly-free — and hence *can* take the exact rational distinguished value
$t_5(\tau_0) = -10$ on the Bring class.

**Relation to the Fricke $125 = 5^3$, made exact.** Under $W_5:\tau\mapsto -1/(5\tau)$,
$S$-invariance of $N$ gives $N(5\,W_5\tau) = N(-1/\tau) = N(\tau)$ and
$N(W_5\tau) = N(5\tau)$, so the norm-ratio $R = (N(\tau)/N(5\tau))^6$ obeys
$R(W_5\tau) = 1/R(\tau)$ and

$$
\bigl\lvert t_5(\tau)\,t_5(W_5\tau)\bigr\rvert \;=\; \bigl(5^{3/2}\bigr)^2 \;=\; 5^3 \;=\; 125 :
$$

the Fricke constant $125$ is **exactly the square of the anomaly-cancellation constant**
$5^{3/2}$ — its magnitude is pure $\mathrm{Im}$-factor bookkeeping; the holomorphic content
of the Fricke relation is the residual phase. On the $W_5$-fixed circle $R = 1/R$ forces
$R = 1$, giving $\lvert t_5\rvert \equiv 5^{3/2} = 5\sqrt5$ — the 2026-07-24
Fricke-circle invariant re-derived from the anomaly bookkeeping alone (asserted:
$t_5(i/\sqrt5) = 5\sqrt5$ to $< 10^{-40}$).

## 3. The classification table

Classes: **(a)** weight-0 holomorphic modular function / holomorphic-sector data —
anomaly-free, exact rational or algebraic distinguished values are the expected behavior;
**(b)** Quillen norm / metric quantity — anomaly-carrying, point values are frame data
(at best period-type $\Gamma$-values at CM points), no rational/algebraic distinguished
constant expected; **(c)** mixed / unresolved.

| object | class | grounds |
|---|---|---|
| $t_5(\tau) = (\eta/\eta(5\cdot))^6$ | **(a)** | weight $3/3$ quotient $\Rightarrow$ weight 0, holomorphic ($\eta \ne 0$); anomaly factors cancel up to $5^{3/2}$ (§2); exact value $-10$ on the Bring class ([gate wiring](2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md), [`BringHauptmodulGate.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BringHauptmodulGate.lean)) |
| $j(\tau)$ | **(a)** | hauptmodul of $X(1)$; exact algebraic values at distinguished points |
| Fricke pair $(t_5(\tau_0),\,5^3/t_5(\tau_0)) = (-10, -25/2)$ | **(a)** | identity of weight-0 functions; $125 = (5^{3/2})^2$ per §2 ([Fricke/cusp/spin audit](2026-07-24-tau-dictionary-fricke-cusp-spin.md)) |
| $a_p$ integers (X₀(50)/50a Hecke data) | **(a)** | Fourier coefficients of a weight-2 *holomorphic* newform: frame-independent integers ([50a Hecke gate](2026-07-25-x050-50a-hecke-gate.md)) |
| $\det{}'\Delta(E_\tau) = (\mathrm{Im}\,\tau)^2\lvert\eta\rvert^4$ | **(b)** | Quillen curvature $-1/(2(\mathrm{Im}\,\tau)^2) \ne 0$ (§1): not $\lvert f\rvert^2$; AGMV Sect. 4 |
| polarized Bring $\det{}'\Delta$ measure $\sqrt{\mathrm{Vol}}/\sqrt{\det{}'\Delta} = 1.38758$ | **(b)** | same object class, genus 4, period $\tau_0 M$ ([polarized det′ audit](2026-07-19-bring-genus4-polarized-epstein-detprime.md)) |
| product-period (unpolarized) $\approx 1.4724\times 10^{12}$ (#3934 lineage) | **(b)** | same norm in the product frame; the ~12-order separation is θ-factor (norm-sector) data |
| per-factor measures $m(\tau_0), m(5\tau_0)$, $m(\tau) = 1/(\sqrt{\mathrm{Im}\,\tau}\,\lvert\eta\rvert^2)$ | **(b)** | genus-1 Quillen norms (reproduced in-probe) |
| $8.226 = m(5\tau_0)^3\,m(\tau_0)$ (retracted) | **(b)** | product of Quillen norms — reproduced in-probe to $8.2263$ / naive product $2.9220$, matching the [2026-07-18 retraction audit](2026-07-18-bring-polarized-epstein-determinant.md); doubly a non-candidate (wrong object *and* frame data) |
| α_EM $1/(8\pi)$ loop weight (target) | **(c)** | unresolved; proposed below (§5) as a *curvature coefficient* — the derivable class — not a norm point-value |

## 4. Retroactive explanation (organizing principle, stated carefully)

**What is claimed.** A *classification* consistent with, and organizing, results already
established scope-(a). **What is not claimed:** no new no-go. The classification does not
by itself prove that no normalization of $1.38758$ can match a constant — the existing
negatives ([no target matched](2026-07-19-bring-genus4-polarized-epstein-detprime.md),
[endpoint blindness](2026-07-19-bring-polarized-q-dictionary-endpoint-blindness.md),
the [8.226 retraction](2026-07-18-bring-polarized-epstein-determinant.md)) stand on their
own evidence and keep their own scope-(a) labels.

**(i) Endpoint/polarization blindness.** The 2026-07-19 result proved that endpoint-anchored
period-side q-dictionaries see only the θ-asymptotics — $\det G$ (covolume) data, which is
polarization-independent — while the entire ~12-order polarized-vs-product separation lives
in the interior θ-factor. The classification identifies *what kind of data* that is: the
interior θ-factor is precisely the anomaly-carrying norm sector (AGMV Sect. 5,
Eqs. (5.1)–(5.4): the determinant over the Jacobian family is
$e^{-\pi(u-\bar u)(\Omega-\bar\Omega)^{-1}(u-\bar u)}\lvert g(u)\rvert^2$ — a holomorphic
theta $g$ times a non-holomorphic Gaussian norm factor; the interior heat-kernel regime
mixes both, the endpoints retain only cohomological data). A dictionary constrained to
carry anomaly-free-sector content is structurally blind to norm-sector separations — which
is what the endpoint-blindness probe measured.

**(ii) No distinguished constant from any $\det{}'\Delta$ magnitude probe.** Every probe
in the #3934 lineage returned an unmatched O(1)-or-blown-up number ($1.38758$ vs
$8\pi$/$b_1$/$8.226$: ratios $0.055/0.17/0.17$; the $1.4724\times10^{12}$ product-frame
blow-up; the retracted per-factor products). Under the classification this is the expected
behavior of class (b): AGMV note explicitly that the Quillen determinant "*also depends on
the choice of $D_0$*" (below their Eq. (4.2)) — point values of anomaly-carrying norms are
frame data. The frame dependence is not hypothetical in our corpus: the *same* Bring
Jacobian data evaluated in two period frames (polarized $\tau_0 M$ vs product
$\mathrm{diag}(5,5,5,1)\tau_0$) differs by twelve orders of magnitude. By contrast, the
objects that did land exactly ($t_5 = -10$, $-25/2$, $a_p \in \mathbb{Z}$) are all
class (a). The sessions' empirical split *is* the anomaly dichotomy.

**What the anomaly sector's derivable objects are.** AGMV Sect. 4 shows the anomaly
sector does carry frame-independent content — not point values but **curvature
coefficients**: the counterterm $q = \tfrac{1}{2\pi}\int_\Sigma d^2z\, A_z A_{\bar z}$
(their Eq. (4.4), Quillen's counterterm Eq. (4.6)), the gravitational
$\tfrac{1}{192\pi}$ coefficient (Eqs. (4.26)–(4.27), their conventions of the conformal
anomaly), the Weil–Petersson form $\bar\delta\delta W \propto \langle\delta g,\delta
g\rangle_{\mathrm{WP}}$ (Eq. (4.31)), and the spin-$n$ obstruction weight
$\sum_i [3(2n_i+1)^2 - 1]$ (following Eq. (4.32)) — all rational multiples of $1/\pi$
computed by index densities, with Belavin–Knizhnik's observation that when the total
anomaly cancels the integrand becomes $\lvert\text{holomorphic}\rvert^2$ *even though the
individual determinants are not*. This motivates §5.

## 5. R2 framing (owner-gated, propose-only): $1/(8\pi)$ as a Quillen-curvature coefficient

**Proposal (not computed here).** The α_EM per-loop weight $1/(8\pi)$ has resisted every
attempt to realize it as a *point value* (a norm magnitude at the Bring modulus). The
classification suggests the opposite assignment: $1/(8\pi)$ has exactly the *shape* of a
**Quillen-curvature coefficient** — the AGMV/Polyakov normalization family
$\tfrac{1}{2\pi}$ (Eq. (4.4)), $\tfrac{c}{48\pi}$-type, $\tfrac{1}{192\pi}$
(Eq. (4.27)) — i.e. a rational multiple of $1/\pi$ arising as the curvature integral of a
determinant line bundle over a family, computed by an index density. Under this framing
the derivation target for the magnitude leg would be: *identify the determinant line
bundle over the Bring family (the τ-functor's target) whose Quillen curvature integral
carries the coefficient $\tfrac18\cdot\tfrac1\pi$* — an object in the **derivable** class
(index theory computes it), unlike the norm point-values every probe has been evaluating.

**Honest tautology-risk caveat.** Coefficients in the $c/(48\pi)$ family are *universal*
in the field content (central charge, spin weights $\sum_i[3(2n_i+1)^2-1]$, AGMV following
Eq. (4.32)): landing on $1/(8\pi)$ by choosing field content is not a derivation of α_EM's
wall but a re-parameterization of the conformal anomaly. A genuine R2 derivation must
(i) obtain the specific bundle and family from the framework's own categorical data (no
field-content tuning), (ii) show why *that* index density integrates to the rational
$\tfrac18$, and (iii) pass the production-vs-exploratory discipline before anything is
wired. **No R2 value is computed here; nothing is wired; this section is a proposal for
the owner-gated R2 attack only.**

## 6. Scope discipline (anti-laundering)

- **Scope-(a) throughout; no new no-go.** The classification is a structural observation
  with a cited theorem (AGMV Sect. 4 / Quillen); the only exact new results are §1 (the
  curvature, symbolic + numeric) and §2 (the cancellation identity) — both identities, not
  exclusions. Existing negatives keep their own labels.
- **NO FIT.** Nothing was adjusted toward any target; the two corpus prints reproduced
  ($2.922$, $8.226$) are consistency checks against committed audit values, not fits.
- **Nothing wired.** Audit-only witness (`set_audit_only`); no production script touched;
  the τ-functor wall and the α_EM magnitude leg remain open.
- **Render-QA:** the preflight grep battery was run by hand (balanced `$`/`$$`/braces, no
  `\operatorname`, no list-hijack lines inside display math, no inline align-family
  environments); the pipeline render was not run in this sandbox — stated explicitly per
  the render-QA gate: this change was not machine-validated.

## 7. Cross-references

- AGMV upload: `library/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invariance-and-strings.pdf` (Commun. Math. Phys. **106**, 1–40 (1986))
- The genus-1 exact anchor + retraction: [`2026-07-18-bring-polarized-epstein-determinant.md`](2026-07-18-bring-polarized-epstein-determinant.md)
- Polarized genus-4 value 1.38758: [`2026-07-19-bring-genus4-polarized-epstein-detprime.md`](2026-07-19-bring-genus4-polarized-epstein-detprime.md)
- Endpoint blindness: [`2026-07-19-bring-polarized-q-dictionary-endpoint-blindness.md`](2026-07-19-bring-polarized-q-dictionary-endpoint-blindness.md)
- The $t_5 = -10$ gate: [`2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md`](2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md), [`BringHauptmodulGate.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BringHauptmodulGate.lean)
- Fricke-circle invariant $5\sqrt5$ (here re-derived from anomaly bookkeeping): [`2026-07-24-tau-dictionary-fricke-cusp-spin.md`](2026-07-24-tau-dictionary-fricke-cusp-spin.md)
- The $a_p$ integer gate: [`2026-07-25-x050-50a-hecke-gate.md`](2026-07-25-x050-50a-hecke-gate.md)
