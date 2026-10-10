---
# alyr
title: 'Analyze: SU_q(2) q-rotor Casimir E_I = (1/2θ)[I]_q[I+1]_q + E_0 vs QOU q-angular-momentum'
status: completed
type: task
priority: normal
created_at: 2026-07-06T04:46:39Z
updated_at: 2026-07-06T11:15:26Z
parent: 4lss
---

Heavy-nuclei rotational bands via SU_q(2) Casimir: E_I=(1/2θ)[I]_q[I+1]_q+E_0. QOU has climax-volume-mass/q-angular-momentum.lean + BraidKnot/CasimirShared.lean. Deliverable: check whether the q-Casimir spectrum is derivable from/consistent with QOU's Casimir; if so add proposition/remark linking; else site as comparison only. Watch: their q fitted to bands, ours is q₀.

PRIMARY SOURCE IN HAND: the owner-uploaded uploads/9605013v1.pdf IS the alyr paper (Minkov-Drenska-Raychev-Roussev-Bonatsos, nucl-th/9605013). Confirmed formula matches the bean exactly: E_I=(1/2θ)[I][I+1]+E_0. CRITICAL q-regime distinction for incorporation: their q=e^{iτ} is a PHASE (|q|=1) giving [I]=sin(τI)/sin(τ) (oscillatory); QOU q₀≈1.10998 is REAL >1 giving sinh-like [I]. Same Casimir formula, different analytic branch — a q-usage-watcher-level distinction. Their τ is fitted per band (one-band model). QOU already has def:q-angular-momentum=[j]_q[j+1]_q (real q). Assessment: the CASIMIR OPERATOR is shared structure (genuine); the rotational-band APPLICATION is fitted phenomenology in the phase-q branch => comparison-only unless a real-q₀ forward test is shown. Next: read alyr assessment into an audit doc + optional comparison remark.

## Resolution (2026-07-11)

Already satisfied. The comparison-only assessment recorded in this bean body
(shared Casimir operator = genuine; rotational-band application = fitted
phase-q phenomenology, so comparison-only) is **already written into the
corpus**: `observations/q-deformed-nuclear-models-comparison.md` §"SU_q(2)
rotor bands" cites `minkov1996`, states the Casimir E_I=[I]_q[I+1]_q/(2θ)+E_0,
and gives the exact q-regime distinction — their q=e^{iφ} phase (|q|=1,
oscillatory) fitted per band vs QOU real q_0>1 hyperbolic — closing with
"We share the Casimir operator, but avoid the fitted phase." No new block
needed (would duplicate). def:q-angular-momentum is the QOU-side Casimir the
section already cross-refs.
