---
# qou-a3n3
title: 'EPIC: Gevrey persistence — does the internal q-NS dynamics keep smooth data Gevrey as q→1⁺'
status: completed
type: milestone
priority: normal
created_at: 2026-07-25T03:32:00Z
updated_at: 2026-07-25T17:42:46Z
---

GP1 landed (PR #4193): discrete Gronwall + finite-rate horizon persistence. Epic stays OPEN — next bricks: GP2 rate improvement (does the q-damping [k]_q dissipation term cut Λ_q from ε⁻¹ to finite effective G — the analytic core), GP3 radius non-collapse (track the Gevrey radius r(t) itself, not just Ω).

GP1+GP2+GP3 all landed on PR #4193 (12 sorry-free theorems). Epic's tractable tranche COMPLETE: local persistence proved ε-free (bootstrap horizon ~1/(cΩ₀)); high modes damped (q-threshold); low modes bounded (quadratic bootstrap). Honest remainder = GLOBAL persistence past the bootstrap horizon at the finite-dim low-mode block (the classical local-vs-global gap, reproduced in-QOU). Epic stays open on that single named item.

SF1 landed: unforced DN q-shell (k_n=[n]_q) shows a TRANSITION — eps≥1e-3 decays, eps=1e-4 sustains 30 turnovers (Om_max/Om0~3.9 transient). Confound flagged (viscous time >> horizon at small eps). Next bean: SF2 discriminator — horizon scaled to viscous time + classical same-nu comparison; that decides whether the sustained channel truly activates as eps→0.

SF2 DISCRIMINATOR DECIDED: at T=1.5·t_visc the q-system tracks the classical same-ν control (R=0.565/0.947/0.995 for eps=1e-1/2/3, →1 as eps→0). SF1's small-eps sustainment was the viscous timescale, NOT q-self-forcing. The unforced finite core decays at every eps on its own clock ⇒ the sustained-forcing blow-up channel requires EXTERNAL or infinite-dimensional sustainment. Hard core sharpened again: no finite unforced structure in the program blows up, in-model. Remaining: infinite-dim sustainment analysis / PDE-uniformity / large-data global.

SF3 DECIDED: N-sweep (8..24) at eps=1e-2 — survival S_q DECREASES monotonically with N (1.35e-8→1.14e-9), R(N)~0.9. The infinite-dimensional escape does NOT open at the shell-model level; unforced decay is N-uniform (improves with N). In-model conclusion: the ONLY route to the sustained channel is EXTERNAL FORCING — but the Clay problem is unforced, so in-model the program now points to global regularity for all unforced channels examined. Remaining honest gaps: shell-model fidelity (DN is a caricature of full NS transfer — no backscatter/nonlocal interactions), PDE-uniformity, large-data global proof.
