<!-- FILE_START: bundle-observation-intro.md -->
The knot--particle dictionary of the previous section assigned a particle to each knot composite but left the carrier untouched: the state bundle of the brane, the observation map, and the colour-fibre dynamics. We now make the carrier explicit. A bundle initial condition fixes the data over the brane, the observation map factors through a braid, and the resulting sorting deposits energy $q + q^{-1}$ per crossing in the colour fibre — making the dictionary measurable.

The argument runs from a physical reading of the Borromean composite to the bundle initial data it fixes over the brane, then to observation itself. The load-bearing step is Proposition: Sorting deposits energy $q + q^{-1}$ per crossing in the colour fibre — observation is an open braid map whose internal crossings each pay the Hecke-eigenvalue cost on the colour fibre. From there the picture acquires dynamics — isotopic bundle data as the same physical state, torsion-driven flow through configuration space — and finally its categorical home, the finite bundles over $\mathbb{P}(V)$. The next section, **Borromean Baryons and Reidemeister Invariance**, takes the bundle and observation data as fixed and uses them to study the Borromean baryon as the test case for Reidemeister invariance of mass.
<!-- FILE_END: bundle-observation-intro.md -->

<!-- FILE_START: quarks-borromean-picture.md -->
Quarks are reassigned from individual knot types to Borromean-linked
unknots for the sake of the mass budget: with this identification a
baryon's mass arises almost entirely from the Borromean linking volume,
matching the QCD result that ${\sim}99\%$ of proton mass is binding
energy.  That payoff motivates the revised dictionary below.

