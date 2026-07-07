<!-- FILE_START: particle-conjectures-intro.md -->
We establish the dictionary between knots and particles using the substrate consistency window. The following four blocks constrain the assignments:
- The quark identification models quarks as Borromean-linked unknots in the exceptional divisor.
- The Higgs boson emerges as the torus link $T(2,8)$, spanning three exceptional divisors.
- The symmetry of Bring's surface restricts $S_5$-equivariant torus-knot embeddings to $T_{2,3}$ and $T_{2,5}$.
- The lepton sector sorts into symmetry-preserving versus symmetry-broken generators depending on whether they commute with the residual symmetry.

These topological assignments provide the necessary input for distinguishing photon propagation from massive-particle propagation in the subsequent double-slit analysis.
<!-- FILE_END: particle-conjectures-intro.md -->

<!-- FILE_START: borromean-quark.md -->
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

The Hopf link $\mathcal{L}_H$, by contrast, links any two components pairwise. A Hopf chain of three unknots permits diquark states (remove one, and the other two remain linked), contradicting confinement.

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
  \mathcal{M}(\mathcal{H})
  = 
  \sum_j P_j(q)\mathcal{M}(\nu)
  +  \sum_k Q_k(q)\mathcal{M}(\mathcal{L}_H).
$$

In the Borromean picture, $\mathcal{M}(\nu) \approx 0$ since unknot mass is vacuum drag only. Thus, the $Q_k(q)\mathcal{M}(\mathcal{L}_H)$ terms dominate the hadronic mass. These represent the Hopf link mass contributions from the Borromean structure. The assertion that the vast majority of hadronic mass derives from Skein polynomials multiplying the Hopf link mass perfectly aligns with the Borromean volume contributing through the Skein resolution.
<!-- FILE_END: borromean-quark.md -->

<!-- FILE_START: higgs-t28.md -->
**Conjecture.**
*The Higgs boson is the torus link $T(2,8)$ — the unique genus-$3$ link on the Bring's surface whose Seifert surface spans all three exceptional divisors simultaneously.*

**The three exceptional divisors.**

The Bring's surface ($\chi = -6$, genus $4$) has three color tubes $(r, g, b)$ ([color tube coordinates](#def:color-tube-coordinates)). The brane tower blow-up produces three exceptional divisors $D_r, D_g, D_b$, one for each color fiber. The Borromean link $\mathcal{B}_3$ ([Borromean quark](#conj:borromean-quark)) lies at the intersection of these three divisors.

The torus links $T(2, 2k)$ on the Bring's surface have genus $k - 1$ and interact with the exceptional divisors by genus:

| Link | Genus | Divisors spanned | Role |
|------|------:|:----------------:|------|
| $T(2,2)$ | 0 | 0 (trivial Seifert) | Gluon |
| $T(2,4)$ | 1 | 1 ($D_r$ or $D_g$ or $D_b$) | $W$ boson |
| $T(2,6)$ | 2 | 2 ($D_r \cup D_g$ etc.) | $Z$ boson |
| $T(2,8)$ | 3 | **all 3** ($D_r \cup D_g \cup D_b$) | **Higgs** |

The torus link $T(2,8)$ is the first and only link with a Seifert surface genus large enough to span all three exceptional divisors. Its genus ($3$) exactly matches the number of color tubes.

**Scalar (spin $0$) character of $T(2,8)$.**

