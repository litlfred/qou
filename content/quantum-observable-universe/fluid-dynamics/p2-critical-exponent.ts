import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:critical-exponent",
  title: "Critical exponent of the enstrophy divergence at $q = 1$",
  uses: [
    "prop:q-ns-nonlinear-uniqueness",
    "conj:regularity-breakdown",
  ],
  tags: ["critical-exponent", "enstrophy", "phase-transition", "scaling"],
});
