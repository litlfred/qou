import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "The proved identity relies on the elementary textbook algebraic factorization $1-q^k = (1-u^k)(1+u^k)$. The novel, framework-specific mathematical contribution lies in its application to the Habiro-weighted-average ratio, linking standard q-series identities to the physical structure." },
  ],
  label: "prop:habiro-pochhammer-bridge",
  title:
    "Habiro–Markov bridge via Pochhammer factorisation",
  lean: {
    ref: "qou:QOU.BraidKnot.HabiroPochhammerBridge",
  },
  uses: [
    "prop:habiro-precision-ladder-equivalence",
    "thm:jones-markov-trace",
    "def:habiro-ring",
  ],
  cites: [
    "habiro2000",
    "jones1987",
  ],
  tags: [
    "habiro-ring",
    "pochhammer",
    "normalization-bridge",
    "1ppQ",
  ],
});
