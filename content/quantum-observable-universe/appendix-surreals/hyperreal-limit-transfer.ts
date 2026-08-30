import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:hyperreal-limit-transfer",
  title:
    "Limit transfer at $\\mathbb{R}^*$: $\\mathrm{st}$ computes limits, and the surreal carrier is not needed",
  tags: [
    "surreals",
    "hyperreals",
    "standard-part",
    "nonstandard-analysis",
    "limit-transfer",
  ],
  lean: {
    ref: "qou:QOU.AppendixSurreals.HyperrealTransfer.st_ofSeq_of_tendstoReal",
    validation: "leanok",
  },
  uses: ["conj:surreal-limit-transfer"],
  cites: ["robinson1966", "conway1976"],
});
