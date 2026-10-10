import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-blowup-physical-evidence",
  title:
    "Physical signatures of the Navier--Stokes blow-up: intermittency, GRBs, CMB anomalies",
  interprets: "prop:blowup-yekutieli",
  uses: [
    "rem:conway-normal-form",
    "sec:cmb-torsion-data",
    "rem:bec-vortex-data",
    "prop:leray-profile",
  ],
  tags: [
    "navier-stokes",
    "blowup",
    "physical-evidence",
    "intermittency",
    "gamma-ray-burst",
    "cmb",
    "falsifiability",
    "millennium-problem",
  ],
});
