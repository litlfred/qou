---
# qou-4rhu
title: S3 Conform to the folio_init layout; QA results to the cat-harness qa-reports branch
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:15Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-n4r9
---

Size M. Owner ruling 2026-10-04 (decision 11): QA sidecars use cat-harness qa-reports. README markers via readme:sync:check. Audit 786 .tex tables vs 444 table blocks and REPORT tables that exist only in .tex; never drop content.

Owner hard rule: no math or physics content is changed. Every story ends with a parity check: block, chapter and .lean counts unchanged, statements byte-identical by hash, witnesses unchanged.


2026-10-05 — part 1 (QA results to qa-reports) and part 2 (README markers) on claude/s3-qa-reports-2026-10-05.
- qou.json now declares the `qa` directory: test/results/, graphKinds [qa], storage branch cat/cat-harness/qa-reports (the platform's QA_BRANCH, same at pin 5693b174). The platform's resolveQaLocation(qou) resolves it, present=true. Gitignored except test/results/.gitkeep.
- .github/workflows/compute-qa.yml (dispatch-only) runs every gate with every gate's setup (`compute-qa.py --every`) and is the ONLY publisher. Reason: qa:publish never overwrites an entry, so if four workflows published the same commit, the first write would stand and the other three would be dropped.
- README: readme:sync:check was red (folio:toc, lean-coverage, lean-modules, workflows). A plain sync would have RENAMED the paper in the README to 'Quantum Observable Universe', taken from folio/folio.ts's paperRef title, a third copy of the title that identity.ts (bean qou-yqko) was made to end. Fixed at the source: folio.ts now carries 'On the Mechanics of Quantum Observable Universes'. It is a literal, not an import of paperIdentity, because the generator reads folio.ts as text (an import made it fall back to the directory name). After that, the sync changes only Lean module counts and the workflow list, and check exits 0.
- Still open in S3: (3) audit the 786 .tex tables against the 444 table blocks and REPORT tables that exist only in .tex, never dropping content; (4) the broader folio_init layout conformance.
Parity: no .lean, witness or content .md change; the only folio/ edit is folio.ts's paperRef title.


2026-10-05 — END-TO-END PUBLISH VERIFIED. compute-qa.py --all at PR head e36739a7a1 (19 gates, the 2 setup gates excluded) was published with qa-store under pr/7518/e36739a7a123f404bed2bad8587157604445ac94: PUBLISHED on attempt 1, commit c804129bdc. This created refs/heads/cat/cat-harness/qa-reports in qou. Read back with `qa-store.ts read`: q0-anchor-flip.json returned intact (exit 0). The key is the PR's own, so no main/<sha> entry was spent.


2026-10-05 — part 3 (.tex tables) MEASURED: docs/audits/2026-10-04-workplan-and-migration/S3_tex_tables{.tsv,_report.md}.
- 4 tracked .tex files. All 786 tabulars are in ONE generated file, qou-all-tables.tex, a stale snapshot of make-all-tables.py output last touched in b7accffcbc. No hand-written .tex holds a content table.
- 444 table blocks confirmed. 786 is not 444 plus 342 orphans: markdown pipe tables in non-table blocks also render to tabulars (remark 167, proof 54, proposition 37, conjecture 34, prose 23, ...).
- 784 of 787 matched to a current block; 3 are the platform legend.
- ONE table exists only in .tex: qou-all-tables.tex:15472 '[appendix-surreals] #12', an 11-row development-history table (rounds 1-11, commits 12202fb0..710039e7). It is recoverable from b7accffcbc. OWNER DECISION: leave it, or restore it as an authorNotes entry. Default if nobody answers: nothing changes.
- Recommendation (judgement): treat qou-all-tables.tex as derived output, and retire the '786' figure rather than updating it.
Remaining in S3: part 4, folio_init layout conformance.


2026-10-05 — owner: 'fix all', taking the recommendation on the one table that exists only in .tex ('[appendix-surreals] #12', an 11-row development history): LEAVE IT. It is a status-history table, probably dropped on purpose, and it stays recoverable from b7accffcbc:qou-all-tables.tex. Nothing restored. qou-all-tables.tex is treated as derived output.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
