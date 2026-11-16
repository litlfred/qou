---
# qou-hxzl
title: Add disclosure — 24 literature-cited projections (do NOT bulk-convert to axioms)
status: in-progress
type: task
priority: high
tags:
    - vacuity
    - issue-2472
    - reorg-2026-10-04
created_at: 2026-08-10T01:47:53Z
updated_at: 2026-11-16T19:22:00Z
parent: qou-6qbv
---

**24 declarations** carrying a non-`[manuscript]` `-- Ref:` directly above a verbatim class-field projection, with no disclosure.

Criterion (3) — *citations point at the claim's provenance, not at its proof*. This is the most misleading configuration available: it makes an assumed statement read as a result imported from a named source.

**Do NOT bulk-convert these to cited `axiom`s.** That was the original recipe and it is unsound wherever the class data is arbitrary: a global axiom over e.g. `RMatrixBraidingContext` (free `comp`, `R12`, `R13`, `R23`) asserts Yang–Baxter for *every* assignment of that data, which is false. It would swap an invisible-but-true hypothesis for a visible-but-false axiom. Six such cases were resolved by disclosure instead in PR #4882 (commit `b53fe380`); recipe 3 applies only where the content is a genuine external input **about fixed objects**.

5 of these are non-exempt after the `isDefProof` narrowing; 19 remain exempt.

- `folio/quantum-observable-universe/brings-surface/mi-sw-abelianisation.lean:53` — `sw_determines_mi`
- `folio/quantum-observable-universe/brings-surface/quaternionic-spectral-resolvents.lean:62` — `uncertainty_vanishes`
- `folio/quantum-observable-universe/climax-volume-mass/mobius-energy.lean:73` — `mobius_energy_nonneg`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/knot_operator_selection.lean:80` — `knot_operator_selection`
- `folio/quantum-observable-universe/lean/QOU/ArchimedeanUniverse.lean:136` — `descartes_universality`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/ElectronShell.lean:95` — `noble_gas_multi_operator`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/LpDualityHypothesisClass.lean:158` — `theorem_3_via_class`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/ShellClosureStability.lean:107` — `shell_closure_monotone`
- `folio/quantum-observable-universe/lean/QOU/ChannelSeparation.lean:96` — `adjoint_vanishing_propagation`
- `folio/quantum-observable-universe/lean/QOU/HadronicMass/pair_skein_mass_formula.lean:57` — `pair_skein_mass_formula`
- `folio/quantum-observable-universe/lean/QOU/MathlibExt/SDP.lean:169` — `strong_duality`
- `folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Propositions.lean:71` — `main_commutative_diagram`
- `folio/quantum-observable-universe/lifting-and-descent/ccg-cosimplicial-identities.lean:43` — `ccg_cosimplicial_identities`
- `folio/quantum-observable-universe/lifting-and-descent/ccg-crossed-module-structure.lean:35` — `ccg_crossed_module_structure`
- `folio/quantum-observable-universe/mass-endomorphism/conj-qbeta-c-k-closed-forms.lean:131` — `qbeta_c_k_closed_forms_derived`
- `folio/quantum-observable-universe/mass-theory/q-beta-bar-even-kernel-typeclass.lean:132` — `bar_even_kernel_implies_direction_sanity`
- `folio/quantum-observable-universe/mass-theory/q-beta-bar-even-kernel-typeclass.lean:122` — `bar_even_kernel_implies_q_one_shadow`
- `folio/quantum-observable-universe/mass-theory/q-beta-bar-even-kernel-typeclass.lean:105` — `bar_even_kernel_implies_radius_of_convergence`
- `folio/quantum-observable-universe/models-of-qous/main-commutative-diagram-proof.lean:63` — `main_commutative_diagram`
- `folio/quantum-observable-universe/braids-and-knots/r-matrix-braiding-structure.lean:108` — `braid_rep_from_R_check`
- `folio/quantum-observable-universe/braids-and-knots/r-matrix-braiding-structure.lean:86` — `r_matrix_braiding_structure`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/LevelSufficiency.lean:112` — `LevelSufficiency`
- `folio/quantum-observable-universe/lean/QOU/Braiding/r_matrix_braiding_structure.lean:59` — `r_matrix_braiding_structure`
- `folio/quantum-observable-universe/lean/QOU/Observations/AlgebraicGnsEmbedding.lean:89` — `markov_gns_embedding`

Criterion: `docs/audits/2026-08-09-honest-placeholder-criterion.md`

## Progress Update (2026-11-16 — Round 48, PR #8165)

- Audited all 24 literature-cited declarations and added the explicit criterion-(1)+(3) `**Assumed, not derived here**` context-class disclosures to `noble_gas_multi_operator` (`ElectronShell.lean`), `shell_closure_monotone` (`ShellClosureStability.lean`), `strong_duality` (`SDP.lean`), `bar_even_kernel_implies_radius_of_convergence`, and `bar_even_kernel_implies_direction_sanity` (`q-beta-bar-even-kernel-typeclass.lean`) without converting any conditional class projection to a global `axiom`.
- Opened PR `litlfred/qou#8165` (`cf010d07bb34f2e3118733212559b61ede4b8cc4`) with `ready-to-merge` + `release` labels.
