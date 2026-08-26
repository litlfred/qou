---
# qou-gue2
title: 'prop:chi-sym-alt-closed-form: create the missing block, un-orphan the Lean'
status: todo
type: task
created_at: 2026-08-26T18:09:36Z
updated_at: 2026-08-26T18:09:36Z
---

Retroactive claim — this work was done and pushed before a bean existed, which is
the omission the end-of-turn reporting rule exists to catch. Opening it so the
work is visible rather than backdating a claim.

## Done ([PR #5847](https://github.com/litlfred/qou/pull/5847))

Two loose ends from #5833 that turned out to be one thing:

- `chi_sym_alt_closed_form.py` declared `set_content_block("rem:chi-sym-alt-closed-form")`
  for a block that did not exist anywhere in `content/`.
- `chi-sym-alt-closed-form.lean` sat in a content chapter directory with no `.ts`
  and no `.md`, so no `.qa.json` and nothing but an agent ever checked it.

Creating the block fixes both: a `proposition` is the kind that takes a `.lean`
sibling. Made it a proposition rather than the `remark` the dead label guessed —
the Lean proves it sorry-free, and a remark would need an `interprets` target
that does not exist.

## Two things worth carrying forward

**The corpus already knew.** `docs/audits/2026-05-06-orphan-witness-characterization.md`
catalogued this exact orphan in May and I presented it as a new finding in #5833.
Its row is resolved rather than deleted, recording that its guess (`remark`)
differs from the kind chosen and why. Corpus-grep before writing up a finding.

**A clean validate run does not prove a new file was read.** `run-validate.ts`
exited 0, which proves nothing about coverage. Broke the label prefix on purpose
(`rem:` on a `proposition`), re-ran, got exit 1 naming the file — *then* the pass
meant something. Same discipline as "a detector whose pattern can match the
detector is not a detector", which bit twice earlier in this arc.

## Verification

validate exit 0 (13 issues, all pre-existing elsewhere); lean-direct exit 0;
`lean-vacuity-axiom-audit --check-ledger` exit 0 / 0 candidates; ratchet NEW
dirty 0 / REGRESSED 0; render preflight clean; sidecars generated (99 criteria,
0 critical / 0 major / 0 minor, 41 `needs-agent` — the designed state for a fresh
block).
