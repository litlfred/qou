# E_unit higher-order counit terms — Magnus order 2 through NA-Stokes (the deuteron −9.2%)

**Date:** 2026-07-24 · **Branch:** `claude/binding-mass-derivation-gaps-0f61i6` · **Bean:** `qou-yofd` (W2
of the merged #4142 workplan) · **Axis:** Δ_λ binding magnitude — the `E_unit`/μ₀ −9.2% closure ·
**Route:** analytic Magnus order-2 (Broda `library/arxiv-math-ph-0012035v3/0012035v3.pdf` + Blanes–Casas–Oteo–Ros
`library/phys-rep09/phys-rep09.pdf`), deliberately **complementary** to PR #4127's octahedral 4-dilogarithm
resummation (route B there; this is that PR's own route A, bean `qou-dp32`, run in parallel per the
parallel-exploration policy — intent posted on #4127). **Tier:** structural derivation + forward
numerics (scope-(a) where numeric, proved identities where symbolic; **no fit, nothing wired, no AME
inversion**).

## 0. Leading order recap (what the −9.2% is measured against)

Merged #4117 ([`2026-07-19-eunit-source-is-the-counit.md`](2026-07-19-eunit-source-is-the-counit.md)):
`E_unit`'s source is the **counit** — the per-crossing weight $h = q - q^{-1}$ (skein $L_+ - L_-$ =
antisymmetric Hecke-eigenvalue difference), with the dimensional bridge
$\mu_0 = m_e/(3h/2) \approx 1.6295$ MeV (0 free parameters). The observable frame is the canonical
rotational tier ([`binding_qhamiltonian_rotational_scale.py`](../../computations/binding_qhamiltonian_rotational_scale.py)
and its witness): $E_{\mathrm{rot}} = \mu_0\,\hbar_q\,[j]_q[j{+}1]_q$ with $j = n/2$, $n = 3A$
strands, compared **forward** against AME (`codata_constants` validation values): deuteron
$2.0196$ vs $2.2245662$ MeV = **−9.21%**; T −48.6%, ³He −43.5%, ⁴He −72.2%. The −9.2% is the size
of the missing higher-order (co)unit / NA-Stokes terms; #4117 fixed the expansion's organizing
identity $(q-q^{-1}) = (v-v^{-1})\,[2]_v$, $v = \sqrt q$.

Pin: numbers below use the computations-layer canonical $q_0$ (muon-pinned string
`1.10997859555733471…`) and are recomputed at the environment/package pin (proton, ~11.5 ppb away);
the difference is immaterial at this audit's $10^{-4}$ relative scale (witness records both — the
measured coefficient shifts by $<10^{-6}$).

## 1. What the order-2 term IS structurally

The Magnus expansion (phys-rep09, Theorem 1 eq. (32)) of the path-ordered holonomy
$U = \mathrm{P}\exp\int A$ is $U = \exp\Omega$ with

$$
\Omega \;=\; \int_0^t A\,dt_1 \;+\; \tfrac12 \int_0^t\!\!\int_0^{t_1} [A(t_1), A(t_2)]\,dt_2\,dt_1 \;+\; \cdots,
$$

i.e. $\Omega_2$ is the ordered double-integral **commutator** $\tfrac12\oint\oint[A,A]$, and every
$\Omega_k$, $k \ge 2$, is a Lie element (sum of nested commutators). In the NA-Stokes form (Broda,
eq. after Fig. 2) the same holonomy is the surface-ordered exponential of the path-dependent
curvature $\mathcal F(x) = U^{-1}(x,O)\,F(x)\,U(x,O)$ — the corpus's $F_q = [\delta q_1, \delta q_2]$
([`germ-commutator-q-curvature`](../../content/quantum-observable-universe/quantum-observable-universes/germ-commutator-q-curvature.md)).

In the QOU Step-3 setting the connection along a braid word is piecewise the generator logarithm:
letters $A_k = \log\sigma_{i_k}$ (letter of $\sigma^{-1}$ is $-\log\sigma$, path reversal). Under
the bar involution ($q \mapsto q^{-1}$, $\sigma_i \mapsto \sigma_i^{-1}$) each letter is
**bar-odd**, so the Magnus grading carries parity $(-1)^k$ with scalar shape $h^k$:

