---
# qcz12
title: 'qcz12 (INFRA): [2]_q-adic valuation on Z[q^pm1] + basic properties'
status: completed
type: task
priority: low
parent: qcz10
created_at: 2026-07-24T21:52:00Z
updated_at: 2026-07-24T21:04:27Z
---

Define v_[2](P) = max{k : (T 1 + 1)^k divides P} on LaurentPolynomial Z. Route:
Laurent ~= Polynomial after clearing a q-power; (q+1) is prime in Z[q] so use
Polynomial.rootMultiplicity at q=-1 (v_[2](P) = multiplicity of (X+1) in the
cleared numerator = rootMultiplicity (-1)). Prove:
- v(P * (T 1 + 1)) = v(P) + 1  (even branch RAISES valuation by 1 under /[2]).
- v of the odd-branch output.
Genuine reusable infra even if the descent (qcz13) walls. Preflight:
lean_leansearch 'rootMultiplicity', 'Polynomial.multiplicity (X - a)'. Heavy —
LaurentPolynomial<->Polynomial bridge is fiddly; timebox.

DONE (infra): qTwoValuation (rootMultiplicity at q=-1) + qTwoValuation_mul_qplus_one (v(P*(q+1))=v(P)+1, i.e. even branch lowers v by 1). Sorry-free. Confirms the wall: even step -1, odd step uncontrolled — no monotone measure follows (qcz13 wall stands).
