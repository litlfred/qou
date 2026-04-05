import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:q-geometric-langlands",
  label: "rem:q-gl-physical-interpretation",
  title: "Physical interpretation of $q$-Geometric Langlands",
  uses: [
    "conj:q-geometric-langlands",
    "def:quantum-observable-universe",
  ],
  tags: ["geometric-langlands", "physical-interpretation"],
});
