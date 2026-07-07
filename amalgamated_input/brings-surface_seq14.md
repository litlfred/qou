<!-- FILE_START: orbital-symmetry-embedding-intro.md -->
The topological mass spectrum of the previous section
extracts particle masses from knots embedded in Bring's surface.
We now ask which cohomological room those knots occupy.
Proposition: The orbital space at shell $n$ is the space of framing-$k$ sections of the normal bundle identifies the orbital space
as a space of sections of the normal bundle, and Proposition: Quantum numbers from Fourier decomposition of normal-bundle sections reads
off quantum numbers from the Fourier decomposition of those sections.
Remark: Five-fold symmetry: the Bring surface, the golden ratio, and the crystallographic obstruction records the $C_5$ symmetry of
Bring's surface and its obstruction to crystallographic embedding.

Proposition: Cohomological embedding: torus knot representations exhaust $H^1(\Sigma_g)$ is the central proposition of the section:
the torus knot representations exhaust the first cohomology of the
genus-$g$ surface, so the knots of the previous sections fill the
available cohomological room without redundancy. Remark: Color content as formal linear combination in $H_3(q)$ records the color
content of an embedded knot as a formal linear combination in the
Hecke algebra, and Remark: Term-by-term interpretation of the trivial knot operator on colored photons closes the chapter with the
explicit term-by-term action on colored photons.

_(draft.)_
<!-- FILE_END: orbital-symmetry-embedding-intro.md -->

<!-- FILE_START: orbital-space-normal-bundle.md -->
**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark)).**
Let $T_{2,3} \hookrightarrow \Sigma_4$ be the trefoil embedded
in the Bring's surface, and let $N = N_{T_{2,3}/\Sigma_4}$ be its
normal bundle.  At shell $n$ (framing twist $k = 2(n-1)$
relative to the Seifert framing), the space of orbital states is

$$
  \mathcal{O}_n
  = 
  \bigl\{
    \sigma \in \Gamma(N)  : 
    \mathrm{tw}(\sigma) = k, \quad
    \Delta_{T}\sigma = \lambda\sigma, \quad
    \lambda \leq \lambda_{n-1}
  \bigr\}
$$

where $\mathrm{tw}(\sigma)$ is the total twist (self-linking
relative to the Seifert framing), $\Delta_T$ is the Laplacian
on $T_{2,3}$ induced by the ambient metric, and $\lambda_\ell$
is the $\ell$-th eigenvalue.

*Claim:* $\dim \mathcal{O}_n = n^2$.

**Setup.**

The trefoil $T_{2,3}$ is a smooth closed curve of length $L$
in the Bring's surface $\Sigma_4$.  The normal bundle $N$ is a
rank-$2$ real vector bundle over $T_{2,3} \cong S^1$.  A
section $\sigma \in \Gamma(N)$ describes a transverse
displacement of the trefoil — a vibration.

