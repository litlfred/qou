import { proof } from "../../schema/builders";

export default proof({
  label: "prf:binding-period-involution-statistic",
  title:
    "Proof that the balanced dimension sum is the $2\\,\\mathrm{maj} + \\mathrm{content} \\circ \\mathrm{RSK}$ involution generating function",
  uses: [
    "prop:binding-period-involution-statistic",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Machine verification.** The Lean sibling decides the exponent multisets and\nproves the identity for $n = 3, 4$ from the computable RSK insertion\n(kernel-checked); exact" },
  ],
});
