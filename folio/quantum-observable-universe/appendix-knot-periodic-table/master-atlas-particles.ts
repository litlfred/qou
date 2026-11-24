import { table } from "../../schema/builders";

export default table({
  label: "tbl:master-atlas-particles",
  title:
    "Table A.1: Elementary particles and gauge couplings ($\\mathcal{L}_0\\text{--}\\mathcal{L}_1$, 80-digit Fréchet--Jacobian atlas)",
  uses: ["prose:master-atlas-calibration-jacobian"],
  cites: ["codata2022", "pdg2024"],
  computation: {
    engine: "mpmath",
    script: "computations/master_atlas_jacobian_80dps.py",
    witness: "computations/master-atlas-80dps.witness.json",
    status: "verified",
  },
  tags: ["archimedean-bridge", "atlas", "particles", "couplings", "extracted-table"],
});
