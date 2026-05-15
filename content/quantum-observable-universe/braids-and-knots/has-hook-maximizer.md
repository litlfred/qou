**Definition ($\mathrm{HasHookMaximizer}\,Z\,N$ hypothesis class —
§3b-cond conditional-class carrier).** *The class
$\mathrm{HasHookMaximizer}\,Z\,N$ axiomatises the hook-shape formula
for the $u$-pole maximizer of the Markov trace on canonical atomic
braids. Its single field is the assertion:*

$$
\arg\max_{\lambda \vdash 3A} \bigl|\mathrm{ord}_{u=0}\bigl(y_\lambda(q) \cdot \chi^\lambda_q(\beta(Z, N))\bigr)\bigr|
\;=\; \bigl\{\,(Z + 2N + 1,\; 1^{2Z + N - 1})\,\bigr\}
$$

*with the argmax being a singleton (uniqueness clause).*

### Why a class and not an axiom

The hook formula is **empirically verified** for the 5 atoms
$\{p, D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$ in the witness
[`per-irrep-pole-atom-crystal.witness.json`](../../folio-assistant/computations/per-irrep-pole-atom-crystal.witness.json),
but the **universal claim** (all $Z, N \geq 0$ with $Z + N \geq 1$)
is not yet substrate-derivable from the q-Hecke + canonical-knot
primitives currently in the repository. The class lets us:

1. State and use the formula as a categorical input in downstream
   propositions (per CLAUDE.md §3b-cond conditional-class pattern).
2. Track exactly where the hypothesis enters via explicit
   `[HasHookMaximizer Z N]` Lean instance arguments.
3. Discharge the assumption unconditionally — without rewriting the
   downstream chain — when (and only when) a substrate-level proof
   of the hook formula lands.

### Trivial model (empirical evidence)

The class is satisfied for $(Z, N) \in \{(1, 0), (1, 1), (1, 2), (2, 1), (2, 2)\}$
by direct empirical verification (witness above, 5/5 atoms). Higher
$(Z, N)$ require either a substrate-derivable proof or an extension
of the empirical bench.

The Lean class declaration is in
[`HasHookMaximizer.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/HasHookMaximizer.lean)
(the actual file in this PR is the sibling stub that re-exports the
canonical module).

### Discharge route

A future Lean proof of the universal hook formula would discharge
the class unconditionally via an instance:

```lean
instance : HasHookMaximizer Z N where
  hook_eq := by
    -- categorical derivation from Kashiwara crystal limit + SYT
    -- eigenline analysis + uniqueness
    sorry  -- Ref: [open work]
```

Until then, the discharge is via the trivial-model `sorry` in the
canonical class file with explicit `-- Ref:` citation to this
content block.