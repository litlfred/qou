import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-archimedean-bridge",
  lean: { ref: "qou:QOU.categorical_archimedean_bridge",
    validation: "not_checked",
  },
  title: "Categorical--geometric correspondence",
  tags: ["bridge", "fibre-functor", "contact-geometry"],
  uses: [
    "def:spatial-realization-functor",
    "def:categorical-q-ext-deriv",
  ],
  proofs: ["prf:categorical-archimedean-bridge"],
  examples: [
    "ex:calabi-yau",
    "ex:ale",
    "ex:brings-surface",
    "ex:cosmological-limits",
    "ex:instanton",
    "ex:irreducible-connection",
    "ex:self-dual-curvature",
    "rem:c-substrate-via-levi",
    "ex:reeb-decomposition",
    "rem:gr-substrate-geometry",
  ],
});
