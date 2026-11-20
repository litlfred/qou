---
# qou-u8oy
title: Vector 3 (multi-level jet tower) is NOT open — conj:binding-manybody-eq-jet-filtration already carries it
status: todo
pr: 8302
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T08:45:07Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

2026-08-29, branch claude/tower-gap-lean-and-infra-2026-08-29 (PR #5978),
milestone qou-xsue.

The third attack vector on the tower gap was framed as "multi-level tower
Sigma_n over jet levels (Kahler-differential propagation), as a Lean
conjecture-class scaffold". Running the AGENTS.md corpus-grep checklist BEFORE
writing anything: THAT SCAFFOLD ALREADY EXISTS. Building it would have been
re-declaring a live conjecture as open, which is the exact failure the checklist
is for.

WHAT IS ALREADY THERE.

  conj:binding-manybody-eq-jet-filtration
      Lean qou:QOU.Mass.BindingManyBodyJetFiltration.
      B(K) = Sum_n m_e a_D^(n). This IS the multi-level jet tower.
  folio/quantum-observable-universe/mass-theory/jet-filtration-binding-extensive.md
      Proposition, PROVED: the body-order binding is monotone non-decreasing in
      the cutoff A, and strictly increasing when a new order contributes. This
      is the qualitative extensivity -- exactly what the intensive
      rotation-phase reading theta_lambda = arccos(chi/d) structurally lacked.
  folio/quantum-observable-universe/mass-theory/binding-genfun-qdifference.md
      Proposition, conditional: q-difference recurrence of the binding
      generating function.
  folio/quantum-observable-universe/mass-theory/binding-closure-conditional.md
      Theorem, conditional on the conjecture.

Also found and NOT to be rebuilt: content/.../quantum-universes/categorical-jet.md,
lifting-and-descent/{brane-tower-terminology,recursive-brane-tower}.md,
observations/brane-tower-q-laplacian-decay-{proof,interpretation}.md, and the
deprecated compute computations/_deprecated/{per_braid_tower_jet_v2,
jet_lifted_hecke,per_braid_tower_hybrid_jet,level1_vhat_brane_tower}.py.

WHAT IS ACTUALLY OPEN, per jet-filtration-binding-extensive's own SCOPE section.
Three inputs are carried as non-negativity HYPOTHESES, not derived:

  (1) the super-exponential magnitude of the Seiberg-Witten period
      a_D^(n) = contour-integral of lambda_SW^(n) -- the sqrt-branch
      falling-factorial growth; the QUANTITATIVE extensive channel;
  (2) the non-abelian-Stokes identity a_D^(n) = lw(n-1), the mean quantum
      dimension -- conjectural, residue-sum form prop:sw-period-residue-sum;
  (3) the per-atom residue weight w_n(K) -- the open rho*A scale rule, a
      q-difference recursion output.

The established content is qualitative extensivity given non-negative period
and weight data. The magnitude that matches experiment depends on (1)-(3).

WHY THIS IS RECORDED RATHER THAN ACTED ON. Picking among (1)-(3) is an
owner-level choice: they are different mathematics (period asymptotics vs a
Stokes identity vs a q-difference recursion), with different costs and different
downstreams, and none is a continuation of the V_hat/Markov-parameter work in
qou-zloi and qou-lbgh -- that is a different object (the Phi_q tower over
generators, not the body-order series over n). Forcing a connection would be the
kind of over-reach the corpus-grep rule exists to prevent.

NOTE ON SCOPE. This bean asserts only that the SCAFFOLD is not open. It does not
claim (1)-(3) are open -- that claim would need its own corpus-grep, which has
not been run here.


CORPUS-GREP RUN 2026-08-29 (this bean explicitly deferred it). PR #6051, audit
docs/audits/2026-08-29-jet-filtration-three-inputs-corpus-grep.md.

The bean closed with: 'This bean asserts only that the SCAFFOLD is not open. It
does not claim (1)-(3) are open -- that claim would need its own corpus-grep,
which has not been run here.' It has now been run. ONE of the three is open.

(1) super-exponential magnitude of a_D^(n) -- NOT OPEN as a growth class.
Settled 2026-06-25 (audit 2026-06-25-sw-jet-prolongation-explicit-and-fork.md,
PR #2795): sqrt-branch at disc_X=0, plus an independent corpus-internal
residue-sum route. Object positively identified (#2822): T_q(n) = n*lw(n-1) is
the q-deformed involution number, T_q(n) -> I(n) (A000085) by RSK -- re-verified
exact n=1..12 today. AND the gloss the SCOPE section carried for it, 'the
sqrt-branch falling-factorial growth', names a form that was PRUNED: re-measured
today, lw / |prod[1/2-k]_q| decays 4.0109 -> 0.0282 over n=2..10 with monotone
decreasing successive ratios (0.889 -> 0.383), so no constant R^n absorbs it --
the falling factorial OUTGROWS lw. Scope-(a), not a structural exclusion; the
nu=1/2 q-Bessel order and the super-exponentiality both stand. What is left is
the exact q-statistic, itself bounded: no q-holonomic recurrence for T_q(n) at
depth <=3, Laurent degree <=3, established precision-independently.

(2) the keystone a_D^(n) = lw(n-1) -- GENUINELY OPEN. 3b conjecture class
QOU.Mass.NaStokesKeystone.ProlongationPeriodMeanQuantumDim, no instance.
Consumed only at c=1,2,3, and as of PR #6051 those three lw values are derived
from the q-hook-length formula rather than substituted as literals; they
reproduce the probe's first three rows exactly (1.0, 1.336966, 2.532780).

(3) the residue weight w_n(K) -- NOT OPEN. Scope-(b) excluded 2026-08-29 by
bean qou-1xne / PR #5967, invariant cited (no_scalar_kernel_on_carrier,
sorry-free): w_3 is a required boundary condition of a rank-2 problem. Read and
cited, not re-derived -- a sibling owns it.

SIDE FIX: the falling-factorial probe's set_audit_only named a file that never
existed, so every witness it wrote carried a dead pointer. Fixed at the
producer; payload byte-identical (also across mpmath 1.3.0 -> 1.4.1).

SO: the remaining research target under this conjecture is (2) alone.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8302, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