The two components of $T(2,8)$ each wind $4$ times around the torus longitude and $1$ time around the meridian. The fermion--boson correspondence ([fermion--boson knot--link](#prop:fermion-boson-knot-link)) identifies even-$n$ links as bosons, with components related by the fiber adjoint involution.

For $T(2,8)$, the linking number is $4$. The two components cross each other $8$ times, contributing $4$ crossings each. The Reeb winding of the two components cancels exactly: one winds $+4$ and the other $-4$ around the Reeb direction. The total angular momentum vanishes:

$$
  J =  J_1 + J_2 =  +4 + (-4) =  0.
$$

The torus link $T(2,8)$ is therefore a scalar (spin-$0$) boson. It is the only member of the $T(2,n)$ family where Reeb windings cancel exactly due to genus-$3$ symmetry.

**The Higgs mechanism as linking with $T(2,8)$.**

A particle (knot or link) acquires mass by crossing with $T(2,8)$. The crossing energy ([crossing energy](#def:crossing-energy)) of the interaction is proportional to the number of crossings between the particle and the Higgs link:

$$
  m_{\mathrm{Higgs}}  \propto 
  N_{\mathrm{cross}}(T(2,8))
   \times  \frac{q - q^{-1}}{q + q^{-1}}
$$

where $N_{\mathrm{cross}}(L)$ counts crossings between the particle braid and the link $L$.

Particles that cross all three exceptional divisors (heavy quarks, $W$, $Z$) interact strongly with $T(2,8)$ and acquire large masses. Particles confined to fewer divisors interact less. The photon ($\mathbf{1}_{B_4}$, the 4-strand identity, knot-trivial under Markov closure; see [confined-particle](#def:confined-particle)) has zero crossings with $T(2, 8)$ and remains massless.

**Mass of the Higgs.**

The torus link $T(2,8)$ has genus $3$. Its Seifert surface area is proportional to the product of the three exceptional divisor volumes. The self-crossing energy of $T(2,8)$ determines its mass ($\sim 125$ GeV) via the Skein polynomial evaluated at $q = q_0$:

$$
  m_H =  \frac{\mathrm{Vol}(\text{Seifert}(T(2,8)))}{\hbar_q^2}
  \cdot \lambda_{\mathrm{scale}}
$$

Here $\lambda_{\mathrm{scale}}$ is the conjectural Borromean scale of [`conj:borromean-baryon-mass-formula`](#conj:borromean-baryon-mass-formula), recorded as an acknowledged-CAL-4 near-form. The canonical production mass shape absorbs it into the per-block density, $m = m_e\,\mathrm{Vol}(K)\,\varrho(K)/\hbar_q^2$ (no standalone $\lambda_{\mathrm{scale}}$ factor). This $\sim 125$ GeV heuristic estimate remains exploratory, conditional on that open closure.

The Higgs mass stems from the genus-$3$ Seifert surface volume, determined by the three color tube volumes of the Bring's surface.

**Uniqueness of the Higgs.**

On the genus-$4$ Bring's surface, the Seifert surface of $T(2,8)$ has genus $3$, filling $3$ of the $4$ available handles. Up to isotopy, there is exactly one way to embed a genus-$3$ surface into a genus-$4$ surface leaving one handle free. The next link $T(2,10)$ would require genus $4$ (all handles), saturating the surface and precluding the coexistence of Borromean and knot structures. Therefore, $T(2,8)$ is the unique Higgs candidate.
<!-- FILE_END: higgs-t28.md -->

<!-- FILE_START: s5-equivariant-torus-knots.md -->
**Proposition.**
*Let $\Sigma$ be a Riemann surface with automorphism group $\mathrm{Aut}(\Sigma) = S_5$ ([Bring's surface](#def:brings-surface)). A torus knot $T_{2, s}$ with $s \geq 3$ coprime to $2$ admits an equivariant embedding into $\Sigma$ if and only if*

$$
  s  \in  \{3,\, 5\}.
$$

*An equivariant embedding preserves the intrinsic cyclic symmetry $\mathbb{Z}_s$ of the knot.*
<!-- FILE_END: s5-equivariant-torus-knots.md -->

<!-- FILE_START: symmetry-preserving-leptons.md -->
**Remark.**
The classification of [prop:s5-equivariant-torus-knots](#prop:s5-equivariant-torus-knots) admits a sharp physical reading. The three charged lepton generations map to torus knots:

$$
  \text{electron} \;=\; T_{2,3},
  \qquad
  \text{muon} \;=\; T_{2,5},
  \qquad
  \text{tau} \;=\; T_{2,7}.
$$

Under pure topological embedding (Seifert genus $\leq 4$), all three fit on Bring's surface. Under the stronger equivariant criterion—preserving the knot's intrinsic cyclic symmetry along the embedding—the proposition cuts the list to two:

| Particle | Knot | Cyclic symmetry | $\mathbb{Z}_s \hookrightarrow S_5$? | Embedding |
|----------|------|:---------------:|:-----------------------------------:|-----------|
| electron | $T_{2,3}$ | $\mathbb{Z}_3$ | yes (3-cycle) | **symmetry-preserving** |
| muon | $T_{2,5}$ | $\mathbb{Z}_5$ | yes (5-cycle) | **symmetry-preserving** |
| tau | $T_{2,7}$ | $\mathbb{Z}_7$ | **no** (no order-7 element in $S_5$) | symmetry-broken |
| (ghost) | $T_{2,9}$ | $\mathbb{Z}_9$ | **no** (no order-9 element) | symmetry-broken, saturates $g=4$ |
| (ghost) | $T_{2,11}$ | $\mathbb{Z}_{11}$ | **no** | doubly excluded ($g = 5 > 4$) |

**Reading.**
The electron and muon are the only leptons whose cyclic rotational symmetry is realized by a genuine element of $\mathrm{Aut}(\Sigma_4) = S_5$. The tau embeds topologically by virtue of its genus ($g(T_{2,7}) = 3 \leq 4$) but fails equivariance: its $\mathbb{Z}_7$ symmetry is not a subgroup of $S_5$. The tau is a lepton in the topological spectrum, but not in the symmetry spectrum.

**Physical consequence.**
If lepton-generation structure derives from the cyclic symmetry of a $\Sigma_4$-embedded torus knot, the equivariant criterion predicts exactly two generations of charged leptons. Three generations are observed, matching the topological-embedding criterion. The equivariant proposition sharpens this: tau carries its mass because the symmetry-broken embedding still admits a Seifert surface, not because an $S_5$-compatible cyclic structure exists. This aligns with the weight-identification picture ([rem:weight-identification-consequences](#rem:weight-identification-consequences)), where the electron and muon representations fit into the $\mathbb{Z}_5$-graded structure of the $\mathcal{X}_5$ substrate.

**Scope.**
The proposition does not prohibit the tau. It dictates that the tau requires a different mechanism (symmetry-broken embedding) than the electron and muon (symmetry-preserving embedding). The genus saturation at $T_{2,9}$ excludes fourth and higher generations. The three-generation structure is $2 + 1$, not $3 + 0$.
<!-- FILE_END: symmetry-preserving-leptons.md -->
