---
# qou-9634
title: 'GAP: Lean n-strand Drinfeld–Kohno (KZ holonomy on Conf_n = Jimbo R-matrix)'
status: todo
type: task
created_at: 2026-10-11T06:39:25Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-ywyq
---

Two strands are proved sorry-free in QOU/Mass/KohnoTwoPoint.lean (KZ transport solved and unique; exchange = q^{-1/2} times a weight-preserving conjugate of Jimbo's Ř). Flatness of the n-point sl2 KZ connection, as the infinitesimal pure braid relations, is proved in mass-endomorphism/kz-connection-sl2.lean. Open for general n: (1) path-ordered holonomy of a flat log connection on Conf_n as a P_n representation (no Mathlib infrastructure); (2) identification with the R-matrix representation, either via Kohno's analytic continuation (kohno1987 Thm 1.2.8, Rem 1.3.14) or via the algebraic route in docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md, which needs Drinfeld's KZ associator, the skein-category universal property and Hecke block theory. Next honest step: formalise (1) for n=3 on the slice z1=0, z3=1 (two loops), matching computations/kz_real_q0_pure_braid_monodromy_probe.py.

**2026-10-11 update.** Part (1) is done and merged to main (PR #7719, commit e1f5d1b4e, `QOU/Mass/KZHolonomy/`). It covers:
- Conf_n and the KZ form, which is flat (`kzForm_isFlatOn`);
- transport depending only on endpoints (`flat_transport_eq`);
- `kzBraidRep : B_n →* Aˣ`, which equals the permutation action at coupling 0;
- continuity in the coupling (`continuous_kzBraidRep`).

Part (2) is still open: identifying it with the Jimbo R-matrix representation. That work is in progress on PR #7673 by the rigidity route (audit §5), so this bean stays open until it lands.

Other Lean ingredients now in place on PR #7673:
- the trace quotient has dimension `catalan` over any field;
- the Jimbo kernel equals the trace radical (ordered fields);
- dim TL_n = catalan, with the Jones basis, over ℝ;
- the quantum sl₂ fundamental representation on V^⊗n.

**Assembly status (later 2026-10-11).** Proved without sorry on PR #7673:
- `BraidHeckeFactor`: one Hecke-quadratic generator makes the braid representation factor through H_m(q).
- `KZTwoStrandHecke`: the two-strand KZ holonomy satisfies the Hecke quadratic.
- `KohnoComparison`: rigidity on connected parameter sets.

Still open:
1. the KZ Hecke quadratic for n ≥ 3 (local monodromy at collisions);
2. continuity in q of the Wedderburn isomorphism;
3. a base point other than coupling 0, where q = 1.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.
