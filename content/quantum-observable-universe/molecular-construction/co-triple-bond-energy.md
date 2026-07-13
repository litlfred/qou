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

*The computation requires assembling the 42-strand transfer matrix chain. We perform this iteratively, reducing to NF at each step. The witness file `co-molecular-binding.witness.json` records:*
- *$\Phi_1$ for isolated C and O atoms.*
- *$\Phi_1$ for the CO molecular braid at each bond order $k = 1, 2, 3$.*
- *The LP dual shadow prices $y_1, y_2, y_3$.*
- *Comparison with observed $D_0 \approx :val[observed_D0_CO_eV]{precision=4, witness=computations/co-bond-order-active-set.witness.json} \;\mathrm{eV}$.*
