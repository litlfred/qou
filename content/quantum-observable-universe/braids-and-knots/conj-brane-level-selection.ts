import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:brane-level-selection",
  title:
    "Canonical brane-tower level-selection rule: $n_\\star(\\mathfrak{H}) = \\ell \\cdot n_0 + k$",
  uses: [
    "conj:brane-tower-z-habiro",
    "prop:atom-knot-mass-derivation",
    "def:confined-particle",
    "prop:gb-spectral-sequence",
  ],
  tags: [
    "brane-tower",
    "level-selection",
    "habiro",
    "gb-filtration",
    "confinement-level",
    "gap-a",
    "audit",
  ],
});
