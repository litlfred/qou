**Remark (branch-phase localisation and the mass-tower falsifiability witness).**

**Branch-phase localisation on $\mathcal{X}_5$.** The five finite branch points $\zeta_5^k$ of the hyperelliptic quintic ([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)) lie on the unit circle. They pick out five preferred phase values $\varphi_k = 2\pi k/5$ on the $\mathrm{U}(1)$ tube ([rem:u1-phase-tube](#rem:u1-phase-tube)). At these phases, the commutative crossing weight ([crossing energy](#def:crossing-energy)) takes only two distinct magnitudes:

$$
  2\lvert\sin(2\pi/5)\rvert  \approx 1.902,
  \qquad
  2\lvert\sin(4\pi/5)\rvert  \approx 1.176.
$$

The golden-ratio identity $\sin(2\pi/5)/\sin(4\pi/5) = \varphi$ relates them, where $\varphi = (1+\sqrt{5})/2$.

**Falsifiability witness.** The computation `isospin-mass-tower-collapse` evaluates the multi-brane mass $\mathfrak{m}_{\mathrm{cat}} = \lvert\mathrm{tr}_M(\beta)\rvert + \sum_n \hbar_q^{2n} \mathrm{tower}^{(n)}$ against AME binding for the three lightest non-trivial nuclei. The derived/observed ratio overshoots by a factor of $3$ to $4$, indicating a missing scalar prefactor. After isospin (Coulomb) correction, the two distinct strong-force ratios match the two branch-phase magnitudes:

See [Table 2](#tbl:commutative-crossing-energy-table2-data).

Removing the $\approx 0.76\;\mathrm{MeV}$ Coulomb energy of ${}^3\mathrm{He}$ collapses the two $A = 3$ ratios to $3.4767$. This matches tritium ($3.4764$) to $0.0086\%$, consistent with the isospin symmetry of strong-force binding (Wigner-energy convention, \cite{satula1997}).

**Caveat.** We have categorically derived the structural form of the per-nucleon scaling between $A = 2$ and $A = 3$. A symbolic computation verifies $\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta)) = 18Z + 21N + 1$ via symbolic Hoefsmit pole-order analysis for the proton ($Z=1, N=0$) and deuteron ($Z=N=1$). Predictions match experimental atomic masses to $\leq 0.30\%$ across $Z = 1 \dots 20$ using the single-generator $\rho_K$ formula. We tested and **rejected** the Wedderburn pair-generator extension (it worsens the fit to $\sim 4.7\%$ MAE). The Hecke structure at $q = 1$ forces the categorical-coordinate identification $i = \sqrt{\lambda_-}$; it does not rely on this numerical confirmation.
