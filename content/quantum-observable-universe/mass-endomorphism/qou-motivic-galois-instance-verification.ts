import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qou-motivic-galois-instance-verification",
  title: "Construction, verification, and coherence of the QOU $\\mathrm{Frob}_p$ instance",
  interprets: "rem:qou-motivic-galois-instance",
  tags: ["motivic-galois", "frobenius", "habiro", "weil-purity", "coherence"],
  uses: [
    "rem:qou-motivic-galois-instance",
    "def:motivic-galois-character",
  ],
  cites: ["habiro2002", "yekutieli2010"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body: "This instance is what discharges GAP 5b of `docs/audits/family-4-motivic-path.md`. That audit is a branch-local working note, so the published prose now states the mathematical consequence (downstream theorems consume the explicit QOU instance instead of carrying `def:motivic-galois-character` as an `[instance]` hypothesis) without citing it.",
    },
  ],
});
