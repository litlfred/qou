---
# qou-uinl
title: 'Mathlib infra: orbit-quotient bridge + invariant-function count = the q=1 Schur-Weyl trace d^c(sigma)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T06:17:38Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-59vq
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


TENSOR-POWER WRAPPER (user request 2026-09-05) — staged, and STAGE 2 IS BLOCKED ON A
MEASURED MATHLIB GAP.

MEASURED: Mathlib/LinearAlgebra/PiTensorProduct.lean contains ZERO occurrences of
'Basis'. There is no basis for the Pi tensor power anywhere in Mathlib, and no
finrank lemma for it either. So a literal 'LinearMap.trace of PiTensorProduct.reindex'
statement cannot be written without first CONSTRUCTING that basis, which is itself a
Mathlib-scale contribution (it is presumably why Mathlib lacks it).

WHAT MATHLIB DOES GIVE, and it is the key step:
  Matrix.trace_permutation : trace (sigma.permMatrix R) = (Function.fixedPoints sigma).ncard
  PiTensorProduct.reindex (e : iota1 =~ iota2)   -- the action exists, just no basis

STAGE 1 (doable, is the wrapper's real content): in the concrete free-module model
V = (kappa -> R), so V^{tensor alpha} = ((alpha -> kappa) -> R), sigma acts on the
monomial basis by index precomposition f |-> f o sigma. That is a PERMUTATION MATRIX,
so trace_permutation gives trace = #fixed points, the fixed points ARE the invariant
functions, and orbitCount_invariant_functions gives (card kappa)^orbitCount sigma.
A genuine trace theorem, fully proved.

STAGE 2 (attempt): construct ⨂[R] i : alpha, (kappa -> R) ≃ₗ ((alpha -> kappa) -> R)
via PiTensorProduct.lift on the multilinear map v |-> (fun f => prod_i v i (f i)),
with inverse g |-> sum_f g f • tprod (single (f i) 1) and PiTensorProduct.induction_on
for one direction. This IS the missing basis in the special case needed.
DO NOT fake stage 2 with a sorry or an axiomatised structure if it does not close.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress 2026-11-17 (Round 66 — PR #8340)

- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/AddableCellRatioFakeDegreeTwoRowBallotWeightTensorPowerCharacterOrbitTrace.lean` (Lean 4.24.0, `0` `sorry`, `0` `axiom`, `0` warnings, `0` directory-mode static vacuity & borrowed-name advisories).
- 80-dps `mpmath` numerical witness stamped in `computations/probes/addable-cell-ratio-fake-degree-two-row-ballot-weight-tensor-power-character-orbit-trace.witness.json` (`scriptHash = 0309390e769d`, `scriptCommitSha = c43b700db42337a2547c8ff1e2a1665156dd27ea`, `HEAD = d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).
- PR: https://github.com/litlfred/qou/pull/8340 (`ready: d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8340, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
