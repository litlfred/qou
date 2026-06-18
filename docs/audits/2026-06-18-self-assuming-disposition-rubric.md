# Self-assuming-projection disposition rubric — restate / queued / conjecture

**Date:** 2026-06-18
**Branch:** `claude/vacuity-disposition-policy-2026-06-18`
**Context:** the 199 `proof-no-self-assuming-projection` defects triaged in
[`2026-06-18-self-assuming-projection-triage.md`](2026-06-18-self-assuming-projection-triage.md) (#2468).
**Campaign tracker:** [#2472](https://github.com/litlfred/qou/issues/2472).

This fixes the drain *policy*. The triage assumed "restate-to-derive (preferred)",
but on inspection the 199 are predominantly conditional-class stubs that carry an
**empirical / computational / explicitly-open** claim as a class field — for which
a cheap restate just shuffles the assumption. Mass-demoting them all to
`conjecture` is **wrong**: most are *clearly-true formalization targets*, not
claims we doubt. Per owner direction (2026-06-18):

> *"We need a label for proof in progress / queued for Lean where it is clearly
> going to be there. `conjecture` is when we are unsure."*

## The defect

```lean
theorem foo [ctx : FooContext] : P := ctx.claim_foo   -- FooContext.claim_foo : P
```

The class carries the *conclusion* `P` verbatim and the theorem projects it
(§3b-cond item 5). It compiles, is axiom-clean, and **reads as `proved`** — but it
is vacuous: it assumes what it claims. This is *worse* than an honest `sorry`,
which at least reports `has_sorry`.

## Three honest dispositions (decide per block)

| disposition | when | what | kind | derived status |
|---|---|---|---|---|
| **restate-to-derive** | a *genuine upstream input* exists from which `P` follows by real content (e.g. an `↔` from its two directions — `q_bkm_criterion`) | class carries the *hypotheses*; theorem **derives** `P` (`Iff.intro`, `And.intro` of proved parts) | `theorem` | `proved` |
| **queued-for-Lean** | `P` is a **clearly-true target**, not yet formalized | strip the conclusion-field; body `:= by sorry`; `-- Ref:` + `-- QUEUED-FOR-LEAN:`; fix imports so it compiles | `theorem` | **`has_sorry`** |
| **conjecture** | we are **genuinely unsure** `P` is true (empirical near-match, open whether it holds) | demote kind; `.md` conditional banner | `conjecture` | (n/a) |

### Decision test

1. **Is there a genuine upstream input** the class could carry as a *hypothesis*
   (weaker than `P`) from which `P` follows by real derivation? → **restate**. (Rare;
   the `↔`-from-directions pattern is the clean case.)
2. Else, **are we confident `P` is true** (the manuscript asserts it; it is a
   formalization TODO)? → **queued-for-Lean**.
3. Else (**genuine doubt** about `P`'s truth) → **conjecture**.

Restate is *preferred* where honest, but it is rare. Most of the 199 are
**queued-for-Lean** (clearly-true targets); a minority are **conjecture**
(empirical/open). Demotion is a claim-change → **owner sign-off**.

## The "queued-for-Lean" label — no schema change

The label the owner asks for **already exists** as the derived formalization status
**`has_sorry`** (CLAUDE.md §4 — status is derived from `.lean`, never stored). A
self-assuming projection bypasses it by reading as `proved`; converting to an honest
`sorry` restores the truthful `has_sorry` = *stated, queued for Lean, not yet
proved*. The block stays a `theorem` (we still assert `P`), distinct from
`conjecture` (we doubt `P`).

Convention for the queued form:

```lean
theorem foo [ctx : FooContext] : P := by
  -- Ref: [manuscript] <path>
  -- QUEUED-FOR-LEAN: clearly-true target; <one line on what the real proof needs>
  sorry
```

The `-- QUEUED-FOR-LEAN:` marker makes the intent greppable (`rg "QUEUED-FOR-LEAN"`)
without a schema field; a future `authorNotes: [{kind:"status"}]` could surface it in
render, but is not required.

## Worked exemplar — `binding_assembly` (verified)

[`binding_assembly.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/SixTermPerDerivationWeights/binding_assembly.lean)
— the file's own docstring already says it *should* be `:= by sorry`, but it was
coded as a self-projection. The clean queued conversion:

- **before:** class field `claim_six_term_recovery : atomic_mass = Σ term_weights`;
  body `:= ctx.claim_six_term_recovery`. (self-assuming; reads `proved`.)
- **after:** field removed; body `:= by sorry` + `-- QUEUED-FOR-LEAN:`; added the
  missing `import Mathlib.Data.Fintype.Basic` (the file did not compile standalone —
  `Fintype (Fin 6)`).

Verified `lean`-direct **exit 0** (only `declaration uses 'sorry'`); the vacuity
scanner drops it from `proof-no-self-assuming-projection` (199 → 198). This is the
template for the queued-disposition batches.

> **Standalone-compile caveat.** Many content-block sibling `.lean` files do not
> compile standalone (missing tactic/instance imports available only through the
> full `lake build`) — the same gap #2306 noted for `beta-decay-skein`. A genuine
> queued stub must compile, so each conversion may carry a small import fix.
> Verify with `lean`-direct (the `lake-cache/qou-v4-24-0` oleans restore in ~2 min;
> per-file check ~1s) — **not** `lake build` (elan can't reach the release server in
> the sandbox).

## Criterion reconsideration — no scanner logic change

The scanner **already** accepts an honest `sorry -- Ref:` (it flags only the
self-projection / trivial-`True` patterns), so the three dispositions all clear the
defect. The only change is to the criterion's **fix-guidance** (this PR updates the
`proof-no-self-assuming-projection` docstring in
[`lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts)
to list restate / queued / conjecture). The registry description in #2306
(`qa-criteria-registry.ts`) should align when that PR lands.

## Campaign

Per-block over the #2472 batches, with owner sign-off (demotions are claim-changes).
Expected mix: mostly **queued-for-Lean**, a minority **conjecture**, rare **restate**.
