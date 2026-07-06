We compute the Gröbner--Shirshov normal form of a nuclear braid word via the division algorithm of \cite{leitnerpawloski2004}, specialized to the Iwahori--Hecke algebra.

**Input:** Mass number $A = Z + N$, proton number $Z$, neutron number $N$. The Iwahori--Hecke algebra $H_A(q) = R[B_A] / I$ over $R = \mathbb{Z}[q, q^{-1}]$. The admissible system ([admissible system](#unital-groebner-bases:def:admissible-system)) $(B, <)$, where $B$ contains positive braid monomials and $<$ denotes the length-lexicographic order. The Gröbner--Shirshov basis $G = \{\sigma_i^2 - (q-q^{-1})\sigma_i - 1,\; \sigma_i\sigma_{i+1}\sigma_i - \sigma_{i+1}\sigma_i\sigma_{i+1},\; \sigma_i\sigma_j - \sigma_j\sigma_i\}$ for $|i-j| \geq 2$.

**Output:** The unique normal form $\mathcal{N}(Z, N) \in H_A(q)$ and its Markov trace $\mathrm{tr}_M(\mathcal{N}(Z, N))$.

1. Set $\mathcal{N}_{\leq 1} := \mathfrak{N}_1$ (the normal form of the first nucleon in $H_1(q)$: proton $\mathfrak{p}$ or neutron $\mathfrak{n}$).
2. **For** $k = 1, \ldots, A-1$:
   - Determine the crossing type $C(\mathfrak{N}_k, \mathfrak{N}_{k+1}; \sigma_k)$:

     $$
       C = \begin{cases}
         \sigma_k & \text{if both protons ($pp$)} \\[3pt]
         \sigma_k^{-1} = \sigma_k - (q - q^{-1})
           & \text{if both neutrons ($nn$)} \\[3pt]
         \sigma_k - \tfrac{1}{2}(q - q^{-1})
           & \text{if mixed ($pn$ or $np$)}
       \end{cases}
     $$

   - Form the product $f_k := \mathcal{N}_{\leq k} \cdot C \cdot \mathfrak{N}_{k+1}$ in $H_{k+1}(q)$.
   - Apply the division algorithm ([division algorithm](#unital-groebner-bases:def:division-algorithm)): set $i := 0$, $f_0 := f_k$.
   - **While** $f_i \neq 0$:
     - Set $i := i + 1$.
     - **If** no $g \in G$ satisfies $\mathrm{LT}(g) \mid f_{i-1}$: set $r_i := \mathrm{LT}(f_{i-1})$ and $f_i := f_{i-1} - r_i$.
     - **Else**: choose $g \in G$ satisfying $\mathrm{LT}(g) \mid f_{i-1}$. Choose $\lambda \in R^*$ and $u, v \in B$ such that $\lambda\,\mathrm{LT}(u \cdot g \cdot v) = \mathrm{LT}(f_{i-1})$. Set $f_i := f_{i-1} - \lambda\,u \cdot g \cdot v$ and $r_i := 0$.
   - Set $\mathcal{N}_{\leq k+1} := \sum_i r_i$.
3. Return $\mathcal{N}(Z, N) := \mathcal{N}_{\leq A}$ and $\mathrm{tr}_M(\mathcal{N}(Z, N))$.

**Correctness.** The output remains independent of the choice of $g \in G$ at each step because $G$ is a Gröbner--Shirshov basis ([main theorem](#unital-groebner-bases:thm:main-theorem)).

**Complexity.** This inductive strategy (reducing after each multiplication) requires $O(A^2)$ multiplications and $O(A^3)$ Hecke reduction steps ([inductive reduction](#prop:inductive-gb-reduction)). Multiplying all crossings before reduction would generate $O(2^{Z \cdot N})$ terms.
