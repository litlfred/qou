# Self-assuming-projection disposition rubric — restate→rfl / queued / conjecture

**Date:** 2026-06-18
**Branch:** `claude/vacuity-disposition-policy-2026-06-18`
**Context:** the 199 `proof-no-self-assuming-projection` defects triaged in
[`2026-06-18-self-assuming-projection-triage.md`](2026-06-18-self-assuming-projection-triage.md) (#2468).
**Campaign tracker:** [#2472](https://github.com/litlfred/qou/issues/2472).

Owner direction (2026-06-18): **don't mass-demote to `conjecture`** — most of
these are clearly-true *formalization targets*, not claims we doubt. A
`conjecture` is "when we are unsure". Mechanism chosen: **mark-only** (default)
+ **restate→`rfl`** where the claim is definitional.

## What these stubs actually are (and the soundness pitfall)

`theorem foo [ctx : Ctx] : P := ctx.claim_foo` (with `Ctx.claim_foo : P`) is a
**valid conditional proof** — `P` holds for *every* instance, because the class
provides `claim_foo : P`. It reads as "proved" only because the conditionality
is degenerate: the class assumes its own conclusion, since the real content (the
*construction* that would establish `P`) is abstracted away.

> **⚠ Soundness pitfall — do NOT strip the field + `sorry`.** The tempting
> "fix" — delete `claim_foo` and write `:= by sorry` — makes the remaining
> fields independent, so `∀ ctx, P` is **false** (a counter-instance exists) and
> the `sorry` proves an *undischargeable falsehood*, strictly worse than the
> original. `lean`-direct exits 0 regardless (`sorry` accepts any goal — exit 0
> ≠ truth). The projection is a *valid* proof; keep it.

## Three dispositions (decide per block)

| disposition | when | what | status |
|---|---|---|---|
| **restate→`rfl`** | the claim is **definitional** — `X` is introduced *by* this identity (`χ = 1−h²`) | replace the free field `X` + `claim` with a *defined* `X := <formula>`; theorem becomes `rfl` | genuinely **proved** |
| **queued** (mark-only) | a **clearly-true target**, content (construction) not yet formalized | **keep** `:= ctx.claim_foo` (valid conditional proof) + a `-- QUEUED-FOR-LEAN:` body comment; scanner recategorises defect→queued | proved-conditionally; audit: **queued** |
| **conjecture** | truth is **genuinely in doubt** (empirical near-match, open derivation) | demote kind `theorem → conjecture` + `.md` banner | (claim-change → **owner sign-off**) |

### Decision test

1. Is the claim **definitional** (the LHS exists only via this identity)? →
   **restate→`rfl`** (best — a real proof). Consider kind `definition`.
2. Else, are we **confident `P` is true** (manuscript asserts it; a formalization
   TODO)? → **queued** (mark-only).
3. Else (**genuine doubt**) → **conjecture** (sign-off).

## The "queued" label — `-- QUEUED-FOR-LEAN:` marker + scanner recategorisation

The label is a one-line body comment on the kept projection:

```lean
-- Ref: [manuscript] <path>
theorem foo [ctx : FooContext] : P :=
  -- QUEUED-FOR-LEAN: clearly-true target; `ctx.claim_foo` is the placeholder
  -- conditional proof, pending formalisation of <construction> that establishes it.
  ctx.claim_foo
```

The scanner ([`lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts))
detects `QUEUED-FOR-LEAN` in a decl's original (comment-bearing) lines and
recategorises a marked self-projection from defect → **exempt** with
`exempt_reason: "queued-for-lean (owner-marked formalization target)"`. No `.lean`
proof change (the projection stays a valid conditional proof — sound), no schema
change, and the marker is greppable (`rg QUEUED-FOR-LEAN`). This is **mark-only**:
the chosen mechanism over keep-field+`sorry` (which would force a *cosmetic*
`sorry` — the proof is trivially the field).

## Worked exemplar — `binding_assembly` (verified)

[`binding_assembly.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/SixTermPerDerivationWeights/binding_assembly.lean):
the projection `:= ctx.claim_six_term_recovery` is **kept** (it is a valid
conditional proof of `atomic_mass = Σ term_weights`), a `-- QUEUED-FOR-LEAN:`
marker added, and the missing `import Mathlib.Data.Fintype.Basic` supplied (the
file did not compile standalone — `Fintype (Fin 6)`).

Verified `lean`-direct **exit 0, no `sorry` warning** (a real conditional proof);
the scanner recategorises it **defect → queued** (`self-assuming-projection`
199 → 198, +1 queued).

> **Standalone-compile caveat.** Many content-block sibling `.lean` files do not
> compile standalone (imports available only through the full `lake build`) — the
> gap #2306 noted for `beta-decay-skein`. Verify with `lean`-direct (restore the
> `lake-cache/qou-v4-24-0` oleans, ~2 min; per-file ~1s) — **not** `lake build`
> (elan can't reach the release server in the sandbox). Add the missing imports
> when marking, so the queued stub genuinely compiles.

## Criterion reconsideration

The scanner now has a third outcome for a self-projection: **defect** (unmarked),
**queued** (`-- QUEUED-FOR-LEAN:` marked → exempt), or — already — the
iff-from-directions precision exemption. The fix-guidance docstring lists the
three dispositions. The registry description in #2306 (`qa-criteria-registry.ts`)
should align when that lands.

## Campaign

Per-block over the #2472 batches: **restate→`rfl`** where definitional, **mark
queued** for clearly-true targets (mechanical, no proof change), **conjecture**
(owner sign-off) for the genuinely-uncertain (empirical/open) ones. Verify each
edit `lean`-direct.
