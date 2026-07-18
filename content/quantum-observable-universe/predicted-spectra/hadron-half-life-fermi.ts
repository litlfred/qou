import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:hadron-half-life",
  label: "rem:hadron-half-life-fermi",
  title: "Fermi-constant relation, $q$-dependence, and parameter count",
  uses: ["prop:hadron-half-life", "prop:em-coupling-projection"],
});
