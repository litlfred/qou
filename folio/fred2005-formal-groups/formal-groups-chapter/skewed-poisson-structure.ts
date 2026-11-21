import { definition } from "../../schema/builders";

export default definition({
  label: "def:skewed-poisson-structure",
  title: "Poisson structure on a splay",
  lean: { ref: "fred2005:Fred2005.SkewedPoissonStructure",
    validation: "not_checked",
  },
  tags: ["poisson", "biderivation", "splay"],
  uses: ["def:commutative-formal-group"],
  cites: ["leitner2006"],
});