| order | object | scalar q-shape | v-level shape | bar-parity |
|---|---|---|---|---|
| 1 | $\Omega_1 = \sum_k A_k$ (the counit/skein tier, $\mu_0$) | $h$ | $(v-v^{-1})\,[2]_v$ | **odd** |
| 2 | $\Omega_2 = \tfrac12\sum_{k>l}[A_k,A_l]$ | $h^2$ | $x\,[2]_v^2$, $x = (v-v^{-1})^2$ | **even** |
| 3 | $\Omega_3$ (nested commutators) | $h^3$ | $x\,(v-v^{-1})\,[2]_v^3$ | odd |

all verified symbolically in the probe (S1–S4, S7). The v-level shape of the order-2 term is **one
unit of the 5g-ladder deformation parameter $x$ dressed by $[2]_v^2$** — exactly the
$q \leftrightarrow \sqrt{q}$ passage #4117 predicted the correction must organize along.

**Bar-parity verdict (task question): the order-2 term is bar-EVEN.** This is the *favourable*
parity: binding is a mass-side (cosh/bar-even) observable per the corpus split, so an order-2
correction is not parity-blocked. The parity alternation $(-1)^k$ means only **even** Magnus orders
can correct the binding form; odd orders are the radiated ($Q_\beta$-like) channel.

## 2. The proved vanishings — order 2 is NOT where the −9.2% lives

Probe ([`eunit_magnus_order2_probe.py`](../../computations/probes/eunit_magnus_order2_probe.py),
witness `eunit-magnus-order2.witness.json`, 20/20 assertions, sympy + mpmath 50 dps, 2-dim Hecke
rep of $B_3$ = rescaled reduced Burau):

1. **Deuteron channel: $\Omega_2 \equiv 0$ exactly.** The 3-crossing pn/trefoil channel word is
   $\sigma_1^3$ — a *single* generator, so every commutator is $[a,a] = 0$: the whole tower
   $\Omega_k = 0$ for $k \ge 2$ and $\exp\Omega_1$ is **exact**. This is a proved identity (the
   invariant is $[X,X]=0$), not a failed numeric: *the inter-crossing Magnus correction to the
   deuteron counit holonomy vanishes at every order.* The −9.2% is **not** an inter-crossing
   commutator effect.
2. **Counit character and Markov trace kill $\Omega_{k\ge2}$ linearly, for every braid.** The
   1-dim counit character is multiplicative (kills commutators); any trace functional kills Lie
   elements ($\mathrm{tr}\,[X,Y] = 0$, S7c). Verified on the adjacent-generator word
   $(\sigma_1\sigma_2^{-1})^3$: $\Omega_2 \ne 0$ at operator level (norm $\approx 8.2$) yet
   $\mathrm{tr}\,\Omega_2 = 0$ to 50 dps.
3. **The order-3 trace term also vanishes identically for $B_3$ words** (found by the probe's own
   numerics, then proved): with only two distinct letters, every constituent of
   $\mathrm{tr}(\Omega_1\Omega_2)$ is $\mathrm{tr}(X[X,Y])$ or $\mathrm{tr}(Y[X,Y])$ — zero by
   cyclicity (S8). Likewise $\mathrm{tr}(\Omega_1^2\Omega_2) = 0$ (only the antisymmetric part of a
   degree-2 word pairs with $[a,b]$ under trace). The **first surviving inter-crossing trace-level
   correction is order 4** ($\mathrm{tr}\,\Omega_2^2 \ne 0$, $\mathrm{tr}(\Omega_1\Omega_3)$) —
   automatically bar-even, magnitude $\sim h^4 \approx 0.19\%$, far below every residual in the
   table.

