Each Planck step is one jet prolongation
([jet-Planck steps](#rem:jet-planck-steps)), and the particle
content resolvable at each step is governed by crossing number.

**Particle content at each step.**
The crossing number of a knot is the number of $R$-matrix
applications in its braid word. Each $R$-matrix application is
one action of $\nabla_q$ — one jet prolongation — one Planck step.
Therefore: **crossing number = minimum jet order at which the knot
first becomes resolvable**.

A particle with crossing number $c$ cannot exist before step $c$:
the $c$-th jet is the first Taylor order that has enough polynomial
degree to encode $c$ crossings of the braid closure.

See [Table 1](#tbl:jet-planck-steps-table1-data).

**Step 0: only the photon.**
Before any transport, only the fiber value exists. The photon is
$K = \varnothing$ — the empty knot
([photon wavefront example](#ex:photon-wavefront)):
background flux on the state bundle with no topological identity.
It requires no braiding, no crossings, no connection. It is
**pre-geometric**: it exists at the zeroth jet because it *is*
the zeroth jet. The photon is its own antiparticle.

**Step 1: neutrino and antineutrino.**
The first application of $\nabla_q$ creates horizontal transport
— the ability to wind around the fiber. The unknot $0_1$ is a
circle with zero crossings: it winds once around the Reeb direction
with trivial braiding
([neutrino](#def:neutrino-knot)). Its Jones polynomial
$J_\nu(q) = 1$ is a degree-0 polynomial — consistent with living
at the linear (degree 1) jet, where the only available structure
is a single winding with slope but no self-intersection.

The unknot is **amphichiral**: $T_{1,0} \cong T_{1,0}^{\sigma}$
as unoriented knots
([antineutrino](#def:antineutrino-knot)). The neutrino $\nu$
and antineutrino $\nu^{\sigma}$ are the same knot distinguished by
**orientation** (framing), not by knot type. Both appear at
step 1. This is the first matter-antimatter pair, but it is a
degenerate one: the two are topologically identical, differing
only in the sign of the Reeb winding.

The neutrino has zero crossing chirality ($Q(\nu) = 0$), zero
hyperbolic volume, and mass arising entirely from vacuum drag:
$m_\nu \sim \mu_0 \cdot (q - 1)$. This is the lightest possible
matter — the minimum topological excitation above the photon
vacuum.

**Step 2: the Hopf link (bosons).**
The Hopf link $L2a1$ is two unknots linked once. The linking
number is $1$, which requires detecting **curvature** — the
failure of parallel transport around a loop to return to the
identity. This is exactly the Hessian $d^2E$: the quadratic jet
detects the first non-trivial holonomy.

Bosons are links with an even number of components
([fermion--boson decomposition](#prop:fermion-boson-knot-link)):
$T(2,n)$ with $n$ even. The simplest is $T(2,2) = L2a1$
(gluon), which exists at step 2. The linking energy is the
first binding — two fibers correlated by curvature. The gluon
is its own antiparticle (the Hopf link is amphichiral).

At step 2 there is still no chirality: the quadratic jet has a
discriminant but no handedness. All particles so far (photon,
$\nu$, $\nu^{\sigma}$, gluon) are either self-conjugate or
distinguished only by orientation.

**Step 3: chirality, the electron, and the positron.**
The trefoil $3_1 = T_{2,3}$ has crossing number $3$: its braid
word $\sigma_1 \sigma_2 \sigma_1 \in B_3$ requires three
$R$-matrix evaluations. It cannot exist before the cubic jet.

Step 3 is where **chirality appears** for the first time. The
trefoil is **not** amphichiral: the left trefoil $T_{2,3}$ and the
The right trefoil $T_{2,3}^{\sigma}$ are distinct knots
([chirality: electron and positron](#rem:chirality-trefoil-electron-positron)).
The mirror operation $\sigma$ (reversing all crossings) produces
a genuinely different topological object. This is the origin of
the particle-antiparticle distinction for chiral matter:

- **Electron** $e^- = T_{2,3}$ (left trefoil, solid ●)
- **Positron** $e^+ = T_{2,3}^{\sigma}$ (right trefoil, outlined ○)

Both have crossing number $3$ and appear at the same Planck step.
The trefoil and its mirror are the two monodromy generators of the
chiral cubic — they arise together as the two orientations of the
holonomy around the branch points. **You cannot have the electron
without the positron**: the cubic jet produces both chiralities
simultaneously.

The same step also produces the **up quark** ($u = T_{2,3}$) and
**down quark** ($d = T_{2,3}^{\sigma}$) — the same trefoil pair
in the color-tube sector. With quarks available, the first
composite hadrons become constructible (though their linking
structure requires step 4).

**Step 4: the Higgs mass mechanism and the first hadrons.**
The figure-eight knot $4_1$ has crossing number $4$ and is the
first **hyperbolic** knot: $\mathrm{Vol}(4_1) = 2.0299$. It is
amphichiral ($4_1 \cong 4_1^{\sigma}$), so the Higgs field $H$
is its own antiparticle — like the neutrino but with non-trivial
topology. The Hodge decomposition
([cohomological embedding](#prop:cohomological-embedding)) places
$4_1$ in $H^{0,1}$ as the **mass mechanism**: its hyperbolic
volume drives the mass formula $m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^2$.

Also at step 4: the **Borromean baryon** $\mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$.
Although each constituent quark ($T_{2,3}$ or $T_{2,3}^{\sigma}$)
has crossing number $3$, the three-component Borromean linking
requires the quartic jet to resolve the inter-component holonomy.
The proton $p$ and neutron $n$ first appear here, along with
their antiparticles $p^{\sigma}$ and $n^{\sigma}$ (obtained by mirroring
all constituent quarks).

**Step 5: the muon and heavy quarks.**
The cinquefoil $5_1 = T_{2,5}$ has crossing number $5$ and genus
$2$. It is chiral: $5_1 \neq 5_1^{\sigma}$. This produces:

- **Muon** $\mu^- = T_{2,5}$ and **antimuon** $\mu^+ = T_{2,5}^{\sigma}$
- **Charm quark** $c = T_{2,5}$ and **strange quark** $s = T_{2,5}^{\sigma}$

(The charm and strange quarks are the mirror pair at genus 2,
as the up and down quarks are the mirror pair at genus 1. The
muon and antimuon share the same torus knot type, distinguished
by chirality — unlike the old $4_1$ assignment, the muon and
antimuon are now distinct knot types, consistent with their
distinct charges.)

**Summary: the unfolding.**

See [Table 2](#tbl:jet-planck-steps-table2-data).

Each row is one Planck step, one tick of discrete time at the
Big Bang. The universe does not spring into existence fully
formed: it **unfolds** through successive jet approximations.
The photon is pre-geometric (step 0). The neutrino and
antineutrino are the first topological excitations (step 1), but
they are amphichiral — topologically the same knot. Binding
appears at step 2. **True chirality** — and with it the
particle-antiparticle distinction for matter — requires three
ticks. At step 3, the cubic jet produces the trefoil and its
mirror simultaneously: the electron and positron, the up quark
and down quark, the golden ratio, and the braid group $B_3$
all emerge together in a single Planck step.

**Crossing number as computational complexity.**
The crossing number $c(K)$ of a knot $K$ is the minimum number
of $R$-matrix evaluations needed to compute its Jones polynomial.
In the jet-Planck correspondence, this is the **computational
cost in Planck steps**: a universe that has existed for $n$ steps
can resolve knots with $c \leq n$ but not those with $c > n$.
The particle spectrum is revealed incrementally, with heavier and
more complex particles appearing at later Planck steps — not
because they are "created" in a dynamical sense, but because the
Taylor approximation of $E$ does not yet have enough polynomial
degree to encode their topology.
