import { table } from "../../schema/builders";

export default table({
  label: "tbl:master-atlas-nuclides-summary",
  title:
    "Table A.4: Benchmark nuclide binding energies and $(m_e, \\mathfrak{D}_\\beta)$ calibration floors ($\\mathcal{L}_2\\text{--}\\mathcal{L}_3$, 80-digit atlas)",
  uses: [
    "prose:master-atlas-calibration-jacobian",
  ],
  cites: ["ame2020", "ame2020tables"],
  computation: {
    engine: "mpmath",
    script: "computations/master_atlas_jacobian_80dps.py",
    witness: "computations/master-atlas-80dps.witness.json",
    status: "verified",
  },
  tags: ["archimedean-bridge", "atlas", "nuclides", "binding-energy", "extracted-table"],
});
