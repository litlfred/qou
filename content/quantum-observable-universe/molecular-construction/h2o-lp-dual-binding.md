**Proposition.**
*The LP dual of the $\mathrm{H}_2\mathrm{O}$ molecular braid
selects the configuration with two single O–H $\sigma$ bonds
(2 shared pairs) and two retained lone pairs on $O$, as optimal
over alternatives with higher bond order or fewer lone pairs.*

*The binding LP for $\mathrm{H}_2\mathrm{O}$ is*

$$
  \min_{k_1, k_2, \pi} \;
    \Phi_1\!\bigl(\mathcal{M}(H_1, H_2, O;\; k_1, k_2, \pi)\bigr)
$$

*over the bond orders $k_1, k_2 \in \{1, 2\}$ of the two O–H
bonds and strand ordering $\pi$.  (Bond orders above $1$ would
require unpairing an oxygen lone pair into a second bonding
channel.)  The feasibility constraints are*

- *$k_1 + k_2 + \#(\text{lone pairs on } O) = 4$
  (oxygen has 4 valence pairs in the $n = 2$ shell),*
- *$k_i \leq 1$ per H atom (each hydrogen contributes a single
  valence electron).*

*The dual*

$$
  \max_{y_1, y_2} \; \sum_{i \in \{1,2\}} k_i \, y_i
  \quad\text{s.t.}\quad
  y_i \leq \Delta\Phi_1(k_i) - \Delta\Phi_1(k_i - 1)
  \;\;\forall\, i
$$

*where $\Delta\Phi_1(k) = \Phi_1^{\mathrm{sep}} -
\Phi_1^{\mathrm{H_2O}}(k)$ is the $\Phi_1$ reduction from the
$k$-th shared pair on a given O–H channel.*

*The marginal $\Phi_1$ reduction per additional bond or lone
pair is:*

| Channel | $k$ | Marginal gain | Selected? |
|:--------|:----|:--------------|:----------|
| O–$H_1$ $\sigma$ | 1 | Large positive (first bond on O) | Yes |
| O–$H_2$ $\sigma$ | 1 | Large positive (first bond on O) | Yes |
| Additional O–H $\pi$ | 2 | **Infeasible** — H has only one valence electron | No |
| O lone pair 1 (trefoil on $O$) | — | Moderate positive — keeps $2p_z$ fully occupied | Yes |
| O lone pair 2 (trefoil on $O$) | — | Moderate positive — keeps $2p_{\perp}$ pair intact | Yes |

*The two lone pairs dominate the alternative in which one lone
pair is "promoted" to a second bond with one of the hydrogens:
doing so would force a 3-electron O–H channel, which is
disallowed by the [electron-shell braid capacity](#def:electron-shell-braid-capacity).*

*The observed O–H bond dissociation energy is
$D_0(\text{O–H}) \approx 4.77 \;\mathrm{eV}$, and the total
atomization energy of $\mathrm{H}_2\mathrm{O}$ is
$D_0(\mathrm{H}_2\mathrm{O}) \approx 9.51 \;\mathrm{eV}$ — the
sum of two O–H bonds, consistent with the LP dual selecting
$k_1 = k_2 = 1$.*
