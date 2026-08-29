---
# qou-ozts
title: 'GAP: universal-ilp.py calls apply_atom_nf, which is defined nowhere'
status: todo
type: task
priority: normal
created_at: 2026-08-28T15:43:18Z
updated_at: 2026-08-28T15:43:18Z
parent: qou-a1lw
---

computations/universal-ilp.py lines 191 and 202 call apply_atom_nf(nf, 1, 0) and apply_atom_nf(nf, 6, 6). NameError at runtime: the name is defined nowhere in the tree. Python suggests build_atom_nf, but that is a DIFFERENT function - build_atom_nf(Z, N) BUILDS a normal form, while these call sites pass an existing nf plus (Z, N). Guessing the rename would change what the ILP computes, so it was left alone. The producer cannot run, so its witness (universal-ilp.witness.json, carrying the OLD-MUON value B) cannot be drained. Found by the B-population sweep, PR #5889.
