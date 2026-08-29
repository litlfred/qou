| Quantity                                 | QOU prediction ($q = q_0$) | CODATA 2018          |
| ---------------------------------------- | -------------------------- | -------------------- |
| $q^{-1}$                                 | $0.900901$                 | —                    |
| $[9]_q$                                  | $10.36404$                 | —                    |
| $[10]_q$                                 | $11.89501$                 | —                    |
| $[9]_q \cdot [10]_q$                     | $123.257$                  | —                    |
| Bare $\alpha_{\mathrm{EM}}^{-1}$         | $136.823$                  | —                    |
| $\delta_{\mathrm{CS}}$                   | $0.001551$                 | —                    |
| CS-corrected $\alpha_{\mathrm{EM}}^{-1}$ | $\mathbf{137.036}$         | $137.035999084(21)$  |
| Discrepancy (bare)                       |                            | $-0.155\%$           |
| Discrepancy (corrected)                  |                            | $-2.1\;\mathrm{ppm}$ |

*Superseded snapshot.* The $-2.1\;\mathrm{ppm}$ row is the Chern-Simons tower
resummed with the Gram factor $\kappa$ set to $1$, evaluated at the muon pin
($-2.128\;\mathrm{ppm}$). With the derived Witten $\kappa \approx 1.722$ at the
standing proton pin the residual is $-468\;\mathrm{ppb}$
([Chern-Simons correction](#rem:em-coupling-chern-simons)). The bare row
($136.823$, $-0.155\%$) is unaffected and remains current. The four intermediate
cells have also drifted from the live values ($q^{-1} = 0.9009183$,
$[9]_q = 10.36352$, $[10]_q = 11.89428$, $[9]_q[10]_q = 123.2665$) and are
internally inconsistent, since $10.36404 \times 11.89501 = 123.280$ rather than
the $123.257$ shown; the drift is not a pin difference, as both pins agree to
seven significant figures here. Reproduce with
[`alpha_em_form_comparison_probe.py`](computations/alpha/alpha_em_form_comparison_probe.py).
