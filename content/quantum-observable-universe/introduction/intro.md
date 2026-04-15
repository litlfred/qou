We see colours — three of them mix to white.  We rotate, translate,
and boost, yet measurements remain invariant.  Time flows forward.
Multiple observers share one world, not private copies.  We
integrate, differentiate, and compute; the universe has volume.
Free will — the ability to choose what to measure — produces
outcomes not determined by initial conditions.

These observations, once stated precisely, determine a specific
algebraic structure: a *rigid monoidal category* equipped with a
fibre functor and a Frobenius trace $\int_A$.  We call this
structure a **quantum observable universe** (QOU).  Its axioms
encode the features listed above and nothing more.

An assumption this paper does *not* make is that the constants of
our universe are constant.  We allow them to vary — in a
controlled, algebraic way — and ask: what does that change?

We do not ask what the universe *is*; we ask what its mechanics
*do*.  Category theory is the natural language, because it
describes transformation without committing to ontology.  Noether's
principle converts observed symmetries into conserved quantities;
the Frobenius trace $\int_A$ is the categorical Noether current.
The $q$-deformation of the substrate shifts conservation laws from
exact identities to approximate ones, with anomalies that are
themselves measurable.

What follows from these axioms is broad in scope and specific in
detail.  The symmetry group $\mathrm{SU}_2(R)$ is not assumed; it
emerges via Tannaka–Krein reconstruction.  Particles are knots;
interactions are braid relations.  The capacity for computation is
a consequence, not an input.

The paper is organised as follows.

