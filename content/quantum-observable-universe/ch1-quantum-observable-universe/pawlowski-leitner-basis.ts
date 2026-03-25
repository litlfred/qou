import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pawlowski-leitner-basis",
  title: "Pawlowski--Leitner basis for $\\mathrm{Hom}(V_j, V_{1/2}^{\\otimes n})$",
  lean: {
    decl: "QOU.PawlowskiLeitnerBasis",
    validation: "not_checked",
  },
  uses: [
    "rem:spin-half-representation",
    "rem:simple-objects-V",
    "thm:su2-emergence",
  ],
  tags: ["basis", "intertwiner", "representation", "pawlowski-leitner"],
});
