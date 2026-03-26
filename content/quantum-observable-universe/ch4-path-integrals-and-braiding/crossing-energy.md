Let $H = [K_1, \ldots, K_n]_c \bowtie \mathcal{L}$ be a composite
of knots linked by a link $\mathcal{L}$, with braid word
$\beta \in B_n$ representing the linking.  The *crossing energy*
of $H$ is

$$
  E_{\mathrm{cross}}(H)
  \;=\;
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
  q \, L_+ \;-\; q^{-1} L_-
  \;=\; (q^{1/2} - q^{-1/2})\, L_0.
$$

The crossing energy measures the net Skein weight of the composite:
positive $E_{\mathrm{cross}}$ indicates repulsion dominates,
negative indicates binding dominates.  This quantity is computed
entirely from the $R$-matrix braiding
([R-matrix](#rem:r-matrix-braiding)) of
$\mathcal{U}_q(\mathfrak{su}(2))$ acting on the tensor product
of constituent representations.
