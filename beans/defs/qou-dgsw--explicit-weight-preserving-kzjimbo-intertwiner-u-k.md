---
# qou-dgsw
title: Explicit weight-preserving KZ→Jimbo intertwiner ⊕U_k; linear independence of Jones words in Pres
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T20:03:36Z
updated_at: 2026-10-12T20:08:45Z
parent: qou-xhci
---

**2026-10-12 — item (1) DONE, sorry-free.** New file `QOU/Mass/KohnoIntertwiner.lean`: block assembly `asm`/`asmUnit` of per-weight-space matrices (`WP_asm`, `res_asm`, `asm_mul`, `asm_one`, `eq_of_res_eq`, `asm_intertwines`); **`kz_jimbo_intertwiner`**: for every complex κ with q(κ) not a root of unity there is ONE unit U on V^{⊗(m+1)} with `WP U` (equivalently `∀ k, Commute (wproj _ k) U`, `WP_iff_commute_wproj`) and `U * kzHeckeC m c κ x = jimboRep _ _ m x * U` for all x. Corollaries by conjugation: `weighted_trace_eq_of_intertwiner`, `weighted_trace_kz_eq_jimbo_of_intertwiner`, `siteWeight_trace_kz_eq_jimbo_of_intertwiner`, `braidTrace_eq_kz_of_intertwiner` (same statement as KohnoWeighted.braidTrace_eq_kz). Verified: lean -DautoImplicit=false -s 65536 exit 0 against a shadow holding main's KohnoAssembly/KohnoWeighted; #print axioms = propext, Classical.choice, Quot.sound. Item (2) (Jones words independent in Pres) next.
