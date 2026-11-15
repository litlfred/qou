---
# qou-kpx7
title: 'content-scaling-correspondence: re-word to the JM-eigenvalue statement and demote the scaling table to a remark (options 1+2 of PR #6600)'
status: completed
type: task
priority: normal
created_at: 2026-09-04T12:21:58Z
updated_at: 2026-09-04T12:43:35Z
---

Owner said 'merge and go' twice with the PR #6600 wording decision and its recommendation (1+2) in front of them; read as approval of the recommendation. Scope: prop:content-scaling-correspondence .md keeps only the true statement (content = q-Jucys-Murphy eigenvalue exponent, a total-spin datum along the sub-tower), lean.ref -> the JM carrier; the BW scaling table moves to a new remark rem:content-scaling-dictionary with interprets: the proposition; BoxContent.lean header updated (refutation stays as the record of the old sentence). Consumer crystal-isospin-degeneracy-proof uses only c(.) and is untouched. Reversible in one revert.


## Result (2026-09-04)

Options 1+2 executed on branch `claude/content-scaling-reword-2026-09-04`.

- `prop:content-scaling-correspondence` now states the true fact: box content `c = j - i` of the box holding `k` in a standard tableau `T` is the q-Jucys–Murphy eigenvalue exponent, `L_k v_T = q^{2c} v_T` (Ram 1997), on the seminormal basis of `S_λ`. Ref moved to `qou:QOU.SchurWeyl.SeminormalRep.seminormalRep_qJM` (resolves via the pipeline grep fallback to `QJucysMurphyEigen.lean`; `lean-ref-owns-decl` pass). Cites jimbo1986 + ram1997.
- The refuted sentence ('the content of a box is the magnetic quantum number / weight of V_λ') is gone from the statement; `BoxContent.lean` keeps the sorry-free refutation theorems as the record and its header now says so.
- The BW scaling table moved to the new remark `rem:content-scaling-dictionary` (`interprets` the prop) with a paragraph on why content ≠ weight (box count ≠ weight count; largest content exceeds largest weight for ≥ 3 boxes).
- Docstring opener fixed at `QJucysMurphyEigen.lean:436` (voice-scholarly-default finding surfaced when the ref resolved there); lean-direct exit 0.
- Verification: validate clean (14 pre-existing, none on touched blocks); qa-sweep on both blocks with no automated findings; check-sidecars clean; render battery clean.
