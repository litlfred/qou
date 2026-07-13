import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qou-motivic-galois-instance-verification",
  title: "Construction, verification, and coherence of the QOU $\\mathrm{Frob}_p$ instance",
  interprets: "def:qou-motivic-galois-instance",
  tags: ["motivic-galois", "frobenius", "habiro", "weil-purity", "coherence"],
  uses: [
    "def:qou-motivic-galois-instance",
    "def:motivic-galois-character",
  ],
  cites: ["habiro2002", "yekutieli2010"],
});
