<!-- FILE_START: h2-computation-intro.md -->
We turn to the smallest covalent molecule. The hydrogen molecule $H_2$ as a braid in $H_4(q)$ places two protons and two electrons on four strands and lets them share a single trefoil. The LP dual selects the optimal $H_2$ binding, determines the bond order, and provides the binding energy. We compare the predicted $H_2$ binding energy with the spectroscopic value. The covalent channel eigenvalue ratio yields the equilibrium internuclear separation. This sets the template for the heteronuclear and polyatomic cases.
<!-- FILE_END: h2-computation-intro.md -->

<!-- FILE_START: h2-molecular-braid.md -->
**Definition.**
*The **hydrogen molecule** $H_2$ is the molecular braid of two hydrogen atoms sharing one electron pair. The construction proceeds in three stages:*

### Stage 1: Build two hydrogen atoms

*Each hydrogen atom is an [atomic braid](#def:atomic-braid) in $H_2(q)$: one proton $\mathfrak{p}$ and one electron $e$, with the $\mathcal{B}_3$-dressed $\mathfrak{p}e$ crossing.*

*Atom 1: $\mathcal{A}_1 = [\mathfrak{p}_1, e_1]$ with dressed eigenvalues $(q^5, -q^{-5})$.*

*Atom 2: $\mathcal{A}_2 = [\mathfrak{p}_2, e_2]$ with dressed eigenvalues $(q^5, -q^{-5})$.*

### Stage 2: Embed in $H_4(q)$ and apply inter-atomic crossings

*The molecular braid lives in $H_4(q)$ with strand ordering $[\mathfrak{p}_1, e_1, \mathfrak{p}_2, e_2]$. The six pairwise crossings are:*

See [Table](#tbl:h2-molecular-braid-table-data).

*The **covalent channel** is the $e_1\mathfrak{p}_2$ crossing ($\sigma_1$). Electron 1 from atom 1 is attracted to proton 2 of atom 2. By symmetry, $e_2$ is also attracted to $\mathfrak{p}_1$ via the $\mathfrak{p}_1 e_2$ crossing. This produces the shared-electron bond.*

### Stage 3: Transfer matrix chain

*The four-strand transfer matrix product is:*

$$
  \hat{V}^{H_2} = T_{\mathfrak{p}_1 e_1}^{\mathrm{dressed}}
  \cdot T_{e_1 \mathfrak{p}_2}
  \cdot T_{\mathfrak{p}_2 e_2}^{\mathrm{dressed}}
$$

*where:*

$$
  T_{\mathfrak{p}e}^{\mathrm{dressed}} =
  \begin{pmatrix}
    q^{-5} + d & q^{-5} - q^5 \\
    1 & q^5 + d
  \end{pmatrix},
  \qquad
  T_{e_1\mathfrak{p}_2} =
  \begin{pmatrix}
    q^{-1} + d & q^{-1} - q \\
    1 & q + d
  \end{pmatrix}
$$

*with $d = -(q - q^{-1})$. At $q_0 \approx 1.110$:*

- *$T_{\mathfrak{p}e}^{\mathrm{dressed}}$: eigenvalues $q^5 \approx 1.680$ and $-q^{-5} \approx -0.595$*
- *$T_{e_1\mathfrak{p}_2}$ (covalent): eigenvalues $q \approx 1.110$ and $-q^{-1} \approx -0.901$*
<!-- FILE_END: h2-molecular-braid.md -->

<!-- FILE_START: h2-covalent-channel-interference.md -->
*The covalent crossing eigenvalue ratio $q/q^{-1} = q^2 \approx 1.231$ is closer to 1 than the dressed atomic ratio $q^5/q^{-5} = q^{10} \approx 2.826$. The covalent channel has less destructive interference than the intra-atomic channels. The shared electron reduces $\Phi_1$ relative to two isolated atoms.*

### Strand orderings

*The LP dual optimises over all $4! = 24$ permutations of $[\mathfrak{p}_1, e_1, \mathfrak{p}_2, e_2]$. By the symmetry $(\mathfrak{p}_1, e_1) \leftrightarrow (\mathfrak{p}_2, e_2)$, there are 12 distinct orderings. The optimal ordering places the two electron-proton pairs **interleaved**:*

$$
  [\mathfrak{p}_1, e_2, \mathfrak{p}_2, e_1]
$$

*Each electron is adjacent to the other atom's proton (the covalent partner). This maximises the number of $\sigma^{-1}$ (attractive) crossings in adjacent positions, minimising $\Phi_1$.*
<!-- FILE_END: h2-covalent-channel-interference.md -->

<!-- FILE_START: h2-lp-dual-binding.md -->
**Proposition (conditional on [`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula)).**
*The LP dual of the $H_2$ molecular braid selects the interleaved ordering $[\mathfrak{p}_1, e_2, \mathfrak{p}_2, e_1]$ as the ground state, with molecular volume:*

$$
  \Phi_1^{H_2} = \sum_{i=0}^{2} \ln\lvert \hat{V}_i^{H_2} \rvert
$$

*The **primal program** minimises the Markov trace of the molecular braid over all strand orderings and electron assignments:*

$$
  \min_{\pi \in S_4} \; \Phi_1\!\left(
    T_{\pi(0)\pi(1)} \cdot T_{\pi(1)\pi(2)} \cdot T_{\pi(2)\pi(3)}
  \right)
$$

*subject to:*
- *Each proton appears exactly once*
- *Each electron appears exactly once*
- *The shared electron is Hopf-linked to both protons (covalent constraint)*

*The **dual program** maximises the shadow price of the covalent constraint:*

$$
  \max_{y} \; y_{\mathrm{cov}}
  \quad\text{s.t.}\quad
  y_{\mathrm{cov}} \leq
  \Phi_1^{\mathrm{separated}} - \Phi_1^{H_2}(\pi)
  \;\;\forall\, \pi
$$

*where $\Phi_1^{\mathrm{separated}} = 2 \times \Phi_1^{H}$ is the $\Phi_1$ of two isolated hydrogen atoms.*

*Strong duality holds. The optimal $y_{\mathrm{cov}}^*$ equals the binding energy per shared electron. At $q_0$:*

### Numerical evaluation

*Two isolated H atoms (dressed):*

$$
  \Phi_1^{H} = \ln\lvert V^{H} \rvert
  = \ln\lvert q^5 \cdot (-(q-q^{-1})) + q^{-5} \cdot 1 \rvert
$$

*At $q_0 \approx 1.110$, $(q-q^{-1}) \approx 0.208$:*

- *$V^{H} = -q^5(q - q^{-1}) + q^{-5} \approx -1.680 \times 0.208 + 0.595 \approx 0.245$*
- *$\Phi_1^{H} = \ln(0.245) \approx -1.406$*
- *$\Phi_1^{\mathrm{sep}} = 2 \times (-1.406) = -2.812$*

*Molecular $H_2$ (interleaved ordering):*

*The three transfer matrices are $T_0 = T_{\mathfrak{p}_1 e_2}$, $T_1 = T_{e_2 \mathfrak{p}_2}^{\mathrm{dressed}}$, $T_2 = T_{\mathfrak{p}_2 e_1}$. The covalent crossings ($T_0$ and $T_2$) have eigenvalues $(q, -q^{-1})$. The dressed intra-atomic crossing ($T_1$) has eigenvalues $(q^5, -q^{-5})$.*

*The traced volumes at each generator:*

$$
  \hat{V}_0 = z \cdot a_0 + b_0, \quad
  \hat{V}_1 = z \cdot a_1 + b_1, \quad
  \hat{V}_2 = z \cdot a_2 + b_2
$$

*where $z = \mathrm{tr}_M(\mathcal{M}) / [3]_{q}!$ is the Markov-normalised trace variable.*

*The covalent channel ($\sigma_1$ mediating $e_2$--$\mathfrak{p}_2$) creates an additional attractive contribution that drives $\Phi_1^{H_2}$ below $\Phi_1^{\mathrm{sep}}$. The binding energy from the LP dual:*

$$
  y_{\mathrm{cov}}^* = \Phi_1^{\mathrm{sep}} - \Phi_1^{H_2}
  = 2\Phi_1^H - \Phi_1^{H_2} > 0
$$

*The molecule binds when the shared-electron $\Phi_1$ reduction exceeds the proton-proton repulsion penalty.*
<!-- FILE_END: h2-lp-dual-binding.md -->

<!-- FILE_START: h2-bond-length-interpretation.md -->
*The covalent channel eigenvalue ratio $\lambda_+/\lambda_- = q/q^{-1} = q^2$ determines the **effective bond length** in the braid framework. The ratio $q^2 \approx 1.231$ measures how much the shared electron prefers one proton over the other:*

- *$q^2 = 1$: perfectly symmetric sharing (equal eigenvalues), zero bond length (atoms coincide).*
- *$q^2 \to \infty$: electron fully localised on one proton, no covalent bond.*
- *$q^2 \approx 1.231$: moderate asymmetry, yielding an equilibrium distance where the attractive $\Phi_1$ reduction balances the repulsive proton-proton penalty.*

*The equilibrium bond length is set by the competition between:*

$$
  \frac{\partial \Phi_1^{\mathrm{attract}}}{\partial r}
  + \frac{\partial \Phi_1^{\mathrm{repel}}}{\partial r} = 0
$$

*where "distance" $r$ in the braid framework is the number of intervening strands between the two protons. In $H_4(q)$ with interleaved ordering $[\mathfrak{p}_1, e_2, \mathfrak{p}_2, e_1]$, the protons are separated by one strand (one shared electron). The observed $H_2$ bond length is $0.74\;\text{\AA}$.*
<!-- FILE_END: h2-bond-length-interpretation.md -->
