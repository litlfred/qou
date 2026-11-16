*Let $A = H_n(R, q)$ be a self-dual Frobenius algebra with Markov trace $\tau$, and suppose $\tau(p_\lambda) \neq 0$ for every central idempotent $p_\lambda$. The quantum-co-dimension element*

$$
  C_{\dim_q}
  \;:=\;
  \sum_{\lambda \in \widehat{A}}
    \frac{1}{\dim_q(\lambda) \cdot \tau(p_\lambda)}
    \cdot p_\lambda
  \;\in\; Z(A)
$$

*lies in the centre of $A$ and satisfies*

$$
  \boxed{
    \tau\bigl(C_{\dim_q}\bigr)
    \;=\;
    \sum_{\lambda \in \widehat{A}} \frac{1}{\dim_q(\lambda)}.
  }
$$

**Scope under convention D.** The hypothesis $\tau(p_\lambda) \neq 0$ fails for $H_n(q)$ with $n \geq 3$ under convention D, $z = q^{3}/(q^{2}+1)$. There $\tau(p_\lambda) = y_\lambda\,d_\lambda$, and the Ocneanu weight $y_\lambda$ vanishes for every $\lambda$ with three or more rows, so $C_{\dim_q}$ is not defined. What survives is the element $C^{\circ}_{\dim_q}$ summed over $\widehat{A}^{\circ} = \{\lambda : \tau(p_\lambda) \neq 0\}$, with $\tau(C^{\circ}_{\dim_q}) = \sum_{\lambda \in \widehat{A}^{\circ}} 1/\dim_q(\lambda)$. The all-partition sum $\sum_{\lambda \vdash n} 1/\dim_q(\lambda)$ remains defined as a formal sum, but for $n \geq 3$ under convention D it is not $\tau$ of any element constructed here. In the block model $A = \prod_\lambda \mathrm{Mat}_{d_\lambda}$ with $\tau = \sum_\lambda y_\lambda d_\lambda \operatorname{Tr}$ over a generic field, Lean proves that $\operatorname{rad}\tau$ is exactly the sum of the dead blocks, that $C^{\circ}_{\dim_q}$ is central and its trace is independent of the lift from $A/\operatorname{rad}\tau$, and that once a block dies no central element $c$ has $\tau(c\,p_\lambda) = 1/\dim_q(\lambda)$ on every block (`QOU.MassTheory.CoCasimirSurviving.mem_traceRadical_iff`, `tr_of_lift`, `no_full_coCasimir`). Under convention D the surviving sum runs over the partitions with at most two rows (`tr_coCasimirSurv_conventionD`).
