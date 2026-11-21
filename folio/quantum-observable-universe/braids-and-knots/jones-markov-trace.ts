import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:jones-markov-trace",
  lean: { ref: "qou:QOU.Braiding.JonesMarkovTrace",
    validation: "not_checked",
  },
  title: "Existence and non-degeneracy of the Markov trace (Jones, 1987)",
  tags: ["hecke-algebra", "markov-trace", "jones-polynomial", "external-proof"],
  cites: ["jones1987", "kimlee2018"],
  uses: ["prop:braid-action-tensor", "prop:braiding-eigenvalue-extraction"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Loop-reciprocal identity tr_M(e_i) = 1/δ: (`loop_reciprocal`, [`TemperleyLiebTower.lean`](../lean/QOU/QBeta/TemperleyLiebTower.lean)).\n\nCatalan count of the Temperley–Lieb quotient: ([`TemperleyLiebTower.lean`](../lean/QOU/QBeta/TemperleyLiebTower.lean))." },
  ],
});
