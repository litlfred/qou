import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hecke-radical-is-temperley-lieb",
  title:
    "The radical is the Temperley--Lieb ideal: $\\sum \\dim^{2}$ over the surviving blocks is $C_n$",
  interprets: "prop:convention-d-kills-antisymmetriser",
  lean: {
    ref: "qou:QOU.QBeta.TemperleyLiebTower.catalan_five",
    validation: "not_checked",
  },
  uses: ["prop:convention-d-kills-antisymmetriser"],
  tags: [
    "temperley-lieb",
    "catalan",
    "radical",
    "convention-d",
    "trace-convention",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **What is now proved in Lean, at general $n$.** Four statements,\nnone of which is the isomorphism:\n\n- $\\sum_\\lambda \\dim_\\lambda\\, y_\\lambda = 1$ --- the normalisation\n  $\\mathrm{tr}(1) = 1$ ([`levelSum_eq_one`](../lean/QOU/QBeta/TwoRowNormalisation.lean));\n- $\\sum_k m_k(n)\\,[n{+}1{-}2k]_q = [2]_q^{\\,n}$ --- the same identity with the\n  denominator cleared, i.e. the $q$-dimension count of $V^{\\otimes n}$\n  ([`qdim_normalisation_general`](../lean/QOU/QBeta/QDimNormalisation.lean));\n- $\\sum \\dim^2 = C_n$ over the two-**row** shapes\n  ([`dimHLF_two_row_sq_sum`](../lean/QOU/Mathlib/TwoRowDimCatalan.lean)) and,\n  separately, over the two-**column** shapes\n  ([`dimHLF_two_col_sq_sum`](../lean/QOU/MassTheory/TwoRowTwoColumnCollision.lean));\n- $\\dim \\lambda = \\dim \\lambda'$ **for this family**\n  ([`dimHLF_two_col_eq_two_row`](../lean/QOU/MassTheory/TwoRowTwoColumnCollision.lean)),\n  which the next section had been asserting without backing.\n\n**What is still not proved: the isomorphism itself.** No formalised statement of\n$H_n(q)/\\mathrm{rad} \\cong TL_n(q)$ exists, and nothing above supplies one --- a\n\nthe trace radical is a two-sided ideal\n([`traceRadical_two_sided`](../lean/QOU/QBeta/TemperleyLiebTower.lean)), which is\nwhat licenses passing to the quotient as an algebra at all, and convention D is\nthe standard normalised Temperley--Lieb trace at loop parameter $\\delta = [2]_q$\n([`loop_reciprocal`](../lean/QOU/QBeta/TemperleyLiebTower.lean)).\n\n## A convention collision to know about before wiring the Lean\n\n[`QOU.MathlibExt.WenzlSchurElement`](../lean/QOU/MathlibExt/WenzlSchurElement.lean)\nproves the Temperley--Lieb stratification in the **conjugate** convention: at\n$X = Q^{-N}$ the surviving blocks are those with $\\lambda_1 \\le N$, i.e. at most\n$N$ **columns**. This section, and convention D, state the survivors as at most\ntwo **rows**. Both are correct in their own convention, and that file's own\ndocstring warns: *\"anyone wiring `schurElement_tl_eq_zero_iff` to that block must\ntranspose.\"*\n\ndimensions cannot tell the two apart. Measured at $n = 3,4,5$ in\n`tl-two-row-weight-family.witness.json`.\n\nBoth halves of that trap are now theorems, at every $n$, in\n[`QOU.MassTheory.TwoRowTwoColumn`](../lean/QOU/MassTheory/TwoRowTwoColumnCollision.lean):\ntransposition is an explicit bijection between the two families\n, so they are equinumerous; the families are nevertheless\ndifferent sets (`atMostTwoRows_iff_atMostTwoCols_false`, witnessed by the single\nrow $(3)$); and their squared-dimension totals agree\n. The equality $\\dim \\lambda = \\dim \\lambda'$ used\nabove is proved there for this family rather than" },
    {
      kind: "status",
      date: "2026-08-09",
      body:
        "OPEN — the Catalan measurement carried in this remark has NO PRODUCER and NO WITNESS. " +
        "The table (n = 2..7, sum of squared Specht dimensions over the surviving blocks = " +
        "2, 5, 14, 42, 132, 429; worst residual 1.34e-51 at 50 dps) is recorded only in the " +
        "module docstring of lean/QOU/QBeta/TemperleyLiebTower.lean. " +
        "computations/y_lambda_su_n.py:90 states verbatim 'Read-only: writes no witness, runs no " +
        "producer', so nothing in the repo emits a *.witness.json for it. The Lean carries the " +
        "arithmetic instances only (catalan_three / catalan_four / catalan_five / radical_four, " +
        "cross-checked against Mathlib's Nat.catalan by counts_are_catalan) plus the branching " +
        "recursion; there is no Lean theorem for the isomorphism H_n(q)/rad = TL_n(q). " +
        "The block is therefore deliberately a REMARK and not a proposition, and the prose " +
        "attributes the numbers as unwitnessed. Promoting it requires a probe + witness pair; " +
        "writing that producer was out of scope for this change and is left to the owner.",
    },
  ],
});
