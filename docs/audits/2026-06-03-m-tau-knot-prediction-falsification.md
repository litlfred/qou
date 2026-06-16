# Falsification of the simple cohomological extension for $m_\tau$

> **Provenance.** Primary content of the former content block
> [`rem:m-tau-knot-prediction`](../../content/quantum-observable-universe/observations/m-tau-knot-prediction.md),
> moved here in PR #1758 per the
> `canonical-no-negative-result-in-paper` discipline criterion. The
> chapter block is retained as a forward-reference; the substantive
> empirical search + falsification analysis lives here.

The CAL-2 cohomological critique
([`rem:epistemic-status-of-calibrations`](../../content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md))
identifies a structural pattern in the paper's muon-mass identity:

$$
\frac{m_\mu}{m_e} \;=\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
\quad\text{at } q = q_0
\qquad
(\mathrm{Vol}(4_1) = 2\Lambda(\pi/3) \approx 2.02988)
$$

where $\mathrm{Vol}(4_1)$ is a Bloch–Wigner motivic period and
$\hbar_q = (q-1)/q$. The paper claims at
[`rem:calibration-inputs`](../../content/quantum-observable-universe/observations/calibration-inputs.md)
that $m_\tau/m_e$ is *"predicted from $q_0$ alone"* but never surfaces
the formula.

This audit **tests and falsifies** the simplest extension of the
muon identity: search for a hyperbolic knot/link $K_\tau$ and integer
exponent $k_\tau \in \{2, 3, 4, 5\}$ such that

$$
\frac{m_\tau}{m_e} \;\approx\; \frac{\mathrm{Vol}(K_\tau)}{\hbar_q^{k_\tau}}
\quad\text{at } q = q_0,
\qquad
\frac{m_\tau}{m_e} \;=\; 3477.23 \;\;(\text{PDG 2024}).
$$

Also tested: pair-products $\mathrm{Vol}(K_1)\,\mathrm{Vol}(K_2)/\hbar_q^k$.

## Methodology

Compute script:
[`computations/m_tau_knot_prediction.py`](../../computations/m_tau_knot_prediction.py).
Operates at 50 dps via mpmath; uses the canonical
$q_0 = 1.10997859555\ldots$ pin
([`q_parameter.Q_50_DIGIT_STR`](../../computations/substrate/q_parameter.py)).

Candidate table: 25 hyperbolic knots and links from the SnapPy census
through 10 crossings + Borromean / Whitehead / $L_{n}$ family. All
volumes verified to $\ge 8$ dps.

Sanity check (muon CAL-2 identity): the script reproduces
$\mathrm{Vol}(4_1)/\hbar_q^2 = m_\mu/m_e$ to relative error
$\sim 10^{-20}$ at 50 dps — confirming the substrate and arithmetic
are correct.

Search:
- 108 candidate (knot, $k$) pairs evaluated for the single-knot pattern.
- $\binom{25}{2} \times 6$ candidate (pair, $k$) tuples evaluated for
  the product pattern, gated at $< 0.1\%$ relative error.

Thresholds: tight $= 100$ ppm, mid $= 0.1\%$, loose $= 1\%$.

## Result — refuted

| Pattern | Best match | Relative error |
|---|---|---|
| Single $\mathrm{Vol}(K)/\hbar_q^3$ | $\mathrm{Vol}(8_1)/\hbar_q^3 = 3523.59$ vs $3477.23$ | $+1.33\%$ |
| Single $\mathrm{Vol}(K)/\hbar_q^3$ (runner-up) | $\mathrm{Vol}(7_2)/\hbar_q^3 = 3425.20$ vs $3477.23$ | $-1.50\%$ |
| Single $\mathrm{Vol}(K)/\hbar_q^3$ (third) | $\mathrm{Vol}(6_1)/\hbar_q^3 = 3252.75$ vs $3477.23$ | $-6.46\%$ |
| Product $\mathrm{Vol}(K_1)\mathrm{Vol}(K_2)/\hbar_q^k$ | *(no match under $0.1\%$ gate)* | $> 0.1\%$ |

**Conclusion (refuted, with evidence):** the simplest cohomological
extension of the muon-mass identity —
$m_\tau = m_e \cdot \mathrm{Vol}(K_\tau)/\hbar_q^{k_\tau}$ for a single
hyperbolic knot $K_\tau$ and small integer $k_\tau$ — **does not**
reproduce CODATA $m_\tau/m_e$ to better than $1.33\%$. The best
candidate misses by $\sim 13\,000$ times the experimental precision
($\sigma_{\text{exp}}(m_\tau/m_e) \approx 5 \times 10^{-5}$).

