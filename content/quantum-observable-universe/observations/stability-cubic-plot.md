At $q = q_0$, the stability cubic ([Diophantine valley](#rem:diophantine-valley))

$$
  t^3 =  2p(1 + ct^2),
  \qquad c = 0.01497, \quad A = t^3
$$

parametrises the valley of stability. The integer lattice points $(p, n) \in \mathbb{N}^2$ on this curve represent the stable nuclei.

See [Table](#tbl:stability-cubic-plot-table-data).

The predicted neutron number $N_{\mathrm{pred}}$ minimizes the convex quadratic $E(p, A)$ ([integer stability](#prop:integer-stability)) at each $p$. The discrepancy $\Delta N = |N_{\mathrm{pred}} - N_{\mathrm{obs}}|$ is zero up to iron, and at most $2$ across the periodic table.

The curve $p = t^3/(2 + 2ct^2)$ bends away from the diagonal $n = p$ as $A$ increases. The Coulomb term $a_C \cdot p^2/A^{1/3}$ penalizes proton-rich nuclei, demanding additional neutrons. Driven entirely by $q_0$, the neutron excess grows from $0\%$ at hydrogen ($p=1, n=0$) to $59\%$ at uranium ($p=92, n=146$).

See the [valley of stability simulator](#sim:valley-stability).
