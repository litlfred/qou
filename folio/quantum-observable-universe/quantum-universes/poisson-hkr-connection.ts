import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:poisson-object",
  label: "rem:poisson-hkr-connection",
  title:
    "HKR and skew-Poisson integration",
  uses: [
    "def:poisson-object",
    "def:classical-limit-obstruction",
    "prop:skew-poisson-integration",
  ],
  tags: ["poisson", "hkr", "deformation-theory"],
  cites: ["yekutieli2010", "leitner2006"],
});
