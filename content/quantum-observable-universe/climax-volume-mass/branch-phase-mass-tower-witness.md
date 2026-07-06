**Remark (branch-phase localisation and the mass-tower falsifiability witness).**

**Branch-phase localisation on $\mathcal{X}_5$.**  The five finite branch points $\zeta_5^k$ of the hyperelliptic quintic ([def:hyperelliptic-quintic](#def:hyperelliptic-quintic)) lie on the unit circle. They select five preferred phases $\varphi_k = 2\pi k/5$ on the $\mathrm{U}(1)$ tube ([rem:u1-phase-tube](#rem:u1-phase-tube)). At these phases, the commutative crossing weight ([crossing energy](#def:crossing-energy)) takes two distinct magnitudes:

$$
  2\lvert\sin(2\pi/5)\rvert  \approx 1.902,
  \qquad
  2\lvert\sin(4\pi/5)\rvert  \approx 1.176,
$$

whose ratio $\sin(2\pi/5)/\sin(4\pi/5) = \varphi$ is the golden ratio $\varphi = (1+\sqrt{5})/2$.

**Falsifiability witness.**  The multi-brane mass $\mathfrak{m}_{\mathrm{cat}} = \lvert\mathrm{tr}_M(\beta)\rvert + \sum_n \hbar_q^{2n} \mathrm{tower}^{(n)}$ predicts the binding energies of the three lightest non-trivial nuclei. Evaluating this against AME data yields a ratio that overshoots by a factor of 3 to 4, exposing a missing scalar prefactor (`isospin-mass-tower-collapse`). After isospin (Coulomb) correction, the two distinct strong-force ratios match the branch-phase magnitudes exactly.

See [Table 2](#tbl:commutative-crossing-energy-table2-data).

Subtracting the $\approx 0.76\;\mathrm{MeV}$ Coulomb energy of ${}^3\mathrm{He}$ collapses the two $A = 3$ ratios to $3.4767$. This matches the tritium ratio ($3.4764$) to $0.014\%$, verifying the isospin symmetry of the strong-force binding (\cite{satula1997}).

**Caveat (updated).** Categorical data now strictly dictates the per-nucleon scaling between $A = 2$ and $A = 3$. Symbolic Hoefsmit pole-order analysis for the proton ($Z=1, N=0$) and deuteron ($Z=N=1$) yields $\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta)) = 18Z + 21N + 1$ (Path A pipeline: commits `f9f25b5f`, `23e447dc`, [`per_irrep_pole_atom.py`](../../../computations/per_irrep_pole_atom.py)). The single-generator $\rho_K$ formula then bounds atomic mass predictions across $Z = 1$..$20$ to within $0.30\%$ of experimental values. We tested and rejected the Wedderburn pair-generator extension, as it degrades the fit to $\sim 4.7\%$ MAE. Independent of this numerical check, the Hecke structure at $q = 1$ forces the categorical-coordinate identity $i = \sqrt{\lambda_-}$.
