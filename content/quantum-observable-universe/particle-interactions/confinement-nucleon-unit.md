The confinement LP proof and the Gram indefiniteness theorem jointly justify treating nucleons as atomic units in the transfer matrix chain. The proof is purely algebraic. We use LP duality, Gram matrix eigenstructure, and braid group realizability. No physics assumptions enter.

**Statement.** The inter-nucleon transfer matrix uses nucleon strand types $p, n$ with crossing coefficients $pp: (1,0)$, $nn: (1,-\mathrm{HA})$, $pn: (1,-\mathrm{HA}/2)$, without resolving the internal quark structure. This is exact because:

1. **LP confinement** proves that the Borromean operator $B_3 = (\sigma_0\sigma_1^{-1})^3$ traps the quark NF coefficients in the Frobenius cone $G\vec{x} \geq 0$. No quark subset can unbind.
2. **Gram indefiniteness** ($\det G < 0$) shows that energy minimization has a global minimum at $\mathrm{tr}_M = 0$. Confinement at $\mathrm{tr}_M \approx 1$ is topological, forced by the braid group realizability constraint $B_3$.
3. **Consequence for the transfer matrix:** Since quarks cannot unbind, the nucleon's internal braid structure acts as a rigid unit. The inter-nucleon crossing between nucleon $i$ and nucleon $j$ depends only on the nucleon types, not on the quark arrangement. The transfer matrix Skein polynomial $P = \prod_i \hat{V}_i$ captures the full inter-nucleon physics at the nucleon level.
4. **Error bound:** The nucleon-as-unit approach introduces no error for the transfer matrix. Quark-level effects manifest only through the nucleon NF coefficients, which we precompute once via `build_nucleon_nf`.
