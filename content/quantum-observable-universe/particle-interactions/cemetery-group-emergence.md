**Conjecture (cemetery group as a homological filter).**
*Let $T_w \in H_n(R, q)$ be a Hecke normal form and let $\beta$ be the corresponding crystal path. If the prefix $\beta_{\leq k}$ of $\beta$ lifts to a graded projective KLR module that lies in the cemetery group $\mathcal{Z}_n = \ker \tau$, then every extension of $\beta$ also lies in $\mathcal{Z}_n$, and its image under the observation functor vanishes:*

$$
  M_{\beta_{\leq k}} \in \mathcal{Z}_n
  \;\Longrightarrow\;
  \tau\bigl(M_{\beta_{\leq k} \cdot w'}\bigr) = 0
  \quad \text{for every continuation } w'.
$$

**Algorithmic role (kill switch).**
*The Gröbner–Shirshov engine uses $\mathcal{Z}_n$ as a dynamic pruning filter. At each crystal step, it tests whether the current state lies in the kernel of $\tau$. If so, the branch is dropped immediately, bypassing all downstream polynomial cancellations. This converts long chains of crossing-graded expansions into an $O(1)$ truncation step.*

**Relation to the spectral-sum cutoff.**
*This conjecture supplies the structural reason for the cutoff. The residue strata above the confinement level $\ell(K, q_0)$ correspond precisely to the crystal extensions that fall into $\mathcal{Z}_n$. They vanish under $\tau$ rather than via term-by-term cancellation.*

**Conjectural status.**
*The defining property of $\mathcal{Z}_n$ as the kernel of $\tau$ is true by construction. What is conjectural is monotonicity under crystal extensions. Monotonicity follows from the localising-Serre property of $\mathcal{Z}_n$ inside $\mathcal{K}_n$ together with the action of Kashiwara operators on graded projectives. Both are standard for KLR algebras. The residual content is the QOU-specific instantiation.*
