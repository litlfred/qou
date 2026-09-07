---
# qou-c041
title: q-integer [n]_q has a canonical impl (qou_substrate.constants.q_int) used by 21 files while 192 define their own — no single place to fix a limit, precision or convention
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T13:41:17Z
updated_at: 2026-09-07T14:02:18Z
---

RESOLVED AS A DIFFERENT PROBLEM 2026-09-07 (audit sec 21). It is NOT gratuitous duplication — it is a CONVENTION SPLIT. Symbolic AST audit (computations/audits/q_integer_duplication_audit.py, compares in a sympy symbol q, never at q0): 366 definitions in 363 files; 179 q0-pinned (1 arg), 187 q-parametric; 158 symbolically comparable, 208 not. FOUR distinct forms: 126 SYMMETRIC (q^n-q^-n)/(q-q^-1); 30 CLASSICAL/Gaussian (q^n-1)/(q-1); 1 sqrt-normalised; 1 symmetric-in-q^2. Bridge identity, verified n=2,3,5,7 and Lean-proved at n=2,3: [n]_symm(q) = q^(1-n) [n]_clas(q^2). ROOT CAUSE: the canonical q_int(n) in qou_substrate/constants.py takes n ONLY, with Q/Q_INV/HA as module globals, so it is q0-pinned and cannot serve any q-parametric caller — which is why 366 local copies exist. Lean: QOU/Substrate/QIntegerConventions.lean, 8 theorems, lean-direct exit 0, 0 sorry, axioms {propext, Classical.choice, Quot.sound}.
