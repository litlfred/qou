import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:morse-wall-q-moduli",
  title:
    "Morse wall in $q$-moduli: the integration-limit pencil degenerates on the golden node",
  tags: [
    "mobius-transformation",
    "morse-wall",
    "integration-limit",
    "golden-ratio",
    "q-moduli",
    "laurent-polynomial",
  ],
  lean: {
    ref: "qou:QOU.Descartes.morse_wall_q_moduli",
    validation: "not_checked",
  },
  uses: [
    "prop:mobius-limit-from-thimble",
    "prop:mobius-golden-fixed-points",
    "rem:color-tube-cubic",
    "rem:golden-ratio-degeneration",
  ],
  cites: [
    "arnold-gusein-zade-varchenko1988",
    "seidel2008",
    "pham1965",
  ],
});
