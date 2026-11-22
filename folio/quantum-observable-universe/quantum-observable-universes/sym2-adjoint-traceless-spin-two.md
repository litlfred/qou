**Proposition.** *Let $G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$ be the gauge group of [the emergence theorem](#thm:su2-emergence), with simple objects $V_j$ labelled by [spin](#prop:spin-labels) and adjoint $V_1 \cong \mathrm{Ad}(A)$. Then*

$$
  \mathrm{Sym}^2(V_1) \;\cong\; V_0 \oplus V_2,
  \qquad
  \dim:\; 6 = 1 + 5 ,
$$

*so the traceless part $\mathrm{Sym}^2(V_1) \ominus V_0$ is the single simple object $V_2$, of spin $2$ and dimension $5$.*

**Proof.** By Clebsch–Gordan \cite{fulton-harris1991}, $V_1 \otimes V_1 \cong V_0 \oplus V_1 \oplus V_2$, and the summand $V_k$ of $V_j \otimes V_j$ lies in $\mathrm{Sym}^2(V_j)$ exactly when $k \equiv 2j \pmod 2$. For $j = 1$ this places $V_0$ and $V_2$ in $\mathrm{Sym}^2(V_1)$ and $V_1$ in $\Lambda^2(V_1)$. The summand $V_0$ is spanned by the invariant symmetric form on $V_1$, so removing it leaves $V_2$. Its dimension is $2 \cdot 2 + 1 = 5$, the [spin-$2$ entry](#ex:spin-labels-su2) of the dimension table, and $1 + 5 = 6 = \binom{4}{2}$. $\square$

**Scope of the proof.** The Clebsch–Gordan decomposition is not proved here. It enters as a definition: the index set of $k \le 2j$ with $k \equiv 2j \pmod 2$. On this index model four facts are proved: the singlet index $0$ occurs for $2j = 2$; removing it leaves exactly the index $2$; that index carries the spin label $2j = 4$; and the dimensions sum to $6 = 1 + 5$.