Note the suggestive structural pattern: the closest candidates all
use $k_\tau = 3$ (one power higher than the muon's $k_\mu = 2$),
consistent with a *"generation-step in $\hbar_q$"* hypothesis. But no
specific $K_\tau$ delivers a clean match, and the 1.33 % gap is too
large to be a small-correction residual.

## What this rules out

The naive "next hyperbolic knot at minimal $H_n$" reading of the
cohomological lepton-generation hierarchy (as proposed in the
companion audit
[`-cal-2-cohomological-vs-calibration-critique.md`](-cal-2-cohomological-vs-calibration-critique.md)
§F5) is falsified for the bare $\mathrm{Vol}(K_\tau)/\hbar_q^{k_\tau}$
form. Specifically:

- $5_2$, $6_1$, $6_2$, $6_3$, $7_2$–$7_7$ tested at $k = 2..5$ — none match;
- $8_n$ family ($8_1$ best at $1.33\%$, $8_{18}$ amphicheiral) — none match;
- Multi-component hyperbolic links (Borromean, Whitehead, $L_{6}a_{1}$, $L_{8}a_{8}$) — none match;
- Two-knot products at $k \le 7$ — none under $0.1\%$.

## Extensions to test (not done in this audit)

The refutation rules out the *simplest* pattern; it does not rule out
cohomological derivability in general. Plausible extensions, queued
for future work:

1. **Volume + Chern–Simons pair.** Hyperbolic knot complements carry
   a complex-valued invariant $\mathrm{Vol}(K) + i\,\mathrm{CS}(K)$. The
   mass formula may need both parts:
   $m_\tau/m_e = |\mathrm{Vol}(K_\tau) + i\,\mathrm{CS}(K_\tau)|/\hbar_q^{k_\tau}$
   or similar.
2. **Polylog tower at $n > 2$.** The electron uses
   $\mathrm{Li}_2(q^{-2})/\hbar_q^2$ in natural units; the tau may
   require $\mathrm{Li}_3$, $\mathrm{Li}_4$, or a sum
   $\sum_n c_n \mathrm{Li}_n(q^{-2})$.
3. **Whitehead doubling / satellite operations.** $K_\tau$ may not be
   a prime knot but a satellite (Whitehead double, $(p,q)$-cable) of
   the figure-eight, with volume relations governed by Thurston's
   geometric decomposition.
4. **Multi-stratum sum.** Parallel to the $Q_\beta$ Khovanov–Rozansky
   strata work (audit
   [`-qbeta-n5-cohomological-breakdown.md`](-qbeta-n5-cohomological-breakdown.md)),
   $m_\tau$ may need a sum over cohomological strata rather than a
   single knot. Candidate: trace over Khovanov–Rozansky homology of a
   $\tau$-distinguished link projection.
5. **Tower correction.** Analogous to the framework's
   $\mathfrak{E}_0^{\text{full}} = \mathfrak{E}_0^{(N=0)}/(1-\hbar_q^2)$
   relation, $m_\tau/m_e$ may equal
   $\mathrm{Vol}(K_\tau)/\hbar_q^{k_\tau} \cdot (1 - c_2 \hbar_q^2 + c_4 \hbar_q^4 - \ldots)$
   with categorical coefficients.

Each extension is a separate research direction; none should be
proposed as a 4th calibration input or as a fit-based ansatz (per
CLAUDE.md "Δ_λ gate" anti-pattern guard).

## Status

**Refuted (specific evidence).** Surfaces a falsifiable claim, tests
it, and reports the falsification. Useful constraints on what
cohomological-generation hierarchies are *compatible* with the
$m_\mu \leftrightarrow 4_1$ pattern: any candidate must produce
$m_\tau/m_e$ exactly, which the simplest single-knot form does not.

This audit does **not** propose a new calibration input, a fit, or a
numerological substitution. It documents an empirical search and its
honest outcome.

## See also

- [`rem:calibration-inputs`](../../content/quantum-observable-universe/observations/calibration-inputs.md) — canonical 3-CAL remark
- [`rem:epistemic-status-of-calibrations`](../../content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md) — unified epistemic accounting
- [`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md) — $H^0$/$H^1$/$H^2$ mapping
- [`-cal-2-cohomological-vs-calibration-critique.md`](-cal-2-cohomological-vs-calibration-critique.md) §F5 — driver question
- Compute script + witness:
  [`m_tau_knot_prediction.py`](../../computations/m_tau_knot_prediction.py),
  [`m-tau-knot-prediction.witness.json`](../../computations/m-tau-knot-prediction.witness.json)
