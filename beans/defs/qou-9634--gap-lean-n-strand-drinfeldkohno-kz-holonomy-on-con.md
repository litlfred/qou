---
# qou-9634
title: 'GAP: Lean n-strand Drinfeld–Kohno (KZ holonomy on Conf_n = Jimbo R-matrix)'
status: todo
type: task
created_at: 2026-10-11T06:39:25Z
updated_at: 2026-10-11T06:39:25Z
parent: qou-ywyq
---

Two strands are proved sorry-free in QOU/Mass/KohnoTwoPoint.lean (KZ transport solved and unique; exchange = q^{-1/2} times a weight-preserving conjugate of Jimbo's Ř). Flatness of the n-point sl2 KZ connection, as the infinitesimal pure braid relations, is proved in mass-endomorphism/kz-connection-sl2.lean. Open for general n: (1) path-ordered holonomy of a flat log connection on Conf_n as a P_n representation (no Mathlib infrastructure); (2) identification with the R-matrix representation, either via Kohno's analytic continuation (kohno1987 Thm 1.2.8, Rem 1.3.14) or via the algebraic route in docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md, which needs Drinfeld's KZ associator, the skein-category universal property and Hecke block theory. Next honest step: formalise (1) for n=3 on the slice z1=0, z3=1 (two loops), matching computations/kz_real_q0_pure_braid_monodromy_probe.py.
