import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:confinement-topological",
  label: "rem:confinement-topological-interpretation",
  title: "Confinement = topology + action minimization",
  tags: [
    "confinement",
    "topological",
    "borromean",
    "linear-programming",
    "physical-interpretation",
  ],
  uses: ["prop:confinement-topological"],
});
