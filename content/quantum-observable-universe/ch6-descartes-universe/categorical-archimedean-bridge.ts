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
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-archimedean-bridge-0.svg", blockIndex: 0, hash: "e4d60d3569a1" },
  ],

});
