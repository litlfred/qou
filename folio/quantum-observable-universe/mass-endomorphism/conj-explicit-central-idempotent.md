**Lemma (Murphy–Lagrange joint-eigenbasis interpolation).** *Let $V$ be a finite-dimensional vector space over a field $K$, and let $J_1, \ldots, J_n \in \mathrm{End}_K(V)$ be commuting operators acting diagonally on a basis $\{v_T\}_{T \in \mathcal{T}}$ indexed by the standard Young tableaux of size $n$:*

$$
  J_k \cdot v_T \;=\; c_T(k; q)\, v_T, \qquad c_T(k; q) \;=\; q^{\,2(j(k) - i(k))},
$$

*where $(i(k), j(k))$ is the cell of $T$ containing $k$ and the eigenvalue tuples $(c_T(1; q), \ldots, c_T(n; q))$ are pairwise distinct across $T \in \mathcal{T}$. Let $\mathrm{C}(n) := \{c_T(k; q) : T \in \mathcal{T},\; 1 \leq k \leq n\}$, and define for each $T \in \mathcal{T}$ and each partition $\lambda \vdash n$ the operators*

$$
  P_T \;:=\; \prod_{k=1}^{n} \prod_{\substack{c \in \mathrm{C}(n) \\ c \neq c_T(k; q)}} \frac{J_k - c}{c_T(k; q) - c}, \qquad e_\lambda \;:=\; \sum_{T \in \mathrm{SYT}(\lambda)} P_T.
$$

*Then:*

1. *Eigenbasis projection: $P_T(v_{T'}) = \delta_{T, T'}\, v_{T'}$ and $e_\lambda(v_{T'}) = \delta_{\mathrm{shape}(T'),\, \lambda}\, v_{T'}$ for all $T, T' \in \mathcal{T}$.*
2. *Completeness: $\sum_{\lambda \vdash n} e_\lambda = \mathrm{id}_V$.*
3. *Mutual orthogonality and idempotency: $e_\lambda e_\mu = \delta_{\lambda\mu}\, e_\lambda$, and in particular $e_\lambda^2 = e_\lambda$.*
4. *Transpose and content-inversion pairing: for every cell $\square = (i, j)$ with transpose $\square' = (j, i)$, the $q$-contents satisfy $c(\square'; q) = c(\square; q^{-1}) = c(\square; q)^{-1}$. If $\tau \in \mathrm{GL}_K(V)$ acts on the eigenbasis by tableau transposition $\tau(v_T) = v_{T'}$, then $\tau e_\lambda \tau^{-1} = e_{\lambda'}$ (equivalently, substituting inverted contents $c_T(k; q^{-1}) = c_{T'}(k; q)$ at fixed $J_k$ maps $e_\lambda$ to $e_{\lambda'}$), fixing $e_\lambda$ whenever $\lambda = \lambda'$.*

*Proof.* By [Jucys–Murphy central elements](#prop:jucys-murphy-central-elements-qou) and [Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form), each linear factor $(c_T(k; q) - c)^{-1}(J_k - c)$ scales $v_{T'}$ by $(c_T(k; q) - c)^{-1}(c_{T'}(k; q) - c)$ \cite{murphy1981,ram1997}. When $T' = T$, every factor in the inner product over $c \in \mathrm{C}(n) \setminus \{c_T(k; q)\}$ equals $1$, so $P_T(v_T) = v_T$. When $T' \neq T$, eigenvalue-tuple separation supplies at least one index $k$ with $c_{T'}(k; q) \neq c_T(k; q)$; since $c_{T'}(k; q) \in \mathrm{C}(n)$, the factor $c = c_{T'}(k; q)$ occurs in the $k$-th inner product and annihilates $v_{T'}$, giving $P_T(v_{T'}) = 0$. Summing over $T \in \mathrm{SYT}(\lambda)$ yields $e_\lambda(v_{T'}) = \delta_{\mathrm{shape}(T'),\, \lambda}\, v_{T'}$, proving (1).

For any $T' \in \mathcal{T}$, evaluating $\bigl(\sum_{\lambda \vdash n} e_\lambda\bigr)(v_{T'})$ isolates the unique summand $\lambda = \mathrm{shape}(T')$ and returns $v_{T'}$; since $\{v_{T'}\}_{T' \in \mathcal{T}}$ is a basis of $V$, $\sum_{\lambda \vdash n} e_\lambda = \mathrm{id}_V$, proving (2). Similarly, $(e_\lambda e_\mu)(v_{T'}) = \delta_{\mathrm{shape}(T'),\,\mu}\, e_\lambda(v_{T'}) = \delta_{\lambda\mu}\,\delta_{\mathrm{shape}(T'),\,\lambda}\, v_{T'} = \delta_{\lambda\mu}\, e_\lambda(v_{T'})$ on every basis vector $v_{T'}$, whence $e_\lambda e_\mu = \delta_{\lambda\mu}\, e_\lambda$ and $e_\lambda^2 = e_\lambda$ \cite{dipper-james1986}, proving (3).

Finally, for $\square = (i, j)$ and $\square' = (j, i)$, $2(i - j) = -2(j - i)$ gives $q^{2(i - j)} = (q^{-1})^{2(j - i)} = (q^{2(j - i)})^{-1}$, so $c_{T'}(k; q) = c_T(k; q^{-1}) = c_T(k; q)^{-1}$. Because tableau transposition $T \mapsto T'$ is an involution carrying $\mathrm{SYT}(\lambda)$ bijectively onto $\mathrm{SYT}(\lambda')$, evaluating $(\tau e_\lambda \tau^{-1})(v_U) = \tau\bigl(e_\lambda(v_{U'})\bigr) = \delta_{\mathrm{shape}(U'),\,\lambda}\, v_U = \delta_{\mathrm{shape}(U),\,\lambda'}\, v_U = e_{\lambda'}(v_U)$ on every basis vector establishes $\tau e_\lambda \tau^{-1} = e_{\lambda'}$, which reduces to $\tau e_\lambda \tau^{-1} = e_\lambda$ when $\lambda = \lambda'$. $\square$
