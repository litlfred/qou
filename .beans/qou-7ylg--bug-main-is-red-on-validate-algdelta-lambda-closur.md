---
# qou-7ylg
title: 'BUG: main is RED on validate — alg:delta-lambda-closure cites only a remark'
status: done
type: bug
priority: high
created_at: 2026-08-07T10:49:35Z
updated_at: 2026-08-21T22:06:16Z
---

Reproduced on origin/main (not a branch artifact): 12 issues, 2 of them ERRORS.

    bun run scripts/run-validate.ts content/quantum-observable-universe
    -> ✗ Invalid — 12 issue(s)

## The two errors

    ✗ [mba-sidecar-delta-lambda-closure] Import error: algorithm block
      "alg:delta-lambda-closure" must cite at least one provable
      (def:/prop:/thm:/lem:/cor:/conj:) in uses[] — algorithms are
      downstream of math.
    ✗ [mba-sidecar-mirror-cancellation] Unresolved uses: alg:delta-lambda-closure

The second is a pure cascade of the first: the closure block fails to import,
so anything using it has an unresolved ref.

## Cause — one line

content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-sidecar-delta-lambda-closure.ts:6

    uses: [
      "rem:term6-binding-density",     <-- a REMARK, not a provable
    ],

The builder rule (folio-assistant/schemas/builders.ts:162,
schemas/constraints.ts:601) requires an algorithm block to cite at least one
provable kind. A remark is not one, by design — remarks make no logical claims,
so an algorithm resting only on a remark has no math under it.

## Why it is live now

The rule is NOT new — it dates to folio-assistant 81329ba (2026-06-15), and the
offending block was last touched 2026-08-02 (a43bc9ed35, "wire(Δ_λ): emit
proved value witness + honest consumer + appendix sync", bean qou-l39s). So
this has been failing since at least that commit and was not caught, which fits
the known CI billing flakiness (AGENTS.md §CI billing failures) — validate has
not been reliably gating.

## The fix is small and the right citation exists

Δ_λ's per-partition VALUE is PROVED sorry-free as of 2026-08-02:
Δ_λ = (-1)^{n(λ)}·dim V_λ, the signed Springer dimension
(QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional, PR #4580), and it is
exactly what this algorithm block computes. So the honest repair is to add the
provable that the closure actually rests on to uses[], keeping the remark.

Do NOT satisfy the checker by citing an arbitrary nearby provable — the point
of the rule is that the cited provable is the math the algorithm implements.
Candidate to check first: prop:toroidal-harmonics-delta-lambda
(content/quantum-observable-universe/mass-theory/toroidal-harmonics-delta-lambda.ts),
but verify it is the right upstream before wiring; the Δ_λ value theorem's own
content block is the better target if one exists.

## Scope at the time of filing

Not fixed in the branch that found it. Found while rebasing claude/c1-theta-canonical-solutions
(qbeta/Stokes domain) onto main; the mass-binding appendix is a different
domain, so per AGENTS.md this does not ride that PR. Needs its own small PR.
My branch introduces ZERO validation regressions — same 12 issues on main and
on the branch, and my diff touches no .ts/.md content blocks at all.

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

x
