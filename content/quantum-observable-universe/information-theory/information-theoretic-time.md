*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Definition.**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with braiding-induced ordering $\prec_c$
([ordering–jet compatibility](#prop:ordering-jet-compatibility)),
and let $f_q(z) = z^2 + c(q)$ be the Julia set iteration on the
exceptional divisor
([Julia set of Reeb flow](#rem:julia-set-reeb)).

The **information-theoretic time** at substrate parameter $q$ is
the cumulative Reeb operation count

$$
  \mathcal{T}(q)  :=  \sum_{n=0}^{N-1} 1
  =  N
$$

where $N$ is the total number of iterations of $f_q$ applied
since a reference configuration $\mathcal{S}_0$
([bundle initial conditions](#def:bundle-initial-conditions)).
Each iteration advances the admissible ordering by one step:
$\mathcal{T}$ counts the position in the braiding-induced ordering $\prec_c$
propagated through the jet tower.
