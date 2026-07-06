Let $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ be a composite
of knots linked by a link $\mathcal{L}$, with braid word
$\beta \in B_n$ representing the linking.  The **crossing energy**
of $\mathfrak{H}$ is

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \sum_{\text{crossings in } \beta}
  \begin{cases}
    q   & \text{positive crossing } (L_+), \\
    -q^{-1} & \text{negative crossing } (L_-),
  \end{cases}
$$

where $q$ is the substrate parameter
([substrate parameter](#def:substrate-parameter)) and the sign
convention follows the Skein relation

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0.
$$

The crossing energy measures the net Skein weight of the composite:
positive $\mathfrak{E}_{\mathrm{cross}}$ indicates repulsion dominates,
negative indicates binding dominates.

**Archimedean specialisation (§7c).** This block is stated over the real field $\mathbb{R}$ — the archimedean side of the substrate wall: its constructs are real-valued (physical observables, real-analytic bounds, or numerical evaluations at the substrate parameter $q_0$) rather than generic-ring $q$-deformation data. The generic categorical / $q$-deformation machinery it draws on is stated over an abstract coefficient ring in its own blocks; only the archimedean realisation is specialised here.
