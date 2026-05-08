import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:three-parameters-wedderburn",
  lean: { ref: "qou:QOU.BraidKnot.three_parameters_wedderburn", validation: "not_started" },
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
