This appendix gives the complete NF decomposition of
$b_i \cdot \beta(T_{m,n}) \cdot b_j$ for every pair of NF basis
elements and every torus knot operator, **symbolic in
$h = q - q^{-1}$**.  All results are exact in $q$ — numerical
values appear only in the witness file for comparison at $q_0$.

**Notation.**  $h = q - q^{-1}$ (Hecke amplitude).  The NF basis
is $\{\ \gamma,\ \sigma_0,\ \sigma_1,\ L_+,\ L_-,\ e^-\ \}$.

**Witness**: `knot-operator-table.witness.json`.

---

## Table L.1: NF basis multiplication table ($T_{1,0}$ — identity operator)

The identity operator $\beta(T_{1,0}) = \mathbf{1}$ gives
the raw product $b_i \cdot b_j$.  Every entry below is **exact
in $h$**.

| $b_i \cdot b_j$ | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $\gamma \cdot b_j$ | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ |
| $\sigma_0 \cdot \gamma$ | $\sigma_0$ | | | | | |
| $\sigma_0 \cdot \sigma_0$ | $1$ | $h$ | — | — | — | — |
| $\sigma_0 \cdot \sigma_1$ | — | — | — | $1$ | — | — |
| $\sigma_0 \cdot L_+$ | — | — | $1$ | $h$ | — | — |
| $\sigma_0 \cdot L_-$ | — | — | — | — | — | $1$ |
| $\sigma_0 \cdot e^-$ | — | — | — | — | $1$ | $h$ |
| $\sigma_1 \cdot \gamma$ | $\sigma_1$ | | | | | |
| $\sigma_1 \cdot \sigma_0$ | — | — | — | — | $1$ | — |
| $\sigma_1 \cdot \sigma_1$ | $1$ | — | $h$ | — | — | — |
| $\sigma_1 \cdot L_+$ | — | — | — | — | — | $1$ |
| $\sigma_1 \cdot L_-$ | — | $1$ | — | — | $h$ | — |
| $\sigma_1 \cdot e^-$ | — | — | — | $1$ | — | $h$ |
| $L_+ \cdot \gamma$ | $L_+$ | | | | | |
| $L_+ \cdot \sigma_0$ | — | — | — | — | — | $1$ |
| $L_+ \cdot \sigma_1$ | — | $1$ | — | $h$ | — | — |
| $L_+ \cdot L_+$ | — | — | — | — | $1$ | $h$ |
| $L_+ \cdot L_-$ | $1$ | $h$ | — | — | — | $h$ |
| $L_+ \cdot e^-$ | — | — | $1$ | $h$ | $h$ | $h^2$ |
| $L_- \cdot \gamma$ | $L_-$ | | | | | |
| $L_- \cdot \sigma_0$ | — | — | $1$ | — | $h$ | — |
| $L_- \cdot \sigma_1$ | — | — | — | — | — | $1$ |
| $L_- \cdot L_+$ | $1$ | — | $h$ | — | — | $h$ |
| $L_- \cdot L_-$ | — | — | — | $1$ | — | $h$ |
| $L_- \cdot e^-$ | — | $1$ | — | $h$ | $h$ | $h^2$ |
| $e^- \cdot \gamma$ | $e^-$ | | | | | |
| $e^- \cdot \sigma_0$ | — | — | — | $1$ | — | $h$ |
| $e^- \cdot \sigma_1$ | — | — | — | — | $1$ | $h$ |
| $e^- \cdot L_+$ | — | $1$ | — | $h$ | $h$ | $h^2$ |
| $e^- \cdot L_-$ | — | — | $1$ | $h$ | $h$ | $h^2$ |
| $e^- \cdot e^-$ | $1$ | $h$ | $h$ | $h^2$ | $h^2$ | $h^3+h$ |

**Key observations:**

1. **$e^-$ channel universality under $T_{2,3}$**: When
   $\beta = \sigma_0\sigma_1\sigma_0$ (trefoil) is inserted
   between any pair, the $e^-$ coefficient is always nonzero.
   For the identity operator ($T_{1,0}$), only 19/36 pairs
   produce $e^-$.

