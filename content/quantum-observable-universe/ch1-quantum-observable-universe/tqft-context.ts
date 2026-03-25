import { remark } from "../../schema/builders";

export default remark({
  label: "rem:tqft-context",
  title: "TQFT context",
  tags: ["tqft", "cobordism"],
  uses: [
    "def:quantum-universe",
    "def:quantum-observable-universe",
    "ex:c-quantum-observable-universe",
  ],
});
