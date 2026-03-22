import { example } from "../../schema/builders";

export default example({
  label: "ex:q-torsion-leaf",
  title: "$q$-Torsion leaf",
  lean: { decl: "QOU.QTorsionLeaf", validation: "not_checked" },
  uses: ["ex:q-reeb-flow"],
  tags: ["torsion-leaf", "archimedean"],
});
