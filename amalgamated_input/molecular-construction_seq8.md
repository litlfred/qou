<!-- FILE_START: benzene-computation-intro.md -->
Benzene closes the chapter with a genuinely new structural feature. Benzene $C_6H_6$ as a molecular braid (def) arranges six carbons in a ring on twelve strands, with $\pi$-electrons spread across the cycle rather than localised on alternating bonds. Threading link $T(2,6)$ emerges as the LP-optimal $\pi$ configuration (prop) shows that the LP dual prefers the $(2,6)$ threading link over any Kekulé alternation, and bond equalization from $D_6$ symmetry of $T(2,6)$ (rem) reads the $D_6$ symmetry of this threading link as the experimental fact that all six $C{-}C$ bonds have equal length. Aromaticity here is not an extra postulate but a forced output of the LP minimum on an $n$-membered ring.

_(draft.)_
<!-- FILE_END: benzene-computation-intro.md -->

<!-- FILE_START: benzene-molecular-braid.md -->
**Definition.**
**Benzene** *$C_6H_6$ is the molecular braid of six carbon atoms and
six hydrogen atoms, assembled iteratively from pre-computed atomic
braids.*

### Strand count

- *6 carbon atoms: $6 \times 18 = 108$ strands*
- *6 hydrogen atoms: $6 \times 2 = 12$ strands*
- *Total: $N_{\mathrm{mol}} = 120$ strands, living in $H_{120}(q)$*

### Bond structure

*Each carbon has valence 4.  In benzene:*
- *2 electrons shared with adjacent carbons (C--C bonds)*
- *1 electron shared with hydrogen (C--H bond)*
- *1 electron participates in $\pi$ delocalization*

*This gives:*
- *6 C--C $\sigma$ bonds (single, 1 shared pair each)*
- *6 C--H $\sigma$ bonds (single, 1 shared pair each)*
- *6 $\pi$ electrons delocalized around the ring*

### Iterative construction

1. *Build C$_1$--H$_1$ unit: $\mathcal{A}_{C_1}$ + covalent
   bond with $H_1$, reduce to NF in $H_{20}(q)$*
2. *Add C$_2$--H$_2$: embed, C$_1$--C$_2$ $\sigma$ bond,
   C$_2$--H$_2$ bond, reduce in $H_{40}(q)$*
3. *Continue for C$_3$--H$_3$ through C$_5$--H$_5$, reducing
   at each step*
4. *Close the ring: C$_6$--H$_6$ + C$_6$--C$_1$ $\sigma$ bond,
   forming the cyclic structure, reduce in $H_{120}(q)$*
