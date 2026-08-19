---
# qou-q407
title: 'GAP: 8 self-assuming projections — ''theorem (h : P) : P := h'' asserts nothing'
status: todo
type: task
priority: high
tags:
    - lean
created_at: 2026-08-07T18:24:34Z
updated_at: 2026-08-19T20:59:59Z
---

Eight provable declarations have the shape 'theorem name ... (h : P) : P := h' — hypothesis identical to conclusion, proof term the identity. They assert nothing about the objects named, and stay true if every definition is swapped.

Found via the folio-assistant triviality probe (6/40 closed; 2 genuine, 4 legit decide/simp), then swept statically by scripts/lean-self-assuming-audit.py (2590 files, 4.5 s). Full analysis + quoted bodies: docs/audits/2026-08-07-self-assuming-projection-sweep.md

Findings (lines on main @ b48ce882fa):
1. defect_legendrian_knot — brings-surface/defect-legendrian-knot.lean:47
2. topological_charge_quantization — brings-surface/topological-charge-quantization.lean:43
3. fomin_identity — lean/QOU/Archimedean/BranchingConvergence.lean:138
4. fomin_identity_n3 — lean/QOU/Archimedean/BranchingConvergence.lean:152
5. length_bound_necessary — lean/QOU/BraidKnot/PSDFeasibilityProxy.lean:94
6. universal_ilp_selects_minimum — nuclear-interactions/universal-ilp-algorithm.lean:43
7. variational_transport — quantum-observable-universes/categorical-action.lean:109
8. ordering_extends — unital-groebner-bases/lean/UGB/GrobnerShirshov/JetOrder.lean:213

Why no existing gate caught them: no sorry, no axiom, no True conclusion, type-checks clean. AGENTS.md 3b-cond item 5 names the pattern; there was no detector.

NOT fixed in the detector PR — rewriting a theorem statement changes what the corpus claims. Per 1a the honest dispositions are prove / state-with-sorry+Ref / demote-to-conjecture, chosen per declaration. fomin_identity needs real SYT definitions rather than its uninterpreted dim_fn/mult_fn parameters.

Scope-(a): the Lean carries no content. NOT a claim the underlying math is wrong — Fomin's identity is a true theorem of the literature.

Follow-ups: wire as a proof-self-assuming criterion in content/pipeline/lean-vacuity-axiom-audit.ts; run the triviality probe corpus-wide to reach the ':= by exact h' variants the static pass cannot see.



## Re-verified 2026-08-19 (current main @ 5b158ef0)
Re-ran scripts/lean-self-assuming-audit.py: **all 8 still live** — none fixed in the 5-week gap. Same 8 decls, same lines (defect_legendrian_knot, topological_charge_quantization, fomin_identity, fomin_identity_n3, length_bound_necessary, universal_ilp_selects_minimum, variational_transport, ordering_extends). Ready to work; still the most concrete item in the vacuity arc.
