**Algorithm (Braid-to-Hecke categorical representation).**
*Construct the group homomorphism $\rho_n \colon B_n \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})$ induced by the braiding $c_{V,V}$ on the fundamental object $V \in \mathbf{C}$, together with its quotient factorisation $\bar{\rho}_n \colon B_n \to H_n(q)^\times$ into the invertible group of the Iwahori–Hecke algebra.*

### Input

- *Artin braid word $w = \sigma_{i_1}^{\varepsilon_1} \cdots \sigma_{i_k}^{\varepsilon_k} \in B_n$ with $1 \le i_r \le n - 1$ and $\varepsilon_r \in \{+1, -1\}$.*
- *$R$-linear rigid braided monoidal category $\mathbf{C}$ with fundamental object $V \in \mathbf{C}$ whose braiding $c_{V,V} \in \mathrm{Aut}_{\mathbf{C}}(V \otimes V)$ has spectral eigenvalues $+q$ on $\mathrm{Sym}^2 V$ and $-q^{-1}$ on $\Lambda^2 V$.*

### Output

- *Categorical automorphism $\rho_n(w) \in \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})$ expressed as a formal composition of local braidings, and its image $\bar{\rho}_n(w) \in H_n(q)^\times$.*

### Algorithm

1. For each positive Artin generator $\sigma_i$ ($1 \le i \le n - 1$) occurring in $w$, assign the local braiding endomorphism
   $$
     \rho_n(\sigma_i)
     \;=\;
     \mathrm{id}_V^{\otimes(i-1)} \otimes c_{V,V} \otimes \mathrm{id}_V^{\otimes(n-i-1)}
     \;\in\; \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})
   $$
   (with monoidal associators inserted canonically by Mac Lane coherence).
2. For each inverse generator $\sigma_i^{-1}$, assign $\rho_n(\sigma_i^{-1}) = \mathrm{id}_V^{\otimes(i-1)} \otimes c_{V,V}^{-1} \otimes \mathrm{id}_V^{\otimes(n-i-1)}$, which satisfies $c_{V,V}^{-1} = c_{V,V} - (q - q^{-1})\,\mathrm{id}_{V \otimes V}$ whenever $(c_{V,V} - q)(c_{V,V} + q^{-1}) = 0$.
3. Compose the local factors in word order: $\rho_n(w) = \rho_n(\sigma_{i_1}^{\varepsilon_1}) \circ \cdots \circ \rho_n(\sigma_{i_k}^{\varepsilon_k})$.

### Termination and Complexity

The assignment executes in $O(|w|)$ symbolic operations for a word of length $k = |w|$. No $2^n \times 2^n$ tensor-space matrix expansion is formed; the word is passed directly as a sequence of Hecke generators to [Gröbner–Shirshov reduction](#alg:gs-reduce-to-hecke-nf).

### Mathematical Justification

1. **Well-definedness:** By [the categorical braid-action definition](#def:categorical-action), the hexagon axioms of $\mathbf{C}$ imply the Yang–Baxter braid relations $\rho_n(\sigma_i \sigma_{i+1} \sigma_i) = \rho_n(\sigma_{i+1} \sigma_i \sigma_{i+1})$ and far commutativity $\rho_n(\sigma_i \sigma_j) = \rho_n(\sigma_j \sigma_i)$ ($|i - j| \ge 2$). Because $\dim V = 2$ and $c_{V,V}$ has minimal polynomial $(\lambda - q)(\lambda + q^{-1}) = \lambda^2 - (q - q^{-1})\lambda - 1$, $\rho_n$ descends through the Iwahori–Hecke quotient $R[B_n] \twoheadrightarrow H_n(q)$.
2. **Existence and uniqueness:** Existence on any quantum observable universe is established by [categorical-action existence](#prop:categorical-action-exists), and uniqueness up to monoidal natural isomorphism follows from [categorical-action uniqueness](#prop:categorical-action-unique). The construction depends purely on the braided monoidal structure of $\mathbf{C}$ prior to applying the fibre functor $\tau$.
