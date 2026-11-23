**Lemma.** *Let $R$ be a field and $\varpi \in R$. Put*

$$
M_\varpi = \begin{pmatrix} 1 & \varpi \\ -1 & \varpi \end{pmatrix}, \qquad C_0 = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}.
$$

*Then*

1. *$M_\varpi = C_0 \, \mathrm{diag}(1, \varpi)$;*
2. *$\det M_\varpi = 2\varpi$;*
3. *$M_\varpi^{\mathsf T} M_\varpi = \mathrm{diag}(2,\, 2\varpi^2)$, so the columns of $M_\varpi$ are orthogonal for the standard bilinear form;*
4. *$(\operatorname{tr} M_\varpi)^2 - 4 \det M_\varpi = \varpi^2 - 6\varpi + 1$.*

*If moreover $\varpi \neq 0$, the Möbius map of $M_\varpi$,*

$$
\mu_\varpi(t) = \frac{t + \varpi}{-t + \varpi},
$$

*sends $-\varpi \mapsto 0$ and $0 \mapsto 1$, and has its pole at $t = \varpi$.*

*Proof.* Each item is a direct $2 \times 2$ computation. For (1), $C_0 \, \mathrm{diag}(1,\varpi)$ scales the second column of $C_0$ by $\varpi$. For (2), $\det M_\varpi = \varpi - (-\varpi) = 2\varpi$. For (3), the columns $(1,-1)$ and $(\varpi,\varpi)$ have squared lengths $2$ and $2\varpi^2$ and inner product $\varpi - \varpi = 0$. For (4), $\operatorname{tr} M_\varpi = 1 + \varpi$, so $(1+\varpi)^2 - 8\varpi = \varpi^2 - 6\varpi + 1$. The values of $\mu_\varpi$ follow by substitution. $\square$

The statement holds over any field; it is formalised over a generic field in the Lean sibling, with $2 \neq 0$ assumed only for the invertibility corollary $\det M_\varpi \neq 0$.
