---
# qou-uinl
title: 'Mathlib infra: orbit-quotient bridge + invariant-function count = the q=1 Schur-Weyl trace d^c(sigma)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-05T06:17:38Z
updated_at: 2026-09-05T06:25:35Z
---

DONE 2026-09-05, sorry-free, lean-direct exit 0 in 3.0 s, zero warnings, #print
axioms clean on all four public results.

WHAT IT IS. The combinatorial core of ClassicalTraceFloor's STEP 1 (the Schur-Weyl
leg), for q = 1 only:
    #{f : alpha -> beta // f o sigma = f} = (card beta) ^ orbitCount sigma
At card beta = 2 that is the 2^c(sigma) step 1 assumes: sigma permuting the factors
of (C^2)^{tensor n} fixes exactly the basis vectors constant on each cycle, and in
the monomial basis that character IS this count.

THE LOAD-BEARING PIECE is the bridge
    Fintype.card (Quotient (SameCycle.setoid sigma)) = orbitCount sigma
built from an explicit equivalence: every orbit is either a FIXED POINT or one of the
CYCLE FACTORS. That is exactly the split orbitCount is defined by, so the bridge is
what turns orbitCount from cycleType bookkeeping into a genuine count of orbits.

MEASURED MATHLIB GAP. Mathlib HAS Equiv.Perm.SameCycle.setoid and NOTHING relating
the quotient to cycleType; no invariant-function count; no permutation character.
Fintype.card_quotient_le is the only quotient-counting lemma in range and an
INEQUALITY is not what is needed. So the equivalence had to be built.

WHAT IS NOT CLOSED, and do not let this be read as more than it is:
  * the LINEAR-ALGEBRA WRAPPER -- identifying this count with a trace over an actual
    tensor power (PiTensorProduct) is a further step, not done here;
  * QUANTUM Schur-Weyl (q != 1) is untouched. Bean qou-mpq5 scoped that as a
    multi-week gap (R2c / R2-inst, the Jimbo double-centralizer + Hoefsmit matrix
    units) and deliberately refused to fake it. That assessment STANDS; this file
    does not contradict it, because it addresses a different and much smaller claim.

PRIOR-WORK CHECK (corpus-grep path 6 earned its keep). qou-mpq5 exists on
'prove Schur-Weyl trace = character sum' and says 'Schur-Weyl already anchored at
q=1 in bean 1ict'. That reference is MISLEADING for formalisation purposes: 1ict is
an Elliott SU(3) CONTENT/literature anchor, completed, with no Lean. So the q=1
formalisation was genuinely absent, not duplicated.

SMOKE TESTS in-file (a direction error would otherwise be invisible): sigma = 1 gives
|beta|^|alpha|; a transposition gives |beta|^(|alpha|-1).
