**Step 1 — Frobenius pairing is σ-symmetric.**
The Frobenius pairing $\langle a, b \rangle_\tau := \tau(ab)$
satisfies, for all $a, b \in A$:

$$
  \langle \sigma(a), \sigma(b) \rangle_\tau
  = \tau(\sigma(a)\sigma(b))
  = \tau(\sigma(ba))
  = \tau(ba)
  = \langle b, a \rangle_\tau
  = \langle a, b \rangle_\tau,
$$

where the second equality is anti-multiplicativity, the third
is trace-invariance, and the last is symmetry of $\tau$ (the
Markov / cyclic property). Hence $\sigma$ is an isometry of the
Frobenius pairing.

**Step 2 — σ stabilises the constraint cone.**
Since $\Sigma$ is $\sigma$-stable, the polyhedral cone
$\mathcal{K}_+ := \{x \in A : \tau(\pi_\lambda \cdot x) \geq 0\
\forall \lambda \in \Sigma\}$ satisfies $\sigma(\mathcal{K}_+) =
\mathcal{K}_+$ (apply Step 1 to each constraint).

**Step 3 — σ stabilises the cost functional.**
Because $\sigma(c) = c$ and $\tau \circ \sigma = \tau$:

$$
  \tau(c \cdot \sigma(x))
  = \tau(\sigma(\sigma(c) \cdot x))
  = \tau(\sigma(c \cdot x))
  = \tau(c \cdot x).
$$

The cost is $\sigma$-invariant: replacing $x$ by $\sigma(x)$
does not change the objective.

**Step 4 — σ relates the two LPs.**
Define $\mathrm{LP}(\beta)$ to be the LP with input $\beta$.
The net constraint $\tau(\beta^* \beta \cdot x) =
n_{\mathrm{target}}(\beta)$ transforms under $x \mapsto
\sigma(x)$ to

$$
  \tau(\beta^* \beta \cdot \sigma(x))
  = \tau\bigl(\sigma(\sigma(\beta^*\beta) \cdot x)\bigr)
  = \tau(\sigma(\beta)^* \sigma(\beta) \cdot x),
$$

where we used $\sigma(\beta^*\beta) = \sigma(\beta)^* \sigma(\beta)$
(anti-multiplicativity preserves the involutive form $a^*a$
when $\sigma$ is a $*$-involution; for the Hecke / Markov case
this is the bar involution). Hence $\sigma$ is a bijection
between the feasible sets of $\mathrm{LP}(\beta)$ and
$\mathrm{LP}(\sigma(\beta))$, preserving the objective.

**Step 5 — LP-duality.**
By Steps 2–4, $\mathrm{LP}(\beta)$ and $\mathrm{LP}(\sigma(\beta))$
have feasible sets in $\sigma$-bijection and the same
$\sigma$-invariant cost; their primal optima coincide. By
strong duality (which holds for Frobenius algebras structurally
— see [`prop:frobenius-self-duality-forces-lp-dual-extraction`](#prop:frobenius-self-duality-forces-lp-dual-extraction)),
the dual optima coincide. In particular,

$$
  y_0^*\bigl(\sigma(\beta)\bigr) = y_0^*(\beta). \qquad
$\qquad\blacksquare$
