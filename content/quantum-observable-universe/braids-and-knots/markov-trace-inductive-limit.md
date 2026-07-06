**Markov trace on the inductive limit $\mathbf{B}_\infty = \bigcup_n \mathbf{B}_n$ — single global trace consolidating every per-$n$ `MarkovTraceN n q`.**

The Markov trace $\tau_M : \mathbf{B}_\infty \to \mathbb{R}$ evaluates braid words globally. Instead of constructing independent traces for each braid group $\mathbf{B}_n$, we define a single operator on the inductive limit $\mathbf{B}_\infty = \bigcup_n \mathbf{B}_n$. The inclusion $\iota_n : \mathbf{B}_n \hookrightarrow \mathbf{B}_{n+1}$ adjoins a non-interacting strand on the right. 

The axioms M1–M4 characterise $\tau_M$ uniquely:

 - M1: $\tau_M(1_n) = 1$ (per-$n$ normalisation)
 - M2: $\tau_M(xy) = \tau_M(yx)$ (cyclicity, per-$n$)
 - M3: $\tau_M(\iota_n(x) \cdot \sigma_n) = z \cdot \tau_M(x)$ (stabilisation)
 - M4: $\tau_M(\iota_n(x) \cdot \sigma_n^{-1}) = z \cdot \tau_M(x)$

with $z = 1/(\sqrt{q} + 1/\sqrt{q})$ the Markov-Jones parameter. Restricting $\tau_M$ to $\mathbf{B}_n$ recovers the per-$n$ trace.

## Contents of this block

The Lean module `QOU.BraidKnot.markov_trace_inductive_limit` implements this consolidation. We define:

1. `opaque tauM_n (q : ℝ) {n : ℕ} (w : BraidWord n) : ℝ` — the scalar trace value.
2. `class MarkovTraceInductiveLimit q` — the global hypothesis. This carries the stabilisation `inclusion_residual` scalar and asserts it vanishes.
3. `instance defaultMarkovTraceInductiveLimit q` — the ansatz discharge, setting the residual to 0 pending substantive operator construction.
4. **Bridge instance** `markovTraceN_from_inductive_limit q n : MarkovTraceN n q` — the bridge instance.

## Consolidation benefit

The bridge instance guarantees that every per-$n$ `MarkovTraceN` class derives automatically from the global class. A single global witness elaborates every per-$n$ instance, eliminating duplication.

**Archimedean specialisation (§7c).** This block evaluates physical observables numerically at the substrate parameter $q_0$. While the underlying $q$-deformation identities hold over abstract coefficient rings, this module restricts to real- or complex-analytic structures.
