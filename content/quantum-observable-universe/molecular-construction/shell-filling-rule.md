**Proposition.**
*The ground-state electron configuration of atom $(Z, N)$ is the
assignment of $Z$ electron trefoils to bonding sites that
minimises the total $\Phi_1$ of the atomic braid.  This
reproduces the aufbau principle:*

1. *Inner shells ($n < n_{\mathrm{val}}$) fill completely because
   each additional electron in a partly filled inner shell reduces
   $\Phi_1$ more than any valence electron.*

2. *Within the valence shell, electrons distribute to maximise the
   number of singly occupied sites (Hund's rule) because parallel
   electron trefoils have lower $\Phi_1$ than antiparallel pairs
   — the $ee$ crossing ($\sigma$, repulsive) is minimised when
   electrons occupy distinct spatial sites.*

3. *The LP dual of the electron assignment problem is:*

$$
  \max_{y} \; Z \cdot y_0
  \quad\text{s.t.}\quad
  y_0 + \sum_{n} G_{n,s} \, y_{n,s} \leq \Phi_1^{(s)}
  \;\;\forall\, \text{sites } s
$$

*where $\Phi_1^{(s)}$ is the $\Phi_1$ contribution of placing
an electron at site $s$, and $G_{n,s}$ encodes the Gram-matrix
penalty for electron-electron repulsion at shell $n$.*

*The dual variable $y_0$ gives the **marginal $\Phi_1$ cost** of
adding one more electron — this is the electronegativity in the
braid framework.*

### ILP electron attachment

*The integer LP builds each electron shell from scratch: starting
from the bare nucleus, add electrons one at a time, at each step
selecting the operator that minimises $|tr_M|$ subject to
Frobenius positivity $G \cdot x \geq 0$.  The ILP discovers
that electrons **alternate generators**:*

See [Table](#tbl:shell-filling-rule-table-data).

*The generator alternation is the Hecke algebra manifestation
of Hund's rule: electrons $e_2$ and $e_6$ (and $e_7$ for $N$, $O$)
attach via $\sigma_0^{-1}$ rather than $\sigma_1^{-1}$, corresponding
to orbital pairing in the $2s$ and $2p$ subshells.*