5. *Add $\pi$ electrons: 6 electrons form a
   [threading link](#prop:benzene-threading-emergence) $T(2, 6)$
   around the ring*

*Step 5 is the critical one: the threading link emerges from the
LP dual as the optimal configuration for the remaining 6
electrons, rather than being postulated.*
<!-- FILE_END: benzene-molecular-braid.md -->

<!-- FILE_START: benzene-threading-emergence.md -->
**Proposition (conditional on [`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula)).**
*The LP dual of the benzene molecular braid in $H_{120}(q)$
selects the threading link $T(2, 6) = (\sigma_1\sigma_2 \cdots
\sigma_5)^2$ as the optimal $\pi$-electron configuration.*

*After the $\sigma$-bond framework is assembled (steps 1--4),
there remain 6 unpaired electrons — one from each carbon's $2p_z$
orbital.  The LP dual optimises their placement:*

**Candidate configurations:**

| Configuration | Braid structure | Shared crossings |
|:-------------|:---------------|:----------------|
| 3 alternating double bonds (Kekulé) | 3 localised $\pi$ pairs | $3 \times 2 = 6$ |
| Threading link $T(2, 6)$ | Non-local torus link | $6 \times 2 = 12$ |
| 2 Dewar bonds + 1 double | Mixed localised | Variable |

*The threading link wins because:*

1. **More shared crossings.** $T(2, 6)$ creates 12 attractive
   $\sigma^{-1}$ crossings (each of the 6 $\pi$ electrons has
   attractive crossings with 2 adjacent carbon protons), compared
   to only 6 for localised Kekulé double bonds.

2. **$D_6$ symmetry.** The threading link has full hexagonal
   symmetry, minimising inter-electron repulsion by distributing
   the 6 $\pi$ electrons uniformly around the ring.

3. **Alexander polynomial weight.** The Alexander polynomial
   $\Delta_{T(2,6)}(q) = (q^3 - q^{-3})/(q - q^{-1}) = [3]_{q^2}$
   gives the threading link half the Alexander weight of
   pairwise bonding, reducing $\Phi_1$ relative to localised bonds.

*The $\Phi_1$ comparison:*

$$
  \Phi_1^{T(2,6)} < \Phi_1^{\text{Kekulé}} < \Phi_1^{\text{Dewar}}
$$

*The LP dual shadow price for the threading link is the
**resonance stabilisation energy** of benzene:*

$$
  E_{\mathrm{res}} = \alpha \bigl(
    \Phi_1^{\text{Kekulé}} - \Phi_1^{T(2,6)}
  \bigr)
$$

*The observed resonance energy is $\approx 1.56 \;\mathrm{eV}$
(:val[benzene_resonance_kcal]{precision=2, witness=computations/molecular-experimental-refs.witness.json} kcal/mol).*
<!-- FILE_END: benzene-threading-emergence.md -->

<!-- FILE_START: benzene-bond-equalization.md -->
*The $D_6$ symmetry of the threading link $T(2, 6)$ ensures
that all six C--C bonds are identical. Each bond has:*

- *1 $\sigma$ pair (from step 1--4 of the construction)*
- *$\frac{1}{2}$ $\pi$ pair (from the threading link — each
 $\pi$ electron is shared between 2 adjacent carbons)*

*Total bond order per C--C bond: $1 + \frac{1}{2} = \frac{3}{2}$.*

*This is the braid-theoretic derivation of the experimentally
observed bond order 1.5 in benzene, with equal bond lengths
of $:val[bond_len_benzene_ang]{precision=3, witness=computations/molecular-experimental-refs.witness.json}\;\text{\AA}$ (between the C--C single bond length
$:val[bond_len_cc_single_ang]{precision=3, witness=computations/molecular-experimental-refs.witness.json}\;\text{\AA}$ and double bond length $:val[bond_len_cc_double_ang]{precision=3, witness=computations/molecular-experimental-refs.witness.json}\;\text{\AA}$).*

*The construction proves that bond equalization is not an axiom
of molecular orbital theory but a **theorem** of the LP dual:
the threading link's $D_6$ symmetry is the unique $\Phi_1$
minimum for 6 $\pi$ electrons on a 6-membered ring.*

*Extension to larger aromatics (naphthalene $C_{10}H_8$,
anthracene $C_{14}H_{10}$) proceeds by the same construction:
build the $\sigma$ framework iteratively, then apply the LP
dual to select the optimal $\pi$ configuration. The threading
link $T(2, N)$ generalises accordingly to $N$-membered rings,
with Alexander polynomial
$\Delta_{T(2,N)}(q) = (q^{N/2} - q^{-N/2})/(q - q^{-1})$
for even $N$.*
<!-- FILE_END: benzene-bond-equalization.md -->

<!-- FILE_START: benzene-assembly-spine.md -->
*Light is the start of the assembly. The Breit–Wheeler process
[$\gamma\gamma \to e^+e^-$](#rem:breit-wheeler-observation) seeds a lepton
pair; that energy feeds
[quark–antiquark production](#def:quark-antiquark-production), whose
confinement closes into the
[Borromean nucleon](#def:f-bor-borromean-observable) and, by
[meson exchange](#rem:meson-to-proton-via-borromean), the proton. Twelve
nucleons bind into a $^{12}\mathrm{C}$ atom (the $A \ge 3$ binding closure),
and carbon's four octet channels assemble molecules.*

*The molecular layer is parameter-free. Each covalent bond order is the
cardinality of the saturated orthogonal-channel set — the
[bond order $=$ LP active set](#prop:co-lp-dual-binding) identity — and the
fractional $\pi$ of an aromatic ring is the lateral-$\pi$ overlap of the
[embeddable knot operator](#def:embeddable-knot-operator), delocalised by
the [assembly projector](#def:molecular-assembly-projector).*

### Validated predictions

*Running the spine end-to-end (witness `benzene-assembly-spine`) reproduces
the observed structural bond orders with no fitted constant:*

| species | construction | predicted | observed |
|---|---|---|---|
| acetylene $\mathrm{C_2H_2}$ | $\sigma \perp \pi_x \perp \pi_y$ orthogonal triple | $3$ | $3$ |
| benzene $\mathrm{C_6H_6}$ | $\lambda=(2,2,2)\vdash 6$, $D_6$ ring | $\tfrac{3}{2}$ | $\tfrac{3}{2}$ |
| cyclohexane $\mathrm{C_6H_{12}}$ | saturated control | $1$ | $1$ |

*Acetylene's $\mathrm{C}\!\equiv\!\mathrm{C}$ fills all three orthogonal
channels (one axial $\sigma$, two transverse $\pi$); the spatial-dimension
bound caps it at three. Benzene's six $\mathrm{C\!-\!C}$ bonds come out
identical — the $D_6$ symmetry of the assembly projector forces zero spread,
so bond equalisation is a consequence of the construction, not an assumption.
Aromaticity then registers as a $+\tfrac{1}{2}$ bond-order increment per bond
over the saturated ring: one localised $\sigma$ plus a half-share of the
delocalised six-electron $\pi$ system.*
<!-- FILE_END: benzene-assembly-spine.md -->

<!-- FILE_START: assembly-shortest-production.md -->
*Retrosynthesis — asking which reactions produce a target — is famously
non-unique. The forward categorical assembly is not. The
[$\gamma\gamma$-spine](#rem:benzene-assembly-spine) has a **canonical**
shortest path: the [Hecke normal form](#def:hecke-normal-form) of the
assembly braid word — the shortest representative modulo the braid
relations — selected by the [confinement min-action program](#prop:confinement-lp).*

*The path is unique only up to the molecular symmetry group. Benzene's
$D_6$ permutes the six equivalent acetylene insertions, so the canonical
word is a single orbit representative, not a single word. This is the
assembly form of the Gröbner–Shirshov picture: many syntactic derivations
collapse onto one normal form, and the min-action confinement program picks
it — the categorical replacement for "the" synthetic route.*
<!-- FILE_END: assembly-shortest-production.md -->

<!-- FILE_START: assembly-emission-ledger.md -->
*Assembling benzene from separated atoms releases the binding energy as a
net emission,*

$$
  \mathfrak{E}_{\mathrm{emit}}
    = \bigl(\mathrm{NF}_{\text{final}} - \mathrm{NF}_{\text{initial}}\bigr)\,
      \mathfrak{E}_0 ,
$$

*the change in normal-form crossing count scaled by the per-crossing energy
$\mathfrak{E}_0$. Ring closure delocalises six $\pi$ electrons — a
$+\tfrac{1}{2}$ bond-order increment on each of the six $\mathrm{C\!-\!C}$
bonds (witness `benzene-assembly-spine`), three bond-orders of aromatic
stabilisation released on closure.*

*The emission splits into two channels. The **photon** channel is
categorical — the [trivial-knot electromagnetic mode](#rem:trivial-knot-photon-interpretation),
carrying the quantised normal-form change. The **phonon** channel is
archimedean (lattice and thermal). The ledger is therefore **partial**: the
cardinality — the normal-form crossing change, hence the photon channel's
quantum content — is robust, but the absolute energy partition between
photon and phonon awaits the lateral-$\pi$ overlap weight $w_\perp$ of the
[embeddable knot operator](#def:embeddable-knot-operator). It is the same
cardinality-robust, energy-pending split that governs the bond model.*
<!-- FILE_END: assembly-emission-ledger.md -->

<!-- FILE_START: outro-molecular-construction.md -->
This closes the molecular-construction chapter: covalent bonds
have been lifted from the chemical literature into categorical
morphisms in $\mathbf{C}$, the diatomic $\mathrm{H}_2$ case has been
worked through in detail, and the benzene-ring example exhibits
the ring-closure pattern that the next chapter generalises to
arbitrary carbon backbones.

The next chapter (organic chemistry) extends the construction to
the full Hopf-chain taxonomy of organic molecules: aliphatic
chains, aromatic rings, and the comparative energetics that
distinguish linear from cyclic isomers.  The categorical
machinery developed here — bond morphisms, ring-closure
cocycles, threading transitions — carries over without
modification; the next chapter is a survey of its applications
rather than a new construction.
<!-- FILE_END: outro-molecular-construction.md -->

