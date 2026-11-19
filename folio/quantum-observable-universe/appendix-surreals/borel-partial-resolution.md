The depth correspondence ([depth–period correspondence](#conj:gb-depth-period-correspondence)) asserts both an inclusion and a sharpness condition. Via the K-theory translation ([K-theory period Rosetta](#rem:k-theory-period-rosetta)), the sharpness condition factors through Borel's theorem on the algebraic K-theory of number fields. This proposition records the explicit Borel dimensions for each Bring-natural number field.

**Theorem (Borel 1977).** Let $F$ be a number field with $r_1$ real embeddings and $r_2$ pairs of complex embeddings. Then for $n \geq 2$:

$$
\dim_{\mathbb{Q}} \bigl( K_{2n-1}(F) \otimes \mathbb{Q} \bigr) =
\begin{cases}
  r_1 + r_2 & \text{if } n \text{ even}, \\
  r_2 & \text{if } n \text{ odd}.
\end{cases}
$$

The same formula holds for the indecomposable part $K_{2n-1}^{\mathrm{ind}}$.

Each Bring-embeddable knot $K$ has a shape parameter $z_K \in \overline{\mathbb{Q}}^\times$ generating a number field $F_K = \mathbb{Q}(z_K)$. The Borel rank gives the minimum dimension of the Beilinson regulator image at depth $n$.

See [Table 1](#tbl:borel-partial-resolution-table1-data).

At depth 2 (figure-8 row), Borel's theorem gives $\dim_\mathbb{Q} K_3^{\mathrm{ind}}(\mathbb{Q}(\zeta_6)) \otimes \mathbb{Q} = 1$. The Bloch–Wigner regulator maps this injectively after rationalisation. The image is exactly the $\mathbb{Q}$-line spanned by $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$. Inclusion and sharpness hold at depth 2 over $\mathbb{Q}(\zeta_6)$. The depth-2 case of the depth correspondence is a theorem at the figure-8 row.

At depth 3 (Bring trilog row), Borel's theorem gives $\dim_\mathbb{Q} K_5^{\mathrm{ind}}(\mathbb{Q}(\zeta_5)) \otimes \mathbb{Q} = 2$. The Goncharov regulator maps this rank-2 space to $\mathcal{P}_3 / \mathcal{P}_2$. The Bring trilog witness ([Bring trilog depth-3 witness](#conj:bring-trilog-depth-3-witness)) provides 4 grouplike values $\{\mathrm{Li}_3(\zeta_5^k) : k = 1,2,3,4\}$. Modulo the orbit-sum relation, these span a $\mathbb{Q}$-vector space of exact rank 2, matching Borel's prediction. Whether the entire $\mathcal{P}_3 / \mathcal{P}_2$ over $\mathbb{Q}(\zeta_5)$ is generated is Beilinson's conjecture.

Borel's theorem gives explicit Borel-rank lower bounds on the dimension of $\tau_\mathrm{arch}(G^{(n)})$ in $\mathcal{P}_n / \mathcal{P}_{n-1}$ for every Bring-natural number field. It does not provide the upper bound (Beilinson's conjecture).

For the depth correspondence, depth 2 is a theorem. Depth 3 has Borel-rank lower bounds as theorems, leaving Beilinson's conjecture as the remaining piece. Depth $\geq 4$ is fully Beilinson-conjectural.
