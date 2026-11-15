---
# qou-jgk6
title: 'PROVE(lean): knot_operator_selection — theorem knot_operator_selection [ctx : KnotOperatorSelectionContext] : ctx.tr_Phi = (Finse [cited manuscript,wenzl1990]'
status: todo
type: task
priority: normal
tags:
    - cited-sorry
    - paper-qou
    - repo-infra
    - cite-wenzl1990
    - reorg-2026-10-04
    - lean
created_at: 2026-08-01T23:31:01Z
updated_at: 2026-10-04T15:22:37Z
parent: qou-l2vh
---

**File:** `QOU/Archimedean/knot_operator_selection.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/Archimedean/knot_operator_selection.lean

### `knot_operator_selection`  —  line 85  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem knot_operator_selection [ctx : KnotOperatorSelectionContext] : ctx.tr_Phi = (Finset.range ctx.n_partitions).sum (fun l => ctx.tr_Phi_lambda l) ∧ ctx.action_pair = ctx.channel_sum ∧ ctx.pairing_kernel_dim = 0 ∧ (∀ Φ_alt : ctx.CategoricalObj → ctx.CategoricalObj, ctx.is_on_shell Φ_alt → ctx.ac`
- **Cited:** `[wenzl1990]`, `[manuscript]`, `[wenzl1990]`
  - [wenzl1990] Wenzl (1990), *Quantum groups and subfactors of type B, C, and D* — https://doi.org/10.1007/BF02097372
  - [manuscript] quantum-observable-universe/predicted-spectra/knot-operator-selection.md
- **Tractability:** Operator-selection LP identity over a context class (trace = block sum, kernel dim 0); repo compute/LP wiring, no pure Mathlib gap.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
