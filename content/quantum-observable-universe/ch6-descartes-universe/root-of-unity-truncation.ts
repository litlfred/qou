import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:root-of-unity-truncation",
  title:
    "Representation-theoretic truncation at roots of unity and the $q = 1$ accumulation",
  uses: [
    "thm:q-ns-wellposedness",
    "thm:quantum-peter-weyl",
    "prop:q-ns-nonlinear-uniqueness",
    "conj:regularity-breakdown",
    "prop:vorticity-lower-bound",
    "def:q-navier-stokes",
    "def:substrate-parameter",
  ],
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
