The Gröbner--Shirshov normal form of each nucleon in $H_3(q)$ has exactly **six terms**, one for each basis element of the Iwahori--Hecke algebra. With typed crossings ($u$-$u = \sigma$, $d$-$d = \sigma - (q - q^{-1})\mathbf{1}$, $u$-$d = \sigma - \tfrac{1}{2}(q - q^{-1})\mathbf{1}$), the sign pattern differs between neutron and proton. We classify each term by **word length** $\ell$ and **observability** (whether the corresponding knot or link is topologically non-trivial).

## The six normal form terms

| Particle | Word | Knot/Link | $\ell$ | Neutron $\mathfrak{n}$ | Proton $\mathfrak{p}$ | Observable? |
|:---:|:---:|:---:|:---:|---:|---:|:---:|
| $\gamma$ | $\mathbf{1}$ | photon | $0$ | $-0.201704$ | $-0.099658$ | No (identity) |
| $\sigma_0$ | $\sigma_0$ | virtual | $1$ | $+0.048130$ | $+0.035729$ | No (virtual) |
| $\sigma_1$ | $\sigma_1$ | virtual | $1$ | $+1.008995$ | $+0.997570$ | No (virtual) |
| $L_+$ | $\sigma_0\sigma_1$ | Hopf link | $2$ | $-0.009641$ | $+0.099354$ | Yes (Hopf link) |
| $L_-$ | $\sigma_1\sigma_0$ | Hopf link | $2$ | $+0.009237$ | $+0.009337$ | Yes (Hopf link) |
| $e^-$ | $\sigma_0\sigma_1\sigma_0$ | trefoil ($3_1$) | $3$ | $-0.044184$ | $-0.043208$ | Yes (trefoil) |

Numerical values at $q_0 \approx 1.1100$ (typed crossings).

## Sign patterns

With typed crossings, the sign patterns are:

- **Neutron**: $[-, +, +, -, +, -]$ — four terms negative ($\gamma, L_+, e^-$). The $L_+$ coefficient flips from positive (untyped) to negative.
- **Proton**: $[-, +, +, +, +, -]$ — two terms negative ($\gamma, e^-$), unchanged from untyped.

The neutron's $L_+$ sign flip represents the key effect of typed crossings: the $d$-$d$ crossing in the neutron $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ shifts the $\sigma_0\sigma_1$ coefficient below zero.

## Observability criterion

A braid word of length $\ell$ is **observable** when the corresponding knot or link is topologically non-trivial:

- **$\ell = 0$**: The identity $\mathbf{1}$ maps to the photon $\gamma$. It is topologically trivial and carries no knot content.
- **$\ell = 1$**: A single crossing $\sigma_i$ can be undone by a Reidemeister-I move. It constitutes a **virtual crossing** (topologically removable). The terms $\sigma_0$ and $\sigma_1$ are virtual.
- **$\ell = 2$**: The products $\sigma_0\sigma_1$ and $\sigma_1\sigma_0$ form Hopf links. These two linked rings cannot be separated by any ambient isotopy, making them topologically non-trivial and observable.
- **$\ell = 3$**: The product $\sigma_0\sigma_1\sigma_0$ is the trefoil knot, the simplest non-trivial knot. This represents the electron $e^-$.

## Positive coefficients: observable vs virtual

The positive terms split into two classes:

|  | Observable ($\ell \geq 2$) | Virtual ($\ell < 2$) |
|:---:|---:|---:|
| **Neutron** | $+0.009$ ($L_-$ only) | $+1.057$ ($\sigma_0, \sigma_1$) |
| **Proton** | $+0.109$ ($L_+, L_-$) | $+1.033$ ($\sigma_0, \sigma_1$) |

Both nucleons are **dominated by virtual content**: the $\sigma_1$ term carries $\sim 94\%$ of the total positive amplitude. This term possesses word length $\ell = 1$, representing a single topologically trivial crossing. It cannot be observed as a free particle.

The observable positive terms are the **Hopf links** $L_+ = \sigma_0\sigma_1$ (proton only) and $L_- = \sigma_1\sigma_0$ (both nucleons). These are bound states of two linked rings. Note that $L_+$ is **negative** for the neutron, as the typed $d$-$d$ crossing transforms it into a debt.

## Location of $\sigma_1$: the color tube fiber

The generator $\sigma_1$ exchanges strands $1$ and $2$ in the $3$-strand braid (the crossing between the second and third quark lines). In the color tube geometry ([color tube fibers](#def:color-tube-fibers)), these strands map to color coordinates:

- **$\sigma_0$** acts on the $(\sigma, r)$ plane. This is the crossing between the space-like backbone $\sigma = w_1 - z$ and the first color tube coordinate $r = w_2 - z$.
- **$\sigma_1$** acts on the $(r, g)$ plane. This is the crossing **within the color tube fiber** between the red and green color coordinates $r = w_2 - z$ and $g = w_3 - z$.

The dominance of $\sigma_1$ thus implies: **the nucleon's internal energy resides overwhelmingly in the color tube fiber direction** — in the relative motion of color charges within the tube, not in the coupling between color and spacetime. This provides the algebraic expression of **color confinement**: the dominant dynamics remain internal to the color tube, invisible from the spacetime base.

## Linearity of the normal form

The transition $\Delta_i = \mathrm{coeff}_i(\mathfrak{n}) - \mathrm{coeff}_i(\mathfrak{p})$ computes the normal form of the **transition element** $\mathfrak{n} - \mathfrak{p} \in H_3(q)$. This holds because coordinate extraction in the Gröbner--Shirshov basis acts as a linear map on the vector space $H_3(q)$ ($\dim = 3! = 6$):

$$
  \mathrm{NF}(\mathfrak{n} - \mathfrak{p})
  = 
  \mathrm{NF}(\mathfrak{n}) - \mathrm{NF}(\mathfrak{p}).
$$

## Sign pattern and beta decay

The negative terms in each nucleon represent **leptonic debt** — topological content that must be supplied by (or released to) the vacuum. In the typed-crossing normal form:

|  | $\gamma$ debt | $L_+$ debt | $e^-$ debt |
|:---:|---:|---:|---:|
| **Neutron** | $-0.201704$ | $-0.009641$ | $-0.044184$ |
| **Proton** | $-0.099658$ | — | $-0.043208$ |

The neutron carries three debts ($\gamma, L_+, e^-$) while the proton carries only two ($\gamma, e^-$). The excess:

$$
  \Delta_\nu = -0.10205, \qquad \Delta_{L_+} = -0.10899,
  \qquad \Delta_{e^-} = -0.00098
$$

drives beta decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar{\nu}_e$. The neutron pays down its excess debt by emitting the physical electron and antineutrino.

## Summary

The nucleon normal form exhibits a clean tripartite structure:

1. **Virtual bulk** ($\ell \leq 1$, positive): $\sim 94\%$ of the amplitude. Confined inside the color tube fiber. Unobservable.
2. **Observable links** ($\ell = 2$, signed): Hopf-linked bound states. $L_-$ is positive for both nucleons; $L_+$ is positive for the proton but **negative for the neutron** (typed-crossing effect).
3. **Leptonic debt** ($\ell = 0$ and $\ell = 3$, negative): The neutrino and electron channels carry negative coefficients, dictating the required inputs from the vacuum. Beta decay settles this debt.

**Witness**: `free-neutron-decay.witness.json` (typed crossings; 17 reductions for $\mathfrak{n}$; 18 for $\mathfrak{p}$).
