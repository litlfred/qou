import { example } from "../../schema/builders";

export default example({
  label: "ex:c-quantum-observable-universe",
  title: "Archimedean realisation: quantum observable universe",
  tags: ["archimedean", "observable"],
  lean: {
    decl: "QOU.CQuantumObservableUniverse",
    validation: "leanok",
  },
  uses: ["ex:c-quantum-universe", "def:quantum-observable-universe"],
});
