import { remark } from "../../schema/builders";

export default remark({
  label: "rem:aether-self-duality-physical",
  renamedFrom: ["rem:substrate-self-duality-physical"],
  interprets: "thm:aether-self-duality",
  title: "Physical interpretation of aether self-duality",
  cites: ["yekutieli2010"],
  tags: ["self-duality", "frobenius", "dualizing-complex"],
  uses: ["thm:aether-self-duality"],
});
