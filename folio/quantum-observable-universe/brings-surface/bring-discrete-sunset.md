*Let $\Gamma$ be the vertex graph of the Bring map $\{5,4\}$: $30$ vertices (the cosets $x\langle S\rangle$), each of degree $4$, with an edge for each of the $60$ edges $\{x, xA\}$. Let $\Delta = 4I - \mathrm{Adj}$ be its graph Laplacian, and $G$ its Green function on mean-zero functions, $\Delta G = I - J/30$.*

*(i) Functions on the vertices split under $S_5 \times \langle c\rangle$ as*

$$
  \mathbb{Q}^{30} = \mathrm{triv}^+ \oplus \mathrm{std}^+ \oplus [2,1^3]^- \oplus [3,2]^+ \oplus [2,2,1]^+ \oplus [2,2,1]^- \oplus [3,1,1]^-,
$$

*each type with multiplicity one, so $\Delta$ is a scalar $\lambda$ on each: $\lambda = 0, 5, 7, 2, 6, 4, 2$ in that order. Hence $\mathrm{spec}\,\Delta = \{0^1, 2^{11}, 4^5, 5^4, 6^5, 7^4\}$. The eigenvalue $2$ carries two types, $[3,2]^+ \oplus [3,1,1]^-$.*

*(ii) Write $G = \sum_{k \ne \mathrm{triv}} P_k/\lambda_k$ with $P_k$ the typed projectors. The typed partial sunset $\sum_{x,y} G_a(x,y)\,G_b(x,y)\,G_c(x,y)$, $G_k = P_k/\lambda_k$, vanishes on every triple forbidden by the selection rule of [the spectral sunset](#prop:bring-spectral-sunset-selection).*

*(iii) The rule is necessary, not sufficient: $\mathrm{std}^+ \otimes \mathrm{std}^+ \otimes [3,2]^+$ is allowed ($N = 1$, all even), and its partial sunset is $0$. The other $25$ unordered allowed triples of nontrivial types are nonzero.*

*(iv) The discrete sunset is*

$$
  \sum_{x,y \in \Gamma} G(x,y)^3 = \frac{18364201}{22680000}.
$$
