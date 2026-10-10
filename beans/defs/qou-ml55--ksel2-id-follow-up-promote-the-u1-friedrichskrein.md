---
# qou-ml55
title: 'KSEL2-ID follow-up: promote the u≡1 Friedrichs/Krein alignment from measured to derived/certified'
status: completed
type: task
priority: normal
created_at: 2026-08-01T15:14:17Z
updated_at: 2026-08-01T17:55:50Z
---

DONE (agent work complete; human closes). Probe computations/probes/ksel2id_u1_promotion_probe.py exit 0 (5 assertion blocks) + witness ksel2id-u1-promotion.witness.json + audit docs/audits/2026-08-01-ksel2id-u1-promotion.md. Results: (LEG A) SW Jacobi closed form EXACT; D(z)=c0 z A_pt(z) Ramanujan identification (6.5e-23); Krein=zeros(A_pt), Friedrichs=zeros(A_pt)/qt (1.7e-8/1.2e-8); SW class = integer lattice 0, K odd / F even; transfer m_k = G_k E^k (p;p)_k EXACT; balanced Jacobi -> E-scaled SW at rate pt => phi_1 = Jackson-edge image of SW class 0 (derivation-shaped modulo one perturbation lemma — open gap). (LEG B) r=6/5 alignment promoted 2e-4 -> 8e-10; ladder certified to q=1.5, measured-preasymptotic 1.3/1.2/1.15 (consistent within unc); pins: SW core CERTIFIED truncation-free (Aitken^2 -8.2e-8), balanced pre-asymptotic, N~375 required (successor-probe target). No fits, nothing wired, no content/Lean edits. Parent session commits.
