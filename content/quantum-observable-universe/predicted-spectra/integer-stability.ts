import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "Beyond standard liquid-drop models, this nearest-integer minimization reframes the even-even dominance algebraically. By grounding the empirical observation in a rigid quadratic convex optimization on the quantum integers, it offers a novel algebraic rigidification of pairing effects." },
  ],
  label: "prop:integer-stability",
  title:
    "Integer stability: the valley of stability as a Diophantine constraint",
  tags: [
    "stability",
    "diophantine",
    "integer",
    "valley-of-stability",
    "coulomb",
    "magic-numbers",
  ],
  lean: { ref: "qou:QOU.Archimedean.integer_stability",
    validation: "not_checked",
  },
  uses: ["def:stable-nucleus"],
});
