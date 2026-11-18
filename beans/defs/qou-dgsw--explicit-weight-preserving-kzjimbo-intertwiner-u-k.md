---
# qou-dgsw
title: Explicit weight-preserving KZ→Jimbo intertwiner ⊕U_k; linear independence of Jones words in Pres
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T20:03:36Z
updated_at: 2026-11-18T07:46:25Z
parent: qou-59vq
---

**2026-10-12 — item (1) DONE, sorry-free.** New file `QOU/Mass/KohnoIntertwiner.lean`: block assembly `asm`/`asmUnit` of per-weight-space matrices (`WP_asm`, `res_asm`, `asm_mul`, `asm_one`, `eq_of_res_eq`, `asm_intertwines`); **`kz_jimbo_intertwiner`**: for every complex κ with q(κ) not a root of unity there is ONE unit U on V^{⊗(m+1)} with `WP U` (equivalently `∀ k, Commute (wproj _ k) U`, `WP_iff_commute_wproj`) and `U * kzHeckeC m c κ x = jimboRep _ _ m x * U` for all x. Corollaries by conjugation: `weighted_trace_eq_of_intertwiner`, `weighted_trace_kz_eq_jimbo_of_intertwiner`, `siteWeight_trace_kz_eq_jimbo_of_intertwiner`, `braidTrace_eq_kz_of_intertwiner` (same statement as KohnoWeighted.braidTrace_eq_kz). Verified: lean -DautoImplicit=false -s 65536 exit 0 against a shadow holding main's KohnoAssembly/KohnoWeighted; #print axioms = propext, Classical.choice, Quot.sound. Item (2) (Jones words independent in Pres) next.

**2026-10-12 — Jones normal words are linearly independent in Pres (sorry-free).** New file `QOU/IwahoriHecke/JonesWordsIndependent.lean`: `presEquivHecke : Pres N (q-qi) (q*qi) ≃ₐ[R] QOU.SchurWeyl.Hecke R q qi N` (same presentation, generator to generator; any CommRing R, any q qi); `presBasis` (via `HeckeCoset.stdBasisAny`, regular rep); `card_words_pres`: exactly (N+1)! distinct normal words; `words_pres_linearIndependent` and `wordsBasis` (words are a basis), `words_pres_linearIndependent_of_le` (every level n ≤ N). Hypotheses: [CommRing R] [Nontrivial R]; quadratic of the form s²=(q−qi)s+q·qi — covers convention D (qi=q⁻¹) and the unbalanced (qi=1) relation. NOT covered: a general pair (a,b) not of that form. Proof: span + rank condition gives |words| ≥ (N+1)!, with card_words_le equality; surjective endomorphism of R^{words} injective (OrzechProperty). Verified lean -DautoImplicit=false -s 65536 exit 0; #print axioms = propext, Classical.choice, Quot.sound. The remaining q425 items (closed Rosso–Jones for general r) are untouched. Item (2) of this bean is DONE.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `qou-xhci` → `qou-59vq`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

- Round 72 (`lane-e667`): Formalized `qou-sx5r`, `qou-slck`, `qou-dgsw`, `qou-jfr8`, `qou-zoyv` in `QOU.Foundations.SandwichTraceCyclicityVectorBraidingReducedWordSeparationRibbonMonodromy` with 80-dps `mpmath` 2-commit witness stamp (`c95261a9c444144dd0cc07d50ddaabb0b496a13f` -> `c3e4ad1f706f5fd2e70cbb90c8c9bd7753ec1e10`, `scriptHash=e347a9e84468088888c8978781442fc5eb1e2e281357cbff708b7491a3fcbcb8`) in PR `litlfred/qou#8390` (`status: in-progress`).
