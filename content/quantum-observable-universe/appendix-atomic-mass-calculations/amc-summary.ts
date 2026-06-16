import { prose } from "../../schema/builders";

export default prose({
  label: "prose:amc-summary",
  title: "Summary and percentage deviations",
  uses: ["prose:amc-calculations"],
  tags: [
    "atomic-mass",
    "summary",
    "deviation",
    "verification",
    "appendix",
  ],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
});
