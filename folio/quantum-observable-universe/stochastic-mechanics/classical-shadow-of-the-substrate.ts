import { remark } from "../../schema/builders";

export default remark({
  label: "rem:classical-shadow-of-the-substrate",
  title: "The classical shadow of the aether: what the obstruction space becomes at $q = 1$",
  interprets: "def:classical-limit-functor",
  uses: [
    "def:classical-limit-functor",
    "def:classical-limit-obstruction",
    "def:hochschild-homology",
    "rem:hkr-theorem",
  ],
  foreshadows: ["conj:wigner-axiom"],
  cites: ["weibel1994", "cartan1956", "kontsevich-2003", "nest-tsygan-1995", "dolgushev-rubtsov-2005", "feng-tsygan-1991", "hadfield-krahmer-2005"],
  tags: ["classical-limit", "hochschild-cohomology", "whitehead-lemma", "formality", "fibre-vs-observable", "obstruction"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Part of the 2026-09-15 explicit-layer selection (owner option B), recording reading (e) of the analysis doc §9: the formal neighbourhood of q = 1 is where formality applies verbatim, and there the obstruction space is zero; the Wigner axiom is a statement about the evaluation at q₀, which no computation in the corpus reaches. The dimension drop at q ≠ 1 (Feng–Tsygan; Hadfield–Krähmer) is cited from the library copies `library/1104248094` and `library/arxiv-math-0405249v5`.",
    },
  ],
});
