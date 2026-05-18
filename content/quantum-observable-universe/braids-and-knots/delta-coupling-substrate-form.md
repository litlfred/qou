**Conjecture (substrate-derivation of the magic-shell stabilization energy).**

*Let $\Delta_{\mathrm{coupling}}(Z, N)$ be the magic-shell
stabilization energy of [`conj:magic-shell-stabilization`](#conj:magic-shell-stabilization)
— the over-binding of a magic-shell nucleus beyond the categorical
six-term mass formula. Then at magic-shell anchors with $A = Z + N \geq 2$,*

$$
\boxed{\quad
\begin{aligned}
  \Delta_{\mathrm{coupling}}(Z, N)
  \;=\;
  & (A - 2) \cdot E_0 \cdot \log\!\frac{1}{h(q_0)} && \text{(leading)} \\
  & + 2\,(Z - 1)_+\,(N - 1)_+ \cdot z^2 \cdot E_0 \cdot h(q_0)^2 && \text{(pp-nn correlation)}
\end{aligned}
\quad}
$$

*where $E_0 = m_e / (q_0 (q_0 - 1))$ is the Hecke energy unit
([`rem:beta-decay-energy-scale`](#rem:beta-decay-energy-scale)),
$z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter, $h = q - q^{-1}$
is the Hecke skein deformation, $(x)_+ := \max(x, 0)$, and the
log-decomposition of the leading-form factor is
[`prop:hecke-log-decomposition`](#prop:hecke-log-decomposition).*

*The correlation term vanishes at single-magic anchors
(where either $Z = 1$ or $N = 1$) and contributes only at
doubly-magic configurations $(Z, N)$ with both $Z \geq 2$ and
$N \geq 2$, matching the empirical observation that single-magic
anchors lie at the leading-form prediction while doubly-magic
exhibit additional over-binding.*

## Status

**Conjecture, single-anchor verified at (2,2) ONLY; single-magic
anchors REFUTE the symmetric (A-2) form.** Cross-anchor test results
from [`probe_delta_coupling_cross_anchor.py`](folio-assistant/computations/probe_delta_coupling_cross_anchor.py)
using Δ_cat data on main:

| Anchor | Predicted (refined) | Extracted | Gap | Status |
|---|---:|---:|---:|---|
| $(2, 2)$ doubly-magic | 13.1945 | 13.1969 | $-0.018\%$ | within 1‰ |
| $(2, 1)$ single-magic | 6.5516 | 6.0252 | $+8.74\%$ | REFUTED |
| $(1, 2)$ single-magic | 6.5516 | 6.8211 | $-3.95\%$ | REFUTED |

The doubly-magic (2,2) match (0.018%) is excellent. The single-magic
anchors deviate by 4-9% in **opposite directions** — the symmetric
$(A-2) \cdot E_0 \cdot \log(1/h)$ leading form predicts zero
asymmetry at $A=3$, but empirically the asymmetry is $+0.796$ MeV
between $(1, 2)$ T and $(2, 1)$ ${}^3$He.

**The (2,2) match was largely coincidence.** Forcing the 3-anchor
data to the system
$\Delta_{\mathrm{coupling}} = \text{leading} + \text{pp} \cdot (Z-1) + \text{nn} \cdot (N-1) + \text{corr} \cdot (Z-1)(N-1)$
gives:

- $\text{pp\_term} \approx -0.526$ MeV  (single-magic σ_pp channel)
- $\text{nn\_term} \approx +0.270$ MeV  (single-magic σ_nn channel; +0.8 MeV asymmetric vs pp)
- $\text{corr} \approx +0.351$ MeV  (doubly-magic σ_pp·σ_nn correlation; ~4× the original $2 z^2 E_0 h^2$ value)

These have natural substrate-asymmetric interpretations
(proton-vs-neutron Hecke operator weights, σ_pp vs σ_nn channel
multiplicities) but the **specific structural form is not yet
identified**. The conjecture remains open at the substrate-derivation
level until this richer 3-term decomposition is closed.

Verification probes (in order of finding):
[`probe_delta_coupling_leading_form.py`](folio-assistant/computations/probe_delta_coupling_leading_form.py)
(leading-form, 0.7% gap at (2,2)),
[`probe_delta_coupling_pp_nn_correlation.py`](folio-assistant/computations/probe_delta_coupling_pp_nn_correlation.py)
(refined-form, 0.04% at (2,2) — apparently confirmed before cross-anchor test),
[`probe_delta_coupling_cross_anchor.py`](folio-assistant/computations/probe_delta_coupling_cross_anchor.py)
(REFUTES refined-form at single-magic anchors via direct cross-anchor extraction).

Cross-anchor verification at $(2, 1)$ ${}^3$He$=$D$+$p and $(1, 2)$
T$=$D$+$n is pending PR #644's $\Delta_{\mathrm{cat}}$ data for
proton and neutron landing on main.

## Substrate-derivation chain

Each factor traces to a substrate primitive:

| Factor | Substrate primitive | Source |
|---|---|---|
| $(A - 2)$ | Excess-strand count of canonical atomic braid in $B_{3A}$ | [`prop:atom-canonical-crossings`](#prop:atom-canonical-crossings) |
| $E_0$ | Hecke energy unit $m_e/(q(q-1))$ | [`rem:beta-decay-energy-scale`](#rem:beta-decay-energy-scale) (CAL-1 + CAL-2 only) |
| $\log(1/(k_B T_q)) = \log(q/(q-1))$ | Shannon-Boltzmann free-energy log at Hecke-thermal scale | [`prop:boltzmann-constant`](#prop:boltzmann-constant) |
| $-\log(1 + q_0)$ | Skein-convention normalisation | [`prop:hecke-log-decomposition`](#prop:hecke-log-decomposition) |

The proposed reading: **magic-shell stabilization at finite $A$ is the
thermodynamic free-energy correction per excess nucleon pair at the
QOU Hecke-thermal scale, in the skein-convention normalisation.**

## Why a conjecture and not a proposition

Three pieces remain open before this can be promoted to a proposition:

1. **Cross-anchor verification.** The 0.71% gap at $(2, 2)$ may
   improve or degrade at $(2, 1)$ and $(1, 2)$ once PR #644's
   $\Delta_{\mathrm{cat}}$ data lands.
2. **Why $(A - 2)$ exactly.** The substrate-derivation takes
   $(A - 2)$ as the canonical-atomic-braid strand count beyond the
   seed pair, but a deeper derivation from the operator-selection LP
   active-set cardinality at magic shells is preferred.
3. **Sign and magnitude of the residual $+0.097$ MeV at $(2, 2)$**
   ($+0.71$%). For exact match the leading form would need a
   multiplicative correction $C \approx 1.01163$, i.e.
   $\Delta_\mathrm{coupling} = (A-2) \cdot E_0 \cdot \log(C/h(q_0))$
   with $\log C \approx 0.01156$. Tested closest candidates from
   elementary substrate primitives:

   | candidate $C$ | value | $\|\Delta\|$ vs needed |
   |---|---:|---:|
   | $1 + h^2/4$ | $1.01093$ | $7.0 \times 10^{-4}$ |
   | $1 + h^2/(2[2]_q)$ | $1.01087$ | $7.6 \times 10^{-4}$ |
   | $1 + \hbar_q^2$ | $1.00982$ | $1.8 \times 10^{-3}$ |
   | $\exp(\hbar_q^2/2)$ | $1.00492$ | $6.7 \times 10^{-3}$ |
   | $(1+h^2)^{1/2}$ | $1.02162$ | $1.0 \times 10^{-2}$ |
   | $(q + q^{-1})/2$ | $1.00545$ | $6.2 \times 10^{-3}$ |

   The closest candidate ($1 + h^2/4$) misses by 700 ppm — equivalent
   to an absolute residual of $\sim 0.006$ MeV, still well above the
   AME measurement precision floor ($\sim 1$ keV). No elementary
   substrate-primitive combination closes the gap exactly at this
   anchor. The q-Edgeworth $\kappa_3$ route is refuted (wrong sign;
   see [`probe_delta_coupling_q_edgeworth.py`](folio-assistant/computations/probe_delta_coupling_q_edgeworth.py)).
   This is open R&D: either a higher-order term in the substrate
   expansion or a per-Wedderburn-block correction is needed.

When all three are addressed, this conjecture can be promoted to
`prop:delta-coupling-substrate-form` with a full categorical
derivation.

## Refuted alternative: q-Edgeworth κ_3 ansatz

A natural alternative — that $\Delta_{\mathrm{coupling}}$ arises from
the leading q-Edgeworth correction to the q-CLT limit
([`conj:q-clt-non-commutative`](#conj:q-clt-non-commutative)) —
was tested in
[`probe_delta_coupling_q_edgeworth.py`](folio-assistant/computations/probe_delta_coupling_q_edgeworth.py)
and is empirically refuted. The q-skewness
$\kappa_3 = \mathrm{tr}_M(\tilde\sigma_1^3) \approx -0.675$ at $q_0$
has the WRONG SIGN for a positive Δ_coupling; all five q-Edgeworth
candidate forms (involving $\kappa_3$ and the variance
$\mathrm{Var}(\tilde\sigma)$) miss the target by $\geq 50$%.

## Relation to the H7a quantum

The expression $E_0 \cdot \log(1/h(q_0))$ is the **H7a energy
quantum** identified empirically in PR #645 at the doubly-magic
anchor. This conjecture identifies it structurally as
$E_0 \cdot [\log(1/(k_B T_q)) - \log(1 + q_0)]$, and the
$(A - 2)$ factor extends it to all magic-shell anchors. The
proposition [`prop:magic-shell-coupling-kappa`](#prop:magic-shell-coupling-kappa)
on PR #664 makes a related but distinct closed-form claim for the
per-(n_pp − n_nn) slope $\kappa$ at single-magic anchors; the two
should be unified once both are derivationally complete.
