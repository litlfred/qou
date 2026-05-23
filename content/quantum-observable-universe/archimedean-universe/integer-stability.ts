import { proposition } from "../../schema/builders";

export default proposition({
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
