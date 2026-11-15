---
# qou-0whz
title: 'GAP: W braid conflict — T(3,5) in def:beta-decay-skein vs T(2,4)=σ₁⁴ in weak-spectral-completeness'
status: in-progress
type: task
priority: normal
created_at: 2026-11-15T19:00:22Z
updated_at: 2026-11-15T19:09:34Z
---

Opened 2026-11-15 (thread 'Derive the left-projector weak vertex'; owner: 'bean to reconcile W braids. explore it now.'). Two blocks assign different braids to the W: def:beta-decay-skein inserts T(3,5)=(σ₁σ₂)⁵ at the converting d quark, reducing to daughter ⊔ T(2,3) ⊔ unknot; conj weak-spectral-completeness / thm:hoefsmit-ew-cell-content assign W ↔ σ₁⁴=T(2,4), W⁻ = alt block. Both are topological assignments, neither derived. Structural constraint (Schur–Weyl, level 2 / convention D): every Hecke element commutes with U_q(gl₂) incl. K, so NO braid word changes flavour; the flavour changer is E/F (matches g-action table W± on T±). So a W braid can only supply a vertex weight/amplitude. T(3,5) trace is not left-supported (−9.33 % at q₀, PR #7887). Open: what (if anything) each braid is, decided structurally — never by selecting against Q_β or τ_n. Do not close while open.



## 2026-11-15 exact probe (PR #7968, issue #7967, commit 502df04fea)
- C1: under D, Markov property forces K = q on the highest-weight vector of the Jimbo Ř (T³=+½); other orientation not Markov. Which quark sits there: open (needs link positive crossing ↔ K=q; see qou-q1a4).
- C2: σ₁, σ₂, T(3,5), σ₁⁴ commute with Δ(K),Δ(E),Δ(F) on (C²)^⊗3 → no braid word changes flavour; flavour changers are E/F.
- C3: 3-strand closure ≤ 3 components; p ⊔ T(2,3) ⊔ unknot ≥ 5 → def:beta-decay-skein reduction cannot be a link equality; lepton emission needs strand creation (coevaluation), not a braid.
Scope (a): excludes a braid as the W *process*, not as amplitude/form factor. Still open: which (if either) is the W form factor; what the W morphism is (E/F ⊗ creation?).