2. **$e^- \cdot e^- = \gamma + h\sigma_0 + h\sigma_1 + h^2 L_+ + h^2 L_- + (h^3+h)e^-$**:
   the self-product of the electron populates all six basis
   elements.  The $e^-$ coefficient is $h^3 + h = h(h^2 + 1)$,
   which is always positive for $q > 1$.

3. **No negative coefficients** appear in any basis product.
   Negative NF coefficients arise only from inverse elements
   ($\sigma_i^{-1}$), i.e., antiparticles.

---

## Table L.2: $T_{2,3}$ operator (trefoil / electron)

$\beta(T_{2,3}) = \sigma_0\sigma_1\sigma_0 = e^-$.

The product $b_i \cdot e^- \cdot b_j$ is computed by composing
the $T_{1,0}$ table entries.  Key entries (symbolic in $h$):

| $b_i \cdot e^- \cdot b_j$ | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $\gamma \cdot e^- \cdot \gamma$ | — | — | — | — | — | $1$ |
| $\sigma_0 \cdot e^- \cdot \sigma_1$ | — | — | — | — | $h$ | $h^2+1$ |
| $\sigma_1 \cdot e^- \cdot \sigma_0$ | — | — | — | $h$ | — | $h^2+1$ |
| $\gamma \cdot e^- \cdot e^-$ | $1$ | $h$ | $h$ | $h^2$ | $h^2$ | $h^3+h$ |
| $e^- \cdot e^- \cdot \gamma$ | $1$ | $h$ | $h$ | $h^2$ | $h^2$ | $h^3+h$ |
| $e^- \cdot e^- \cdot e^-$ | $h^3+h$ | $h^4+h^2$ | $h^4+h^2$ | ... | ... | ... |

**All 36 pairs produce nonzero $e^-$ coefficient under $T_{2,3}$.**

This is the fundamental result:
the trefoil operator **unconditionally opens the electron
channel** regardless of the incoming state, confirming
$T_{2,3}$ as the universal pair-production operator.

---

## Table L.3: $T_{2,1}$ operator (single crossing)

$\beta(T_{2,1}) = \sigma_0$.

| $b_i \cdot \sigma_0 \cdot b_j$ | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $\gamma \cdot \sigma_0 \cdot \gamma$ | — | $1$ | — | — | — | — |
| $\sigma_0 \cdot \sigma_0 \cdot \sigma_0$ | $h$ | $h^2+1$ | — | — | — | — |
| $\sigma_0 \cdot \sigma_0 \cdot \sigma_1$ | — | — | $1$ | $h$ | — | — |
| $\sigma_1 \cdot \sigma_0 \cdot \sigma_1$ | — | — | — | — | — | $1$ |
| $L_+ \cdot \sigma_0 \cdot L_-$ | $1$ | $h$ | $h$ | $h^2$ | $h^2$ | $h^3+h$ |

**24/36 pairs produce $e^-$ under $T_{2,1}$** — but the
photon-photon pair ($\sigma_0 \cdot \sigma_0 \cdot \sigma_0$)
does **not**.  $T_{2,1}$ requires specific polarization content
to open the electron channel.

---

## Summary: operator channel opening

| Operator | Braid word | Pairs with $e^- \neq 0$ | $\gamma \cdot T \cdot \gamma$ has $e^-$? |
|:---:|:---:|:---:|:---:|
| $T_{1,0}$ | $\mathbf{1}$ | 19/36 | **No** |
| $T_{2,1}$ | $\sigma_0$ | 24/36 | **No** |
| $T_{2,2}$ | $\sigma_0^2 = h\sigma_0 + \gamma$ | 24/36 | **No** |
| $T_{2,3}$ | $\sigma_0\sigma_1\sigma_0 = e^-$ | **36/36** | **Yes** ($= 1$) |
| $T_{2,5}$ | $(\sigma_0\sigma_1)^2\sigma_0$ | **36/36** | **Yes** ($= h^2$) |

$T_{2,3}$ is the **unique lowest-crossing operator that
unconditionally produces the electron channel for all incoming
pairs**.  Higher operators ($T_{2,5}$, etc.) also open all
channels but at higher crossing energy cost ($h^2$ vs $1$
for the photon-photon pair).

**Witness**: `knot-operator-table.witness.json`,
`gram-matrix-dual.witness.json`.
