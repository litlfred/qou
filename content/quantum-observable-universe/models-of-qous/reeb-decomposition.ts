import { example } from "../../schema/builders";

export default example({
  interprets: "def:weight-decomposition",
  label: "ex:reeb-decomposition",
  title: "Reeb decomposition",
  tags: ["reeb", "archimedean"],
  lean: { ref: "qou:QOU.ReebDecomposition",
    validation: "leanok",
  },
  uses: ["ex:c-quantum-universe"],
});
