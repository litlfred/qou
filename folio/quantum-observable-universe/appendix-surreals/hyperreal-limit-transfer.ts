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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Original wording: the class \"is stated over `SurrealField` and carried with **no instance**\"; \"in Mathlib's hyperreals\"; \"literally Mathlib's characterisation of `IsSt`. The two agree by `rfl`.\"; \"convergence along `atTop`\"; \"which Mathlib does not package\"; \"exposed something about `SurrealField` itself\"." },
  ],
});
