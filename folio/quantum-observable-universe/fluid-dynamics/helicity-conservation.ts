import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:helicity-conservation",
  lean: { ref: "qou:QOU.FluidDynamics.helicity_conservation", validation: "not_checked" },
  title: "Categorical helicity conservation",
  uses: [
    "rem:braid-fluid",
    "prop:discrete-vortex-spectrum",
  ],
  cites: ["moffatt-ricca-helicity"],
  tags: ["helicity", "topological-invariant", "conservation", "fluid-dynamics", "knot"],
});
