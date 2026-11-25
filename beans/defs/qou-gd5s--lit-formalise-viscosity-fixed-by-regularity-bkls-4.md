---
# qou-gd5s
title: 'Lit-formalise: viscosity fixed by regularity (BKLS §4 / BHMR §4.5) — paper stmt + QOU nu_q conjecture carrier'
status: in-progress
type: task
priority: normal
created_at: 2026-11-25T16:27:36Z
updated_at: 2026-11-25T16:32:15Z
parent: qou-i6e2
---

Owner (2026-11-25): 'bean up to lean formalize and add'; desired = author request (case a). Process per owner: (1) Lean the paper statement faithfully, proof as template; (2) round-trip verdict on statement+result; (3) general QOU q-NS statement as separate declaration, general→paper where possible; (4) staged conjectures with attempt log; (5) provenance in narrative and formally. Done when: sorry-free Lean or honest conjecture carrier + validated content block. Base: QOU/FluidDynamics/DECNavierStokes.lean (PR #9434), audit docs/audits/2026-11-25-qns-literature-formalisation.md.

RESUME STATE 2026-11-25T16:30Z: not started. Route (coordinator, owner question 'can we generalize and make use?'): (1) Lean BKLS §4 statement (smoothness at cutoff forces eta = r_c) in their setting; (2) QOU analogue as conjecture carrier: does a regularity/convergence condition on the q-step (Habiro convergence of q-difference NS operator; well-posedness of q-difference Cauchy problem; positivity of q-energy dissipation) FORCE nu_q, force another value, or leave it free. Anti-fit: do not pick the condition because it gives hbar_q/2. First observation: positivity of dissipation (energy_nonincreasing) only needs nu >= 0, so it leaves nu_q free (scope-(a) negative for that candidate).

2026-11-25T16:45Z: three QOU conditions tested (ViscosityRegularityRoutes.lean, PR #9434, sorry-free): dissipation positivity leaves nu free; explicit-step stability on unbounded ladder forces nu=0; Habiro integrality EXCLUDES nu_q=hbar_q/2 (at q=i, (1+i)/2 not in Z[i]; Habiro evaluation property cited). All scope (a). Remaining: Lean BKLS §4 statement in their setting (paper-faithful) — needs a metric/ODE model, not started; content block.
