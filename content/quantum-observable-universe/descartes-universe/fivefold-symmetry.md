The Bring surface $\Sigma_4$ (genus $4$, Euler characteristic
$\chi = -6$) has automorphism group $S_5$, the symmetric group
on $5$ elements.  This $5$-fold symmetry is not a coincidence —
it is the deepest structural feature of the QOU and has
consequences at every level of the theory.

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

| Order | Compatible with lattice? | QOU structure |
|:-----:|:---:|:---:|
| $2$ | Yes | $\mathbb{Z}/2$ crossing sign ($q \leftrightarrow q^{-1}$) |
| $3$ | Yes | Borromean $\mathcal{B}_3$ (color $\mathrm{SU}(3)$) |
| $4$ | Yes | Genus $g = 4$ of the Bring surface |
| $5$ | **No** | $S_5$ automorphism, $T_{3,5}$ weak vertex |
| $6$ | Yes | $\chi = -6$ (Euler characteristic) |

The $5$-fold symmetry of the Bring surface is **the unique
symmetry that breaks periodicity**.  It is carried by $T_{3,5}$,
the weak force mediator — the only force that violates parity
($q \neq q^{-1}$ accumulated over $10 = \binom{5}{2}$ crossings)
and the only force with massive carriers ($W^{\pm}$, $Z^0$).
The weak force is weak precisely because $5$-fold symmetry
cannot propagate through a lattice — it is confined to local,
aperiodic interactions.

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
so the full $5$-fold symmetry is recovered by encircling all
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

## Beyond shell dynamics

The $5$-fold symmetry appears at every scale:

| Scale | $5$-fold manifestation | Mathematical home |
|:---:|:---:|:---:|
| Substrate | $5$ sheets of $\Sigma_4$ | Bring curve $S_5$ |
| Particles | $6$ embeddable torus knots | Genus $4$ embedding |
| Quarks $\to$ leptons | $T_{3,5}$ weak vertex | Cross-family mediator |
| Nuclear shells | $5$ orbital channels ($\ell = 0$–$4$) | Standard rep of $H_3(q)$, phase $153.6°$ |
| Shell dynamics | $[A\!-\!1]_q! > [2]_q^{A-1}$ at $A = 5$ | Finiteness bound |
| Information | $P_{7,6}(q)$ zero at $q = 1/\varphi^2$ | Golden ratio phase transition |
| Macroscopic | Quasicrystals, icosahedral viruses | Crystallographic obstruction |

The $3$-fold symmetry (Borromean, color, lattice-compatible)
and $5$-fold symmetry (aperiodic, weak, parity-violating) are
the two irreducible components of the Bring surface structure.
The interplay between them — mediated by $T_{3,5}$ — generates
the full complexity of the physical world: the strong force
binds (periodically), the weak force transforms (aperiodically),
and the electromagnetic force (the involutive $2$-fold structure)
measures the interface.
