The single-vortex mass formula admits a **unified presentation**
via the pentagon operation that structurally trivialises to the
"linear form" at $A \leq 3$ without any case distinction.

## Starting point

From [mass endomorphism tower](#prop:mass-endomorphism-tower), the
per-irrep mass is a sum over nonempty subsets of the
$A - 1$ Hecke generators:

$$
  \mathfrak{m}^\lambda(\varrho) \;=\; \sum_{\varnothing \neq S \subseteq \{0,\dots,A-2\}}
  z^{|S|-1} \cdot \Phi_q\!\Bigl(\prod_{i \in S} \hat V_i^\lambda\Bigr).
$$

The Markov weight $z^{|S|}$ is stripped by one factor of $z$ during
the descent from tree-level to loop-level (the leading $|S|=1$ term
has coefficient $1$).

## Pentagon reduction

When the pentagon identity operates — i.e. when
$\hat V_i \hat V_j = q^{\pm 2}\,\hat V_j \hat V_i$ for all $i < j$
in $S$ — the quantum dilogarithm $\Phi_q$ factorises:

$$
  \Phi_q\!\Bigl(\prod_i \hat V_i\Bigr) \;=\; \prod_i \Phi_q(\hat V_i).
$$

Substituting into $\mathfrak{m}^\lambda$ yields the **Euler generating
function** over the per-generator dilogarithms:

$$
  \mathfrak{m}^\lambda(\varrho) \;=\; \frac{1}{z}\Bigl[\prod_{i=0}^{A-2}\!
  \bigl(1 + z\,\Phi_q(\hat V_i^\lambda)\bigr) - 1\Bigr].
$$

## Structural crossover at $A = 4$

This single formula encodes both regimes:

**$A \leq 3$ (pentagon cannot close).**  With $A - 1 \leq 2$
generators there are too few insertions to satisfy the pentagon
(Faddeev–Kashaev) relation.  Expanding the product:

$$
  \mathfrak{m}^\lambda \;\big|_{A=3} \;=\; \Phi_q(\hat V_0^\lambda) + \Phi_q(\hat V_1^\lambda)
  + z \cdot \Phi_q(\hat V_0^\lambda) \Phi_q(\hat V_1^\lambda).
$$

This is the **linear form** — a bare sum of $\Phi_q$'s with one
pair-correction.  Taking $\ln|\mathfrak{m}^\lambda|$ does NOT split
into $\sum_i \ln|\Phi_q(\hat V_i)|$ because the pentagon cannot
ascend the pair.

**$A \geq 4$ (pentagon operational).**  The product
$\prod_i(1 + z\,\Phi_q(\hat V_i))$ is dominated by its top-degree
term $z^{A-1}\prod_i \Phi_q(\hat V_i)$ when $|\Phi_q(\hat V_i)| \gg 1/z$.
Then

$$
  \ln|\mathfrak{m}^\lambda| \;\approx\; (A-2)\ln z + \sum_{i=0}^{A-2}\ln|\Phi_q(\hat V_i^\lambda)|
  + O(\hbar_q^2),
$$

recovering the **log form**.

## Descent to binding

The Archimedean descent
([Archimedean fibre descent](#prop:archimedean-fibre-descent)) gives

$$
  B(Z, N) \;=\; \sum_{\lambda \vdash A} w_\lambda^{(A)} \cdot m_e
  \cdot \ln|\mathfrak{m}^\lambda(\varrho_{Z,N})|,
$$

with $w_\lambda^{(A)} = d_q(\lambda)^2 / \sum_\mu d_q(\mu)^2$ the
Wedderburn weights at $H_A(q)$ — **one** formula for all $A \geq 2$.

## Operational note

The numerical fit of this unified formula to AME data is somewhat
looser than the separately optimised linear/log conventions (≈0.4%
vs. 0.01–0.2% when the pair $R$-factor is tuned per regime).  The
discrepancy is the **pentagon residual** $R(u,v) = \Phi_q(uv) /
(\Phi_q(u)\Phi_q(v))$, which the operational formula sets to $1$.

The exact formula

$$
  \mathfrak{m}^\lambda = \sum_{\varnothing \neq S} z^{|S|-1} \Phi_q\Bigl(\prod_{i\in S} \hat V_i\Bigr)
$$

retains the $R$-factor structure and agrees with the operational
reduction at $A \geq 4$ up to $O(\hbar_q^2)$.  The triple and higher
subset contributions are empirically verified negligible at three
decimal places (see
`b-consistent-all-orders.witness.json`), but must be **retained for
$1$ ppm precision**.
