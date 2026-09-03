---
# qou-gue2
title: 'prop:chi-sym-alt-closed-form: create the missing block, un-orphan the Lean'
status: completed
type: task
priority: normal
created_at: 2026-08-26T18:09:36Z
updated_at: 2026-08-26T18:42:31Z
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


## Completed 2026-08-26 — merged as `ff53a41ba` ([PR #5847](https://github.com/litlfred/qou/pull/5847))

Rebase-merge, 5 commits linear on main, branch preserved.

`prop:chi-sym-alt-closed-form` exists, with `.ts` + `.md` + `.qa.json`, and
`chi-sym-alt-closed-form.lean` is no longer an orphan Lean file in a content
chapter directory. The producer's `set_content_block` now resolves for the first
time since it was written.

### The merge, which was the interesting part

`/prepare-merge-auto` **stopped at Phase 3** rather than merging. Phase 0 found
[#5849](https://github.com/litlfred/qou/pull/5849) touching the same two files —
`git merge-tree` reported 4 conflict markers — and that PR was fixing a defect I
introduced in #5833:

- `set_compute_dps` imported and never called → the producer ran at mpmath's
  default **dps=15** while `fmt` serialised at 50.
- `from q_parameter import Q as Q0` (a float64, a hazard AGENTS.md names) fed
  into `sp.N(e.subs(q_sym, Q0), dps)`, capping every seminormal entry at 17
  digits however large `dps` was.

I had converted the arithmetic to mpmath and left the inputs float64 — the
**same error** retracted an hour earlier about the braid word, committed in a
different place at the same time. Two instances, one root cause: checking the
arithmetic and not the inputs.

The owner chose to hold #5847 and let #5849 land first. Correct on the merits:
their diff touched the function they had rewritten; mine touched a comment and a
string literal.

### What the rebase actually needed

Less than expected. **Only the witness conflicted, not the `.py`** — the two
changes sat in different regions and git took both. Verified rather than
assumed: their precision fix present in full, both float64 imports gone, my
block reference and `n_pn` / exact-prediction additions intact.

The witness was **regenerated, not hand-merged**. Hand-resolving a generated
file is how a precision fix gets silently reverted. It reproduced #5849's
numbers exactly (`rel_error_exact` 1.31e-14 / 1.99e-14 / 2.67e-14,
`compute_dps: 70`) with the new fields on top.

### Verification at merge

`witness_float64_padding_audit.py --strict` NEW 0 · raw-float64 ratchet NEW
dirty 0 / REGRESSED 0 · `check-sidecars` clean · `validate` exit 0 · producer
16/16 · `lean`-direct exit 0. Audit witnesses the gates rewrite as a side effect
were checked and came back byte-identical, so nothing was committed blind.

### Two lessons, both the same one

- `docs/audits/2026-05-06-orphan-witness-characterization.md` had catalogued this
  orphan in **May**. I presented it as a new finding. Corpus-grep first.
- A clean `validate` run does not prove a new file was **read**. Breaking the
  label prefix on purpose and confirming exit 1 is what made the pass mean
  something.
