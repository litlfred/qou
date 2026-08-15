## Proof

The chain has three steps:

**Step 1 (Categorical trace $\to$ Frobenius integral).**
The categorical trace $\mathrm{tr}(f) = \mathrm{ev}_A \circ (f \otimes \mathrm{id}_{A^\vee}) \circ \mathrm{coev}_A$ descends under the fibre functor $\tau$ to the Frobenius integral $\int_A : A \to R$—the Jones–Markov trace on $H_n(R, q)$ ([RJ interpretation](#rem:rj-inner-product-interpretation)), satisfying Markov properties I and II ([vertex algebra relations](#prop:vertex-algebra-relations), QU-3).

**Step 2 (Nakayama automorphism = identity).**
The mass involves $\Psi = (\int_A \otimes \mathrm{id}) \circ \Delta$, the **Nakayama automorphism** of the Frobenius algebra $A$. For Frobenius–Hopf algebras, $\Psi = S^2$. In $H_n(R, q)$ the antipode $S(\sigma_i) = \sigma_i^{-1}$ yields $S^2(\sigma_i) = \sigma_i$, hence $\Psi = \mathrm{id}_A$.

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

Evaluating at $q_0 \approx 1.110$ with Markov parameter $z = q^3/(q^2+1) \approx 0.613$ (**convention D**, SU(2)/Temperley–Lieb — see the [trace-convention registry](../../../docs/coordination/trace-convention-registry.md)) and $h = q - q^{-1} \approx 0.209$:

| Particle | Braid $\beta_\mathcal{K}$ | $\int_A \rho(\beta_\mathcal{K})$ | Symbolic |
|:---:|:---:|:---:|:---:|
| $\gamma$ (photon) | $\mathbf{1}$ | $1$ | $1$ |
| $\sigma_0$ (pol.) | $\sigma_0$ | $z \approx 0.613$ | $z$ |
| $L_+$ (gluon) | $\sigma_0\sigma_1$ | $z^2 \approx 0.375$ | $z^2$ |
| $e^-$ (electron) | $\sigma_0\sigma_1\sigma_0$ | $\approx 0.691$ | $hz^2 + z$ |
| $4_1$ (figure-eight) | $(\sigma_0\sigma_1^{-1})^2$ | $\approx 0.280$ | $\dfrac{q^8-q^6+q^4-q^2+1}{q^6+2q^4+q^2}$ |

> **Convention change, 2026-08-09 (owner ruling; bean `qou-wgta` item 19).**
> This table published **convention C** ($z = 1/(q^{1/2}+q^{-1/2}) \approx 0.499$),
> which has been excised. Measured at the proton pin $q_0 =
> 1.1099785827513808\ldots$, 12 significant figures:
>
> <!-- literal-source: C column is preserved history, no producer (qou-ft3p) -->
> | quantity | convention C (was) | convention D (now) |
> |:---|---:|---:|
> | $z$ | $0.499320334184$ | $0.612688037146$ |
> | $z^2$ | $0.249320796129$ | $0.375386630862$ |
> | $hz^2+z$ | $0.551443414318$ | $0.691166478358$ |
> | $4_1$ | $0.182304485938$ | $0.280195642273$ |
>
> The **convention-C column has no producer by design**: C was excised by the
> owner ruling of 2026-08-09, so nothing in the repo computes it and no
> witness can carry it. The **convention-D column is witnessed** by
> `computations/markov/markov-trace-canonical.witness.json` (6 assertions at
> $10^{-40}$) — the script this note already names below as the reproducer,
> which until now emitted no witness at all (bean `qou-ft3p`).
>
> $h$ is convention-independent. The $4_1$ closed form is new here: it was
> "(see witness)", and the witness held the C value. Reproduce with
> `python3 computations/markov/markov_trace_canonical.py`, whose prop-table
> check now gates at $10^{-40}$ rather than $10^{-9}$.

These constitute **dimensionless ratios** relative to the photon ($\mathfrak{m}_{q,\gamma} = 1$). Physical masses in MeV require a calibration constant $E_0$, determined by anchoring to one experimental value (e.g., the free neutron $\beta$-decay $Q$-value).

## Role in the unified mass formula

This proposition supplies the $k = 0$ stratum of the curvature-rank decomposition ([unified mass formula](#prop:unified-curvature-rank-mass-formula)): $\mathfrak{m}^{(0)}_{q,\mathcal{K}}(1) = |\!\int_A\! \rho(\beta_\mathcal{K})|$ is the descended Frobenius integral, equal to $E_\infty^{0,*}$ of the GB spectral sequence.

The integral $\int_A \rho(\beta_\mathcal{K})$ is **vortex-specific**, distinguishing $\varrho_{\mathfrak{p}}$ from $\varrho_{\mathfrak{n}}$ and capturing fine isotope variations. The vortex-independent constant offset is the Frobenius co-Casimir $m_e \cdot \tau(C_{\dim_q})$ ([Frobenius universal](#thm:frobenius-codim-universal)). The full mass is:

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \sum_{k \geq 0} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(1)
       \;+\; m_e \cdot \tau(C_{\dim_q}),
$$

with this proposition governing the $k = 0$ component.
