---
# qou-1nv0
title: 'Watcher queues drained: 3 stale items, and the pair-gen .md published a vacuous carrier'
status: completed
type: task
priority: normal
created_at: 2026-08-30T07:57:44Z
updated_at: 2026-08-30T07:59:10Z
---

## Done — PR #6133, branch claude/watcher-queue-stale-and-md-vacuous-carrier-2026-08-30

Idle-backlog pass on the four integration-watcher queues (AGENTS.md §5 priority 3).
Open items across all four: **3 → 0**.

### All three open items were stale

Recorded against `source_sha 565be78e866d`; all three fixed since, verified on `main`
`b7ebf991c0f`. `casimir-first-q-correction` (ref is now `FirstInteractingCasimirCorrection`,
resolves), `lqg-entropy-qdim-partition-pole` (has both a ref and a sibling `.lean`, contrary
to the entry), `conj-rho-k-pair-gen-canonical-form` (ref is now `PairGenCanonical`, resolves).
Marked resolved with the evidence inline rather than deleted.

### The live defect the queue does not name

`conj-rho-k-pair-gen-canonical-form.md` still published the **superseded** carrier —
`pair_gen_functional := sorry` plus a field `∀ M ≥ 0, ∃ M_rec, |M_rec − M| ≤ M/100`, which is
**trivially inhabited** (take `M_rec := M`). Proved, not argued:
`instance : MdPublishedVersion := ⟨fun M hM => ⟨M, by simpa using by linarith⟩⟩` compiles.

The sibling `.lean` had already been fixed to a content-bearing field and its docstring says
so explicitly; only the `.md` was unsynced. **The vacuity audit cannot catch this class: it
scans `.lean`, and the defect was in the `.md`.**

### CROSS-REFERENCE — this widens live bean `qou-ffwk`

`qou-ffwk` ("10 conjecture carriers use a trivially-inhabited 'residual = 0' placeholder",
status `todo`) is the same defect class and does **not** cover this instance (grep: 0 mentions).
Two reasons, both of which extend its scope:

1. **Different schema.** `qou-ffwk` keys on `residual : ℝ; residual_eq_zero : residual = 0`,
   inhabited by `⟨0, rfl⟩`. This one is `∀ M ≥ 0, ∃ M_rec, |M_rec − M| ≤ M/100`, inhabited by
   the identity witness. A scan for the first spelling cannot see the second — the same
   detector-blindness pattern AGENTS.md catalogues for convention-C.
2. **Different surface.** `qou-ffwk` is about the `.lean` library. This one was in the `.md`,
   where the `.lean` had *already been fixed*. So the count of live vacuous carriers a reader
   can encounter is not bounded by the count in the Lean tree.

Recorded on `qou-ffwk` as well.

### The note I added was itself a §4d violation

The `> **Note on this block.**` blockquote I first used to explain the change flipped
`voice-editorializing` and `voice-author-notes-pollution` from pass (2026-08-29) to fail —
Category H banner-in-prose. Moved to `.ts` `authorNotes[kind: "refined-framing"]`; both
re-swept individually, both pass. Caught by the preflight, which is what it is for.

### Verification

`qa-sweep` exit 0; block tally 81 pass / 14 n/a / 1 warn / 1 fail. The residual fail is
`voice-status-section`, which **failed identically on 2026-08-29 before this branch existed** —
pre-existing, left alone. `run-validate` exit 0 (14 issues, **none naming this block**; the
13→14 delta is `main` moving 44+ commits between runs). Render-QA grep battery clean. No
`.lean` changed.

### Method notes

- `--only` takes ONE criterion; passing it twice silently runs only the last.
- Do not let `json.dump` reformat `.beans/*.json` — `indent=1` produced a 2432-line diff for
  three field edits; the file's own `indent=2` gives 18.
