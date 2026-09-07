Fix the **shortlex order** on words in the generators induced by $\sigma_1 < \sigma_2 < \cdots < \sigma_{n-1}$. The **Hecke normal form** of an element $h \in H_n(R, q)$ is a representative obtained by iterated application of three rewriting rules, each of which sends a word to shortlex-smaller words:

1. Hecke relation: $\sigma_i^2 \to (q - q^{-1})\sigma_i + \mathbf{1}$.
2. Far commutativity: $\sigma_i \sigma_j \to \sigma_j \sigma_i$ for $i > j + 1$.
3. Yang--Baxter: $\sigma_{i+1} \sigma_i \sigma_{i+1} \to \sigma_i \sigma_{i+1} \sigma_i$.

Each rule strictly decreases the shortlex order, so the reduction terminates. The one-directional form of rule 2 is what makes this so: the symmetric form $|i - j| \geq 2$ applies to its own output and does not terminate.

**This reduction is not confluent, and the resulting normal form therefore depends on the rule order.** Rule 3 for $(\sigma_2, \sigma_3)$ and rule 2 for $(\sigma_3, \sigma_1)$ overlap over the word $\sigma_3 \sigma_2 \sigma_3 \sigma_1$, which reduces in one step to $\sigma_2 \sigma_3 \sigma_2 \sigma_1$ or to $\sigma_3 \sigma_2 \sigma_1 \sigma_3$ according to which rule is applied; no rule of the system applies to either result. This is proved in Lean, without hypotheses and without `sorry`, as `UGB.GrobnerShirshov.HeckeGS.NotAGSBasis.hecke_not_gs_basis_four`.

The failure is invisible in small cases: all 504 words of length at most 8 over $H_3$ reduce to a unique normal form whatever the order, and the first counterexample requires both $n \geq 4$ and length $\geq 4$.

The repair is to *complete* the system with the family
$$
\sigma_i \sigma_{i-1} \cdots \sigma_j \sigma_i \;\to\; \sigma_{i-1} \sigma_i \sigma_{i-1} \cdots \sigma_j \qquad (i > j),
$$
whose $i = j + 1$ case is rule 3 and whose first new instance $\sigma_3 \sigma_2 \sigma_1 \sigma_3 \to \sigma_2 \sigma_3 \sigma_2 \sigma_1$ rewrites one of the two words above, dissolving the overlap. The corresponding statement for Coxeter *groups* is due to Bokut and Shiao \cite{bokut2001}; the $q$-deformed type-$A$ statement is due to Kang, Lee, Lee and Oh \cite{kang2002}, and the analogous completion for the Temperley--Lieb quotient — two further families beyond the defining relations — is Proposition 3.1 of \cite{kimlee2018}. Until that completion is carried out here, the normal form is *defined* by a fixed rule order rather than characterised by the reduction.

Modulo this, the basis elements correspond bijectively to the symmetric group $S_n$. Computationally, the reduction may be evaluated by directed Kashiwara crystal traversal rather than by S-polynomial overlap analysis.
