---
# qou-jgk6
title: 'PROVE(lean): knot_operator_selection — theorem knot_operator_selection [ctx : KnotOperatorSelectionContext] : ctx.tr_Phi = (Finse [cited manuscript,wenzl1990]'
status: in-progress
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
updated_at: 2026-11-18T07:49:45Z
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

## Round 83 Progress (PR #8392)
- Branch: `feat/round83-lambdasum-taupos-pairenergy-c1eval-nobranch-43c1`
- Commit 1 (code + probe): `e226ba66ce53cea91430549ce1efc48cd1eeef24`
- Commit 2 (witness): `17c21a76b062fd76e16d4f84b23687e02fc0050c` (`scriptSha256 = 0635fcc96bfd3bd66e7452f9553ce1314e6829b0b1a6b7202ea86d48b4b232a6`)
