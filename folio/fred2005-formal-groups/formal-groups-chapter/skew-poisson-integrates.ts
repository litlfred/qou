import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:skew-poisson-integrates",
  title: "Integration theorem",
  lean: { ref: "fred2005:Fred2005.skew_poisson_integrates",
    validation: "not_checked",
  },
  tags: ["integration", "formal-group", "main-theorem"],
  uses: [
    "def:commutative-formal-group",
    "def:skewed-poisson-structure",
    "def:non-commutative-formal-group",
  ],
  cites: ["fred2005"],
});
