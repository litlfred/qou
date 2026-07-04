**Algorithm (Mass identity at $q = q_0$).**
*Evaluate the absolute nucleon mass via the muon-anchored Hecke energy
(owner ruling 2026-06-24)*

$$
m_p = \dim V_{(2,1)} \cdot \bigl( m_\mu \cdot F_{\mathrm{Bor}} - |S_3| \cdot m_e \bigr) \cdot R_{\mathrm{s5bb}}(q_0), \qquad
m_\mu = m_e \cdot \mathrm{Vol}(4_1) / \hbar_q^2 ,
$$

*with the dimensionless Hecke factor
$F_{\mathrm{Bor}} = |\mathrm{tr}_M(\beta_{\mathrm{Bor}})| \cdot [3]_q! / q^3$
and the s5bb Habiro 4-loop dressing
$R_{\mathrm{s5bb}} = (1 + c_4 u^4)(1 + 4 u^5)(1 - 29 u^6)$,
$u = b\,\hbar_q^2$, $b = \sqrt{(q^4+q^2+1)/(q^2+1)^2}$,
$c_4 = 4143/90$, via the canonical chain Steps 1 $\to$ 3 $\to$ 5
$\to$ here.*

### Input

- *Substrate parameter $q_0 \in \mathbb{R}_{> 1}$ (CAL-2 anchor;
  phys-obs layer pins on $m_p/m_e$).*
- *Electron mass $m_e$ in MeV (CAL-1 anchor).*
- *$\mathrm{Vol}(4_1) \approx 2.0299$ (figure-eight knot, Lobachevsky
  closed form; the muon's knot).*

### Output

- *Predicted masses $m_p, m_n \in \mathbb{R}_{> 0}$ in MeV.*

### Algorithm

```
1. Compute |tr_M(β_Bor, q)| = (4 + h² − 3h⁴ − h⁶)/(h² + 4)
   (Lean-proved closed form, BorromeanMarkovTrace.lean; h = q − q⁻¹).
2. Form F_Bor = |tr_M(β_Bor)| · [3]_q! / q³   ([3]_q! Lean-proved).
3. Muon anchor: m_μ = m_e · Vol(4₁) / ℏ_q²  (ℏ_q = 1 − q⁻¹).
4. m_p = 2·(m_μ·F_Bor − 6·m_e) · habiro_ratio_s5bb(q₀).
5. m_n = m_p + Q_β + m_e with the parameter-free Kashiwara b²
   truncation Q_β (derived_masses.q_beta_kashiwara_n2_mev).
6. Evaluate at q = q₀ with 50-dps mpmath precision.
```

### Correctness conditions

1. *[`prop:mass-identity-exists`](#prop:mass-identity-exists) gives
   existence of the mass identity in the QOU premise.*
2. *[`prop:mass-identity-unique`](#prop:mass-identity-unique) makes
   the identity unique modulo the calibration choice.*
3. *[`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified)
   ties the categorical scalar to the archimedean MeV observable.*

### Complexity

*Closed-form throughout (no Hecke machinery needed): sub-millisecond
at 50 dps.*

### Python API entry point

```python
from canonical_mass import proton_neutron_mass_mev

m_p_MeV, m_n_MeV = proton_neutron_mass_mev()
```

*`computations/canonical_mass.py` is the SINGLE facade (owner ruling
2026-06-24): it prefers the producer witness and falls back to the
live formula above (including the $R_{\mathrm{s5bb}}$ dressing —
facade/producer alignment fixed 2026-07-04, PR #3266). Producer:
[`m_p_substrate_identity_50dps.py`](../../../computations/m_p_substrate_identity_50dps.py).*

### Witness contract

*Canonical witness:
[`m-p-substrate-identity-50dps.witness.json`](../../../computations/m-p-substrate-identity-50dps.witness.json)
(predictions $m_p, m_n, m_\mu$, CODATA anchors, ppb residuals).
Dashboard roll-up:
[`per-observable-100x-status.witness.json`](../../../computations/per-observable-100x-status.witness.json).*

### Notes

*Deprecation (owner ruling 2026-06-24, guardrail
[`canonical-mass-formula-guardrail.md`](../../../docs/canonical-mass-formula-guardrail.md)):
the volume-density forms
$m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \lambda_A / \hbar_q^2$
($\approx 966$ MeV, a CODATA-implied fit) and
$m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \mathrm{tr}_M / \hbar_q^2$
($\approx 406$ MeV) are NOT the absolute nucleon mass; the old
"+2.89 % $m_p$ gap" was the $\lambda_A$ fit artifact.
`vol_density_per_block` remains valid for **binding ratios only**
(the scale cancels) — the binding-side per-knot density is Step 9b's
$\Delta_\lambda$ frontier.*

*Anchor bookkeeping: at the proton-pinned $q_0$ the $m_p$ value is an
anchor round-trip (exact in ratio space), $m_\mu$ and $m_n$ are the
predictions; the pin's Habiro dressing reconciles the muon identity to
$\approx 1.4$ ppb (per-stage attribution in the
[2026-07-03 deuteron ledger](../../../docs/audits/2026-07-03-deuteron-from-scratch-error-ledger.md);
the $c_4$ pin-vs-producer 46 vs $4143/90$ reconcile is owner-gated,
bean `2i8g`).*

*Linking-weight selection rule (binding-side, retained for Step 9b):
the factor
$\mathrm{lw}(c) = \frac{1}{c+1}\sum_{\lambda \vdash c+1} \dim_q V_\lambda$
reproduces $\mathrm{lw}(1)=1$ (muon) and
$\mathrm{lw}(3) = (3q^2+4+3q^{-2})/4$ (Family-A — bit-for-bit equal to
`linking_weight_family_a`, now deprecated for absolute mass), and gives
$\mathrm{lw}(2) = (q+1)^2/(3q)$
([`prop:selection-rule-c2-prediction`](../climax-volume-mass/selection-rule-c2-prediction.md)).
Regression-tied to production by
[`binding_selection_rule_tau_closure.py`](../../../computations/binding_selection_rule_tau_closure.py)
$\to$ [witness](../../../computations/binding-selection-rule-tau-closure.witness.json).
The same $\mathrm{lw}(c)$ values are the SW-period anchors of the
depth-2 binding kernel — see
[`mba-step09b`](mba-step09b-per-isotope-binding.md).*
