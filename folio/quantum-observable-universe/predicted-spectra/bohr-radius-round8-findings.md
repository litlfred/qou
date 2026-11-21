**Remark (Hecke-algebraic structure).**

The Hecke-algebraic formulation of the Bohr radius possesses three structural properties.

#### Additive decomposition in $\{h_b, h_d\}$

Recomputing the $H_2$ binding pipeline at the optimal ordering $[p_1, e_2, e_1, p_2]$ yields:

$$
\begin{aligned}
  V_H &= z + h_b - h_d, \\
  V[1] &= 1 + 2 z h_b - z h_d, \\
  V[2] &= z - h_b.
\end{aligned}
$$

The bare skein parameter is $h_b = q - q^{-1}$. The K-shell-dressed skein parameter is $h_d = q^5 - q^{-5}$. The Markov parameter is $z = q^3/(q^2+1)$ (convention D, canonical since the ruling of 2026-08-15). The transfer-matrix chain generates multiplicative cross-terms $h_b \cdot h_d$. These cancel exactly.

**Convention comparison ($z_D$ versus $z_C$).** The ratio cancellation immediately above depends only on $h_b$ and $h_d$ and is independent of $z$. The auxiliary numerical tables below were evaluated at the Convention-C parameter $z_C = \sqrt{q}/(q+1) \approx 0.4993203$ rather than the canonical Convention-D parameter $z_D = q^3/(q^2+1) \approx 0.6126880$ at $q_0 \approx 1.1099786$.

The kinetic ($h_d$) and Coulomb ($h_b$) contributions to $V_i$ decouple linearly. This additive decomposition relies on the permutation structure of the optimal ordering.

#### Shell ratios and the Bohr $1/n^2$ scaling

The categorical spectral-gap ratio $\Delta_{\mathrm{kin}}(k)/\Delta_{\mathrm{Coul}} = (4k+2)/2 = 2k+1$ depends only on the shell and the Hecke structure. Inverting yields:

$$
  (2k+1)^{-2} \in \left\{1, \tfrac{1}{9}, \tfrac{1}{25}, \tfrac{1}{49}, \dots\right\}
  \quad\text{for}\quad k \in \{0, 1, 2, 3, \dots\}.
$$

Identifying $n = 2k+1$ exactly reproduces the Bohr $1/n^2$ energy-level spacing. The dressing-power $2k+1$ plays the role of the principal quantum number.

The relative shell spacing $E_n / E_1 = 1/n^2$ emerges from the Hecke spectral-gap analysis without transport. This determines only ratios, not the absolute $\alpha_{EM}^{2}$ scale.

#### Curvature rank and covalent bonds

The Grothendieck-Brieskorn curvature-rank stratification gives $y_{\mathrm{cov}}^{*} \sim \alpha_{EM}^{(\text{rank})}$. The rank counts independent electromagnetic force-carrier insertions. A covalent bond shares two electrons, mediated by one exchange. This gives rank 2. It produces the $\alpha^{2}$ scaling.

Atomic spectra (single electron) also scale as $\alpha^{2}$. The rank interpretation predicts the covalent scale. It does not explain the atomic scale. The atomic scale still requires the virial-balance argument of [Categorical Bohr radius $a_0^{\mathrm{cat}} = \hbar/(m_e c\,\alpha_{EM})$](#conj:bohr-radius-categorical).

#### Transport dependence

The Hecke structure determines the relative shell spacing and the kinetic/Coulomb additive decomposition. The absolute scale $E_h = m_e c^2 \alpha^2$ remains transported. Fixing $m_e c^2$ as the mass-energy unit and determining the power of $\alpha$ requires extending the curvature-rank mapping to handle atomic binding.
