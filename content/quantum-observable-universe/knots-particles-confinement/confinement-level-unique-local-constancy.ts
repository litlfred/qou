import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:confinement-level-unique",
  label: "rem:confinement-level-unique-local-constancy",
  title: "Local constancy of the confinement level in $q$",
  tags: ["uniqueness", "confinement", "filtration", "shadow-price"],
  uses: ["prop:confinement-level-unique"],
});
