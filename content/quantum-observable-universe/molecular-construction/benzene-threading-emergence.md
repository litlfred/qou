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
