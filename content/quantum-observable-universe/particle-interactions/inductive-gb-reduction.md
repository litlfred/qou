We compute the nuclear normal form inductively by reducing intermediate words after each multiplication.

**Proposition.**
*Let $\mathcal{N}_{\leq k}$ denote the Gröbner–Shirshov normal form of the first $k$ nucleons in $H_k(q)$. The inductive step*

$$
  \mathcal{N}_{\leq k+1} = r\!\bigl(\mathcal{N}_{\leq k} \cdot C(\mathfrak{N}_k, \mathfrak{N}_{k+1}; \sigma_g) \cdot \mathfrak{N}_{k+1},\; G\bigr)
$$

*yields a normal form containing at most $\binom{A-1}{\lfloor(A-1)/2\rfloor}$ terms. Here, $r(\cdot, G)$ denotes the Gröbner–Shirshov division algorithm ([nuclear Gröbner reduction](#prop:nuclear-groebner-reduction)).*
