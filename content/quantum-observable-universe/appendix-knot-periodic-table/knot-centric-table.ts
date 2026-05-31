import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:shell-transition-knot",
  label: "rem:knot-centric-table",
  title:
    "Knot-centric periodic table: reorganization by nuclear and electronic knot structure",
  tags: [
    "periodic-table",
    "knot-centric",
    "visualization",
    "nuclear-shell",
    "borromean",
    "magic-receptive",
    "transfer-matrix",
    "skein-polynomial",
  ],
  uses: [
    "prop:shell-structure-eigenvalues",
    "thm:generation-completeness",
    "rem:knot-exhaustiveness",
  ],
});
