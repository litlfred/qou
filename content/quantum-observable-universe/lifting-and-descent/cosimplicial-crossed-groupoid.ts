import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cosimplicial-crossed-groupoid",
  title: "Cosimplicial crossed groupoid",
  tags: ["cosimplicial", "crossed-groupoid", "gerbe", "yekutieli"],
  lean: { ref: "qou:QOU.LiftingDescent.cosimplicial_crossed_groupoid_exists", validation: "not_checked" },
  uses: ["def:yekutieli-triple"],
  proofs: ["prf:cosimplicial-crossed-groupoid"],
});
