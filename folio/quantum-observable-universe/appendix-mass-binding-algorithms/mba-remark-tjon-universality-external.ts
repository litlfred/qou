import { remark } from "../../schema/builders";

export default remark({
  label: "rem:tjon-universality-external",
  title: "External three-body/four-body correlation and inequivalence with the $\\mu_4 = 0$ simplex baseline",
  interprets: "alg:delta-lambda-closure",
  tags: [
    "mba",
    "delta-lambda",
    "external-literature",
    "epistemic-status",
  ],
  uses: [
    "alg:delta-lambda-closure",
    "alg:per-isotope-binding",
  ],
  cites: [
    "platter2005tjon",
    "hammer2007fourbody",
    "jurgenson2009srg",
    "ame2020",
  ],
});
