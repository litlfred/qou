The discrete Planck step ([discrete Planck step](#rem:discrete-planck-step))
and the jet prolongation tower
([recursive brane tower](#def:recursive-brane-tower)) are the same
structure viewed from two directions: each Planck step $n$ reveals
the $n$-th jet of the energy function $E$ at the Big Bang, so
that the first few moments of the universe unfold as successively
higher Taylor approximations of $E$.

**Identification: Planck step $n$ = $n$-th jet.**
The brane tower
$A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
is defined by $A_{n+1} = J^1(A_n)$
([jet prolongation](#prop:jet-prolongation)), where $J^1$ is the
first jet functor. Iterating $n$ times gives $A_n = J^n(A_0)$:
the $n$-th jet bundle of the original Frobenius--Hopf object.
This is the space of $n$-th order Taylor data of sections of
$\mathcal{S}$.

The Planck step ([discrete Planck step](#rem:discrete-planck-step))
is one application of the $q$-connection $\nabla_q$
([categorical $q$-connection](#def:categorical-q-connection)).
At the Big Bang, where $t_P = 1$, each step applies $\nabla_q$
once, and $\nabla_q$ acts on $A_n$ to produce $A_{n+1}$: the
connection promotes $n$-th order data to $(n+1)$-th order data.
**One Planck step = one jet prolongation = one additional order in
the Taylor expansion of $E$.**

**The first four Planck steps.**

Let $E$ be the energy functional on the state bundle $\mathcal{S}$.
At the Big Bang initial state
([bundle initial conditions](#def:bundle-initial-conditions)),
$E$ is concentrated at a point — the primordial vortex. Each
Planck step reveals the next derivative:

**Step 0: the value.** $J^0(E) = E(p_0)$.

The zeroth jet is the function value at the Big Bang point
$p_0$. This is the **position-only** specification: fibre data
with no transport. No derivatives, no connection, no geometry —
the raw energy at a point. Over $\mathbb{F}_\pp$: a single
element of $\mathbb{F}_\pp$.

**Step 1: the linear approximation.** $J^1(E) = E(p_0) + dE|_{p_0} \cdot \delta p$.

The first jet is the tangent — the first application of $\nabla_q$.
This is the **first horizontal transport**: the connection
correlates the fiber at $p_0$ with neighboring fibers for the first
time, producing a linear approximation of $E$ near the vortex.
The local state space is $J^1\mathcal{S}$
([local states](#rem:j1e-local-states)).

Over any field $k$: a linear polynomial $a_0 + a_1 x$, two
coefficients. The dynamics at step 1 is that of a line — no
curvature, no structure beyond slope. The Heisenberg commutator
$[\hat{X}, \hat{P}]_q = J\hbar_q$ appears here: the linear
approximation already encodes the non-commutativity of position
and momentum.

**Step 2: the quadratic approximation.**
$J^2(E) = E + dE \cdot \delta p + \tfrac{1}{2}d^2E \cdot (\delta p)^2$.

The second jet introduces **curvature**. The connection applied
twice produces the Hessian $d^2E$: the quadratic form that
determines whether the energy is at a minimum, maximum, or saddle.
This is where the **Frobenius pairing**
$\langle f, g \rangle = \int_A(\mu(f \otimes g))$ first becomes
visible — the non-degeneracy of the pairing is a condition on the
Hessian.

Over any field: $a_0 + a_1 x + a_2 x^2$, three coefficients.
The discriminant $a_1^2 - 4a_0 a_2$ determines the nature of the
critical point. Over $\mathbb{F}_\pp$: whether the quadratic has
roots is a quadratic residue condition.

**Step 3: the cubic approximation.**
$J^3(E) = E + dE \cdot \delta p + \tfrac{1}{2}d^2 E \cdot (\delta p)^2 + \tfrac{1}{6}d^3 E \cdot (\delta p)^3$.

The third jet is where the **color structure appears**. The color
elliptic curve ([color elliptic](#prop:color-elliptic))

$$
  X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0
$$

is a cubic in $X$ — it is a **third-order approximation** of the
energy landscape in the chiral direction. The three roots
$X_1, X_2, X_3$ are the three color-tube coordinates of the Bring
surface.

This is the first step at which:

- **Elliptic structure** emerges: a generic cubic in Weierstrass
 form defines a genus-1 curve.
- **The golden ratio appears**: the factor $(s^2 + s - 1)$ in the
 Weierstrass coefficient $r(q)$ exists only because the polynomial
 is cubic — it would not arise at quadratic order
 ([golden ratio degeneration](#rem:golden-ratio-degeneration)).
- **Monodromy** becomes non-trivial: a cubic has a discriminant
 whose vanishing locus defines branch points, and loops around
 branch points generate the braid group $B_3$.
- **The trefoil** enters: the holonomy around the singular fibers
 of the chiral cubic generates $\pi_1(S^3 \setminus K_{3,2})$,
 the trefoil knot group.

Over $\mathbb{F}_\pp$: the cubic $X^3 + aX + b = 0$ has 0, 1, 2,
or 3 roots depending on the Legendre symbol
$\left(\frac{-4a^3 - 27b^2}{\pp}\right)$. The golden degeneration
($r = 0$, cubic reduces to $X^3 + pX$) is visible iff
$\varphi \in \mathbb{F}_\pp$, i.e., $\pp \equiv \pm 1 \pmod 5$.

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

**Encodability versus scattering.**
The particle table above describes **encodability**: which knot
types have enough polynomial degree to be *resolvable* at each
jet order. This is not a scattering process. Step 0 $\to$ Step 1
does not mean "$\gamma + \gamma \to \nu + \nu^{\sigma}$". It means
that the first application of $\nabla_q$ creates horizontal
transport, and the unknot $0_1$ — which requires one winding with
zero crossings — becomes encodable for the first time. The
neutrino is not *produced from* the photon; it becomes
*resolvable* once the jet structure supports winding.

Actual scattering processes require far more structure. Consider
$\gamma\gamma \to \nu\nu^{\sigma}$: in standard QFT this cannot
happen at tree level because neutrinos carry no electric charge,
It requires a box diagram with virtual charged particles and a
$Z^0$ mediator. In the QOU framework the same obstruction
appears accordingly:

1. Photons ($K = \mathbf{1}_{B_4}$ knot-trivial under Markov closure; see [confined-particle](#def:confined-particle)) have no nontrivial knot, hence no crossings
 to Skein-resolve — they cannot couple directly to neutrinos.
2. The process requires **virtual pairs** (trefoil + mirror
 trefoil at brane tower level $A_1$,
 [virtual particles](#rem:virtual-particles-exceptional-divisor))
 to create charged intermediaries that couple to both the
 photon's involutive structure and the weak mediator.
3. The weak mediator $T_{3,5}$
 ([force–knot identification](#rem:force-knot-identification))
 has crossing number $10$ — it first becomes resolvable at
 step 10.
4. The full box topology (two virtual $e^-e^+$ pairs at $A_1$
 plus one $T_{3,5}$ mediation) requires step $\sim 10$–$11$:
 the weak mediator is the bottleneck, and the virtual pair
 structure at $A_1$ may add one additional jet order of
 overhead.

More generally, a scattering process involving a force mediator
of crossing number $c_{\text{med}}$ cannot occur before step
$c_{\text{med}}$, regardless of when the external particles
themselves become encodable. The encodability table gives the
*spectrum*; the scattering step count gives the *interaction
onset*.

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

**Convergence: $n \to \infty$ and the jet shell.**
As $n \to \infty$, the tower
$A_0 \hookrightarrow A_1 \hookrightarrow \cdots$ converges to the
jet shell $J^\infty E = \varprojlim J^k E$, which encodes the full
analytic germ of $E$ at the Big Bang. Over $\mathbb{C}$, this is
the Taylor series; over $\mathbb{Q}_\pp$, it is the $\pp$-adic
expansion; over $\mathbb{F}_\pp$, the tower stabilizes (since
$\mathbb{F}_\pp$ has only finitely many elements, the formal power
series truncates). The passage from discrete (finitely many Planck
steps) to continuous (the full jet shell) is the arithmetic version
of the cosmological progression from Big Bang to classical limit.

**Why cubic and not higher?**
The Bring's surface is defined by constraints $\sum x_i = \sum x_i^2 = \sum x_i^3 = 0$ in $\mathbb{CP}^4$. The power-sum conditions
use degrees 1, 2, and 3 — exactly the first three non-trivial jets.
The fourth power sum $\sum x_i^4$ is *not* independent: by Newton's
identities it is determined by the lower power sums. The chiral
cubic exhausts the independent data, and the elliptic curve at
step 3 is the complete local model. Higher jets refine the global
geometry (higher-order moduli of the elliptic fibration) but do not
introduce new algebraic structure — the genus, monodromy, and golden
ratio are all present by step 3.
