## Worked example: tritium

${}^3\mathrm{H}(p, n, n) \to {}^3\mathrm{He}(p, p, n)$.
Converting nucleon: position 1 (first neutron to proton).

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

Generator $\sigma_1$ (the converting nucleon's own generator)
contributes $78\%$ of the total --- consistent with the generator
volume profile for heavier nuclei.
