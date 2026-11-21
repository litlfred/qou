import { proposition } from "../../schema/builders";

/**
 * The multiplicative-chain identity for the inverse fine-structure
 * constant.
 *
 *   α_EM⁻¹ = q · [α_shift(T_{2,9})]_q · [α_shift(T_{3,5})]_q
 *
 * This composes two named identities:
 *
 *   (1) prop:em-coupling-projection
 *         α_EM⁻¹ = q · [9]_q · [10]_q
 *       (bare combinatorial form, derived from the antisymmetric
 *       eigenvalue and force-carrier crossing numbers).
 *
 *   (2) prop:alpha-shift-torus-knot at (p, k) ∈ {(2, 9), (3, 5)}
 *         α_shift(T_{2,9}) = 9
 *         α_shift(T_{3,5}) = 10
 *       (closed-form pole-order on V_{(1^p)}, witness-verified).
 *
 * Substituting the two α_shift values into (1) yields the stated
 * identity exactly — there is no further conjectural content. This
 * upgrades AXKIA's δ_q-trace identity (prop:alpha-em-categorical-
 * trace-ratio) into a **shift-exponent identity** living in the same
 * combinatorial universe as the w3-w4 atomic-shift D(u) formula
 * (docs/audits/2026-05-03-w3-habiro-unblocked.md), exposing the same
 * primitive — pole order at q = 0 of a seminormal Hecke trace — at
 * both ends of the derivation chain.
 *
 * The basis is exactly two knots: prop:force-carrier-bring-uniqueness
 * proves the genus-4 saturating torus-knot set on Σ_4 is
 * {T_{2,9}, T_{3,5}}; no further factors enter.
 *
 * Witness: computations/alpha/alpha_em_shift_chain.py
 *          computations/alpha/alpha-em-shift-multiplicative-chain.witness.json
 *   Numerically verifies chain = bare to mpmath 50-dps precision
 *   (delta = 0 exactly), with the α_shift values *read from* the
 *   upstream alpha-shift-torus.witness.json (composition, not
 *   re-derivation).
 */
export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "**Lean scope (disclosure, not a change of claim).** The `lean.ref` theorem `alpha_em_shift_chain` states `chainIndices = bareIndices`, i.e. the index lists [α_shift(2,9), α_shift(3,5)] and [9, 10] agree, and proves it by rewriting with the instance data of `HasAlphaShiftTorus 2 9` and `HasAlphaShiftTorus 3 5`. α_EM does not occur in the Lean. The `.md` writes an equality for a model quantity whose comparison to CODATA shows a reported gap; the equality is a statement about the model quantity only, and the comparison is where the empirical claim sits. Found by the blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B06; bean qou-tdhw).",
    },
  ],
  label: "prop:alpha-em-shift-multiplicative-chain",
  title:
    "Multiplicative-chain form: $\\alpha_{EM}^{-1} = q \\cdot [\\alpha_{\\mathrm{shift}}(T_{2,9})]_q \\cdot [\\alpha_{\\mathrm{shift}}(T_{3,5})]_q$",
  computation: {
    engine: "mpmath",
    script: "computations/alpha/alpha_em_shift_chain.py",
    witness: [
      "computations/alpha/alpha-em-shift-multiplicative-chain.witness.json",
      "computations/alpha/alpha-shift-torus.witness.json",
    ],
    status: "verified",
    requires: ["mpmath", "sympy"],
  },
  lean: { ref: "qou:QOU.Archimedean.AlphaEmShiftChain.alpha_em_shift_chain" },
  tags: [
    "alpha-em",
    "multiplicative-chain",
    "fine-structure-constant",
    "shift-exponent",
    "torus-knot",
    "force-carrier",
    "delta-q",
    "categorical-composition",
  ],
});
