import { definition } from "../../schema/builders";

export default definition({
  label: "def:non-commutative-formal-group",
  title: "Non-commutative formal group and its distribution algebra",
  lean: { ref: "fred2005:Fred2005.NoncommutativeFormalGroup",
    validation: "not_checked",
  },
  tags: ["formal-group", "non-commutative", "distribution-algebra"],
  uses: ["def:commutative-formal-group"],
  cites: ["leitner2006"],
});
