import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
  label: "conj:quantum-computational-universality",
  title:
    "Quantum computational universality via descent to roots of unity",
  tags: [
    "tier:S",
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
    "prop:reeb-turing-completeness-classical",
    "rem:toffoli-q-and",
    "rem:jet-planck-steps",
    "rem:complex-substrate-interpretation",
  ],
  cites: [
    "freedman2003",
  ],
});
