import { proposition } from "../../schema/builders";

/**
 * Closed-form pole-order formula for torus-knot characters.
 *
 * For the torus knot T_{p,k} (gcd(p, k) = 1) represented as the
 * closure of β_{p,k} = (σ_1 σ_2 ⋯ σ_{p-1})^k in B_p, define
 *
 *   α_shift(T_{p,k}) := max_{λ ⊢ p} ord_{q=0}^{(−)} χ_λ(β_{p,k})
 *
 * — the largest pole order at q = 0 of the seminormal character
 * χ_λ(β_{p,k}) over all irreducible H_p(q)-representations.
 *
 * **Proposition.** For gcd(p, k) = 1:
 *   1. The maximizer is the all-anti-symmetric channel
 *      V_{(1^p)}.
 *   2. α_shift(T_{p,k}) = k(p − 1).
 *
 * On V_{(1^p)} the unique SYT carries axial-distance pattern
 * (−1, −2, …, −(p−1)) along the column; each generator σ_i acts
 * as the eigenvalue −q⁻¹ (Hoefsmit 1×1 block at ρ = −1). The
 * trace of (σ_1 ⋯ σ_{p-1})^k is therefore (−q⁻¹)^{k(p−1)},
 * which has pole order exactly k(p−1) at q = 0 with no
 * within-partition cancellation (every step visits a distinct
 * axial distance, so the b² = (1 − q^{2ρ−2})(1 − q^{2ρ+2})/
 * (1 − q^{2ρ})² zeroing on adjacent contents never fires).
 *
 * Verification: computations/alpha/alpha_shift_torus.py
 * Witness:      computations/alpha/alpha-shift-torus.witness.json
 * Audit:        docs/audits/2026-05-04-alpha-shift-torus-multiplicative-chain.md
 *
 * Test bench: (2, 3) → 3, (2, 5) → 5, (2, 9) → 9, (3, 4) → 8,
 *             (3, 5) → 10, (3, 7) → 14 — all match k(p−1) and the
 * maximizer is V_{(1^p)} in every case.
 *
 * Used by: prop:alpha-em-shift-multiplicative-chain (refactors α_EM⁻¹
 * = q · [9]_q · [10]_q as q · [α_shift(T_{2,9})]_q · [α_shift(T_{3,5})]_q).
 */
export default proposition({
  label: "prop:alpha-shift-torus-knot",
  title:
    "Pole order at $q=0$ of the torus-knot character: $\\alpha_{\\mathrm{shift}}(T_{p,k}) = k(p-1)$ on $V_{(1^p)}$",
  uses: [
    // prop:force-carrier-intertwining-correspondence removed (qou-tm3c): alpha_shift is a pole order of the seminormal characters; which channel a force carrier dominates is not used.
    "def:delta-q-decoration",
  ],
  computation: {
    engine: "sympy",
    script: "computations/alpha/alpha_shift_torus.py",
    witness: "computations/alpha/alpha-shift-torus.witness.json",
    status: "verified",
    requires: ["sympy", "numpy"],
  },
  lean: { ref: "qou:QOU.BraidKnot.AlphaShiftTorus.alpha_shift_torus_knot" },
  tags: [
    "alpha-shift",
    "torus-knot",
    "pole-order",
    "seminormal",
    "wedderburn-channel",
    "hoefsmit",
    "delta-q",
    "force-carrier",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ### Cross-link\n\nThe two values $\\alpha_{\\mathrm{shift}}(T_{2,9}) = 9$ and\n$\\alpha_{\\mathrm{shift}}(T_{3,5}) = 10$ are precisely the\n$q$-integer indices appearing in\n[Electromagnetic coupling from the antisymmetric braiding and force-carrier crossings](#prop:em-coupling-projection)'s\nformula\n\n$$\n  \\alpha_{EM}^{-1} \\;=\\; q \\cdot [9]_q \\cdot [10]_q.\n$$\n\n[Multiplicative-chain form](#prop:alpha-em-shift-multiplicative-chain)\ncombines the two identities into the **shift-exponent form**\n\n$$\n  \\alpha_{EM}^{-1}\n  \\;=\\;\n  q \\cdot\n  \\bigl[\\alpha_{\\mathrm{shift}}(T_{2,9})\\bigr]_q \\cdot\n  \\bigl[\\alpha_{\\mathrm{shift}}(T_{3,5})\\bigr]_q,\n$$\n\nrecasting the $\\delta_q$-trace identity in the same combinatorial\nterms as the atomic-shift formula." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The canonical evidence ([`alpha-shift-torus.witness.json`](../../../computations/alpha/alpha-shift-torus.witness.json)) records" },
  ],
});
