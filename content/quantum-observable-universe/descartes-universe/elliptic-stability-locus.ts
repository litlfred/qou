import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:elliptic-stability-locus",
  title:
    "The nuclear degeneracy locus is an elliptic curve over the Bring's surface",
  tags: [
    "elliptic-curve",
    "stability",
    "diophantine",
    "coral-fibration",
    "coulomb",
    "pairing",
    "bring-surface",
  ],
  uses: [
    "prop:integer-stability",
    "def:color-tube-fibers",
  ],
});
