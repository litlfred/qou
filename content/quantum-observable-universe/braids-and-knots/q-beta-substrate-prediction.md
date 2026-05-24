**Proposition** (substrate prediction of $Q_\beta(n)$).
*Let $m_e$ be the electron mass (CAL-1) and $q_0$ be the substrate
parameter (CAL-2, fixed by $m_\mu / m_e$). The free-neutron
$\beta$-decay Q-value satisfies the single-wrap substrate identity*

$$
\boxed{\;\;
Q_\beta(n) \;=\; m_e \cdot \lvert q_0^2 - 2 q_0 - 1 \rvert \cdot
              \frac{q_0 + 1}{2\, q_0^{\,3}}
\;\;}
$$

*as an algebraic expression in the substrate. At $q_0 \approx
1.10998$ this evaluates to $0.78365\,\mathrm{MeV}$, agreeing with
CODATA $Q_\beta(n) = 0.78233\,\mathrm{MeV}$ to $+0.168 \%$
($+1.31\,\mathrm{keV}$). The residual is the brane-tower truncation
at $N = 0$ (closed by the tower-summed form, Workplan 2 Phase 2).*

## Derivation

The hadronic energy scale at the single-Planck-tick level
([energy scale](#rem:energy-scale-planck)) is

$$\mathfrak{E}_0^{(N=0)} \;=\; \frac{m_e}{q_0 (q_0 - 1)} \;=\; m_e \cdot c_q^2 \cdot \hbar_q,$$

derived from CAL-1 + CAL-2 alone. Combining with the symbolic NF
difference between the canonical neutron and proton braids
([`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic))

$$\Delta(\mathrm{net}) \;=\; \frac{h_q (h_q - 2)}{2}, \qquad h_q = q - q^{-1},$$

and tracing the single-wrap algebra (see
[`derived_masses.py:49-62`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/derived_masses.py)
for the explicit reduction) gives the closed form above. The
absolute value $\lvert q_0^2 - 2 q_0 - 1 \rvert$ accounts for the
sign convention of the NF difference (neutron above proton in $\beta^-$).
$\square$

## Numerical evaluation at $q_0$

| Quantity | Value |
|---|---:|
| $q_0$ (50-dps pin) | $1.10998\,\ldots$ |
| $m_e$ (CAL-1, CODATA) | $0.510999\,\mathrm{MeV}$ |
| $\lvert q_0^2 - 2 q_0 - 1 \rvert$ | $1.2092\,\ldots$ |
| $(q_0 + 1)/(2 q_0^{\,3})$ | $0.7707\,\ldots$ |
| **$Q_\beta(n)$ substrate prediction** | **$0.78365\,\mathrm{MeV}$** |
| $Q_\beta(n)$ CODATA / PDG 2024 | $0.78233\,\mathrm{MeV}$ |
| Absolute residual | $+1.31\,\mathrm{keV}$ |
| Relative residual | $+0.168 \%$ |

Witness: [`q-beta-substrate-prediction.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/q-beta-substrate-prediction.witness.json).

## Cohomological role: the alt channel

[`prop:three-parameters-wedderburn`](#prop:three-parameters-wedderburn)
identifies $Q_\beta$ as the calibration of the **alternating
channel** of $H_3(R, q)$ — the irrep where every $\sigma_i$ acts
as $-q^{-1}$. This channel controls the antisymmetric / antimatter
sector responsible for $\beta$ decay. The present proposition does
**not** demote CAL-3 to a prediction; it records that the alt-channel
value is *algebraically determined* by the sym channel (via $q_0$)
and the std channel (via $m_e$) up to the brane-tower correction.

**If** the tower-summed form
$\mathfrak{E}_0^{\text{full},\mathrm{Li}_2^q}$ (conjectured in
[`derived_masses.py:28`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/derived_masses.py))
closes the residual to within 1 ppb (Workplan 2 Phase 2), then the
calibration count reduces $3 \to 2$ while preserving the
cohomological 3-channel structure: the alt channel becomes a
*prediction* read off from the sym + std channels.

## Tolerance comparison

| Downstream consumer | MAE budget | Substrate residual fits? |
|---|---:|:---:|
| Production mass-table predictions ($m_n$ via $m_p + Q_\beta + m_e$) | $\sim 4 \%$ | ✓ |
| $\beta$-chain α-cluster derivation ([`c_alpha_from_Q_beta_trace.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/c_alpha_from_Q_beta_trace.py)) | $\sim 4 \%$ | ✓ |
| L2 100× target ($Q_\beta$ row of [`per-observable-100x-status`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/per-observable-100x-status.witness.json)) | $7.8\,\mathrm{ppb}$ | ✗ (needs tower closure) |
| 1 ppb / L1 gate | $1\,\mathrm{ppb}$ | ✗ (needs tower closure) |

Every production consumer tolerates the $+0.168 \%$ residual; only
the precision-targeting dashboards fail it. The closure path is the
existing tower-summation work item, not a new substrate derivation.

## What this proposition does not claim

- It does **not** assert CAL-3 is droppable today.
- It does **not** replace the canonical
  [`cal-3-q-beta.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/cal-3-q-beta.witness.json)
  calibration witness — the substrate prediction is emitted in
  parallel.
- It does **not** propose a fourth calibration input.
- The residual sign ($+1.31 \,\mathrm{keV}$, prediction > CODATA) is
  the same direction as the geometric-tower CAL residual
  ([`calibration-inputs.md`](calibration-inputs.md):72–84
  +1.75 % overshoot), confirming the same physical origin: missing
  high-$N$ tower terms.

## See also

- [`prop:three-parameters-wedderburn`](#prop:three-parameters-wedderburn) — cohomological 3-channel theorem
- [`rem:calibration-inputs`](#rem:calibration-inputs) — current 3-CAL declaration
- [`rem:energy-scale-planck`](#rem:energy-scale-planck) — $\mathfrak{E}_0^{(N=0)}$ derivation
- [`prop:q-zero-complex-extension`](#prop:q-zero-complex-extension) — sibling content block on the complex-q lift
- Companion audit: [`docs/audits/2026-05-24-q-beta-droppability-cohomology.md`](../../../docs/audits/2026-05-24-q-beta-droppability-cohomology.md)
