At $q = q_0$, the stability cubic
([Diophantine valley](#rem:diophantine-valley))

$$
  t^3 =  2p(1 + ct^2),
  \qquad c = 0.01497, \quad A = t^3
$$

parametrises the valley of stability as a rational curve in the
$(p, n)$-plane, where $Z$ is the proton number (atomic number) and $N = A - Z$
(neutron number).  The lattice points
$(p, n) \in \mathbb{N}^2$ on this curve are the stable nuclei.

The following table lists the lattice points and their
corresponding atoms, compared with observed stable isotopes
(CODATA/AME2020):

See [Table](#tbl:stability-cubic-plot-table-data).

The predicted neutron number $N_{\mathrm{pred}}$ is the exact
integer minimiser of the convex quadratic $E(p, A)$
([integer stability](#prop:integer-stability)) at each $p$.
The discrepancy $\Delta N = |N_{\mathrm{pred}} - N_{\mathrm{obs}}|$
is at most $2$ across the entire periodic table, with
$\Delta N = 0$ for all elements up to iron.

The curve $p = t^3/(2 + 2ct^2)$ bends away from the diagonal
$n = p$ as $A$ increases: the Coulomb term $a_C \cdot p^2/A^{1/3}$
penalises proton-rich nuclei, requiring additional neutrons for
stability.  At $p = 1$ (hydrogen), $n = 0$; at $p = 92$ (uranium),
$n = 146$ — the neutron excess grows from $0\%$ to $59\%$, driven
entirely by the single parameter $q_0$.

A plot of this curve in the $(p, n)$-plane, with the lattice
points marked and labeled by element, is shown in the
[valley of stability simulator](#sim:valley-stability).
