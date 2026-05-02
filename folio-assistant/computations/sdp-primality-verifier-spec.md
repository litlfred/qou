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
| 2 | 6 | 1 ($[3,2,1]$) | ✓ |
| 8 | 24 | 11 | ✓ all |
| 20 | 60 | 209 | ✓ all |
| 28 | 84 | 1004 | ✓ all |

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
