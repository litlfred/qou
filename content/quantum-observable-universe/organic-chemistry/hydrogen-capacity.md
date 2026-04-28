**Statement.**
For a molecule $\mathrm{C}_{N}\mathrm{H}_{m}$ formed from a
molecular Hopf chain or ring of $N$ carbons with bond-order pattern
$(k_{1}, \ldots, k_{N-1})$ (open) or $(k_{1}, \ldots, k_{N})$
(closed), the hydrogen capacity is

$$
  m = \begin{cases}
      2N + 2 - 2d & \text{open chain},\\
      2N - 2d & \text{closed ring},
    \end{cases}
$$

where $d = \sum_{i}\,(k_{i} - 1)$ is the **total degree of unsaturation**.

**Empirical verification.**
The formula was checked against $19$ standard organic molecules
(alkanes, alkenes, alkynes, dienes, allenes, cycloalkanes,
cyclohexenes, benzene) drawn from IUPAC nomenclature: agreement is
$19/19$ (see witness `hydrogen-capacity.witness.json`).

**Proof sketch.**
A bare carbon vertex has valence $4$.  The backbone consumes
$\sum_{i} k_{i} = (N - 1) + d$ valence units per interior carbon
(open chain) or $N + d$ per ring carbon, distributed across two
neighbours.  The remaining valence at each carbon binds hydrogen.
Open-chain endpoints carry one fewer backbone bond, contributing
the additive $+2$ in the formula.  For closed rings, every carbon
has two backbone neighbours, eliminating the endpoint correction.
A bookkeeping over all $N$ vertices yields the stated formula.
$\square$
