import { proof } from "../../schema/builders";

export default proof({
  label: "prf:h3-markov-wenzl-weights",
  title: "Proof of h3 markov wenzl weights",
  uses: ["prop:h3-markov-wenzl-weights"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Temperley–Lieb uniqueness argument (... $z = q^3/(q^2+1)$; `QOU.BraidsAndKnots.MarkovTraceTLUniqueness`)" },
  ],
});
