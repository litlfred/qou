import { remark } from "../../schema/builders";

/**
 * Follow-on to def:co2-molecular-braid: the linear-vs-bent LP-dual strand
 * ordering question, the [O1,C,O2] vs [C,O1,O2] comparison, and the observed
 * D₀ ≈ 16.56 eV. Carries the molecular-experimental-refs witness consumed by
 * the :val directive. Overlaps prop:co2-lp-dual-binding (geometry selection).
 */
export default remark({
  label: "rem:co2-linear-geometry-and-d0",
  title: "Linear vs bent $CO_2$ geometry and observed dissociation energy",
  interprets: "def:co2-molecular-braid",
  uses: ["def:co2-molecular-braid"],
  computation: {
    engine: "python",
    script: "computations/molecular_experimental_refs.py",
    witness: [
      "computations/molecular-experimental-refs.witness.json",
    ],
    status: "experimental",
  },
  tags: ["CO2", "linear", "geometry", "LP-dual", "dissociation-energy"],
});
