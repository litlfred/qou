| Quantity                                  | Value                              |
| ----------------------------------------- | ---------------------------------- |
| Base: $q \cdot [9]_q \cdot [10]_q$        | ${{ qou.computations.meson-em-sinh-closed-form.data.cs_tower_order_sweep.0.alpha_em_inv | precision: 10 }}$ |
| $\mathrm{CS}(T_{2,9})$                    | $\pi^2 \cdot 10/9 \approx 10.966$  |
| $\mathrm{CS}(T_{3,5})$                    | $\pi^2 \cdot 16/15 \approx 10.528$ |
| $\hbar_q^2$                               | $0.00981719$                       |
| $[2]_q / 2$                               | $1.005448$                         |
| $\delta_{\mathrm{CS}}$                    | $0.00155060$                       |
| $\kappa$ (Witten 1988)                    | $1.7216$                           |
| $\alpha^{-1}_{\mathrm{CS}}$ (all orders)  | $\mathbf{{{ qou.computations.meson-em-sinh-closed-form.data.alpha_em_inv_derived_exact | precision: 10 }}}$ |
| CS residual vs.\ CODATA 2022              | $-468\;\mathrm{ppb}$               |
| Additive Bring zero-mode ($+2/(3\pi)$)    | ${{ qou.computations.alpha-em-form-ladder.data.ladder.proton.additive | precision: 10 }}$ (${{ qou.computations.alpha-em-form-ladder.data.ladder.proton.additive_resid_ppb | precision: 4 }}\;\mathrm{ppb}$) |
| Form A quadratic ($+\alpha H$, $H = [2]_q/(8\pi)$) | ${{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_A_alpha_inv | precision: 13 }}$ ($+{{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_A_no_schwinger_ppb | precision: 4 }}\;\mathrm{ppb}$) |
| Form B Bring–Schwinger cubic ($+\alpha H(1 - h^2\alpha)$) | $\mathbf{{{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_B_alpha_inv | precision: 13 }}}$ ($\mathbf{{{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_B_schwinger_ppb | precision: 4 }}\;\mathrm{ppb}}$, ${{ qou.computations.alpha-em-schwinger-ladder.data.ladder_proton.form_B_sigma | precision: 3 }}\,\sigma_\alpha$) |
| CODATA 2022                               | ${{ qou.computations.alpha-em-schwinger-ladder.data.codata_reference.alpha_inv | precision: 12 }}(21)$ |

All rows are evaluated at the **proton** pin $q_0$, the production default
([local aether parameter](#prop:local-substrate-q)), and compared against the
**CODATA-2022** adjustment.

The $\alpha^{-1}_{\mathrm{CS}}$ row is the Chern--Simons tower summed to **all
orders**. The tower is geometric with ratio $\delta_{\mathrm{CS}}\kappa
\approx 2.7\times 10^{-3}$, so it closes in the form
$1 + \delta_{\mathrm{CS}}/(1 - \delta_{\mathrm{CS}}\kappa)$ and carries no
truncation order to choose.

*Superseded values, recorded so the change is legible.* This table previously
read $\alpha^{-1}_{\mathrm{CS}} = 137.035944$, CODATA 2018, residual
$399$ ppb. Those figures are the order-$\delta_{\mathrm{CS}}^2$ truncation
evaluated at the **muon** pin against the superseded adjustment. Both moves
are small and they act in the same direction:

| change | effect on the residual |
| ------ | ---------------------- |
| order-$\delta_{\mathrm{CS}}^2$ $\to$ all orders | $11.06$ ppb (at either pin) |
| muon pin $\to$ proton pin | $79.17$ ppb (for either form) |
