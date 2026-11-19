Let $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ be a composite of knots linked by $\mathcal{L}$, with braid word $\beta \in B_n$ representing the linking. Define the **crossing energy** of $\mathfrak{H}$ as:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \sum_{\text{crossings in } \beta}
  \begin{cases}
    q   & \text{positive crossing } (L_+), \\
    -q^{-1} & \text{negative crossing } (L_-),
  \end{cases}
$$

where $q$ is the aether parameter ([aether parameter](#def:substrate-parameter)). The sign convention follows the Skein relation:

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0.
$$

The crossing energy measures the net Skein weight of the composite. A positive $\mathfrak{E}_{\mathrm{cross}}$ indicates that repulsion dominates; a negative value indicates that binding dominates.
