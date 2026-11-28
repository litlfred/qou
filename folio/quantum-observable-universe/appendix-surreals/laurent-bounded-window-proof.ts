import { proof } from "../../schema/builders";

export default proof({
  label: "prf:laurent-bounded-window",
  title: "Proof of bounded-window convergence via $\\mathbb{F}_2{[q]}$ reduction",
  uses: [
    "prop:laurent-bounded-window",
    "prop:q-syracuse-lift",
    "prop:balanced-holonomy-exclusion",
  ],
});
