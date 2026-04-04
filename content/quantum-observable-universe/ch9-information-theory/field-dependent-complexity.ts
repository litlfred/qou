import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:field-dependent-complexity",
  title:
    "Computational complexity is field-dependent",
  tags: [
    "complexity",
    "field-dependence",
    "finite-field",
    "root-of-unity",
    "P-vs-NP",
    "obstruction",
    "base-field",
  ],
  uses: [
    "def:skein-resolution-obstruction",
    "def:computational-horizon",
    "rem:base-field-independence",
    "rem:braid-base-field",
    "conj:quantum-computational-universality",
    "def:operational-entropy",
  ],
});
