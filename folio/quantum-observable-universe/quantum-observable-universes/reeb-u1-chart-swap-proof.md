The argument is the routine identification "$T_q$-orbits on the
projective quotient are unique up to reparameterisation".

**Step 1: $T_q$ acts canonically on $\mathbb{P}(V)$.** The
projective-line object $\mathbb{P}(V) = G_q / T_q$ is, by
construction, the quotient of $G_q$ by the right action of $T_q$.
The residual *left* $T_q$-action on $G_q$ descends to a well-defined
$T_q$-action on the quotient, yielding a canonical homomorphism
$T_q \hookrightarrow \mathrm{Aut}_{\mathbf{C}}(\mathbb{P}(V))$. The
image is a one-dimensional connected subgroup, hence a $U(1)$.

**Step 2: the Reeb flow factors through this $T_q$.** By
construction ([Constructive Reeb derivation on Bring's coordinate
ring](#ex:categorical-reeb-brings)), the Reeb generator
$\xi = e_3 \in \mathfrak{su}(2)$ is the infinitesimal generator of
the maximal torus $T_q \subset G_q$. The one-parameter group
$\phi_t = \exp(t \xi) \subset G_q$ is therefore exactly $T_q$
(as a real one-parameter group). Its induced action on
$\mathbb{P}(V) = G_q / T_q$ is the standard $T_q$-action of Step 1.
Hence $\langle \phi_t \rangle = T_q \subset \mathrm{Aut}_{\mathbf{C}}(\mathbb{P}(V))$.

**Step 3: the chart-swap factors through the same $T_q$.** By
[affine-chart origin of $i$ and $q$](#rem:affine-chart-origin-of-i-and-q),
the chart-swap family
$\rho_\varTheta : Z \mapsto e^{i\varTheta} Z$
on the affine coordinate $Z$ of the
[contact affine chart](#def:contact-affine-chart) is the
$U(1)$ acting on $\mathbb{P}(V)$ by scaling the standard affine
chart at $0$. This scaling is, by construction of the projective
quotient $\mathbb{P}(V) = G_q / T_q$, the induced left $T_q$-action
of Step 1 (the $T_q$-grading on the affine coordinate $Z$ has weight
$-1$ for $Z = y x^{-1}$, hence $T_q$ scales $Z$ by a phase). Hence
$\langle \rho_\varTheta \rangle = T_q \subset \mathrm{Aut}_{\mathbf{C}}(\mathbb{P}(V))$.

**Step 4: conclusion.** Both subgroups equal $T_q$ by Steps 2–3, so
they are equal as subgroups of $\mathrm{Aut}_{\mathbf{C}}(\mathbb{P}(V))$.
$\square$

**Explicit parameterisation (corollary).** The two parameterisations
differ only by a scale and sign determined by SU(2) conventions. With
$\xi = e_3 = \tfrac{1}{2}\mathrm{diag}(1, -1)$ and $Z = y x^{-1}$
($x$ weight $+\tfrac{1}{2}$, $y$ weight $-\tfrac{1}{2}$, so $Z$ has
$T_q$-weight $-1$), the flow acts as

$$
  \phi_t \cdot Z  =  e^{-t}\, Z  =  \rho_{i t}(Z)
  \qquad (\text{equivalently } \varTheta = i\,t),
$$

consequently the chart-swap parameter $\varTheta$ and the Reeb parameter $t$
are related by Wick rotation $\varTheta = i\,t$ (real Reeb time
$\leftrightarrow$ imaginary chart-swap angle, recovering the
Bargmann–Hall–Wightman forward-tube reading).
