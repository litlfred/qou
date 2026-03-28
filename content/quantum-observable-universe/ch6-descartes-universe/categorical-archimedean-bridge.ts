import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-archimedean-bridge",
  lean: {
    decl: "QOU.categorical_archimedean_bridge",
    validation: "not_checked",
  },
  title: "Categorical--geometric correspondence",
  tags: ["bridge", "fibre-functor", "contact-geometry"],
  uses: [
    "def:spatial-realization-functor",
    "def:categorical-q-ext-deriv",
  ],
  proofs: ["prf:categorical-archimedean-bridge"],
});
