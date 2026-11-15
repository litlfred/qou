---
# qou-g0jn
title: 'GAP: beta-decay rate law — μ₀, |M_q|², f(Q) underived; no trigger/probability mechanism; no SDP→rate link'
status: todo
type: task
priority: normal
created_at: 2026-11-15T19:00:22Z
updated_at: 2026-11-15T19:38:28Z
---

Opened 2026-11-15 from owner question on a decay trigger and translating ILP/SDP likelihood into a rate; owner chose 'bean both gaps, then probe'. prop:hadron-half-life: Γ_β = |W|²μ₀/(2π³)·[2]_q·|M_q|²·f(Q). W(q) has a D closed form (qou-egvf); μ₀, |M_q|² (prop:trace-ratio-observable, proportionality only) and f(Q) do not. def:beta-decay-skein says WHAT, not WHEN. LP/SDP shadow prices are used only for shell binding from measured Q-values. Candidate to test, pre-registered: per-step probability = trace weight of the channel where the insertion reduces to the daughter. half-life-as-q-probe states environmental predictions (neutron-star q ≫ q₀; 1e-9 per metre) with no derivation — scope (a). Neutron lifetime not derived.



## 2026-11-15 pre-registration blocked by qou-0whz C3 (PR #7968)
The planned probe was 'per-step decay probability = trace weight of the channel where the T(3,5) insertion reduces to the daughter'. C3 shows that insertion can never reduce to daughter ⊔ T(2,3) ⊔ unknot (≤3 components vs ≥5). So the 'channel' has no definition yet, and building one now would be a choice made against the target. The probe waits until a strand-creating W morphism (E/F ⊗ coevaluation) is defined. Then the channel weight is the trace of that morphism's image, fixed before any comparison with τ_n.


## PRE-REGISTRATION 2026-11-15 19:35Z (owner card: 'Probe both, compare'), written before any computing
Question Q (same for both arms): applied to the neutron state (labels udd, with u = the K = q vector, as derived in #7971), does the map give a component proton-labels (uud) ⊗ X, where X has weight T³ = -1 (W⁻ quantum numbers)? Report the coefficient as an exact function of q, for each variant. No target value; CODATA/PDG are not used. A nonzero coefficient means 'allowed', not 'rate'.
Arm A, strand/categorical: maps built from the braiding and coev (U_q intertwiners). Concretely V -> V ⊗ (V ⊗ V*) by coev, then one crossing of the incoming strand with the created V. Variants: crossing sign ±; coev plain Σ e_i⊗e^i or pivotal Σ K e_i⊗e^i; both R conventions.
Arm B, 𝓗_q substrate Δ, read as deconcatenation of braid words (q-shuffle Hopf algebra, notation register table 4). This reading is an assumption, flagged. Test words: s1^4, (s1 s2)^5, s1 s2 s1. Each tensor factor of Δ(w) acts on the same 3 strands.
Prediction made in advance, stated before computing: Arm B coefficient = 0 for every word, by C2 (letters preserve weight). Arm A: nonzero only through the transposition term. Either outcome gets reported.


RESULT 2026-11-15 (PR #7973, d4ba09a0b0). Arm A gives a W⁻ coefficient of 1 (plain coev) or q (pivotal). It is the same for both signs and both R conventions, and comes from the transposition term, so no strand changes flavour: this is quark rearrangement, a d ū pair with π⁻ and W⁻ quantum numbers. It carries no chirality or weak suppression, so no rate. Arm B (deconcatenation, an assumed reading) gives 0, as predicted. Next: the flavour-changing E/F vertex (left projector) that composes with the arm A split. Bean stays open.
