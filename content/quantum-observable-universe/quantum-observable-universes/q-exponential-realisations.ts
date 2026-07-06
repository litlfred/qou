import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-exponential-realisations",
  interprets: "def:q-exponential",
  title:
    "Realisations of $\\exp_q$: universal property, base rings, the Habiro ring, and the Reeb flow",
  tags: ["hopf-algebra", "grouplike", "q-exponential", "reeb-flow"],
  uses: ["def:q-exponential", "def:categorical-laplace", "def:habiro-ring"],
});
