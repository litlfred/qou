import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:mass-comparison-table",
  label: "rem:mass-formula-validation",
  title: "Mass formula validation: source classification and isotope coverage",
  tags: [
    "mass",
    "validation",
    "isotope",
    "CODATA",
    "AME2020",
    "certificate",
    "hecke-engine",
  ],
  uses: [
    "rem:mass-comparison-table",
  ],
});
