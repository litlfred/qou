import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:helicity-conservation",
  lean: { ref: "qou:QOU.FluidDynamics.helicity_conservation", validation: "not_checked" },
  title: "Categorical helicity conservation",
  uses: [
    "rem:braid-fluid",
    "prop:discrete-vortex-spectrum",
    "prop:closure-unseen-subword",
  ],
  cites: ["moffatt-ricca-helicity", "komendarczyk2008"],
  tags: ["helicity", "topological-invariant", "conservation", "fluid-dynamics", "knot"],
});
