import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:elliptic-stability-locus",
  title:
    "The nuclear degeneracy locus is an elliptic curve over the Bring surface",
  tags: [
    "elliptic-curve",
    "stability",
    "diophantine",
    "chiral-fibration",
    "coulomb",
    "pairing",
    "bring-surface",
  ],
  uses: [
    "prop:integer-stability",
    "prop:chiral-elliptic",
    "rem:color-tube-cubic",
    "def:coulomb-charge",
    "def:skein-binding-lagrangian",
    "prop:beta-stability",
    "rem:color-tube-fibers",
    "def:substrate-parameter",
  ],
});
