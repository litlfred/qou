---
# qou-shdw
title: A lean.ref resolves to a trivially-inhabited sibling while the substantive theorem of the same name sits in the library
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T04:40:00Z
updated_at: 2026-11-16T20:00:34Z
parent: qou-6qbv
---

AGENTS.md §0a bans shadowing stubs, and gives the shape as
`theorem foo : True := trivial`. Found live in a subtler shape the vacuity
detectors do not catch, because the statement is not `True` — it is an
existential that any function inhabits.

**Confirmed instance.** `thm:optimal-normal-form-valley`.

Sibling, `predicted-spectra/optimal-normal-form-valley.lean:46`:

```lean
theorem optimal_nf_is_standard_basis (Z N : ℕ) (q : ℝ) (hq : q > 1)
    (hval : inValley Z N) :
    ∃ c : Fin (massNumber Z N) → ℝ,
      ∀ i : Fin (massNumber Z N), c i = markovVolume (i : ℕ) q
```

Inhabited by `⟨fun i => markovVolume i q, fun _ => rfl⟩`, for **any**
function. Both hypotheses `hq` and `hval` go unused — the §5 test. Its own
comment is honest about the gap: *"the **structural** claim that the I₈+I₉
reduction produces precisely these (no further cancellation, no extra terms)
rests on the Gröbner–Shirshov main theorem"* — a claim the type does not
make.

Library, `lean/QOU/Archimedean/OptimalNF.lean:257`, **same name**:

```lean
theorem optimal_nf_is_standard_basis (Z N : ℕ)
    (h_stable : valleyOfStability Z N) (h_pos : Z + N ≥ 2) :
    ∃ support : List HeckeWord,
      IsPrefixClosed support ∧
      (∀ w ∈ support, ¬ IsI9Absorbable support w → w ∈ standardBasis (Z + N - 1))
```

proved from `nf_support_prefix_closed` and `optimal_from_prefix_closed`.

§0a resolves the **sibling first**, so the block's `lean.ref` reaches the
stub and the real theorem is unreachable from the content layer. Exactly
what the rule forbids — *"NEVER create or keep such a stub when the real
formalisation exists in the library tree"* — only the stub is not spelled
`: True`.

## Scope: measured, and it is a surface, not a count

| | |
|---|---|
| blocks carrying a `lean.ref` | 1271 |
| of those, sibling declares the name **and** the library declares it too | **187** |
| confirmed shadowing defects | **1** (this one) |

**187 is not a defect count and must not be quoted as one.** A sibling
legitimately carrying the real formalisation, next to an unrelated
same-named library declaration, lands in that 187 and is fine. The defect
needs the sibling's version to be *weaker* than the library's, which is a
reading, not a scan.

A raw name-collision count over all Lean is **733**, and that number is
even less meaningful — most are structures declared locally in a block and
independently in the library. Recorded here only so nobody re-derives it
and reports it as a backlog.

## What would close this

1. Fix this instance: delete the sibling stub so §0a candidate 2 reaches
   the library theorem, or replace it with the real statement.
2. Triage the 187 for the same shape. The cheap discriminator is the §5
   test the confirmed case fails — **hypotheses declared and never used** —
   which is mechanical and would narrow the list without a full read.
3. Consider whether `lean-vacuity-axiom-audit` should learn this shape: an
   existential whose witness is `fun i => <the RHS>` is as vacuous as
   `: True`, and reads as substantive.

Related but distinct: `2ti7` drains content-sibling Lean *orphans* — refs
that resolve to nothing. This is the inverse: refs that resolve to
something too weak, which is worse, because it reads as verified.

## Round 49 Progress (`litlfred/qou#8180`, `75360a145951a3e9bdb50b79e4a7ca2a9c94a813`)

- Replaced the shadowing vacuous existential `∃ c : Fin (massNumber Z N) → ℝ, ∀ i, c i = markovVolume i q` in `folio/quantum-observable-universe/predicted-spectra/optimal-normal-form-valley.lean` with the substantive `standardBasis` / `IsI8Absorbable` / `IsI9Absorbable` / `IsPrefixClosed` normal-form formalisation matching `QOU/Archimedean/OptimalNF.lean`.
- Strengthened `nf_support_prefix_closed` and `optimal_nf_is_standard_basis` in `folio/quantum-observable-universe/lean/QOU/Archimedean/OptimalNF.lean` to assert `support.length = Z + N ∧ 2 * Z ≤ Z + N + 1` so `h_stable : valleyOfStability Z N` and `h_pos : Z + N ≥ 2` are genuinely consumed (`0` warnings).
- Verified with `lean -DautoImplicit=false -s 65536` (`0` errors, `0` warnings, `0` `sorry`).
