*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Conjecture.**
*In the quotient atom model $H_{Z+1}(q)$ — where the nuclear
core is a single strand $\mathcal{N}$ and each electron is a
strand $e_k$ — the growth ratio
$\gamma(Z) = n(Z)/n(Z-1)$ of the Gröbner–Shirshov normal form
term count separates three regimes:*

$$
  \gamma(Z) \in
  \begin{cases}
    \{1\}         & \text{s-shell pairing (exact)} \\
    [1.2,\, 1.4]  & \text{p-shell pairing (approximate)} \\
    [3.0,\, 4.0]  & \text{sub-shell opening}
  \end{cases}
$$

*No $Z$ falls in the gap $(1.4, 3.0)$.  This gap is the
algebraic shell gap of the Hecke chain.*

## Setup

**The quotient atom model.**  Given a neutral atom with $Z$
protons, $N$ neutrons, and $Z$ electrons, quotient the nuclear
core $\mathcal{N}(Z, N)$ to a single formal variable.  The
resulting element lives in $H_{Z+1}(q)$ with crossing types:

| Pair | Element | Coefficients |
|:-----|:--------|:-------------|
| $\mathcal{N}\text{-}e$ | $(\sigma^{-1})^Z$ | Chebyshev (see below) |
| $e\text{-}e$ | $\sigma$ | $(1,\; 0)$ |

The nucleus–electron crossing is the $Z$-fold composition
$(\sigma^{-1})^Z$, not the scalar multiple $Z \cdot \sigma^{-1}$.
In the braid picture, quotienting $Z$ proton strands to one
means the electron wraps $Z$ times.

**Closed form.**  The Hecke relation $\sigma^2 = h\sigma + 1$
reduces $(\sigma^{-1})^Z = c_Z \sigma + d_Z$ with eigenvalues
$q^{-Z}$ (trivial) and $(-q)^Z$ (sign):

$$
  c_Z = \frac{q^{-Z} - (-1)^Z q^Z}{[2]_q}, \qquad
  d_Z = \frac{q^{-(Z+1)} + (-1)^Z q^{Z+1}}{[2]_q}
$$

These are Chebyshev $U$-type polynomials in $h = q - q^{-1}$
with the Hecke eigenvalues $q^{-1}$ and $-q$ as roots.
The sign of $c_Z$ alternates: positive for odd $Z$, negative
for even $Z$.  This alternation drives the pairing mechanism.

**The NF.** Build the atom by sequential Hopf-linking:
start with $\mathcal{N}$, add $e_1, e_2, \ldots, e_Z$ one at
a time, reducing via Gröbner–Shirshov at each step.

## Computational evidence

The quotient NF term count for $Z = 1$ through $8$
(corrected $(\sigma^{-1})^Z$ crossing):

| $Z$ | Atom | $n(Z)$ | $\gamma$ | $|c_Z|$ | PAL | Regime |
|:----|:-----|:-------|:---------|:---------|:----|:-------|
| 1 | H | 2 | — | $1.000$ | $\star$ | |
| 2 | He | 2 | $1.00$ | $0.209$ | $\star$ | s-pair close |
| 3 | Li | 6 | $3.00$ | $1.044$ | $\star$ | sub-shell open |
| 4 | Be | 6 | $1.00$ | $0.427$ | $\star$ | s-pair close |
| 5 | B | 24 | $4.00$ | $1.133$ | — | sub-shell open |
| 6 | C | 30 | $1.25$ | $0.664$ | — | p-pair close |
| 7 | N | 120 | $4.00$ | $1.272$ | — | sub-shell open |
| 8 | O | 156 | $1.30$ | $0.930$ | — | p-pair close |

**The algebraic shell gap.**  The growth ratio $\gamma$ falls
into two bands separated by the gap $(1.4, 3.0)$:

- **Pairing band** $\gamma \leq 1.4$: even $Z$, the second
  electron in a sub-shell pair.  For s-shells ($Z = 2, 4$),
  $\gamma = 1.00$ exactly — no new NF words.  For p-shells
  ($Z = 6, 8$), $\gamma \approx 1.25$–$1.30$ — a few new words
  from the growing $(\sigma^{-1})^Z$ coefficients.

- **Opening band** $\gamma \geq 3.0$: odd $Z$, a new sub-shell
  electron.  The NF triples or quadruples as genuinely new
  reduced words appear in $H_{Z+1}(q)$.

The gap separating these bands is the **algebraic shell gap** —
a discrete structural feature of the Hecke normal form that
encodes the pairing principle without any input from angular
momentum or spin.

## Pairing mechanism

The Chebyshev sign alternation of $c_Z$ drives pairing:

- **Odd $Z$** (sub-shell opening): $c_Z > 0$, $d_Z < 0$.
  The crossing element $c_Z \sigma + d_Z$ is $\sigma$-heavy.
  The positive $\sigma$ coefficient creates new reduced words
  at higher word-lengths, expanding the NF.

- **Even $Z$** (pairing): $c_Z < 0$, $d_Z > 0$.
  The crossing is identity-heavy.  The negative $\sigma$
  coefficient cancels against existing NF words rather than
  creating new ones, suppressing growth.

For s-shells, the suppression is exact ($\gamma = 1$) because
$|c_Z|$ is small ($0.209$ at $Z = 2$, $0.427$ at $Z = 4$).
For p-shells, $|c_Z|$ has grown ($0.664$ at $Z = 6$, $0.930$
at $Z = 8$) so the suppression is only approximate
($\gamma \approx 1.3$).

## Global scaling

All coefficients in the $Z$-electron quotient atom carry a
global prefactor $Z^Z$:

$$
  \text{coeff}(\mathcal{A}(Z)) \in Z^Z \cdot \mathbb{Z}[q, q^{-1}]
$$

For carbon ($Z = 6$): $6^6 = 46656$ appears in every term.

## Scope and limitations

The $\gamma < 2$ criterion detects **electron pairing**
(every even $Z$), not full noble-gas shell closures
($Z = 2, 10, 18, 36, \ldots$).  The 1D Hecke chain
$H_{Z+1}(q)$ encodes radial shell structure but lacks
angular momentum — it cannot distinguish $2p^2$ ($Z = 6$)
from $2p^6$ ($Z = 10$, neon).  Detecting noble-gas closures
would require a product structure
$H_{Z+1}(q) \otimes \mathrm{Rep}(\mathrm{SO}(3))$
where the Hecke chain handles radial pairing and the
rotation group handles sub-shell degeneracy $2\ell + 1$.
