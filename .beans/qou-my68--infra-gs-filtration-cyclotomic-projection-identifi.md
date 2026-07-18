---
# qou-my68
title: 'Infra: GS-filtration ↔ cyclotomic-projection identification (b3ix residual same_element)'
status: todo
type: task
priority: normal
tags:
    - alien-habiro
created_at: 2026-07-18T17:48:54Z
updated_at: 2026-07-18T17:48:54Z
parent: qou-89f9
---

The one open algebraic input of the b3ix §3b-cond wiring (HabiroGBSameElement, no instance): prove the Habiro cyclotomic construction and the GS residue-spectral construction yield the SAME element of Ẑ[q]. Route (formalize-first reduction): Habiro injectivity Ẑ[q]↪∏_ζ ℤ[ζ] (Habiro 2004) ⇒ same_element reduces to 'agree at every root of unity ζ_ℓ'; and cyclotomic_value_truncates already shows the value at ζ_N is a finite partial sum = the projection. So the residual is: GS graded trace tr_{M,ℓ} (prop:graded-markov-trace-from-gs-filtration) = cyclotomic projection to ℤ[q]/Φ_{n_ℓ} (prop:residue-at-root) at each ζ_ℓ. Genuinely multi-week (needs Hecke/GS-filtration + Habiro-ring infra, QOU.AlgebraicSubstrate). Deliverable this pass: read residue-at-root.lean + graded-trace-residue-split.lean, land the injectivity-reduction lemma if tractable, else scope the abstract framework. Files: gb-residue-spectral-sum.lean, residue-at-root.lean, graded-markov-trace-from-gs-filtration.md.
