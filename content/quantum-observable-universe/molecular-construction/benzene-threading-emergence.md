**Proposition (conditional on [`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula)).**
*The LP dual of the benzene molecular braid in $H_{120}(q)$ selects the threading link $T(2, 6) = (\sigma_1\sigma_2 \cdots \sigma_5)^2$ as the optimal $\pi$-electron configuration.*

*After assembling the $\sigma$-bond framework (steps 1–4), six unpaired electrons remain, one from each carbon's $2p_z$ orbital. The LP dual optimises their placement among the following candidates:*

| Configuration | Braid structure | Shared crossings |
|:-------------|:---------------|:----------------|
| 3 alternating double bonds (Kekulé) | 3 localised $\pi$ pairs | $3 \times 2 = 6$ |
| Threading link $T(2, 6)$ | Non-local torus link | $6 \times 2 = 12$ |
| 2 Dewar bonds + 1 double | Mixed localised | Variable |

*The threading link succeeds because:*

1. **More shared crossings.** $T(2, 6)$ creates 12 attractive $\sigma^{-1}$ crossings. Each of the six $\pi$ electrons has attractive crossings with two adjacent carbon protons. Localised Kekulé double bonds yield only six crossings.
2. **$D_{6h}$ symmetry.** The threading link possesses full hexagonal symmetry. It minimises inter-electron repulsion by uniformly distributing the six $\pi$ electrons around the ring.
3. **Alexander polynomial weight.** The Alexander polynomial $\Delta_{T(2,6)}(q) = (q^3 - q^{-3})/(q - q^{-1}) = [3]_{q^2}$ assigns the threading link half the Alexander weight of pairwise bonding. This reduces $\Phi_1$ relative to localised bonds.

*The $\Phi_1$ comparison yields:*

$$
  \Phi_1^{T(2,6)} < \Phi_1^{\text{Kekulé}} < \Phi_1^{\text{Dewar}}
$$

*The LP dual shadow price for the threading link corresponds to the **resonance stabilisation energy** of benzene:*

$$
  E_{\mathrm{res}} = \alpha \bigl(
    \Phi_1^{\text{Kekulé}} - \Phi_1^{T(2,6)}
  \bigr)
$$

*The observed resonance energy is $\approx 1.56 \;\mathrm{eV}$ (:val[benzene_resonance_kcal]{precision=2, witness=computations/molecular-experimental-refs.witness.json} kcal/mol).*
