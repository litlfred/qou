import { definition } from "../../schema/builders";

export default definition({
  label: "def:commutative-formal-group",
  title: "Commutative formal group",
  lean: { ref: "fred2005:Fred2005.CommutativeFormalGroup",
    validation: "not_checked",
  },
  tags: ["formal-group", "commutative"],
  cites: ["hazewinkel1978", "leitner2006"],
});
