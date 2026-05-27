**Proposition (conditional on [`prop:q-integer-mass-formula`](#prop:q-integer-mass-formula)).**
*The LP dual of the $CO$ molecular braid selects the triple-bond
configuration (3 shared pairs) as optimal over single ($k=1$) and
double ($k=2$) bonds.*

*The binding LP for $CO$ is:*

$$
  \min_{k, \pi} \; \Phi_1\bigl(\mathcal{M}(C, O; k\text{-bond}, \pi)\bigr)
$$

*over bond order $k \in \{1, 2, 3\}$ and strand ordering $\pi$.
The dual:*

$$
  \max_{y_1, y_2, y_3} \; \sum_{k} k \cdot y_k
  \quad\text{s.t.}\quad
  y_k \leq \Delta\Phi_1(k) - \Delta\Phi_1(k-1)
  \;\;\forall\, k
$$

*where $\Delta\Phi_1(k) = \Phi_1^{\mathrm{sep}} - \Phi_1^{CO}(k)$
is the $\Phi_1$ reduction from $k$ shared pairs.*

*The marginal $\Phi_1$ reduction per additional bond:*

| Bond | $k$ | Additional crossings | $\Delta\Phi_1(k) - \Delta\Phi_1(k-1)$ |
|:-----|:----|:---------------------|:--------------------------------------|
| $\sigma$ | 1 | 2 attractive $\sigma^{-1}$ | Large positive (first bond, biggest gain) |
| $\pi_1$ | 2 | 2 attractive $\sigma^{-1}$, less $e$-$e$ repulsion penalty | Moderate positive |
| $\pi_2$ | 3 | 2 attractive $\sigma^{-1}$, more $e$-$e$ repulsion penalty | Small positive but still $> 0$ |

*Triple bond wins because the marginal binding gain from the
3rd shared pair still exceeds the additional electron-electron
repulsion penalty ($ee$ crossing is $\sigma$, eigenvalue $q$).*

*The observed $CO$ bond dissociation energy is
$D_0(CO) \approx 11.09 \;\mathrm{eV}$ — the strongest diatomic
bond, consistent with the LP dual selecting the maximum feasible
bond order $k = 3$ for C (valence 4, using 3) + O (valence 2,
using 2, plus 1 dative bond from C's lone pair).*

*The triple bond also explains why $CO$ is isoelectronic with
$N_2$ in the braid framework: both have 3 shared pairs with the
same Hecke algebra structure in the covalent channels.*
