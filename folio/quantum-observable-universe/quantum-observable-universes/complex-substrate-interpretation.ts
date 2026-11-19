import { remark } from "../../schema/builders";

export default remark({
  label: "rem:complex-substrate-interpretation",
  title: "Complex aether parameter and the observability constraint",
  interprets: "def:substrate-parameter",
  uses: [
    "ex:substrate-parameter-su2",
    "rem:q-laplacian-interpretation",
  ],
  tags: ["complex-q", "observability", "chirality", "interpretation"],
  cites: ["lusztig1993"],
});
