import { prose } from "../../schema/builders";

export default prose({
  label: "prose:amc-summary",
  title: "Summary and percentage deviations",
  uses: [
    "prose:amc-calculations",
    "prose:amc-method",
  ],
  tags: [
    "atomic-mass",
    "summary",
    "deviation",
    "verification",
    "appendix",
  ],
});
