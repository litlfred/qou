*Proof.* We exhibit $G$ as the quadratic kernel via three identifications.

**Step 1: LP-duality quadratic form.** The operator-selection LP
([`prop:operator-selection-lp`](#prop:operator-selection-lp))
minimises a *linear* objective $\sum_\lambda t_\lambda x_\lambda$
subject to a *quadratic* feasibility region defined by Frobenius
positivity $\sum_\mu G_{\lambda\mu} x_\mu \geq 0$. The associated
Lagrangian (in the optimisation sense) at the optimum has the form
$$
  \mathcal{L}_{\mathrm{LP}}(x; y)
  \;=\;
  \sum_\lambda t_\lambda x_\lambda
  - \sum_{\lambda, \mu} y_\mu G_{\lambda\mu} x_\lambda
  + y_0\!\left(\sum_\lambda x_\lambda - n_{\mathrm{target}}\right).
$$
The bilinear coupling $\sum_{\lambda,\mu} G_{\lambda\mu} y_\mu x_\lambda$
between primal and dual variables IS the Frobenius Gram matrix
$G_{\lambda\mu}$. It is the *single* quadratic form in the LP
formulation, and the unique quadratic kernel that arises from the
trace-induced geometry of $\widehat{A}_q$.

**Step 2: GNS inner-product identification.** On the GNS Hilbert
space $\mathcal{H}$ ([`prop:algebraic-gns-embedding`](#prop:algebraic-gns-embedding)),
the inner product is
$$
  \langle [a], [b] \rangle_{\mathcal{H}}
  \;:=\;
  \mathrm{tr}_M(a^* b).
$$
For the basis $\{b_\lambda\}$ chosen self-adjoint (the standard
Wedderburn idempotent basis), this gives
$\langle b_\lambda, b_\mu \rangle_{\mathcal{H}} = \mathrm{tr}_M(b_\lambda
b_\mu) = G_{\lambda\mu}$. So $G$ is the metric tensor on $\mathcal{H}$
restricted to the Wedderburn basis — the natural inner-product
kernel of the operator algebra.

**Step 3: Quadratic-action form.** A general functional $S(\rho)$
with kernel $K$, $S(\rho) = \sum_{\lambda,\mu} K_{\lambda\mu}
\rho_\lambda \rho_\mu$, with $\rho_\lambda$ a measure on
$\widehat{A}_q$, has continuum lift
$\iint K(x, y) d\rho(x) d\rho(y)$ where $K(x, y)$ is the
$\widehat{A}_q$-indexed kernel evaluated at the spectral data of
$x$ and $y$.

For $K = G$, the kernel $G(x, y) = \mathrm{tr}_M(x \cdot y)$ is the
trace of the operator product — a bilinear function of $x$ and
$y$, evaluable at any pair $(x, y) \in H_\infty(q) \times H_\infty(q)$
without reference to a specific basis. The basis-independent
form is
$$
  G(x, y) \;=\; \mathrm{tr}_M(x \cdot y),
$$
and the quadratic-action form is
$$
  S_{\mathrm{QOU}}(\rho)
  \;=\;
  \iint \mathrm{tr}_M(x \cdot y)\,d\rho(x)\,d\rho(y)
  \;=\;
  \mathrm{tr}_M\!\left(
    \int x\,d\rho(x) \;\cdot\;
    \int y\,d\rho(y)
  \right),
$$
the Markov trace of the squared first moment of $\rho$.

**Step 4: Uniqueness.** Any other candidate quadratic kernel on
QOU's pre-Archimedean side would be a different bilinear form on
$H_\infty(q) \times H_\infty(q)$. By the cyclic property of
$\mathrm{tr}_M$, any tracial bilinear form factors through the
Hilbert–Schmidt inner product — i.e., through $G$. Therefore $G$
is the *unique* tracial quadratic kernel up to scalar normalisation.
This justifies calling it *the* natural QOU continuum kernel for
comparison with CFS.

$\square$
