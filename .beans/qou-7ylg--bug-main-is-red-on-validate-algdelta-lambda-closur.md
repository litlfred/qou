
## FIXED 2026-08-07 — validate is green again

`uses[]` on `alg:delta-lambda-closure` now also cites
**`prop:wedderburn-trace-identity`**. Both errors clear (the second was a pure
cascade), and the paper goes from `✗ Invalid — 12` to `✓ Valid — 10`; the
remaining 10 are pre-existing warnings, not errors.

**Why that citation and not another.** `Δ_λ = (−1)^{n(λ)}·dim V_λ`. The
magnitude leg `dim V_λ` is the Wedderburn block dimension `d_λ = f^λ`, and
`prop:wedderburn-trace-identity` is what establishes those blocks
(`Σ_λ d_λ·y_λ(q) = 1` partitions the Markov weight among them). So the
algorithm genuinely is downstream of it — which is what the rule is for.

**Rejected candidate, recorded so nobody re-tries it.**
`prop:toroidal-harmonics-delta-lambda` matches on name and is in
`mass-theory/`, so it is the obvious thing to grab. It is **wrong**: it states
a toroidal-harmonic change of variables for the `z`-recursion
(`QOU.QBeta.toroidal_ode_to_markov_w`), which has nothing to do with the
per-partition value. Citing it would have satisfied the checker while making
the manifest assert something false — exactly the failure the rule exists to
prevent.

## Follow-up left open — the proved theorem has no content block

The theorem the algorithm actually implements is
`Δ_λ = (−1)^{n(λ)}·dim V_λ`, sorry-free and general-`n`:
`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional` in
`lean/QOU/BraidsAndKnots/DeltaLambdaGeneralNUnconditional.lean` (PR #4580).

**It has no `.ts`/`.md` face.** Corpus-wide it is referenced from exactly two
places, both algorithm `.md` prose:
`mba-sidecar-delta-lambda-closure.md` and `mba-step09b-per-isotope-binding.md`.

So a sorry-free general-`n` result is carrying weight in the mass-binding chain
while being invisible to the manifest graph — nothing `uses[]` it, no
dependency edge reaches it. Giving it a `proposition` block (with
`lean.ref: "qou:QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional"`) is
the proper fix, and then this algorithm should cite *that* instead. Not done
here: authoring the statement belongs with whoever owns the Δ_λ derivation, and
getting its scope subtly wrong would be worse than the citation above.