The total twist $\mathrm{tw}(\sigma) = k$ constrains the
winding of $\sigma$ around the trefoil: it is the self-linking
number of the displaced curve $T_{2,3} + \epsilon\sigma$
relative to the Seifert surface.  This is the global R-I count
([Reidemeister invariance](#conj:reidemeister-mass-invariance)).

**The $q$-Laplacian on the trefoil.**

The $q$-Laplacian $\Delta_q$ on $T_{2,3} \cong S^1$ has
eigenvalues

$$
  \lambda_\ell =  [\ell]_q  [\ell + 1]_q,
  \qquad \ell = 0, 1, 2, \ldots
$$

where $[\ell]_q = (q^\ell - q^{-\ell})/(q - q^{-1})$ is the
$q$-integer.  At $q = 1$ this recovers $\ell(\ell + 1)$.
The eigenfunctions are $q$-deformed exponentials on the
circle.  Each eigenvalue $\lambda_\ell$ for $\ell \geq 1$ has
**multiplicity $2$** (cosine and sine modes).

**From $S^1$ modes to $S^2$ harmonics.**

The normal bundle $N$ is rank $2$: at each point of the
trefoil, the transverse displacement has **two independent
directions** (the two normal directions in the $3$-dimensional
ambient space of the Bring's surface).  A section $\sigma$ with
Fourier mode $\ell$ along the trefoil and direction $\hat{n}$
in the normal plane gives a vibration pattern:

$$
  \sigma(\varTheta)
  = 
  A_\ell  e^{i\ell\varTheta}  \hat{n}(\varTheta)
$$

The direction $\hat{n}(\varTheta)$ rotates as we go around the
trefoil (the normal bundle may be twisted).  The combined
mode — Fourier mode $\ell$ on $S^1$ times direction in the
normal plane — parametrises the same space as a **spherical
harmonic** $Y_\ell^m$ on the unit sphere surrounding the
proton.

This identification works because the trefoil orbits the
proton (spinning around the Borromean anchor).  The time
average of the vibrating trefoil sweeps out a sphere.  A
mode-$\ell$ vibration on the trefoil, averaged over the
trefoil's orbit, projects to the spherical harmonic
$Y_\ell^m$ on this sphere.  The magnetic quantum number
$m = -\ell, \ldots, +\ell$ labels the $2\ell + 1$
orientations of the mode relative to the Reeb axis
([categorical Reeb](#def:categorical-reeb)).

**Proof of $\dim \mathcal{O}_n = n^2$.**

At shell $n$, the energy constraint admits modes
$\ell = 0, 1, \ldots, n-1$ (modes $\ell \geq n$ have
eigenvalue $\lambda_\ell > \lambda_{n-1}$ and cost more
energy than the shell can provide).

For each mode $\ell$:
- On $S^1$: multiplicity $2$ (cosine and sine), except
  $\ell = 0$ which has multiplicity $1$.
- In the normal plane: direction $\hat{n}$ adds another
  factor.
- Combined with the $\mathrm{SO}(3)$ action on the ambient
  space: the mode-$\ell$ section space transforms as the
  irreducible representation $V_\ell$ of dimension $2\ell + 1$.

The total orbital dimension is

$$
  \dim \mathcal{O}_n
  = 
  \sum_{\ell=0}^{n-1} \dim V_\ell
  = 
  \sum_{\ell=0}^{n-1} (2\ell + 1)
  =  n^2.
  \qquad\square
$$

**The critical step.**

The non-trivial claim is that **mode $\ell$ on the trefoil
curve transforms as the irreducible $\mathrm{SO}(3)$
representation $V_\ell$ of dimension $2\ell + 1$** when
embedded in the Bring's surface.

This follows from two facts:

1. The trefoil $T_{2,3}$ orbits the proton
   ($\mathcal{B}_3$), sweeping out a topological $S^2$ in
   the time average.  The $\mathrm{SO}(3)$ symmetry of
   this $S^2$ acts on the normal-bundle sections.

2. A Fourier mode $\ell$ on $S^1$, embedded in $\mathbb{R}^3$
   via the trefoil map $\gamma: S^1 \to \Sigma_4 \hookrightarrow \mathbb{R}^3$, transforms under $\mathrm{SO}(3)$ rotations
   of the ambient space as $V_\ell$.  This is because the
   $\ell$-th Fourier mode of a curve in $\mathbb{R}^3$, when
   restricted to the unit sphere, is a degree-$\ell$ spherical
   harmonic.

**The cutoff $\ell \leq n - 1$.**

The energy of mode $\ell$ at shell $n$ is

$$
  E_\ell
  = 
  \frac{[\ell]_q  [\ell + 1]_q}{[n]_q^2} \cdot E_{\mathrm{ion}}
$$

where $E_{\mathrm{ion}} = 13.6$ eV and $[\ell]_q [\ell+1]_q$
is the $q$-Laplacian eigenvalue (centrifugal barrier).  At
$q = 1$ this reduces to $\ell(\ell+1)/n^2$.

For the mode to fit within shell $n$, we need
$[\ell]_q [\ell+1]_q \leq [n]_q [n-1]_q$, which gives
$\ell \leq n - 1$ (since $[\cdot]_q$ is monotone for
$q > 0$).
<!-- FILE_END: orbital-space-normal-bundle.md -->

<!-- FILE_START: orbital-fourier-decomposition.md -->
**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark)).**
Let $\varrho: S^1 \hookrightarrow \Sigma_4$ be the trefoil
$T_{2,3}$ embedded in the Bring's surface, and let
$N = N_{\varrho/\Sigma_4}$ be the normal bundle.  The four
quantum numbers $(n, \ell, m, s)$ arise from the Fourier
decomposition of sections $\sigma \in \Gamma(N)$ as follows.

**The normal bundle.**

The trefoil $\varrho(S^1)$ is a smooth closed curve in the
$3$-dimensional Bring's surface $\Sigma_4$ (viewed locally as a
real $3$-manifold via the spatial realization functor).  The
normal bundle $N$ is a rank-$2$ real vector bundle over
$S^1$:

$$
  N_p =  T_p \Sigma_4 / T_p \varrho
  \qquad\text{for } p \in \varrho(S^1).
$$

At each point of the trefoil, $N_p \cong \mathbb{R}^2$ — two
independent transverse directions.  A section
$\sigma \in \Gamma(N)$ is a smooth choice of transverse
displacement at each point of the trefoil.

**Parametrisation.**

Let $\varTheta \in [0, 2\pi)$ parametrise the trefoil
$\varrho(\varTheta)$.  A section decomposes as

$$
  \sigma(\varTheta)
  = 
  \sum_{\ell=0}^{\infty}
  \bigl(
    a_\ell \cos(\ell\varTheta) + b_\ell \sin(\ell\varTheta)
  \bigr)
  \hat{n}_1(\varTheta)
  + 
  \sum_{\ell=0}^{\infty}
  \bigl(
    c_\ell \cos(\ell\varTheta) + d_\ell \sin(\ell\varTheta)
  \bigr)
  \hat{n}_2(\varTheta)
$$

where $\hat{n}_1(\varTheta), \hat{n}_2(\varTheta)$ are an
orthonormal frame for $N_{\varrho(\varTheta)}$ that rotates
smoothly as $\varTheta$ varies.

The **total framing twist** is

$$
  k =  \mathrm{tw}(\sigma)
  = 
  \frac{1}{2\pi} \oint_{S^1}
  \kappa(\sigma, \hat{n}_1)  d\varTheta
$$

where $\kappa$ is the rotation angle of $\sigma$ relative to
the Seifert framing.  The shell number is
$n = k/2 + 1$ ([Reidemeister
invariance](#conj:reidemeister-mass-invariance)).

**The four quantum numbers.**

**(1) Principal quantum number $n$.**

The total twist $k = 2(n-1)$ is the **global R-I count** —
the self-linking number relative to the Seifert framing.  It
constrains the total energy:

$$
  E_n =  -\frac{E_{\mathrm{ion}}}{n^2}.
$$

The twist $k$ is the norm-squared of $\sigma$ in the $L^2$
sense:

$$
  k = 
  \sum_{\ell=0}^{\infty}
  \ell  (a_\ell^2 + b_\ell^2 + c_\ell^2 + d_\ell^2).
$$

At fixed $k = 2(n-1)$, only finitely many Fourier modes can
be nonzero.

**(2) Angular momentum quantum number $\ell$.**

The $\ell$-th Fourier mode is the **$\ell$-th resonance
frequency** of the trefoil's transverse vibration.  Mode
$\ell$ has wavelength $L/\ell$ on the trefoil (where $L$ is
the trefoil length) and eigenvalue
$\lambda_\ell = [\ell]_q [\ell + 1]_q$ under the
**$q$-Laplacian** $\Delta_q$, where

$$
  [\ell]_q =  \frac{q^\ell - q^{-\ell}}{q - q^{-1}}
$$

is the $q$-integer.  At $q = 1$, this recovers the classical
eigenvalue $\ell(\ell + 1)$.  At $q = q_0$, the
$q$-deformation shifts the eigenvalues:

| $\ell$ | $\ell(\ell+1)$ | $[\ell]_q [\ell+1]_q$ | Shift |
|-------:|------:|------:|------:|
| 0 | 0 | 0 | 0 |
| 1 | 2 | 2.012 | $+0.6\%$ |
| 2 | 6 | 6.139 | $+2.3\%$ |
| 3 | 12 | 12.55 | $+4.6\%$ |

The shifts are of order $(q - 1)^2 \sim \alpha^2$, producing
the **fine-structure splitting** between sub-shells at the
same $n$.

The energy constraint at shell $n$ admits modes
$\ell = 0, 1, \ldots, n-1$ only: modes $\ell \geq n$ require
more twist than available at framing $k = 2(n-1)$.

**(3) Magnetic quantum number $m$.**

At each Fourier mode $\ell$, the section $\sigma$ vibrates in
the $2$-dimensional normal plane $N_p$.  The trefoil is
embedded in $\Sigma_4 \hookrightarrow \mathbb{R}^3$ (via
spatial realization), so the normal plane is embedded in
$\mathbb{R}^3$.  The vibration at mode $\ell$ can be
**oriented** in the ambient space.

The $\mathrm{SO}(3)$ rotation group acts on $\mathbb{R}^3$
and hence on the normal-bundle sections.  Under this action,
the mode-$\ell$ sections transform as the **irreducible
representation $V_\ell$** of $\mathrm{SO}(3)$, with
dimension $2\ell + 1$.  The magnetic quantum number
$m = -\ell, \ldots, +\ell$ labels the weight spaces of
$V_\ell$ relative to the Reeb axis
([categorical Reeb](#def:categorical-reeb)):

$$
  V_\ell = 
  \bigoplus_{m=-\ell}^{+\ell} \mathbb{C} \cdot Y_\ell^m
$$

where $Y_\ell^m$ is the spherical harmonic — the restriction
of the mode-$\ell$ vibration pattern to the unit sphere
around the proton.

**Identification of the representation as $V_\ell$.**  The
Fourier mode $\ell$ on $S^1$, transported to $\mathbb{R}^3$
by the embedding $\varrho$, generates a function on the
sphere $S^2$ surrounding the proton (the time-averaged orbit
of the trefoil).  This function is a **homogeneous harmonic
polynomial of degree $\ell$** restricted to $S^2$, which is
by definition a spherical harmonic.  The space of degree-$\ell$
spherical harmonics is $V_\ell$ with $\dim V_\ell = 2\ell + 1$.

**(4) Spin quantum number $s$.**

The fiber adjoint involution
([fiber adjoint involution](#prop:fiber-adjoint-involution))
acts on the normal bundle by exchanging the two orientations
of the Hopf link between the electron and proton.  This is
an involution $\sigma \mapsto -\sigma$ on $\Gamma(N)$ that
commutes with the Laplacian and the $\mathrm{SO}(3)$ action.

Each orbital $(n, \ell, m)$ splits into two states under this
involution:

$$
  s = +\tfrac{1}{2}: \quad
  \sigma  \text{in the } (+1)\text{-eigenspace},
  \qquad
  s = -\tfrac{1}{2}: \quad
  \sigma  \text{in the } (-1)\text{-eigenspace}.
$$

This doubles the orbital count: each of the $n^2$ orbitals
holds $2$ states, giving $2n^2$ states per shell.

**Summary.**

$$
  \Gamma(N)\big|_{k=2(n-1)}
   \cong 
  \bigoplus_{\ell=0}^{n-1}
  \bigoplus_{m=-\ell}^{+\ell}
  \bigoplus_{s=\pm 1/2}
  \mathbb{C}
  \qquad
  \text{(dimension } 2n^2\text{)}
$$

| Quantum number | Fourier origin | Representation |
|:-:|---|---|
| $n$ | Total framing twist $k = 2(n-1)$ | Energy shell |
| $\ell$ | Fourier mode on $S^1$ | $\mathrm{SO}(3)$ irreducible $V_\ell$ |
| $m$ | Weight in $V_\ell$ (Reeb projection) | Spherical harmonic $Y_\ell^m$ |
| $s$ | Fiber adjoint involution eigenvalue | Spin $\pm 1/2$ |
<!-- FILE_END: orbital-fourier-decomposition.md -->

<!-- FILE_START: fivefold-symmetry.md -->
The Bring surface $\Sigma_4$ (genus $4$, Euler characteristic
$\chi = -6$) has automorphism group $S_5$, the symmetric group
on $5$ elements.  This $5$-fold symmetry is not a coincidence —
it is the deepest structural feature of the QOU and has
consequences at every level of the theory.

Its three structural consequences are developed in the
following remarks:

- the **crystallographic obstruction** and the weak force as
  the non-lattice $5$-fold symmetry
  ([crystallographic obstruction](#rem:fivefold-crystallographic-obstruction));
- the **five sheets** of $\Sigma_4$, the golden ratio $\varphi$,
  and the $q = 1/\varphi^2$ golden-ratio phase transition
  ([five sheets and the golden ratio](#rem:fivefold-sheets-golden-ratio));
- the **five-fold symmetry of the affine charts**, the five
  observer types, and the $3 + 2$ generation partition
  ([affine charts and generations](#rem:fivefold-affine-charts-generations)).

## Beyond shell dynamics

The $5$-fold symmetry appears at every scale:

See [Table 2](#tbl:fivefold-symmetry-table2-data).

The $3$-fold symmetry (Borromean, color, lattice-compatible)
and $5$-fold symmetry (aperiodic, weak, parity-violating) are
the two irreducible components of the Bring surface structure.
The interplay between them — mediated by $T_{3,5}$ — generates
the full complexity of the physical world: the strong force
binds (periodically), the weak force transforms (aperiodically),
and the electromagnetic force (the involutive $2$-fold structure)
measures the interface.
<!-- FILE_END: fivefold-symmetry.md -->

<!-- FILE_START: fivefold-crystallographic-obstruction.md -->
## The crystallographic obstruction

**Theorem (Crystallographic Restriction).**
*A lattice $\Lambda \subset \mathbb{R}^n$ is invariant under
a rotation of order $k$ only if $k \in \{1, 2, 3, 4, 6\}$
(for $n = 2$) or $k \in \{1, 2, 3, 4, 5, 6\}$ (for $n = 3$,
where $5$-fold is allowed only for non-lattice symmetry).*

Periodic lattices — the mathematical substrate of crystals —
cannot have $5$-fold rotational symmetry.  This is why:
- There are no crystals with pentagonal unit cells.
- Quasicrystals (Shechtman, 1984 \cite{shechtman1984})
  exhibit $5$-fold diffraction patterns precisely because
  they are **aperiodic** — their order is not captured by
  any lattice.
- Penrose tilings have local $5$-fold symmetry but no
  translational period.

The forces compatible with periodic structure are exactly those
with symmetry orders in $\{1, 2, 3, 4, 6\}$:

See [Table 1](#tbl:fivefold-symmetry-table1-data).

The $5$-fold symmetry of the Bring surface is **the unique
symmetry that breaks periodicity**.  It is carried by $T_{3,5}$,
the weak force mediator — the only force that violates parity
($q \neq q^{-1}$ accumulated over $10 = \binom{5}{2}$ crossings)
and the only force with massive carriers ($W^{\pm}$, $Z^0$).
The weak force is weak precisely because $5$-fold symmetry
cannot propagate through a lattice — it is confined to local,
aperiodic interactions.
<!-- FILE_END: fivefold-crystallographic-obstruction.md -->

<!-- FILE_START: fivefold-sheets-golden-ratio.md -->
## The Bring surface and its five sheets

The Bring curve is the projective variety

$$
  \Sigma_4  :  x_1^5 + x_2^5 + x_3^5 + x_4^5 + x_5^5 = 0
  \quad\subset \mathbb{P}^3
$$

(after fixing $x_1 + x_2 + x_3 + x_4 + x_5 = 0$).  The
$S_5$ action permutes the five coordinates $(x_1, \ldots, x_5)$.
Each coordinate $x_i$ defines a **sheet** of the surface —
a local branch of the covering $\Sigma_4 \to \mathbb{P}^1$.
The five sheets are the five "copies" of the base that are
glued together along the ramification locus.

The **golden ratio** enters through the diagonal of the regular
pentagon.  The five sheets of $\Sigma_4$ meet at ramification
points where two or more coordinates coincide.  At a generic
ramification point, two sheets merge (simple branching).  The
**monodromy** around such a point is a transposition
$(x_i x_j) \in S_5$.  The transpositions generate $S_5$,
The full $5$-fold symmetry is recovered by encircling all
ramification points.

The regular pentagon inscribed in the unit circle has vertices
at $e^{2\pi i k/5}$ for $k = 0, 1, 2, 3, 4$.  The ratio of
diagonal to side is

$$
  \frac{\text{diagonal}}{\text{side}}
  = 
  \varphi
  = 
  \frac{1 + \sqrt{5}}{2}
   \approx  1.618
$$

the golden ratio.  In the Bring surface: the five sheets at a
generic point are spaced by fifth roots of unity, and the
"diagonal" connection between non-adjacent sheets (the $T_{3,5}$
interaction, which skips from sheet $i$ to sheet $i+2$ or
$i+3$) has amplitude proportional to $\varphi$ relative to the
"side" connection (the $T_{2,3}$ interaction between adjacent
sheets).

The $q$-deformed version: the $q$-AND polynomial
$P_{7,6}(q)$ ([Toffoli gate](#prop:toffoli-transfer-matrix))
has a zero at $q = 1/\varphi^2 = (3 - \sqrt{5})/2 \approx 0.382$.
This is the **golden ratio phase transition** — the substrate
parameter at which the diagonal $T_{3,5}$ connection vanishes
and the $5$-fold symmetry degenerates to $3$-fold
([golden ratio transport](#rem:golden-ratio-transport)).
<!-- FILE_END: fivefold-sheets-golden-ratio.md -->

<!-- FILE_START: fivefold-affine-charts-generations.md -->
## Five-fold symmetry in the affine chart

Each fibre functor $\tau \colon \mathbf{C} \to \mathbf{Vect}$
is an affine chart
([contact affine chart](#def:contact-affine-chart)) — one
observer's local coordinate system.  The Tannaka–Krein
reconstruction gives a $G$-torsor of natural isomorphisms
between charts (the transition functions).

The $S_5$ symmetry of $\Sigma_4$ acts on the **space of
affine charts itself**.  The five sheets of the Bring surface
correspond to five **classes of affine charts**, related by
the $S_5$ permutation.  Two charts in the same class
(on the same sheet) are related by a continuous $G$-transformation.
Two charts in different classes (on different sheets) are related
by a **sheet-crossing monodromy** — a discrete transformation
that cannot be continuously deformed to the identity.

This means:

1. **Five types of observer.**  There are five topologically
   distinct ways to embed a fibre functor into the Bring
   surface.  Each type "sees" the same physics (the categorical
   structure is $S_5$-invariant) but with different
   **conventions** — different identifications of which
   torus knot is the electron, which is the muon, etc.
   The $5$-fold ambiguity is the **generation problem**:
   why three generations of matter?  Because three of the
   five sheets carry the three families ($T_{2,3}$, $T_{2,5}$,
   $T_{2,7}$), while the remaining two carry the force
   mediators ($T_{2,9}$, $T_{3,5}$).  The $S_5$ action
   permutes all five, but physics distinguishes the $3 + 2$
   partition.

2. **Aperiodic global structure.**  The transition functions
   between different-sheet charts involve $5$-fold monodromy,
   which (by the crystallographic restriction) cannot be
   realised as a lattice symmetry.  The global structure of
   the QOU is therefore **aperiodic** — like a quasicrystal,
   not like a crystal.  Translational symmetry
   (homogeneity of space) holds locally (within each sheet)
   but the inter-sheet gluings are aperiodic.

3. **Penrose-like tiling of spacetime.**  The five affine
   chart types tile the base $\mathbb{P}(V)$ in a pattern
   analogous to a Penrose tiling: local $5$-fold symmetry,
   no global period, but long-range order determined by the
   Bring surface monodromy.  The "inflation rules" of the
   Penrose tiling correspond to the Iwahori--Hecke algebra relations
   (the Gröbner--Shirshov basis) acting on the chart overlaps.
<!-- FILE_END: fivefold-affine-charts-generations.md -->

<!-- FILE_START: klein-bring-icosahedral-bridge.md -->
**Conjecture (Klein icosahedral–quintic bridge, sharpened).** *There is a
faithful icosahedral $A_5$-action on the categorical base $\mathbb{P}(V)$ — the
projective space of the $2$-dimensional braiding object $V$, whose archimedean
realisation is $\tau(\mathbb{P}(V)) \cong \mathbb{P}^1(\mathbb{C})$ — realising
Klein's icosahedral solution of the Bring–Jerrard quintic, with orbifold
quotient $\mathbb{P}(V)/A_5 \cong S^2(2,3,5)$, the base of the Seifert fibration
$S^3/2I \to S^2(2,3,5)$ of the Poincaré homology sphere. Its order-$2$ and
order-$3$ generators are at the icosahedral angle and are therefore **distinct**
from the trefoil $S_3$ generators carried by the exceptional divisor.*

## Established skeleton (classical)

1. **The Bring curve is the Bring–Jerrard root variety.** The defining
   equations $\sum_j x_j = \sum_j x_j^2 = \sum_j x_j^3 = 0$
   ([Bring's curve](#rem:brings-curve)) are the vanishing of the first three
   power sums of the five roots — the configuration of quintics in
   **Bring–Jerrard normal form** $z^5 + az + b$ \cite{bring1786}.
2. **The $(2,3,5)$ triangle rotation group is the icosahedral $A_5$.** The
   triangle is spherical, $\tfrac12 + \tfrac13 + \tfrac15 = \tfrac{31}{30} > 1$,
   so its orientation-preserving group is finite of order $60$, namely $A_5$,
   acting on $\mathbb{P}(V)$ with exceptional orbits $\{12, 20, 30\}$.
3. **Klein's solution.** The one-parameter Bring–Jerrard quintic is solved by
   the icosahedral equation \cite{klein1888}, with the five roots on the five
   inscribed tetrahedra ($5 = [A_5 : A_4]$).

## Proof attempt — the naive assembly is refuted (scope-limited)

The natural first route is to *reuse* the corpus's existing force operations as
the $(2,3,5)$ generators. This route is **refuted**, decisively, from the
corpus's own data. The canonical generators ([SU(2) generators](#def:su2-generators))
are

$$
  \alpha = \exp\!\bigl(\tfrac{2\pi}{3}e_3\bigr) \ (\text{order } 3,\ \text{colour/trefoil}),
  \qquad
  \beta = \exp(\pi e_1) \ (\text{order } 2,\ \text{EM involution } z \mapsto 1/z),
$$

with the **established dihedral relation** $\beta\alpha\beta^{-1} = \alpha^{-1}$.
Since $\beta^2 = 1$ in $\mathrm{SO}(3)$ (so $\beta^{-1} = \beta$), this gives
$\beta\alpha\beta = \alpha^{-1}$, whence

$$
  (\beta\alpha)^2 = (\beta\alpha\beta)\,\alpha = \alpha^{-1}\alpha = 1.
$$

So $\beta\alpha$ has order $2$ (equivalently $\mathrm{tr}\,R_\beta R_\alpha = -1$,
a $\pi$-rotation): $\langle \alpha, \beta\rangle$ satisfies the **$(2,3,2)$
dihedral** relation and is the trefoil $S_3 \cong D_3$ — **not** the icosahedral
$(2,3,5)$ group, which would require $(\beta\alpha)$ of order $5$
($\mathrm{tr} = 2\cos 72^\circ$ or $2\cos 144^\circ$, never $-1$). The order-$5$
$\zeta_5$ pentad sits on a *third* axis and is not in any triangle relation with
$\alpha, \beta$.

This is a **scope-limited negative (a)**: it refutes the *as-is* assembly of the
existing trefoil generators, not the existence of an icosahedral realisation.
Its content is exactly the corpus's own structural split
([fivefold symmetry](#rem:fivefold-symmetry)): the $3$-fold (colour, periodic,
lattice-compatible) and the $5$-fold (weak, aperiodic, parity-violating) are
**distinct irreducible components** — they do not assemble into one icosahedral
group through the trefoil's perpendicular $e_1, e_3$ axes.

## Construction — the surviving group-theoretic core is discharged

Klein's icosahedral generators on $\mathbb{P}(V)$ (coordinate $w$,
$\varepsilon = e^{2\pi i/5}$ \cite{klein1888}) supply the icosahedral-angle pair
the trefoil could not — and the order-$5$ element is *exactly the corpus
$\zeta_5$ pentad*:

$$
  S : w \mapsto \varepsilon\, w \quad (\text{the } \zeta_5 \text{ pentad, order } 5,\ \text{fixing } 0/\infty),
  \qquad
  T = \tfrac{1}{\sqrt5}\begin{pmatrix} \varepsilon-\varepsilon^4 & \varepsilon^2-\varepsilon^3 \\ \varepsilon^2-\varepsilon^3 & -(\varepsilon-\varepsilon^4)\end{pmatrix}
  \ (\text{icosahedral } 2\text{-fold}).
$$

Setting $c_2 = T$ (order $2$) and $c_3 = TS$ (order $3$) gives
$c_2 c_3 = T\,TS = S$ — the $\zeta_5$ pentad, of order **exactly $5$**, with
$S^5 = T^2 = (ST)^3 = 1$, so $\langle S, T\rangle \cong A_5$ (order $60$). Thus
order-$2$/order-$3$ generators at the icosahedral angle, *distinct* from the
trefoil's perpendicular pair, **exist** and assemble the $\zeta_5$ pentad into
the icosahedral $A_5$. Verified parameter-free in
[`scripts/keystone_klein_icosahedral_construction.py`](https://github.com/litlfred/qou/blob/main/scripts/keystone_klein_icosahedral_construction.py);
the abstract realizability of the $(2,3,5)$ relation is Lean-proved sorry-free
(`icosahedral_235_realizable`: explicit even permutations $(1\,2)(3\,4)$,
$(0\,2\,4)$ with product the $5$-cycle), the positive complement to the
$(2,3,2)$ refutation.

The six branch points $\{\zeta_5^k, \infty\}$ are not $A_5$-invariant (no
icosahedral orbit has size $6$; minimum $12$): they are the $C_5$-pentagon
skeleton — the equatorial $S$-orbit — not the full icosahedral set.

## Keystone-base orbifold identification (established)

The orbifold quotient is classical icosahedral geometry, and it is the keystone
base. The three exceptional $A_5$-orbits on $\mathbb{P}(V)$ — vertices ($12$),
faces ($20$), edges ($30$) — have cyclic stabilisers of orders
$60/\{12,20,30\} = \{5,3,2\}$, the **cone-point orders** of the quotient. Hence

$$
  \mathbb{P}(V)/A_5 \;=\; S^2(2,3,5),
  \qquad
  \chi_{\mathrm{orb}} = 2 - \!\sum_{m\in\{2,3,5\}}\!\bigl(1-\tfrac1m\bigr)
   = \tfrac{1}{30}
   = \frac{\chi(\mathbb{P}^1)}{|A_5|} = \frac{2}{60},
$$

the matching Euler characteristics confirming the underlying surface is the
genus-$0$ sphere \cite{klein1888}. This spherical orbifold $S^2(2,3,5)$ is
exactly the base of the Seifert fibration $S^3/2I \to S^2(2,3,5)$ of the
**Poincaré homology sphere** — $2I \subset \mathrm{SU}(2)=S^3$ being the binary
cover of $A_5 \subset \mathrm{SO}(3)$, so the induced fibration descends to
$\mathbb{P}^1/A_5$. The cone-structure facts are Lean-proved sorry-free
(`cone_orders`, `orbifold_euler_char`, `orbifold_euler_char_eq_cover`,
`orbifold_spherical`).

## Canonicity of the icosahedral group (established)

The icosahedral $A_5$ is **not imposed** — it is generated by two
corpus-canonical operations. The $\zeta_5$ pentad (weak $5$-fold, a $5$-cycle)
and the colour trefoil ($3$-fold, a $3$-cycle) are both **even**, and

$$
  \langle\, \zeta_5\text{ pentad},\ \text{colour trefoil}\,\rangle \;=\; A_5
  \quad (\text{the alternating subgroup of } \mathrm{Aut}(\text{Bring}) = S_5,
  \ \text{order } 60).
$$

(Verified: `keystone_klein_icosahedral_construction.py`; a $5$-cycle and a
$3$-cycle generating $A_5$ is classical. Parities Lean-proved sorry-free:
`pentad_even`, `trefoil_even`.) The reason the naive trefoil+EM assembly was
dihedral is now sharp: the EM involution $z\mapsto 1/z$ is a *single*
transposition $x_0\leftrightarrow x_1$ — **parity-odd**, so it lies in the coset
$S_5\setminus A_5$, *not* in the icosahedral $A_5$ (`em_involution_odd`). Klein's
icosahedral $2$-fold $T$ is instead an **even** double-transposition,
$T = (\text{EM})\circ(\text{colour swap})$. The even/odd split is the corpus's
own physics: even $=$ the stable weak $+$ colour sector ($A_5$); odd $=$ the EM /
chirality / parity coset.

## Möbius realization via Klein's resolvent (explicit)

The single-$\mathbb{P}(V)$ icosahedral Möbius action is explicit, and its
quotient map is Klein's resolvent. On $\mathbb{P}(V)$ (coordinate $w$) the three
icosahedral orbit forms are

$$
\begin{aligned}
  f_{12}(w) &= w^{11} + 11w^6 - w && (\text{12 vertices}),\\
  H_{20}(w) &= -w^{20} + 228w^{15} - 494w^{10} - 228w^5 - 1 && (\text{20 faces}),\\
  T_{30}(w) &= w^{30} + 522w^{25} - 10005w^{20} - 10005w^{10} - 522w^5 + 1 && (\text{30 edges}),
\end{aligned}
$$

satisfying **Klein's syzygy**

$$
  T_{30}^2 + H_{20}^3 = 1728\, f_{12}^5
$$

(exact — Lean `klein_syzygy`, verified by integer-polynomial arithmetic in
`scripts/keystone_klein_icosahedral_construction.py`). The forms are
**pentad-anchored**: $f_{12}$ is $\zeta_5$-relative-invariant
($f_{12}(\varepsilon w) = \varepsilon f_{12}(w)$, all exponents $\equiv 1
\bmod 5$) and $H_{20}, T_{30}$ are $\zeta_5$-invariant. Hence the degree-$0$
ratio

$$
  I(w) = \frac{H_{20}(w)^3}{1728\, f_{12}(w)^5}
$$

is $A_5$-invariant — the **icosahedral equation**, i.e. the quotient map
$\mathbb{P}(V) \to \mathbb{P}(V)/A_5 = S^2(2,3,5)$. Its three branch values
$I = (\infty, 0, 1)$ occur at the vertex/face/edge orbits ($f_{12}=0$,
$H_{20}=0$, $T_{30}=0$) with cone orders $(5, 3, 2)$ — exactly the proved cone
structure. This is Klein's resolvent of the Bring–Jerrard quintic, anchored on
the corpus $\zeta_5$ pentad.

## The sole residual sliver — the spectral identification $\eta \leftrightarrow w$

With the group canonical, the orbifold proved, and the resolvent explicit, the
one remaining step is a *coordinate identification*: the $\zeta_5$ pentad acts on
the base ratio $z = x_0/x_1$ (and is exactly Klein's $S: w \mapsto \varepsilon
w$), while the colour trefoil acts on the **spectral ratios** $\eta$
([braid-group action](#rem:braid-group-action)). Establishing that the trefoil's
$\eta$-action is the icosahedral $3$-fold of *this* $A_5$ — i.e. that Klein's
resolvent identifies $\eta$ with $w$ — promotes the bridge to a theorem. It is
the lone open object (Lean class fields `proj_orbit_constant` /
`proj_separates_orbits`, no instance).

**Scope (unchanged).** Even fully established, this bridge sits on the geometric
/ $V_\lambda$ (icosahedral-selector) side of the Schur–Weyl duality: it
identifies and motivates the keystone $S^3/2I$ arena, but does **not** produce
the Hecke-side measure $W_\lambda$, its Schur–Weyl dual. The keystone
$W_\lambda$ closure remains the separate open problem.

## Scope

This bridge lives on the geometric / $V_\lambda$ (icosahedral-selector) side of
the Schur–Weyl duality. It **motivates** the keystone's $S^3/2I$ arena; it does
**not** by itself produce the Hecke-side measure $W_\lambda$, its Schur–Weyl
dual. Promotion to a theorem requires constructing the icosahedral-angle
generators on $\mathbb{P}(V)$ (Klein's resolvent) and identifying
$\mathbb{P}(V)/A_5$ with the keystone base — both open; the trefoil-generator
route is closed by the refutation above.
<!-- FILE_END: klein-bring-icosahedral-bridge.md -->

<!-- FILE_START: cohomological-embedding.md -->
The torus knots embeddable on the moduli surface $\Sigma_g$
of a QOU form a **complete set of representations** — they
exhaust the available cohomology and span the space of
knot observables.

## Statement

**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with moduli surface
$\Sigma_g$ of genus $g$ and Euler characteristic
$\chi = 2 - 2g$.*

**(i) Embeddability = representation.**
*A torus knot $T_{r,s}$ with $\gcd(r, s) = 1$ admits a
representation in $\mathbf{C}$ if and only if its Seifert
rank embeds in the first cohomology of $\Sigma_g$:*

$$
  \mathrm{rank} H_1(\mathrm{Seifert}(T_{r,s}))
  =  \frac{(r-1)(s-1)}{2}
   \leq  g
$$

**(ii) Fiber degree.**
*The knot $T_{r, p^k}$ acts at fiber degree $k$, where $p$
is prime.  On $\Sigma_g$, the maximum fiber degree is:*

$$
  k_{\max}(r, p, g)
  = 
  \max\!\left\{k : \frac{(r-1)(p^k - 1)}{2} \leq g\right\}
$$

*Degree $1$ knots define **shells**.  Degree $2$ knots define
**subshells**.  Degree $\geq 3$ knots, if embeddable, would
define sub-subshells.*

**(iii) Completeness.**
*The Jones polynomials of the embeddable torus knots, evaluated
in the irreducible representations of $H_2(q) \oplus H_3(q)$,
**span** the space of knot invariants on $\Sigma_g$.  Every
knot observable on $\Sigma_g$ is a linear combination
of evaluations of the embeddable torus knots.*

**(iv) Genus $4$ is forced.**
*The QOU axioms require:*
- *$T_{2,3}$ embeds (SU$_2$ reconstruction from trefoil structure):
  $(1)(2)/2 = 1 \leq g$.*
- *$T_{2,9} = T_{2,3^2}$ embeds (color-squared strong force, degree $2$):
  $(1)(8)/2 = 4 \leq g$.*
- *$T_{2,11}$ does NOT embed (no additional particles observed):
  $(1)(10)/2 = 5 > g$.*

*Therefore $g = 4$ and $\chi = 2 - 2(4) = -6$.*

## The 6 representations on $\Sigma_4$

For $g = 4$, the embeddability constraint $(r-1)(s-1) \leq 8$
with $\gcd(r, s) = 1$ and $2 \leq r < s$ yields exactly $6$
torus knots:

See [Table 1](#tbl:cohomological-embedding-table1-data).

The total Seifert rank used: $1 + 2 + 3 + 4 + 3 + 4 = 17$.
The available rank: $2g = 8$ (from $H^1(\Sigma_4) = \mathbb{Z}^8$).
The knots **overlap** in $H^1$ (they share Seifert cycles), so
$17 > 8$ does not contradict embeddability — each knot individually
fits within rank $\leq 4 = g$.

## Knot basis for $H^*(\Sigma_4)$

The cohomology of $\Sigma_4$ admits a **knot basis** — each
generator is identified with a specific knot-particle or force
operator.  The Hodge decomposition $H^1 = H^{1,0} \oplus H^{0,1}$
separates holomorphic (degree-$1$) from antiholomorphic
(degree-$2$) sectors:

$$
  H^*(\Sigma_4)
  = 
  \underbrace{H^0 \oplus H^2}_{\dim 2}
   \oplus 
  \underbrace{H^{1,0}}_{\dim 4}
   \oplus 
  \underbrace{H^{0,1}}_{\dim 4}
$$

See [Table 2](#tbl:cohomological-embedding-table2-data).

**Dimension count**: $\dim H^0 + \dim H^1 + \dim H^2 = 1 + 8 + 1 = 10$.  Euler characteristic: $\chi = 1 - 8 + 1 = -6$.  The $8$
generators of $H^1$ comprise $4$ holomorphic ($H^{1,0}$, degree-$1$
torus knots) and $4$ antiholomorphic ($H^{0,1}$, degree-$2$ knots
$+$ the amphichiral Higgs mass mechanism).

**Gravity** is not a knot — it is the categorical trace
$\int_A$ (the Frobenius pairing), operating at degree $0$.
It acts universally on all knot-particles.

**The Higgs mass mechanism** $4_1$ is the figure-eight knot:
the closure of the Borromean braid
$(\Delta_{\mathrm{mix}})^2 = (\sigma_0\sigma_1^{-1})^2$.
It is amphichiral ($4_1 = 4_1^{-1}$, its own antiparticle),
hyperbolic ($\mathrm{Vol}(4_1) = 2.0299$, giving mass), and
couples to every knot-particle with crossings $> 0$
(proportional to crossing count $=$ proportional to mass).
Massless knot-particles (photon: $0$ crossings, neutrino:
$0$ crossings) do not couple.  The open braid
$(\Delta_{\mathrm{mix}})^2$ gives the axial coupling
$g_A \approx 1.277$; the closed knot gives the mass mechanism.

The **Higgs boson** — the excitable scalar particle at
$\sim 125 \mathrm{GeV}$ — is separately identified with
the torus link $T(2,8)$
([Higgs as $T(2,8)$](#conj:higgs-t28)), a spin-$0$ boson
consistent with the fermion--boson decomposition
([fermion--boson knot--link](#prop:fermion-boson-knot-link)).
The two objects play complementary roles: $4_1$ is the
**mass mechanism** (the Higgs field condensate), while
$T(2,8)$ is the **mass boson** (the excitation of the field).

## Completeness via Jones polynomials

The Iwahori--Hecke algebras on the embeddable strand counts are:
- $H_2(q)$: $2$ irreducible representations (partitions of $2$:
  $(2)$ trivial, $(1,1)$ sign).  Dimension $2! = 2$.
- $H_3(q)$: $3$ irreducible representations (partitions of $3$:
  $(3)$ trivial, $(1,1,1)$ sign, $(2,1)$ standard of dimension
  $[2]_q$).  Dimension $3! = 6$.

Total irreps: $2 + 3 = 5$.

The Jones polynomial of a torus knot $T_{r,s}$ decomposes over
the irreps of $H_r(q)$ via the Markov trace:

$$
  V_{T_{r,s}}(q)
  = 
  \sum_{\lambda \vdash r}
  d_\lambda(q) \chi_\lambda(T_{r,s})
$$

where $d_\lambda$ is the $q$-dimension and $\chi_\lambda$ is the
character in irrep $\lambda$.

The $6$ embeddable knots, evaluated in the $5$ irreps, give a
$6 \times 5$ matrix $M_{ij} = \chi_{\lambda_j}(\sigma_i)$.  This
matrix has rank $5$ (= number of irreps, verified numerically).
Therefore the $6$ knot evaluations **span** the $5$-dimensional
space of irrep characters.

**Completeness**: any knot observable on $\Sigma_4$ is
a function of the irrep characters, which are spanned by the
$6$ torus knots.  No knot on $\Sigma_4$ can have an invariant
independent of $\{T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}, T_{3,4}, T_{3,5}\}$.

## Corollaries

1. **Particle finiteness**: the $6$ torus knots are the complete
   knot-particle content.  Every observable hadron is a composite
   of these $6$ building blocks $\mathcal{K}_{\tau(r,s)}$.  No
   additional knot-particles exist on $\Sigma_4$.

2. **Shell model completeness**: the nuclear orbital shell structure
   (magic numbers, subshells) is entirely determined by the
   knot invariants (products and crossing numbers) of these $6$
   representations.  No additional shell structure can arise.

3. **Interaction completeness (no other forces).**  Each embeddable
   torus knot $\tau(r,s)$ defines a transfer matrix
   $T_{\tau(r,s)}(q) \in \mathrm{M}_2(\mathbb{Z}[q^{\pm 1/2}])$
   — a **force operator** governing the interaction it mediates.
   The $7$ transfer matrices ($6$ non-trivial + the identity)
   exhaust the harmonic $1$-forms on $\Sigma_4$: every interaction
   between knot-particles is a composition of these $7$ operators.
   An $8$th would require an embeddable torus knot at genus $> 4$
   — contradicting the brane tower cohomology.  **There are exactly
   $7$ force operators (including free propagation), and we prove
   there can be no others.**

   | Transfer matrix | Knot-particle | Interaction |
   |:---:|:---:|:---|
   | $T_{\tau(1,0)}(q) = \mathbf{I}$ | $\mathcal{K}_\nu$ (unknot) | Free propagation (identity) |
   | $T_{\tau(2,3)}(q)$ | $\mathcal{K}_e$ (trefoil) | Mass / electromagnetic |
   | $T_{\tau(2,5)}(q)$ | $\mathcal{K}_{\tau(2,5)}$ | 2nd generation |
   | $T_{\tau(2,7)}(q)$ | $\mathcal{K}_c$ (charm) | 3rd generation |
   | $T_{\tau(3,5)}(q)$ | $\mathcal{K}_{\tau(3,5)}$ | Weak ($\beta$-decay vertex) |
   | $T_{\tau(2,9)}(q)$ | $\mathcal{K}_{\tau(2,9)}$ | Strong binding (degree-$2$ tower of trefoil) |
   | $T_{\tau(3,4)}(q)$ | $\mathcal{K}_t$ (top) | Hopf-squared binding (degree-$2$ tower of Hopf) |

4. **$\chi = -6$ is the unique solution**: genus $4$ is the
   unique genus that accommodates exactly $\mathrm{SU}_2$
   reconstruction + color-squared strong force + no extra
   knot-particles.  Any other genus gives either too few forces
   ($g < 4$: no strong binding) or too many knot-particles
   ($g > 4$: $\tau(2,11)$ embeds, predicting unobserved matter).
<!-- FILE_END: cohomological-embedding.md -->

<!-- FILE_START: knot-basis-color-content.md -->
The knot basis for $H^*(\Sigma_4)$ identifies the identity
$\mathbf{1} \in H_3(q)$ with the generator of $H^0(\Sigma_4)$. An
element of $H_3(q)$ of the form

$$
  \gamma
  = 
  \mathbf{1} + \varphi_0 \sigma_0 + \varphi_1 \sigma_1
  + \varphi_{01} \sigma_0\sigma_1,
  \qquad
  \varphi_0, \varphi_1, \varphi_{01} \in R,
$$

where $R$ is the ground ring $\mathbb{Z}[q^{\pm 1}]$ (or any
commutative ring over which the Iwahori--Hecke algebra is defined),
is called a **photon with color content**
$(\varphi_0, \varphi_1, \varphi_{01})$.
The identity $\mathbf{1}$ is the photon proper; the generators
$\sigma_0, \sigma_1$ contribute additive color dressing; the Hopf link
term $\varphi_{01}\sigma_0\sigma_1$ contributes Hopf link dressing.
Setting $\varphi_{01} = 0$ recovers the 3-term specialization used in
the derivations below.

Given two such elements (in the 3-term specialization
$\varphi_{01} = \psi_{01} = 0$)

$$
  \gamma_1 = \mathbf{1} + \varphi_0 \sigma_0 + \varphi_1 \sigma_1,
  \qquad
  \gamma_2 = \mathbf{1} + \psi_0 \sigma_0 + \psi_1 \sigma_1,
$$

with $\varphi_0, \varphi_1, \psi_0, \psi_1 \in R$ all
**independent formal variables**, the Gröbner--Shirshov normal form of
their product in $H_3(q)$ is computed by expanding all nine
terms and applying the Hecke relation
$\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$.

**Result.** Writing $h = q - q^{-1}$ for the Hecke
parameter,

$$
  \mathrm{NF}(\gamma_1 \cdot \gamma_2)
  = 
  \underbrace{(1 + \varphi_0\psi_0 + \varphi_1\psi_1)}_{\text{identity coeff.}}
  \cdot \mathbf{1}
  + 
  (\varphi_0 + \psi_0 + \varphi_0\psi_0h)
  \cdot \sigma_0
  + 
  (\varphi_1 + \psi_1 + \varphi_1\psi_1h)
  \cdot \sigma_1
  + 
  \varphi_0\psi_1 \cdot \sigma_0\sigma_1
  + 
  \varphi_1\psi_0 \cdot \sigma_1\sigma_0.
$$

The five NF basis elements are precisely the first five entries
of the knot basis (word length $\ell \leq 2$):

| Basis | Word | $\ell$ | NF coefficient |
|:---:|:---:|:---:|:---|
| $\mathbf{1}$ | $\mathbf{1}$ | $0$ | $1 + \varphi_0\psi_0 + \varphi_1\psi_1$ |
| $\sigma_0$ | $\sigma_0$ | $1$ | $\varphi_0 + \psi_0 + \varphi_0\psi_0h$ |
| $\sigma_1$ | $\sigma_1$ | $1$ | $\varphi_1 + \psi_1 + \varphi_1\psi_1h$ |
| $L_+$ | $\sigma_0\sigma_1$ | $2$ | $\varphi_0\psi_1$ |
| $L_-$ | $\sigma_1\sigma_0$ | $2$ | $\varphi_1\psi_0$ |

The net (sum of all NF coefficients) factors as:

$$
  \mathrm{net}(\gamma_1 \cdot \gamma_2)
  = 
  (1 + \varphi_0 + \varphi_1)(1 + \psi_0 + \psi_1)
  + 
  (\varphi_0\psi_0 + \varphi_1\psi_1)h.
$$

The first factor $(1 + \varphi_0 + \varphi_1)(1 + \psi_0 + \psi_1)$
is the product of the total weights of the two elements.  The
correction term $(\varphi_0\psi_0 + \varphi_1\psi_1)h$
arises from the Hecke self-energy $\sigma_i^2 \neq \mathbf{1}$.

**Observability by word length.**  The Hopf-link terms
$L_{\pm} = \sigma_0\sigma_1$ and $\sigma_1\sigma_0$ (word
length $\ell = 2$) arise exclusively from **cross-color** products:
$\varphi_0\psi_1$ and $\varphi_1\psi_0$ respectively. They
vanish whenever both elements share the same color axis
($\varphi_1 = \psi_1 = 0$ or $\varphi_0 = \psi_0 = 0$).
The word-length $\ell = 1$ terms $\sigma_0, \sigma_1$ include
both additive contributions $(\varphi_i + \psi_i)$ and
Hecke self-energy corrections $(\varphi_i\psi_ih)$.

**Independence of color weights.** Each $\varphi_i$ and
$\psi_j$ is independent in $R$: the NF formula is a polynomial
identity in four formal variables over $R[h]$.
Setting $\varphi_0 = \varphi_1 = \psi_0 = \psi_1 = 0$
recovers $\gamma_1 \cdot \gamma_2 = \mathbf{1}$ (the product
of two bare photons is the identity).
<!-- FILE_END: knot-basis-color-content.md -->

<!-- FILE_START: trivial-knot-photon-interpretation.md -->
The trivial knot operator $T_{1,0}$ has braid word
$\beta = \mathbf{1}$, so a photon pair collision under $T_{1,0}$
is the raw Hecke product $\gamma_1 \cdot \gamma_2$ with
no crossings inserted between the two photons. Every structure
that appears in the output comes from the color content the photons
already carry. The knot operator contributes nothing --- it lets
the photons talk to each other, and nothing more.

## The sixteen cross-products

Writing $\gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
+ \varphi_{01}\sigma_0\sigma_1$ and
$\gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1
+ \psi_{01}\sigma_0\sigma_1$, the product $\gamma_1 \cdot \gamma_2$
expands into $4 \times 4 = 16$ cross-terms. Each is an elementary
Hecke product that reduces to normal form via the Hecke relation
$\sigma_i^2 = h\sigma_i + \mathbf{1}$ (where $h = q - q^{-1}$) and the Yang--Baxter relation
$\sigma_1\sigma_0\sigma_1 = \sigma_0\sigma_1\sigma_0 = e^-$.

### Block I: the photon core ($\mathbf{1}$) meets everything

See [Table 1](#tbl:trivial-knot-photon-interpretation-table1-data).

The photon identity $\mathbf{1}$ is the unit of the algebra:
it transmits everything it encounters without modification.
Physically, the "pure photon" component of one photon is
transparent to the other.

### Block II: horizontal polarization ($\varphi_0\sigma_0$) meets everything

See [Table 2](#tbl:trivial-knot-photon-interpretation-table2-data).

### Block III: vertical polarization ($\varphi_1\sigma_1$) meets everything

See [Table 3](#tbl:trivial-knot-photon-interpretation-table3-data).

### Block IV: Hopf dressing ($\varphi_{01}\sigma_0\sigma_1$) meets everything

See [Table 4](#tbl:trivial-knot-photon-interpretation-table4-data).

## Collecting by output channel

Summing all 16 terms by NF basis element recovers the full
$T_{1,0}$ formula:

See [Table 5](#tbl:trivial-knot-photon-interpretation-table5-data).

## Physical interpretation of each channel

**Vacuum channel ($\gamma$):**
The coefficient $1 + \varphi_0\psi_0 + \varphi_1\psi_1$ is always
at least $1$ (from $\mathbf{1} \cdot \mathbf{1}$) and grows with
**co-polarized** content. The $\varphi_0\psi_0 + \varphi_1\psi_1$
correction is a dot product of the two photons' linear polarization
vectors. Photons with aligned polarization amplify the vacuum
channel --- they reinforce each other's identity. Note that
$\varphi_{01}$ does not appear: Hopf dressing does not feed the
vacuum.

**Linear polarization channels ($\sigma_0$, $\sigma_1$):**
Each has three sources: (i) additive pass-through from each photon
($\varphi_i + \psi_i$), (ii) Hecke self-energy from same-axis
collision ($\varphi_i\psi_i h$), and (iii) a twist-rotation term
where the Hopf dressing of one photon emits the orthogonal
polarization of the other ($\varphi_{01}\psi_1$ for $\sigma_0$;
$\varphi_0\psi_{01}$ for $\sigma_1$). The first two are
symmetric between the two photons; the third is not.

**Positive Hopf link ($L_+$):**
Five contributing terms versus two for $L_-$. The asymmetry arises
because the photon's own Hopf term is $\sigma_0\sigma_1 = L_+$
(not $L_-$), so it preferentially feeds the $L_+$ channel via
direct contributions (terms 4, 13) and Hecke corrections
(terms 8, 15). The cross-polarization term $\varphi_0\psi_1$
(term 7) also feeds $L_+$ because $\sigma_0 \cdot \sigma_1 = L_+$.

**Negative Hopf link ($L_-$):**
Only two sources: cross-polarization in the reversed order
$\varphi_1\psi_0$ (term 10, where $\sigma_1 \cdot \sigma_0 = L_-$)
and the Hopf self-product $\varphi_{01}\psi_{01}$ (term 16).
The $L_+/L_-$ asymmetry is a chirality signature: the two Hopf
link orientations are not equally accessible because the photon's
internal twist has a definite handedness.

**Electron channel ($e^-$):**
Entirely absent in the 3-term specialization ($\varphi_{01} =
\psi_{01} = 0$). Opens only when at least one photon carries Hopf
dressing, through three distinct mechanisms:

1. **$L_+ \cdot \sigma_0 = e^-$** (term 14): the Hopf dressing of
 photon 1 combines with the horizontal crossing of photon 2 to
 complete a trefoil.

2. **$\sigma_1 \cdot L_+ = e^-$** (term 12): the vertical crossing
 of photon 1 combines with the Hopf dressing of photon 2 via
 Yang--Baxter.

3. **$L_+ \cdot L_+ \ni he^-$** (term 16): two Hopf dressings
 collide, producing an electron suppressed by $h \approx 0.209$.

In all three cases, the trefoil $e^- = \sigma_0\sigma_1\sigma_0$
forms because one photon supplies two of the three crossings (via
$L_+ = \sigma_0\sigma_1$) and the other supplies the remaining
one ($\sigma_0$ or $\sigma_1$).

## Cancellation conditions

**Trivial-output condition.**
If $\varphi_0 = \varphi_1 = \varphi_{01} = \psi_0 = \psi_1 =
\psi_{01} = 0$ (two bare photons), then
$\gamma_1 \cdot \gamma_2 = \mathbf{1}$. Light passes through
light. All channels except $\gamma$ vanish.

**Vanishing of the Hopf links.**
$L_+$ and $L_-$ both vanish when the photons are co-polarized on a
single axis (e.g., $\varphi_1 = \psi_1 = \varphi_{01} = \psi_{01}
= 0$). Co-polarized photons reinforce their shared polarization
and feed the vacuum, but they cannot link. Linear plus linear
produces more linear --- never circular.

**Vanishing of the electron channel.**
$e^- = 0$ whenever $\varphi_{01} = \psi_{01} = 0$ (no Hopf
dressing on either photon). The trivial knot operator **cannot
produce electrons from photons that carry only linear
polarization**. The twist content ($\sigma_0\sigma_1$) is the
essential pre-condition: it supplies two of the three crossings
needed for a trefoil, and the remaining single crossing comes from
the other photon's linear polarization.

**Vanishing of the $L_+/L_-$ asymmetry.**
For two photons that each carry only Hopf dressing and no linear
polarization ($\varphi_0 = \varphi_1 = \psi_0 = \psi_1 = 0$,
$\varphi_{01}, \psi_{01} \neq 0$), the $L_+$ coefficient is
$\varphi_{01} + \psi_{01}$ and the $L_-$ coefficient is
$\varphi_{01}\psi_{01}$. The asymmetry persists: $L_+$ is additive
(each Hopf dressing contributes independently) while $L_-$ is
multiplicative (requires both to interact). The asymmetry
disappears only when $\varphi_{01} = \psi_{01} = 0$, i.e., when
there is no twist content at all.

## The twist as polarization rotator

Terms (8) and (15) reveal a striking pattern: when Hopf dressing
meets linear polarization, the Hecke relation absorbs the
same-axis crossing and emits the **orthogonal** polarization.
Specifically:

- $\sigma_0 \cdot L_+ = \sigma_0^2\sigma_1 = h L_+ + \sigma_1$:
 horizontal in, vertical out.
- $L_+ \cdot \sigma_1 = \sigma_0\sigma_1^2 = h L_+ + \sigma_0$:
 vertical in, horizontal out.

The Hopf link acts as a $90°$ polarization rotator. The residual
$hL_+$ term is the "cost" of the rotation --- some twist content
is retained, reduced by the Hecke parameter $h$. This is the
mechanism by which circular polarization (Hopf dressing) converts
between linear polarization axes.
<!-- FILE_END: trivial-knot-photon-interpretation.md -->

<!-- FILE_START: outro-archimedean-universe.md -->
This closes the Descartes-universe chapter — the archimedean
realisation of the QOU programme.  Bring's surface
($\chi = -6$) has been fixed as the spacetime base; the
substrate parameter $q_0 \approx 1.1097$ acquires a numerical
value via the cohomological-defect / pair-production /
nucleon-stability arc; the EM completeness and gauge-coupling
section pins $\alpha_{\mathrm{EM}}$; and the orbital-symmetry
embedding records the five-fold-symmetric basis that the
particle-interactions chapter consumes as its native frame.

The next chapter (particle interactions and nuclear structure)
takes the assignments fixed here — meson / proton / neutron /
stable-isotope torus knots — and computes their interactions
under the Gröbner–Shirshov / linear-program / SDP-as-thimble
machinery.  The orbital-symmetry frame closing this chapter is
the substrate-level basis those computations are evaluated in.
<!-- FILE_END: outro-archimedean-universe.md -->

