import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:reeb-linking-cwf-normalization",
  title:
    "CWF linking normalization: the pn-bond amplitude is the unit-normalized exchange-channel component, $\\ell(z)^2\\,(1+z^2)=z^2$",
  lean: {
    ref: "qou:QOU.MassTheory.ReebLinkingCWF",
  },
  uses: [
    "prop:reeb-pn-magnitude-criticality",
  ],
  cites: [
    "jones1987",
  ],
  computation: {
    engine: "python",
    script:
      "computations/probes/reeb_5g_unit_anchor_scan.py",
    witness:
      "computations/probes/reeb-5g-unit-anchor-scan.witness.json",
    status: "experimental",
  },
  tags: [
    "exchange-sector",
    "pn-bond",
    "cwf",
    "reeb-flow",
    "open-postulate",
    "gap-a4",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-07",
      body:
        "Primary conjecture (no instance; content-bearing class per §3b-tax). " +
        "Per the Anti-Laundering rule this class does NOT prove the ²H linear " +
        "law and does NOT authorize production wiring: the MeV unit anchor " +
        "remains open (audit §2f constraint ledger; §3d single-factor scan " +
        "negative), and the ²H tier carries a NEAR-MATCH label by owner " +
        "ruling (audit §3f, 2026-07-07).",
    },
  ],
});
