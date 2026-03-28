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
  lean: {
    decl: "QOU.Descartes.integer_stability",
    validation: "not_checked",
  },
  uses: [
    "prop:beta-stability",
    "def:stable-nucleus",
    "def:coulomb-charge",
    "def:skein-binding-lagrangian",
    "def:substrate-parameter",
    "prop:local-substrate-q",
  ],
});
