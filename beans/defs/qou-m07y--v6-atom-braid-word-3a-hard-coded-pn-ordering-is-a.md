---
# qou-m07y
title: 'V6: atom_braid_word_3A hard-coded p/n ordering is a non-physical DOF; re-measure the spread under convention D'
status: completed
type: task
priority: normal
created_at: 2026-08-29T18:45:57Z
updated_at: 2026-08-29T18:52:47Z
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


## RESOLVED as a STRUCTURAL EXCLUSION 2026-08-29 (PR #6059)

Lean: QOU/MassTheory/ChainBondOrderDependence.lean, sorry-free, lean-direct
exit 0, #print axioms clean on all 8 decls (five need [propext] alone).

The bean asked to re-measure the ordering spread under convention D and make
the answer order-independent. The structural question turns out to settle it
without the sweep:

  orderIndependent_iff -- the chain bond sum is invariant under every
  rearrangement IFF L_pp = L_pn = L_nn. Two A=3 witnesses force it:
    B(ppn) = L_pp + L_pn  vs  B(pnp) = 2 L_pn  =>  L_pp = L_pn
    B(nnp) = L_nn + L_pn  vs  B(npn) = 2 L_pn  =>  L_nn = L_pn

  not_orderIndependent_of_ne -- L_pp != L_nn ALONE breaks it, every A >= 3.

With InterfaceScalar.charge_independence_iff (L_pp = L_nn <-> h = 0 <-> q = 1):
the linear chain is arrangement-independent ONLY at q = 1. At q0 no bond-scalar
assignment repairs it.

SCOPE-(b), invariant named. Excludes the LINEAR-CHAIN ANSATZ as a well-defined
binding functional at q != 1. Does NOT exclude the bond picture. Do not
symmetrise over arrangements and do not hunt a better convention -- the defect
is that the chain has an arrangement at all. The repair changes the BOND SET
(coordination graph / all-pairs / derived edge set, qou-h7mh).

The D-frame spread re-measurement is now MOOT as a decision input (the answer
is "nonzero for any q != 1"), though the numbers would still be worth having
for the audit record if a probe is ever cheap.
