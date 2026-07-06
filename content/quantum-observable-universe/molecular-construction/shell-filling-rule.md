**Proposition.**
*The ground-state electron configuration of an atom $(Z, N)$ corresponds to the assignment of $Z$ electron trefoils to bonding sites that minimises the total $\Phi_1$ of the atomic braid. This assignment recovers the aufbau principle:*

1. *Inner shells ($n < n_{\mathrm{val}}$) fill completely. Each additional electron in a partly filled inner shell reduces $\Phi_1$ more steeply than any valence electron.*
2. *Within the valence shell, electrons distribute to maximise singly occupied sites, recovering Hund's rule. Parallel electron trefoils yield lower $\Phi_1$ than antiparallel pairs. The repulsive $ee$ crossing ($\sigma$) achieves its minimum when electrons occupy distinct spatial sites.*
3. *The LP dual of the electron assignment problem is:*

$$
  \max_{y} \; Z \cdot y_0
  \quad\text{s.t.}\quad
  y_0 + \sum_{n} G_{n,s} \, y_{n,s} \leq \Phi_1^{(s)}
  \;\;\forall\, \text{sites } s
$$

*The parameter $\Phi_1^{(s)}$ denotes the $\Phi_1$ contribution of placing an electron at site $s$. The tensor $G_{n,s}$ encodes the Gram-matrix penalty for electron-electron repulsion within shell $n$.*
