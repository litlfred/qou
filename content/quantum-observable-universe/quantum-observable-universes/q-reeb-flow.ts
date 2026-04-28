import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-reeb",
  label: "ex:q-reeb-flow",
  title: "$q$-Deformed Reeb flow",
  lean: { ref: "qou:QOU.QReebFlow", validation: "not_checked" },
  uses: ["ex:q-reeb-vector-field"],
  tags: ["reeb-flow", "archimedean"],
});
