**Notation register (resolved collision).**
This paper now uses two distinct symbols for what were previously
both written $y_\lambda$:

1. *Jones–Markov central coefficients* — keeps $y_\lambda$.  These
   appear in the trace expansion $\mathrm{tr}_M = \sum_\lambda
   y_\lambda \chi_\lambda$
   ([procedure](#prop:alpha-k-derivation-procedure),
   [explicit H_3](#prop:explicit-alpha-k-h3)).  **Sign-indefinite**
   — the subject of this remark.
2. *Operator-selection LP dual variables* (shadow prices) — written
   $u_\lambda$ (Schrijver LP-duality convention) in the
   operator-selection LP
   ([BW shadow price](#prop:mass-coefficient-shadow-price)).
   **Non-negative** by LP duality.

The two symbols denote unrelated quantities and should never be
conflated.  In what follows, $y_\lambda$ refers exclusively to sense
(1) (Jones–Markov central coefficient).  The choice $u_\lambda$ for
LP shadow prices avoids collision with $\pi_\lambda$, already used
in [BW shadow price](#prop:mass-coefficient-shadow-price) for the
central idempotents of the Wedderburn block decomposition.

**Empirical observation.**
At the canonical Markov parameter $z = 1/(\sqrt q + 1/\sqrt q)$ and
substrate $q_0 = 1.109978595554181\ldots$ (50 dps), the Jones–Markov block weights
$y_\lambda$ from
([procedure](#prop:alpha-k-derivation-procedure)) are non-negative
for $n \leq 3$ but acquire negative components at $n \geq 4$.  The
LP feasibility problem

$$
  \text{find } y \in \mathbb{R}^{p(n)} :
  \quad A(q_0)\, y = b(q_0), \quad y \geq 0
$$

is **infeasible** at $n = 4, 5, 6$ — empirically verified via
[`y_lambda_sdp.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_sdp.py).
The full sign pattern at $n \in \{2, \ldots, 6\}$ — including the
sign-changing entries $y_{(1^4)} \approx -8.4 \times 10^{-4}$ at
$n = 4$ and $y_{(2, 1^3)} \approx -9.3 \times 10^{-4}$ at $n = 5$
— is recorded in
[`y-lambda-jones-markov-witness.json`](https://github.com/litlfred/qou/blob/main/computations/y-lambda-jones-markov-witness.json).

The negative components are small in absolute value but
non-negligible — they enter every $\alpha_k$ derivation and the
unified mass formula at the right depths.

**Why this is not a contradiction.**
The Markov trace is positive on positive elements: for any
$a \in H_n(R, q)$, $\mathrm{tr}_M(a^\ast a) \geq 0$.  In the
central decomposition $\mathrm{tr}_M = \sum_\lambda y_\lambda
\chi_\lambda$, each character $\chi_\lambda$ is itself indefinite
on $H_n(R, q)$ — $\chi_\lambda(a^\ast a)$ may be negative for some
$a$.  Positivity of $\mathrm{tr}_M$ is preserved through
cancellation across blocks: the negative $y_\lambda \cdot
\chi_\lambda(a^\ast a)$ contributions are dominated by positive
terms in the sum.  This is the standard operator-algebraic
phenomenon of an indefinite signature on the centre yet a
positive total trace.

**Structural reading.**
The negative-$y_\lambda$ partitions at $n = 4, 5$ are
$(1^4)$ and $(2, 1, 1, 1)$ — both deep in the alternating-block
sector ($\mathrm{depth}(\lambda) = n - 1$ and $n - 2$).  This
matches the qualitative picture: the alternating idempotent
$e_{(1^n)}$ is "the chirality block", and chirality-dominant
configurations contribute with negative weight in the central
expansion.  The cancellation against positive symmetric / standard
contributions is what keeps mass observables positive.

**Implication for LP/SDP formulations.**
The LP

$$
  \text{find } y :
  \quad A y = b, \quad y \geq 0
$$

is infeasible at $n \geq 4$, so it is **not** a viable formulation
of the Markov-trace problem.  The correct convex variant is the
SDP moment-matrix on the regular representation of $H_n(R, q)$:

$$
  \text{find } M \succeq 0 :
  \quad M_{1, 1} = 1, \quad
  M_{\sigma_n w, w'} = z \cdot M_{w, w'},
  \quad \text{(Hecke + Markov rels.)}
$$

— positivity is on the **functional**, encoded as the moment
matrix, not on the block weights $y_\lambda$.  The SDP recovers
the unique positive trace at every $q$ (including root-of-unity
$q$ where the linear system is singular) and produces the same
$y_\lambda$ values, with their sign pattern intact.

**Cross-check status.**
At $n \in \{2, \ldots, 6\}$, the unconstrained LS solve (cvxpy /
CLARABEL) reproduces the linear-solve $y_\lambda$ to $\sim 10^{-15}$
([`y-lambda-sdp-witness.json`](#)).  Symbolic linear-solve via
sympy
([`y_lambda_symbolic.py`](#)) gives exact $q$-rational forms,
matching the numerical values to machine precision at $q_0$.  All
three pathways agree; the negative components are real, not
artifacts.
