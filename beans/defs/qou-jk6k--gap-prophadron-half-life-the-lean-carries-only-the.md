---
# qou-jk6k
title: 'GAP: prop:hadron-half-life — the Lean carries only the q-prefactor shape; the Γ_β rate formula is unformalised'
status: completed
type: task
priority: normal
created_at: 2026-09-04T06:21:23Z
updated_at: 2026-09-04T10:46:29Z
---

Opened 2026-09-04 from docs/audits/2026-09-04-lean-ref-resolution-count-mass-theory.md (bean qou-jkam, PR #6554). The block's lean.ref RESOLVES, so no presence-keyed or sorry-keyed detector fires; the resolved declaration is not the block's claim. Honest next step: state the proposition as a real Lean statement (a theorem with sorry + -- Ref:, or the named-Prop carrier form the qou-z9ws drain uses), then derive what can be derived. Do not repoint the ref at a positivity or specialisation lemma — that swaps one non-claim for another (Correction 2 in the audit).



DONE 2026-09-04 (branch claude/hadron-half-life-rate-2026-09-04): the rate formula is in Lean. hadron-half-life.lean now carries BetaRateData (W2, mu0, M2, fQ as positive data — no closed form for any of them exists in the corpus: W(q) is a crossing budget only in beta-decay-skein.lean; M2 is trace-ratio-observable's product, in a content sibling not importable from the library; f(Q) is Sargent), betaRate = W2*mu0/(2π³)*[2]_q*M2*fQ, hadron_half_life d r = ln2/betaRate (replacing the alias def), betaRate_pos, hadron_half_life_pos, betaRate_eq_qPrefactor_iff (the legacy qPrefactor IS the formula with the four factors collapsed onto (q−1/q)^5 — iff), hadron_half_life_eq_halfLife, hasDerivAt_qPrefactor, qSensitivity_eq_logDeriv (the block's ∂lnΓ/∂lnq = (q²−1)/(q²+1)+5(q²+1)/(q²−1) is exactly q·Γ'/Γ of the q-shape), qSensitivity_near_48 (48 < S(1.1097) < 49 by norm_num). lean-direct exit 0, sorry-free. Still a GAP, one level down: W(q) = tr_M((σ1σ2)^5) in H_3(q) has no closed form in Lean; that is the next honest step, and it is the same object the 'open computation' N_v in rem:hadron-half-life-fermi needs.
