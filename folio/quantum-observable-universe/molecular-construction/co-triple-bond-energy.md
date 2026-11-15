*The CO bond energy decomposes into three Wedderburn channels:*

$$
  \mathfrak{E}_{\mathrm{bind}}(CO) = \alpha \sum_{i \in \mathrm{bonds}}
  \ln\lvert \hat{V}_i^{\mathrm{full}} \rvert
$$

*where the sum runs over all 6 covalent-channel generators (3 bonds $\times$ 2 crossings each). The full traced volume includes symmetric, standard, and alternating representations:*

$$
  \hat{V}_i^{\mathrm{full}} =
  w_{\mathrm{sym}} \lambda_i^{\mathrm{sym}} +
  w_{\mathrm{std}} \hat{V}_i^{\mathrm{std}} +
  w_{\mathrm{alt}} \lambda_i^{\mathrm{alt}}
$$

*For the triple bond:*
- *$\sigma$ bond generators: eigenvalue products from the head-on overlap of $2s/2p_z$ orbitals.*
- *$\pi$ bond generators: eigenvalue products from lateral overlap of $2p_x$ and $2p_y$ orbitals.*
- *The $\sigma$ bond contributes the largest $|\hat{V}|$ (strong overlap). The $\pi$ bonds contribute smaller $|\hat{V}|$ (weaker lateral overlap).*

> **Provenance and scope (2026-08-25).** The witness cited below,
> `co-molecular-binding.witness.json`, is absent from the tree — it was added
> 2026-04-13 in commit `a3e8c2c82d` under `folio-assistant/computations/` and
> left with the platform code in the miga migration. Recovered and read
> ([analysis](https://github.com/litlfred/qou/blob/main/docs/audits/2026-08-25-atom-mass-complete-wedderburn-witness-recovered.md)), it does not support the surrounding text:
>
> - Its energy scale is **fitted**. `calibration_factor = 0.23879110765149733`
>   is exactly $4.478 / 18.753$, the ratio that makes the uncalibrated result
>   equal $\mathrm{H}_2$'s *measured* bond energy — a fourth calibration, on a
>   molecular observable, outside CAL-1/2/3. The owner directive of 2026-08-25
>   is **no fitting**, so the resulting number is not admissible as a
>   parameter-free prediction.
> - Its three bonds are **not differentiated**. The text below says the
>   $\sigma$ bond contributes the largest $\lvert\hat{V}\rvert$ and the
>   $\pi$ bonds smaller; in the witness all three carry the identical
>   $\Delta\Phi_1 = 0.687012518457808$, and the $k=3$ total is exactly three
>   times the $k=1$ value.
> - It records **no LP duals**. The list below claims shadow prices
>   $y_1, y_2, y_3$; `y0_star`, `y_star`, `active_set`, `primal_obj`,
>   `dual_obj` and `duality_gap` are all absent.
>
> Its own surviving assertion is "CO triple bond within 25 % of observed"
> against $D_0(\mathrm{CO}) = 11.09$ eV; the computed $13.434$ eV is
> $+21.1\%$ — inside a loose bar, reached via a scale fitted on a different
> molecule. Do not cite this bond energy as derived.

*The computation requires assembling the 42-strand transfer matrix chain. We perform this iteratively, reducing to NF at each step. The witness file `co-molecular-binding.witness.json` records:*
- *$\Phi_1$ for isolated C and O atoms.*
- *$\Phi_1$ for the CO molecular braid at each bond order $k = 1, 2, 3$.*
- *The LP dual shadow prices $y_1, y_2, y_3$.*
- *Comparison with observed $D_0 \approx {{ qou.computations.co-bond-order-active-set.data.observed_D0_CO_eV | precision: 4 }}\;\text{eV} \;\mathrm{eV}$.*
