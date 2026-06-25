Quarks are not fundamental knots.  A quark is a **neutrino
(unknot) trapped in a color tube of Bring's surface,
Borromean-linked with two other unknots** in the exceptional
divisor.

**Conjecture.**
*The baryon is the Borromean link $\mathcal{B}_3$ of three
unknots threaded through the color tubes $(r, g, b)$ of the
Bring's surface ([color tube coordinates](#def:color-tube-coordinates)),
bound by the Hopf link $\mathcal{L}_H$:*

$$
  \mathfrak{p}
  = 
  \mathcal{B}_3(\nu_r, \nu_g, \nu_b)
   \oplus  \mathcal{L}_H
$$

*where $\nu_r$, $\nu_g$, $\nu_b$ are unknots
([neutrino](#def:neutrino-knot)) localized in the red, green,
and blue color tubes respectively.  The "up" and "down" quark
flavours correspond to the crossing orientation of each unknot
within the Borromean structure.*

**Why Borromean, not Hopf.**

The Borromean link $\mathcal{B}_3$ has the defining property
that **no two components are linked, but all three together
are inseparable**.  Removing any one component frees the other
two.  This is exactly **color confinement**: no isolated quark
(single unknot removed from $\mathcal{B}_3$) can exist, and
no two-quark bound state (diquark) is stable.  Only the
three-quark composite is confined.

The Hopf link $\mathcal{L}_H$, by contrast, links any two
components pairwise.  A Hopf chain of three unknots would
allow diquark states (remove one, the other two remain linked)
— contradicting confinement.

**Mass from linking, not from constituents.**

The three unknots individually have zero hyperbolic volume:
$\mathrm{Vol}(K_{0_1}) = 0$.  The neutrino mass is near zero.
But the Borromean link has nonzero hyperbolic volume:

$$
  \mathrm{Vol}(S^3 \setminus \mathcal{B}_3) =  7.32772\ldots
$$

By the topological mass formula
$\mathfrak{m} = \mathrm{Vol}(K) / \hbar_q^2$, the baryon mass comes
**entirely from the Borromean linking** — not from the
constituent unknots.  This matches the QCD result: approximately
$99\%$ of the proton's $938$ MeV comes from gluon binding
energy, with the quark Higgs masses contributing only
$\sim 10$ MeV.

**Up and down from crossing orientation.**

Within $\mathcal{B}_3$, the three components are related by
the cyclic symmetry of the color tubes.  The $S_3$ permutation
symmetry acts on the color assignment $(r, g, b)$.  Breaking
this symmetry into a $2 + 1$ partition gives two components
with one crossing orientation (**up quarks**) and one with the
reversed orientation (**down quark**):

- **Up quark** $u$: unknot in color tube with positive
  crossing orientation within $\mathcal{B}_3$.
  Coulomb charge contribution: $+2/3$ of the proton charge.

- **Down quark** $d$: unknot in color tube with negative
  (reversed) crossing orientation within $\mathcal{B}_3$.
  Coulomb charge contribution: $-1/3$ of the proton charge.

The proton $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p$ has the $2 + 1$
partition: two positive-orientation unknots and one negative.
The neutron $\mathfrak{n} = [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p$ has the $1 + 2$
partition.

**Crossing orientation is not writhe.**
The $\pm$ labels are the **exponent sign** of the braid generator
at each crossing of $\mathcal{B}_3$ — explicitly, $\sigma_i$ for
positive and $\sigma_i^{-1}$ for negative — while the generator
index $i \in \{0, 1\}$ identifies *which* adjacent pair of strands
crosses (independently of the sign).  These are crossings *between
distinct strands*, not self-crossings of any one strand: in the
standard braid projection each strand has **self-writhe zero**
(no self-crossings appear), and the free neutrino is the same
unknot drawn outside any Borromean context.  All three pairwise
linking numbers vanish (Brunnian property); the triple Milnor
invariant $\bar{\mu}_{123} = \pm 1$ encodes confinement.

**The exceptional divisor as quark habitat.**

The Borromean linking happens in the **exceptional divisor**
of the brane tower — the blow-up locus where the color tubes
of Bring's surface meet.  The unknots (neutrinos) are
spacetime objects; their Borromean linking is a **fiber
phenomenon** that exists only in the exceptional divisor.
A free neutrino (unknot not in a color tube) has no Borromean
partners and no mass from linking.

This explains why quarks are never observed in isolation: the
Borromean structure exists only within the exceptional divisor.
Pulling a quark out of the baryon means extracting an unknot
from $\mathcal{B}_3$ — which unlinks the remaining two,
destroying the baryon.  The energy required to separate exceeds
the threshold for creating a new quark-antiquark pair
(a new Borromean triple), so the extracted quark immediately
re-confines.

**The T(2,n) family.**

The torus knot/link family $T(2,n)$ on the Bring's surface
splits into two parallel ladders:

The torus-knot particle spectrum is tabulated in
[Table: Torus-knot particle spectrum](#tbl:borromean-quark-table-data).

**Odd $n$**: knots (1 component) = **fermions** (matter).
**Even $n$**: links (2 components) = **bosons** (force carriers).

The gluon is $T(2,2)$ = Hopf link, not $T(2,7)$.  The Hopf
link has two components that mediate the color interaction
between two of the three Borromean unknots.  There are
$\binom{3}{2} = 3$ such pairs, giving **eight gluons** from
the $\mathrm{SU}(3)$ color algebra acting on the three
Borromean components.

**Consistency with the Skein mass relation.**

The terminal resolution
([terminal resolution](#prop:terminal-resolution)) decomposes
any hadronic link into a polynomial in unknots and Hopf links:

$$
  \mathcal{M}(\mathcal{H})
  = 
  \sum_j P_j(q)\mathcal{M}(\nu)
  +  \sum_k Q_k(q)\mathcal{M}(\mathcal{L}_H)
$$

In the Borromean picture, $\mathcal{M}(\nu) \approx 0$ (unknot
mass is vacuum drag only), so the hadronic mass is dominated by
the $Q_k(q)\mathcal{M}(\mathcal{L}_H)$ terms — the Hopf
link mass contributions from the Borromean structure.  The
"vast majority of hadronic mass is generated by the Skein
polynomials multiplying the Hopf link mass" is exactly the
Borromean volume contributing through the Skein resolution.
