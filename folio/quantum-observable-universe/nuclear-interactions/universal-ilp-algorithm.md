**Definition (Universal ILP Algorithm).**
*Given a state $x \in H_3(q)$, the Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ and the Markov traces $t_i = \mathrm{tr}_M(b_i)$, the **universal ILP algorithm** selects the operator*

$$
  K \;=\; \operatorname*{arg\,min}_{K} \; \mathrm{cr}(K) \quad
  \text{s.t.} \quad K \in \{\text{knots}\} \setminus \{1\}, \quad
  G \cdot \mathrm{NF}(x \cdot K) \geq 0,
$$

*breaking ties among feasible $K$ of equal crossing number by minimising $|\mathrm{tr}_M(x \cdot K)|$, and updates the state by $x \leftarrow \mathrm{NF}(x \cdot K)$ before proceeding to the next level.*
