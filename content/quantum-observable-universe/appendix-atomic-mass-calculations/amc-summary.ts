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
    script: "folio-assistant/computations/codata_masses.py",
    witness: "folio-assistant/computations/codata-masses.witness.json",
    status: "verified",
  },
});
