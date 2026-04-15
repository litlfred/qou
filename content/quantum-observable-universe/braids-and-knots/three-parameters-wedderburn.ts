import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:three-parameters-wedderburn",
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
