The Skein binding Lagrangian
([Skein binding Lagrangian](#def:skein-binding-lagrangian)) is not a new
Lagrangian: it is the categorical action
$\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$
([canonical action](#prop:qou-canonical-action)) evaluated on the
field configuration $\psi = Z\mathfrak{p} \oplus N\mathfrak{n}$.

The categorical Lagrangian
([categorical Lagrangian](#def:categorical-lagrangian))
$\mathcal{L}_q = \mathcal{D}_\nabla^2 + \psi^* \otimes \mathcal{D}_\nabla\psi$ decomposes via the Frobenius--Hopf structure
into gravity + gauge + matter sectors.  When the state $\psi$ is a
multi-nucleon Hopf link, the Skein crossing asymmetry
([crossing asymmetry](#rem:skein-crossing-asymmetry)) further
splits the gauge sector by crossing chirality, producing the
familiar nuclear binding terms.

**Notation.** The conventional Bethe--Weizsäcker coefficients are
related to the Skein scales by:

$$
  a_V = \tfrac{1}{2}(q + q^{-1}) \cdot \lambda_V,
  \qquad
  a_C = (q - q^{-1}) \cdot \lambda_C,
  \qquad
  a_S = \tfrac{1}{2}(q + q^{-1}) \cdot \lambda_S.
$$

At $q = q_0$: $a_V \approx 15.56$ MeV,
$a_C = (q - q^{-1}) \times 3.334 \approx 0.697$ MeV,
$a_S \approx 17.23$ MeV, $a_A \approx 23.29$ MeV.

**$q$-dependence.**  The Coulomb coefficient $a_C$ vanishes at
$q = 1$ (classical limit: no crossing asymmetry, no electromagnetic
repulsion) and grows with $q$.  The strong binding $a_V$ is nearly
$q$-independent ($(q + q^{-1})/2 \approx 1$ for $q$ near $1$).
The ratio

$$
  \frac{a_C}{a_V}
  =  \frac{q - q^{-1}}{q + q^{-1}}
  \cdot \frac{\lambda_C}{\lambda_V}
  =  \tanh(\ln q) \cdot \frac{\lambda_C}{\lambda_V}
$$

controls the balance between the strong and electromagnetic
interactions.

**Derivation from the canonical action.**
The five terms arise from the three sectors of $\mathfrak{S}_q$
([canonical action](#prop:qou-canonical-action)) as follows:

| Canonical sector | Evaluation on $L$ | Nuclear term |
|-----------------|-------------------|--------------|
| Gauge: $\int_A \mathrm{tr}_A(F_\nabla \wedge_q \star_q F_\nabla)$ | Hopf junction curvature, bulk | $\mathcal{L}_{\mathrm{vol}}$ |
| Gauge: same, boundary | Surface deficit in linking number | $\mathcal{L}_{\mathrm{surf}}$ |
| Gauge: $q$-weighting of $\wedge_q$ on $\mathfrak{p}$--$\mathfrak{p}$ crossings | Crossing asymmetry $q$ vs $q^{-1}$ | $\mathcal{L}_{\mathrm{Coul}}$ |
| Matter: $\int_A(\psi^* \cdot \mathcal{D}_\nabla\psi)$ | Fermionic exclusion cost | $\mathcal{L}_{\mathrm{Pauli}}$ |
| Matter: same, even--even pairing | Closed Hopf loops | $\mathcal{L}_{\mathrm{pair}}$ |

The gravity sector $\mathrm{tr}(q \cdot R_{\int})$ contributes a
constant background that does not depend on $(p, n)$ and hence
drops out of the beta-stability variation.  The key insight is
that the $q$-deformed wedge product $\wedge_q$ in the gauge
sector automatically distinguishes same-chirality crossings
(proton--proton, coefficient $q$) from mixed crossings
(coefficient $(q + q^{-1})/2$), producing the Coulomb repulsion
without any additional structure.  The mass identity
([mass identity](#def:mass-identity)) then evaluates
$\|\mathrm{tr}(\cdots)\|$ to give the nuclear mass.
