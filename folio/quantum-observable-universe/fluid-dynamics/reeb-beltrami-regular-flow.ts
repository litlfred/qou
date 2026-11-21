import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-beltrami-regular-flow",
  lean: {
    ref: "qou:QOU.FluidDynamics.BeltramiSteadyEuler.L3.deformation_V",
    validation: "not_checked",
  },
  title: "The fibre-rotation field of $\\mathrm{UT}(\\Sigma_4)$ is a regular Navier--Stokes flow",
  uses: [
    "def:brings-surface",
    "thm:ns-singularity-descartes",
  ],
  cites: ["ebin-marsden1970"],
  tags: [
    "navier-stokes",
    "euler",
    "beltrami",
    "killing-field",
    "reeb",
    "descartes",
    "regularity",
  ],
});
