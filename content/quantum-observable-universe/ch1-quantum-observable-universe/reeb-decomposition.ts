import { example } from "../../schema/builders";

export default example({
  label: "ex:reeb-decomposition",
  title: "Reeb decomposition",
  tags: ["reeb", "archimedean"],
  lean: {
    decl: "QOU.ReebDecomposition",
    validation: "leanok",
  },
  uses: ["ex:c-quantum-universe", "def:weight-decomposition", "def:maximal-torus"],
});
