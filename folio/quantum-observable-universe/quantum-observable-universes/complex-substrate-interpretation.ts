import { remark } from "../../schema/builders";

export default remark({
  label: "rem:complex-aether-interpretation",
  renamedFrom: ["rem:complex-substrate-interpretation"],
  title: "Complex aether parameter and the observability constraint",
  interprets: "def:aether-parameter",
  uses: [
    "ex:aether-parameter-su2",
    "rem:q-laplacian-interpretation",
  ],
  tags: ["complex-q", "observability", "chirality", "interpretation"],
  cites: ["lusztig1993"],
});
