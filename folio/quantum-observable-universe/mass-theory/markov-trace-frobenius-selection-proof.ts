import { proof } from "../../schema/builders";

export default proof({
  label: "prf:markov-trace-frobenius-selection",
  title: "Proof of markov trace frobenius selection",
  uses: ["prop:markov-trace-frobenius-selection"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): *Formal status.* The elimination above is\n`QOU.BraidsAndKnots.markovWeights_eq_jones_of_threeRow_eq_zero`\n(division-free, over a commutative domain), the spurious\nbranch is `markovWeights_degenerate_root`, and the fibre-side\nantecedent is `markovWeights_eq_jones_of_fibre_categorical`. The\ngeneral-$n$ closed form is *not* proved by induction in Lean: what is" },
  ],
});
