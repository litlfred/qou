**Conjecture.**
*In the quotient atom model $H_{Z+1}(q)$ — where the nuclear core is a single strand $\mathcal{N}$ and each electron is a strand $e_k$ — the growth ratio $\gamma(Z) = n(Z)/n(Z-1)$ of the Gröbner–Shirshov normal form term count separates three regimes:*

$$
  \gamma(Z) \in
  \begin{cases}
    \{1\}         & \text{s-shell pairing (exact)} \\
    [1.2,\, 1.4]  & \text{p-shell pairing (approximate)} \\
    [3.0,\, 4.0]  & \text{sub-shell opening}
  \end{cases}
$$

*No $Z$ falls in the gap $(1.4, 3.0)$. This gap is the algebraic shell gap of the Hecke chain.*

## Setup

**The quotient atom model.** Given a neutral atom with $Z$ protons, $N$ neutrons, and $Z$ electrons, we quotient the nuclear core $\mathcal{N}(Z, N)$ to a single formal variable. The resulting element lives in $H_{Z+1}(q)$ with crossing types:

See [Table 1](#tbl:shell-closure-nf-term-count-table1-data).

The nucleus–electron crossing is the $Z$-fold composition $(\sigma^{-1})^Z$, not the scalar multiple $Z \cdot \sigma^{-1}$. In the braid picture, quotienting $Z$ proton strands to one means the electron wraps $Z$ times.

**Closed form.** The Hecke relation $\sigma^2 = h\sigma + 1$ reduces $(\sigma^{-1})^Z = c_Z \sigma + d_Z$ with eigenvalues $q^{-Z}$ (trivial) and $(-q)^Z$ (sign):

$$
  c_Z = \frac{q^{-Z} - (-1)^Z q^Z}{[2]_q}, \qquad
  d_Z = \frac{q^{-(Z+1)} + (-1)^Z q^{Z+1}}{[2]_q}
$$

These are Chebyshev $U$-type polynomials in $h = q - q^{-1}$ with the Hecke eigenvalues $q^{-1}$ and $-q$ as roots. The sign of $c_Z$ alternates. It is positive for odd $Z$ and negative for even $Z$. This alternation drives the pairing mechanism.

**Proved (algebraic engine).** The reduction $(\sigma^{-1})^Z = c_Z\sigma + d_Z$ with these closed forms, and the sign-alternation $c_Z<0$ (even $Z$) / $c_Z>0$ (odd $Z$) with $|c_Z|$ strictly increasing for $q>1$, is established rigorously by diagonalising $\sigma$ in the two-dimensional $H_2(q)$ (eigenvalues $q,-q^{-1}$, so $(\sigma^{-1})^Z$ has eigenvalues $q^{-Z},(-1)^Zq^Z$). This is confirmed numerically as an exact $q$-independent identity to $10^{-40}$. The conjectural content is how its sign-alternation propagates through the full Gröbner–Shirshov reduction of the quotient atom in $H_{Z+1}(q)$ to the three $\gamma$-regimes above.

**The NF.** We build the atom by sequential Hopf-linking. We start with $\mathcal{N}$ and add $e_1, e_2, \ldots, e_Z$ one at a time, reducing via Gröbner–Shirshov at each step.

## Computational evidence

The quotient NF term count for $Z = 1$ through $8$ (corrected $(\sigma^{-1})^Z$ crossing):

See [Table 2](#tbl:shell-closure-nf-term-count-table2-data).

**The algebraic shell gap.** The growth ratio $\gamma$ falls into two bands separated by the gap $(1.4, 3.0)$:

- **Pairing band** $\gamma \leq 1.4$: even $Z$, the second electron in a sub-shell pair. For s-shells ($Z = 2, 4$), $\gamma = 1.00$ exactly (no new NF words). For p-shells ($Z = 6, 8$), $\gamma \approx 1.25$–$1.30$ (a few new words from the growing $(\sigma^{-1})^Z$ coefficients).

- **Opening band** $\gamma \geq 3.0$: odd $Z$, a new sub-shell electron. The NF triples or quadruples as genuinely new reduced words appear in $H_{Z+1}(q)$.

The gap separating these bands is the **algebraic shell gap**. This discrete structural feature of the Hecke normal form encodes the pairing principle without input from angular momentum or spin.

## Pairing mechanism

The Chebyshev sign alternation of $c_Z$ drives pairing:

- **Odd $Z$** (sub-shell opening): $c_Z > 0$, $d_Z < 0$. The crossing element $c_Z \sigma + d_Z$ is $\sigma$-heavy. The positive $\sigma$ coefficient creates new reduced words at higher word-lengths, expanding the NF.

- **Even $Z$** (pairing): $c_Z < 0$, $d_Z > 0$. The crossing is identity-heavy. The negative $\sigma$ coefficient cancels against existing NF words rather than creating new ones, suppressing growth.

For s-shells, the suppression is exact ($\gamma = 1$) because $|c_Z|$ is small ($0.209$ at $Z = 2$, $0.427$ at $Z = 4$). For p-shells, $|c_Z|$ has grown ($0.664$ at $Z = 6$, $0.930$ at $Z = 8$) so the suppression is approximate ($\gamma \approx 1.3$).

## Global scaling

All coefficients in the $Z$-electron quotient atom carry a global prefactor $Z^Z$:

$$
  \text{coeff}(\mathcal{A}(Z)) \in Z^Z \cdot \mathbb{Z}[q, q^{-1}]
$$

For carbon ($Z = 6$), $6^6 = 46656$ appears in every term.

## Scope and limitations

The $\gamma < 2$ criterion detects electron pairing (every even $Z$), not full noble-gas shell closures ($Z = 2, 10, 18, 36, \ldots$). The 1D Hecke chain $H_{Z+1}(q)$ encodes radial shell structure but lacks angular momentum. It cannot distinguish $2p^2$ ($Z = 6$) from $2p^6$ ($Z = 10$, neon). Detecting noble-gas closures requires a product structure $H_{Z+1}(q) \otimes \mathrm{Rep}(\mathrm{SO}(3))$ where the Hecke chain handles radial pairing and the rotation group handles sub-shell degeneracy $2\ell + 1$.
