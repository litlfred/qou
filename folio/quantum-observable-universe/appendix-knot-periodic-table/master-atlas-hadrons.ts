import { table } from "../../schema/builders";

export default table({
  label: "tbl:master-atlas-hadrons",
  title:
    "Table A.2: Meson, baryon, and Eightfold multiplet spectrum ($\\mathcal{L}_1\\text{--}\\mathcal{L}_2$, 80-digit Fréchet--Jacobian atlas)",
  uses: ["prose:master-atlas-calibration-jacobian"],
  cites: ["codata2022", "pdg2024"],
  computation: {
    engine: "mpmath",
    script: "computations/master_atlas_jacobian_80dps.py",
    witness: "computations/master-atlas-80dps.witness.json",
    status: "verified",
  },
  tags: ["archimedean-bridge", "atlas", "hadrons", "mesons", "baryons", "extracted-table"],
});
