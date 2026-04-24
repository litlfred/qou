import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ns-blowup-physical-evidence",
  title:
    "Physical signatures of the Navier--Stokes blow-up: intermittency, GRBs, CMB anomalies",
  interprets: "prop:blowup-yekutieli",
  uses: [
    "prop:blowup-yekutieli",
    "rem:ns-surreal-bound",
    "rem:millennium-unification",
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "rem:cmb-torsion-data",
    "rem:bec-vortex-data",
    "rem:hecke-algebra-from-braiding",
    "prop:leray-profile",
    "rem:big-o-surreal",
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
