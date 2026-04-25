import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pawlowski-leitner-basis",
  title: "Pawlowski--Leitner basis for $\\mathrm{Hom}(V_j, V_{1/2}^{\\otimes n})$",
  lean: { ref: "qou:QOU.PawLeiBasis",
    validation: "not_checked",
  },
  uses: [
    "rem:spin-half-representation",
    "unital-groebner-bases:cor:pbw",
  ],
  examples: ["rem:adjoint-trace"],
  tags: ["basis", "intertwiner", "representation", "pawlei"],
});
