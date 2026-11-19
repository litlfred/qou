**Algorithm (Gröbner–Shirshov reduction to reduced Coxeter normal form).**
*Reduce an arbitrary braid or affine Hecke word in $B_n$ modulo the quadratic Iwahori–Hecke ideal and Artin braid relations to its unique canonical normal form $\mathrm{NF}(w) = \sum_{u \in S_n} c_u(q)\,T_u \in H_n(q)$ over $\mathbb{Z}[q, q^{-1}]$.*

### Input

- *Braid word $w \in B_n$ (from [Step 1](#alg:categorical-action)) or product of affine Hecke letters $\prod_{r=1}^{m} (c_r\,\sigma_{i_r} + d_r)$ with $c_r, d_r \in \mathbb{Z}[q, q^{-1}, \tfrac{1}{2}]$.*
- *Formal Laurent parameter $q$ with quadratic discriminant $h = q - q^{-1}$.*

### Output

- *Canonical normal-form expansion $\mathrm{NF}(w) = \sum_{u \in S_n} c_u(q)\,T_u \in H_n(q)$ indexed by permutations $u \in S_n$ in shortlex-minimal reduced Coxeter expression $T_u = T_{s_{j_1}} \cdots T_{s_{j_{\ell(u)}}}$ ($\ell(u) \le \binom{n}{2}$), with exact Laurent coefficients $c_u(q)$.*

### Algorithm

1. **Eliminate inverses:** Replace every negative crossing $\sigma_i^{-1}$ by the affine linear combination $\sigma_i - h \cdot 1$.
2. **Compress single-generator runs via $2 \times 2$ transfer matrices:** Whenever $m \ge 2$ consecutive affine factors $(c_r\,C + d_r)$ act on the same generator $C = \sigma_i$ ($C^2 = h\,C + 1$), evaluate the $2 \times 2$ matrix product
   $$
     \begin{pmatrix} A_m & B_m \\ * & * \end{pmatrix}
     \;=\;
     \prod_{r=1}^{m}
     \begin{pmatrix} c_r h + d_r & c_r \\ c_r & d_r \end{pmatrix},
   $$
   replacing the $m$-fold product in one pass by $A_m\,\sigma_i + B_m\cdot 1$. In particular, pure powers satisfy $C^k = a_k(h)\,C + b_k(h)$ with $(a_{k+1}, b_{k+1}) = (h\,a_k + b_k,\; a_k)$ from $(a_0, b_0) = (0, 1)$, and even powers of the bar-fixed achiral crossing $\sigma_i - \tfrac{h}{2}$ collapse to central scalars: $(\sigma_i - \tfrac{h}{2})^2 = \bigl(1 + \tfrac{h^2}{4}\bigr)\cdot 1$.
3. **Apply Gröbner–Shirshov rewrite rules:** Under shortlex order on $\{s_1 < s_2 < \cdots < s_{n-1}\}$, repeatedly apply:
   - *Far commutativity:* $T_j T_i \to T_i T_j$ for $j - i \ge 2$;
   - *Artin braid reduction:* $T_{i+1} T_i T_{i+1} \to T_i T_{i+1} T_i$ (and higher Shirshov overlap words $T_j T_{j-1} \cdots T_i T_j \to T_{j-1} \cdots T_i T_j T_{j-1}$);
   - *Quadratic Hecke reduction:* $T_i T_u \to h\,T_u + T_{s_i u}$ whenever $\ell(s_i u) < \ell(u)$, and $T_i T_u \to T_{s_i u}$ whenever $\ell(s_i u) > \ell(u)$.
4. **Collect basis coefficients:** Sum coefficients of identical reduced Coxeter words $T_u$ in $\mathbb{Z}[q, q^{-1}]$ and discard zero terms.

### Termination and Complexity

Every rewrite step strictly decreases either the word length or the shortlex rank in a well-founded ordering, guaranteeing finite termination. Compressing an $m$-crossing single-generator run via step 2 requires $O(m)$ ring operations instead of $2^m$ binary-tree splits; full basis reduction in $H_n(q)$ touches at most $|S_n| = n!$ basis elements ($6$ for $n = 3$, $24$ for $n = 4$) and runs in $O(|w|\,n^2\,|\mathrm{supp}|)$ Laurent-ring operations where $|\mathrm{supp}| \le n!$ is the active support size.

### Mathematical Justification

1. **Basis theorem and confluence:** By [the Hecke normal-form definition](#def:hecke-normal-form) and Matsumoto's theorem, $H_n(q)$ is a free $\mathbb{Z}[q, q^{-1}]$-module of rank $n!$ on $\{T_u : u \in S_n\}$. All overlap ambiguities among quadratic and Artin relations resolve by Bergman's Diamond Lemma (equivalently, the Coxeter Gröbner–Shirshov basis of $S_n$), so $\mathrm{NF}(w)$ is independent of reduction order.
2. **Categorical compatibility:** [The categorical braid-action definition](#def:categorical-action) ensures that $\bar{\rho}_n(w)$ depends only on $\mathrm{NF}(w)$, making $\mathrm{NF}(w)$ the exact algebraic input for trace and representation functionals downstream.
