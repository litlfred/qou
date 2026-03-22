import { example } from "../../schema/builders";

export default example({
  label: "ex:q-reeb-vector-field",
  title: "$q$-Deformed Reeb vector field",
  lean: { decl: "QOU.qReebVectorField", validation: "not_checked" },
  uses: ["def:categorical-reeb", "ex:q-lie-bracket"],
  tags: ["reeb", "archimedean"],
});
