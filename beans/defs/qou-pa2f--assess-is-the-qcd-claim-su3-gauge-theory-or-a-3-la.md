---
# qou-pa2f
title: 'Assess: is the QCD claim SU(3) gauge theory or a 3-label colour index'
status: in-progress
type: task
priority: normal
tags:
    - 8f-decide
    - reorg-2026-10-04
created_at: 2026-09-14T18:08:47Z
updated_at: 2026-11-16T17:50:00Z
parent: qou-8lxd
---

## Cross-reference (`qou-q6lw`, PR `litlfred/qou#8140`, `468e210bfac6c8438bd4b6331f2fa807f91853e8`)

Companion Lean module `QOU/StandardModel/ColorVsCharmAdditiveSector.lean` and probe `computations/probes/charm_vs_color_sector_additive_term_probe.py` verify the 3-sheet color-tube sector (`(r, g, b)` spanning the 3-dim icosahedral irrep $T_1$ of $A_5 \cong I$, $T_1 \otimes T_1 = A \oplus T_1 \oplus H$) and its separation from discrete charge conjugation $C$ (`c-from-color-flavor-swap`) and heavy-meson flavor dressing (`Flavor.charm`). Kept `in-progress` pending owner decision (`Q-8LXD-1`).

MEASURED (subagent). NO SU(3): 'LieAlgebra' occurs ONCE in QOU code and it is sl(Fin 2) C; no gauge connection, no Yang-Mills functional (Glossary.lean:250 YangMillsFunctional = {manifold, energy : (manifold->R)->R, energy_nonneg}). 'Colour' = three S_3 subgroups of S_5 / polynomial variable names r,g,b on a cubic / a CIE chromaticity analogy. CONFINEMENT IS IMPOSED: ParticleKnots.lean:140 'confined : Bool := true'; up-quark.lean:49 'theorem up_quark_confined : ({} : UpQuark).confined = true := rfl'. The confinement SDP's Lean proves ONLY strong duality via 'exact hi.strong_duality', and the SAME FILE proves its Slater hypothesis freely dischargeable with PosDef := fun _ => True at Phi=0 (:245). The corpus itself proves the scalar LP is degenerate: optimum == 0, y_0* = 0, positive-dimensional minimiser face, 'downstream blocks have read the program as a selection principle, which it is not'. The Python producer is CIRCULAR: ranks candidates by |net - target_net| where target_net IS B3's own normal-form net (0.99912512524278...). NO beta function, NO running coupling, NO asymptotic freedom, NO Wilson loop, NO area law, NO string-tension value. Quark charges 2/3,-1/3 are hardcoded struct defaults that the corpus's OWN down-quark.md refutes (Q in (1/2)Z, cannot give thirds; neutral neutron forces all quark charges to vanish). Vol(B3)=8G matched to dim su(3)=8 is numerology AND load-bearing (produces the He-4 binding). Published binding table is a knot-census fit with a visible GAP at A=5,6,7 ('no census knot with Vol ~ B_AME/m_e found'); audit's own verdict: 'They are not predictions and should not be quoted as such.' WHAT IS REAL: GammaGammaSelectionTen.vertexPow_frobeniusFeasible_iff_three_dvd (Frobenius-feasible IFF 3|k for all 1<q<=23/20 -> selects k=3=beta_Bor by cost, on an INTERVAL not a point, sorry-free) and its consequence DiprotonResponseClosedForm (diproton unbound for every q>1, closed form, no measured input, right sign) — a genuine parameter-free prediction. Also ColourObstruction.lean PROVES the framework CANNOT have colour (real rep => 3 iso 3-bar). VERDICT: QCD is a vocabulary map; the one derived object is a braid word, not a colour structure.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
