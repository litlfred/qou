Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$, and let
$p \colon \mathbf{1} \to A$ be a
([categorical point](#def:categorical-point)).  Let
$\alpha$ be a ([fermion](#def:fermion-boson-decomposition)) with germ
$\alpha_p \in A / \mathfrak{m}_p^2$.
Consider two independent observations at $p$,
$\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p} \colon A / \mathfrak{m}_p^2 \to A / \mathfrak{m}_p^2$
([observation](#def:observation)).  These data
assemble into a *parallelogram of observations at $p$*:

```tex
\begin{equation}\label{eq:observation-parallelogram}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  & \mathfrak{O}_{1,p}(\alpha_p) \arrow[dr, "\text{compare}"] & \\
  \alpha_p \arrow[ur, "\mathfrak{O}_{1,p}"]
           \arrow[dr, "\mathfrak{O}_{2,p}"']
  & & \delta\alpha_p \\
  & \mathfrak{O}_{2,p}(\alpha_p) \arrow[ur, "\text{compare}"'] &
\end{tikzcd}
\end{equation}
```

The discrepancy is the *commutator of observations at $p$*:

$$
  [\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p}](\alpha_p)
  = 
  \mathfrak{O}_{1,p}(\mathfrak{O}_{2,p}(\alpha_p))
  - \mathfrak{O}_{2,p}(\mathfrak{O}_{1,p}(\alpha_p)).
$$

Each observation perturbs the substrate parameter at $p$ by
$\delta q_i(p)$ ([observation](#def:observation), condition (2)),
inducing shifted parameters $q_1'(p) = q(p) + \delta q_1(p)$
and $q_2'(p) = q(p) + \delta q_2(p)$.  The commutator
$[q_1'(p), q_2'(p)]$ measures the obstruction:

$$
  [\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p}](\alpha_p)
  = 
  [q_1'(p), q_2'(p)] \cdot (\alpha_V)_p.
$$

This vanishes if and only if $[q_1'(p), q_2'(p)] = 0$ (the shifted
parameters commute at $p$) or $(\alpha_V)_p = 0$ (the particle is a
boson at $p$).  Generically, the non-cocommutativity of the Hopf
structure ensures $[q_1'(p), q_2'(p)] \neq 0$: independent
observations of a fermion at the same point necessarily disagree.

**Why germs, not global morphisms.**
The categorical algebra $A$ carries no intrinsic topology (it is an
object in $\mathbf{C}$, not a topological ring).  Working with germs
$A / \mathfrak{m}_p^2$ at a point $p$ plays the role of localisation:
it captures the first-order jet of the observation without requiring a
topology on $A$.  In the archimedean realisation
([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), where
$A = C^{\infty}(M)$, germs at $p$ recover the usual smooth germs
$C^{\infty}_p(M) / \mathfrak{m}_p^2$.
