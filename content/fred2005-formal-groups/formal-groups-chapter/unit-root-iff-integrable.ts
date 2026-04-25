import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:unit-root-iff-integrable",
  title: "Unit-root iff integrable",
  lean: { ref: "fred2005:Fred2005.unit_root_iff_integrable",
    validation: "not_checked",
  },
  tags: ["f-crystal", "unit-root", "integrability", "equivalence"],
  uses: [
    "def:commutative-formal-group",
    "def:skewed-poisson-structure",
    "def:unit-root-f-crystal",
    "def:non-commutative-formal-group",
    "thm:skew-poisson-integrates",
  ],
  cites: ["fred2005"],
});
