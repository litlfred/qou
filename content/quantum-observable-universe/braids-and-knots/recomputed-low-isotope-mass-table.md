**Remark (recomputed low-isotope mass table after q-Hecke
character gap closure).** *After PR #572's q-Hecke character
closure ([`prop:q-hecke-seminormal-character-closure`](#prop:q-hecke-seminormal-character-closure))
and the cherry-picked* $\rho_K$ *refinement infrastructure from
PR #564, **three independent production paths** to* $\mathrm{tr}_M(\beta_K)$
*at* $q = q_0$ *now agree to machine epsilon across* $\{p, n, D, T, ^{3}\mathrm{He}\}$:

1. **Canonical Markov-axiom reducer** —
   [`markov_trace_recursive.markov_trace_of_word`](../../../folio-assistant/computations/markov_trace_recursive.py)
   at mpfr 50-dps; reference values stored in
   [`atomic-tr-m-mpfr-50dps.witness.json`](../../../folio-assistant/computations/atomic-tr-m-mpfr-50dps.witness.json).
2. **Hybrid partition-sum** (this PR) — 30-dps sympy `Float`
   for $y_\lambda$ via Wenzl's Schur principal specialization,
   float64 for $\chi^\lambda_q$ via Hoefsmit seminormal matrices,
   per-`n` cache.  Module:
   [`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`](../../../folio-assistant/computations/wedderburn_jones_markov.py);
   driver: [`tr_m_q_hecke_seminormal.py`](../../../folio-assistant/computations/tr_m_q_hecke_seminormal.py).
3. **Symbolic partition-sum** (PR #564) — full 50-dps mpmath via
   [`rho_k_h3a_refinement.py`](../../../folio-assistant/computations/rho_k_h3a_refinement.py),
   the production path for binding-fraction $\Delta_\lambda$ analysis.

## Cross-check (machine epsilon for all 5 atoms)

| Atom | $Z$ | $N$ | $n = 3A$ | canonical $|\mathrm{tr}_M|$ | hybrid partition-sum | rel err |
|---|:-:|:-:|:-:|---:|---:|---:|
| $p$ | 1 | 0 | 3 | 1.0653062286 | 1.0653062286 | $3.96 \times 10^{-15}$ |
| $n$ | 0 | 1 | 3 | 0.9232332972 | 0.9232332972 | $4.21 \times 10^{-15}$ |
| $D$ | 1 | 1 | 6 | 0.3882864715 | 0.3882864715 | $7.01 \times 10^{-15}$ |
| $T$ | 1 | 2 | 9 | 0.1040521187 | 0.1040521187 | $1.07 \times 10^{-14}$ |
| $^{3}\mathrm{He}$ | 2 | 1 | 9 | 0.2065408586 | 0.2065408586 | $1.03 \times 10^{-14}$ |

## Mass-table predictions (direct binding formulation)

The atomic-mass formula is

$$
  \mathcal{M}(K) \;=\; (Z m_p + N m_n) \;+\; \mathrm{Binding}(K), \qquad
  \mathrm{Binding}(K) \;=\; m_e \cdot \sum_{\lambda \vdash 3A} y_\lambda(q)\,\chi^\lambda(\beta_K)\,\Delta_\lambda(K),
$$

with $\beta_K = \mathtt{atom\_braid\_word\_3A}(Z, N) \in H_{3A}(q)$
the canonical 3A-strand atomic braid (β-decay-operator-unfolded form;
see [`mass_at_3A_proper.atom_braid_word_3A`](../../../folio-assistant/computations/mass_at_3A_proper.py)),
$y_\lambda$ the canonical Wenzl Markov weight (see
[`prop:markov-trace-recursive-reducer`](markov-trace-recursive-reducer.md)),
$\chi^\lambda$ the Hoefsmit q-character of the atomic braid, and
$\Delta_\lambda(K)$ the per-Wedderburn-block binding fraction.

This direct form supersedes the equivalent but cosmetically
tautological factorisation
$\mathcal{M}(K) = \rho_K \cdot m_e \cdot |\mathrm{tr}_M(K)|$ with
$\rho_K = \rho_K^{\mathrm{LO}} + (\Sigma_\lambda y_\lambda \chi^\lambda \Delta_\lambda)/|\mathrm{tr}_M|$:
the leading-order term $\rho_K^{\mathrm{LO}} = (Z m_p + N m_n)/(m_e\,|\mathrm{tr}_M|)$
has the $|\mathrm{tr}_M|$ factor cancel against the formula's outer
$|\mathrm{tr}_M|$ multiplier, so $\rho_K^{\mathrm{LO}}\cdot m_e\,|\mathrm{tr}_M| = Z m_p + N m_n$
identically.  The factorisation packages constituent + binding
into a single symbol $\rho_K$, but the only physical content is
the $\Delta_\lambda$ correction; we therefore write the formula
with constituent sum and binding side by side.

Reference scripts:
[`atomic_mass_via_rho_k.py`](../../../folio-assistant/computations/atomic_mass_via_rho_k.py)
(LO baseline, retained as reference);
[`binding_K_direct.py`](../../../folio-assistant/computations/binding_K_direct.py)
(direct binding formulation; consumes $\Delta_\lambda$ from the
in-flight derivation race in PRs #602 / #603 / #613).

### Calibrated form (LO ρ_K with CODATA $m_p$, $m_n$ inputs)

This table is the calibrated form: $\rho_K^{\mathrm{LO}} = (Z m_p + N m_n)/(m_e |\mathrm{tr}_M|)$
consumes CODATA $m_p$ and $m_n$ as upstream inputs. Per the
[three-calibration discipline](three-calibration-inputs.md), this
violates CAL-1/2/3 by injecting $m_p$ and $m_n$ as 4th and 5th
calibration constants (tracked under
[Workplan 0b](../../../docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md)).
The proton and neutron rows are **tautological** by construction.

Witness:
[`atomic-mass-via-rho-k.witness.json`](../../../folio-assistant/computations/atomic-mass-via-rho-k.witness.json).

| Atom | $\mathcal{M}_{\text{pred}}^{\mathrm{LO}}$ (MeV) | $\mathcal{M}_{\text{CODATA}}$ (MeV) | $\Delta$ (MeV) | rel err | binding (CODATA) |
|---|---:|---:|---:|---:|---:|
| $p$ † | 938.272088 | 938.272088 | 0.0000 | 0.000 % | (anchor) |
| $n$ † | 939.565421 | 939.565421 | 0.0000 | 0.000 % | (anchor) |
| $D$ | 1877.837509 | 1875.612943 | $+2.2246$ | $+0.119$ % | 2.225 MeV |
| $T$ | 2817.402929 | 2808.921133 | $+8.4818$ | $+0.302$ % | 8.482 MeV |
| $^{3}\mathrm{He}$ | 2816.109597 | 2808.391607 | $+7.7180$ | $+0.275$ % | 7.718 MeV |
| $^{4}\mathrm{He}$ | 3755.675017 | 3727.379378 | $+28.2956$ | $+0.759$ % | 28.295 MeV |

† Proton and neutron predictions equal CODATA exactly because $m_p$
and $m_n$ are upstream inputs in this LO form; $0.000\%$ is a
calibration tautology, not a prediction quality.

### FULL Q_β prediction (framework, no CODATA mass injection)

Per [`prop:beta-decay-energy-scale`](../../../content/quantum-observable-universe/particle-interactions/beta-decay-energy-scale.md)
the framework predicts the β-decay Q-value using only CAL-1 ($m_e$)
and CAL-2 ($q_0$) — no CAL-3 ($Q_\beta$) input, no CODATA $m_p$ or
$m_n$ injection. CAL-3 becomes the **output**, not an input.

$$
E_0^{\text{full}} = \frac{m_e}{q_0(q_0 - 1)} = m_e \cdot c_q^2 \cdot \hbar_q \approx 4.186\,\text{MeV},
\qquad
Q_\beta^{\text{pred}} = |\Delta(\mathrm{net})| \cdot E_0^{\text{full}}
$$

with $\Delta(\mathrm{net}) = \mathrm{net}(\mathfrak{n}) - \mathrm{net}(\mathfrak{p})
= -0.18829$ from the GS-NF coefficients of the canonical neutron
and proton braids. **Result**: $Q_\beta^{\text{pred}} = 0.7882$ MeV
vs CODATA $0.7823$ MeV — $0.75\%$ framework prediction.

The $0.75\%$ residual is the brane-tower correction
([beta-decay-energy-scale.md §Calibration cross-check](../../../content/quantum-observable-universe/particle-interactions/beta-decay-energy-scale.md));
the cross-check $E_0^{(\text{cal})} = Q_\beta^{\text{CODATA}} / |\Delta(\mathrm{net})| = 4.155$ MeV
agrees with the derived $4.186$ MeV to the same $0.75\%$.

#### Observable / virtual decomposition

Per [`beta-decay-energy-scale.md §"Observable vs virtual"`](../../../content/quantum-observable-universe/particle-interactions/beta-decay-energy-scale.md),
NF terms split by Coxeter length $\ell$:

| | $\ell$ | Knots / links | $\Delta_\lambda$ | $\Delta_\lambda \cdot E_0$ (MeV) | fraction |
|---|:-:|---|---:|---:|---:|
| $\gamma$ (identity) | 0 | photon | $-0.10205$ | $+0.4240$ | virtual |
| $\sigma_0$ | 1 | virtual crossing | $+0.01240$ | $-0.0515$ | virtual |
| $\sigma_1$ | 1 | virtual crossing | $+0.01143$ | $-0.0475$ | virtual |
| $L_+$ | 2 | Hopf link | $-0.10899$ | $+0.4529$ | **observable** |
| $L_-$ | 2 | Hopf link | $-0.00010$ | $+0.0004$ | **observable** |
| $e^-$ | 3 | trefoil $3_1$ | $-0.00098$ | $+0.0041$ | **observable** |
|  |  |  | **Sum** | **$+0.7882$** |  |

| Component | $\lvert\Delta\rvert$ | $\Delta \cdot E_0$ (MeV) | fraction |
|---|---:|---:|---:|
| **Observable** ($\ell \ge 2$): Hopf links $L_\pm$ + trefoil $e^-$ | $0.11007$ | $0.4608$ | **58.46%** |
| **Virtual** ($\ell < 2$): identity $\gamma$ + crossings $\sigma_0, \sigma_1$ | $0.07822$ | $0.3274$ | $41.54\%$ |
| Total | $0.18829$ | $0.7882$ | $100\%$ |

The **observable** component is the topologically non-trivial
part — physical kinetic energy released in the β-decay event. The
**virtual** component is the gauge / vacuum-debt contribution that
cancels in asymptotic states (single crossings $\sigma_0, \sigma_1$
are gauge artefacts; identity $\gamma$ is the photon-debt baseline).

Witness:
[`q-beta-predicted.witness.json`](../../../folio-assistant/computations/q-beta-predicted.witness.json)
(2026-05-10, derived via
[`derived_masses.q_beta_predicted_mev`](../../../folio-assistant/computations/derived_masses.py)).

### Atomic-mass FULL chain — not yet wired

The proton, neutron, and light-nucleus rest masses do **not** yet
have a FULL framework prediction wired. The LO form above is
tautological by construction (the $|\mathrm{tr}_M|$ factor cancels
exactly in $\rho_K^{\mathrm{LO}} \cdot m_e \cdot |\mathrm{tr}_M|$,
so $\mathcal{M}^{\mathrm{LO}}_\text{pred} = Z m_p + N m_n$); the
Strategy-3 multi-term implementation in
[`atomic_braid_mass_table.py`](../../../folio-assistant/computations/atomic_braid_mass_table.py)
has a known structural bug (multiplicative T1 base instead of
additive LP active-set, per its own deprecation banner lines 24-46).
Per owner directive 2026-05-10, neither is the FULL framework
prediction — both should be replaced by the unified knot mass
formula $M(\mathfrak{H}) = \rho \cdot [|\mathrm{tr}_M(T_w)| +
\mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})]$ once the LP-dual
shadow-price closure ([`prop:operator-selection-lp`](operator-selection-lp.md))
or Phase 2 50-dps $m_e^{\mathrm{Hecke}}$ lift lands.

The accessors
[`derived_masses.proton_mass_mev`](../../../folio-assistant/computations/derived_masses.py)
and friends raise `NotImplementedError` with pointers to these
blockers; consumers must NOT fall back to the LO or Strategy-3 forms.

## Two structural notes

**1. The 0.000 % on $p$ and $n$ is a calibration-discipline
violation, not a prediction.** The ρ_K leading-order ansatz used
in this table consumes $m_p$ and $m_n$ as CODATA inputs (via
[`folio-assistant/computations/codata_constants.py`](../../../folio-assistant/computations/codata_constants.py)),
so for $K = p$ ($Z = 1, N = 0$) and $K = n$ ($Z = 0, N = 1$)
the formula returns the input mass exactly. **This is a bug, not
a feature**: the QOU framework admits exactly three calibration
inputs ([three calibration inputs](three-calibration-inputs.md))
— CAL-1 $= m_e$, CAL-2 $= m_\mu/m_e$ (fixes $q_0$),
CAL-3 $= Q_\beta(n)$ (fixes hadronic scale $E_0$). $m_p$ and $m_n$
are **predictions** of the framework, derivable as
$m_p = |\mathrm{tr}_M(p, q_0)| \cdot E_0$ and
$m_n = m_p + Q_\beta + m_e$ per the 3-input convention recommended
in [`neutron-gap-probes-round3.witness.json`](../../../folio-assistant/computations/neutron-gap-probes-round3.witness.json).
The script-side migration is tracked as Workplan 0b
(see [`docs/audits/2026-05-10-1ppb-workplan-update.md`](../../../docs/audits/2026-05-10-1ppb-workplan-update.md));
until it lands, the $0.000\%$ rows above are tautologies and the
$D / T / {}^{3}\mathrm{He}$ residuals understate the true binding
prediction error by the n/p split scale ($\sim 0.14\%$).

**2. The $\Delta$ column is the prediction target, not an error.**
The $+2.225$ MeV / $+8.482$ MeV / $+7.718$ MeV differences are
the actual nuclear binding energies — the
[deuteron binding](https://en.wikipedia.org/wiki/Deuterium),
[tritium binding](https://en.wikipedia.org/wiki/Tritium),
[³He binding](https://en.wikipedia.org/wiki/Helium-3).  Predicting
these from the categorical structure (rather than reading them
from CODATA) is the territory of:

- $\rho_K^{\text{full}}(Z, N) = \rho_K^{\mathrm{LO}}(Z, N) + (1/|\mathrm{tr}_M|)
  \cdot \sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda(K)$
  ([`rho_k_h3a_refinement.py`](../../../folio-assistant/computations/rho_k_h3a_refinement.py)
  on PR #564 deuteron-only proof-of-concept; closure error
  $2.7 \times 10^{-48}$ MeV by construction).
- The per-block binding fractions $\Delta_\lambda(K)$ — currently
  determined by Occam's-razor minimal-perturbation selection
  (single dominant partition); the categorical derivation of
  $\Delta_\lambda$ from first principles is an open research
  question.

## Performance summary

| Path | Time (5 atoms) | Precision floor |
|---|---:|---:|
| Canonical reducer (`markov_trace_recursive`, 50 dps mpmath) | ~30 s | $10^{-50}$ |
| Hybrid partition-sum (30-dps $y_\lambda$ + float64 $\chi^\lambda_q$) | ~66 s | $10^{-14}$ (machine $\varepsilon$) |
| Full mpmath partition-sum (PR #564) | ~5–10 min | $10^{-50}$ |
| Pure float64 partition-sum (legacy) | ~1 s | $10^{-5}$ at $n = 9$ |
| Pure symbolic Wenzl + symbolic χ^λ | timeout (>4 min) | exact |

The hybrid technique (30-dps $y_\lambda$ + float64 $\chi^\lambda_q$,
with per-`n` cache) is the **recommended default** for
partition-sum consumers needing better than $10^{-5}$ agreement
without the overhead of full 50-dps mpmath.

## Path A categorical verification of `18` (proton, 2026-05-09)

The atomic-shift exponent $\mathrm{shift}_{\mathrm{NF}}(\beta_K)$
that controls the $u$-power in the $D(u)$ denominator
([`prop:per-nucleon-shift-additive-linearity`](per-nucleon-shift-additive-linearity.md))
is now categorically verified for the proton by direct symbolic
Hoefsmit pole-order analysis
([`per_irrep_pole_proton_h3.py`](../../../folio-assistant/computations/per_irrep_pole_proton_h3.py),
witness:
[`per-irrep-pole-proton-h3.witness.json`](../../../folio-assistant/computations/per-irrep-pole-proton-h3.witness.json)):

$$
  \mathrm{ord}_{u=0}\bigl(\mathrm{tr}_M(\beta_p)\bigr) \;=\; 19 \;=\; 18 \cdot Z + 21 \cdot N + 1 \quad \text{at } (Z, N) = (1, 0).
$$

**Cross-confirmation:** the orthogonal computation in
[`shift_from_nf_basis.py`](../../../folio-assistant/computations/shift_from_nf_basis.py)
(NF-basis decomposition, recorded in
[`shift-from-nf-basis.witness.json`](../../../folio-assistant/computations/shift-from-nf-basis.witness.json))
independently reports `shift_proton_h3 = 19` — two independent
symbolic methods agree exactly on the per-proton u-pole.

**Multi-nucleon verification (deuteron, 2026-05-09):**
[`per_irrep_pole_deuteron_h6.py`](../../../folio-assistant/computations/per_irrep_pole_deuteron_h6.py)
(witness:
[`per-irrep-pole-deuteron-h6.witness.json`](../../../folio-assistant/computations/per-irrep-pole-deuteron-h6.witness.json))
extends Path A to $A = 2$ via three optimisations: cached
symbolic $y_\lambda(q)$ for $n = 6$, auto-cached symbolic
$\chi^\lambda_q(\beta_D)$
([`chi-deuteron-h6.witness.json`](../../../folio-assistant/computations/chi-deuteron-h6.witness.json)),
and per-term pole order. The per-term maximum is uniquely $40$
at $\lambda = (4, 1, 1)$, so

$$
  \mathrm{ord}_{u=0}\bigl(\mathrm{tr}_M(\beta_D)\bigr) \;=\; 40 \;=\; 18 \cdot 1 + 21 \cdot 1 + 1
$$

rigorously (lower-order per-term poles cannot cancel a strict
maximum). Multi-nucleon Path A closed.

The "$18$" in $18Z + 21N + 1$ is the per-proton additive
coefficient of the FULL summed $u$-pole order, not the q-pole
order of any per-irrep $\chi^\lambda_q$ (per-irrep max at $H_3$
is $11$ at $\lambda = (2, 1)$).

## Cross-references

- [`prop:atomic-mass-gb-nf`](atomic-mass-gb-nf.md) — the master
  mass formula $\mathcal{M}(K) = \rho_K \cdot m_e \cdot |\mathrm{tr}_M|$.
- [`prop:q-hecke-seminormal-character-closure`](q-hecke-seminormal-character-closure.md)
  — the partition-sum / canonical-reducer agreement at machine $\varepsilon$.
- [`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md)
  — the operator-valued LR-block formula behind the partition sum.
- [`prop:per-nucleon-shift-additive-linearity`](per-nucleon-shift-additive-linearity.md)
  — Path A categorical verification of the per-proton coefficient.
- [`docs/audits/2026-05-08-q-hecke-character-gap-closure.md`](../../../docs/audits/2026-05-08-q-hecke-character-gap-closure.md)
  — full audit of the closure with three-path comparison.
- [`docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md`](../../../docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md)
  — Path A audit doc with reading correction.
- [`docs/audits/2026-05-08-rho-k-mass-table-audit.md`](../../../docs/audits/2026-05-08-rho-k-mass-table-audit.md)
  — pre-q-Hecke audit of the ρ_K mass table at 0.23 % MAE.
