The $CO$ bond energy decomposes into three Wedderburn channels, mirroring the atomic mass formula:

$$
  \mathfrak{E}_{\mathrm{bind}}(CO) = \alpha \sum_{i \in \mathrm{bonds}} \ln\lvert \hat{V}_i^{\mathrm{full}} \rvert
$$

where the sum runs over all 6 covalent-channel generators (3 bonds $\times$ 2 crossings each). The full traced volume incorporates the symmetric, standard, and alternating representations:

$$
  \hat{V}_i^{\mathrm{full}} = w_{\mathrm{sym}} \lambda_i^{\mathrm{sym}} + w_{\mathrm{std}} \hat{V}_i^{\mathrm{std}} + w_{\mathrm{alt}} \lambda_i^{\mathrm{alt}}
$$

For the triple bond, the $\sigma$ bond generators derive from the head-on overlap of $2s/2p_z$ orbitals, contributing the largest $|\hat{V}|$. The $\pi$ bond generators derive from the lateral overlap of $2p_x$ and $2p_y$ orbitals, contributing a smaller $|\hat{V}|$.

We compute the binding energy by assembling the 42-strand transfer matrix chain. The iterative constructor makes this feasible by applying Gröbner--Shirshov reduction to normal form at each step. We record $\Phi_1$ for the isolated atoms and for the $CO$ molecular braid at each bond order $k = 1, 2, 3$, alongside the LP dual shadow prices $y_1, y_2, y_3$. We compare the result with the observed $D_0 \approx :val[observed_D0_CO_eV]{precision=4, witness=computations/co-bond-order-active-set.witness.json} \;\mathrm{eV}$.

