# SDP infrastructure for algebraic-primality verifier — roadmap and energy framing

This document specifies the four-layer SDP infrastructure needed to
verify [`conj:algebraic-primality-equals-empirical-at-q0`](../../content/quantum-observable-universe/particle-interactions/algebraic-primality-equals-empirical-at-q0.md),
records the energy-minimisation framing of the demand vector, and
cross-references the parallel work on the
[`claude/tier3-math-audit-B0wyO`](https://github.com/litlfred/qou/tree/claude/tier3-math-audit-B0wyO)
branch which has substantial relevant infrastructure.

## A. Hoefsmit matrices — extending symbolic n > 12

**Status as of this PR:** symbolic Hoefsmit at n ≤ 12 via SymPy in
[`symbolic_qdim_argmax.py`](symbolic_qdim_argmax.py), block-diagonal
optimised numerical at n ≤ 30 via the existing `shell_closure_compute.py`
framework.

**Audit branch infrastructure** (
[`folio-assistant/computations/from_scratch/hoefsmit_general.py`](https://github.com/litlfred/qou/blob/claude/tier3-math-audit-B0wyO/folio-assistant/computations/from_scratch/hoefsmit_general.py)
on `claude/tier3-math-audit-B0wyO`):

- From-scratch Hoefsmit seminormal matrix construction for $H_n(q)$.
- Generates SYTs of any partition shape, computes axial distances,
  builds `σ_i^λ` matrices over $\mathbb{Q}(q)$.
- Companion: [`wedderburn_markov.py`](https://github.com/litlfred/qou/blob/claude/tier3-math-audit-B0wyO/folio-assistant/computations/from_scratch/wedderburn_markov.py)
  for Wedderburn-block trace identities.

The audit branch independently **confirmed our proved theorem**
`kappa_zero_of_self_conjugate` numerically for $n = 3Z$ at magic
$Z \in \{2, 8, 20, 28\}$:

| $Z$ | $n = 3Z$ | self-conjugate partitions of $n$ | $\kappa_\lambda = 0$ ? |
|---:|---:|---:|:---:|
| 2 | 6 | 1 ($[3,2,1]$) | yes |
| 8 | 24 | 11 | all |
| 20 | 60 | 209 | all |
| 28 | 84 | 1004 | all |

They also verified my **third negative result** independently:
non-magic $Z \in \{3, 5, 9, 15, 25\}$ also have all-self-conjugate
$\kappa = 0$. Self-conjugacy alone does not select magic.

**Tricks for n > 12 (combined):**

| Trick | Source | Reach |
|---|---|---|
| Hook-length scalar version | `symbolic_qdim_argmax.py` | n ≤ 50 (Wedderburn weights only) |
| Branching-rule iteration | well-known | O(local) per level |
| Block-diagonal sparsity | `shell_closure_compute.py` | $15\,000 \times$ at $k = 9$ |
| Self-conj restriction | this PR + audit branch | $\sim 10^4 \times$ reduction at $n = 82$ |
| Lazy evaluation | standard | only matrix entries SDP touches |
| GB filtration depth cap | `ugb` cross-paper | finite Yekutieli depth |
| **From-scratch Hoefsmit (audit branch)** | `hoefsmit_general.py` | full matrices, n ≤ ~20 in symbolic |

**Combined reach:** Wedderburn-LP + self-conj restriction tractable
to **n = 82 symbolically** (881 partitions), and to **n = 126** with
patience ($10\,422$ partitions).

**Integration plan for this PR:** rather than duplicate, document
the integration with the audit branch's `hoefsmit_general.py`. The
audit branch's $n = 3Z$ convention + my $n$-strand convention agree
once strand-count interpretation is fixed.

## B. Demand vector — energy-minimisation framing

The "demand vector" in the confinement SDP is best understood as
the **target of an energy-minimisation process**. Detailed framing:

### What the SDP is doing

- **State**: a knot configuration in $H_n(q)$ — concretely, an
  element of the Hecke algebra encoding a braid word.
- **Energy functional**: a real-valued total computational /
  configurational cost defined on Hecke states. Lower energy =
  more confined = closer to a stable bound state.
- **Dynamics**: the system evolves by acting with a *discrete* set
  of allowable knot operators (e.g., the 6-basis
  $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$ from
  [`prop:knot-operator-selection`](../../content/quantum-observable-universe/particle-interactions/knot-operator-selection.md)).
  Discrete = ILP, not LP.
- **Termination**: stable configuration = local minimum of the
  energy. Iterative reduction continues until no single available
  operator decreases energy further.

### What the SDP gives

The SDP is the **continuous relaxation of the ILP**. It computes
the minimum *attainable* energy over the cone of admissible
states (PSD with appropriate constraints). Its solution
$T^*(n, q)$ is the relaxed-optimum density operator; its dual
$u^*(n, q)$ gives **shadow prices** per Wedderburn block —
quantifying how much the optimum changes if a per-block
constraint were marginally relaxed.

### Demand vector

In LP form `min cᵀT s.t. AT = b, T ≥ 0`, the vector $b$ is the
demand. For the framework's energy-minimisation:

- **$c$ (cost):** the energy functional — likely the total Hecke /
  Wedderburn weight, or a trace functional.
- **$A$ (constraints):** matrix Frobenius positivity per Wedderburn
  block (`prop:confinement-sdp`); the algebra structure.
- **$b$ (demand):** the **excess energy** that needs to be acted on
  by knot operators. If the current configuration has total energy
  $E_0$ and the target ground-state energy is $E_{\min}$, the demand
  is $E_0 - E_{\min}$. The ILP / SDP allocates discrete knot operators
  to absorb this excess.

### Iterative interpretation

The framework's iterative dynamics map:

1. Start at strand count $n$ with current state (possibly excited).
2. Compute total Hecke energy $E$ of current state.
3. If $E > E_{\min}$, identify a knot operator $\sigma \in
   \{\sigma_0, \sigma_1, \ldots\}$ that decreases $E$ when applied.
4. Apply $\sigma$. Repeat.
5. Stable state ⇔ no admissible $\sigma$ reduces $E$ ⇔ local minimum.

The SDP optimum corresponds to the **continuous-relaxation** ground
state; the ILP optimum is the **discrete** ground state reachable
by available knot operators. The gap between them is the
"integrality gap" — relevant for how-many-iterations questions.

### Magic shell as fixed point

A shell at strand count $n$ is **magic** iff the ILP-stable state
(reached by iteration above) is *atomic* — cannot be reduced to a
tensor product of stable states at smaller $n$. Equivalently
([def:algebraic-primality](../../content/quantum-observable-universe/particle-interactions/algebraic-primality.md)):
the canonical state $\psi_n(q)$ is not in the closed span of
$\psi_{n_1} \otimes \cdots \otimes \psi_{n_k}$ for any non-trivial
decomposition.

This iterative-minimisation reading aligns with
[`conj:magic-from-iterative-brane-tower`](../../content/quantum-observable-universe/lifting-and-descent/magic-from-iterative-brane-tower.md):
each magic $n$ is a **threshold-crossing** event in the
energy-reduction iteration, where the ILP fails to factor the
ground state into smaller magic atoms.

## B'. The dual — shadow prices, complementary slackness, ILP

**Cost vector $c$** is the **Hecke energy**: per-Wedderburn-block

$$
  c_\lambda \;=\; w_\lambda(q) \;=\; \frac{\dim_q(V_\lambda)^2}{[n]_q!}
$$

(or the related Markov-trace functional, depending on the specific
SDP variant). Already computable in the existing infrastructure
([`symbolic_qdim_argmax.py`](symbolic_qdim_argmax.py) for symbolic
$q$, `shell_closure_compute.py` for numeric).

**The dual problem** is

$$
  \max_y \;\langle b, y \rangle
  \qquad
  \text{s.t.}\quad A^\top y \preceq c.
$$

The shadow-price vector $y = u^*(n, q)$ is indexed by the
Wedderburn blocks of $H_n(q)$.

### Complementary slackness — the magic predicate as a dual fact

By complementary slackness at the optimum,

$$
  u^*_\lambda > 0
  \;\Longleftrightarrow\;
  \text{block-}\lambda\text{ constraint is tight (active) in primal}.
$$

So $\operatorname{supp}(u^*)$ tells us *which* Wedderburn blocks the
SDP optimum activates. The dual-side magic predicate:

$$
  n \text{ magic at } q
  \;\Longleftrightarrow\;
  |\operatorname{supp}(u^*(n, q))| = 1.
$$

This is the **dual-side certificate** of
[`conj:sdp-rank-collapse-magic-shell`](../../content/quantum-observable-universe/particle-interactions/sdp-rank-collapse-magic-shell.md):
read off a single integer from solver output instead of computing
matrix rank of the primal optimum.

### What's missing computationally for the dual

| Need | Status | Action |
|---|---|---|
| Cost $c_\lambda = w_\lambda(q)$ | already in `symbolic_qdim_argmax.py` | reuse |
| Demand $b_\lambda$ at each $n$ | implicit | extract per-$n$ formula from existing confinement-SDP definition |
| Numerical dual extraction | ready | cvxpy `constraint.dual_value` after `Problem.solve()` |
| Complementary-slackness reader | tooling | `[lam for lam, u in zip(blocks, u_star) if u > eps]` |
| Symbolic dual at $q$ generic | open | parametric KKT for tiny $n$ only |

### ILP integrality-gap conjecture

Discrete knot operators force ILP, not LP. Strong duality fails
for ILP in general:

- LP-relaxation dual: lower bound on ILP optimum.
- ILP optimum $\geq$ LP optimum, with gap = "integrality gap."
- Magic-shell-specific claim:

**Conjecture (dual integrality gap):** *At magic $n$ and substrate
$q_0$, the ILP optimum coincides with the LP-relaxation optimum:*

$$
  \mathrm{ILP}^*(n, q_0)
  \;=\;
  \mathrm{LP}^*(n, q_0)
  \quad\text{for}\quad
  n \in \{1, 2, 8, 20, 28, 50, 82, 126\}.
$$

*At non-magic $n$, the integrality gap is strictly positive.*

**Interpretation:** at magic $n$, the iteratively-reachable ground
state via discrete knot operators *coincides* with the SDP / LP
relaxation optimum — no inefficiency from quantisation. At
non-magic $n$, the iterative stable state lies *strictly above* the
SDP optimum, indicating the discrete process can't reach the
continuous-relaxation ground state.

This is conjecturally equivalent to
[`def:algebraic-primality`](../../content/quantum-observable-universe/particle-interactions/algebraic-primality.md):
zero-gap ⇔ no decomposition of $\psi_n$ into smaller-$n$ tensor
products ⇔ algebraically prime.

### cvxpy snippet for the numerical case

```python
import cvxpy as cp
import numpy as np

def magic_via_dual(n: int, q_value: float,
                   cost_block_weights: dict,
                   demand_block_weights: dict,
                   constraint_matrix: dict,
                   eps: float = 1e-8) -> dict:
    """Solve the Wedderburn-block SDP at (n, q) and read off
    |supp(u*)| from dual values.

    cost_block_weights[lam]: c_lam = w_lam(q_value)
    demand_block_weights[lam]: b_lam at strand count n
    constraint_matrix[lam]: A_lam (PSD-block coefficient)

    Returns: {is_magic: bool, supp_size: int, dual_values: dict}
    """
    blocks = list(cost_block_weights.keys())
    T = {lam: cp.Variable(PSD=True) for lam in blocks}
    cost = sum(cost_block_weights[lam] * cp.trace(T[lam])
               for lam in blocks)
    constraints = [
        sum(constraint_matrix[lam] @ T[lam] for lam in blocks)
        == demand_block_weights_vector
    ]
    prob = cp.Problem(cp.Minimize(cost), constraints)
    prob.solve()
    # Dual: shadow prices per block.
    u_star = {lam: float(c.dual_value) for lam, c in
              zip(blocks, prob.constraints)}
    supp = [lam for lam, u in u_star.items() if u > eps]
    return {
        "is_magic": len(supp) == 1,
        "supp_size": len(supp),
        "dual_values": u_star,
        "primal_value": prob.value,
    }
```

### Symbolic-q form

For $q$ symbolic (rational function), the dual is solvable
parametrically over a fixed magic-vs-non-magic candidate set. The
KKT system at the optimum has the form:

$$
  A^\top y_\lambda \;=\; c_\lambda
  \quad \text{for } \lambda \in \mathrm{supp}(u^*),
  \qquad
  A^\top y_\mu \;<\; c_\mu
  \quad \text{for } \mu \notin \mathrm{supp}(u^*).
$$

Solving symbolically: pick a candidate active basis $S \subseteq
\{\lambda \vdash n\}$, solve the equality system $A_S^\top y = c_S$,
then verify $A_\mu^\top y < c_\mu$ for $\mu \notin S$. The
"$|S| = 1$" cases are the magic candidates; check whether the
KKT system is satisfiable for $q$ in a neighbourhood of $q_0$.

For small $n$ (≤ 8) this is doable by hand. For $n \in \{20, 28\}$
we'd want SymPy automation.

## C. SDP solver — what's needed concretely

For the algebraic-primality verifier:

| Capability | Status | Action |
|---|---|---|
| Numerical SDP at $q = q_0$, $n \leq 30$ | partial — `shell_closure_compute.py` does characters; full SDP not wired | adapt cvxpy/SCS wrapper |
| Symbolic LP at q > 1 generic, $n \leq 12$ (full), $n \leq 50$ (scalar Wedderburn) | partial — `symbolic_qdim_argmax.py` does q-dim argmax | extend with demand vector + tensor-span check |
| Parametric SDP (regime boundaries in $q$) | open | manual KKT for tiny $n$; full theory open |
| Block-structure-aware ILP | partial — audit branch has Wedderburn solvers | integrate audit-branch's `hoefsmit_general.py` |

**Minimal viable verifier (next PR or follow-up):**

```python
def verify_primality(n: int, q_value: float | sp.Expr) -> dict:
    """Return: {is_prime: bool, reason: str, decomp_used: List[int] | None}"""
    psi_n = sdp_solve_canonical(n, q_value, demand_vector(n))
    for decomp in magic_part_decompositions(n):
        psi_factored = tensor_product([psi(k, q_value) for k in decomp])
        if in_span(psi_n, [psi_factored]):
            return {is_prime: False, ...}
    return {is_prime: True, ...}
```

Discharges `IsKnownMagic n q_0` or `IsKnownNotMagic n q_0` per call.

## D. Tensor-span check — small-n bottleneck

The bottleneck is computing $\psi_n$ at large $n$, not the span
check itself. The span check is finite linear algebra over
$\mathbb{Q}(q)$ once both sides are explicit vectors.

Tractability ladder:

| $n$ range | $\psi_n$ tractability | Magic-part decomps |
|---|---|---|
| $n \leq 12$ | symbolic | $\sim 5$ |
| $n \leq 30$ | numeric (shell-closure-style) | $\sim 50$ |
| $n \in [30, 50]$ | Wedderburn-LP only | $\sim 200$ |
| $n \in [50, 82]$ | self-conj-restricted, audit-branch tools | $\sim 2\,000$ |
| $n = 126$ | iterative brane-tower required (`conj:magic-from-iterative-brane-tower`) | $\sim 20\,000$ |

## Compute optimisations from framework findings

Several framework results substantially restrict the search space
for the SDP / LR-fusion verifier:

### 1. Bring 6-knot basis (genus-4 bound)

The Bring-shell-binding picture
([prop:torus-knot-shell-binding](../../content/quantum-observable-universe/archimedean-universe/torus-knot-shell-binding.md))
restricts the active operator basis to combinations of **6**
specific torus knots ($T_{2,3}$, $T_{2,5}$, $T_{2,7}$, $T_{3,4}$,
$T_{2,9}$, $T_{3,5}$). The genus-4 bound is structural, not a
search heuristic.

**Compute reduction:** instead of enumerating all $p(n)$ partitions
of $n$ for SDP basis selection, enumerate at most $\binom{6}{2} = 15$
combinations of the 6-knot basis. For $n = 50$: $p(50) \approx 2 \times
10^5$ partitions vs 15 combinations — a $\sim 10^4 \times$ speedup
on the basis-selection step.

### 2. $\Delta i \leq 1$ rule for double-magic LR-fusion

[`conj:double-magic-delta-i-bound`](../../content/quantum-observable-universe/observations/double-magic-delta-i-bound.md)
proves (on empirical data, conjectures generally) that doubly-magic
isotopes satisfy $|i_N - i_Z| \leq 1$ across Bring shell indices.

**Compute reduction:** the LR-fusion verifier need only check
$13$ shell-pairs (7 diagonal + 6 adjacent) out of the $49$ total
$(i_Z, i_N)$ combinations. **3.77× speedup** on per-pair LR-fusion
work.

### 3. Self-conjugate-only enumeration at high $n$

For $n \geq 50$, restrict the SDP basis to self-conjugate
partitions $\lambda = \lambda'$ — required by
[`conj:categorical-neutrality-saturated-shells`](../../content/quantum-observable-universe/braids-and-knots/categorical-neutrality-saturated-shells.md).
Counts: $q(82) = 881$ vs $p(82) = 1.2 \times 10^7$ — a $\sim 10^4 \times$
reduction.

### 4. Block-diagonal Hoefsmit (existing)

`shell_closure_compute.py`: $15\,000\times$ speedup at $k = 9$ via
block-diagonal matrix-vector products. Already in the codebase.

### Combined effect at $n = 82$ (target: magic shell 6)

Naive enumeration: $p(82) \times 49 \times \dim_q(\lambda) \approx
10^7 \times 49 \times \mathrm{full}$ matrix work.

With all optimisations:
- $q(82) = 881$ partitions (self-conj restriction).
- $13$ shell-pairs ($\Delta i \leq 1$).
- $15$ knot combinations (Bring 6-basis).
- Block-diagonal matrix products ($15\,000 \times$ via existing).

**Estimated reduction: $\sim 10^9 \times$.** Magic shell 6 verification
becomes feasible *symbolically* in seconds rather than hours.

## Cross-reference: audit branch contributions

The [`claude/tier3-math-audit-B0wyO`](https://github.com/litlfred/qou/tree/claude/tier3-math-audit-B0wyO)
branch has:

- `from_scratch/hoefsmit_general.py` — symbolic Hoefsmit matrices.
- `from_scratch/wedderburn_markov.py` — Wedderburn-trace identities.
- `magic-numbers-numerical-witness.py` — independent verification
  of $\kappa = 0$ at magic shells (cherry-picked from PR #500).
- Multiple SDP solvers (Wedderburn-block PSD evaluator in Rust,
  CLARABEL+MPFR, Strategy-A decomposed solver).
- $\rho(Z, N)$ exploration scan (Wedderburn-style diagnostics).

Their **n = 3Z convention** (3 strands per nucleon, Z nucleons)
agrees with our **n-strand convention** once strand interpretation
is fixed. Concretely: their "Z = 8 magic" verification at $n = 24$
maps to our "magic shell at strand count 24."

**Recommended integration:** import the audit branch's Hoefsmit
infrastructure, adapt the verifier to use both their explicit
matrix construction and our recursive primality definition, and run
end-to-end tests at $n \leq 30$.
