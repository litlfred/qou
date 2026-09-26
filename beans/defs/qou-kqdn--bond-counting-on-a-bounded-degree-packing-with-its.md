---
# qou-kqdn
title: 'Boundary deficit of a bounded-degree bond count: does it produce the SEMF surface term, and how sharp is the parameter-free magnitude?'
status: completed
type: task
priority: normal
created_at: 2026-09-05T07:15:37Z
updated_at: 2026-09-05T08:10:23Z
---

Branch claude/coordination-surface-deficit-2026-09-05. Follow-on to qou-yau0 (#6690), which re-promoted the surface term (corr −0.298 on the artifact-free law, SEMF projection R² = 0.96).

CORPUS-GREP FIRST (6 paths; path 0 unavailable — paper-assistant MCP failed to connect, so a differently-worded prior approach could have been missed). The boundary-deficit bond count is OPEN: proposed 2026-05-02 (level-1-binding-energy-probe §Term 2, 'Status. Not currently implemented'), re-proposed 2026-09-04 (decision frame Avenue 2), never built, never refuted. Four nearby closures checked, none reaches it: bounded_degree_saturates is the c=0 special case; ChainBondOrderDependence PRESCRIBES this repair; the 2026-06-10 audit bounds integer multisets at A≤4; UniformBondSimpleGraphExclusion.b3Uniform_nonpos DOES bite and forbids claiming this explains b₃>0. Distinguished from av_surface_correction_probe (different baseline law, a_V·A at the net scale, double-counts).

LEAN QOU/Mass/CoordinationSurfaceDeficit.lean (sorry-free, 6 decls axiom-clean): bondCount_split (M = kA/2 − (k−k')A_surf/2), perNucleon_split, perNucleon_surfaceLaw (under A_surf = c·A^{2/3}: B/A = εk/2 − (εc(k−k')/2)A^{−1/3}, the SEMF volume-minus-surface shape), perNucleon_lt_plateau (approach from BELOW), perNucleon_tendsto_plateau (recovers bounded_degree_saturates as the limit — refines, does not contradict), surfaceToVolume_ratio (a_S/a_V = c(k−k')/k: ε AND k both cancel, only the fractional loss 1−k'/k survives).

PROBE coordination_surface_deficit_probe.py, 12/12, 50 dps, 2548 AME nuclides. Data full-SEMF basis |a_S/a_V| = 0.9607 (R² 0.964); textbook 1.130. Falsification check passes: median B/A rises 6.03 → 8.01 → 8.55 over A ≤ 62 then turns over (Coulomb, out of scope).

HEADLINE IS A NEGATIVE AGAINST MY OWN MAGNITUDE CLAIM. fcc(100) leading order gives exactly 1.00 vs measured 0.96 — and that is the move qou-rav3 forbids. My ratio IS k-independent so the guard does not apply verbatim, but I applied its METHOD to my own quantity: 3 facets × 2 shell treatments reach 0.571..1.250 = 67.9 % of the plausible window [0.5,1.5], against the guard's own 73.7 %. SAME FAILURE MODE. So the magnitude is a consistency check, NOT a prediction, and the fcc(100) coincidence must not be quoted as support for close packing.

WHAT SURVIVES: the shape, cleanly and choice-free — A^{−1/3} form, SEMF sign, approach from below, A→∞ saturation recovery. Avenue 2 is NOT closed (it wants the edge set from the braid geometry; this assumes a packing) but its question is sharpened to a single k-free number: what fixes 1 − k'/k? Recommendation (judgement): attack that from the braid side; it is immune to the qou-rav3 inversion trap by construction, and a negative would close Avenue 2. Audit: docs/audits/2026-09-05-coordination-surface-deficit.md. Nothing wired, nothing fitted.



**Follow-on landed 2026-09-05 (qou-glji).** §6's recommendation was to attack `1 - k'/k` from the braid side. The other half of the split was taken instead — the surface EXPONENT rather than the amplitude. Result: the production chain's p = 1 is rejected by the AME chart at every analysis choice (RSS 147.0 vs 38.2), but the inverse-dimension reading p = 1/d is NOT established (the fitted exponent drifts 0.364 -> 0.582 with the mass cut, disjoint 1 %-RSS intervals). Genericity of the exponent by the same self-applied qou-rav3 method: 17.66 %, against this bean's 67.9 %. See `docs/audits/2026-09-05-surface-exponent-is-dimension.md`.
