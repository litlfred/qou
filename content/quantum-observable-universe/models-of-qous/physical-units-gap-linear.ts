import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:physical-units-gap-linear",
  proofs: ["prf:physical-units-gap-linear"],
  lean: { ref: "qou:QOU.physical_units_gap_linear",
    validation: "not_checked",
  },
  title: "The physically normalised gap vanishes linearly at $q = 1$",
  tags: ["symmetric-point", "mass-gap", "crossing-energy"],
  uses: ["def:crossing-energy"],
});
