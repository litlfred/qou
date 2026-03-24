import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-archimedean-bridge",
  title: "Categorical--geometric correspondence",
  tags: ["bridge", "fibre-functor", "contact-geometry"],
  uses: [
    "def:spatial-realization-functor",
    "def:weight-decomposition",
    "def:categorical-q-ext-deriv",
  ],
  proofs: ["prf:categorical-archimedean-bridge"],
});
