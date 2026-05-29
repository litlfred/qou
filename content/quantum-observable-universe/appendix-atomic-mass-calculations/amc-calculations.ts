import { prose } from "../../schema/builders";

export default prose({
  label: "prose:amc-calculations",
  title: "Worked calculations for all elements",
  uses: [
    "prose:amc-method",
    "prose:knot-periodic-table",
  ],
  tags: [
    "atomic-mass",
    "calculation",
    "knot",
    "periodic-table",
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
