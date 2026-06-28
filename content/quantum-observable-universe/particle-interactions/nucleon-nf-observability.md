The Gröbner--Shirshov normal form of each nucleon in $H_3(q)$ has exactly
**six terms**, one for each basis element of the Iwahori--Hecke algebra.
With typed crossings ($u$-$u = \sigma$, $d$-$d = \sigma - (q - q^{-1})\mathbf{1}$,
$u$-$d = \sigma - \tfrac{1}{2}(q - q^{-1})\mathbf{1}$), the sign pattern
differs between neutron and proton.  We classify each term by
**word length** $\ell$ and **observability** — whether the
corresponding knot/link is topologically non-trivial.

## Observability structure of the nucleon normal form

### The six NF terms

| Particle | Word | Knot/Link | $\ell$ | Neutron $\mathfrak{n}$ | Proton $\mathfrak{p}$ | Observable? |
|:---:|:---:|:---:|:---:|---:|---:|:---:|
| $\gamma$ | $\mathbf{1}$ | photon | $0$ | $-0.201704$ | $-0.099658$ | No (identity) |
| $\sigma_0$ | $\sigma_0$ | virtual | $1$ | $+0.048130$ | $+0.035729$ | No (virtual) |
| $\sigma_1$ | $\sigma_1$ | virtual | $1$ | $+1.008995$ | $+0.997570$ | No (virtual) |
| $L_+$ | $\sigma_0\sigma_1$ | Hopf link | $2$ | $-0.009641$ | $+0.099354$ | Yes (Hopf link) |
| $L_-$ | $\sigma_1\sigma_0$ | Hopf link | $2$ | $+0.009237$ | $+0.009337$ | Yes (Hopf link) |
| $e^-$ | $\sigma_0\sigma_1\sigma_0$ | trefoil ($3_1$) | $3$ | $-0.044184$ | $-0.043208$ | Yes (trefoil) |

Numerical values at $q_0 \approx 1.1100$ (typed crossings).

### Sign patterns

With typed crossings, the sign patterns are:

- **Neutron**: $[-, +, +, -, +, -]$ — four terms negative ($\gamma, L_+, e^-$)
  and **$L_+$ flips** from positive (untyped) to negative.
- **Proton**: $[-, +, +, +, +, -]$ — two terms negative ($\gamma, e^-$),
  unchanged from untyped.

The neutron's $L_+$ sign flip is the key effect of typed crossings:
the $d$-$d$ crossing in neutron $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$
shifts the $\sigma_0\sigma_1$ coefficient below zero.

### Observability criterion

A braid word of length $\ell$ is **observable** when the
corresponding knot or link is topologically non-trivial:

- **$\ell = 0$**: the identity $\mathbf{1}$ maps to the photon $\gamma$.
  Topologically trivial — carries no knot content.
  This is the photon channel $\gamma$.

- **$\ell = 1$**: a single crossing $\sigma_i$ can be undone by
  a single Reidemeister-I move.  It is a **virtual crossing** —
  topologically removable.  The terms $\sigma_0$ and
  $\sigma_1$ are virtual.

- **$\ell = 2$**: the products $\sigma_0\sigma_1$ and
  $\sigma_1\sigma_0$ are Hopf links — two linked rings that
  **cannot** be separated by any ambient isotopy.
  Topologically non-trivial and therefore observable.

- **$\ell = 3$**: the product $\sigma_0\sigma_1\sigma_0$ is
  the trefoil knot — the simplest non-trivial knot.  This is
  the electron $e^-$.

### Positive coefficients: observable vs virtual

The positive terms split into two classes:

|  | Observable ($\ell \geq 2$) | Virtual ($\ell < 2$) |
|:---:|---:|---:|
| **Neutron** | $+0.009$ ($L_-$ only) | $+1.057$ ($\sigma_0, \sigma_1$) |
| **Proton** | $+0.109$ ($L_+, L_-$) | $+1.033$ ($\sigma_0, \sigma_1$) |

