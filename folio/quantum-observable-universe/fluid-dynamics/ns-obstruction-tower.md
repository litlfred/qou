**Proposition (conditional collision-locus criterion;
"NS obstruction tower").**

Let $(\mathbf{C}, A, \tau)$ be a QOU carrying Euler characteristic $\chi(A)$ and [obstruction classes](#def:quantum-characteristic-classes) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$, and let $\Sigma \subset \mathcal{S}$ be a posited collision locus with restriction map

$$
  \mathrm{Obs}_\partial(A)
  = 
  \ker\!\left(
    \bigoplus_{n \geq 0}
    H^2(\mathcal{S}, \mathcal{B})
    \xrightarrow{ \mathrm{res}_\Sigma}
    \bigoplus_{n \geq 0}
    H^2(\Sigma, \mathcal{B}|_\Sigma)
  \right).
$$

Assuming the sufficiency and necessity hypotheses linking singular behaviour to a non-vanishing restricted class, singular behaviour holds if and only if $\mathrm{res}_\Sigma(\kappa_n) \neq 0$ for at least one $n$. However, when $\Sigma \subset \mathcal{S}$ is a one-dimensional curve, $H^2(\Sigma, \mathcal{F}) = 0$ for every sheaf $\mathcal{F}$, so $\mathrm{res}_\Sigma(\kappa_n) = 0$ identically for all $n$; the non-degenerate topological invariant of the surface is therefore the global Euler class $\mathrm{NS}(A) = e(\xi) \in H^2(\mathcal{S}, \mathbb{Z})$ of [NS-regular QOU](#def:ns-regular-qou) rather than its curve restriction.

**Proof and cohomological scope.**

**(a) Global surface class vs.\ tower bands.**

By the [QU-to-QOU theorem](#thm:qu-to-qou), the base discrete-band obstruction of the Reeb $\mathrm{U}(1)$-bundle $\xi$ is $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{Z})$ of degree $\chi(\mathcal{S}) = \chi(A)$. In the Kummer filtration $1 \to \mu_n \to \mathrm{U}(1) \xrightarrow{(\cdot)^n} \mathrm{U}(1) \to 1$, the $n$-th-root obstruction $\chi(\mathcal{S}) \bmod n \in H^2(\mathcal{S}, \mu_n)$ vanishes if and only if $n \mid \chi(\mathcal{S})$. On a closed complex curve $\mathcal{S}$ (such as Bring's surface $\Sigma_4$), $H^2(\mathcal{S}, \mathcal{O}_{\mathcal{S}}) = 0$ and $H^2(\mathcal{S}, \mathcal{O}_{\mathcal{S}}^{\times}) = 0$, so sheaf-cohomological jet corrections $\delta_n \in \mathrm{im}\bigl(H^2(\mathcal{S}, \mathcal{O}_{\mathcal{S}}) \to H^2(\mathcal{S}, \mathcal{B})\bigr)$ vanish identically.

**(b) Vanishing on a one-dimensional collision curve.**

Consider the long exact sequence of the pair $(\mathcal{S}, \mathcal{S} \setminus \Sigma)$:

$$
  \cdots \to
  H^1(\mathcal{S} \setminus \Sigma, \mathcal{B})
  \xrightarrow{\partial}
  H^2_\Sigma(\mathcal{S}, \mathcal{B})
   \to 
  H^2(\mathcal{S}, \mathcal{B})
  \xrightarrow{ \mathrm{res}_{\mathcal{S}\setminus\Sigma}}
  H^2(\mathcal{S} \setminus \Sigma, \mathcal{B})
  \to \cdots
$$

The sequence restricts to the complement $\mathcal{S} \setminus \Sigma$ (detecting local-cohomology support in $H^2_\Sigma(\mathcal{S}, \mathcal{B})$), whereas the direct restriction $\mathrm{res}_\Sigma \colon H^2(\mathcal{S}, \mathcal{B}) \to H^2(\Sigma, \mathcal{B}|_\Sigma)$ lands in $H^2(\Sigma, \mathcal{B}|_\Sigma) = 0$ whenever $\Sigma$ is one-dimensional. Moreover, on a closed oriented surface $H^2_{\{p\}}(\mathcal{S}, \mathbb{Z}) \to H^2(\mathcal{S}, \mathbb{Z})$ is an isomorphism for every point $p$, so $e(\xi)$ alone does not single out a preferred curve $\Sigma$.

**(c) Local cohomology at an intersection point.**

Evaluating the [local cohomology](#def:local-cohomology-group) at $p \in \Sigma$ gives $H^1_{\mathfrak{m}_p}(A) = R^1\Gamma_{\mathfrak{m}_p}(A)$; in the two-filament model where each filament carries $V_{1/2}$ of $\mathrm{SU}_q(2)$, the local fibre at $p$ is $V_{1/2}^{(1)} \oplus V_{1/2}^{(2)}$.

**(d) Levi scalar on a three-dimensional flow domain.**

By the [core Levi form](#prop:core-levi-form), the Levi datum of the vorticity plane field in three dimensions is the single scalar $\xi\cdot\mathrm{curl}\,\xi$ rather than a pair of core-aspect-ratio eigenvalues, and no bridge from $\xi\cdot\mathrm{curl}\,\xi$ to $H^1_{\mathfrak{m}_p}(A)$ is established.

**(e) Consequence for the Descartes surface.**

On Bring's surface $\Sigma_4$ ($\chi(\Sigma_4) = -6$), the global surface invariant is $e(\xi) = -6 \in H^2(\Sigma_4, \mathbb{Z})$, while for every one-dimensional locus $\Sigma \subset \Sigma_4$ both $e(\xi)|_\Sigma = 0$ and $\delta_n|_\Sigma = 0$ in $H^2(\Sigma, \cdot) = 0$. The conditional equivalence therefore reduces to two false predicates unless the target group is replaced by a global or relative cohomology group. $\square$
