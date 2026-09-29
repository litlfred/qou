import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-reeb",
  label: "ex:q-reeb-vector-field",
  title: "$q$-Deformed Reeb vector field",
  lean: { ref: "qou:QOU.qReebVectorField", validation: "not_checked" },
  uses: ["ex:q-lie-bracket"],
  tags: ["reeb", "archimedean"],
});
