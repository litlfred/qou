import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:quantum-computational-universality",
  title:
    "Quantum computational universality via descent to roots of unity",
  tags: [
    "computation",
    "universality",
    "descent",
    "root-of-unity",
    "FKLW",
    "toffoli",
    "hecke-algebra",
    "path-integral",
  ],
  uses: [
    "prop:toffoli-transfer-matrix",
    "rem:toffoli-q-and",
    "prop:skein-polynomial-transfer-matrix",
    "def:descent-involution",
    "prop:descent-eigenspaces",
    "rem:jet-planck-steps",
    "def:substrate-parameter",
    "rem:complex-substrate-interpretation",
  ],
});
