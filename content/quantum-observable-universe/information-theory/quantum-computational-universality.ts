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
  lean: {
    ref: "qou:QOU.QuantumComputationalUniversality.QuantumComputationalUniversality",
    validation: "not_checked",
  },
  uses: [
    "rem:toffoli-q-and",
    "rem:jet-planck-steps",
    "rem:complex-substrate-interpretation",
  ],
});
