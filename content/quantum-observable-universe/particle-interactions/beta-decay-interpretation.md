## Universality

The universality $\Delta_\beta^{nn \to \mathrm{mix}} = \Delta_\beta^{\mathrm{mix} \to pp}$ means the matrix perturbation produced by converting one nucleon from $\mathfrak{n}$ to $\mathfrak{p}$ is the same regardless of whether the partner nucleon is a proton or a neutron.

This is a consequence of the crossing coefficients being equally spaced:

$$
  T_{\mathrm{mix}} = \tfrac{1}{2}(T_{pp} + T_{nn})
$$

The mixed matrix is exactly the midpoint. Therefore the steps $T_{nn} \to T_{\mathrm{mix}}$ and $T_{\mathrm{mix}} \to T_{pp}$ are the same displacement $\Delta_\beta$.

**Physical interpretation**: Beta decay shifts each crossing at the converting nucleon by the same universal amount $\Delta_\beta(q)$, independent of the partner. The effect on the Skein polynomial depends only on the number of crossings affected and their positions in the transfer matrix chain.

## Worked example: tritium

Consider ${}^3\mathrm{H}(p, n, n) \to {}^3\mathrm{He}(p, p, n)$. The converting nucleon is at position 1 (first neutron to proton).

**Generator $\sigma_0$** (2 crossings: with nucleons 1 and 2):

| Crossing | Parent | Daughter | Change |
|----------|--------|----------|--------|
| $(0, 1)$ | $\mathfrak{p}\mathfrak{n}$ = mixed | $\mathfrak{p}\mathfrak{p}$ = pp | $+\Delta_\beta$ |
| $(0, 2)$ | $\mathfrak{p}\mathfrak{n}$ = mixed | $\mathfrak{p}\mathfrak{n}$ = mixed | unchanged |

$$
  M_0^{\mathrm{par}} = T_{\mathrm{mix}} \cdot T_{\mathrm{mix}},
  \quad
  M_0^{\mathrm{dau}} = T_{pp} \cdot T_{\mathrm{mix}}
$$

$$
  \hat{V}_0^{\mathrm{par}} = 0.7684, \quad
  \hat{V}_0^{\mathrm{dau}} = 0.7510
$$

**Generator $\sigma_1$** (1 crossing: with nucleon 2):

| Crossing | Parent | Daughter | Change |
|----------|--------|----------|--------|
| $(1, 2)$ | $\mathfrak{n}\mathfrak{n}$ = nn | $\mathfrak{p}\mathfrak{n}$ = mixed | $+\Delta_\beta$ |

$$
  M_1^{\mathrm{par}} = T_{nn},
  \quad
  M_1^{\mathrm{dau}} = T_{\mathrm{mix}}
$$

$$
  \hat{V}_1^{\mathrm{par}} = 1.3029, \quad
  \hat{V}_1^{\mathrm{dau}} = 1.2036
$$

**Skein polynomial ratio:**

$$
  \frac{P_{{}^3\mathrm{He}}(q)}{P_{{}^3\mathrm{H}}(q)}
  = 
  \frac{0.7510 \times 1.2036}{0.7684 \times 1.3029}
  = 
  \frac{0.9039}{1.0011}
  =  0.9029
$$

$$
  \ln\!\left(\frac{P_{{}^3\mathrm{He}}}{P_{{}^3\mathrm{H}}}\right)
  =  -0.1021
$$

Per-generator contribution:

| Generator | $\ln(\hat{V}^{\mathrm{dau}}/\hat{V}^{\mathrm{par}})$ | Fraction |
|:---------:|:---:|:---:|
| $\sigma_0$ | $-0.0229$ | $22\%$ |
| $\sigma_1$ | $-0.0792$ | $78\%$ |

Generator $\sigma_1$ (the converting nucleon's own generator) contributes $78\%$ of the total. This matches the generator volume profile for heavier nuclei.

## Double beta decay

For $2\beta$ decay, two nucleons convert. At each affected generator, the transfer matrix perturbation is a product of two $\Delta_\beta$ matrices (with intervening unchanged matrices):

$$
  \Delta M_i^{(2\beta)}
  = 
  L_i \cdot \Delta_\beta \cdot C_i \cdot \Delta_\beta \cdot R_i
  + 
  (\text{linear terms})
$$

Here $C_i$ is the product of unchanged matrices between the two converting positions. The quadratic term $\Delta_\beta \cdot C_i \cdot \Delta_\beta$ is the 2-jet cross-term, which forms the nuclear matrix element of double beta decay ([jet expansion](#prop:generator-volume-decomposition)).

Since $\Delta_\beta$ is universal, the double beta matrix element depends only on $C_i$ — the unchanged matrices between the two converting nucleons. We compute this from the nucleon types in that region.
