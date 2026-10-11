---
# qou-uir6
title: Reconcile qou-za3q (Omega_2 Wenzl z_D ruling, 2026-09-13) with D7 full-tower binding
status: todo
type: task
priority: normal
created_at: 2026-10-11T07:23:25Z
updated_at: 2026-10-11T07:31:56Z
parent: qou-slz5
---

Owner 2026-10-11 asked to reconcile. The qou-za3q ruling adopted convention-D Wenzl weights for the Magnus Omega_2 binding pairing (Jones-Ocneanu characterisation; Plancherel refused). D7 (2026-09-07) puts binding on the full tower, and D is not faithful there (not_isFaithful_trLim). Faithful positive Markov traces are exactly z in [0, q-1/q] (FullTowerTraceWindow, #7612). Question: does the Omega_2 pairing belong to the decay channel (so D stands) or to binding (so it must move into the window)? Frame the options for the owner.


## 2026-10-11 corpus result (session_01ST9RpvTF7JHNdUNafrjf9J; paths 1-4 and 6; library and corpus_search not run)
- za3q (qou-za3q:522-526) adopted Wenzl z_D for P = Σ y_λ tr(ρ_λ Ω₂_λ). Its basis is Jones–Ocneanu: tr(1)=1, cyclicity, Markov stabilisation (qou-gba1:98-187). Its text never mentions D7, decay/binding or faithfulness, and it knowingly uses the r=2 row cap (qou-za3q:36).
- **Every author classifies Ω₂ as a BINDING correction** (probe titles, qou-gba1:21-23, qou-za3q:577). None calls it decay; the trace-convention registry has no Ω₂ row.
- **The za3q basis is z-generic.** Every Ocneanu weight is a z-Markov trace (FullTowerTraceWindow markov_ocneanuWeight / eq_ocneanu_of_markov). The 'pins z to 140 digits' control swapped only the scalar z under D weights, so it never compared against another Markov trace. The ruling correctly excludes Plancherel and is silent between z_D and the window.
- Blast radius: probes and beans only. No content block and no dashboard reads the Ω₂ witnesses.
- Ω₂ at z in [0,h]: NOT evaluated. P(z) is a polynomial in the weights (degree ≤ 3A); the per-λ traces are already in the three witnesses, so it is a cheap scan.
- Options: (i) classify as decay (contradicts every description); (ii) classify as binding and scan P(z) across the window; (iii) relabel the D results as a two-row/TL diagnostic. Agent judgement: (iii) plus the (ii) scan.
