*Proof.*

1. *Compute the normal form $T_w \in H_{n(K)}(q)$ via Gröbner–Shirshov reduction ([hecke normal form](#def:hecke-normal-form)). This terminates in finite time by the Diamond Lemma.*
2. *Compute the confinement level ([confinement level](#def:confinement-level)) $\ell(K, q)$. Sort the finite set of shadow prices and find the smallest $\ell$ such that $T_w \in J^\ell(q)$.*
3. *Construct the LP-dual constraint matrix $\mathrm{G}(q) \in R^{N \times N}$, where $N$ is the number of primitive operators in $J^{\ell(K, q)}(q)$. This set is finite by [confinement-level-exists](#prop:confinement-level-exists).*
4. *Read off the coefficient vector $x(K, q)$ of $T_w$ in the primitive basis, check that it lies in $\mathbb{Z}_{\geq 0}^N$, and evaluate the $N$ coordinates of $\mathrm{G}(q)\,x(K, q)$. Over a ring with decidable order this is a finite computation.*

*Each step is decidable. Their composition is decidable.* $\square$

**Complexity.**
*The bottleneck is step 1, the normal-form reduction. Step 4 is one matrix-vector product of size $N$. No integer-programming search is needed, because the vector being tested is fixed by $T_w$.*
