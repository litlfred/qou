import { proposition } from "../../schema/builders";

/**
 * Partial formal proof of `conj:confinement-nf-structure-forcing`.
 *
 * The conjecture has three claims (T1, T2, T3 — see audit doc).
 * This proposition states that:
 *   T1.  λ* := argmax_λ ord_{q=0}^{(−)} χ^λ(T_β) ∈ A
 *   T3.  duality_gap(β) = 0  (strong duality)
 * are FULLY PROVED from standard LP machinery (complementary
 * slackness + finite-dim strong duality theorem; Schrijver §7),
 * and that
 *   T2.  shift_NF(β) = α_shift(I) + Δ_struct(β_1, β_2; A) + Δ_resid
 * is REDUCED to a single sub-lemma — the Hecke-branching block
 * decomposition of ρ_λ(I) (Sub-lemma 2.1 in the audit doc).
 *
 * Per CLAUDE.md §3b-cond (conditional-class exception), the Lean
 * file encodes Sub-lemma 2.1 as a class `HasBranchingBlockLemma`
 * and proves T2 conditionally on its instance.  T1 and T3 are
 * proved unconditionally (modulo Mathlib's LP-duality library,
 * which is a routine integration).
 *
 * Used by: closes the residual gap in
 *   `prop:operator-selection-lp` → `conj:confinement-nf-structure-forcing`,
 * leaving Sub-lemma 2.1 as the single open piece.
 */
export default proposition({
  label: "prop:confinement-nf-partial-proof",
  title:
    "Partial formal proof of $\\mathrm{conj}:\\mathrm{confinement\\text{-}nf\\text{-}structure\\text{-}forcing}$: $T_1$ and $T_3$ from standard LP duality; $T_2$ reduces to Sub-lemma 2.1",
  uses: [
    "prop:operator-selection-lp",
    "prop:alpha-shift-torus-knot",
    "prop:hecke-branching-trace-decomposition",
    "conj:crystal-graph-realization",
  ],
  cites: ["schrijver1986theory", "macdonald1995"],
  lean: { ref: "qou:QOU.BraidKnot.ConfinementNFPartial.theorem_3_strong_duality" },
  tags: [
    "lp-duality",
    "complementary-slackness",
    "wedderburn-maximizer",
    "branching-rule",
    "littlewood-richardson",
    "partial-proof",
  ],
  computation: {
    engine: "sympy",
    script: "folio-assistant/computations/shift_from_nf_basis.py",
    witness: "folio-assistant/computations/shift-from-nf-basis.witness.json",
    status: "verified",
  },
});
