import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:root-of-unity-truncation",
  lean: { ref: "qou:QOU.FluidDynamics.root_of_unity_truncation", validation: "not_started" },
  title:
    "Representation-theoretic truncation at roots of unity and the $q = 1$ accumulation",
  uses: ["prop:vorticity-lower-bound"],
  tags: [
    "root-of-unity",
    "truncation",
    "verlinde",
    "modular-tensor-category",
    "regularity",
    "accumulation-point",
    "millennium-problem",
  ],
});
