import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:flavor-split-substrate",
  label: "rem:flavor-split-substrate-codata-comparison",
  title: "Comparison of the flavor-split formula with CODATA",
  tags: ["flavor-split", "codata-comparison", "comparison-boundary", "precision"],
  uses: ["prop:flavor-split-substrate"],
  computation: {
    engine: "python",
    script: "computations/probes/flavor_split_substrate_probe.py",
    witness: "computations/probes/flavor-split-substrate-probe.witness.json",
    status: "verified",
    requires: ["mpmath"],
  },
});
