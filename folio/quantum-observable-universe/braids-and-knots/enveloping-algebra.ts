import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:su2-basis",
  label: "rem:enveloping-algebra",
  lean: { ref: "ugb:UGB.GrobnerShirshov.uq_pbw_basis" },
  title: "Universal enveloping algebra",
  tags: ["enveloping-algebra", "pbw", "quantum-group"],
  uses: ["def:su2-basis", "def:direct-limit-algebra"],
});
