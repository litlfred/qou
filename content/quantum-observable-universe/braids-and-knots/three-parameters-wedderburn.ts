import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:three-parameters-wedderburn",
  title: "Three calibration parameters from Wedderburn-Artin decomposition of $H_3(q)$",
  uses: ["rem:calibration-inputs"],
  tags: [
    "wedderburn",
    "calibration",
    "irrep",
    "hecke-algebra",
    "young-symmetrizer",
    "on-shell",
  ],
});
