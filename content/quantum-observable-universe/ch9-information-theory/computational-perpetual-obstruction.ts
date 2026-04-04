import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:computational-perpetual-obstruction",
  title:
    "Perpetual computational obstruction (QU-to-QOU item 3 for computation)",
  tags: [
    "perpetual-obstruction",
    "QU-to-QOU",
    "complementary-subgroups",
    "P-vs-NP",
    "irreducible-tree-weight",
    "yekutieli",
    "q-NS-parallel",
  ],
  uses: [
    "thm:qu-to-qou",
    "def:skein-resolution-obstruction",
    "def:quantum-characteristic-classes",
    "prop:ns-obstruction-tower",
    "prop:computational-kummer-specialisation",
    "rem:substrate-gm-torsion",
    "def:quantum-universe",
    "def:computational-horizon",
    "conj:quantum-computational-universality",
  ],
});
