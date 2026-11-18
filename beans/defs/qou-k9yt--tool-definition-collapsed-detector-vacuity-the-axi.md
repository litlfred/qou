---
# qou-k9yt
title: 'TOOL: definition-collapsed detector — vacuity the axiom audit cannot see'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T11:43:54Z
updated_at: 2026-10-04T15:25:07Z
parent: qou-5vkl
---


## What it is

[`scripts/lean-definition-collapsed-audit.py`](../scripts/lean-definition-collapsed-audit.py)
detects theorems made true by a *local definition* rather than by an argument —
the shape found in bean `qou-sk6h`, where six theorems documented as
"**Open input** … body is `sorry`" contained no `sorry` and asserted nothing.

Two independent signals per theorem:

- **A. COLLAPSED** — proof is `rfl` / `by rfl` / `intro; rfl`, or a one-to-three
  line `simp`/`unfold` whose arguments include a plain `def` (not `opaque`, not
  `axiom`) declared in the *same file*.
- **B. OPEN-CLAIM** — the docstring says the statement is unproved or hard:
  "open input", "open analytic", "body is `sorry`", "not in Mathlib",
  "conjecture", …

`A ∧ B` ⇒ **CRITICAL**: the prose says open, the proof says definitional.
`A` alone ⇒ advisory (many definitional restatements are legitimate and say so).

**Exclusion:** if the proof discharges the goal via a *hypothesis field* of an
instance/structure binder (`C.ruleLinear`, `h.foo`), it is a genuine conditional
derivation and is skipped. This removed the one false positive found in testing,
`BraneTowerLevelAmplitude.fullCoordAmplitude_eq` — whose docstring correctly
*disclaims* ("not a proof of the rule; the rule `ruleLinear` is the open input"),
and whose disclaimer was tripping signal B.

## Why it is needed

A vacuous proof carries no `sorry`, no `axiom`, no `native_decide`, so
`#print axioms` reads perfectly clean and no existing checker fires. Measured on
the LiftingDescent lemmas before/after repair:

    before  [propext, Classical.choice, Quot.sound]            <- reads as proved
    after   [propext, sorryAx, Classical.choice, Quot.sound]   <- honestly open

Same structural blind spot AGENTS.md §3b-tax records for empty Prop carriers.

## First run — it immediately found a new instance

6 CRITICAL corpus-wide. Five were the already-known LiftingDescent group
(fixed in PR #4741). The sixth was new:

`QOU/TopologicalMass/cat_transient_localises_blowup.lean` — and it is *more*
degenerate than the LiftingDescent group:

```lean
def N : ℕ := 0
def alpha : ℝ := 0
def tauHat : ℝ → ℝ := fun x => x     -- the IDENTITY ⇒ α − τ̂(α) ≡ 0
def trFrob : ℝ →+ ℝ := 0             -- the ZERO homomorphism ⇒ every trace is 0
def localComponent (i : ℕ) : ℝ := 0
```

so `transient_decomposition` ("Open geometric input … not in Mathlib; body is
`sorry`") was `0 = 0`, and the headline `cat_transient_localises_blowup` derived
`0 = 0` from it. Repaired the same way: primitives made `opaque`, the open input
stated with `sorry` + its citation; the headline theorem keeps its real proof
(`rw` + `map_sum`) and is now a genuine derivation. Verified exit 0.

## Caveat / future work

The advisory tier (~1259) is too noisy to action directly — that is signal A
alone and is expected to be mostly legitimate. Only the `A ∧ B` tier is
actionable today. Sharpening advisory would need either a Lean-side check
(does the statement still hold with the defs made opaque?) or a docstring-vs-
proof-term comparison. The `A ∧ B` tier is the high-precision part and is what
should go into CI.


---

## 2026-08-27 — the Lean-side sharpening this bean asked for now exists

Recorded by the `qou-0avp` session, which built a second text-detector without
finding this bean first (a corpus-grep failure; `grep -rl definition-collapsed
.beans/` would have caught it). Follow-up to merge the shared machinery:
`qou-rfq9`.

**The two detectors turn out to be near-disjoint, measured:**

    qou-0avp's 19 CRITICAL flagged by THIS tool at any tier :  0 of 19
    qou-0avp's 115 major   flagged by THIS tool at any tier : 21 of 115  (18%)
    THIS tool's 1 CRITICAL flagged by qou-0avp at any tier  :  0 of 1

This tool keys on docstring-says-OPEN + proof-is-definitional; the other keys on
a name invoking a MATHEMATICIAN + local-only defs + cheap proof. Different
populations. The duplicated part is the generic machinery (COLLAPSED signal,
binder-field exclusion, docstring extraction) — that is what `qou-rfq9` proposes
to share, keeping both front-ends.

**§"Caveat / future work" above asks for "a Lean-side check (does the statement
still hold with the defs made opaque?)". It is built:**
`scripts/lean/BorrowedNameKernel.lean` runs `Meta.isDefEq` under
`forallTelescopeReducing` on each theorem's statement, driven by
`scripts/lean/audit-driver.sh` (batch at 8 modules; more times out).
42 modules / 615 theorems / 102 collapses so far —
`docs/audits/2026-08-26-kernel-defeq-sample.witness.json`.
`scripts/lean/compile-cone.sh` reaches modules with no olean without letting
`lake build` evict the restored cache.

**It independently reproduced this tool's single surviving CRITICAL,
`qInt_eq_canonical` — and that one is a FALSE POSITIVE for both of us.** Its
docstring reads: *"`qInt` is kept rather than aliased … The two are
definitionally the same object, so the consolidation here is this equation —
checked, not asserted."* A compatibility lemma between two definitions SHOULD be
`rfl`. So `defeq_collapse` is a candidate signal, never a verdict — the same
position this bean takes on signal A.

Still `todo`: the CRITICAL count here is 1 (down from 6) because #4741 drained
the LiftingDescent group, so the `--strict` gate is cheap to turn on. Whether it
belongs in the (dispatch-only) CI is part of `qou-rfq9`.
