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
    {
      kind: "note",
      body: "Computational witness: tl-two-row-weight-family.witness.json.",
    },
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
