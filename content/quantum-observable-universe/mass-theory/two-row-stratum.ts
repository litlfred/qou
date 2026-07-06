import { definition } from "../../schema/builders";

/**
 * Two-row Wedderburn stratum of the Hecke algebra H_n(q).
 *
 * Let n = 3A be the strand count of an A-nucleon atomic braid. The
 * Wedderburn decomposition H_n(q) ≅ ⊕_{λ ⊢ n} End(V_λ) splits the
 * Markov trace into per-partition contributions:
 *
 *   tr_M(β) = Σ_{λ ⊢ n} y_λ(q) · χ^λ_q(β).
 *
 * The **two-row stratum** is the subset of partitions with at most
 * two parts:
 *
 *   Λ²(n) := { λ ⊢ n : ℓ(λ) ≤ 2 } = { (n-k, k) : 0 ≤ k ≤ ⌊n/2⌋ }.
 *
 * This stratum carries the SU(2) Schur-Weyl image — partitions
 * outside Λ²(n) lie in the kernel of the natural restriction
 * H_n(q) ↠ End_{SU(2)}(V^{⊗n}), so the two-row sector is where
 * the q-deformed spin-pairing observables live.
 *
 * The corresponding projection
 *
 *   π_{2-row} : H_n(q) → ⊕_{λ ∈ Λ²(n)} End(V_λ)
 *
 * is idempotent (the orthogonal projection onto the two-row
 * Wedderburn subalgebra) and the trace splits canonically:
 *
 *   tr_M = tr_M ∘ π_{2-row}  +  tr_M ∘ (id − π_{2-row}).
 *
 * **Notation.** Λ²(n) is the two-row stratum; for the (single-row)
 * trivial rep λ = (n) alone we write Λ⁰(n) = {(n)}; the standard
 * rep is λ = (n-1, 1) ∈ Λ²(n).
 *
 * Used by:
 *   - prop:he4-two-row-dominance — empirical proposition that
 *     the ⁴He canonical Markov trace lives in Λ²(12) at ≥ 80 %.
 *   - delta_lambda_2row_stratum_analysis.py — earlier empirical
 *     evidence across {D, T, ³He, ⁴He} that the dominant block
 *     is always two-row.
 *
 * Verification:
 *   computations/delta_lambda_2row_stratum_analysis.py
 *   computations/probe_he4_canonical_tr_m_fingerprint.py
 */
export default definition({
  label: "def:two-row-stratum",
  title:
    "Two-row Wedderburn stratum $\\Lambda^2(n) := \\{\\lambda \\vdash n : \\ell(\\lambda) \\le 2\\}$",
  defines: ["two-row-stratum", "two-row-projection"],
  uses: ["prop:wedderburn-weight-canonical"],
  lean: { ref: "qou:QOU.BraidKnot.TwoRowStratum" },
  tags: [
    "wedderburn-decomposition",
    "su2-schur-weyl",
    "magic-shell",
    "two-row",
    "projection",
  ],
});
