import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-universe",
  label: "rem:mass-noncommutative-drag",
  title: "Non-commutativity and geometric drag",
  tags: ["mass", "non-commutativity", "direct-limit"],
  uses: [
    "def:direct-limit-algebra",
    "rem:mass-geometric-drag",
  ],
});
