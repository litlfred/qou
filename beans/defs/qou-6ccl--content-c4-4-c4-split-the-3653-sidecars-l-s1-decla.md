---
# qou-6ccl
title: '[CONTENT C4] Split the 3,653 sidecars'
status: todo
type: feature
priority: normal
tags:
    - migration
    - content
    - needs-owner
created_at: 2026-10-04T16:35:55Z
updated_at: 2026-10-04T16:36:30Z
parent: qou-5lsb
---

From the CONTENT migration analysis (2026-10-04), story C4. Full report: docs/audits/2026-10-04-workplan-and-migration/CONTENT_report.md.

4. C4: Split the 3,653 sidecars (L; S1 declares `test/attestations` + `qa` storage; owner confirm for removal). - Derived: `qa:refresh` → `qa:publish` to qou's qa-reports branch. - Judgements: `qa:attestations:migrate`, verbatim. - Done when: the attestation store holds exactly 126,315 agent+human entries; the 128 null entries have an owner ruling; `qa:verify-moved` answers IDENTICAL; `qa:attestations:migrate:check` exits 0; P-C holds.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.

## 2026-11-15 — evidence relayed from stream 10 (bean `qou-4jhp`), session 01Qmmkt8RPNkJLAu7MkUPE3f

Coordinator (qou-s4ws) asked for an owner-decision bean "In-tree .qa.json sidecars are
no longer the qa-sweep destination; retire or regenerate?" — this bean already is that
question, so the evidence lands here instead of a duplicate.

- Measured: once `qa-sweep` loads (platform `a6e58846b`), it writes each verdict to
  `test/results/block-qa/<path>.qa.json` (gitignored, published to the qa-reports
  branch), NOT to the in-tree `<block>.qa.json` beside the block.
- Meanwhile agents still COMMIT in-tree sidecars by hand: `f4756e775` (2026-11-15)
  added `.qa.json` for `prop:sl-n-color-framing` / `rem:sl-n-color-frame-scope`,
  run against a locally patched platform. So the in-tree store keeps growing while
  nothing in the pipeline can refresh it; every such file is stale-by-construction
  after its block's next edit.

**Decision (owner):**
1. **Retire in-tree sidecars** (this bean's C4 split). Means: qa-reports becomes the
   only QA store. Costs: the C4 migration as scoped above. Risks: loses nothing if
   `qa:verify-moved` is IDENTICAL; irreversible once deleted. Commits to: agents stop
   committing `.qa.json`.
2. **Keep and regenerate in-tree** — needs a platform option to write beside blocks;
   none was found at `a6e58846b`. Costs: platform work. Commits to: two stores.
3. **Default (no ruling):** nothing changes; in-tree files keep aging and agents keep
   hand-adding a few.
Recommendation (judgement): 1, and in the meantime tell agents to stop committing new
in-tree `.qa.json` files.
