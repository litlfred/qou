| Quantity                                 | QOU prediction ($q = q_0$, proton pin) | CODATA 2022          |
| ---------------------------------------- | -------------------------------------- | -------------------- |
| $q^{-1}$                                 | $0.900918284$                          | —                    |
| $[9]_q$                                  | $10.3635176$                           | —                    |
| $[10]_q$                                 | $11.8942752$                           | —                    |
| $[9]_q \cdot [10]_q$                     | $123.266530$                           | —                    |
| Bare $\alpha_{\mathrm{EM}}^{-1}$         | $136.8232089$                          | —                    |
| $\delta_{\mathrm{CS}}$                   | $0.00155060213$                        | —                    |
| CS-corrected $\alpha_{\mathrm{EM}}^{-1}$ | $\mathbf{137.035935094}$               | $137.035999177(21)$  |
| Discrepancy (bare)                       |                                        | $-0.15528\%$         |
| Discrepancy (corrected)                  |                                        | $-468\;\mathrm{ppb}$ |

*Refreshed 2026-08-29 to the proton pin and CODATA 2022.* Every cell is recomputed
from [`alpha_em_form_comparison_probe.py`](../../../computations/alpha/alpha_em_form_comparison_probe.py)
and the canonical `alpha_em_inv_derived`, and the table is now internally
consistent: $10.3635176 \times 11.8942752 = 123.266530$. The previous cells were
drifted and did **not** multiply out — they showed $[9]_q[10]_q = 123.257$ against
their own product of $123.280$ — and the correction row read
$-2.1\;\mathrm{ppm}$, which is the Chern-Simons tower resummed with the Gram
factor $\kappa$ set to $1$ (no Gram correction at all) at the **muon** pin
($-2.128\;\mathrm{ppm}$). The row above uses the derived Witten
$\kappa \approx 1.7216$ with the tower resummed in closed form.

**The correction remains conjectural.** Only the bare row is derived. The
Chern-Simons correction is a conjecture whose Gram constant $\kappa$ is carried
as an unproved Lean `sorry`; exact closure at this pin would need
$\kappa \approx 1.9153$, which differs from the Witten value by $11.2\%$
([Chern-Simons correction](#rem:em-coupling-chern-simons),
[open problems](#rem:alpha-em-derivation-open-problems)).
