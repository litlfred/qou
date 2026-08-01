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
        "corollary are proved sorry-free. Open: an instance for the " +
        "intended instantiation (the faithful action itself).",
    },
  ],
});
