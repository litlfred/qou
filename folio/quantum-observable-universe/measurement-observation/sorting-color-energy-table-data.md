Across the six elements of $S_3$, the colour energy tracks the inversion count exactly, $E_{\mathrm{colour}} = \mathrm{inv}(\pi)\,(q + q^{-1})$: each transposition needed to sort $\pi$ contributes one crossing $\sigma_i$ and one unit $q + q^{-1}$, so $E_{\mathrm{colour}}$ grows linearly in the number of swaps.

| Permutation $\pi$ | $\mathrm{inv}(\pi)$ | Crossings | $E_{\mathrm{colour}}$ |
|:-:|:-:|:-:|:-:|
| $(1,2,3)$ sorted | $0$ | $0$ | $0$ |
| $(1,3,2)$ one swap | $1$ | $\sigma_2$ | $q + q^{-1}$ |
| $(2,1,3)$ one swap | $1$ | $\sigma_1$ | $q + q^{-1}$ |
| $(2,3,1)$ two swaps | $2$ | $\sigma_1 \sigma_2$ | $2(q + q^{-1})$ |
| $(3,1,2)$ two swaps | $2$ | $\sigma_2 \sigma_1$ | $2(q + q^{-1})$ |
| $(3,2,1)$ reverse | $3$ | $\sigma_1 \sigma_2 \sigma_1$ | $3(q + q^{-1})$ |
