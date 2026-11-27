import { example } from "../../schema/builders";

export default example({
  interprets: "def:quantum-universe",
  label: "ex:c-quantum-universe",
  title: "Archimedean realisation: quantum universe",
  tags: ["archimedean", "cr-geometry"],
  lean: { ref: "qou:QOU.CRManifoldData",
    validation: "leanok",
  },
  uses: ["def:aether-parameter"],
  cites: ["tanaka1974", "tanaka1975", "webster1978"],
});
