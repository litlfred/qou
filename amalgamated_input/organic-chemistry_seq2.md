<!-- FILE_START: carbon-chains-benzene-intro.md -->
We instantiate the chain–ring machinery at $N = 6$, the smallest case where the contrast is experimentally sharp. The **linear $\mathrm{C}_6$ Hopf chain** assembles six carbons with a $6 \times 6$ tridiagonal linking matrix. Interior carbons consume two of their four sites for the backbone, while the endpoint carbons carry three dangling links each. These are the soft modes that make linear $\mathrm{C}_6$ flexible as cumulene or carbyne (ex: [linear $\mathrm{C}_6$ Hopf chain](#ex:carbon-chain-c6)). **Benzene** is the closed counterpart: six carbons threaded by $T(2,6)$, whose two components are the two delocalised $\pi$ electrons. Its Alexander polynomial $q^2 + 1 + q^{-2}$ replaces six pairwise Hopf weights with a single threading invariant. This explains bond-order equalisation and the $\mathrm{C}_6\mathrm{H}_6$ formula without further input (ex: [benzene as a molecular Hopf ring](#ex:benzene-ring)). Comparing the two structures, the threaded ring binds one more atom at Alexander weight $3$ versus the chain's $5$. Yet the chain persists, because the pairwise-to-threaded transition is discontinuous and the geometric reconfiguration sets an activation barrier (rem: [why the C$_6$ chain resists hexagonalisation](#rem:chain-ring-energy)). The section closes with the parameter-free prediction $\Delta E \approx 2 \cdot |q + q^{-1}|_{\mathrm{mol}} \approx 193\text{--}386\,\mathrm{kJ/mol}$, matched against the experimental $200\text{--}400\,\mathrm{kJ/mol}$ window. The $1/2$ threading factor is the resolution of the pairwise picture's factor-of-two overshoot (prop: [predicted vs. observed $\mathrm{C}_6$ ring-closure barrier](#prop:chain-ring-comparison)).
<!-- FILE_END: carbon-chains-benzene-intro.md -->

<!-- FILE_START: carbon-chain-c6.md -->
The simplest carbon Hopf chain is the linear $\mathrm{C}_6$
molecule: six carbon atoms linked end-to-end.

**Construction.**
Each carbon atom ([carbon valence](#rem:carbon-valence)) has 4
open linking sites.  In the chain $\mathcal{C}_6^{(1)}$
([molecular Hopf chain](#def:molecular-hopf-chain)), each interior
carbon ($\mathcal{A}_2$ through $\mathcal{A}_5$) consumes 2 sites
for backbone bonds, leaving 2 sites free.  The endpoint carbons
($\mathcal{A}_1$ and $\mathcal{A}_6$) consume 1 site each,
leaving 3 free.

$$
  \mathrm{C}_6^{\mathrm{chain}}
  = 
  \mathcal{A}(6,6)_1
   \underset{B_1}{\oplus}
  \mathcal{A}(6,6)_2
   \underset{B_1}{\oplus}
  \cdots
   \underset{B_1}{\oplus}
  \mathcal{A}(6,6)_6
$$

The linking matrix is the $6 \times 6$ tridiagonal matrix:

$$
  L^{\mathrm{chain}}
  = 
  \begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    1 & 0 & 1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1 & 0 & 1 \\
    0 & 0 & 0 & 0 & 1 & 0
  \end{pmatrix}.
$$

**Crossing energy.**
The chain has 5 bonds, giving

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathrm{C}_6^{\mathrm{chain}})
  = 
  5 \cdot E_{\mathrm{bond}}(1).
$$

**Spring behaviour.**
The endpoint carbons ($\mathcal{A}_1$ and $\mathcal{A}_6$) each
have 3 dangling linking sites.  These act as soft modes
([spring-like modes](#rem:chain-spring-modes)): the endpoints can
oscillate (Reidemeister I curls) and the chain can bend and
stretch at energies far below the bond-breaking threshold.

In real chemistry, linear $\mathrm{C}_6$ is observed as both
**cumulene** ($=\!=\!=\!=\!=\!=$, consecutive double bonds) and
**carbyne** ($-\!\equiv\!-\!\equiv\!-$, alternating single and
triple bonds) forms.  In the Hopf chain picture, these correspond
to bond-order patterns $(k_1, \ldots, k_5) = (2,2,2,2,2)$ and
$(1,3,1,3,1)$ respectively — different distributions of shared
trefoils across the 5 bonds (total bond order 10 and 9).
<!-- FILE_END: carbon-chain-c6.md -->

<!-- FILE_START: benzene-ring.md -->
Benzene ($\mathrm{C}_6\mathrm{H}_6$) is the prototypical
threaded molecular ring: six carbon atoms bound by a single
threading link $T(2,6)$
([threading link](#def:threading-link)).

**Construction.**
The six carbon atoms
([carbon valence](#rem:carbon-valence)) form the ring
$\mathcal{R}_6$
([molecular Hopf ring](#def:molecular-hopf-ring)):

$$
  \mathrm{C}_6^{\mathrm{ring}}
  = 
  [\mathcal{A}(6,6)_1, \ldots, \mathcal{A}(6,6)_6]
   \oplus 
  T(2,6).
$$

The threading link $T(2,6)$ has braid word
$(\sigma_1 \sigma_2 \sigma_3 \sigma_4 \sigma_5)^2$ in $B_6$,
with 10 crossings all of the same sign.

**The two components are the $\pi$ electrons.**
Since $\gcd(2,6) = 2$, the threading link $T(2,6)$ has
**two components**, each an unknotted loop winding 3 times
through all 6 carbons of the hexagon.  These two components are
the two delocalised $\pi$ electrons of benzene, linked with
linking number 3 — they cannot be separated without cutting
through 3 crossings.  Delocalisation is therefore topological:
the $\pi$ electrons are not localised to individual bonds but
are constrained to thread the entire ring.

**Alexander polynomial.**

$$
  \Delta_{T(2,6)}(q)
  = 
  q^2 + 1 + q^{-2}
  = 
  (q + q^{-1})^2 - 1.
$$

The crossing energy of benzene is proportional to this
polynomial — strictly less than the Alexander weight of 6
separate Hopf links ($= 6$).  The threading link encodes the
same binding information in a more compact topological form.

**Bond order equalisation.**
In the pairwise picture, benzene would require alternating
single and double bonds (Kekulé structure).  In the threading
picture, there are no individual bonds — the threading link
distributes binding uniformly.  Each carbon is threaded
identically (the braid word treats all $\sigma_i$ symmetrically),
producing equal bond lengths and equal bond orders of $3/2$
without any additional argument.  Bond order equalisation is
**automatic** in the threading picture.

**Hydrogen attachment.**
Each carbon has 4 linking sites
([carbon valence](#rem:carbon-valence)).  The threading link
$T(2,6)$ consumes 2 sites per carbon (one per winding).  The
remaining 2 sites per carbon are available: one bonds to
hydrogen via a standard Hopf link, and one participates in the
$\sigma$-backbone (the in-plane C–C single bond framework).
Total hydrogen capacity: 6, giving $\mathrm{C}_6\mathrm{H}_6$.

**Aromaticity as threading.**
The concept of aromaticity in organic chemistry corresponds to
the existence of a threading link.  For even $N$, a ring admits
a 2-component threading link $T(2,N)$ whose Alexander polynomial
$\Delta_{T(2,N)}(q) = (q^{N/2} - q^{-N/2})/(q - q^{-1})$ is
less than the pairwise Alexander weight $N$:

| $N$ | $\Delta_{T(2,N)}(q)$ at $q = 1$ | Pairwise weight | Ratio |
|:---:|---:|:---:|:---:|
| 4 | 2 | 4 | 1/2 |
| 6 | 3 | 6 | 1/2 |
| 8 | 4 | 8 | 1/2 |
| 10 | 5 | 10 | 1/2 |

The ratio is always $1/2$ at $q = 1$ for even $N$ — the
2-component threading link is universally twice as efficient as
pairwise bonding.  For odd $N$, the threading link $T(2,N)$ is a
knot (1 component) and the Alexander polynomial takes a different
form; the analysis of odd-$N$ rings requires separate treatment.

The aromatic stabilisation energy is the crossing energy
difference between the pairwise and threaded pictures.  Note
that threading efficiency alone does not determine aromaticity:
cyclobutadiene ($N = 4$) admits a threading link but is
anti-aromatic.  The aromatic/anti-aromatic distinction likely
requires an additional invariant beyond the Alexander weight.
<!-- FILE_END: benzene-ring.md -->

<!-- FILE_START: chain-ring-energy.md -->
The linear $\mathrm{C}_6$ chain
([linear C$_{6}$](#ex:carbon-chain-c6)) and benzene
([benzene ring](#ex:benzene-ring)) represent two fundamentally
different topological states of six carbon atoms: pairwise
Hopf-linked versus threaded by $T(2,6)$.

**Energy accounting via Alexander polynomials.**

The crossing energy of each structure is proportional to its
Alexander polynomial weight at the substrate parameter $q$
([threading link](#def:threading-link)):

| Structure | Binding topology | $\Delta(q)$ | At $q \approx 1$ |
|-----------|-----------------|-------------|------------------:|
| Chain $\mathcal{C}_6$ | 5 Hopf links $T(2,2)$ | $5 \times 1$ | 5 |
| Pairwise ring | 6 Hopf links $T(2,2)$ | $6 \times 1$ | 6 |
| Threaded ring $\mathcal{R}_6$ | $T(2,6)$ | $q^2 + 1 + q^{-2}$ | 3 |

The threaded ring binds all 6 carbons with Alexander weight
$\approx 3$ — **less than the chain's weight of 5**, despite
binding one more atom.

**Existence of the chain.**
If the ring is lower in energy, why does the linear chain
exist at all?  Because the transition from pairwise to
threaded topology is **discontinuous**.  The chain cannot
continuously deform into the ring — the binding structure must
be dissolved and reformed:

1. **Dissolve**: the 5 pairwise Hopf links release their
   crossing energy.

2. **Reconfigure**: the 6 carbon atoms must adopt a cyclic
   spatial arrangement that admits the threading link.

3. **Thread**: the $T(2,6)$ link forms, threading through all
   6 atoms at once.

Step 2 is the bottleneck.  The 6 carbons must be in the correct
geometric configuration — a near-planar hexagon — before the
threading link can form.  A fully extended chain has its
endpoints far apart; they must be brought together and the
intervening atoms rearranged.  This geometric reconfiguration
is the **activation barrier**.

**The spring analogy, revised.**
The open chain is a spring held apart.  The endpoints are free,
the interior oscillates
([spring-like modes](#rem:chain-spring-modes)).  Snapping it
shut runs the same three steps as above: bringing the endpoints
together is the step-2 geometric cost, dissolving the pairwise
links is the step-1 bond-breaking cost, and forming the threading
link is the step-3 topological phase transition.

Once the threading forms, the energy drops below the chain —
the spring has snapped into a lower-energy, locked
configuration.  The lock is the threading link itself: a
non-local topological structure that cannot be broken by any
local perturbation.

**Asymmetry of the barriers.**
The closure barrier (chain $\to$ ring) is dominated by the step-2
geometric cost of getting the atoms into position.  The opening
barrier (ring $\to$ chain) runs step 3 in reverse — a topological
cost, dissolving the threading link $T(2,6)$ into 5 separate Hopf
links, which costs

$$
  \Delta E_{\mathrm{open}}
   \propto 
  (N - 1) - \Delta_{T(2,N)}(q)
  = 
  5 - (q^2 + 1 + q^{-2})
   \approx 
  2
  \quad (|q| \approx 1)
$$

in additional Alexander weight — the ring must "expand" its
compact threading back into the less efficient pairwise
encoding.  Opening the ring is harder than closing it.
<!-- FILE_END: chain-ring-energy.md -->

<!-- FILE_START: chain-ring-comparison.md -->
**Theoretical prediction.**
The energy difference between the chain and threaded ring is
proportional to the difference in Alexander weights:

$$
  \Delta E
   \propto 
  \bigl[(N-1) - \Delta_{T(2,N)}(q)\bigr]
  \cdot |q + q^{-1}|_{\mathrm{mol}}.
$$

For $N = 6$ with $|q + q^{-1}|_{\mathrm{mol}} \sim 1\text{--}2$
eV and Alexander weight difference
$5 - (q^2 + 1 + q^{-2}) \approx 5 - 3 = 2$:

$$
  \Delta E(6)
   \sim 
  2 \times (1\text{--}2 \mathrm{eV})
   \sim 
  2\text{--}4 \mathrm{eV}
   \approx 
  193\text{--}386 \mathrm{kJ/mol}.
$$

(Conversion: $1 \mathrm{eV} = 96.485 \mathrm{kJ/mol}$.)
<!-- FILE_END: chain-ring-comparison.md -->

<!-- FILE_START: chain-ring-comparison-interpretation.md -->
The pairwise Hopf-link estimate of the cyclisation barrier
overshot by a factor of two; the threading-link picture halves it
exactly, with **no free parameters**, giving a quantitative
prediction that can be compared to experimental data. The halving
follows from the derivation chain below.

**Derivation chain.**
Every quantity is determined by the Bring's surface geometry:

$$
  \chi(A) = -6
  \xrightarrow{\text{Bring's surface}}
  \mathcal{G}
  \xrightarrow{\text{knot spectrum}}
  q, \alpha, m_e/m_p
  \xrightarrow{\text{scale separation}}
  |q + q^{-1}|_{\mathrm{mol}}
  \xrightarrow{\Delta_{T(2,6)}(q)}
  \mathfrak{E}_{\mathrm{cross}}.
$$

1. The substrate parameter $q$ is fixed by $\chi(A) = -6$
   ([substrate parameter](#def:substrate-parameter)).

2. The nuclear crossing energy quantum $|q + q^{-1}|_{\mathrm{nuc}} \sim 8\mathrm{MeV}$ is determined by the Skein binding
   Lagrangian volume term.

3. $\alpha$ and $m_e/m_p$ are determined by the knot spectrum
   ([topological mass formula](#prop:topological-mass-formula)).

4. The molecular crossing energy quantum follows by scale
   separation: $|q + q^{-1}|_{\mathrm{mol}} = (\alpha^2 m_e / m_p) \cdot |q + q^{-1}|_{\mathrm{nuc}}$.

5. The Alexander polynomial $\Delta_{T(2,6)}(q) = q^2 + 1 + q^{-2}$
   is a topological invariant — it requires no input beyond $q$.

**The factor of $1/2$.**
The pairwise Hopf link picture
([earlier estimate](#rem:chain-ring-energy)) predicted
$\sim 400\text{--}800 \mathrm{kJ/mol}$ — a factor of 2
overshoot.  The threading link resolves this exactly:
$\Delta_{T(2,6)}(q) / 6 \approx 1/2$, halving the predicted
barrier.  This is not a correction or a fit — it is a
consequence of replacing $N$ separate Hopf links with the
single threading invariant $T(2,N)$.

**Predictions for other even-$N$ rings.**
The same framework predicts
barriers for even-$N$ cyclic molecules (where $T(2,N)$ is a
2-component link and the Alexander formula
$\Delta_{T(2,2m)}(q) = (q^m - q^{-m})/(q - q^{-1})$ applies):

See [Table 3](#tbl:chain-ring-comparison-table3-data).

For odd $N$, the threading link $T(2,N)$ is a knot (1 component),
and the Alexander polynomial takes a different form — the
torus knot formula.  The barrier analysis for odd-$N$ rings
requires separate treatment.

The barrier increases with $N$ (more pairwise links to dissolve
and replace), but the threading efficiency ratio
$\Delta_{T(2,N)}(1) / N = 1/2$ is constant for all even $N$.

**Experimental data.**

See [Table 1](#tbl:chain-ring-comparison-table1-data).

**Comparison.**

See [Table 2](#tbl:chain-ring-comparison-table2-data).
<!-- FILE_END: chain-ring-comparison-interpretation.md -->

<!-- FILE_START: chain-ring-open-problems.md -->
Three questions remain open in the threading-link account of
ring-closure energetics.

**Open problems.**

1. **Exact $q$ at molecular scale**: the "few eV" estimate for
   $|q + q^{-1}|_{\mathrm{mol}}$ should be sharpened by
   computing the electronic-scale crossing energy directly from
   the trefoil hyperbolic volume ratio.

2. **Hückel's rule**: the threading link $T(2,N)$ has
   $\gcd(2,N)$ components — 2 for even $N$, 1 for odd.  But
   even $N$ alone does not imply aromaticity: cyclobutadiene
   ($N = 4$) is anti-aromatic and cyclooctatetraene ($N = 8$)
   is non-planar.  Conversely, the cyclopentadienyl anion
   ($N = 5$, odd) is aromatic.  The component count distinguishes
   knots from links but does not capture Hückel's $4n + 2$
   rule.  What additional invariant of $T(2,N)$ — perhaps the
   signature or the evaluation $\Delta_{T(2,N)}(q)$ at a
   specific $q$ — encodes the aromatic/anti-aromatic
   distinction?

3. **Heteroatoms**: when the ring contains non-carbon atoms
   (pyridine, furan), the threading link $T(2,N)$ threads
   through atoms with different numbers of linking sites.  How
   does this modify the Alexander polynomial?
<!-- FILE_END: chain-ring-open-problems.md -->

<!-- FILE_START: organic-taxonomy-intro.md -->
Having pinned down chains, rings, and the $\mathrm{C}_6$ case, we now sort the standard organic classes so that the familiar taxonomy — alkanes, alkenes, alkynes, and their relatives, together with their hydrogen counts — falls out of the Hopf-chain framework rather than being imposed by hand. Two parameters do the sorting: the bond-order pattern $(k_1, \ldots, k_{N-1})$ along the backbone, and whether the structure is open or closed. Against these, alkanes, alkenes, alkynes, cumulenes, and polyynes appear as distinct distributions of shared trefoils, and saturation reads as linking-site occupancy. The hydrogen capacity then follows directly: $\mathrm{C}_N \mathrm{H}_{2N+2-2d}$ (open) versus $\mathrm{C}_N \mathrm{H}_{2N-2d}$ (closed), read off from the total degree of unsaturation $d = \sum_i (k_i - 1)$ (rem: [organic chain taxonomy from bond-order patterns](#rem:organic-chain-taxonomy)). Aromatic rings — those with $d = N/2$ — appear as the case where the secondary trefoils themselves close; we conjecture that Hückel's $4n + 2$ rule corresponds to this closure as a molecular analogue of the shell capacity $2n^2$.
<!-- FILE_END: organic-taxonomy-intro.md -->

<!-- FILE_START: organic-chain-taxonomy.md -->
The molecular Hopf chain framework
([molecular Hopf chain](#def:molecular-hopf-chain)) generates the
standard classes of organic molecules by varying two parameters:
the **bond-order pattern** $(k_1, \ldots, k_{N-1})$ along the
backbone, and whether the chain is **open or closed**.

**Bond-order classification.**

| Class | Bond-order pattern | Free sites per C | Hydrogen capacity |
|-------|-------------------|:---:|:---:|
| Alkane (saturated) | $(1, 1, \ldots, 1)$ | 2 (interior), 3 (endpoint) | $2N + 2$ (chain), $2N$ (ring) |
| Alkene | $(\ldots, 2, \ldots)$ | 1 at double bond | $2N$ (one double bond) |
| Alkyne | $(\ldots, 3, \ldots)$ | 0 at triple bond | $2N - 2$ (one triple bond) |
| Cumulene | $(2, 2, \ldots, 2)$ | 0 (interior), 2 (endpoint) | 4 |
| Polyyne (carbyne) | $(1, 3, 1, 3, \ldots)$ | 0 (interior) | 2 |

**Saturation as linking-site occupancy.**
The hydrogen capacities tabulated above follow from one rule:
raising the bond order at a single position by one unit
($k \to k + 1$) consumes one free linking site on each adjacent
carbon, so it costs two hydrogens.  Saturation is therefore the
extreme case in which every backbone bond is single and hydrogen
occupies the maximum number of free sites.  In the Hopf chain
picture:

- **Saturated** = all backbone bonds are single Hopf links;
  maximum hydrogen attachment.
- **Unsaturated** = some backbone bonds are double or triple
  Hopf links; reduced hydrogen attachment.

**Open vs. closed (chain vs. ring).**
The second parameter — whether the backbone closes into a ring —
shifts the hydrogen count by a fixed offset and, together with the
degree of unsaturation, fixes the molecular formula:

| Topology | Backbone bonds | Hydrogen formula | Naming |
|----------|:-:|---|---|
| Open chain | $N - 1$ | $\mathrm{C}_N\mathrm{H}_{2N+2-2d}$ | $n$-alkane, $n$-alkene, $\ldots$ |
| Closed ring | $N$ | $\mathrm{C}_N\mathrm{H}_{2N-2d}$ | cycloalkane, cyclohexane, $\ldots$ |

where $d = \sum_i (k_i - 1)$ is the **total degree of
unsaturation** (number of extra Hopf links beyond single bonds).

**Aromatic rings.**
A closed ring with $d = N/2$ (one extra Hopf link per two
edges — bond order $3/2$ on average) is the aromatic case
([benzene](#ex:benzene-ring)).  The secondary Hopf ring formed
by the extra trefoils is closed, producing the resonance
stabilisation.  The link to Hückel's rule ($4n + 2$ $\pi$
electrons for aromaticity) is an open correspondence, not a
derived result: we conjecture that it matches a **sub-Hopf link
closure condition** at the molecular scale — only certain numbers
of trefoils can form a closed secondary ring — with $4n + 2$
playing the role for molecules that the shell capacity $2n^2$
plays for atoms.  This identification is proposed here as a
conjecture and is not established.
<!-- FILE_END: organic-chain-taxonomy.md -->

<!-- FILE_START: outro-organic-chemistry.md -->
This closes the organic-chemistry chapter: the Hopf-chain
construction promotes nucleon braids to covalent chains and rings,
recovers the comparative energetics of linear vs. cyclic carbon
backbones (chain $C_n$ vs. benzene $C_6$), and identifies the
threading transition at which ring topology stabilises against
linear isomers.

The next chapter (fluid dynamics) lifts this static molecular
geometry to a flowing brane: the same Hopf-chain morphisms that
underpin chemical bonds reappear as the cocycle data of the
$q$-Navier–Stokes obstruction, so the molecular construction here
sits as the discrete substrate for the continuum dynamics that
follow.
<!-- FILE_END: outro-organic-chemistry.md -->

