The Gröbner--Shirshov normal form of each nucleon in $H_3(q)$ has exactly
**six terms**, one for each basis element of the Iwahori--Hecke algebra.
The sign pattern is $[-, +, +, +, +, -]$ for both neutron and
proton.  We classify each term by **word length** $\ell$ and
**observability** — whether the corresponding knot/link is
topologically non-trivial.

## The six NF terms

| Basis | Word | $\ell$ | Neutron $\mathfrak{n}$ | Proton $\mathfrak{p}$ | Observable? |
|:---:|:---:|:---:|---:|---:|:---:|
| $\nu$ | $\mathbf{1}$ | $0$ | $-0.1373$ | $-0.0616$ | No (unknot) |
| $H^0$ | $\sigma_0$ | $1$ | $+0.0564$ | $+0.0473$ | No (virtual) |
| $H^1$ | $\sigma_1$ | $1$ | $+1.5350$ | $+1.2417$ | No (virtual) |
| $L_+$ | $\sigma_0\sigma_1$ | $2$ | $+0.1543$ | $+0.1920$ | Yes (Hopf link) |
| $L_-$ | $\sigma_1\sigma_0$ | $2$ | $+0.0137$ | $+0.0118$ | Yes (Hopf link) |
| $e^-$ | $\sigma_0\sigma_1\sigma_0$ | $3$ | $-0.0664$ | $-0.0530$ | Yes (trefoil) |

Numerical values at $q_0 \approx 1.1097$.

## Observability criterion

A braid word of length $\ell$ is **observable** when the
corresponding knot or link is topologically non-trivial:

- **$\ell = 0$**: the identity $\mathbf{1}$ is the unknot.
  Topologically trivial — passes through everything undetected.
  This is the neutrino channel $\nu$.

- **$\ell = 1$**: a single crossing $\sigma_i$ can be undone by
  a single Reidemeister-I move.  It is a **virtual crossing** —
  topologically removable.  The terms $H^0 = \sigma_0$ and
  $H^1 = \sigma_1$ are virtual.

- **$\ell = 2$**: the products $\sigma_0\sigma_1$ and
  $\sigma_1\sigma_0$ are Hopf links — two linked rings that
  **cannot** be separated by any ambient isotopy.
  Topologically non-trivial and therefore observable.

- **$\ell = 3$**: the product $\sigma_0\sigma_1\sigma_0$ is
  the trefoil knot — the simplest non-trivial knot.  This is
  the electron $e^-$.

## Positive coefficients: observable vs virtual

The four positive terms in each NF split into two classes:

|  | Observable ($\ell \geq 2$) | Virtual ($\ell < 2$) |
|:---:|---:|---:|
| **Neutron** | $+0.168$ (Hopf links) | $+1.591$ (crossings) |
| **Proton** | $+0.204$ (Hopf links) | $+1.289$ (crossings) |

Both nucleons are **dominated by virtual content**: the $\sigma_1$
term ($H^1$) carries $\sim 90\%$ of the total positive amplitude.
This term has word length $\ell = 1$ — a single crossing that is
topologically trivial.  It cannot be observed as a free particle.

The observable positive terms are exclusively the **Hopf links**
$L_+ = \sigma_0\sigma_1$ and $L_- = \sigma_1\sigma_0$, which are
bound states of two linked rings.

## Where $\sigma_1$ lives: the color tube fiber

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

## Sign pattern and beta decay

The two negative terms are precisely the **observable
endpoints** — the neutrino $\nu$ ($\ell = 0$) and the electron
$e^-$ ($\ell = 3$).  Both nucleons carry this debt:

|  | $\nu$ debt | $e^-$ debt |
|:---:|---:|---:|
| **Neutron** | $-0.1373$ | $-0.0664$ |
| **Proton** | $-0.0616$ | $-0.0530$ |

The neutron's debts are larger than the proton's.  The excess:

$$
  \Delta_\nu = -0.076, \qquad \Delta_{e^-} = -0.013
$$

is released in beta decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar{\nu}_e$:
the neutron pays down its excess $\nu$ and $e^-$ debt by emitting
the physical electron and antineutrino.

## Summary

The nucleon NF has a clean tripartite structure:

1. **Virtual bulk** ($\ell \leq 1$, positive): $\sim 90\%$ of the
   amplitude.  Confined inside the color tube fiber.  Unobservable.

2. **Observable links** ($\ell = 2$, positive): $\sim 10\%$ of the
   amplitude.  Hopf-linked bound states.  The nuclear binding
   visible as stable structure.

3. **Leptonic debt** ($\ell = 0$ and $\ell = 3$, negative): the
   neutrino and electron channels carry negative coefficients.
   These are the inputs required from the vacuum; beta decay is the
   process of settling this debt.

Witness: `free-neutron-decay.witness.json` (19 Hecke + 5 YB
reductions for $\mathfrak{n}$; 18 total for $\mathfrak{p}$).
