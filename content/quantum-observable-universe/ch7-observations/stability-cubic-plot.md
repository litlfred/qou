At $q = 1.110$, the stability cubic
([Diophantine valley](#rem:diophantine-valley))

$$
  t^3 \;=\; 2Q\,(1 + c\,t^2),
  \qquad c = 0.01497, \quad A = t^3
$$

parametrises the valley of stability as a rational curve in the
$(Q, N)$-plane, where $Q = p$ (proton number) and $N = A - Q$
(neutron number).  The lattice points
$(Q, N) \in \mathbb{N}^2$ on this curve are the stable nuclei.

The following table lists the lattice points and their
corresponding atoms, compared with observed stable isotopes
(CODATA/AME2020):

| $Q$ | $N_{\mathrm{pred}}$ | $N_{\mathrm{obs}}$ | Atom | $N/Q$ | $\Delta N$ |
|----:|----:|----:|--------|------:|---:|
| 1 | 0 | 0 | H | 0.00 | 0 |
| 2 | 2 | 2 | He | 1.00 | 0 |
| 6 | 6 | 6 | C | 1.00 | 0 |
| 8 | 8 | 8 | O | 1.00 | 0 |
| 14 | 14 | 14 | Si | 1.00 | 0 |
| 20 | 20 | 20 | Ca | 1.00 | 0 |
| 26 | 30 | 30 | Fe | 1.15 | 0 |
| 28 | 30 | 30 | Ni | 1.07 | 0 |
| 36 | 48 | 48 | Kr | 1.33 | 0 |
| 50 | 69 | 70 | Sn | 1.40 | 1 |
| 56 | 82 | 82 | Ba | 1.46 | 0 |
| 74 | 109 | 110 | W | 1.49 | 1 |
| 82 | 125 | 126 | Pb | 1.54 | 1 |
| 92 | 144 | 146 | U | 1.59 | 2 |

The predicted neutron number $N_{\mathrm{pred}}$ is the exact
integer minimiser of the convex quadratic $E(Q, A)$
([integer stability](#prop:integer-stability)) at each $Q$.
The discrepancy $\Delta N = |N_{\mathrm{pred}} - N_{\mathrm{obs}}|$
is at most $2$ across the entire periodic table, with
$\Delta N = 0$ for all elements up to iron.

The curve $Q = t^3/(2 + 2ct^2)$ bends away from the diagonal
$N = Q$ as $A$ increases: the Coulomb term $a_C \cdot Q^2/A^{1/3}$
penalises proton-rich nuclei, requiring additional neutrons for
stability.  At $Q = 1$ (hydrogen), $N = 0$; at $Q = 92$ (uranium),
$N = 146$ — the neutron excess grows from $0\%$ to $59\%$, driven
entirely by the single parameter $q = 1.110$.

A plot of this curve in the $(Q, N)$-plane, with the lattice
points marked and labeled by element, is shown in the
[valley of stability simulator](#sim:valley-stability).
