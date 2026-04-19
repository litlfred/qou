Let $\hat{V}_i^\lambda(q)$ be the per-generator vertex volume in
Wedderburn channel $\lambda \in \{\mathrm{sym}, \mathrm{std},
\mathrm{alt}\}$ at the base brane level $n = 0$
([tower binding energy](#prop:tower-binding-energy)), viewed as a
function of the substrate parameter $q$.  Recall the brane tower
$\mathbf{A}_{n+1} = \mathbf{A}_n \otimes \Omega^1(\mathbf{A}_n)$
([recursive brane tower](#def:recursive-brane-tower)), where
$\Omega^1$ is the module of Kähler differentials of the substrate
coordinate ring.

## Statement

**Definition (Kähler jet lift).**
*The **Kähler-differential jet lift** of $\hat{V}_i^\lambda$ at
level $n$ is*

$$
  \hat{V}_i^{\lambda,\,(n+1)}(q)
  \;=\;
  \hat{V}_i^{\lambda,\,(n)}(q)
  \;+\;
  \hbar_q \cdot q \cdot
  \frac{d\,\hat{V}_i^{\lambda,\,(n)}}{d q}(q),
$$

*with base case $\hat{V}_i^{\lambda,\,(0)}(q) = \hat{V}_i^\lambda(q)$
from [tower binding energy](#prop:tower-binding-energy) and
$\hbar_q = (q - 1)/q$.  The coefficient $q \cdot d/dq$ is the
**logarithmic derivation** — the natural $q$-derivation dual to
the 1-form $d\log q$ under the Frobenius pairing
([knot factor Frobenius pairing](#prop:knot-factor-frobenius-pairing)).*

## Structural role

At each jet level $n$, the mass contribution inherits the
$\hbar_q^{2n}$ damping factor of the recursive brane tower:

$$
  \mathfrak{m}
  \;=\;
  \sum_{n=0}^{\infty} \hbar_q^{2n} \cdot \mathfrak{m}^{(n)},
  \qquad
  \mathfrak{m}^{(n)}
  \;=\;
  \sum_\lambda w_\lambda \cdot m_e
  \sum_{i=0}^{A-2} \ln\bigl\lvert
  \Phi_q\bigl(\hat{V}_i^{\lambda,\,(n)}(q)\bigr)
  \bigr\rvert.
$$

The level-0 term $\mathfrak{m}^{(0)}$ is the formula of
[tower binding energy](#prop:tower-binding-energy); the higher
levels are the Kähler corrections via this definition.

## Well-definedness

The definition presumes $\hat{V}_i^\lambda(q)$ is **differentiable
in $q$ on the open window $q \in (1, q^*)$** where $q^* = q$ is
the first pole of $\Phi_q$.  For the three Wedderburn channels of
$H_3(q)$ the vertex volumes are:

- $\hat{V}_i^{\mathrm{sym}}(q) = \prod_j (c_j q + d_j)$
  — polynomial in $q$, smooth.
- $\hat{V}_i^{\mathrm{alt}}(q) = \prod_j (-c_j/q + d_j)$
  — rational in $q$, smooth for $q > 0$.
- $\hat{V}_i^{\mathrm{std}}(q) = z(q) \cdot a_i(q) + b_i(q)$
  with $z(q) = 1/(\sqrt{q} + 1/\sqrt{q})$ and $a_i, b_i$ polynomials
  in $h = q - q^{-1}$ — smooth for $q > 0$.

All three channels are therefore differentiable, and the Kähler
jet lift is well-defined for each.

## Link to the Markov stabilisation

A simpler lift used in provisional computations
([canonical Markov plus multibrane tower](https://github.com/litlfred/qou/blob/claude/continue-hamdover-QGLMZ/folio-assistant/computations/canonical_plus_multibrane.py))
is the **Markov stabilisation**  $\hat{V}_i^{(n)} = z^n \cdot
\hat{V}_i^{(0)}$.  This is an order-0 approximation of the Kähler
jet lift: it preserves the scaling $\hbar_q$ but misses the
$q \cdot dV/dq$ correction.  The Markov stabilisation is correct
for atoms where $V$ is roughly $q$-independent; it diverges when
the per-atom NF has strong $q$-dependence (e.g. T, ${}^3\mathrm{He}$
at $q_0 \approx 1.11$ where $V \to q$).

## Convergence of the Kähler tower

**Conjecture.**
*For $q \in (1, q_*)$ strictly below the first Pochhammer pole, the
Kähler jet series $\sum_n \hbar_q^{2n} \mathfrak{m}^{(n)}$
converges absolutely.  Sharpness and the convergence radius
$q_*$ are open; heuristically $q_* = q^{1/2}$ from the
leading-pole expansion of $\Phi_q$.*

Empirical support: session 2026-04-19 witness data on D, ${}^4$He,
${}^{12}$C show mean error $0.071\%$ at level 0 alone; higher
levels (via Markov stabilisation at least) are expected to reduce
this further under the Kähler correction above.

## Code reference

Numeric stub: `lift_V_kahler(V_func, level, delta_q=1e-6)` in
[`folio-assistant/computations/canonical_plus_multibrane.py`](https://github.com/litlfred/qou/blob/claude/continue-hamdover-QGLMZ/folio-assistant/computations/canonical_plus_multibrane.py#L144).
The code evaluates $V(q \pm \delta)$, central-differences to
obtain $dV/dq$, and applies the formula above iteratively.

**Witness**: `kahler-pade-probe.witness.json` (level-1 convergence
data for light atoms).
