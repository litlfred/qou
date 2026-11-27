import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# QOU.BraidKnot.e_infinity_identifications

**§3b-cond conditional canonical** for content block
[`prop:e-infinity-page-identifications`](../../../quantum-observable-universe/braids-and-knots/e-infinity-page-identifications.md): *QOU.BraidKnot.e_infinity_identifications*.

The six `E_∞^{p,*}` page identifications are axiomatised as fields of
`EInfinityIdentificationsContext` (§3b-cond); the `def`
`e_infinity_identifications` then *derives* the six-term conjunction
from those fields, conditional on `[EInfinityIdentificationsContext]`.
It is therefore sorry-free at this file's level — the conjectural
content sits in the class fields (a concrete instance discharges
`claim_wenzl_bridge_correction_holds` etc. by `sorry`). The `lean.ref`
URI `qou:QOU.BraidKnot.e_infinity_identifications` resolves here.
-/

namespace QOU.BraidKnot


/-- Abstract context for the `e_infinity_identifications` claim —
    manuscript-themed typed fields below; sub-claims encode the six
    `E_∞^{p,*}` page identifications corresponding to the six mass-
    formula terms of `thm:knot-mass-formula-unified`. -/
class EInfinityIdentificationsContext (wenzlBridgeCorrection : Prop) where
  /-- Total mass `m(ϱ)`. -/
  m_total : ℝ
  /-- Per-page contribution `<tr_M, E_∞^{p, *}(T_w)>`. -/
  page_pairing : ℕ → ℝ
  /-- Number of pages in the finite truncation used to compute
      `m_total`. -/
  n_pages : ℕ
  /-- Ribbon-closure contribution `<tr_M ∘ (id ⊗ Θ), E_∞^{0, *}(T_w)>`. -/
  ribbon_closure : ℝ
  /-- Frobenius co-Casimir contribution `m_e · τ(C_{dim_q})`. -/
  frobenius_co_casimir : ℝ
  /-- Manuscript master identity:
      `m(ϱ) = Σ_p <tr_M, E_∞^{p,*}> + ribbon_closure + frobenius_co_casimir`. -/
  claim_mass_formula_unified :
    m_total = (Finset.range n_pages).sum (fun p => page_pairing p) +
              ribbon_closure + frobenius_co_casimir
  /-- Manuscript term 1 (DERIVED) — descended `|tr_M(T_w)|`
      identification with `E_∞^{0, *}` (encoded as the explicit value
      of `page_pairing 0`, which equals `|tr_M(T_w)|`). -/
  trM_T_w_abs : ℝ
  claim_descended : page_pairing 0 = trM_T_w_abs
  /-- Number of brane indices `i` in the single-generator brane tower. -/
  n_branes : ℕ
  /-- Single-generator brane contribution `Φ_q(|V̂_i|)` at index `i`. -/
  brane_pairing : ℕ → ℝ
  /-- Manuscript term 2 — single-generator brane tower identification:
      `<tr_M, E_∞^{1, *}> = Σ_i Φ_q(|V̂_i|)`. -/
  claim_brane_tower_single :
    page_pairing 1 = (Finset.range n_branes).sum (fun i => brane_pairing i)
  /-- Pairwise-product brane contribution `Φ_q(|V̂_i| · |V̂_j|)`. -/
  brane_pairwise : ℕ → ℕ → ℝ
  /-- Manuscript term 3 — pairwise-product brane tower identification:
      `<tr_M, E_∞^{2, *}> = Σ_{i,j} Φ_q(|V̂_i| · |V̂_j|)`. -/
  claim_brane_tower_pairwise :
    page_pairing 2 = (Finset.range n_branes).sum (fun i =>
      (Finset.range n_branes).sum (fun j => brane_pairwise i j))
  /- Manuscript term 4 (DERIVED) — Frobenius co-Casimir is the
     designated `frobenius_co_casimir` field. (No additional Prop
     needed: the identification IS the field.) This is a plain
     comment, not a field docstring: term 4 introduces no new field. -/
  /-- Chirality / sign factor of the mass-formula term 5 (must be ±1). -/
  chirality_sign : ℤ
  /-- Manuscript term 5 — chirality / sign factor: `chirality_sign ∈ {±1}`. -/
  claim_chirality_sign : chirality_sign = 1 ∨ chirality_sign = -1
  /-- Witness for manuscript term 6 — the Wenzl-bridge `y_λ` correction.

      **Parameterised 2026-09-13.**  This was `claim_wenzl_bridge_correction
      : Prop` plus a witness of it: a field typed with the *universe* `Prop`,
      so the instance chose the proposition and `⟨True, trivial⟩` discharged
      the pair, leaving term 6 of `e_infinity_identifications` unconditional.
      As a parameter the proposition is fixed by the binder and visible in
      every consumer's type.  The conjecture is untouched and still open. -/
  claim_wenzl_bridge_correction_holds : wenzlBridgeCorrection

