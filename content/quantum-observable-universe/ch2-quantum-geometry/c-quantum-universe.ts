import { example } from "../../schema/builders";

export default example({
  interprets: "def:quantum-universe",
  label: "ex:c-quantum-universe",
  title: "Archimedean realisation: quantum universe",
  tags: ["archimedean", "cr-geometry"],
  lean: {
    decl: "QOU.CRManifoldData",
    validation: "leanok",
  },
  uses: ["def:quantum-universe", "def:substrate-parameter"],
});
