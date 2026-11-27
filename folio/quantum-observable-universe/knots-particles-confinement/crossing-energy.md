Let $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ be a composite of knots linked by $\mathcal{L}$, with braid word $\beta \in B_n$ representing the linking. The **crossing energy** of $\mathfrak{H}$ is defined by

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \sum_{\text{crossings in } \beta}
  \begin{cases}
    q   & \text{positive crossing } (L_+), \\
    -q^{-1} & \text{negative crossing } (L_-),
  \end{cases}
$$

where $q$ is the aether parameter ([aether parameter](#def:substrate-parameter)). The sign convention follows the Skein relation

$$
  q\,L_+ - q^{-1} L_-
  = (q^{1/2} - q^{-1/2})\,L_0.
$$

The crossing energy is an un-traced, crossing-additive Skein writhe functional in dimensionless aether units, distinct from the traced [categorical Hamiltonian](#def:categorical-hamiltonian) (on the trivial $n$-strand braid $\mathfrak{E}_{\mathrm{cross}} = 0$, whereas the traced rest Hamiltonian is nonzero). A positive $\mathfrak{E}_{\mathrm{cross}}$ indicates that positive-crossing repulsion dominates; a negative value indicates that negative-crossing pairing dominates.

**Archimedean specialisation.** What follows sits on the archimedean side of the algebraic→archimedean wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the aether parameter $q_0$. The generic categorical/$q$-deformation identities it relies upon remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
