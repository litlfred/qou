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
