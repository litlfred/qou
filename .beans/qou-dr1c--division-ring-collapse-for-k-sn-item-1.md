---
# qou-dr1c
title: 'division-ring collapse for k[S_n] (residual item 1 of sn_isotypic_specht_split)'
status: todo
type: task
created_at: 2026-08-10T03:55:00Z
updated_at: 2026-08-10T03:55:00Z
---

Residual item 1 from PR #4876: prove the Wedderburn division rings of `k[S_n]`
collapse, `𝔇 i ≃ R`, for a characteristic-zero field.

Scoped 2026-08-10 —
`docs/audits/2026-08-10-sn-division-ring-collapse-scoping.md`. The item is
cheaper than the residual list implies, and less independent of item 2.

Already owned, sorry-free (verified by `#print axioms`):
- `SpechtIrreducible.specht_isSimple` — S^μ simple over an ARBITRARY char-0
  field, which is the absolute-irreducibility input, not just the ℚ/ℂ case.
- `SpechtBaseChange` — Specht data defined over ℤ functorially; span transfer.

Genuinely remaining:
1. tensor comparison `S^μ_k ⊗_k K ≅ S^μ_K` as K[S_n]-modules;
2. bijectivity of `Module.End.baseChangeHom` for f.d. modules — Mathlib has
   the algebra hom only, no bijectivity lemma; this is the load-bearing step;
3. linkage `𝔇 i ≃ End(S_i)ᵒᵖ` from Wedderburn's existential — shared with
   items 2 and 3, so those three are coupled, not separable.

Preferred route: build `k[S_n] ≃ₐ[k] ∏_λ Matrix (d_λ) k` directly from the
Specht modules, which never introduces the opaque `𝔇 i` and folds items 1-3
into one construction.

Mathlib has nothing upstream (all 6990 modules scanned): 0 for `Specht`,
`AbsolutelyIrreducible`, `SchurIndex`, `numSYT`.
