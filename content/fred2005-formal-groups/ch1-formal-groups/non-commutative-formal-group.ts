import { definition } from "../../schema/builders";

export default definition({
  label: "def:non-commutative-formal-group",
  title: "Non-commutative formal group",
  lean: {
    decl: "Fred2005.NoncommutativeFormalGroup",
    validation: "not_checked",
  },
  tags: ["formal-group", "non-commutative", "distribution-algebra"],
  uses: ["def:commutative-formal-group"],
  cites: ["fred2005"],
});
