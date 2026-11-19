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
  authorNotes: [
    {
      kind: "note",
      body:
        "Proved in Mathlib's hyperreals (Real*) in QOU.AppendixSurreals.HyperrealTransfer.st_ofSeq_of_tendstoReal: infinitesimal closeness agrees definitionally (by rfl) with Mathlib's IsSt, pushing Filter.Tendsto along Filter.atTop to IsSt without the converse.",
    },
  ],
});
