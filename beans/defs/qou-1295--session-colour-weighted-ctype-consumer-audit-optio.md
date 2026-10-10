---
# qou-1295
title: 'Session: colour-weighted ctype consumer audit (option-3 sweep)'
status: completed
type: epic
priority: normal
created_at: 2026-08-14T19:41:55Z
updated_at: 2026-08-14T22:11:51Z
---

MERGED as PR #5029 (rebase-merge, 6 commits, e46f710109..728eed27fc).

Pipeline run per AGENTS.md rule 10: Phase 0 sibling coordination, Phase 1 rebase+verify, Phase 1b Copilot review (3 threads, all resolved), Phase 2 resolution, Phase 4 rebase-merge, Phase 5 post-merge note. Branch preserved.

COLLISION, recorded because it is the notable part: PR #5028 (claude/agent-muon-proton-binding-wryo38) independently found the SAME root cause -- test_ctype_consumer_coverage Part B exempting any file that imports canonical_braid_crossings -- within the same afternoon, and fixed 12 consumer defects with 13 files overlapping mine. It explicitly deferred four files to #5029 in its own baseline comments. Two coordination comments posted on #5028: a pre-merge per-file map (take-yours / take-mine / same-approach) and a post-merge rebase guide naming the three things a naive resolution would drop (the d_for_ctype delta= kwarg, Parts C+D, and the four now-drained UNTRIAGED rows).

Copilot's third comment claimed the symbolic delta path would crash. It does not -- mpmath returns NotImplemented and sympy's reflected op takes over; the module runs exit 0. But it exposed a real smaller defect: mpf(1)/q seeds a Float(1.0) into the symbolic delta. Fixed by passing q_inv=1/q explicitly. Witness refreshed, provenance fields only, numeric payload byte-identical (the proton word has no averaged_weighted crossing).

Children: qou-uzk0 completed, qou-nmva completed, qou-hy6q open (owner call).
