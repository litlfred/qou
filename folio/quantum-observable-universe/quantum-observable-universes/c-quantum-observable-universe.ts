import { example } from "../../schema/builders";

export default example({
  interprets: "def:quantum-observable-universe",
  label: "ex:c-quantum-observable-universe",
  title: "Archimedean realisation: quantum observable universe",
  tags: ["archimedean", "observable"],
  lean: { ref: "qou:QOU.CQuantumObservableUniverse",
    validation: "leanok",
  },
  uses: ["ex:c-quantum-universe"],
});
