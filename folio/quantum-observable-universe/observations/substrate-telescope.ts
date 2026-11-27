import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:aether-parameter",
  label: "rem:aether-telescope",
  renamedFrom: ["rem:substrate-telescope"],
  title: "Aether Telescopes",
  uses: ["ex:q-reeb-flow"],
  tags: ["detector", "substrate", "observation"],
});
