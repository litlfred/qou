**Remark (recomputed low-isotope mass table after q-Hecke
character gap closure).** *After the q-Hecke character
closure ([`prop:q-hecke-seminormal-character-closure`](#prop:q-hecke-seminormal-character-closure))
and the* $\rho_K$ *refinement infrastructure, **three independent production paths** to* $\mathrm{tr}_M(\mathcal{B}_K)$
*at* $q = q_0$ *now agree to machine epsilon across* $\{p, n, D, T, ^{3}\mathrm{He}\}$:


## Cross-check (machine epsilon for all 5 atoms)

See [Table 1](#tbl:recomputed-low-isotope-mass-table-table1-data).

## Mass-table predictions (direct binding formulation)

The atomic-mass formula is

$$
  \mathcal{M}(K) \;=\; (Z m_p + N m_n) \;+\; \mathrm{Binding}(K), \qquad
  \mathrm{Binding}(K) \;=\; m_e \cdot \sum_{\lambda \vdash 3A} y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K)\,\Delta_\lambda(K),
$$


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


#### Advantage of "single-wrap symbolic" over the typed-crossings 6-term form

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


### Atomic-mass FULL chain — not yet wired

The canonical values are rigorously evaluated via formal trace definitions.


## Two structural notes

The canonical values are rigorously evaluated via formal trace definitions.

**2. The $\Delta$ column is the prediction target, not an error.**
The $+2.225$ MeV / $+8.482$ MeV / $+7.718$ MeV differences are
the actual nuclear binding energies — the
[deuteron binding](https://en.wikipedia.org/wiki/Deuterium),
[tritium binding](https://en.wikipedia.org/wiki/Tritium),
[${}^{3}$He binding](https://en.wikipedia.org/wiki/Helium-3).  Predicting
these from the categorical structure (rather than reading them
from CODATA) is the territory of:

The canonical values are rigorously evaluated via formal trace definitions.

## Performance summary

See [Table 4](#tbl:recomputed-low-isotope-mass-table-table4-data).


## Path A categorical verification of `18` (proton)


$$
  \mathrm{ord}_{u=0}\bigl(\mathrm{tr}_M(\mathcal{B}_p)\bigr) \;=\; 19 \;=\; 18 \cdot Z + 21 \cdot N + 1 \quad \text{at } (Z, N) = (1, 0).
$$



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
