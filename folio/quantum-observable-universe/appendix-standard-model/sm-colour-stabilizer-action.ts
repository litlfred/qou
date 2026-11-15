import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:sm-colour-stabilizer-action",
  title: "Colour stabilizer action on the state space",
  lean: {
    ref: "qou:QOU.StandardModel.ColourStabilizerAction",
    validation: "not_checked",
  },
  uses: ["def:gauge-action-groupoid", "conj:sm-gauge-truncation"],
  tags: [
    "appendix",
    "standard-model",
    "color",
    "octonion",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-01",
      body:
        "**Primary conjecture, no instance (bean qou-ni4b).** The class " +
        "lives in the library at `QOU/StandardModel/ColourStabilizerAction.lean` " +
        "(the sibling stub was removed per the no-shadowing rule). The " +
        "concrete wiring to the octonion stabilizer `su3 e` is " +
        "`ColourStabilizerActionOnSU3` and the bracket closure of `su3 e` " +
        "(a Lie subalgebra of Der(O) = g2) is proved sorry-free, both in " +
        "`QOU.MathlibExt.OctonionSU3BracketClosure` (beans qou-iibg, " +
        "qou-51st). The dimension obstruction and the 3-strand minimality " +
        "corollary are proved sorry-free. Calibration (2026-08-01, bean " +
        "qou-1gix): the abstract class is SATISFIED by the octonion base " +
        "module (DV-Todorov 1+3; tautological inclusion su3 e < End(O)) — " +
        "instance in QOU.MathlibExt.OctonionColourActionBaseModule. Open " +
        "content sharpened: the action on the framework's own three-strand " +
        "Hecke state space, compatible with its braid structure.",
    },
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "**Calibration: the class as written is a dimension count (bean " +
        "qou-cb3r).** `ColourStabilizerAction g V` asks only for an " +
        "injective linear map g -> End V. The corpus proves that this needs " +
        "finrank g <= (finrank V)^2 (`not_colourStabilizerAction_of_dim_sq_lt`), " +
        "and `ColourBridgeObstructions.colourStabilizerAction_of_finrank_le` " +
        "proves the converse. So the class is equivalent to that inequality, " +
        "and an instance on the tower triplet Q^3 exists for any 8-dimensional " +
        "colour algebra with no octonion or Hecke input. No instance of this " +
        "class is evidence for the bridge. The bridge question needs a " +
        "Lie-hom, complex-structure and crossing-compatible strengthening; " +
        "by the audit (docs/audits/2026-11-15-colour-stabilizer-bridge.md, " +
        "sections 0, 8 and 8.1) that strengthening is satisfiable only after " +
        "complexification, with one 3 vs 3bar bit, and only at q = 1. " +
        "No q-deformed G2 braiding restricts to the tower crossing on the " +
        "colour triplet at generic q.",
    },
  ],
});
