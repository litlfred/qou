import { proof } from "../../schema/builders";

export default proof({
  label: "prf:ice-pauling-residual",
  title: "Proof of ice pauling residual",
  uses: ["prop:ice-pauling-residual"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling proves $\\binom{4}{2}=6$ and $\\binom{4}{2}(\\tfrac12)^2 = \\tfrac32$ exactly over $\\mathbb{Q}$." },
  ],
});
