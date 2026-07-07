<!-- FILE_START: molecular-chains-rings-intro.md -->
Bonds in hand, we assemble atoms into extended molecular structures. A **[molecular Hopf chain](#def:molecular-hopf-chain)** of length $N$ composes $N - 1$ covalent bonds along a backbone, giving a tridiagonal linking matrix with free endpoint sites. The crucial step in passing to closed rings is to replace the naïve picture — $N$ pairwise Hopf links — with a single non-local invariant: the **[threading link](#def:threading-link)** $T(2,N)$ whose braid word $(\sigma_1 \cdots \sigma_{N-1})^2$ winds twice through every atom and whose Alexander polynomial $\Delta_{T(2,2m)}(q) = (q^m - q^{-m})/(q - q^{-1})$ records half the pairwise Alexander weight. A **[molecular Hopf ring](#def:molecular-hopf-ring)** is then $[\mathcal{A}_1, \ldots, \mathcal{A}_N] \oplus \mathcal{T}_N$ — atoms bound globally by the threading link rather than locally by Hopf links.

The remaining blocks read off the dynamical consequences. Open chains behave as **[topological springs](#rem:chain-spring-modes)**: dangling endpoint trefoils support Reidemeister-I curl modes, backbone Reidemeister-II shifts propagate as phonons, and bending stiffness rises with bond order. Ring closure, by contrast, is a **[topological phase transition](#prop:ring-closure-barrier)**: the $N - 1$ pairwise bonds must dissolve before the threading link can form, and the activation barrier sits at the transition state where neither encoding stabilises the system. The same proposition explains ring super-stability — opening a ring costs $(N-1) - \Delta_{T(2,N)}(q)$ in extra Alexander weight plus the full activation climb.
<!-- FILE_END: molecular-chains-rings-intro.md -->

<!-- FILE_START: molecular-hopf-chain.md -->
A **molecular Hopf chain** is a linear sequence of atoms bonded
by covalent Hopf links ([covalent bond](#def:covalent-bond-types)),
where the first and last atoms retain unused linking sites — the
unclosed "missing link" that distinguishes an open chain from a
closed ring.

**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms with residual
sub-links $R_1, \ldots, R_N$.  A **molecular Hopf chain** of
length $N$ and bond order $k$ is the composite

$$
  \mathcal{C}_N^{(k)}
  = 
  \mathcal{A}_1
   \underset{B_k}{\oplus}
  \mathcal{A}_2
   \underset{B_k}{\oplus}
  \cdots
   \underset{B_k}{\oplus}
  \mathcal{A}_N
$$

where the operator $\underset{B_k}{\oplus}$ joins two adjacent atoms
by an order-$k$ covalent bond, and $B_k(R_i, R_{i+1})$ is that bond —
formed between the residual sub-links $R_i$ and $R_{i+1}$ of the atoms
it connects.  The **linking matrix** of the chain is the
$N \times N$ matrix

$$
  L^{\mathrm{chain}}_{ij}
  = 
  \begin{cases}
    k & \text{if } |i - j| = 1, \\
    0 & \text{otherwise}.
  \end{cases}
$$

This is a **tridiagonal** matrix — each atom is linked only to its
immediate neighbours.

**Boundary conditions.**
The endpoint atoms $\mathcal{A}_1$ and $\mathcal{A}_N$ each
consume only $k$ of their available linking sites for the chain
bond.  The remaining open sites are **free endpoints**: they can
bond to hydrogen, to side chains, or remain as dangling links.
For a homoatomic chain of carbon atoms ($k = 1$), each interior
carbon uses 2 of its 4 sites for the chain backbone, leaving 2
for side bonds; each endpoint carbon uses 1, leaving 3.

**Crossing energy of the chain.**
The total crossing energy is the sum over $N - 1$ bonds:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{C}_N^{(k)})
  = 
  (N - 1) \cdot E_{\mathrm{bond}}(k).
$$

The absence of a bond between $\mathcal{A}_1$ and $\mathcal{A}_N$
— the **missing link** — is the defining feature distinguishing
chains from rings.
<!-- FILE_END: molecular-hopf-chain.md -->

<!-- FILE_START: threading-link.md -->
A **threading link** is a single torus link that passes through
all atoms in a molecular ring simultaneously, replacing the
pairwise Hopf link picture with a non-local, correlated binding
structure.

**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms arranged in
a cycle.  The **threading link** of the ring is the torus link

$$
  \mathcal{T}_N =  T(2, N),
$$

whose closure in the braid group $B_N$ is

$$
  \hat{\beta}_N
  = 
  (\sigma_1  \sigma_2  \cdots  \sigma_{N-1})^2.
$$

The threading link winds **twice** around the torus defined by
the $N$ atoms, passing through every atom on each winding.  It
has $2(N-1)$ crossings in the standard braid representation —
all of the same sign.

**Component structure.**
The number of components of $T(2,N)$ is $\gcd(2,N)$:

| $N$ | $\gcd(2,N)$ | Components | Each component |
|:---:|:---:|:---:|---|
| odd | 1 | 1 (knot) | $T(1, N)$ — unknot wrapping $N$ times |
| even | 2 | 2 (link) | each unknotted, wrapping $N/2$ times |

For even $N$ (the case of benzene, $N = 6$), the threading link
is a **2-component link**: two unknotted loops, each threading
through all $N$ atoms.  These two components are the topological
realisation of the two delocalised $\pi$ electrons.

**Alexander polynomial.**
To read off how the winding structure distinguishes threading
links of different ring sizes, we record the Alexander polynomial
of $T(2,N)$ — the standard topological invariant of the link — and
evaluate it at the substrate parameter, where the resulting
$q$-symmetric Laurent polynomial tracks the winding count $m = N/2$.
The Alexander polynomial of $T(2,N)$ for even $N = 2m$ is

$$
  \Delta_{T(2,2m)}(t)
  = 
  \frac{t^m - t^{-m}}{t - t^{-1}}.
$$

Evaluated at the substrate parameter $t = q$:

| Threading | $m$ | $\Delta(q)$ |
|-----------|:---:|-------------|
| $T(2,2)$ (Hopf) | 1 | $1$ |
| $T(2,4)$ | 2 | $q + q^{-1}$ |
| $T(2,6)$ | 3 | $q^2 + 1 + q^{-2}$ |
| $T(2,8)$ | 4 | $q^3 + q + q^{-1} + q^{-3}$ |
<!-- FILE_END: threading-link.md -->

<!-- FILE_START: threading-link-weight.md -->
**Key identity.**
The threading link's Alexander weight is what sets the ring-closure
barrier, so the payoff of this section is its relation to the Hopf
link energy quantum $|q + q^{-1}|_{\mathrm{mol}}$.  For $T(2,6)$:

$$
  \Delta_{T(2,6)}(q)
  = 
  q^2 + 1 + q^{-2}
  = 
  (q + q^{-1})^2 - 1.
$$

The threading link's Alexander weight is **one less than the
square** of the Hopf link energy quantum $|q + q^{-1}|_{\mathrm{mol}}$.  This
quadratic relation encodes the non-local correlation: the
threading link "knows" about the Hopf link, but carries strictly
less weight.

**Contrast with pairwise Hopf links.**
Take the $T(2,6)$ ring above, so $N = 6$ atoms and $m = 3$ (hence
$2m = 6 = N$).  The pairwise picture bonds $N$ atoms with $N$ separate
Hopf links, giving total Alexander weight $N \cdot \Delta_{T(2,2)}(q) = N$.  The threading link replaces all $N$ bonds with a single
invariant:

$$
  \frac{\Delta_{T(2,2m)}(q)}{N}
  = 
  \frac{q^2 + 1 + q^{-2}}{6}
   \approx 
  \frac{1}{2}
  \qquad (|q| \approx 1).
$$

The threading carries **half the Alexander weight** of the
pairwise construction.  This factor of $\tfrac{1}{2}$ propagates
directly into the crossing energy, halving the predicted
ring-closure barrier.
<!-- FILE_END: threading-link-weight.md -->

<!-- FILE_START: molecular-hopf-ring.md -->
A **molecular Hopf ring** is not a chain with its ends joined —
it is a fundamentally different topological object.  Where the
chain bonds atoms pairwise via Hopf links
([molecular Hopf chain](#def:molecular-hopf-chain)), the ring
binds all atoms simultaneously via a single **threading link**
([threading link](#def:threading-link)).

**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms arranged in
a cycle.  A **molecular Hopf ring** of length $N$ is the
composite

$$
  \mathcal{R}_N
  = 
  [\mathcal{A}_1, \ldots, \mathcal{A}_N]
   \oplus 
  \mathcal{T}_N,
$$

where $[\mathcal{A}_1, \ldots, \mathcal{A}_N]$ denotes the $N$
atoms held in their fixed cyclic arrangement, and $\oplus$
superposes that arrangement with the single threading link
$\mathcal{T}_N = T(2, N)$ — a single torus link that passes
through all $N$ atoms.  The threading
link's braid word in $B_N$ is

$$
  \hat{\beta}_N
  = 
  (\sigma_1  \sigma_2  \cdots  \sigma_{N-1})^2,
$$

with $2(N-1)$ crossings, all of the same sign.
<!-- FILE_END: molecular-hopf-ring.md -->

<!-- FILE_START: hopf-ring-rigidity.md -->
**Crossing energy of the ring.**
Why should a ring whose atoms are held together by a single link
threaded through all of them be both cheaper to form than the same
ring bonded pair by pair and stiffer once formed?  Both answers come
from one object — the threading link's Alexander polynomial — so we
begin there.  The crossing energy is determined by that
Alexander polynomial evaluated at the substrate parameter:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{R}_N)
   \propto 
  \Delta_{T(2,N)}(q).
$$

For even $N = 2m$:

$$
  \Delta_{T(2,2m)}(q)
  = 
  \frac{q^m - q^{-m}}{q - q^{-1}}.
$$

**Contrast with the pairwise picture.**
A naïve ring built from $N$ separate Hopf links would have
crossing energy proportional to $N \cdot \Delta_{T(2,2)}(q) = N$.
The threading link replaces this with a single polynomial that
evaluates to roughly $N/2$ — the threading is **topologically
more efficient** than pairwise bonding.

| Structure | Binding | Alexander weight | Crossings |
|-----------|---------|:---:|:---:|
| Chain ($N-1$ Hopf links) | pairwise | $N - 1$ | $2(N-1)$ |
| Ring ($N$ Hopf links) | pairwise | $N$ | $2N$ + rearrangement |
| Ring ($T(2,N)$ threading) | non-local | $\Delta_{T(2,N)}(q) \approx N/2$ | $2(N-1)$ |

The threading ring has **fewer crossings than the pairwise ring**
and **no rearrangement cost** — the threading link already
connects all strands.

**Rigidity.**
The threading link passes through every atom twice (once per
winding).  Deforming the ring requires moving the threading link
through all $N$ atoms simultaneously — a global operation.  This
is the topological origin of ring rigidity: it is not that
individual bonds are stiff, but that the threading link
correlates all atoms non-locally.
<!-- FILE_END: hopf-ring-rigidity.md -->

<!-- FILE_START: chain-spring-modes.md -->
An open molecular Hopf chain
([molecular Hopf chain](#def:molecular-hopf-chain)) behaves like
a **topological spring**. The endpoints carry free linking sites
that are not anchored to any neighbouring atom, and these dangling
links can undergo Reidemeister I moves (curl/uncurl) and
Reidemeister II moves (crossing exchanges) without affecting the
interior bonds.

**Longitudinal modes.**
A compression or extension of the chain corresponds to a
correlated sequence of Reidemeister II moves along the backbone:
crossings shift from one bond to the next, propagating like a
phonon. The restoring force is the crossing energy gradient —
compressing two adjacent atoms below their equilibrium crossing
distance increases $\mathfrak{E}_{\mathrm{cross}}$ (overcrowded crossings),
while stretching them reduces Hopf linking and destabilises the
bond.

**Bending modes.**
The chain can bend at any interior atom where the two backbone
bonds meet. The bending stiffness depends on the bond order $k$:
a single-bond backbone ($k = 1$) is flexible (each bond is a
single Hopf link, rotated), while a double-bond backbone
($k = 2$) is rigid (the two parallel Hopf links resist torsion).

**Endpoint oscillation.**
The free endpoints are the softest part of the chain. Their
dangling trefoils can oscillate — gaining and losing crossings
with the environment — at energies far below those needed to
break an interior bond. This is the topological analogue of the
**stretching vibration** of terminal groups in infrared
spectroscopy.

In a closed ring ([molecular Hopf ring](#def:molecular-hopf-ring)),
all these soft modes are quenched: every atom is interior, every
site is bonded, and the ring's lowest-energy deformation requires
a **global** braid rearrangement rather than a local endpoint
wiggle.
<!-- FILE_END: chain-spring-modes.md -->

<!-- FILE_START: ring-closure-barrier.md -->
Closing a molecular Hopf chain into a ring is a **topological
phase transition**: the pairwise Hopf link structure is replaced
by a single threading link $T(2,N)$
([threading link](#def:threading-link)).  The energy barrier
arises not from adding one more bond, but from reorganising the
entire binding topology.

**Statement.**
Let $\mathcal{C}_N$ be a molecular Hopf chain of length $N$
([molecular Hopf chain](#def:molecular-hopf-chain)), and let
$\mathcal{R}_N$ be the corresponding threaded ring
([molecular Hopf ring](#def:molecular-hopf-ring)).  The crossing
energies, measured by Alexander polynomial evaluation at the
substrate parameter $q$, are:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{C}_N)
   \propto 
  (N-1) \cdot \Delta_{T(2,2)}(q)
  = 
  N - 1,
$$

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{R}_N)
   \propto 
  \Delta_{T(2,N)}(q)
  = 
  \frac{q^{N/2} - q^{-N/2}}{q - q^{-1}}
  \quad (\text{for even } N).
$$

For $N = 6$:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{C}_6)
   \propto  5,
  \qquad
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{R}_6)
   \propto 
  q^2 + 1 + q^{-2}
   \approx  3
  \quad (|q| \approx 1).
$$

The ring has **lower crossing energy** than the chain.  It binds
6 atoms with Alexander weight $\approx 3$, compared to the
chain's weight of $5$ for only 5 pairwise bonds.

**The barrier: topological reorganisation.**
Despite the ring being energetically favourable, the transition
$\mathcal{C}_N \to \mathcal{R}_N$ requires a discontinuous
change in topology: $N - 1$ separate Hopf links must be
**replaced** by a single threading link $T(2,N)$.  This is not a
continuous deformation — the braid word changes from a product of
non-adjacent generators $\sigma_i^2$ to the correlated product
$(\sigma_1 \cdots \sigma_{N-1})^2$.

The transition state is the configuration where the chain's
pairwise links are partially dissolved but the threading link has
not yet formed.  At this point, some bonds are broken but no
threading stabilisation has been gained — the crossing energy is
at a **maximum**:

$$
  \mathfrak{E}_{\mathrm{cross}}(\text{transition})
   > 
  \max\bigl(
    \mathfrak{E}_{\mathrm{cross}}(\mathcal{C}_N),
    \mathfrak{E}_{\mathrm{cross}}(\mathcal{R}_N)
  \bigr).
$$

The activation barrier is the energy required to reach this
intermediate state.

The energy cost of ring-opening is:

$$
  \Delta E_{\mathrm{open}}
  = 
  (N - 1) - \Delta_{T(2,N)}(q)
  + 
  E_{\mathrm{activation}}.
$$
<!-- FILE_END: ring-closure-barrier.md -->

<!-- FILE_START: ring-closure-superstability.md -->
**The spring analogy.**
The open chain is a spring held apart, and closing it into a ring
is the spring snapping shut: the separate coils — the pairwise
Hopf links — merge into a single, tighter winding, the threading
link $T(2,N)$.

**Ring super-stability from threading.**
Concretely, for $N = 6$ the crossing weight computed in
[the ring-closure barrier](#prop:ring-closure-barrier) drops from
$5$ — the chain's $N - 1$ pairwise bonds — to $\approx 3$, the
Alexander weight of the threading link, a net $5 - 3 = 2$ units of
additional stabilisation beyond the pairwise picture.  Once
$T(2,N)$ forms it locks the ring in a deep topological trap:
breaking the ring requires not just severing one bond but
**dissolving the threading link entirely** — converting the
correlated $T(2,N)$ back into $N$ separate Hopf links and
re-climbing the full activation barrier.  The threading link is
thus a **lower-energy encoding** of the same binding that the
pairwise Hopf links carried, so reverting to that pairwise
encoding costs energy.

**The barrier: topological reorganisation.**
More generally, although the ring is energetically favourable, the
transition $\mathcal{C}_N \to \mathcal{R}_N$ requires a
discontinuous change in topology: $N - 1$ separate Hopf links must
be **replaced** by a single threading link $T(2,N)$.  This is not a
continuous deformation — the braid word changes from a product of
non-adjacent generators $\sigma_i^2$ to the correlated product
$(\sigma_1 \cdots \sigma_{N-1})^2$.
<!-- FILE_END: ring-closure-superstability.md -->

