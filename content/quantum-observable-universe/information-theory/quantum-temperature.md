> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](../braids-and-knots/rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$ and Planck time
$t_P(q) = q/(q-1) = 1/\hbar_q$
([Planck time](#def:planck-time)).  The **quantum temperature**
of a region $U \subset M$ is

$$
  T_q(U) \;:=\; \hbar_q \;=\; \frac{q - 1}{q},
$$

with inverse temperature $\beta_q := 1/T_q = t_P(q)$.

In terms of the substrate density $\rho_q = 1/\hbar_q^{2}$
introduced by the Kashaev volume--density reading
([Kashaev volume--density](#rem:kashaev-volume-density)), the
temperature and its inverse square are

$$
  T_q \;=\; \rho_q^{-1/2},
  \qquad
  \beta_q^{2} \;=\; \rho_q.
$$

Temperature and substrate density are thus **conjugate square roots**:
a state at high drag density (small $\hbar_q$) is at low temperature,
and the inverse-temperature squared is the density itself.  This
absorbs several dimensional-analysis identities that otherwise require
separate derivation.

The quantum entropy of $U$ is the non-abelian surface integral

$$
  S_q(U) \;:=\; -\,\mathrm{tr}_{\mathrm{Ad}}
  \!\oint_{\partial U}
  \omega_{\mathcal{F}} \,\wedge\, *\eta_q,
$$

where $\mathcal{F} = \mathrm{Ad}(A)$ is the adjoint bundle,
$\omega_{\mathcal{F}}$ is the adjoint connection,
$\eta_q = (2q-1)/q^3$ is the operational entropy density
([operational entropy](#def:operational-entropy)),
and $*$ is the Hodge star on $\partial U$.

The measurability conditions $c_1(\mathcal{F}) = 0$,
$c_2(\mathcal{F}) = 0$
([quantum observable universe](#def:quantum-observable-universe))
ensure that the surface integral is independent of the choice
of bounding surface via the Yekutieli non-abelian Stokes
theorem ([Yekutieli triple](#def:yekutieli-triple)).

The quantum temperature is the thermodynamic conjugate:

$$
  \frac{1}{T_q}
  \;=\; \frac{\partial S_q}{\partial \mathfrak{E}_q}\bigg|_V
  \;=\; \frac{1}{\hbar_q}.
$$
