---
# qou-m07y
title: 'V6: atom_braid_word_3A hard-coded p/n ordering is a non-physical DOF; re-measure the spread under convention D'
status: todo
type: task
priority: normal
created_at: 2026-08-29T18:45:57Z
updated_at: 2026-08-29T18:46:56Z
parent: qou-mhj9
---

NOT YET STARTED — opened 2026-08-29 (PR #6059 session). Carried by qou-h7mh's
2026-08-08 correction block; this bean tracks the fix rather than the finding.

DEFECT (a code fact, convention-independent): atom_braid_word_3A hard-codes
ordering = ['p']*Z + ['n']*N, and B depends on the ordering. A nucleus has no
ordering, so the spread is a non-physical degree of freedom.

C-FRAME spreads (2026-08-08, MUST be re-measured under convention D before
quoting): 3He 0.9825, 4He 2.2708, 6Li 2.5766, 7Li 2.8823 MeV. The canonical
choice is not even the good one: 3He ppn -11.9% vs pnp +0.79%. The mirror pair
is decided by it — pnn/ppn splits 2.271 MeV, npn/pnp splits EXACTLY 0 (nature
0.764).

WHY IT BLOCKS: up to ~2.9 MeV of every A>=3 magnitude measurement is this DOF,
including the body-order cumulants b3/b4 that qou-i5yp's target is built from.
Isospin T-typing does NOT dissolve it (ppn -> {pp,pn} vs pnp -> {pn,pn} are
different multisets).

DO NOT fit m_pp/m_pn/m_nn (the lever exists in the signature; tuning it buys a
table and costs the parameter-free claim). The fix is to make the answer
order-INDEPENDENT, or to derive the ordering.
