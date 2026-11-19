import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
  label: "def:quantum-pressure",
  title: "Quantum pressure",
  tags: [
    "pressure",
    "statistical-mechanics",
    "frobenius",
    "boundary",
    "q-anomaly",
  ],
  lean: { ref: "qou:QOU.Information.boundaryPressure",
    validation: "not_checked",
  },
  uses: ["def:quantum-temperature"],
});
