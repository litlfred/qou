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
      date: "2026-07-31",
      body:
        "**Primary conjecture, no instance (bean qou-ni4b).** The class " +
        "is stated over an abstract colour-algebra slot; the intended " +
        "instantiation is the octonion stabilizer `su3 e` " +
        "(QOU.MathlibExt.OctonionSU3Stabilizer, finrank = 8 gate). " +
        "Type-level wiring to that concrete module is a recorded " +
        "follow-up (the import pulls the decide-heavy octonion cone). " +
        "The dimension obstruction and the 3-strand minimality " +
        "corollary are proved sorry-free.",
    },
  ],
});
