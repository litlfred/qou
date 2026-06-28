## Proof

The chain has three steps:

**Step 1 (Categorical trace $\to$ Frobenius integral).**
The categorical trace
$\mathrm{tr}(f) = \mathrm{ev}_A \circ (f \otimes \mathrm{id}_{A^\vee}) \circ \mathrm{coev}_A$
descends under the fibre functor $\tau$ to the Frobenius integral
$\int_A : A \to R$ — the Jones--Markov trace on $H_n(R, q)$
([RJ interpretation](#rem:rj-inner-product-interpretation)),
satisfying Markov properties I and II
([vertex algebra relations](#prop:vertex-algebra-relations), QU-3).

**Step 2 (Nakayama automorphism = identity).**
The mass involves $\Psi = (\int_A \otimes \mathrm{id}) \circ \Delta$,
the **Nakayama automorphism** of the Frobenius algebra $A$.  For
Frobenius--Hopf algebras, $\Psi = S^2$.  In $H_n(R, q)$ the antipode
$S(\sigma_i) = \sigma_i^{-1}$ gives $S^2(\sigma_i) = \sigma_i$, so $\Psi = \mathrm{id}_A$.

**Step 3 (Mass = trace of cycle).**
Substituting $\Psi = \mathrm{id}$:

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \bigl\lVert \mathrm{tr}\bigl(
    \underbrace{(\textstyle\int_A \otimes \mathrm{id}) \circ \Delta}_{= \,\mathrm{id}_A}
    \circ\, \varrho \bigr) \bigr\rVert
  \;=\; \Bigl|\!\int_A\! \rho(\beta_\mathcal{K})\Bigr|.
$$

## Explicit values

Evaluating at $q_0 \approx 1.110$ with Markov parameter
$z = 1/(q^{1/2} + q^{-1/2}) \approx 0.499$ and
$h = q - q^{-1} \approx 0.209$:

| Particle | Braid $\beta_\mathcal{K}$ | $\int_A \rho(\beta_\mathcal{K})$ | Symbolic |
|:---:|:---:|:---:|:---:|
| $\gamma$ (photon) | $\mathbf{1}$ | $1$ | $1$ |
| $\sigma_0$ (pol.) | $\sigma_0$ | $z \approx 0.499$ | $z$ |
| $L_+$ (gluon) | $\sigma_0\sigma_1$ | $z^2 \approx 0.249$ | $z^2$ |
| $e^-$ (electron) | $\sigma_0\sigma_1\sigma_0$ | $\approx 0.551$ | $hz^2 + z$ |
| $4_1$ (figure-eight) | $(\sigma_0\sigma_1^{-1})^2$ | $\approx 0.182$ | (see witness) |

These are **dimensionless ratios** relative to the photon
($\mathfrak{m}_{q,\gamma} = 1$).  To obtain physical masses in MeV,
multiply by a calibration constant $E_0$, determined by matching one
experimental value (e.g. the free neutron beta-decay Q-value).

## Role in the unified mass formula

This proposition supplies the $k = 0$ stratum of the curvature-rank
decomposition
([unified mass formula](#prop:unified-curvature-rank-mass-formula)):
$\mathfrak{m}^{(0)}_{q,\mathcal{K}}(1) = |\!\int_A\! \rho(\beta_\mathcal{K})|$
is the descended Frobenius integral, equal to $E_\infty^{0,*}$ of the GB
spectral sequence.

The integral $\int_A \rho(\beta_\mathcal{K})$ is **vortex-specific**:
it differs for $\varrho_{\mathfrak{p}}$ vs $\varrho_{\mathfrak{n}}$ and
is the source of fine isotope distinctions.  The vortex-independent
constant offset is the Frobenius co-Casimir
$m_e \cdot \tau(C_{\dim_q})$
([Frobenius universal](#thm:frobenius-codim-universal)).  The full
mass is

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \sum_{k \geq 0} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(1)
       \;+\; m_e \cdot \tau(C_{\dim_q}),
$$

with this proposition supplying the $k = 0$ piece.
