**Algorithm (Nucleon mass ratio at $q = q_0$).**

> The name *mass identity* is deliberately not used here. It is already taken by
> [the vortex-filament mass-identity definition](#def:mass-identity), which is a different object — inertial mass as a
> nonabelian multiplicative integral around a vortex filament. This step computes the
> dimensionless nucleon ratio from the muon-anchored Hecke energy.
*Evaluate the nucleon mass ratio via the muon-anchored Hecke energy — the
form adopted here as canonical. Absolute nucleon mass in MeV is not a framework
prediction: $m_e$ sets the MeV scale by fiat, so the
predictive content is the dimensionless ratio $m_p/m_e$; the MeV outputs below
are that ratio rendered against the $m_e$ unit, a rendering rather than an
independent absolute-mass claim.*

$$
m_p = \dim V_{(2,1)} \cdot \bigl( m_\mu \cdot F_{\mathrm{Bor}} - |S_3| \cdot m_e \bigr), \qquad
m_\mu = m_e \cdot \mathrm{Vol}(4_1) / \hbar_q^2 ,
$$

*with the dimensionless Hecke factor
$F_{\mathrm{Bor}} = |\mathrm{tr}_M(\beta_{\mathrm{Bor}})| \cdot [3]_q! / q^3$,
via the canonical chain Steps 1 $\to$ 3 $\to$ 5 $\to$ here. This is the
**raw** identity: the substrate parameter $q_0$ is pinned by solving
exactly this form against $m_p/m_e$ (with no Habiro 4-loop dressing), so the
identity round-trips $m_p$ by construction and $m_\mu$, $m_n$ are the
predictions.*

> **Fit-tier dressing (not canonical).** An optional 4-loop factor
> $R_{\mathrm{s5bb}} = (1 + c_4 u^4)(1 + 4 u^5)(1 - 29 u^6)$,
> $u = b\,\hbar_q^2$, $b = \sqrt{(q^4+q^2+1)/(q^2+1)^2}$, is retained in
> the producer (`m_p_substrate_identity_50dps.habiro_ratio_s5bb`) but is
> **fit-tier, not derived**: the exact $c_4$ that lands $m_p$ on CODATA
> is *linear in the $q_0$ pin offset* (so $c_4$ merely reparametrizes the
> $\mu$–$p$ tension), and neither $c_4 = 46$ nor $c_4 = 4143/90$ is derived
> anywhere in this paper. Applied at the raw pin it *overshoots*
> CODATA $m_p$ by $\approx 242$ ppb. Which value to adopt — or whether to
> drop the dressing altogether — is unresolved.

### Input

- *Substrate parameter $q_0 \in \mathbb{R}_{> 1}$ (CAL-2 anchor;
  phys-obs layer pins on $m_p/m_e$).*
- *Electron mass $m_e$ in MeV (CAL-1 anchor).*
- *$\mathrm{Vol}(4_1) \approx 2.0299$ (figure-eight knot, Lobachevsky
  closed form $6\Lambda(\pi/3) = 2\,\mathrm{Cl}_2(\pi/3)$: two regular ideal
  tetrahedra, each of volume $\Lambda(\alpha)+\Lambda(\beta)+\Lambda(\gamma)$ at
  $\alpha=\beta=\gamma=\pi/3$ \cite{martelli2016} (Thm.~13.1.3, Cor.~13.1.4);
  the muon's knot).*

### Output

- *Mass ratios $m_p/m_e, m_n/m_e$, rendered against the $m_e$ scale as
  $m_p, m_n \in \mathbb{R}_{> 0}$ in MeV (the MeV figure is a rendering of the
  dimensionless ratio, not an absolute-mass prediction).*

### Algorithm

```
1. Compute |tr_M(β_Bor, q)| = (4 + h² − 3h⁴ − h⁶)/(h² + 4)
   (exact rational closed form; h = q − q⁻¹).
2. Form F_Bor = |tr_M(β_Bor)| · [3]_q! / q³   ([3]_q! = (1 + q)(1 + q + q²)).
3. Muon anchor: m_μ = m_e · Vol(4₁) / ℏ_q²  (ℏ_q = 1 − q⁻¹).
4. m_p = 2·(m_μ·F_Bor − 6·m_e)   (raw identity; no habiro dressing).
5. m_n = m_p + Q_β + m_e with the parameter-free Kashiwara b²
   truncation Q_β (derived_masses.q_beta_kashiwara_n2_mev).
6. Evaluate at q = q₀ with 50-dps mpmath precision.
```

### Correctness conditions

1. *[The nucleon-ratio existence proposition](#prop:mass-identity-exists) gives
   existence of the nucleon mass ratio in the QOU premise.*
2. *[The nucleon-ratio uniqueness proposition](#prop:mass-identity-unique) makes
   the identity unique modulo the calibration choice.*
3. *[The unified knot-mass theorem](#thm:knot-mass-formula-unified)
   ties the categorical scalar to the archimedean MeV observable.*

### Complexity

*Closed-form throughout (no Hecke machinery needed): sub-millisecond
at 50 dps.*

### Python API entry point

```python
from canonical_mass import (
    proton_neutron_mass_mev,
    nucleon_mass_mev,
    proton_qed_self_energy_borromean_mev,
    np_qed_splitting_borromean_conn_mev,
    neutron_mass_two_term_mev,
    gpmt_dmod_111,
    gpmt_dmod_211,
    gpmt_dmod_1111,
    gpmt_three_row_cumulants,
)

m_p_MeV, m_n_MeV = proton_neutron_mass_mev()
m_n_2term_MeV = neutron_mass_two_term_mev()
```

*`canonical_mass.py` is the single production facade. `proton_neutron_mass_mev()` and `nucleon_mass_mev(species)` read directly from the git-tracked 50-dps witness [`m-p-substrate-identity-50dps.witness.json`](../../../computations/m-p-substrate-identity-50dps.witness.json) produced by [`m_p_substrate_identity_50dps.py`](../../../computations/m_p_substrate_identity_50dps.py); there is **no inline formula fallback** (a missing witness raises `FileNotFoundError` rather than substituting an unverified value). The facade also exposes:*
- *the connected fourth-order Borromean $V^3 = (\sigma_1\sigma_2^{-1})^3$ Two-Term QED helpers `proton_qed_self_energy_borromean_mev()` ($M_p^{\mathrm{QED,conn}} = +{{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector1_proton_self_energy_and_mup_tension.candidates.derived_borromean_V3_plain.M_p_QED_keV | precision: 6 }}\;\mathrm{keV}$, closing the $+211.2\;\mathrm{ppb}$ $\mu$–$p$ anchor tension to $+{{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector1_proton_self_energy_and_mup_tension.candidates.derived_borromean_V3_plain.m_mu_err_ppb | precision: 3 }}\;\mathrm{ppb}$), `np_qed_splitting_borromean_conn_mev()` ($\Delta m_{\mathrm{QED}}^{\mathrm{conn}} = {{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector2_np_and_qbeta_two_term_splitting.Delta_m_QED_conn_plain_keV | precision: 6 }}\;\mathrm{keV}$), and `neutron_mass_two_term_mev()` ($m_n^{\mathrm{2\text{-}term}} = {{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector2_np_and_qbeta_two_term_splitting.substrate_identity_neutron_mass.m_n_2term_plain_MeV | precision: 10 }}\;\mathrm{MeV}$, $+{{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector2_np_and_qbeta_two_term_splitting.substrate_identity_neutron_mass.m_n_2term_plain_err_ppb | precision: 4 }}\;\mathrm{ppb}$ vs.\ CODATA 2022), backed by [`two-term-qed-isotope-and-nucleon-compute.witness.json`](../../../computations/two-term-qed-isotope-and-nucleon-compute.witness.json); and*
- *the Convention-D Geer–Patureau-Mirand–Turaev (GPMT) modified-dimension cumulant helpers `gpmt_dmod_111()` (${{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector3_light_isotopes_and_gpmt_cumulants.gpmt_modified_dimensions_and_cumulants_at_q0.dMod111 | precision: 6 }}$), `gpmt_dmod_211()` (${{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector3_light_isotopes_and_gpmt_cumulants.gpmt_modified_dimensions_and_cumulants_at_q0.dMod211 | precision: 6 }}$), `gpmt_dmod_1111()` ($+{{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector3_light_isotopes_and_gpmt_cumulants.gpmt_modified_dimensions_and_cumulants_at_q0.dMod1111 | precision: 6 }}$), and `gpmt_three_row_cumulants()`, which feed the three-dimensional tetrahedral $\alpha$-simplex coordination functional.*

### Witness contract

*Canonical witness:
[`m-p-substrate-identity-50dps.witness.json`](../../../computations/m-p-substrate-identity-50dps.witness.json)
(predictions $m_p, m_n, m_\mu$, CODATA anchors, ppb residuals).
Residuals for this and the other observables are collected in
[`per-observable-100x-status.witness.json`](../../../computations/per-observable-100x-status.witness.json).*

### Notes

*Superseded forms: the volume-density expressions
$m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \lambda_A / \hbar_q^2$
($\approx 966$ MeV, a CODATA-implied fit) and
$m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \mathrm{tr}_M / \hbar_q^2$
($\approx 406$ MeV) are NOT the absolute nucleon mass; the old
"+2.89 % $m_p$ gap" was the $\lambda_A$ fit artifact.
The per-block volume-density formula remains valid for **binding ratios only**
(the scale cancels) — the binding-side per-knot density is Step 9b's
$\Delta_\lambda$ frontier.*

*Anchor bookkeeping: at the proton-pinned $q_0$ the $m_p$ value is an
anchor round-trip (exact in ratio space), $m_\mu$ and $m_n$ are the
predictions; the pin's Habiro dressing reconciles the muon identity to
$\approx 1.4$ ppb (the $c_4$ discrepancy between the pin and the producer,
46 versus $4143/90$, is unresolved).*

*Linking-weight selection rule (binding-side, retained for Step 9b):
the factor
$\mathrm{lw}(c) = \frac{1}{c+1}\sum_{\lambda \vdash c+1} \dim_q V_\lambda$
reproduces $\mathrm{lw}(1)=1$ (muon) and
$\mathrm{lw}(3) = (3q^2+4+3q^{-2})/4$ (Family-A — identical to
the Family-A linking-weight helper, now deprecated for absolute mass), and gives
$\mathrm{lw}(2) = (q+1)^2/(3q)$
([the $c = 2$ selection-rule proposition](../climax-volume-mass/selection-rule-c2-prediction.md)).
Regression-tied to production by
[`binding_selection_rule_tau_closure.py`](../../../computations/binding_selection_rule_tau_closure.py)
$\to$ [witness](../../../computations/binding-selection-rule-tau-closure.witness.json).
The same $\mathrm{lw}(c)$ values are the SW-period anchors of the
depth-2 binding kernel — see
[`mba-step09b`](mba-step09b-per-isotope-binding.md).*
