import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:conway-normal-form",
  label: "rem:body-asymptotics-catalog-jet-structures",
  title:
    "Recursive jet structures read in surreal $\\ordw$-form",
  uses: [
    "rem:conway-normal-form",
    "def:surreal-blowup-calculus",
  ],
  tags: [
    "surreal-numbers",
    "jet-tower",
    "asymptotic",
    "blow-up-calculus",
  ],
});
