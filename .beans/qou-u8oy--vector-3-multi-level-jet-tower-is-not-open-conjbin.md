---
# qou-u8oy
title: Vector 3 (multi-level jet tower) is NOT open — conj:binding-manybody-eq-jet-filtration already carries it
status: todo
type: task
priority: normal
created_at: 2026-08-29T08:45:07Z
updated_at: 2026-08-29T08:45:47Z
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
  content/quantum-observable-universe/mass-theory/jet-filtration-binding-extensive.md
      Proposition, PROVED: the body-order binding is monotone non-decreasing in
      the cutoff A, and strictly increasing when a new order contributes. This
      is the qualitative extensivity -- exactly what the intensive
      rotation-phase reading theta_lambda = arccos(chi/d) structurally lacked.
  content/quantum-observable-universe/mass-theory/binding-genfun-qdifference.md
      Proposition, conditional: q-difference recurrence of the binding
      generating function.
  content/quantum-observable-universe/mass-theory/binding-closure-conditional.md
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
