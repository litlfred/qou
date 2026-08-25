**Remark.**
*This proposition is the formal justification for a default-coarse computational strategy across the full confinement category. The hierarchy has at least four relevant levels:*

| *Level $\ell$* | *Confined particle* | *Default strand count $n_0$* |
|---|---|---|
| *0* | *quark* | *1* |
| *1* | *nucleon (proton, neutron)* | *3 (quark-strands)* |
| *2* | *atom / nucleus* | *$A$ (nucleon-strands)* |
| *3* | *compound / molecule* | *# atoms* |

*At each level, any trace-class invariant is exact at the coarsest representation satisfying $k_{\max}(P, q, n_0) \le n_0$.*

**Default-coarse rule.**
*Every computational pipeline executes the following steps:*

1. *Identify the confined particle $P$ at its natural level $\ell$.*
2. *Read $k_{\max}(P, q, n_0)$ from the witness data.*
3. *If $k_{\max}(P, q, n_0) \le n_0$, compute $\mathrm{tr}_M$ at the coarse level and halt.*
4. *If $k_{\max}(P, q, n_0) > n_0$, apply the unfolding morphism $\uparrow_\ell$ and repeat at $\ell - 1$.*

**Unfolding triggers.**

- ***Magic shell closure.*** *Atoms at $A \in \{2, 8, 20, 28, 50, 82, 126\}$ and noble-gas electron counts $Z \in \{2, 10, 18, 36, 54, 86\}$ exhibit binding multiplicity $\mu(S, q) \ge 2$. This forces $k_{\max}$ above the coarse count. Atoms in these rows evaluate one level deeper.*
- ***SDP cross-channel demand.*** *The active dual support $\mathcal{S}^*$ of the confinement SDP spans blocks $\lambda_1, \lambda_2$. When $\max(|\lambda_1|, |\lambda_2|) > n_0$, the coarse representation cannot express the coupling. Unfolding is required.*

*Non-magic atoms and molecules without SDP cross-channel demand evaluate at their natural coarse level. This is the minimal exact representation.*

**Dressing preserves computational minimality.**
*Under the dressing morphism $\mathrm{dress}_S: P_{\mathrm{bare}} \to P_{\mathrm{dressed}}$, the witnessed truncation updates to*

$$
  k_{\max}(P_{\mathrm{dressed}}, q)
  \;=\;
  \max\bigl(k_{\max}(P_{\mathrm{bare}}, q),\;
            k_{\max}^{\mathrm{bind}}(S, q)\bigr),
$$

*where $k_{\max}^{\mathrm{bind}}$ is the partition reach of the binding subword $W_{\mathrm{bind}}$. The dressed particle's computational level follows from the updated $k_{\max}$. Adding a single electron to a non-magic atom typically leaves the computational level unchanged. Closing to a noble gas triggers $\mu \ge 2$ and raises the required level.*

**Computational implication.**
*For a non-magic atom with $A$ nucleons, the Hecke algebra dimension drops from $|H_{3A}(q)| = (3A)!$ to $|H_A(R, q)| = A!$. Partition enumeration drops from $p(3A)$ to $p(A)$. Default-coarse computation is the computational content of this proposition applied via the confinement category.*
