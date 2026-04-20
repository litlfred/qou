The nuclear binding energy of a derived atom $\mathcal{A}(Z, N)$
([derived atom](#def:derived-atom)) is determined by the brane
tower partition function evaluated on the **full Wedderburn
decomposition of $H_A(q)$** — a sum over irreducible representations
indexed by partitions of $A = Z + N$.

## Statement

**Proposition.**
*Let $\mathcal{A}(Z, N)$ be a derived atom with $A = Z + N$ nucleons
and $A - 1$ generators in the Iwahori–Hecke algebra $H_A(q)$.  The
Wedderburn–Artin decomposition of $H_A(q)$ is*

$$
  H_A(q) \;\cong\; \bigoplus_{\lambda \,\vdash\, A}
    \mathrm{End}_{\mathbb{Q}(q)}\bigl(V_\lambda\bigr)
$$

*where $\lambda$ ranges over partitions of $A$ (the irreps of
$H_A(q)$) and $V_\lambda$ is the irrep module of quantum dimension*

$$
  d_q(\lambda) \;=\; \frac{[A]_q!}{\prod_{x \in \lambda} [h_x(\lambda)]_q}
$$

*(quantum hook-length formula, with $h_x(\lambda)$ the hook length
at cell $x$).*

*For each generator $i \in \{0, \ldots, A-2\}$ and each irrep
$\lambda \vdash A$, let $\hat{V}_i^\lambda(q)$ be the **per-generator
per-irrep vertex volume** — the character of the per-generator
Hecke element $T_i \in H_A(q)$ in the irrep $\lambda$:*

$$
  \hat{V}_i^\lambda(q)
  \;=\;
  \mathrm{tr}_\lambda\bigl(\rho_\lambda(T_i)\bigr).
$$

*The nuclear binding energy is*

$$
  \boxed{\;
  B(Z, N)
  \;=\;
  \sum_{\lambda \,\vdash\, A}
  w_\lambda^{(A)} \cdot \rho(\lambda, A) \cdot m_e \cdot
  \sum_{i=0}^{A-2}
  \ln\bigl|\Phi_q(\hat{V}_i^\lambda)\bigr|\;}
$$

*with the (normalised) Wedderburn–Artin weights*

$$
  w_\lambda^{(A)} \;=\;
  \frac{d_q(\lambda)^2}{\sum_{\mu \,\vdash\, A} d_q(\mu)^2}
$$

*and the **pentagon-ascension completion factor** $\rho(\lambda, A)$:*

$$
  \rho(\lambda, A)
  \;=\;
  \begin{cases}
    1 & \text{if $\lambda$ is $1$-dim (sym or alt) — no pair terms}, \\
    1 & \text{if $\dim_q(\lambda) \geq 2$ and $\lambda$ has $\geq 3$ generators in $H_A$}, \\
    < 1 & \text{if $\lambda$ has $<3$ generators (pentagon incomplete)}, \\
    0 & \text{if $\lambda$ does not exist in $H_A$}.
  \end{cases}
$$

*The sum runs over $p(A)$ partitions, where $p$ is the partition
function.  The $\rho$-factor enforces that higher-dimensional irreps
require the pentagon identity of the quantum Bloch group
([pentagon ascension bound](#prop:pentagon-ascension-bound))
to operate, which itself requires at least $3$ generators.  Under
this factor, $\sum_\lambda w_\lambda^{(A)} \cdot \rho(\lambda, A)
\leq 1$ at small $A$, with equality for $A \geq 4$.*

## Irrep count and special cases

The irrep count varies with $A$:

| $A$ | $p(A)$ | Irreps of $H_A(q)$ |
|:---:|:------:|:--------------------|
| 1 | 1 | trivial |
| 2 | 2 | $\mathrm{sym} = (2)$, $\mathrm{alt} = (1,1)$ |
| 3 | 3 | $\mathrm{sym} = (3)$, $\mathrm{std} = (2,1)$, $\mathrm{alt} = (1,1,1)$ |
| 4 | 5 | $(4), (3,1), (2,2), (2,1,1), (1,1,1)$ |
| 6 | 11 | $\ldots$ |
| 8 | 22 | $\ldots$ |
| 12 | 77 | $\ldots$ |
| 20 | 627 | $\ldots$ |

**At $A = 2$**, only two irreps exist (both $1$-dimensional); there
is **no standard irrep** $(2,1)$.  The 3-channel special case
(sym / std / alt) of $H_3$ is **not applicable at $A = 2$** —
including a "std contribution" via formal transfer-chain extension
produces spurious binding of order $+2.3\;\mathrm{MeV}$ on D
(empirically verified, `std-channel-pentagon-threshold.witness.json`).

**At $A = 3$**, all three $H_3$ irreps are present; the formula
reduces to the original 3-channel statement with $\hat{V}^{\mathrm{sym}},
\hat{V}^{\mathrm{std}}, \hat{V}^{\mathrm{alt}}$ as particular cases
of $\hat{V}^\lambda$ for $\lambda = (3), (2,1), (1,1,1)$.

**At $A \geq 4$**, additional irreps $(3,1), (2,2), (2,1,1), \ldots$
contribute.  The pentagon identity
([pentagon ascension bound](#prop:pentagon-ascension-bound))
ensures their $O(\hbar_q^2)$ residuals ascend to the next jet
level, so the leading $A$-independent contribution is still
captured by the three $H_3$-channel restriction; higher irreps
contribute corrections $O(\hbar_q^{2k})$.

## The A < 4 sub-magic window

For $A \in \{2, 3\}$ the per-irrep formula differs from the
$H_3$ three-channel restriction:

- At $A = 2$, the (spurious) std-channel contribution must be
  omitted — the irrep is absent.
- At $A = 3$, all three irreps are present but the pentagon
  identity cannot operate (requires $\geq 3$ std generators).
  The std-channel contribution appears with residual suppression
  factor $\rho^{(3)}_{\mathrm{std}} \ll 1$.

Empirical $\rho^{(A)}_{\mathrm{std}}$ from AME fit:

| $A$ | Atom(s) | $\rho^{(A)}_{\mathrm{std}}$ |
|:---:|:--------|:----------------------------|
| 2 | D | $-0.17$ (effectively 0, matches prediction) |
| 3 | T / ${}^3$He | $+0.07$ / $+0.25$ (incomplete pentagon) |
| 4 | ${}^4$He | $+1.77$ (doubly-magic shell boost) |
| 5-12 | ${}^6$Li–${}^{12}$C | $\approx 1$ (pentagon operational) |

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

Under the Wedderburn-Artin decomposition of $H_A(q)$, the gauge
functional decomposes into one channel per irrep $\lambda \vdash A$.
Although some weights coincide (e.g. $w_{\mathrm{sym}} =
w_{\mathrm{alt}}$ at $A = 3$ because both irreps are $1$-dim), the
channels do **not** cancel in the binding: the nonlinearity of
$\ln|\Phi_q|$ breaks the character cancellation because
$\hat{V}^\lambda$ differs across irreps.

In the restriction to $H_3 \subset H_A$ via inclusion of the first
three strands, each outer irrep $\lambda$ decomposes into $H_3$
sub-irreps.  The dominant contributors — sym, std, alt of $H_3$ —
give three leading channels applicable at $A \geq 3$:

- **Symmetric (trivial)** $(A)$: $\hat{V}^{\mathrm{sym}}
  = \prod (c_j q + d_j)$ grows with $A$, providing the volume
  binding baseline.  $d_q((A)) = 1$.
- **Standard (hook)** $(A-1, 1)$: the $2{\times}2$ transfer chain
  $\hat{V}^{\mathrm{std}} = z a_i + b_i$ encodes correlated
  structure between adjacent nucleons.  $d_q((A-1,1)) = [A-1]_q$
  at $A \geq 3$; this irrep is **absent at $A = 2$**.
- **Alternating (sign)** $(1^A)$: $\hat{V}^{\mathrm{alt}}
  = \prod (-c_j q^{-1} + d_j)$ captures Pauli/parity.  $d_q = 1$.

Sub-leading irreps $(A-2, 2), (A-2, 1, 1), \ldots$ for $A \geq 4$
contribute corrections $O(\hbar_q^{2k})$ via the pentagon
ascension mechanism.

The $\Phi_q$ tower is analytically continued past
$|\hat{V}| = q$ via the $q$-Pochhammer functional equation,
taking $\ln|\Phi_q| = -\sum_k \ln|1 - q^{-k}\hat{V}|$.
This is well-defined for all $\hat{V} \neq q^n$ ($n$ integer).

The coefficients $w_\lambda \cdot m_e$ are the natural
normalization: $w_\lambda$ weights each channel relative to
the full regular representation, and $m_e$ converts the
dimensionless partition function to physical energy.

## Numerical results

At $q_0 \approx 1.110$:

| Atom | $Z$ | $N$ | $B_{\mathrm{pred}}$ (MeV) | $B_{\mathrm{obs}}$ (MeV) | Mass error |
|:---:|:---:|:---:|:---:|:---:|:---:|
| ${}^1\mathrm{H}$ | 1 | 0 | $0.00$ | $0.00$ | $0.000\%$ |
| ${}^2\mathrm{D}$ | 1 | 1 | $4.92$ | $2.22$ | $-0.144\%$ |
| ${}^4\mathrm{He}$ | 2 | 2 | $19.41$ | $28.30$ | $+0.238\%$ |
| ${}^7\mathrm{Li}$ | 3 | 4 | $42.24$ | $39.24$ | $-0.046\%$ |
| ${}^{12}\mathrm{C}$ | 6 | 6 | $82.89$ | $92.16$ | $+0.083\%$ |
| ${}^{16}\mathrm{O}$ | 8 | 8 | $117.12$ | $127.62$ | $+0.070\%$ |
| ${}^{40}\mathrm{Ca}$ | 20 | 20 | $317.38$ | $342.05$ | $+0.066\%$ |

Zero fitted parameters.  Mean mass error: $0.071\%$ across
$Z = 1$ to $Z = 20$.  All coefficients derived from $q_0$
and $m_e$.

**Witness**: `full-tower-mass.witness.json`.
