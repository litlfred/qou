import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-langlands-dual",
  lean: { ref: "qou:QOU.QLanglandsDual", validation: "not_checked" },
  title: "$q$-Langlands dual group",
  uses: [
    "def:quantum-gauge-group",
    "def:quantum-su2",
  ],
  tags: ["geometric-langlands", "langlands-dual", "quantum-group"],
});
