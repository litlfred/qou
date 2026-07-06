The four principal physical quantities — mass, Q-value,
decay rate, and density — correspond to four distinct
functionals on the categorical action
([categorical action](#def:categorical-action)):

| Physical quantity | Categorical functional | Formula |
|-------------------|----------------------|---------|
| **Mass** | Markov trace (absolute value) | $\mathfrak{m} = |\mathrm{tr}_M(\Phi)|$ |
| **Q-value** | Character sum | $Q = \sum_\lambda \chi_\lambda(\Delta) \times m_e$ |
| **Decay rate** | Frobenius matrix element | $\mathfrak{D} \propto |\langle v, \Phi v \rangle_F|^2$ |
| **Density** | Partial trace (crossing count) | $\rho = \mathrm{tr}_A(\varrho)$ |

Each functional extracts different information from the
same underlying Hecke algebra element:

- The **Markov trace** is a single number — the action
  at rest.  It determines the mass.
- The **character sum** decomposes the action difference
  across irreducible representations.  It determines
  the transition energy.
- The **Frobenius norm** measures the overlap between
  initial and final states.  It determines the
  transition rate.
- The **partial trace** counts crossings per strand.
  It determines the spatial density.
