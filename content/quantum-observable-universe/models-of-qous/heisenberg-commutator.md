> *Science no longer is in the position of observer of nature, but
> rather recognises itself as part of the interplay between man and
> nature.  The scientific method \ldots\ can no longer keep its distance
> from the object.*
>
> --- Werner Heisenberg, *Physics and Philosophy* (1958) \cite{heisenberg1958}

The Heisenberg uncertainty principle emerges as a *fibre coordinate
measurement*.  Let $\hat{X}, \hat{P}$ be position and momentum
observables on the fibre $\mathbb{P}^1(\mathbb{C})$, and let
$J \colon H \to H$ be the complex structure on the Levi distribution
($J^2 = -\mathrm{Id}$; throughout this paper $i$ is identified with
the action of $J$ on horizontal planes).  The substrate parameter $q \in \mathrm{End}(\mathbf{1})$
([substrate parameter](#def:substrate-parameter)) parametrises the
categorical interpolation family between $d$ and $\pi_V \circ d$;
the quantum Planck constant
$\hbar_q = 1 - q^{-1}$
([quantum Planck constant](#def:quantum-planck-constant)) measures
displacement along this fibre.  The $q$-deformed commutator at
$p \in M$ is

$$
  [\hat{X}, \hat{P}]_q := J\hbar_q(p),
  \qquad \hbar_q(p) = 1 - q(p)^{-1}.
$$

As $q \to 1$, $[\hat{X}, \hat{P}]_q \to 0$ (classicality: one sits at
the base of the Reeb fibre, where $d_q = d$); as $q \to \infty$,
$[\hat{X}, \hat{P}]_q \to J$ (maximal uncertainty: one sits at the tip
of the fibre, where $d_q \to \pi_V \circ d$).

Geometrically, $[\hat{X}, \hat{P}]_q$ equals $\varTheta(\xi_q)$, the
$q$-deformed Reeb field
([$q$-Reeb vector field](#ex:q-reeb-vector-field)) evaluated on the
contact form: $\xi_q$ is the unique direction along which $d\varTheta$
degenerates, so it encodes the obstruction to commutativity.
Uncertainty is displacement along the Reeb fibre --- the further from
classicality ($q = 1$), the larger the non-commutativity.  Heisenberg's
observation that the observer is ``part of the interplay'' is here made
precise: the observer's position in the fibre (the value of $q$)
determines how much the observables fail to commute.
