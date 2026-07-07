*The ground-state electron configuration of atom $(Z, N)$ is the assignment of $Z$ electron trefoils to bonding sites that minimises the total $\Phi_1$ of the atomic braid. This reproduces the aufbau principle:*

1. *Inner shells ($n < n_{\mathrm{val}}$) fill completely because each additional electron in a partly filled inner shell reduces $\Phi_1$ more than any valence electron.*

2. *Within the valence shell, electrons distribute to maximise the number of singly occupied sites (Hund's rule). Parallel electron trefoils have lower $\Phi_1$ than antiparallel pairs. The $ee$ crossing ($\sigma$, repulsive) is minimised when electrons occupy distinct spatial sites.*

3. *The LP dual of the electron assignment problem is:*

$$
  \max_{y} \; Z \cdot y_0
  \quad\text{s.t.}\quad
  y_0 + \sum_{n} G_{n,s} \, y_{n,s} \leq \Phi_1^{(s)}
  \;\;\forall\, \text{sites } s
$$

*where $\Phi_1^{(s)}$ is the $\Phi_1$ contribution of placing an electron at site $s$, and $G_{n,s}$ encodes the Gram-matrix penalty for electron-electron repulsion at shell $n$.*
