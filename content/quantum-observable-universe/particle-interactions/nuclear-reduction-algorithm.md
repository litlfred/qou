The following algorithm computes the Groebner--Shirshov normal form
of a nuclear braid word, following the division algorithm of
\cite{leitnerpawloski2004} specialised to the Iwahori--Hecke algebra.

**Input:** Mass number $A = Z + N$, proton number $Z$, neutron
number $N$; the Iwahori--Hecke algebra $H_A(q) = R[B_A] / I$ with
$R = \mathbb{Z}[q, q^{-1}]$;
the admissible system $(B, <)$ where $B$ = positive braid monomials
and $<$ = length-lexicographic ordering
([admissible system](#unital-groebner-bases:def:admissible-system));
the Groebner--Shirshov basis $G = \{\sigma_i^2 - (q-q^{-1})\sigma_i - 1,\;
\sigma_i\sigma_{i+1}\sigma_i - \sigma_{i+1}\sigma_i\sigma_{i+1},\;
\sigma_i\sigma_j - \sigma_j\sigma_i\}$ for $|i-j| \geq 2$.

**Output:** The unique normal form
$\mathcal{N}(Z, N) \in H_A(q)$ and the Markov trace
$\mathrm{tr}_M(\mathcal{N}(Z, N))$.

1. Set $\mathcal{N}_{\leq 1} := \mathfrak{N}_1$ (the first
   nucleon's normal form in $H_1(q)$: proton
   $\mathfrak{p}$ or neutron $\mathfrak{n}$).
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

   - Form the product
     $f_k := \mathcal{N}_{\leq k} \cdot C \cdot \mathfrak{N}_{k+1}$
     in $H_{k+1}(q)$.
   - Apply the division algorithm
     ([division algorithm](#unital-groebner-bases:def:division-algorithm)):
     set $i := 0$, $f_0 := f_k$.
   - **While** $f_i \neq 0$:
     - Set $i := i + 1$.
     - **If** no $g \in G$ has $\mathrm{LT}(g) \mid f_{i-1}$:
       set $r_i := \mathrm{LT}(f_{i-1})$,
       $f_i := f_{i-1} - r_i$.
     - **Else**: choose $g \in G$ with
       $\mathrm{LT}(g) \mid f_{i-1}$; choose
       $\lambda \in R^*$, $u, v \in B$ with
       $\lambda\,\mathrm{LT}(u \cdot g \cdot v) = \mathrm{LT}(f_{i-1})$;
       set $f_i := f_{i-1} - \lambda\,u \cdot g \cdot v$,
       $r_i := 0$.
   - Set $\mathcal{N}_{\leq k+1} := \sum_i r_i$.
3. Return $\mathcal{N}(Z, N) := \mathcal{N}_{\leq A}$ and
   $\mathrm{tr}_M(\mathcal{N}(Z, N))$.

**Correctness.** The output is independent of the choice of
$g \in G$ at each step because $G$ is a Groebner--Shirshov basis
([main theorem](#unital-groebner-bases:thm:main-theorem)).

**Complexity.** The inductive strategy (reduce after each
multiplication) yields $O(A^2)$ multiplications and $O(A^3)$ Hecke
reduction steps
([inductive reduction](#def:inductive-gb-reduction)),
compared to $O(2^{Z \cdot N})$ terms if all crossings are multiplied
before reducing.
