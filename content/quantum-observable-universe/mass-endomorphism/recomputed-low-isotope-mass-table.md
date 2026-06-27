**Remark (recomputed low-isotope mass table after q-Hecke
character gap closure).** *After the q-Hecke character
closure ([`prop:q-hecke-seminormal-character-closure`](#prop:q-hecke-seminormal-character-closure))
and the* $\rho_K$ *refinement infrastructure, **three independent production paths** to* $\mathrm{tr}_M(\mathcal{B}_K)$
*at* $q = q_0$ *now agree to machine epsilon across* $\{p, n, D, T, ^{3}\mathrm{He}\}$:

1. **Canonical Markov-axiom reducer** —
   [`markov_trace_recursive.markov_trace_of_word`](../../../computations/markov/markov_trace_recursive.py)
   at mpfr 50-dps; reference values stored in
   [`atomic-tr-m-mpfr-50dps.witness.json`](../../../computations/atomic-tr-m-mpfr-50dps.witness.json).
2. **Hybrid partition-sum** (this PR) — 30-dps sympy `Float`
   for $y_\lambda$ via Wenzl's Schur principal specialization,
   float64 for $\chi^\lambda_q$ via Hoefsmit seminormal matrices,
   per-`n` cache.  Module:
   [`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`](../../../computations/wedderburn_jones_markov.py);
   driver: [`tr_m_q_hecke_seminormal.py`](../../../computations/tr_m_q_hecke_seminormal.py).
3. **Symbolic partition-sum** — full 50-dps mpmath via
   [`rho_k_h3a_refinement.py`](../../../computations/rho_k_h3a_refinement.py),
   the production path for binding-fraction $\Delta_\lambda$ analysis.

## Cross-check (machine epsilon for all 5 atoms)

See [Table 1](#tbl:recomputed-low-isotope-mass-table-table1-data).

## Mass-table predictions (direct binding formulation)

The atomic-mass formula is

$$
  \mathcal{M}(K) \;=\; (Z m_p + N m_n) \;+\; \mathrm{Binding}(K), \qquad
  \mathrm{Binding}(K) \;=\; m_e \cdot \sum_{\lambda \vdash 3A} y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K)\,\Delta_\lambda(K),
$$

with $\mathcal{B}_K = \mathtt{atom\_braid\_word\_3A}(Z, N) \in H_{3A}(q)$
the canonical 3A-strand atomic braid (β-decay-operator-unfolded form;
see [`mass_at_3A_proper.atom_braid_word_3A`](../../../computations/mass_at_3A_proper.py)),
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
[`atomic_mass_via_rho_k.py`](../../../computations/atomic_mass_via_rho_k.py)
(LO baseline, retained as reference);
[`binding_K_direct.py`](../../../computations/binding_K_direct.py)
(direct binding formulation; consumes $\Delta_\lambda$ from the
in-flight derivation race in PRs #602 / #603 / #613).

### Calibrated form (LO ρ_K with CODATA $m_p$, $m_n$ inputs)

This table is the calibrated form: $\rho_K^{\mathrm{LO}} = (Z m_p + N m_n)/(m_e |\mathrm{tr}_M|)$
consumes CODATA $m_p$ and $m_n$ as upstream inputs. Per the
[three-calibration discipline](three-calibration-inputs.md), this
violates CAL-1/2/3 by injecting $m_p$ and $m_n$ as 4th and 5th
calibration constants (tracked under
[Workplan 0b](../../../docs/audits/-workplan-0b-script-rewire-handoff.md)).
The proton and neutron rows are **tautological** by construction.

Witness:
[`atomic-mass-via-rho-k.witness.json`](../../../computations/atomic-mass-via-rho-k.witness.json).

See [Table 2](#tbl:recomputed-low-isotope-mass-table-table2-data).

† Proton and neutron predictions equal CODATA exactly because $m_p$
and $m_n$ are upstream inputs in this LO form; $0.000\%$ is a
calibration tautology, not a prediction quality.

### FULL $\mathfrak{Q}_\beta$ prediction (framework, no CODATA mass injection)

Per [`prop:neutron-qvalue-symbolic`](../particle-interactions/neutron-qvalue-symbolic.md)
the framework predicts the β-decay Q-value using only CAL-1 ($m_e$)
and CAL-2 ($q_0$) — no CAL-3 ($\mathfrak{Q}_\beta$) input, no CODATA $m_p$ or
$m_n$ injection. CAL-3 becomes the **output**, not an input.

The canonical closed form at single wrap:

$$
\boxed{
\mathfrak{Q}_\beta^{\text{pred}} \;=\;
\frac{m_e \cdot |q_0^2 - 2q_0 - 1| \cdot (q_0 + 1)}{2 q_0^3}
\;\approx\; 0.7836 \text{ MeV}
}
$$

vs CODATA $0.7823$ MeV — **+0.168% / +1.31 keV** framework prediction.

The closed form is derived via $\Delta(\mathrm{net}) = h(h-2)/2$
with $h = q_0 - q_0^{-1}$ (the symbolic NF difference between the
single-wrap proton $\mathrm{NF} = L_+ - \tfrac{h}{2}\sigma_0$ and
neutron $\mathrm{NF} = L_+ - h\sigma_0 - \tfrac{h}{2}\sigma_1 + \tfrac{h^2}{2}\gamma$),
times the energy scale $E_0 = m_e/(q_0(q_0-1))$. At single wrap the
$L_+$, $L_-$, and $e^-$ contributions cancel exactly between
proton and neutron, so the $Q$-value is carried entirely by the
$\gamma + \sigma_0 + \sigma_1$ channels:

See [Table 3](#tbl:recomputed-low-isotope-mass-table-table3-data).

The $+0.168\%$ / $+1.31$ keV residual is the **brane-tower
truncation correction** ([`neutron-qvalue-symbolic.md:110-114`](../particle-interactions/neutron-qvalue-symbolic.md)):
the derived $E_0 = m_e/(q_0(q_0-1))$ is the single-level
(Planck-tick) approximation; the exact tower-summed $E_0$ would
absorb this $0.17\%$. Closure path: Workplan 2 Phase 2 50-dps
$m_e^{\mathrm{Hecke}}$ lift.

#### Why "single-wrap symbolic" beats the typed-crossings 6-term form

An earlier draft used the typed-crossings 6-term decomposition
([`beta-decay-energy-scale.md`](../particle-interactions/beta-decay-energy-scale.md))
with $|\Delta(\mathrm{net})| = 0.18829$ from the witness, giving
$\mathfrak{Q}_\beta^{(\text{6-term})} = 0.7882$ MeV ($+0.747\%$). The
single-wrap form is **4.46$\times$ tighter** because the $L_\pm$ and
$e^-$ contributions, which exactly vanish in the symbolic
single-wrap difference, picked up small asymmetric finite-size
contributions in the typed-crossings basis. The single-wrap form
is the canonical clean prediction; the typed-crossings form is
retained in the witness for cross-check only.

#### Observable / virtual basis-dependence note

The "observable vs virtual" decomposition by Coxeter length
$\ell \ge 2$ vs $\ell < 2$ is only meaningful in the typed-
crossings 6-term basis (where it gives $58.46\% / 41.54\%$).
At single wrap, all $\ell \ge 2$ channels cancel by Hopf-content
matching between proton and neutron — the entire single-wrap
$Q$-value lives in the virtual ($\ell < 2$) sector. This is not
a contradiction: the typed-crossings basis is finer, and the
observable share reflects multi-wrap / finite-size structure
absent from the single-wrap closed form.

Witness:
[`q-beta-predicted.witness.json`](../../../computations/q-beta-predicted.witness.json)
( derived via
[`derived_masses.q_beta_predicted_mev`](../../../computations/derived_masses.py)).
3 assertions pass: residual $<0.5\%$, residual $<2$ keV,
single-wrap residual $<$ typed-crossings residual.

### Atomic-mass FULL chain — not yet wired

The proton, neutron, and light-nucleus rest masses do **not** yet
have a FULL framework prediction wired. The LO form above is
tautological by construction (the $|\mathrm{tr}_M|$ factor cancels
exactly in $\rho_K^{\mathrm{LO}} \cdot m_e \cdot |\mathrm{tr}_M|$,
so $\mathcal{M}^{\mathrm{LO}}_\text{pred} = Z m_p + N m_n$); the
Strategy-3 multi-term implementation in
[`atomic_braid_mass_table.py`](../../../computations/atomic_braid_mass_table.py)
has a known structural bug (multiplicative T1 base instead of
additive LP active-set, per its own deprecation banner lines 24-46).
Per owner directive, neither is the FULL framework
prediction — both should be replaced by the unified knot mass
formula $M(\mathfrak{H}) = \rho \cdot [|\mathrm{tr}_M(T_w)| +
\mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})]$ once the LP-dual
shadow-price closure ([`prop:operator-selection-lp`](operator-selection-lp.md))
or Phase 2 50-dps $m_e^{\mathrm{Hecke}}$ lift lands.

The accessors
[`derived_masses.proton_mass_mev`](../../../computations/derived_masses.py)
and friends raise `NotImplementedError` with pointers to these
blockers; consumers must NOT fall back to the LO or Strategy-3 forms.

## Two structural notes

**1. The 0.000 % on $p$ and $n$ is a calibration-discipline
violation, not a prediction.** The ρ_K leading-order ansatz used
in this table consumes $m_p$ and $m_n$ as CODATA inputs (via
[`computations/substrate/codata_constants.py`](../../../computations/substrate/codata_constants.py)),
so for $K = p$ ($Z = 1, N = 0$) and $K = n$ ($Z = 0, N = 1$)
the formula returns the input mass exactly. **This is a bug, not
a feature**: the QOU framework admits exactly three calibration
inputs ([three calibration inputs](three-calibration-inputs.md))
— CAL-1 $= m_e$, CAL-2 $= \mathfrak{D}_\beta$ (proxy $m_\mu/m_e$,
fixing $q_0$), CAL-3 $= \mathfrak{D}_\pi$ (proxy $m_\pi$, the meson
scale). The hadronic energy scale $E_0 = m_e/(q_0(q_0-1))$ is
**derived** from CAL-1 + CAL-2 (equivalently $E_0 = \mathfrak{Q}_\beta(n)/\lvert\Delta(\mathrm{net})\rvert$
via the CAL-2 proxy $\mathfrak{Q}_\beta$), not a calibration input. $m_p$ and $m_n$
are **predictions** of the framework, derivable as
$m_p = |\mathrm{tr}_M(p, q_0)| \cdot E_0$ and
$m_n = m_p + \mathfrak{Q}_\beta + m_e$ per the 3-input convention recommended
in [`neutron-gap-probes-round3.witness.json`](../../../computations/neutron-gap-probes-round3.witness.json).
The script-side migration is tracked as Workplan 0b
(see [`docs/audits/-1ppb-workplan-update.md`](../../../docs/audits/-1ppb-workplan-update.md));
until it lands, the $0.000\%$ rows above are tautologies and the
$D / T / {}^{3}\mathrm{He}$ residuals understate the true binding
prediction error by the n/p split scale ($\sim 0.14\%$).

**2. The $\Delta$ column is the prediction target, not an error.**
The $+2.225$ MeV / $+8.482$ MeV / $+7.718$ MeV differences are
the actual nuclear binding energies — the
[deuteron binding](https://en.wikipedia.org/wiki/Deuterium),
[tritium binding](https://en.wikipedia.org/wiki/Tritium),
[${}^{3}$He binding](https://en.wikipedia.org/wiki/Helium-3).  Predicting
these from the categorical structure (rather than reading them
from CODATA) is the territory of:

- $\rho_K^{\text{full}}(Z, N) = \rho_K^{\mathrm{LO}}(Z, N) + (1/|\mathrm{tr}_M|)
  \cdot \sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda(K)$
  ([`rho_k_h3a_refinement.py`](../../../computations/rho_k_h3a_refinement.py)
  on  deuteron-only proof-of-concept; closure error
  $2.7 \times 10^{-48}$ MeV by construction).
- The per-block binding fractions $\Delta_\lambda(K)$ — currently
  determined by Occam's-razor minimal-perturbation selection
  (single dominant partition); the categorical derivation of
  $\Delta_\lambda$ from first principles is an open research
  question.

## Performance summary

See [Table 4](#tbl:recomputed-low-isotope-mass-table-table4-data).

The hybrid technique (30-dps $y_\lambda$ + float64 $\chi^\lambda_q$,
with per-`n` cache) is the **recommended default** for
partition-sum consumers needing better than $10^{-5}$ agreement
without the overhead of full 50-dps mpmath.

## Path A categorical verification of `18` (proton)

The atomic-shift exponent $\mathrm{shift}_{\mathrm{NF}}(\mathcal{B}_K)$
that controls the $u$-power in the $D(u)$ denominator
([`prop:per-nucleon-shift-additive-linearity`](per-nucleon-shift-additive-linearity.md))
is now categorically verified for the proton by direct symbolic
Hoefsmit pole-order analysis
([`per_irrep_pole_proton_h3.py`](../../../computations/per_irrep_pole_proton_h3.py),
witness:
[`per-irrep-pole-proton-h3.witness.json`](../../../computations/per-irrep-pole-proton-h3.witness.json)):

$$
  \mathrm{ord}_{u=0}\bigl(\mathrm{tr}_M(\mathcal{B}_p)\bigr) \;=\; 19 \;=\; 18 \cdot Z + 21 \cdot N + 1 \quad \text{at } (Z, N) = (1, 0).
$$

**Cross-confirmation:** the orthogonal computation in
[`shift_from_nf_basis.py`](../../../computations/shift_from_nf_basis.py)
(NF-basis decomposition, recorded in
[`shift-from-nf-basis.witness.json`](../../../computations/shift-from-nf-basis.witness.json))
independently reports `shift_proton_h3 = 19` — two independent
symbolic methods agree exactly on the per-proton u-pole.

**Multi-nucleon verification (deuteron):**
[`per_irrep_pole_deuteron_h6.py`](../../../computations/per_irrep_pole_deuteron_h6.py)
(witness:
[`per-irrep-pole-deuteron-h6.witness.json`](../../../computations/per-irrep-pole-deuteron-h6.witness.json))
extends Path A to $A = 2$ via three optimisations: cached
symbolic $y_\lambda(q)$ for $n = 6$, auto-cached symbolic
$\chi^\lambda_q(\beta_D)$
([`chi-deuteron-h6.witness.json`](../../../computations/chi-deuteron-h6.witness.json)),
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
- [`docs/audits/-q-hecke-character-gap-closure.md`](../../../docs/audits/-q-hecke-character-gap-closure.md)
  — full audit of the closure with three-path comparison.
- [`docs/audits/-per-irrep-pole-18-21-research-note.md`](../../../docs/audits/-per-irrep-pole-18-21-research-note.md)
  — Path A audit doc with reading correction.
- [`docs/audits/-rho-k-mass-table-audit.md`](../../../docs/audits/-rho-k-mass-table-audit.md)
  — pre-q-Hecke audit of the ρ_K mass table at 0.23 % MAE.
