---
# qou-nfn4
title: 'GAP: lem:descent has no Lean proof'
status: in-progress
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:20:31Z
updated_at: 2026-11-22T09:51:30Z
parent: qou-uwyf
---

lifting-and-descent/descent-lemma.lean defines the predicate descent_surjective and proves composition and a counterexample, but nothing states or proves that the descent homomorphism End(A_n) -> End(A_{n-1}) is surjective. The ref now points at the predicate (PR #8977). State the lemma and prove it, or queue it with sorry + Ref.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.


2026-11-22 (branch claude/honest-lean-descent-reidemeister-schurweyl-2026-11-22, commit 1420e8fb9): descent-lemma.lean now proves, from r ∘ ℓ = id alone: descentCompression_surjective (φ ↦ r∘φ∘ℓ surjective linear) and descentHom_surjective (surjective algebra hom on the subalgebra commuting with e = ℓ∘r). It also proves the .md wording does not follow: descentCompression_not_multiplicative (ℤ×ℤ counterexample) and not_surjective_matrix_algHom (no surjective algebra map M_k → M_j over a field, 0<j<k). Proof Step 4 shows r_n onto, not 𝔡_n. Open: owner decision on the .md wording; repoint lean.ref to QOU.descentHom_surjective after #8977 merges.
