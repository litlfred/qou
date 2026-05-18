**Definition.**
*Let $K$ be an atom-knot ([atom](#def:atom-knot)) with NF
$T_w \in H_{n(K)}(q)$.  Let $G(q)$ be the Frobenius Gram matrix
of the primitive Wedderburn-block operators
$\{e_\lambda\}_{\lambda \vdash k,\;k \leq k_{\max}}$
([mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)).
Decompose the NF in the primitive basis:*

$$
  T_w
  \;=\;
  \sum_\lambda x_\lambda \cdot e_\lambda,
  \qquad
  x_\lambda \in \mathbb{Z}_{\geq 0}.
$$

*The atom $K$ is **stable at $q$** iff this decomposition admits
an **ILP** (integer linear program) solution:*

$$
  \exists\, x \in \mathbb{Z}_{\geq 0}^N
  \;\text{such that}\;
  G(q) \, x \;\geq\; 0
  \;\text{coordinatewise.}
$$

*That is, the Frobenius positivity constraint $(Gx)_\gamma \geq 0$
holds for every primitive constraint $\gamma$ with $x$ a
nonnegative integer vector.*

**Independence of neighborhood.**
*Stability is a **fixed-$q$** property — it does NOT require the
ILP to be feasible on a neighborhood of $q$.  An atom may be
stable at $q_0$ and unstable at $q_0 + \epsilon$ without
contradiction: stability tracks ILP-feasibility pointwise.*

**Connection to LP-feasibility.**
*The continuous LP relaxation
($x \in \mathbb{R}_{\geq 0}^N$, $G(q) x \geq 0$) is always
feasible (the trivial identity NF $T_e = e_{(k)}$ has
$y_{(k)} = 0$).  The ILP version is strictly stronger:
the proton derivation in
[mass-endomorphism-tower](#prop:mass-endomorphism-tower) shows
that the $9$-crossing element
$\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$
violates Frobenius positivity (LP-infeasible at integer values),
and ILP search adjoining $\{\sigma_0, \sigma_1, L_+, L_-\}$
finds the unique integer solution
$\sigma_0 \to \sigma_0$ ($2$ gluon crossings) restoring stability.*

**Confined operators only.**
*The ILP is solved within the confinement filtration
([confinement level](#def:confinement-level)) at $q$: we only
consider primitives $e_\lambda$ in $J^{\ell(K, q)}(q)$, since
operators above the atom's confinement level are not available
without further phase transitions.*
