import { remark } from "../../schema/builders";

export default remark({
  label: "rem:substrate-self-duality-physical",
  interprets: "thm:substrate-self-duality",
  title: "Physical interpretation of aether self-duality",
  cites: ["yekutieli2010"],
  tags: ["self-duality", "frobenius", "dualizing-complex"],
  uses: ["thm:substrate-self-duality"],
});
