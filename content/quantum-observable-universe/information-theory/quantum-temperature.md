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
  \;=\; \frac{\partial S_q}{\partial \mathbf{E}_q}\bigg|_V
  \;=\; \frac{1}{\hbar_q}.
$$
