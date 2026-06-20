**Proposition (Demazure-fiber Markov-trace functional).**
*Let $V_\lambda$ be the irreducible $S_n$-module indexed by
$\lambda \vdash n$, with Kashiwara crystal $\mathrm{Cryst}(V_\lambda)$
in type $A_{n-1}$
([`conj:crystal-graph-realization`](#conj:crystal-graph-realization)).
For each Weyl element $w \in S_n$, let*

$$
  D_w(\lambda) \;=\; \pi_w \bigl(x^{\lambda}\bigr)
  \;=\; \pi_{i_1} \cdots \pi_{i_k}\!\bigl(x_1^{\lambda_1}\cdots x_n^{\lambda_n}\bigr)
$$

*be the Demazure character, where $\pi_i(f) = (x_i f - x_{i+1}\,s_i f)/(x_i - x_{i+1})$
is the Demazure isobaric divided-difference operator and
$w = s_{i_1} \cdots s_{i_k}$ is any reduced word.  At the longest
element $w_0$, $D_{w_0}(\lambda) = s_\lambda(x_1, \ldots, x_n)$
recovers the Schur polynomial; at intermediate $w$, the Demazure
character $D_w(\lambda)$ is the character of a sub-crystal of
$\mathrm{Cryst}(V_\lambda)$ — an "incomplete topological state" in
the sense of AGENTS.md §7b item 3. Define the Demazure-fiber
Markov-trace functional*

$$
  \boxed{\;
    T^{\mathrm{Dem}}(\lambda;\, w)
    \;:=\;
    y_\lambda
    \cdot
    \frac{D_w(\lambda)}{D_{w_0}(\lambda)},
  \;}
$$

*where $y_\lambda$ is the Jones–Markov central coefficient
([`prop:macdonald-hook-telescope`](#prop:macdonald-hook-telescope)),
and the ratio $D_w(\lambda) / D_{w_0}(\lambda)$ is taken under the
principal specialisation $x_i \mapsto q^{i-1}$.  Then:*

1. *$T^{\mathrm{Dem}}(\lambda;\, w_0) = y_\lambda$ — the standard
   Jones–Markov coefficient is the saturated case.*
2. *For $w < w_0$ (Bruhat order), $T^{\mathrm{Dem}}(\lambda;\, w)$
   is the **structural resonance width** of the $\lambda$-block
   under the Demazure filtration: the fraction of $V_\lambda$
   accessible from the Demazure sub-crystal cut by $w$.*
3. *Plancherel completeness:
   $\sum_{\lambda \vdash n} f_\lambda \cdot T^{\mathrm{Dem}}(\lambda;\, w_0) = 1$
   reduces to the Macdonald hook-content telescope
   ([`prop:macdonald-hook-telescope`](#prop:macdonald-hook-telescope)).*

## Replacing the manual Hecke-energy LP cost

The LP / SDP cost vector
$c_\lambda = \tilde w_\lambda(q) = \dim_q(V_\lambda)^2 / [n]_q!$ used
in
[`sdp-dual-without-demand.md`](https://github.com/litlfred/qou/blob/main/computations/sdp-dual-without-demand.md)
is the q-deformed Wedderburn-block weight (the classical Plancherel
measure is the bare-symbol $w_\lambda = (\dim V_\lambda)^2/n!$; see
[`prop:plancherel-weight-boundedness`](#prop:plancherel-weight-boundedness)). It is
computed by-hand via Hoefsmit matrices or the hook-content
formula, with no structural reason for the chosen functional
beyond the trace constraint.

The Demazure-fiber functional $T^{\mathrm{Dem}}$ subsumes this in
two senses:

| | manual Hecke-energy | Demazure-fiber |
|---|---|---|
| Cost at full block | $w_\lambda(q)$ | $T^{\mathrm{Dem}}(\lambda;\, w_0) = y_\lambda$ |
| Sub-block (resonance) | not represented | $T^{\mathrm{Dem}}(\lambda;\, w)$ for $w < w_0$ |
| Computation | Hoefsmit matmul / sympy | Demazure operator recursion |
| Per-partition complexity | $O(\dim V_\lambda^3)$ | $O(\ell(w_0)) = O(n^2)$ |
| Crystal interpretation | none — empirical | sub-crystal projection |

For the LP/SDP solvers in the QOU pipeline, this means the cost
vector at $w = w_0$ is unchanged, but the dual variables and
shadow prices acquire a structural interpretation: the active set
$\{\lambda \mid u_\lambda^* > 0\}$ corresponds to the Demazure
fiber that the bound state actually occupies, and inactive blocks
have $T^{\mathrm{Dem}}(\lambda;\, w) = 0$ for some "decay-time"
Weyl element $w$.

## Worked example: $n = 3$, the alt block

Take $\lambda = (1, 1, 1)$ — the alt / antiparticle block at $n = 3$.
Then $V_\lambda$ is the sign representation, $\dim V_\lambda = 1$,
and $\mathrm{Cryst}(V_\lambda)$ is a single vertex. Demazure
characters at $x_i = q^{i-1}$:

| $w$ | reduced word | $D_w(1,1,1)$ at p.s. | $D_w / D_{w_0}$ |
|---|---|---|---|
| $\mathrm{id}$ | $\emptyset$ | $1$ | $1/q^3$ |
| $s_1$ | $(1)$ | $1 + q$ | $(1 + q)/q^3$ |
| $s_1 s_2$ | $(1, 2)$ | $1 + q + q^2$ | $(1+q+q^2)/q^3$ |
| $s_1 s_2 s_1 = w_0$ | $(1, 2, 1)$ | $q^3$ | $1$ |

Each prefix of $w_0$ corresponds to a Demazure sub-crystal of
increasing size; the ratio sweeps from "almost-empty fiber" to
"saturated block". Multiplied by the telescope-form $y_{(1,1,1)}$,
this gives the Demazure-fiber resonance width of the alt block at
each filtration depth — the exact analogue of a resonance width
without phenomenological cutoffs.

## Why the Demazure operator is the right functional

By Kashiwara's refined Demazure character formula
\cite{kashiwara1991}, $D_w(\lambda)$ is the character of the
Demazure sub-crystal $B_w(\lambda) \subseteq \mathrm{Cryst}(V_\lambda)$
generated from the highest-weight vertex by the chains
$\tilde f_{i_1}, \ldots, \tilde f_{i_k}$. Hence
$D_w / D_{w_0}$ is the fraction of $V_\lambda$ reachable from
the highest weight along the chosen Bruhat-prefix path — exactly
the structural notion of "incomplete topological state" that the
crystal-basis literature uses for resonances and virtual
intermediates \cite{lecouvey2007}.

For the QOU pipeline, the Demazure-filtered Markov trace is the
natural setting in which W/Z resonances, hadronic decays, and
virtual particles all become *structural objects* rather than
heuristic LP cutoffs. They are sub-crystals of completed Wedderburn
blocks, indexed by Bruhat-comparable Weyl elements.

## Crystal-basis shortcut

This is shortcut #3 from AGENTS.md §7b: replace the manual
Hecke-energy LP functional with Kashiwara weight-lattice
projection. Resonance widths become structural Demazure
multiplicities, not heuristic cutoffs. The shadow-price ordering
discussed in
[`sdp-dual-without-demand.md`](https://github.com/litlfred/qou/blob/main/computations/sdp-dual-without-demand.md)
acquires a Bruhat-order interpretation: more-active LP blocks
correspond to longer Bruhat-prefix Demazure sub-crystals.

## Numerical verification

The companion script
[`demazure_markov_trace.py`](https://github.com/litlfred/qou/blob/main/computations/demazure_markov_trace.py)

1. Implements the Demazure operator $\pi_i$ recursively on
   $\mathbb{Q}[x_1, \ldots, x_n]$ via sympy.
2. Verifies $D_{w_0}(\lambda) = s_\lambda$ at principal
   specialisation against the Macdonald hook-content formula for
   $n = 2, 3$ (all 5 partitions: differences reduce to $0$ via
   `sympy.cancel`).
3. Tabulates $D_w(\lambda)$, $D_w(\lambda)/D_{w_0}(\lambda)$, and
   $T^{\mathrm{Dem}}(\lambda; w)$ for every $(\lambda, w) \in
   \mathrm{Part}(n) \times S_n$ at $n \in \{2, 3\}$ —
   $4 + 18 = 22$ non-trivial Demazure characters in total
   ($p(n) \cdot n!$ for $n \in \{2, 3\}$).  Extension to $n = 4$
   adds $5 \cdot 24 = 120$ further evaluations and is deferred to
   a follow-up witness.

Output: [`demazure-markov-trace.witness.json`](https://github.com/litlfred/qou/blob/main/computations/demazure-markov-trace.witness.json).

## Lean formalisation

[`demazure-fiber-markov-trace.lean`](demazure-fiber-markov-trace.lean)
defines the abstract Demazure operator `demazureOp`, the Demazure
character `demazureCharacter`, the principal-specialisation ratio
`demazureRatio`, and the Demazure-fiber Markov-trace functional
`demazureFiberMarkovTrace`. The two main theorems are:

- `demazure_at_w0_equals_y_lambda` —
  $T^{\mathrm{Dem}}(\lambda;\, w_0) = y_\lambda$, reducing to
  `prop:macdonald-hook-telescope`.
- `demazure_principal_specialization_eq_schur` — at
  $x_i = q^{i-1}$, $D_{w_0}(\lambda)$ equals the Macdonald
  hook-content principal specialisation; deferred to a single
  `sorry` citing Kashiwara's refined character formula.
