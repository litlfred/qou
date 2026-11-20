---
# qou-ozts
title: 'GAP: universal-ilp.py calls apply_atom_nf, which is defined nowhere'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T15:43:18Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-trd0
---

computations/universal-ilp.py lines 191 and 202 call apply_atom_nf(nf, 1, 0) and apply_atom_nf(nf, 6, 6). NameError at runtime: the name is defined nowhere in the tree. Python suggests build_atom_nf, but that is a DIFFERENT function - build_atom_nf(Z, N) BUILDS a normal form, while these call sites pass an existing nf plus (Z, N). Guessing the rename would change what the ILP computes, so it was left alone. The producer cannot run, so its witness (universal-ilp.witness.json, carrying the OLD-MUON value B) cannot be drained. Found by the B-population sweep, PR #5889.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8411, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
