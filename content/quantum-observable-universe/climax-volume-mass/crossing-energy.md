Let $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ be a composite of knots connected by a link $\mathcal{L}$, encoded by the braid word $\beta \in B_n$. The **crossing energy** of $\mathfrak{H}$ is

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \sum_{\text{crossings in } \beta}
  \begin{cases}
    q   & \text{positive crossing } (L_+), \\
    -q^{-1} & \text{negative crossing } (L_-),
  \end{cases}
$$

where $q$ is the substrate parameter ([substrate parameter](#def:substrate-parameter)). The sign convention respects the Skein relation

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0.
$$

The crossing energy evaluates the net Skein weight of the composite. A positive $\mathfrak{E}_{\mathrm{cross}}$ implies that repulsion dominates; a negative value implies that binding dominates.

**Archimedean specialisation (§7c).** This block lies on the archimedean side of the substrate wall. It relies on real- or complex-analytic constructs: real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the specific parameter $q_0$. All underlying categorical identities hold over an abstract coefficient ring; we merely specialise their archimedean realisation.