**Refutation scope (per the (a)/(b) discipline):** for the *braid-word connection* the exclusion is
class (b) — the cited invariants are $[X,X] = 0$ (deuteron word) and trace cyclicity (all $B_3$
words), so the inter-crossing Magnus tower cannot carry the −9.2% at orders 2–3, and contributes at
most $\sim 0.2\%$ at order 4. For the *general* "second-order NA-Stokes" idea the verdict is
scope-(a): two second-order candidates **survive** this pruning because they are not inter-crossing
commutators — (i) the **per-crossing** octahedral $e_2$ cross-terms (PR #4127's route B: the other
3 tetrahedra of each crossing's octahedron), and (ii) the **surface-curvature pairing**
$\tfrac12\,\mathcal P\!\iint\!\iint [\mathcal F, \mathcal F]$ of the NA-Stokes surface ordering,
quadratic in the germ commutator $F_q = [\delta q_1, \delta q_2]$, which lives *transverse* to the
strand ordering (the two-observer parallelogram direction) and so survives even on the
single-generator deuteron channel. Computing (ii) needs a canonical discretization of the
Yekutieli surface 2-form on the pn channel's Seifert surface — **data the corpus currently lacks**
(named wall; this is the "surface-ordering needs data" outcome anticipated in the task).

## 3. Forward decomposition of the −9.2% (no fit)

The rotational form rewrites exactly (S5, S6 — the counit weight $h$ *cancels* between
$\mu_0 \propto 1/h$ and $\hbar_q = h/(1+q)$):

$$
E_{\mathrm{rot}} \;=\; \mu_0\,\hbar_q\,[j]_q[j{+}1]_q \;=\; \frac{m_e\,[j]_q[j{+}1]_q}{3}\cdot\frac{2}{1+q}
\;=\; E^{+}\,(1 - t), \qquad
E^{+} = \frac{m_e\,[j]_q[j{+}1]_q}{3}, \quad t = \frac{q-1}{q+1} = \frac{v-v^{-1}}{[2]_v}.
$$

$E^{+}$ is manifestly bar-even (balanced q-integers times $m_e$); $t$ is bar-odd. So the
first-order form is **parity-impure**: its bar-odd impurity is exactly $-t \approx -5.212\%$ — a
sinh-channel (radiated-parity) factor sitting inside a mass-side observable. Decomposing the
deuteron residual forward (all identities verified to 50 dps; nothing tuned):

| quantity | value | status |
|---|---|---|
| $E_{\mathrm{rot}}$ (canonical first-order form) | 2.01958 MeV (−9.215%) | derived (#4117 frame) |
| bar-odd impurity $t = (v-v^{-1})/[2]_v$ | 5.2123% | exact decomposition $E_{\mathrm{rot}} = E^{+}(1-t)$ |
| bar-even projection $E^{+} = m_e[3]_q[4]_q/3$ | 2.13064 MeV (−4.222%) | structural assumption: mass-side bar-even discipline applies to this tier |
| remaining bar-even gap on $E^{+}$ | +4.4084% | measured forward |
| natural order-2 unit $h^2 = x[2]_v^2$ | 4.3707% | derived shape (§1) |
| measured coefficient $g_2 = \mathrm{gap}/h^2$ | **1.0087** | **NEAR-MATCH — underived** |
| $E^{+}(1+h^2)$ | 2.22376 MeV (**−0.036%**) | near-match tier, NOT wired |

Forward across the tier (same recipe, no per-isotope freedom):

| isotope | $E_{\mathrm{rot}}$ err | $E^{+}$ err | $E^{+}(1+h^2)$ err | AME (MeV) |
|---|---|---|---|---|
| D | −9.21% | −4.22% | **−0.036%** | 2.2245662 |
| T | −48.6% | −45.8% | −43.4% | 8.4817962 |
| ³He | −43.5% | −40.4% | −37.8% | 7.7180413 |
| ⁴He | −72.2% | −70.7% | −69.4% | 28.2956624 |

**A≥3 is untouched** — the 44–72% deficit is the per-rep structure (highest-weight $j = n/2$
collapse), not an order-2 effect; an $h^2$-size term cannot and does not reach it. This audit does
not claim otherwise.

**Anti-fit accounting.** No coefficient was scanned: the only freedoms exercised are (i) the parity
projection — a single structural assumption (binding = bar-even projection), the same prescription
the corpus already uses for $b_4$
([`b4_connected_bar_parity_probe.py`](../../computations/probes/b4_connected_bar_parity_probe.py):
retained binding = bar-even part, bar-odd part radiated) — and (ii) comparing the leftover to the
*pre-derived* order-2 unit $h^2$ at unit coefficient. The measured $g_2 = 1.0087$ is reported as a
**near-match** (cf. the $c_3 = -2$ flip-flop lesson: near-match ≠ derived); deriving $g_2$ — from
the octahedral $e_2$ term or the surface-curvature pairing — is the **named open object**. If it is
not exactly 1, the −0.036% is partly accidental; nothing here is wired to production.

## 4. Convergence/divergence vs PR #4127 (octahedral route B)

Route B's hypothesis: $\mu_0$ = 1 of the 4 ideal tetrahedra of the crossing octahedron
(2509.02354), the −9% = the other 3 tetrahedra. This audit's results interact with it in three
ways:

1. **Supportive:** the inter-crossing alternative is now pruned (proved, §2), so *within the
   NA-Stokes organization the missing second-order structure must be per-crossing* — exactly where
   route B localizes it.
2. **Constraining:** if the 4 tetrahedra contributed comparably at first order, the completion
   would be $\sim +300\%$ — wildly inconsistent with the forward requirement (+10.15% on
   $E_{\mathrm{rot}}$, or −5.2% odd + 4.4% even in the parity decomposition). Consistency with the
   forward numbers requires the 3 missing tetrahedra to enter with strongly suppressed/cancelling
   first-order parts, leaving a bar-even $e_2$-size remainder $\approx h^2$ with coefficient
   $\approx 1$.
3. **Discriminating test (for route B to run):** compute the deuteron crossing's 4-$\Phi_q$
   holonomy and split it by bar-parity. Routes **converge** if the octahedral first-order (linear)
   completion reproduces the bar-odd impurity $-t \approx -5.21\%$ and the $e_2$ cross-terms give
   the bar-even $\approx 1.0\,h^2$; they **diverge** if the octahedral completion is first-order
   dominated with a large bar-even linear part. Either outcome is decisive for one of the two
   machineries.

## 5. Verdict (honest)

- **Does not close the −9.2% — and proves why this route cannot:** the analytic Magnus
  inter-crossing tower contributes exactly 0 at order 2 (deuteron word), 0 at order 3 at trace
  level (two-letter cyclicity), and $\lesssim 0.2\%$ ($h^4$) at order 4 — class-(b) for the
  braid-word connection, invariants cited.
- **Bar-parity verdict:** order 2 is bar-even (favourable, not parity-blocked); odd orders are
  parity-blocked *and* trace-vanishing; only even orders can touch binding.
- **What the forward numbers say:** the −9.2% decomposes exactly into a bar-odd parity impurity
  $-t = -5.21\%$ (the $\hbar_q$ factor's odd part) plus a bar-even gap $+4.41\% \approx 1.009\,h^2$
  on the parity-projected form $E^{+} = m_e[j]_q[j{+}1]_q/3$. Near-match tier; the coefficient of
  $h^2$ is the open object; A≥3 untouched.
- **Wall named:** the surviving non-octahedral second-order candidate — the NA-Stokes
  surface-curvature pairing quadratic in $F_q = [\delta q_1, \delta q_2]$ — needs a canonical
  surface discretization the corpus lacks.

## Files

- Probe: [`computations/probes/eunit_magnus_order2_probe.py`](../../computations/probes/eunit_magnus_order2_probe.py)
- Witness: [`computations/probes/eunit-magnus-order2.witness.json`](../../computations/probes/eunit-magnus-order2.witness.json) (audit-only, 20/20 assertions)
- This report: `docs/audits/2026-07-24-eunit-magnus-order2.md`

Refs: `library/arxiv-math-ph-0012035v3/0012035v3.pdf` (Broda, NA-Stokes review, eqs. (5)–(10) + the surface-ordered
theorem); `library/phys-rep09/phys-rep09.pdf` (Blanes–Casas–Oteo–Ros, Phys. Rep. 470 (2009) 151, Thm 1
eq. (32)); [`2026-07-19-eunit-source-is-the-counit.md`](2026-07-19-eunit-source-is-the-counit.md);
PR #4127 (`2026-07-19-octahedral-four-dilogarithm-missing-tetrahedra.md`, `FourDilogFirstOrder.lean`);
[`binding_qhamiltonian_rotational_scale.py`](../../computations/binding_qhamiltonian_rotational_scale.py);
[`germ-commutator-q-curvature.md`](../../content/quantum-observable-universe/quantum-observable-universes/germ-commutator-q-curvature.md).

> **Notation note (added 2026-07-24, owner query).** The gap coefficient here is
> written $g_2$ (drafted as "$c_2$" — collides with the Q_β ladder; then "$\gamma_2^E$" — γ is the photon; settled as $g_2$, owner pick 2026-07-24) precisely to avoid collision
> with the **Q_β precision-ladder** $c_k$ family — a different object entirely: the
> ladder's $c_2 = -1$ is PROVED Taylor-exact and is unaffected by anything in this
> audit. $g_2$ is the measured ratio (bar-even E_unit gap)/$h^2$ = 1.0087,
> NEAR-MATCH tier, underived.

> **Follow-up (2026-07-25):** three $g_2$ derivation mechanisms tested exactly — cosh/crossing-count
> (predicts $9/8$, not 1.0087), BCH/Bernoulli (predicts 0), next-order-unit parity sweep (no bar-even
> unit within 10% of $g_2-1$) — see
> [`2026-07-25-eunit-g2-derivation-attempt.md`](2026-07-25-eunit-g2-derivation-attempt.md). $g_2$
> remains NEAR-MATCH, underived.
