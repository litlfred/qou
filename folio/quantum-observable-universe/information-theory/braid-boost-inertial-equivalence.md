*Let $(\mathbf{C}, A, \tau)$ be an archimedean quantum observable universe over $\mathbb{R}$ with substrate parameter $q > 1$ and causal-cone speed $c_q = 1/(q-1)$ ([speed of light](#def:information-speed-of-light)). For every braid class $\beta$, the kinematic inertia $m_{\mathrm{in}}(\beta)$ that $\beta$ carries as a worldline under a boost along the causal cone equals its Frobenius--Hopf holonomy mass ([mass identity](#def:mass-identity)):*

$$
  m_{\mathrm{in}}(\beta) = \mathfrak{m}(\beta).
$$

The statement has content only once $m_{\mathrm{in}}(\beta)$ is defined without reference to $\mathfrak{m}(\beta)$, through an action of boosts on braid classes. No such action is defined in this work. Two candidate definitions are recorded.

1. **Reeb-clock kinetic coefficient.** Write $\hbar_q = 1 - q^{-1}$ and $\iota_\xi\nabla$ for the Reeb contraction of the connection in the [categorical Dirac operator](#def:categorical-dirac-operator). Scaling the Reeb contraction by a clock rate $\omega$ turns the traced [categorical Hamiltonian](#def:categorical-hamiltonian) Lagrangian into $a_2\,\omega^2 + a_1\,\omega + a_0$, and $m_{\mathrm{in}} = 2a_2 = 2\hbar_q^2\,\tau(\iota_\xi\nabla \circ \iota_\xi\nabla)$ is the natural kinetic coefficient. Under non-abelian Stokes descent the trace $\tau(\iota_\xi\nabla \circ \iota_\xi\nabla)$ is the Casimir-weighted, regular trace of the Hecke algebra, not the Markov trace. This candidate fails. In $H_2(q)$ and $H_3(q)$ the ratio $m_{\mathrm{in}}/\mathfrak{m}$ is a non-constant rational function that depends on $\beta$, and at $q = 1$ one has $m_{\mathrm{in}} = 0$ while $\mathfrak{m} = 2^{c(\beta)}$, with $c(\beta)$ the number of components of the closure. Any candidate of the form $\hbar_q^2$ times a trace that is finite at $q = 1$ fails for the same reason.
2. **Boost action.** A one-parameter family of automorphisms of the braided Frobenius--Hopf data, preserving the cone $|v| < c_q$, with $m_{\mathrm{in}}(\beta)$ read off as the second-order response of the traced Lagrangian of $\beta$ to the boost parameter. This candidate is not yet constructed.

If the conjecture holds, the rest energy of a braid class is $\mathfrak{E}(\beta) = \mathfrak{m}(\beta)\,c_q^2$ ([mass--energy equivalence](#prop:mass-energy)).
