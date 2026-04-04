import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:computational-kummer-specialisation",
  title:
    "Kummer specialisation of the computational obstruction",
  tags: [
    "kummer",
    "specialisation",
    "Gm-torsion",
    "obstruction",
    "divisibility",
    "P-vs-NP",
    "root-of-unity",
    "hecke-radical",
  ],
  uses: [
    "def:skein-resolution-obstruction",
    "prop:ns-kummer-specialisation",
    "rem:substrate-gm-torsion",
    "conj:quantum-computational-universality",
    "prop:field-dependent-complexity",
    "def:quantum-characteristic-classes",
    "prop:ns-obstruction-tower",
  ],
});
