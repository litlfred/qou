---
# qou-tqr9
title: 'Agent-adjudicated QA axes are silently lost by "regenerate rather than merge" conflict resolution'
status: todo
type: task
priority: normal
created_at: 2026-08-19T21:20:00Z
updated_at: 2026-08-19T21:20:00Z
---

The standard resolution for a `.qa.json` conflict is: do not hand-merge
generated output, let `qa-sweep` regenerate it against the merged tree
(`local/integration-audit`). That is right for **script** criteria and
wrong for **agent-adjudicated** ones, and nothing in the tooling marks
the difference at the point where an agent is choosing a resolution.

Measured instance. The #5103 takeover (`0afc0097f`) resolved 742 sidecar
conflicts to main's side, stating "the honest sidecar state is whatever
qa-sweep produces against the merged tree, which the QA pipeline
regenerates on its next pass." No pass can produce those entries: the
`trap-*` family is `automated: false`, so `qa-sweep` regenerates the
high-recall SCRIPT candidates and never the verdicts. 7381 agent verdicts
over 738 blocks — each one an agent having read a block in full across
ten categories — went back to reading as never-audited. Restored in
`a89de3169` by re-validating each entry's `field_hash.md` against live
main and porting only the 97 % that still certify the current source.

The exposure is not limited to `trap-*`. Every agent-adjudicated axis has
the same shape: `da-*` (devils-advocate), `clarity-*`, `q-usage-*`, and
the `lean-vacuity-review-ledger` verdicts. Each one is expensive to
produce, cheap to drop, and drops **silently** — the sidecar stays
well-formed and the axis just reports fewer findings.

Candidate fixes, cheapest first:

1. **Say it in the skill.** `local/integration-audit` and
   `local/prepare-merge-auto` should carve out agent-kind entries from
   the "regenerate, don't merge" rule, with the reason (a verdict has no
   producer) rather than just the instruction.
2. **Make the resolution mechanical.** A small script that takes the
   union of both sides' agent entries and drops those whose `field_hash`
   no longer matches the merged tree. That is what the restoration did by
   hand; it generalises to any axis and removes the judgement call.
3. **Make the loss visible.** A check that fails when a merge or takeover
   reduces the count of agent-kind entries on any axis, so the drop is a
   red check rather than a silent regression.

Item 2 is the one that would have prevented this without anyone needing
to know the axis was agent-adjudicated.
