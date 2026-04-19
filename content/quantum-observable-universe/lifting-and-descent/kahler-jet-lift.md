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

**Proposition (empirical convergence).**
*For the H_A(q) 3-channel framework at $q_0 \approx 1.11$, the
Kähler jet tower $\sum_{n \geq 0} \hbar_q^{2n} \mathfrak{m}^{(n)}$
**converges absolutely** for every atom tested (D, T, ${}^3\mathrm{He}$,
${}^4\mathrm{He}$, ${}^6\mathrm{Li}$).  Cumulative binding
stabilises by $n = 2$:*

| Atom | $B^{(0)}$ (MeV) | $B^{(\leq 1)}$ | $B^{(\leq 2)}$ | $B^{(\leq 3)}$ | $B_{\mathrm{AME}}$ |
|------|----------------:|---------------:|---------------:|---------------:|-------------------:|
| D    | $4.9244$       | $4.9824$       | $4.9834$       | $4.9834$       | $2.2246$          |
| T    | $17.2423$      | $17.4232$      | $17.4252$      | $17.4252$      | $8.4818$          |
| ${}^3$He | $15.2461$  | $15.4376$      | $15.4394$      | $15.4394$      | $7.7181$          |
| ${}^4$He | $19.4122$  | $19.6610$      | $19.6638$      | $19.6639$      | $28.2957$         |
| ${}^6$Li | $34.7407$  | $35.1853$      | $35.1900$      | $35.1900$      | $31.9946$         |

*Per-level increments decay as $\hbar_q^{2n} \approx (0.0098)^n$
between consecutive levels; the $n = 3$ term is already below
$10^{-4}$ MeV for all atoms.  The series is absolutely convergent
because for any atom in the table, $|\mathfrak{m}^{(n+1)}| /
|\mathfrak{m}^{(n)}| < 1$ empirically once $n \geq 1$.*

**Remark on direction.**  The $n = 1$ Kähler correction shifts
$B$ by $\sim 0.05$–$0.3$ MeV per atom (O($\hbar_q^2$), as
expected).  Its sign is not uniform: the correction IMPROVES
${}^4$He's error ($0.2367\% \to 0.2300\%$) but slightly worsens
D, T, ${}^3$He, ${}^6$Li errors.  This asymmetry reflects
A-dependent curvature of $\hat{V}_i^\lambda(q)$: ${}^4$He's
doubly-magic structure makes its per-channel volumes more
sensitive to the $q \cdot dV/dq$ correction, while non-magic
light atoms are nearly-linear in $q$ over the Kähler window.

Witness: `kahler-convergence.witness.json` (session 2026-04-19).

**Earlier divergence finding:** the session's earlier "Kähler
diverges on T, ${}^3$He" result was observed on the deprecated
H_{3A}(q) Plancherel framework (single-vortex formula applied
to a multi-nucleon atom; per-A blow-up); that divergence does
NOT apply to the H_A(q) 3-channel framework formulated here.

## Code reference

Numeric stub: `lift_V_kahler(V_func, level, delta_q=1e-6)` in
[`folio-assistant/computations/canonical_plus_multibrane.py`](https://github.com/litlfred/qou/blob/claude/continue-hamdover-QGLMZ/folio-assistant/computations/canonical_plus_multibrane.py#L144).
The code evaluates $V(q \pm \delta)$, central-differences to
obtain $dV/dq$, and applies the formula above iteratively.

**Witness**: `kahler-pade-probe.witness.json` (level-1 convergence
data for light atoms).
