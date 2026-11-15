---
# qou-bk77
title: Cite PhysRevD.108.106023.pdf at conj:stokes-dt-bps-bridge
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:41Z
updated_at: 2026-09-05T09:03:21Z
---

The non-degeneracy table in conj:stokes-dt-bps-bridge asserts the 4_1 open count is 5; the explicit published quiver is the direct evidence for that entry.

**From the source**
- sec. III A, the explicit matrix C^{4_1}, with the size formula in sec. III ("(4mp+1) x (4mp+1)") — The figure-eight knot, as the double-twist knot with both twist parameters equal to one, has an explicit 5x5 quiver matrix under the knots-quivers correspondence.
  Use here: Independently confirms the 5-node open-BPS count that conj:stokes-dt-bps-bridge's sector non-degeneracy argument infers from det(4_1) = 5, turning an inference into a checked value.
- sec. II, eq. (8)-(9) and sec. IV — A quiver presentation of the colored Jones polynomial is proposed for all double twist knots, with the quiver matrix built recursively from a base set of blocks; the Alexander polynomial of the family takes the form 1 - pmX.
  Use here: Extends the check beyond the figure-eight to a family, so the corpus's open-vs-closed sector separation could be tested at a second knot rather than only at 4_1.

Source: `library/physrevd108106023/PhysRevD.108.106023.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/physrevd108106023/  ->  [singh-physrevd108106023]
  Knot-quiver correspondence for double twist knots

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [singh-physrevd108106023] as the citation key when you do it.


## DONE 2026-09-05 — cited, and the rule behind the count is now recorded too

The block's non-degeneracy table asserted the 4₁ open-BPS count as
`det(4₁) = 5` with only the knots-quivers **rule** behind it ("one node per
HOMFLY-PT generator"), calibrated on a single worked trefoil. The direct
evidence was in the corpus and uncited.

`singh-physrevd108106023` is now cited in `stokes-dt-bps-bridge.{md,ts}`. The
ref entry already existed (`qou-qu53`, completed) but had never been wired to
any block — so the reference was registered and unreachable.

Beyond what the bean asked, the prose now records **why the rule is trustworthy
rather than lucky**: node count equals determinant at **four** knots — 3₁ (3×3),
4₁ (5×5), 6₁ (9×9), 8₁ (13×13) — all equal to `1 + 4pm`. The old parenthetical
calibrated on the trefoil alone, and a one-knot calibration cannot separate a
rule from a coincidence.

Verdict untouched: `5 ∉ {3,4}`, the open-HOMFLY bridge still fails, the
closed-sector bridge is still the one adopted. Firming up the 5 strengthens that
FAIL.

**Verification.** Render-QA grep battery 9/9; both cite keys resolve in
`references.ts`; `qa-sweep` refreshed this block's sidecar (source-hash churn
only, scoped to this block); `run-validate.ts` exits 0 at "Valid", 10
pre-existing issues, none naming this block.

Companion probe (`qou-48dw`):
`d1b_published_41_quiver_confirms_node_count_probe.py`, 7/7.
