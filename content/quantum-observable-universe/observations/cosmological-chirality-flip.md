The [time reversal barrier](#rem:time-reversal-energy-barrier)
shows that chirality reversal costs infinite energy **in the
observable sector** — where the Frobenius form is non-degenerate
and $q$ is forced to be real.  But the
[cosmological limits](#ex:cosmological-limits) identify two
regimes where this protection breaks down.

**Formalization status.**  The claims below are **conjectural**.
The cosmological limits block is an example with "conjectural
interpretation"; the Frobenius degeneration at $q \to \infty$ is
not formalized in Lean.  The only proved limits are the trivial
evaluations $\hbar_q(1) = 0$ and $|\hbar_q(q) - 1| < \epsilon$
for large $q$.  The categorical picture sketched here — initial
and terminal objects in a category of QOU degenerations — is a
research direction, not an established result.

**At the Big Bang ($q \to \infty$).**
The Frobenius form degenerates:
$\int_A(f^\dagger f) \sim q^{-1} \to 0$.  The
[Heisenberg commutator](#rem:heisenberg-commutator)
$[\hat{X}, \hat{P}]_q \to J$ reaches its maximum — all
observables become maximally non-commutative.  The
positive-definiteness axiom that forces $q$ real
**no longer constrains**: with the Frobenius pairing
degenerate, the dagger structure has no norm to be
positive-definite *with respect to*.

In this regime, $q$ is free to acquire an imaginary part
$\theta \neq 0$.  The [complex substrate
interpretation](#rem:complex-substrate-interpretation)
then permits continuous chirality rotation in the fibers.
Concretely: at each blow-up point, the
[exceptional divisor](#def:exceptional-divisor)
$\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ becomes the stage
where trefoils and their mirrors can interconvert via the
phase rotation $\mathcal{X}_\varphi$.  The chirality flip
happens **in the fibers**, not at the base level.

This is precisely where Sakharov's conditions are met:
(i) the Frobenius form degeneration allows processes
that violate baryon number conservation (the topological
protection of link type weakens when the pairing
degenerates); (ii) the complex phase $\theta$ provides
CP violation; (iii) the Big Bang itself is the departure
from equilibrium.

**At heat death ($q \to 1$).**
The Hopf algebra becomes cocommutative
($\sigma \circ \Delta = \Delta$),
[$\hbar_q \to 0$](#def:substrate-parameter), and by
[prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction) the
three Descartes color tubes collapse to a single $\mathrm{U}(1)$
phase tube on $\mathcal{X}_5$.  The crossing-energy asymmetry
$q - q^{-1} = 2\sinh(\ln q) \to 0$ vanishes, so chirality is
undetectable: $T_{2,3}$ and $T_{2,3}^{\sigma}$ dissolve into one,
strong and Coulomb channels merge.  Only the two
$S_5$-equivariant generators of
[rem:symmetry-preserving-leptons](#rem:symmetry-preserving-leptons)
--- electron and muon --- survive as distinguishable topological
excitations; their masses vanish with $q - q^{-1}$.

**Categorical picture (conjectural).**

The correct categorical framework for these limits would involve
a **category of QOU degenerations** $\mathbf{QOU}_{\mathrm{deg}}$,
whose objects are triples $(\mathbf{C}, A, \tau)$ equipped with
a substrate parameter $q$, and whose morphisms are
structure-preserving maps that may degrade axioms:

- The **initial object** would be the Big Bang state: the
  maximally degenerate QOU where $q = \infty$, the Frobenius
  form is zero, and the only data is the
  [bundle initial condition](#def:bundle-initial-conditions)
  $E_0 = \sum_i (p_i, H_i)$ — positions without momenta.
  Every QOU with finite $q$ receives a unique morphism from
  this state (time evolution from the initial singularity).

- The **terminal object** is already established:
  [Bring's surface](#thm:descartes) $\Sigma_4$ is terminal in
  $\mathbf{C}_{-6}$.  In the degeneration category, the
  $q = 1$ classical limit would be terminal — every QOU
  admits a unique morphism *to* the classical (fully
  cocommutative) structure by sending $q \mapsto 1$.

- The **observable era** is the full subcategory on objects
  with $1 < q < \infty$ — where all QOU axioms hold
  non-degenerately.

This picture has **not been formalized**.  The key missing
ingredients are:

1. A precise definition of "degenerate QOU" (weakening
   the non-degeneracy axiom on the Frobenius pairing).
2. A proof that the $q \to \infty$ limit is initial
   (requires showing the bundle initial condition
   determines all subsequent time evolution).
3. A proof that $q \to 1$ is terminal (requires showing
   the classical projection is unique and
   structure-preserving).
4. Lean formalization of any of the above.

**The aeon boundary.**

At both cosmological extremes, the fiber geometry permits what
the observable interior forbids.  Between the endpoints, the
physically meaningful regime $1 < q < \infty$ enforces strict
chirality conservation.  This suggests a picture in which:

1. **Big Bang** (initial object): Frobenius degeneration releases
   the observability constraint.  Chirality flips occur freely
   in the fibers at the exceptional divisors.
   Matter--antimatter asymmetry is generated by the
   residual complex phase $\theta$ (CP violation) during
   the brief epoch before the Frobenius form restabilises.

2. **Observable era** (full subcategory, $1 < q < \infty$):
   chirality is frozen.  Electrons, protons, and neutrons
   maintain their handedness.  The topological barrier is
   infinite.

3. **Heat death** (terminal object): $q \to 1$ erases the
   chirality distinction.  All particles become their own
   antiparticles in the degenerate limit.  The crossing
   energy vanishes; matter and radiation become
   indistinguishable in the frozen geometry.

If the universe is cyclic — one aeon's heat death becoming
the next aeon's big bang (in the sense of Penrose's Conformal
Cyclic Cosmology, though without his conformal rescaling) —
then the chirality flip happens at the **aeon boundary**,
where the Frobenius form either degenerates ($q \to \infty$)
or trivialises ($q \to 1$).  The exceptional divisors are
the geometric locus of this transition: they are where
the fibers "reset", allowing the next aeon to begin with a
fresh chirality assignment.

The categorical conjecture is that the aeon transition is a
morphism from the terminal object of one copy of
$\mathbf{QOU}_{\mathrm{deg}}$ to the initial object of the
next — a categorical "recycling" map that preserves topological
data (knot types) while resetting metric data (masses, charges).
