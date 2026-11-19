import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:lp-dual-stability",
  label: "rem:lp-dual-stability-confinement-reading",
  title: "Confinement reading of the LP-dual stability criterion",
  tags: ["lp-duality", "confinement", "hadron", "quark", "shadow-price"],
  uses: ["prop:lp-dual-stability"],
  computation: {
    engine: "numpy",
    script: "computations/gram-matrix-dual.py",
    witness: "computations/gram-matrix-dual.witness.json",
    status: "verified",
  },
});
