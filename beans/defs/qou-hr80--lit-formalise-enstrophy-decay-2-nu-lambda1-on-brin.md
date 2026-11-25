---
# qou-hr80
title: 'Lit-formalise: enstrophy decay >= 2 nu lambda1 on Bring (prove gap 5-sqrt5 in Lean) as content block'
status: todo
type: task
priority: normal
created_at: 2026-11-25T16:27:37Z
updated_at: 2026-11-25T16:27:55Z
parent: qou-i6e2
---

Owner (2026-11-25): 'bean up to lean formalize and add'; desired = author request (case a). Process per owner: (1) Lean the paper statement faithfully, proof as template; (2) round-trip verdict on statement+result; (3) general QOU q-NS statement as separate declaration, general→paper where possible; (4) staged conjectures with attempt log; (5) provenance in narrative and formally. Done when: sorry-free Lean or honest conjecture carrier + validated content block. Base: QOU/FluidDynamics/DECNavierStokes.lean (PR #9434), audit docs/audits/2026-11-25-qns-literature-formalisation.md.

RESUME STATE 2026-11-25T16:30Z: conditional lemma enstrophy_decay_of_spectral_gap proved (PR #9434). NEXT: build the Bring {5,4} complex in Lean (24x24 integer d1, reuse BringRegularMap.lean from #9430) and prove hgap with lambda=5-sqrt5 (PSD certificate), then content block. BLOCKERS: #9430 not merged. ROUTE: exact charpoly from computations/probes/bring54_cochain_complex_probe.py (#9428).
