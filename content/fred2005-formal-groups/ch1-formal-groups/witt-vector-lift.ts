import { definition } from "../../schema/builders";

export default definition({
  label: "def:witt-vector-lift",
  title: "Witt vector lift",
  lean: {
    decl: "Fred2005.WittVectorLift",
    validation: "not_checked",
  },
  tags: ["witt-vector", "formal-group", "lift"],
  uses: [
    "def:commutative-formal-group",
    "def:skewed-poisson-structure",
    "def:non-commutative-formal-group",
  ],
  cites: ["fred2005", "hazewinkel1978"],
});
