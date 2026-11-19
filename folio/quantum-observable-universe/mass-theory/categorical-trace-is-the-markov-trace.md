The [trace ledger](#rem:trace-ledger) lists the rigid trace of an endomorphism and the Markov trace on the Hecke algebra as two operations. On the tensor representation they are one operation, and this remark says in what sense.

**The tensor representation.** Let $V$ be the fundamental object of $\mathrm{SU}_q(2)$, of quantum dimension $[2]_q = q + q^{-1}$. The braiding gives $B_n$, hence the Hecke algebra $H_n(q)$, an action on $V^{\otimes n}$; the generator $\sigma_i$ acts on the $i$-th and $(i{+}1)$-st factors by the $R$-matrix $\check{R}$, which in the Hecke normalisation satisfies $(\check R - q)(\check R + q^{-1}) = 0$. Every endomorphism $\rho(\beta)$, $\beta \in H_n(q)$, has a rigid trace in $\operatorname{End}(\mathbf{1}) = R$: close the strands with the evaluation and coevaluation of $V^{\otimes n}$. Since the coevaluation of a rigid braided category with a pivotal structure is weighted, the rigid trace is the *quantum trace*, $\mathrm{tr}(\rho(\beta)) = \operatorname{Tr}\bigl(K^{\otimes n} \rho(\beta)\bigr)$ with $K$ the pivotal element \cite{reshetikhin-turaev1990}; at $\beta = 1$ it returns $\dim_q(V^{\otimes n}) = [2]_q^{\,n}$.

**The identification.** Define $\tau_n(\beta) = \mathrm{tr}(\rho(\beta)) / [2]_q^{\,n}$. Then $\tau_n(1) = 1$; $\tau_n$ is cyclic because a trace is; and closing one generator gives, by direct computation on $V \otimes V$,

$$
  \tau_2(\sigma_1) \;=\; \frac{\operatorname{Tr}(K^{\otimes 2}\check R)}{[2]_q^{\,2}} \;=\; \frac{q^{3}}{q^{2} + 1} \;=\; z_D ,
$$

the Markov parameter of convention D. The Markov property $\tau_{n}(\beta \sigma_{n-1}) = z_D\, \tau_{n-1}(\beta)$ for $\beta \in H_{n-1}(q)$ follows by closing the last strand first: the partial quantum trace of $\check R$ over that strand is an endomorphism of $V$ commuting with the action, hence a scalar by Schur's lemma, and the one-generator computation identifies the scalar as $z_D\,[2]_q$. Hence $\tau_n$ is a Markov trace with parameter $z_D$, and by the uniqueness clause of the [Markov-trace selection proposition](#prop:markov-trace-frobenius-selection) it *is* $\mathrm{tr}_M^{z_D}$, the trace the framework uses \cite{jones1987}.

**The weights, read off.** Decompose $V^{\otimes n} = \bigoplus_{k} V_{n-2k} \otimes S_{(n-k,k)}$ over the two-row partitions, with $S_\lambda$ the irreducible $H_n(q)$-module of partition $\lambda$ (the quantum Schur–Weyl duality of $\mathrm{SU}_q(2)$). The quantum trace of $\rho(\beta)$ on this sum is $\sum_k \dim_q(V_{n-2k})\, \chi_{(n-k,k)}(\beta) = \sum_k [n-2k+1]_q\, \chi_{(n-k,k)}(\beta)$, so

$$
  \mathrm{tr}_M^{z_D} \;=\; \sum_{k} \frac{[n - 2k + 1]_q}{[2]_q^{\,n}}\, \chi_{(n-k,k)}, \qquad y_{(n-k,k)} = \frac{[n-2k+1]_q}{[2]_q^{\,n}}, \quad y_\lambda = 0 \text{ for } \ell(\lambda) \geq 3 ,
$$

which are the weights the proposition states. Two of the four traces of the ledger therefore coincide on the tensor representation, and the row cap of convention D is the statement that $V$ is two-dimensional: a partition with three rows has no room in $V^{\otimes n}$ \cite{kassel1995}.

**Scope of the rigid-trace identification.** It identifies the Markov trace with a rigid trace, and thereby with an evaluation of the [Chern character](#def:chern-character) of $V^{\otimes n}$ at the pivotal element, divided by $[2]_q^{\,n}$; the quantum dimensions $[m]_q$ in the weights are values of $\dim_q$ on the [Grothendieck group](#def:grothendieck-group-of-a-qou). It does not identify either trace with the Euler characteristic of the base curve, which is not a trace on $H_n(q)$ at all.
