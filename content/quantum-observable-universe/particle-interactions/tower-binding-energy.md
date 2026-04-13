The nuclear binding energy of a derived atom $\mathcal{A}(Z, N)$
([derived atom](#def:derived-atom)) is determined by the brane
tower partition function evaluated on the $2{\times}2$ standard
channel of $H_3(q)$.

## Statement

**Proposition.**
*Let $\mathcal{A}(Z, N)$ be a derived atom with $A + Z$ strands
and $A + Z - 1$ generators in $H_{A+Z}(q)$.  For each generator
$i$, let $M_i \in \mathrm{M}_2(\mathbb{R})$ be the accumulated
$2{\times}2$ standard-representation matrix obtained by multiplying
all typed crossings at generator $i$ through the Garside staircase,
including LP-derived gluon crossings
([integer LP gluon](#prop:mass-endomorphism-tower)).*

*The brane tower partition function at generator $i$ is*

$$
  Z_i(q)
  =
  \prod_{k=1}^{\infty}
  \det\!\bigl(I - q^{-k} M_i\bigr)^{-1},
$$

*converging when both eigenvalues of $M_i$ satisfy $|\lambda| < q$.*

*The nuclear binding energy is*

$$
  B(Z, N)
  =
  w_{\mathrm{std}}(q) \cdot m_e
  \cdot
  \sum_{i=0}^{A+Z-2}
  \ln\bigl|Z_i(q)\bigr|,
$$

*where $w_{\mathrm{std}} = [2]_q^2 / ([2]_q^2 + 2)$ is the
Wedderburn weight of the standard irrep of $H_3(q)$, and $m_e$
is the electron mass (energy scale).*

*The atomic mass is then*

$$
  M(Z, N)
  =
  Z \cdot m_{\mathfrak{p}}
  + N \cdot m_{\mathfrak{n}}
  + Z \cdot m_e
  - B(Z, N).
$$

## Derivation

The binding energy arises from the gauge sector of the categorical
action ([canonical action](#prop:qou-canonical-action)):

$$
  \mathcal{S}_{\mathrm{gauge}}
  =
  \int_A \mathrm{tr}_A\bigl(
    F_\nabla \wedge_q \star_q F_\nabla
  \bigr).
$$

Under the Wedderburn decomposition of $H_3(q)$, the gauge
functional decomposes into three channels.  Since the Wedderburn
weights satisfy $w_{\mathrm{sym}} = w_{\mathrm{alt}}$, the
symmetric and alternating contributions cancel in the binding
([charge--mass duality](#rem:hecke-charge-mass-duality)).
Only the **standard channel** (dim $= 2$) contributes.

The standard channel carries the $2{\times}2$ transfer matrix
$M_i$ at each generator.  The brane tower
([recursive brane tower](#def:recursive-brane-tower)) evaluates
the gauge functional at each tower level $k$ with weight
$q^{-k}$, giving the product $\prod_k \det(I - q^{-k}M_i)^{-1}$.
This is the **VOA partition function**
$Z_i = \mathrm{tr}_{V}(q^{L_0} M_i)$
([vertex operator](#def:vertex-operator)) at generator $i$.

The coefficient $w_{\mathrm{std}} \cdot m_e$ is the natural
normalization: $w_{\mathrm{std}}$ weights the standard channel
relative to the full regular representation, and $m_e$ converts
the dimensionless partition function to physical energy (the
scalar ambiguity of the Frobenius form $\int_A$).

## Numerical results

At $q_0 \approx 1.110$ with $w_{\mathrm{std}} \approx 0.669$
and $w_{\mathrm{std}} \cdot m_e \approx 0.342$ MeV:

| Atom | $A$ | $\sum \ln|Z_i|$ | $B_{\mathrm{pred}}$ (MeV) | $B_{\mathrm{obs}}$ (MeV) | Error |
|:---:|:---:|:---:|:---:|:---:|:---:|
| ${}^4\mathrm{He}$ | 4 | $82.9$ | $28.0$ | $28.3$ | $-1.1\%$ |
| ${}^{12}\mathrm{C}$ | 12 | $302.8$ | $102.3$ | $92.2$ | $+11.0\%$ |
| ${}^{16}\mathrm{O}$ | 16 | $413.4$ | $139.7$ | $127.6$ | $+9.5\%$ |
| ${}^{40}\mathrm{Ca}$ | 40 | $1044.8$ | $353.0$ | $342.1$ | $+3.2\%$ |

Zero fitted parameters.  The coefficient $w_{\mathrm{std}} \cdot m_e$
is derived from the Wedderburn decomposition and the energy scale.

**Witness**: `full-tower-mass.witness.json`.
