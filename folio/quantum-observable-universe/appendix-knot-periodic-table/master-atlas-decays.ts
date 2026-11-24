import { table } from "../../schema/builders";

export default table({
  label: "tbl:master-atlas-decays",
  title:
    "Table A.3: Weak and nuclear $\\beta^-$ decay $Q$-values ($\\mathcal{L}_1\\text{--}\\mathcal{L}_3$, 80-digit Fréchet--Jacobian atlas)",
  uses: ["prose:master-atlas-calibration-jacobian"],
  cites: ["codata2022", "nndc2024"],
  computation: {
    engine: "mpmath",
    script: "computations/master_atlas_jacobian_80dps.py",
    witness: "computations/master-atlas-80dps.witness.json",
    status: "verified",
  },
  tags: ["archimedean-bridge", "atlas", "q-value", "beta-decay", "extracted-table"],
});
