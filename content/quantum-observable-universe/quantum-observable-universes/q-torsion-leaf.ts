import { example } from "../../schema/builders";

export default example({
  interprets: "def:categorical-q-connection",
  label: "ex:q-torsion-leaf",
  title: "$q$-Torsion leaf",
  lean: { ref: "qou:QOU.QTorsionLeaf", validation: "not_checked" },
  uses: ["ex:q-reeb-flow"],
  tags: ["torsion-leaf", "archimedean"],
});
