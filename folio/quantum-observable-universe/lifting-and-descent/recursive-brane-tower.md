Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe over a ring $R$. Set $A_0 = A$ and inductively $A_{n+1} = J^1(A_n) = (A_n \otimes A_n)/I_n^2$, the [jet object](#def:categorical-jet) of $A_n$, where $I_n = \ker(m\colon A_n \otimes A_n \to A_n)$.

The **recursive brane tower** is the sequence
$$
  A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots
$$
in $\mathbf{C}$, where each embedding is the section $\ell_n(a) = [a \otimes 1]$ of $A_n \hookrightarrow J^1(A_n) = A_{n+1}$. The retraction $r_n\colon A_{n+1} \to A_n$ induced by $m$ satisfies $r_n \circ \ell_n = \mathrm{id}$, so each level is a direct summand of the next, with complement $I_n/I_n^2 = \Omega^1_{A_n/R}$ ([direct-summand lemma](#lem:jet-prolongation-categorical-jet)).

The *brane relation* makes the structure recursive: each jet object $A_n$ is the base object — the *brane* — of $A_{n+1}$, and the comultiplication $\Delta_n$ on $A_n$ encodes the $n$-th level connection, inherited via jet prolongation.