**Part I: Foundations.**
[Chapter 1](#chap:qu) introduces the **quantum universe** (QU):
a rigid monoidal category $\mathbf{C}$, a Frobenius–Hopf object
$A$, and a fibre functor $\tau$.  The Frobenius trace
$\int_A \colon A \to \mathbf{1}$ provides categorical integration;
combined with Kähler differentials on $A$, it provides
differentiation.  Self-duality $A \cong A^{\vee}$ ensures these
operations are compatible.  From these ingredients the chapter
derives the Frobenius relation, the dagger involution, and the
Tannaka–Krein reconstruction of the symmetry group.

[Chapter 2](#chap:qou) imposes three cohomological constraints —
observability, measurability, and volume — that promote the QU to
a **quantum observable universe** (QOU).  These constraints remove
unobservable hidden structures and bad behaviour.  Self-duality
within this constrained space forces the gauge group
$G = \mathrm{SU}_2(R)$ to emerge naturally, together with a
natural coordinate $q$, an ordering direction, and a strict genus
limitation of four on the state space.  The QOU is characterised
by the archimedean tuple

$$
  (\mathbf{C}, \theta, G, \mathcal{S}).
$$

A categorical Dirac operator $\mathcal{D}_\nabla$, forced by the
Frobenius–Hopf structure, decomposes into gravity (Ricci), gauge
(Yang–Mills), and matter terms — yielding the categorical action

$$
  \mathcal{S}_q[\nabla, \textstyle\int_A, \psi]
  = 
  \underbrace{\mathrm{tr}\bigl(q \cdot R_{\int}\bigr)}_{\text{gravity}}
  + 
  \underbrace{\textstyle\int_A \!\circ \mathrm{tr}_A\bigl(
    F_\nabla \wedge_q \star_q F_\nabla
  \bigr)}_{\text{gauge}}
  + 
  \underbrace{\textstyle\int_A\!\bigl(\psi^{\ast} \cdot \mathcal{D}_\nabla\psi\bigr)}_{\text{matter}},
$$

from which quantum versions of the Einstein, Yang–Mills, and Dirac
equations follow.

[Chapter 3](#chap:torsion) addresses the obstructions that arise
when local categorical data is extended globally.  The Yekutieli
lifting condition makes this precise: an object admits a lift if
and only if its obstruction class $\kappa(x) \in H^2(S, B)$
vanishes.  A key result is the Descartes condition $\chi(A) = -6$,
forced by the lifting obstructions and the Archimedean constraint.

**Part II: Structure.**
[Chapter 4](#chap:path-integrals-braiding) replaces continuum path
integrals with discrete braid-group computations.  Fundamental
particles — photons, electrons, protons — are defined purely
mathematically as specific knots and words on the genus-$4$ state
space.  Particle interactions are modelled through braid relations
by computing the Gröbner--Shirshov basis normal form of knot words using
Hecke relations, where the parameter $q$ tracks the energy cost of
each crossing.  The topological mass formula

$$
  \mathfrak{m}(K) =  \frac{\mathrm{Vol}(K)}{\hbar_q^{2}}
$$

acts as a Feynman path integral via the non-abelian Stokes formula,
but because the space is finite-dimensional it naturally avoids
standard infinities.  The embeddability bound on $\Sigma_4$ yields
exactly $7$ transfer matrices — six non-trivial force operators
and the identity (**interaction completeness**).  The volumes of
the hyperbolic knots that appear — $\mathrm{Vol}(4_1)$,
$\mathrm{Vol}(B_3)$, and others — encode the physical constants;
understanding the arithmetic relations between these volumes is a
question of independent interest.

[Chapter 5](#chap:models-qou) examines concrete realisations of
the QOU axioms: archimedean, $p$-adic, and finite-field models.

[Chapter 6](#chap:algebraic-substrate) develops the spectral theory
of the Frobenius–Hopf algebra.  The local $q$-zeta function of
Bring's curve encodes the Frobenius eigenvalues, and the
Hasse–Weil bound confines them to the critical line
$|\alpha_i| = q^{1/2}$.  The categorical machinery provides a
natural framing for classical questions in analytic number theory —
including the Riemann hypothesis, the Birch and Swinnerton-Dyer
conjecture \cite{birch1965}, and the Collatz problem — through the Kummer tower
associated to the Frobenius–Hopf algebra.

[Chapter 7](#chap:fluid-dynamics) explores the correlation between
the knot structures developed in earlier chapters and topological
fluid dynamics, offering an obstruction-based perspective on
Navier–Stokes regularity.

[Chapter 8](#chap:info-theory) examines the categorical framework
through the lens of information theory and computational
complexity.  The Gröbner--Shirshov basis makes computation *confluent*; the
Reeb flow generates a dynamical system whose boundary is a
Julia-set fractal.  The framework provides an interesting
perspective on questions such as P versus NP in terms of
categorical obstructions and event horizons for information flow.
Crossing energy relates to categorical mass by
$E_{\mathfrak{H}} = \mathfrak{m}_{\mathfrak{H}} \cdot c_q^{2}$
where $c_q = 1/(q - 1)$.

**Part III: The Descartes Universe and Observations.**
[Chapter 9](#chap:descartes-universe) maps the genus-$4$ constraint
to Bring's surface $\Sigma_4$, a complex curve with Euler
characteristic $-6$ and maximal automorphisms ($S_5$).  This
surface serves as the foundational state space: its coral tubes —
the exceptional divisors — provide coordinate systems for spacetime
and the electromagnetic field, mapping exactly where vertex
operators interact.  Within this space, embeddable knots form a
basis for homology and cohomology; specific knots and torus-knot
words define the full particle spectrum.  The geometric structure
also provides a natural setting in which to examine Yang–Mills
theory and the question of a mass gap.

[Chapter 10](#chap:observations) confronts theory with experiment.
We use observed CODATA values for the muon and electron mass to
determine $q_0$ for our local patch of the universe:

$$
  (1 - q^{-1})^2 =  \frac{\mathrm{Vol}(4_1)}{m_\mu / m_e}
  \qquad\Longrightarrow\qquad
  q =  q_0 +  O\!\bigl(2.2 \times 10^{-8}\bigr).
$$

From this single parameter we derive formulas for the masses of
all atoms parametrised by $q_0$, which align with observed values
to good precision.  The transfer matrices describe hadron
half-lives that match observation.

[Chapter 11](#chap:q-geometric-langlands) develops the
$q$-geometric Langlands correspondence that connects the
categorical framework to the geometric Langlands programme.

The [Glossary](#chap:glossary) maps paper terminology to Mathlib
declarations, the [Knot-Periodic Table](#app:knot-periodic-table)
collects the elements with their knot assignments, and the
[Index of Definitions](#app:index-definitions) provides a
searchable reference.