/-- **Chirality sign involutivity (proved):** since `chirality_sign ∈ {1, -1}`,
    its square is identically `1`. -/
theorem e_infinity_chirality_sq_eq_one {wenzlBridgeCorrection : Prop}
    [ctx : EInfinityIdentificationsContext wenzlBridgeCorrection] :
    ctx.chirality_sign ^ 2 = 1 := by
  rcases ctx.claim_chirality_sign with h | h <;> rw [h] <;> ring

/-- **Content statement** (from manuscript):

Having established the GB spectral sequence exists and converges
([GB spectral sequence](#prop:gb-spectral-sequence)), the remaining
task is to **identify** each $E_\infty^{p, *}$ page with a specific
mass-formula term from
([unified knot mass](#thm:knot-mass-formula-unified)).  This
proposition attempts that identification for all six terms, marking
derivation status per term.

    **Assumed, not derived here:** the six `E_∞^{p,*}` page identifications are
    carried as fields of `[EInfinityIdentificationsContext wenzlBridgeCorrection]`;
    `def e_infinity_identifications` bundles their six-term conjunction together
    with the derived involutivity `ctx.chirality_sign ^ 2 = 1` as the `lean.ref`
    entry point, while `e_infinity_first_three_pages_sum` below proves the
    3-page truncation expansion from those fields (bean `qou-bvo3`). -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/e-infinity-page-identifications.ts
def e_infinity_identifications {wenzlBridgeCorrection : Prop}
    [ctx : EInfinityIdentificationsContext wenzlBridgeCorrection] :
    ctx.m_total =
      (Finset.range ctx.n_pages).sum (fun p => ctx.page_pairing p) +
      ctx.ribbon_closure + ctx.frobenius_co_casimir ∧
    ctx.page_pairing 0 = ctx.trM_T_w_abs ∧
    (ctx.page_pairing 1 =
      (Finset.range ctx.n_branes).sum (fun i => ctx.brane_pairing i)) ∧
    (ctx.page_pairing 2 =
      (Finset.range ctx.n_branes).sum (fun i =>
        (Finset.range ctx.n_branes).sum (fun j => ctx.brane_pairwise i j))) ∧
    (ctx.chirality_sign = 1 ∨ ctx.chirality_sign = -1) ∧
    ctx.chirality_sign ^ 2 = 1 ∧
    wenzlBridgeCorrection := by
  exact ⟨ctx.claim_mass_formula_unified, ctx.claim_descended,
   ctx.claim_brane_tower_single, ctx.claim_brane_tower_pairwise,
   ctx.claim_chirality_sign, e_infinity_chirality_sq_eq_one,
   ctx.claim_wenzl_bridge_correction_holds⟩

/-- **Three-page truncation expansion (proved):** when `n_pages = 3`, combining
    `claim_mass_formula_unified` with the page-0, page-1, and page-2
    identifications expands `m_total` explicitly in terms of `trM_T_w_abs`,
    the single-generator brane sum, the pairwise brane sum, `ribbon_closure`,
    and `frobenius_co_casimir`. -/
theorem e_infinity_first_three_pages_sum {wenzlBridgeCorrection : Prop}
    [ctx : EInfinityIdentificationsContext wenzlBridgeCorrection]
    (h_pages : ctx.n_pages = 3) :
    ctx.m_total =
      ctx.trM_T_w_abs +
      (Finset.range ctx.n_branes).sum (fun i => ctx.brane_pairing i) +
      (Finset.range ctx.n_branes).sum (fun i =>
        (Finset.range ctx.n_branes).sum (fun j => ctx.brane_pairwise i j)) +
      ctx.ribbon_closure + ctx.frobenius_co_casimir := by
  have hm := ctx.claim_mass_formula_unified
  rw [h_pages] at hm
  rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_one] at hm
  rw [ctx.claim_descended, ctx.claim_brane_tower_single, ctx.claim_brane_tower_pairwise] at hm
  linarith

end QOU.BraidKnot
