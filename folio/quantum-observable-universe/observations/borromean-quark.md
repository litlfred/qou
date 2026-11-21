Quarks are not fundamental knots. A quark is a neutrino (an unknot) trapped in a color tube of Bring's surface. It links Borromean-style with two other unknots in the exceptional divisor.

**Conjecture.**
*The baryon is the Borromean link $\mathcal{B}_3$ of three unknots threaded through the color tubes $(r, g, b)$ of the Bring's surface ([color tube coordinates](#def:color-tube-coordinates)), bound by the Hopf link $\mathcal{L}_H$:*

$$
  \mathfrak{p}
  = 
  \mathcal{B}_3(\nu_r, \nu_g, \nu_b)
   \oplus  \mathcal{L}_H,
$$

*where the unknots $\nu_r$, $\nu_g$, $\nu_b$ ([neutrino](#def:neutrino-knot)) localize in the red, green, and blue color tubes, respectively. The "up" and "down" quark flavours correspond to the crossing orientation of each unknot within the Borromean structure.*

**Borromean rather than Hopf.**

The Borromean link $\mathcal{B}_3$ requires that no two components link, yet all three together remain inseparable. Removing any one component frees the other two. This enforces color confinement. No isolated quark (a single unknot removed from $\mathcal{B}_3$) can exist. No two-quark bound state (a diquark) is stable. Only the three-quark composite remains confined. 

The Hopf link $\mathcal{L}_H$, by contrast, links any two components pairwise. A Hopf chain of three unknots permits diquark states (remove one, and the other two remain linked), contradicting confinement. The two cases are told apart by link-homotopy invariants: three-component links in $S^3$ are classified up to link homotopy by their pairwise linking numbers and Milnor's triple linking number, and the Borromean rings have all pairwise numbers zero and triple number $\pm 1$ \cite{dgkmsv2013}.

**Mass from linking, not from constituents.**

The three individual unknots possess zero hyperbolic volume: $\mathrm{Vol}(K_{0_1}) = 0$. The neutrino mass is near zero. However, the Borromean link possesses a nonzero hyperbolic volume:

$$
  \mathrm{Vol}(S^3 \setminus \mathcal{B}_3) =  7.32772\ldots
$$

By the topological mass formula $\mathfrak{m} = \mathrm{Vol}(K) / \hbar_q^2$, the baryon mass derives entirely from the Borromean linking, not from the constituent unknots. This matches the standard QCD result: roughly $99\%$ of the proton's $938$ MeV derives from gluon binding energy, while quark Higgs masses contribute only roughly $10$ MeV.

**Up and down from crossing orientation.**

Within $\mathcal{B}_3$, the cyclic symmetry of the color tubes relates the three components. The $S_3$ permutation symmetry acts on the color assignment $(r, g, b)$. Breaking this symmetry into a $2 + 1$ partition yields two components with one crossing orientation (up quarks) and one with the reversed orientation (down quark):

- **Up quark** ($u$): Unknot in a color tube with positive crossing orientation within $\mathcal{B}_3$. It contributes $+2/3$ to the proton charge.
- **Down quark** ($d$): Unknot in a color tube with negative (reversed) crossing orientation within $\mathcal{B}_3$. It contributes $-1/3$ to the proton charge.

The proton $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p$ exhibits the $2 + 1$ partition: two positive-orientation unknots and one negative. The neutron $\mathfrak{n} = [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p$ exhibits the $1 + 2$ partition.

**Crossing orientation is not writhe.**
The $\pm$ labels denote the exponent sign of the braid generator at each crossing of $\mathcal{B}_3$ (explicitly, $\sigma_i$ for positive and $\sigma_i^{-1}$ for negative). The generator index $i \in \{0, 1\}$ identifies which adjacent pair of strands crosses, independently of the sign. These crossings occur between distinct strands, not as self-crossings of any single strand. In the standard braid projection, each strand maintains zero self-writhe. The free neutrino remains the same unknot drawn outside any Borromean context. All three pairwise linking numbers vanish (the Brunnian property), while the triple Milnor invariant $\bar{\mu}_{123} = \pm 1$ encodes confinement.

**The exceptional divisor as quark habitat.**

Borromean linking occurs in the exceptional divisor of the brane tower, the blow-up locus where the color tubes of Bring's surface meet. The unknots (neutrinos) are spacetime objects. Their Borromean linking is a fiber phenomenon existing exclusively in the exceptional divisor. A free neutrino (an unknot outside a color tube) lacks Borromean partners and acquires no mass from linking.

This framework explains why quarks never appear in isolation. The Borromean structure requires the exceptional divisor. Pulling a quark out of the baryon means extracting an unknot from $\mathcal{B}_3$. This action unlinks the remaining two components and destroys the baryon. The energy required for this separation exceeds the threshold to create a new quark-antiquark pair (a new Borromean triple). Consequently, the extracted quark immediately re-confines.

**The T(2,n) family.**

The torus knot/link family $T(2,n)$ on the Bring's surface splits into two parallel ladders. The torus-knot particle spectrum is tabulated in [Table: Torus-knot particle spectrum](#tbl:borromean-quark-table-data).

- **Odd $n$:** Knots (1 component) yield fermions (matter).
- **Even $n$:** Links (2 components) yield bosons (force carriers).

The gluon is $T(2,2)$, the Hopf link, not $T(2,7)$. The Hopf link has two components that mediate the color interaction between two of the three Borromean unknots. There are $\binom{3}{2} = 3$ such pairs, yielding eight gluons from the $\mathrm{SU}(3)$ color algebra acting on the three Borromean components.

**Consistency with the Skein mass relation.**

The terminal resolution ([terminal resolution](#prop:terminal-resolution)) decomposes any hadronic link into a polynomial in unknots and Hopf links:

$$
  \mathfrak{m}(\mathcal{H})
  = 
  \sum_j P_j(q)\mathfrak{m}(\nu)
  +  \sum_k Q_k(q)\mathfrak{m}(\mathcal{L}_H).
$$

In the Borromean picture, $\mathfrak{m}(\nu) \approx 0$ since unknot mass is vacuum drag only. Thus, the $Q_k(q)\mathfrak{m}(\mathcal{L}_H)$ terms dominate the hadronic mass. These represent the Hopf link mass contributions from the Borromean structure. This is consistent with the Borromean volume entering the hadronic mass through the Skein resolution.
