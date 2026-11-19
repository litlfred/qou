The **Breit-Wheeler process** ($\gamma\gamma \to e^-e^+$) creates an electron-positron pair from two real photons. The QOU encodes this vertex entirely within the Iwahori-Hecke algebra $H_n(R, q)$ acting on the exceptional divisor $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$.

## Polarisation states as Hecke generators

The homogeneous coordinates $[v_1 : v_2]$ of $\mathcal{S}_p$ parametrise the two independent polarisation directions of a spin-1 field at $p$. The Reeb bundle holonomy $e^{2\pi i/[2]_q}$ provides the phase acquired by a photon completing one full rotation in the polarisation sphere.

The two Hecke generators act on $\mathcal{S}_p$:

| Generator | Coordinate patch | Polarisation mode | Eigenvalues |
|-----------|-----------------|-------------------|----------------------|
| $\sigma_0$ | $v_2 \neq 0$ ($z = v_1/v_2$) | horizontal ($\leftrightarrow$) | $+q$ (left), $-q^{-1}$ (right) |
| $\sigma_1$ | $v_1 \neq 0$ ($w = v_2/v_1$) | vertical ($\updownarrow$) | $+q$ (left), $-q^{-1}$ (right) |

The labels *horizontal* and *vertical* are model names for the two generators. They are not an orthogonal pair of polarisation states. In the two-dimensional block of $H_3(q)$ the $q$-eigenlines of $\sigma_0$ and $\sigma_1$ sit at Bloch angle $\cos\theta = -(q^4+1)/(q^2+1)^2$ ($120^\circ$ at $q = 1$) rather than at antipodes. No algebra automorphism of $H_3(q)$ carries $(\sigma_0, \sigma_1)$ to the generators of an orthogonal pair of polarisation lines, because generators attached to such a pair commute and $\sigma_0\sigma_1 \neq \sigma_1\sigma_0$.

The Hecke relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ constitutes the photon helicity equation. Its roots $+q$ and $-q^{-1}$ are the left and right circular polarisation eigenvalues. A linearly polarised photon is a superposition of these eigenstates.

## The pair-creation vertex

The two-photon state $\gamma_1 \otimes \gamma_2$ is a word in $H_n(R, q)$. Two primary polarisation cases arise:

**Parallel polarisation.**
$$
  \sigma_i \cdot \sigma_i = (q - q^{-1})\sigma_i + \mathbf{1}.
$$
In the model, the Hecke relation reduces the word to a dressed photon plus the vacuum, so the word contains no pair-creation channel.

**Perpendicular polarisation.**
$$
  \sigma_0 \cdot \sigma_1 = L_+ \quad (\text{Hopf link intermediate}).
$$
The product is the normal-form basis element $L_+$, a two-strand entangled state. Applying an aether Reeb insertion completes the trefoil:
$$
  L_+ \cdot \sigma_0 = \sigma_0\sigma_1\sigma_0 = e^-.
$$
The positron $e^+$ is supplied by the mirror process $\sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$. The complete vertex pairs orthogonal photons to produce the chiral trefoil channels.

## Polarisation selection rule (model statement)

In the model, the vertex vanishes unless the photons occupy distinct polarisation patches of $\mathbb{P}^1(\mathbb{C})$. Evaluating the Frobenius pairing $\langle \cdot, \cdot \rangle_F$:

$$
  \langle v_{e^-e^+}, \sigma_i\sigma_i \rangle_F = 0, \qquad \langle v_{e^-e^+}, \sigma_0\sigma_1 \rangle_F \neq 0.
$$

Within the model, a repeated generator applies the Hecke relation and returns lower-energy states, and only the product of the two distinct generators produces the Hopf-link intermediate that the aether completes into the $e^-e^+$ trefoil pair.

**Comparison with QED.** This rule is a statement about Hecke words. It does not hold for physical photons read as linear polarisations. Tree-level QED gives nonzero $\gamma\gamma \to e^-e^+$ for parallel linear polarisations. For example, with $e = m_e = 1$, photon energy $5/4$ in the centre-of-mass frame and the electron along the beam axis, the exact spin-summed squared amplitude is $9/2$ for parallel and $25/2$ for perpendicular polarisations. The ratio $9/25$ equals $\beta^2$ at that point. The perpendicular channel dominates near threshold, where the pair forms in the pseudoscalar ${}^1S_0$ state, and that dominance is the only part of the rule that agrees with QED.