Both nucleons are **dominated by virtual content**: the $\sigma_1$
term carries $\sim 94\%$ of the total positive amplitude.
This term has word length $\ell = 1$ — a single crossing that is
topologically trivial.  It cannot be observed as a free particle.

The observable positive terms are the **Hopf links**
$L_+ = \sigma_0\sigma_1$ (proton only) and
$L_- = \sigma_1\sigma_0$ (both), which are bound states of
two linked rings.  Note that $L_+$ is **negative** for the
neutron — the typed $d$-$d$ crossing turns it into a debt.

### Location of $\sigma_1$: the color tube fiber

The generator $\sigma_1$ exchanges strands $1$ and $2$ in the
$3$-strand braid — the crossing between the second and third quark
lines.  In the color tube geometry
([color tube fibers](#def:color-tube-fibers)), these strands map to
the color coordinates:

- **$\sigma_0$** acts on the $(\sigma, r)$ plane — the crossing
  between the space-like backbone $\sigma = w_1 - z$ and the first
  color tube coordinate $r = w_2 - z$.

- **$\sigma_1$** acts on the $(r, g)$ plane — the crossing
  **within the color tube fiber** between the red and green color
  coordinates $r = w_2 - z$ and $g = w_3 - z$.

The dominance of $\sigma_1$ therefore means: **the nucleon's
internal energy lives overwhelmingly in the color tube fiber
direction** — in the relative motion of color charges within the
tube, not in the coupling between color and spacetime.  This is the
algebraic expression of **color confinement**: the dominant
dynamics is internal to the color tube, invisible from the
spacetime base.

### Linearity of the normal form

The transition $\Delta_i = \mathrm{coeff}_i(\mathfrak{n}) -
\mathrm{coeff}_i(\mathfrak{p})$ is itself the normal form of the
**transition element** $\mathfrak{n} - \mathfrak{p} \in H_3(q)$.
This follows because $\mathrm{NF}$ is a linear map — coordinate
extraction in the Gröbner--Shirshov basis (a vector space basis
for $H_3(q)$, $\dim = 3! = 6$):

$$
  \mathrm{NF}(\mathfrak{n} - \mathfrak{p})
  = 
  \mathrm{NF}(\mathfrak{n}) - \mathrm{NF}(\mathfrak{p}).
$$

### Sign pattern and beta decay

The negative terms in each nucleon represent **leptonic debt** —
topological content that must be supplied by (or released to) the
vacuum.  In the typed-crossing NF:

|  | $\gamma$ debt | $L_+$ debt | $e^-$ debt |
|:---:|---:|---:|---:|
| **Neutron** | $-0.201704$ | $-0.009641$ | $-0.044184$ |
| **Proton** | $-0.099658$ | — | $-0.043208$ |

The neutron carries three debts ($\gamma, L_+, e^-$) while the
proton carries only two ($\gamma, e^-$).  The excess:

$$
  \Delta_\nu = -0.10205, \qquad \Delta_{L_+} = -0.10899,
  \qquad \Delta_{e^-} = -0.00098
$$

drives beta decay
$\mathfrak{n} \to \mathfrak{p} + e^- + \bar{\nu}_e$:
the neutron pays down its excess debt by emitting the physical
electron and antineutrino.

## Summary

The nucleon NF has a clean tripartite structure:

1. **Virtual bulk** ($\ell \leq 1$, positive): $\sim 94\%$ of the
   amplitude.  Confined inside the color tube fiber.  Unobservable.

2. **Observable links** ($\ell = 2$, signed): Hopf-linked bound
   states.  $L_-$ is positive for both nucleons; $L_+$ is positive
   for proton but **negative for neutron** (typed-crossing effect).

3. **Leptonic debt** ($\ell = 0$ and $\ell = 3$, negative): the
   neutrino and electron channels carry negative coefficients.
   These are the inputs required from the vacuum; beta decay is the
   process of settling this debt.

Witness: `free-neutron-decay.witness.json` (typed crossings;
17 reductions for $\mathfrak{n}$; 18 for $\mathfrak{p}$).
