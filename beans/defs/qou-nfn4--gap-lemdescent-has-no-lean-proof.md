---
# qou-nfn4
title: 'GAP: lem:descent has no Lean proof'
status: in-progress
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:20:31Z
updated_at: 2026-11-22T10:53:09Z
parent: qou-uwyf
---

lifting-and-descent/descent-lemma.lean defines the predicate descent_surjective and proves composition and a counterexample, but nothing states or proves that the descent homomorphism End(A_n) -> End(A_{n-1}) is surjective. The ref now points at the predicate (PR #8977). State the lemma and prove it, or queue it with sorry + Ref.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.


2026-11-22 (branch claude/honest-lean-descent-reidemeister-schurweyl-2026-11-22, commit 1420e8fb9): descent-lemma.lean now proves, from r ∘ ℓ = id alone: descentCompression_surjective (φ ↦ r∘φ∘ℓ surjective linear) and descentHom_surjective (surjective algebra hom on the subalgebra commuting with e = ℓ∘r). It also proves the .md wording does not follow: descentCompression_not_multiplicative (ℤ×ℤ counterexample) and not_surjective_matrix_algHom (no surjective algebra map M_k → M_j over a field, 0<j<k). Proof Step 4 shows r_n onto, not 𝔡_n. Open: owner decision on the .md wording; repoint lean.ref to QOU.descentHom_surjective after #8977 merges.


## 2026-11-22 progress (PR #8999, 987570e0e)
Proved in descent-lemma.lean (lean-verify exit 0, axioms propext/Quot.sound/Classical.choice): descent surjective linear on End; surjective algebra hom on the commutant of e_n = ℓr (descentHom_surjective); not multiplicative on all End; no surjective M_k(K)→M_j(K), 0<j<k; Hopf adjoint-action equivariance of r, ℓ derived from Hopf-morphism equations and intertwining of induced actions; archimedean surjective StarAlgHom in a Hilbert-space model (ℓ isometry, r = ℓ†); tower corollary.
STILL OPEN (keep this bean open): (1) J¹(A) is not defined in Lean, and the claim that restriction yields a Frobenius-Hopf object with (C, A_{n-1}, τ) again a QuantumObservableUniverse (proof Steps 1-3) is unformalised; (2) the identification of Γ(J¹S_n, SU_q(2)) with the Hilbert-space operator algebras (the functor τ) is unformalised.
