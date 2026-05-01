import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:critical-exponent",
  title: "Critical exponent of the enstrophy divergence at $q = 1$",
  uses: [
    "prop:q-ns-nonlinear-uniqueness",
    "conj:regularity-breakdown",
  ],
  tags: ["critical-exponent", "enstrophy", "phase-transition", "scaling"],
});
