**Step 1: Frobenius pairing.** The Markov trace
$\tau : H_n(R,q) \to R$ satisfies
$\tau(ab) = \tau(ba)$ for all $a,b \in H_n$, and is
non-degenerate: if $\tau(ab) = 0$ for all $b$, then $a = 0$.
Non-degeneracy is the content of the
[Wedderburn trace identity](#prop:wedderburn-trace-identity)
$\sum_{\lambda \vdash n} \dim_q(\lambda)^2 = [n]_q!$, which
expresses $\tau$ as a strictly positive linear combination of
characters $\chi_\lambda$ on each Wedderburn block.

The pairing $\langle a, b \rangle_\tau := \tau(ab)$ is
therefore a non-degenerate symmetric bilinear form, making
$(H_n(R,q), \tau)$ a **Frobenius algebra** in the sense of
Frobenius (1903) and Nakayama (1939).

**Step 2: Self-duality isomorphism.** The map

$$
  \Phi_\tau : H_n(R,q) \longrightarrow H_n(R,q)^*,
  \quad a \mapsto \big(b \mapsto \tau(ab)\big)
$$

is an isomorphism of $R$-modules (and a bimodule isomorphism
when both sides carry the regular bimodule structure). This is
the canonical Frobenius self-duality.

**Step 3: Operator-selection LP under self-duality.** The
[operator-selection LP](#prop:operator-selection-lp) at level
$n$ has primal:

$$
  \min_{x \in H_n} \tau(\Theta \cdot x)
  \quad \text{s.t.} \quad
  \tau(\mathbf{1} \cdot x) = n_{\mathrm{target}}, \;\;
  \tau(\pi_\lambda \cdot x) \geq 0 \;\; \forall \lambda
$$

where $\Theta$ is the cost operator (knot-energy weight) and
$\pi_\lambda$ is the central idempotent for block $V_\lambda$.

The dual program is

$$
  \max_{u_0, u_\lambda \geq 0} n_{\mathrm{target}} u_0
  \quad \text{s.t.} \quad
  u_0 \mathbf{1} + \sum_\lambda u_\lambda \pi_\lambda
  \;\preceq_\tau\; \Theta
$$

where $\preceq_\tau$ denotes the partial order induced by the
Frobenius pairing: $a \preceq_\tau b \iff \tau(c \cdot (b - a))
\geq 0$ for all $c \succeq_\tau 0$.

**Step 4: Primal-dual coincidence (under standard LP
hypotheses).** Under $\Phi_\tau$, the primal feasible set
$P = \{x \in H_n : \tau(\pi_\lambda \cdot x) \geq 0\}$ is
$\Phi_\tau$-isomorphic to the dual feasible cone
$D = \{u : u \succeq_\tau 0\}$. The cost functional
$x \mapsto \tau(\Theta \cdot x)$ is, under $\Phi_\tau$,
identified with the dual objective $u \mapsto \langle u, \Theta
\rangle$. **Strong duality holds whenever the standard finite-
dimensional LP regularity conditions are met** — primal
feasibility and primal boundedness (or, equivalently for the
canonical operator-selection LP of
[`prop:operator-selection-lp`](#prop:operator-selection-lp),
existence of a strictly feasible point, i.e. Slater's
condition). For the per-atom operator-selection LP these
hypotheses are verified by direct construction in
[`prop:operator-selection-lp`](#prop:operator-selection-lp);
the proposition above adds *structurally* that the primal-
dual identification itself does not require additional
analytic argument because the Frobenius pairing is non-
degenerate. Strong duality + the Frobenius identification
together imply the $\tau$-extraction is the dual map.

**Step 5: τ-extraction is the dual map.** The Observation
Frame $\mathrm{Obs}_\tau : H_n(R,q) \to H_n(R,q)^*$ defined by
$\mathrm{Obs}_\tau(a) = \tau(a \cdot -)$ is **literally**
$\Phi_\tau$. Therefore, an observable produced by τ-extraction
is — *by definition* — a dual-space element.

**Consequence.** Every coefficient
$c_\lambda \in \mathbb{R}$ that arises as a τ-extracted
observable from a Frobenius-positivity-constrained LP is a
**shadow price** $u_\lambda^*$ of the corresponding constraint.
This is not a derivation; it is the structure of the
observation frame in a Frobenius-self-dual category.
$\qquad\blacksquare$
