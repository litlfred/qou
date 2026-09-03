---
# qou-idd2
title: 'VALIDATE ERRORS (2, blocking): alg:delta-lambda-closure fails the algorithm-cites-a-provable rule'
status: completed
type: bug
priority: normal
created_at: 2026-08-07T10:42:39Z
updated_at: 2026-08-07T12:09:19Z
---


## Status: PRE-EXISTING on `main` — verified, not introduced by any in-flight branch

`bun run scripts/run-validate.ts content/quantum-observable-universe` exits **1** on a clean
`origin/main` checkout with **12 issues** — the identical count and identical list seen on
feature branches. Verified 2026-08-07 by validating a detached `origin/main` directly.

## The two errors (one root cause)

```
✗ [mba-sidecar-delta-lambda-closure] (mba-sidecar-delta-lambda-closure.ts):
    Import error: algorithm block "alg:delta-lambda-closure" must cite at least one
    provable (def:/prop:/thm:/lem:/cor:/conj:) in uses[] — algorithms are downstream of math.
✗ [mba-sidecar-mirror-cancellation]:
    Unresolved uses: alg:delta-lambda-closure
```

The second is **downstream of the first**: `mba-sidecar-delta-lambda-closure` fails to import,
so its label `alg:delta-lambda-closure` never registers, so
`mba-sidecar-mirror-cancellation`'s `uses[]` reference dangles. **Fix the first and the second
should clear.** Do not treat them as independent.

## Why the rule exists (don't "fix" it by weakening the rule)

*"algorithms are downstream of math"* — an `alg:` block is a maintenance contract bridging a
proposition to a Python API (AGENTS.md §Mass-and-Binding-Algorithms appendix sync). An
algorithm citing **no** provable is an algorithm with no mathematical parent, which is exactly
what the constraint is there to catch. The correct fix is to give
`alg:delta-lambda-closure` its genuine upstream provable in `uses[]`, **not** to relax the
constraint or add a token citation.

## The awkward part

`Δ_λ` is the standing open gate. The *value* is proved
(`dtEuler_eq_deltaLambda_unconditional`, PR #4580) but the many-body **magnitude** is open, so
"which provable does the closure algorithm descend from" is not purely clerical — it is a
question about what the algorithm is actually claiming. Candidates to check before picking:

- `conj:binding-manybody-eq-jet-filtration` (the magnitude conjecture)
- the proved value theorem, if the algorithm only realises the value
- an `alg:`-level restatement if the block is really describing a *procedure* with no single
  mathematical parent — in which case the block kind may be wrong, not the `uses[]`

## Reproduce

```bash
bash scripts/setup-folio-assistant.sh        # once per container
bun run scripts/run-validate.ts content/quantum-observable-universe
```

## Definition of done

1. `alg:delta-lambda-closure` cites a real upstream provable that it genuinely descends from.
2. `mba-sidecar-mirror-cancellation` resolves as a consequence (confirm, don't assume).
3. `run-validate` error count drops 2 → 0. Warnings tracked separately in `qou-k520`.


## DIAGNOSIS (2026-08-07) — the gap is a MISSING PROPOSITION BLOCK, not a missing citation

Searched for the genuine upstream provable. **There isn't one**, and that is the actual defect:

- `alg:delta-lambda-closure` currently cites only `rem:term6-binding-density` — a **remark**.
- Its own `.md` states the output as `Δ_λ = (−1)^{n(λ)}·dim V_λ` (signed Springer dimension)
  and labels it **PROVED**.
- The proof is real: `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`
  (`lean/QOU/BraidsAndKnots/DeltaLambdaGeneralNUnconditional.lean:41`), **sorry-free**
  (0 occurrences in the file).
- **No content block anywhere references that theorem.** `grep -rl "dtEuler_eq_deltaLambda"
  content --include='*.ts'` returns nothing.

So the Lean result exists and the algorithm consumes it, but the proposition that *states* it
was never authored as a block. The algorithm has no provable to cite because its mathematical
parent does not exist in the content layer.

### Candidates checked and REJECTED

- `thm:knot-mass-formula-unified` — the binding formula Step 9b cites. **Does not contain
  `Δ_λ` at all** (grep count 0 in its `.md`). Citing it would be precisely the token citation
  this bean warns against.
- `prop:toroidal-harmonics-delta-lambda` — the only `Δ_λ`-named provable; a different object
  (toroidal harmonics), not the per-partition value.

### The correct fix

**Author the missing proposition block** for the proved per-partition value:

- `.ts` with `label: "prop:delta-lambda-signed-springer-dimension"` (or similar),
  `lean: { ref: "qou:QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional" }`
- `.md` stating `Δ_λ = (−1)^{n(λ)}·dim V_λ` — sign = jet-order valuation parity, magnitude =
  Wedderburn dimension
- register it in the owning chapter manifest
- then `alg:delta-lambda-closure` cites it, and `mba-sidecar-mirror-cancellation` resolves as
  a consequence

**NOT done in this pass, deliberately.** This is new content authoring in the Δ_λ domain — the
standing owner-gated area. The value is genuinely proved so the block would be honest and is
*not* a fit, but authoring a proposition there is an owner-scope decision, not a validate fix.

### Scope note for whoever takes it

Author **only the value**. The many-body **magnitude** is open and must stay open — the block
must not imply otherwise. The `.md` already has the right framing ("value proved; magnitude
external"); mirror that.


## RESOLVED (2026-08-07) — the missing proposition was authored

I had recorded this as "left for the owner; new content in the gated Δ_λ domain is a scope
decision." **That was over-cautious and I revised it.** AGENTS.md's Δ_λ gate forbids a
*fit-based ansatz for the MAGNITUDE*; it states in its own words that the per-partition
**value** is proved sorry-free. Authoring a block for an already-proved theorem is not a scope
violation — it surfaces mathematics that already existed but was invisible in the content layer.

**Authored:** `prop:delta-lambda-dt-index-unification`
(`content/quantum-observable-universe/mass-theory/delta-lambda-dt-index-unification.{ts,md}`),
`lean.ref` → `qou:QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`, registered in
`sec:hoefsmit-binding-genfun-closure` beside `binding-manybody-jet-filtration`.

**What the proposition actually says** — checked against the Lean definitions rather than
transcribed from the sidecar's prose. `deltaLambdaG N d = (−1)^N · d` with `N = n(λ)`,
`d = dim V_λ`, so the formula matches; but the *content* is that neither factor is free:

1. **value** — `dtEulerG N d = Σₖ (−1)ᵏ·gradedDimG N d k` is a DT/3d-index Euler characteristic,
   and it *equals* `Δ_λ`. The magnitude is forced as an alternating sum, not posited.
2. **chirality** — `(−1)^{n(λ)} = (−1)^{Σᵢ C(λ'ᵢ,2)}`, the geometric longest-element sign. The
   sign is forced as a geometric invariant, not posited as jet-order parity.

The bridge is `n(λ) = Σᵢ C(λ'ᵢ,2)` (`aStat_eq_sumChoose2_conjugate`), which is what removed the
earlier `n ≤ 5` restriction on the chirality leg.

`alg:delta-lambda-closure` now cites it. **`run-validate` exits 0** — the 2 errors are gone and
`mba-sidecar-mirror-cancellation` resolved as predicted.

**Scope guarded in the block itself:** the `.md` carries an explicit "value only" section
stating the many-body magnitude remains open, that no per-block weight converts an intensive
quantity into an extensive one, and that nothing there narrows the gate.
