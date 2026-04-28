import { definition } from "../../schema/builders";

export default definition({
  label: "def:skewed-poisson-structure",
  title: "Skewed-Poisson structure",
  lean: { ref: "fred2005:Fred2005.SkewedPoissonStructure",
    validation: "not_checked",
  },
  tags: ["poisson", "biderivation", "formal-group"],
  uses: ["def:commutative-formal-group"],
  cites: ["fred2005"],
});