The original dictionary assigned individual knot types to quarks
(three-twist $5_2$ for strange, torus $7_1$ for charm, etc.).  The
revised picture ([Conjecture](#conj:borromean-quark)) identifies quarks
not as fundamental knots but as **unknots (neutrinos) Borromean-linked
in the exceptional divisor** of Bring's surface.  A baryon is the
Borromean link $\mathcal{B}_3(\nu_r, \nu_g, \nu_b)$ bound by the Hopf
link $\mathcal{L}_H$ ([Definition](#def:borromean-baryon)):

- **Proton**: $\mathcal{B}_3(\nu_r, \nu_g, \nu_b) \oplus \mathcal{L}_H$
  with the $2 + 1$ crossing-orientation partition (two up + one down).
- **Neutron**: $\mathcal{B}_3(\nu_r, \nu_g, \nu_b) \oplus \mathcal{L}_H$
  with the $1 + 2$ partition (one up + two down).

Up/down flavour arises from the **crossing orientation** of each unknot
within $\mathcal{B}_3$, not from distinct knot types.  The baryon mass
comes almost entirely from the Borromean linking volume
$\mathrm{Vol}(S^3 \setminus \mathcal{B}_3) = 7.328\ldots$.

The mass of each hadron is determined by the terminal resolution
([terminal resolution](#prop:terminal-resolution)) and matches CODATA values to
sub-keV precision.
<!-- FILE_END: quarks-borromean-picture.md -->

<!-- FILE_START: bundle-initial-conditions.md -->
A measurement records where each constituent sits on the fibre while
leaving its momentum entirely free; a **bundle initial condition** is
the object that encodes exactly this position-only data. Over the
projective line $\mathbb{P}(V)$ at a reference point in an affine
chart it is a formal sum of localized hadrons and photons at base
points:

$$
  \mathcal{S}_0 =  \sum_{i \in I} (p_i, H_i)
$$

where each $(p_i, H_i)$ is a localized hadron
([Definition](#def:localized-hadron)) or a photon
($H_i = \mathbf{1}_{B_4}$; see
[confined-particle](#def:confined-particle)).
The photon identity $\mathbf{1}_{B_4}$, the 4-strand identity in $B_4$,
is knot-trivial under Markov closure yet carries four internal
polarisation$\times$chirality components on the exceptional divisor.
The index set $I$ may be infinite, and multiple constituents may share
the same base point (bosonic and fermionic statistics are determined by
the Skein algebra, not by a support constraint).

Equivalently, $\mathcal{S}_0$ is a section of the free commutative monoid on the
hadron sheaf $\mathcal{H}$:

$$
  \mathcal{S}_0  \in 
  \Gamma\!\bigl(\mathbb{P}(V),
  \mathrm{Free}_{\mathrm{CMon}}(\mathcal{H})\bigr).
$$

This is a **position-only** specification: the positions $\{p_i\}$ on
$\mathbb{P}(V)$ are known exactly, while the momenta are entirely
undetermined.  The categorical content is that $\mathcal{S}_0$ specifies
the *fibre data* of the bundle — which constituent sits in which fibre —
without any information about the horizontal transport connecting
neighbouring fibres.

The subsequent configurations $\mathcal{S}_1, \mathcal{S}_2, \ldots$
represent the forward light cone from $\mathcal{S}_0$: each step applies
one iteration of the Reeb flow
([information-theoretic time](#def:information-theoretic-time)),
adding horizontal transport and accumulating interaction relations.
The backward sequence $\mathcal{S}_{-1}, \mathcal{S}_{-2}, \ldots$
represents the past light cone (reversing computation).  Whether the
sequence extends infinitely in either direction, or terminates, is
**not assumed** — it depends on the dynamics within the given affine
chart.

For the equivalence relation on bundle initial conditions, see
[Definition](#def:bundle-isotopy-equivalence).
<!-- FILE_END: bundle-initial-conditions.md -->

<!-- FILE_START: observation-braid.md -->
An observation
([observation](#def:observation)) injects genuinely new
information: its outcome is not necessarily determined by the
initial conditions $\mathcal{S}_0$
([bundle initial conditions](#def:bundle-initial-conditions)).
This is precisely the **open-map** property by which an
observation is reflected in the braid — it maps open sets in
the state space to open sets, so new open neighbourhoods can be
created that were not present in the reference configuration
$\mathcal{S}_0$.

**Observation as crossing injection.**
In the braid picture, an observation inserts a new crossing
into the braid word.  The open map property means the
crossing type ($\mathfrak{p}\mathfrak{p}$, $\mathfrak{n} \mathfrak{n}$, or mixed) is not forced by the existing
braid — it is a genuine addition.  This is how a
computation receives its **input**: each observation is one
crossing injected at a discrete Planck step, one bit of
information that was not encoded in $\mathcal{S}_0$.

The Toffoli gate
([Toffoli transfer matrix](#prop:toffoli-transfer-matrix))
requires three crossings.  An observer performing one
Toffoli computation injects three crossings into the braid
— three Planck steps of intentional interaction with the
state bundle.
<!-- FILE_END: observation-braid.md -->

<!-- FILE_START: observation-intent-energy.md -->
**Intent and energy.**
Choosing to sort a sock drawer is a sequence of crossings
that increase local order (decrease classical entropy) at
the cost of quantum energy ($\delta q > 0$ per crossing) —
a concrete instance of the general fact that every
observation costs at least one crossing's worth of
$\hbar_q$.

An observation is done with intent.  Physically, intent
increases the quantum energy of the system: the substrate
perturbation $\delta q > 0$
([observation](#def:observation)) shifts $q$ upward,
increasing the quantum Planck constant
$\hbar_q = 1 - q^{-1}$.  The crossing energy
([crossing energy](#def:crossing-energy)) of the injected
crossing is the energetic cost of the observation.

The intent can either increase or decrease the **classical**
energy of the system — the observer can push or pull, heat
or cool, organise or scatter — provided the change is
continuous.  What cannot be done continuously is to leave
the quantum energy unchanged.
<!-- FILE_END: observation-intent-energy.md -->

<!-- FILE_START: observation-braid-not-predetermined.md -->
**The braid is not predetermined.**
The initial conditions $\mathcal{S}_0$ specify fibre data
without horizontal transport — position without momentum.
The braid that unfolds from $\mathcal{S}_0$ encodes the
horizontal transport: which fibres become connected, in
which order, with which crossing types.  Observations
modify this braid in real time.  The full braid word of
the universe is the interleaving of two sources:

1. **The flow**: crossings generated by the Reeb dynamics
   — the autonomous evolution of the state bundle.  These
   are determined by $\mathcal{S}_0$ and the variational
   equations.

2. **Observations**: crossings injected by observers via
   the adjoint action on the colour fibre.  These are
   **not** determined by $\mathcal{S}_0$ — they are the
   open-map contributions.

Concretely: suppose the flow alone winds three colour
fibres into the partial word $\sigma_1\sigma_2$, leaving
the first and third strands unlinked.  An observer
measuring that pair injects a single inverse crossing
$\sigma_1^{-1}$, completing the word to
$\sigma_1\sigma_2\sigma_1^{-1}$ — a finite braid, and
hence a computable section, that no autonomous
continuation of $\mathcal{S}_0$ would have produced.  The
observation does not perturb the flow; it appends a
crossing the flow could not.

The computable sections $E$ of
([Chapter 8](#chap:info-theory)) are those whose braid
word is finite.  The open map structure of observation
means that the set of reachable sections is **larger**
than the set determined by the initial conditions alone
— observers expand the computable fragment of the QOU.
<!-- FILE_END: observation-braid-not-predetermined.md -->

<!-- FILE_START: sorting-color-energy.md -->
Observation sorts colour: swapping two adjacent items into
their correct order is a projection between the two eigenspaces
of the R-matrix, and each such swap deposits a fixed quantum of
energy in the colour fibre.  The proposition below makes this
precise — the eigenspace decomposition is the mechanism, the
projection is the sorting operation, and the eigenvalue gap is
the energy per crossing.

**Proposition.**
*Let $\sigma_i$ be the Hecke generator
([R-matrix braiding](#rem:r-matrix-braiding)) acting on
$V \otimes V$, where $V$ is the fundamental representation.
Then:*

1. **(Eigenspace decomposition.)** *The R-matrix decomposes
   $V \otimes V$ into two eigenspaces:*

   $$
     V \otimes V
     = 
     \mathrm{Sym}^2(V)  \oplus  \textstyle\bigwedge^2(V)
   $$

   *with eigenvalues $q$ (symmetric, ordered) and $-q^{-1}$
   (antisymmetric, disordered) respectively.  These are the
   two roots of the Hecke relation
   $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$.*

2. **(Sorting is projection.)** *A sorting operation —
   swapping two adjacent items into the correct order —
   is the projection from $\bigwedge^2(V)$ to
   $\mathrm{Sym}^2(V)$ at the generator $\sigma_i$.  This
   projection is the $\mathrm{Ad}$ component of the
   observation: it acts on the colour fibre by rotating
   the gauge degrees of freedom from the antisymmetric
   (disordered) to the symmetric (ordered) eigenspace.*

3. **(Energy per crossing.)** *The energy deposited in the
   colour fibre by one sorting operation is the eigenvalue
   gap:*

   $$
     \Delta E_{\mathrm{colour}}
     =  q - (-q^{-1})
     =  q + q^{-1}
   $$

   *At $q = q_0$: $\Delta E = 2.011$ action units per
   crossing.*

4. **(Total sorting energy.)** *Let $\pi \in S_n$ be a
   permutation representing the disordered state of $n$
   items.  The minimum number of adjacent transpositions
   (braid crossings) needed to sort $\pi$ is the inversion
   count $\mathrm{inv}(\pi)$.  The total energy deposited
   in the colour fibre is:*

   $$
     E_{\mathrm{colour}}(\pi)
     = 
     \mathrm{inv}(\pi) \cdot (q + q^{-1})
   $$

   *The worst case (reverse permutation) requires
   $\binom{n}{2}$ crossings; the identity requires zero.*
<!-- FILE_END: sorting-color-energy.md -->

<!-- FILE_START: bundle-isotopy-equivalence.md -->
The physical content of a bundle initial condition depends only on
*which* hadron types are placed *where* — not on the labeling of the
index set or the particular representative of each ambient isotopy
class. The natural equivalence relation records exactly this. Two bundle
initial conditions ([Definition](#def:bundle-initial-conditions)) are
**isotopy equivalent** if they are related by a permutation of indices
and an ambient isotopy within each fibre:

$$
  \{(p_i, H_i)\}_{i \in I}  \sim 
  \{(p_{\sigma(i)}, H_{\sigma(i)}')\}_{i \in I}
$$

where $\sigma$ is a bijection on $I$ and each $H_{\sigma(i)}'$ is
ambient-isotopic to $H_{\sigma(i)}$ in the fibre $E_{p_{\sigma(i)}}$.
<!-- FILE_END: bundle-isotopy-equivalence.md -->

<!-- FILE_START: torsion-knot-flow.md -->
**Base-ring note (§7c).** The combinatorial knot data — the crossing number
$c(K)$, the $q$-factorial $[c(K)]_q!$, and the $q$-Alexander polynomial
$\Delta_q(K)$ — lives over the combinatorial ground ring
$R_q = \mathbb{Z}[q, q^{-1}]$. The angular-momentum normalisation ($2\pi$),
the round metric on $S^2$, and the evaluation $q = e^{-r}$ are the
archimedean specialisation over $\mathbb{R}$. The Lean sibling realises only
the real-valued $2\pi\,c(K)$ term (`intrinsicAngularMomentum` over
$\mathbb{R}$, via `Real.pi`); the $[c(K)]_q!$ normalisation of $\omega_K$ and
the interaction kernel remain over $R_q$.

Given a bundle initial condition $\mathcal{S}_0 = \{(p_i, K_i)\}_{i=1}^{N}$
([Definition](#def:bundle-initial-conditions)), the **torsion-driven knot
flow** is the one-parameter family of bundle states

$$
  \mathcal{S}_t =  \bigl\{\bigl(\Phi_t^q(p_i), K_i\bigr)\bigr\}_{i=1}^{N}
  \qquad t \geq 0,
$$

where $\Phi_t^q$ is the flow on $\mathbb{P}(V)$ generated by the
$q$-deformed Reeb vector field $\xi_q$
([Definition](#def:categorical-q-reeb-flow)).

The flow has two components:

1. **Intrinsic rotation.**  Each knot type $K$ carries an intrinsic
   angular momentum proportional to its crossing number $c(K)$:

   $$
     \omega_K =  c(K) \cdot \frac{2\pi}{[c(K)]_q!}
   $$

   where $[n]_q! = [1]_q [2]_q \cdots [n]_q$ is the $q$-factorial.
   This drives geodesic motion on $\mathbb{P}(V) \cong S^2$ along
   a great circle whose axis is determined by the initial fibre
   framing.

2. **Pairwise interaction.**  When two localized knots $(p_i, K_i)$
   and $(p_j, K_j)$ are within Planck-scale separation
   $d_{\mathbb{P}(V)}(p_i, p_j) < \ell_P$, they experience a
   short-range repulsive force

   $$
     F_{ij} = 
     \frac{\Delta_q(K_i) \cdot \Delta_q(K_j)}{d(p_i, p_j)^2 + \ell_P^2}
   $$

   where $\Delta_q(K)$ is the $q$-Alexander polynomial of $K$ evaluated
   at $q = e^{-r}$, and $d$ is the round metric on $S^2$.

The flow preserves the total knot content $\sum_i K_i$ (knot types do not
change under evolution) but redistributes positions on $\mathbb{P}(V)$.
Categorically, the flow is a natural transformation

$$
  \Phi^q  \colon 
  \mathrm{id}_{\mathrm{Bun}(\mathbb{P}(V))}
  \Longrightarrow
  \mathrm{id}_{\mathrm{Bun}(\mathbb{P}(V))}
$$

in the category $\mathrm{Bun}(\mathbb{P}(V))$ of finite bundles over the
projective line, where morphisms are equivariant maps that preserve knot
type.
<!-- FILE_END: torsion-knot-flow.md -->

<!-- FILE_START: bundle-category.md -->
This category is the categorical counterpart of the Feynman path
integral: rather than integrating over all field configurations, we
follow a single deterministic flow on a finite bundle.  Concretely, a
configuration is a fixed collection of knots pinned to base points in
the projective fibres — if a cosmological initial state exists in the
given affine chart, it is one such $\mathcal{S}_0$ — and the content of
the theory is the trajectory that configuration traces as the torsion
flow carries it forward.  We formalize this picture as follows.

The bundle initial conditions and the torsion-driven knot flow together
define a category $\mathrm{Bun}(\mathbb{P}(V))$:

- **Objects**: bundle initial conditions $\mathcal{S}_0 = \{(p_i, K_i)\}$
  ([Definition](#def:bundle-initial-conditions)).
- **Morphisms**: $\mathcal{S}_0 \to \mathcal{S}_0'$ are pairs $(\sigma, \{\phi_i\})$
  consisting of a permutation $\sigma \in S_N$ and a family of
  ambient isotopies $\phi_i \colon K_{\sigma(i)} \simeq K_{\sigma(i)}'$
  in the respective fibres.  In particular, morphisms preserve the total
  knot content.
- **Identity**: the identity permutation with trivial isotopies.
- **Composition**: permutation composition followed by isotopy
  concatenation.

The torsion flow $\Phi_t^q$ ([Definition](#def:torsion-knot-flow)) is an
endofunctor $\Phi_t^q \colon \mathrm{Bun}(\mathbb{P}(V)) \to \mathrm{Bun}(\mathbb{P}(V))$ that acts on objects by moving base points
and acts on morphisms by conjugating the isotopies with the flow.  The
family $\{\Phi_t^q\}_{t \geq 0}$ assembles into a continuous functor from
$(\mathbb{R}_{\geq 0}, +)$ — viewed as a one-object category — into the
endofunctor category $\mathrm{End}(\mathrm{Bun}(\mathbb{P}(V)))$.

The reference configuration $\mathcal{S}_0$ sits at $t = 0$; the physics
is the trajectory $t \mapsto \mathcal{S}_t$ in $\mathrm{Bun}(\mathbb{P}(V))$.  The
braid-group action on fibres ([Chapter 3](#chap:path-integrals-braiding)) then encodes the interactions
that occur when two knots approach within Planck-scale separation.
<!-- FILE_END: bundle-category.md -->

<!-- FILE_START: outro-measurement-observation.md -->
This closes the measurement-and-observation chapter.  Quarks live
in a Borromean configuration; bundle initial conditions fix the
observable's pre-state, the observation braid sorts colour by
energy, and the bundle-category-level isotopy equivalence pins
the measurement classes.  Taken together, these constitute the
bundle-structure picture, which identifies observation as a
categorical torsion-knot flow on the state bundle $\mathcal{S}$.

The next chapter (Bring's surface) lifts these measurement
constructions to the archimedean side and identifies the
spacetime base — the Bring surface $\mathcal{E}_q$ — on which
the bundle category lives.  The orbital symmetry and
cohomological embedding from that chapter inherit the
measurement structure recorded here.
<!-- FILE_END: outro-measurement-observation.md -->

