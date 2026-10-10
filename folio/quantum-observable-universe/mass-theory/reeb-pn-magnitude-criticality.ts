import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-pn-magnitude-criticality",
  title:
    "Deformed exchange criticality: $g^2\\,(1+[2]_v^2)=1$ characterizes the pn-bond magnitude, with $5+(v-v^{-1})^2 = 1+[2]_v^2$",
  lean: {
    ref: "qou:QOU.MassTheory.ReebPnMagnitude.ss_det_zero_at_criticality",
  },
  uses: [
    "prop:wigner-np-pairing",
  ],
  cites: [
    "jones1987",
  ],
  computation: {
    engine: "python",
    script:
      "computations/probes/reeb_g_structural_identity_probe.py",
    witness:
      "computations/probes/reeb-g-structural-identity.witness.json",
    status: "verified",
  },
  tags: [
    "exchange-sector",
    "pn-bond",
    "temperley-lieb",
    "marginal-stability",
    "gap-a4",
  ],
});
