import { table } from "../../schema/builders";

export default table({
  label: "tbl:master-atlas-molecules",
  title:
    "Table A.5: Benchmark molecular bond angles and hydrogen-bond cohesion ($\\mathcal{L}_4$, 80-digit Fréchet--Jacobian atlas)",
  uses: [
    "prose:master-atlas-calibration-jacobian",
    "prop:symmetric-block-domain-weight",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/master_atlas_jacobian_80dps.py",
    witness: "computations/master-atlas-80dps.witness.json",
    status: "verified",
  },
  tags: ["archimedean-bridge", "atlas", "molecules", "vsepr", "extracted-table"],
});
