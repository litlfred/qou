*Let $\mathrm{tr}$ be a Markov trace with parameter $z$ on the Hecke tower, and let the constituent vacuum $\mathcal{B}_K^{\mathrm{vac}} \in H_{3A}(q)$ be the product of $Z$ proton and $N$ neutron block words on disjoint $3$-strand windows (generators $3k, 3k+1$ for block $k$), with no interface crossings. For a generator $\sigma_g$ carrying the accumulated factor $W_g = \alpha_g\,\sigma_g + \beta_g$, define $\hat V_g := \mathrm{tr}(W_g)$. Then*

$$
  \hat V_g \;=\; \beta_g + \alpha_g\, z,
$$

*independent of the strand count $3A$, of the position $g$, and of the other blocks. If a block word is the ascending product $W_{3k} W_{3k+1}$, its trace is $\hat V_{3k}\,\hat V_{3k+1}$. For any arrangement of the blocks,*

$$
  \mathrm{tr}\bigl(\mathcal{B}_K^{\mathrm{vac}}\bigr) \;=\; v_p^{Z}\, v_n^{N},
  \qquad
  v_p = \hat V^{p}_0\, \hat V^{p}_1, \quad v_n = \hat V^{n}_0\, \hat V^{n}_1 .
$$

The proof uses only the trace axioms and the three Hecke relations, over a generic commutative ring. The last identity is the disjoint-block trace law, with each block read at offset $0$ by shift invariance.

**Scope.** The product formula holds for the *ascending* block word $W_{3k}W_{3k+1}$. When a block's braid word interleaves its two generators, the trace of that word is $\mathrm{tr}(w_p)$ and not $\hat V_0 \hat V_1$, because reordering changes the trace. For example, $\mathrm{tr}(\sigma_1\sigma_2\sigma_1\sigma_2) - \mathrm{tr}(\sigma_1^2\sigma_2^2) = z^2 - hz - 1 = -(q^4+q^2+1)/(q^2+1)^2$ at $z = q^3/(q^2+1)$. The disjoint-block law still gives $\mathrm{tr}(\mathcal{B}_K^{\mathrm{vac}}) = \mathrm{tr}(w_p)^Z\,\mathrm{tr}(w_n)^N$ in that case.
