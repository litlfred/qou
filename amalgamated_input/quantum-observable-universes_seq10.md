<!-- FILE_START: intro-heisenberg-commutator.md -->
The Heisenberg commutator
$[\hat{p}, \hat{q}] = -i\hbar$ — the substrate-level signature of
quantum non-commutativity — emerges in the QOU framework from the
fibre structure of $\mathcal{S}$ rather than as a postulated
canonical relation.  This short section proves the substrate
Heisenberg commutator as a structural identity (uses the
$q$-Planck constant defined upstream) and exhibits the
non-commutative drag that the categorical commutator imparts on
mass-spectrum predictions.
<!-- FILE_END: intro-heisenberg-commutator.md -->

<!-- FILE_START: q-deformed-commutator.md -->
Let $\hat{X}, \hat{P}$ be the position and momentum observables on the
fibre $\mathbb{P}^1(\mathbb{C})$, let $J \colon H \to H$ be the complex
structure on the Levi distribution ($J^2 = -\mathrm{Id}$), and let
$q \in \mathrm{End}(\mathbf{1})$ be the substrate parameter
([substrate parameter](#def:substrate-parameter)).  The
**$q$-deformed commutator** of $\hat{X}$ and $\hat{P}$ at a point
$p \in M$ is

$$
  [\hat{X}, \hat{P}]_q := J\,\hbar_q(p),
  \qquad \hbar_q(p) = 1 - q(p)^{-1},
$$

where $\hbar_q$ is the quantum Planck constant
([quantum Planck constant](#def:quantum-planck-constant)).
<!-- FILE_END: q-deformed-commutator.md -->

<!-- FILE_START: heisenberg-commutator-prop.md -->
Let $[\hat{X}, \hat{P}]_q = J\hbar_q(p)$ be the $q$-deformed commutator
([$q$-deformed commutator](#def:q-deformed-commutator)) of the fibre
observables $\hat{X}, \hat{P}$ on $\mathbb{P}^1(\mathbb{C})$, with
$\hbar_q(p) = 1 - q(p)^{-1}$ the quantum Planck constant
([quantum Planck constant](#def:quantum-planck-constant)).  Then the
commutator interpolates between the classical and maximally-uncertain
regimes:

1. As $q \to 1$, $[\hat{X}, \hat{P}]_q \to 0$ (classical limit,
   $\hbar_q \to 0$).
2. As $q \to \infty$, $[\hat{X}, \hat{P}]_q \to J$ (maximal
   uncertainty, $\hbar_q \to 1$).
<!-- FILE_END: heisenberg-commutator-prop.md -->

<!-- FILE_START: heisenberg-commutator.md -->
> *Science no longer is in the position of observer of nature, but
> rather recognises itself as part of the interplay between man and
> nature.  The scientific method \ldots\ can no longer keep its distance
> from the object.*
>
> --- Werner Heisenberg, *Physics and Philosophy* (1958) \cite{heisenberg1958}

The Heisenberg uncertainty principle emerges as a *fibre coordinate
measurement*.  The $q$-deformed commutator
$[\hat{X}, \hat{P}]_q = J\hbar_q(p)$
([$q$-deformed commutator](#def:q-deformed-commutator)) measures
displacement along the Reeb fibre: the complex structure
$J \colon H \to H$ on the Levi distribution ($J^2 = -\mathrm{Id}$;
throughout this paper $i$ is identified with the action of $J$ on
horizontal planes) supplies the imaginary unit, and the quantum
Planck constant $\hbar_q = 1 - q^{-1}$
([quantum Planck constant](#def:quantum-planck-constant)) measures the
displacement itself.  The substrate parameter
$q \in \mathrm{End}(\mathbf{1})$
([substrate parameter](#def:substrate-parameter)) parametrises the
categorical interpolation family between $d$ and $\pi_V \circ d$.

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
<!-- FILE_END: heisenberg-commutator.md -->

