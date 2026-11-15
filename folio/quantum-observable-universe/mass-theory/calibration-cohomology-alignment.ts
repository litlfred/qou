import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:calibration-cohomology-alignment",
  lean: {
    ref: "qou:QOU.Mass.calibrations_eq_cohomology",
    validation: "validated",
  },
  title: "The three calibrations are the three cohomological data of H¹(Bring)",
  uses: [
    "prop:prolonged-periods-fixed-depth",
    "prop:sl2-prolongation-recurrence",
    "prop:electron-period-base",
  ],
  proofs: ["prf:calibration-cohomology-alignment"],
});
