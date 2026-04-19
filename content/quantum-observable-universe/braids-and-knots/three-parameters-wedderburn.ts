import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:three-parameters-wedderburn",
  lean: {
    decl: "QOU.BraidsAndKnots.three_parameters_wedderburn",
    file: "QOU/BraidsAndKnots.lean",
    validation: "not_checked",
  },
  title: "Three calibration parameters from Wedderburn-Artin decomposition of $H_3(q)$",
  uses: [
    "def:categorical-action",
    "rem:calibration-inputs",
    "prop:rj-canonical-inner-product",
    "prop:cohomological-embedding",
  ],
  tags: [
    "wedderburn",
    "calibration",
    "irrep",
    "hecke-algebra",
    "young-symmetrizer",
    "on-shell",
  ],
});
