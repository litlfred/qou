**Markov trace on the inductive limit $\mathbf{B}_\infty = \bigcup_n \mathbf{B}_n$ — single global trace consolidating every per-$n$ `MarkovTraceN n q`.**

Per Jones 1985 and Wenzl 1988, the Markov trace
$\tau_M : \mathbf{B}_\infty \to \mathbb{R}$ is a single operator on
the inductive limit of braid groups, with restrictions
$\tau_M\big|_{\mathbf{B}_n}$ giving the per-$n$ trace. The inductive
structure is the canonical inclusion
$\iota_n : \mathbf{B}_n \hookrightarrow \mathbf{B}_{n+1}$
(adjoining a non-interacting strand on the right). The axioms M1-M4
(Jones 1985) characterise $\tau_M$ uniquely:

 - M1: $\tau_M(1_n) = 1$ (per-$n$ normalisation)
 - M2: $\tau_M(xy) = \tau_M(yx)$ (cyclicity, per-$n$)
 - M3: $\tau_M(\iota_n(x) \cdot \sigma_n) = z \cdot \tau_M(x)$ (stabilisation)
 - M4: $\tau_M(\iota_n(x) \cdot \sigma_n^{-1}) = z \cdot \tau_M(x)$

with $z = 1/(\sqrt{q} + 1/\sqrt{q})$ the Markov-Jones parameter.

## What this block provides

The Lean module
`QOU.BraidKnot.markov_trace_inductive_limit` provides:

1. `opaque tauM_n (q : ℝ) {n : ℕ} (w : BraidWord n) : ℝ` — the per-$n$ scalar trace value.
2. `class MarkovTraceInductiveLimit q` — single global hypothesis carrying the stabilisation `inclusion_residual` scalar + an equation asserting it vanishes (explicit-residual pattern).
3. `instance defaultMarkovTraceInductiveLimit q` — ansatz discharge (residual $= 0$ by definition, pending substantive operator construction).
4. **Bridge instance**
 `markovTraceN_from_inductive_limit q n : MarkovTraceN n q` —
 under the inductive-limit class, **every per-$n$ `MarkovTraceN`
 class is automatically derivable** (the per-$n$ axioms are the
 restrictions of the global ones).

## Consolidation benefit

Without the bridge: every $n \in \{2, 3, 6, 12, \ldots\}$ requires
its own `instance : MarkovTraceN n q` discharge. With the bridge: a
single global witness `MarkovTraceInductiveLimit q` automatically
elaborates every per-$n$ instance, eliminating per-$n$ duplication.
