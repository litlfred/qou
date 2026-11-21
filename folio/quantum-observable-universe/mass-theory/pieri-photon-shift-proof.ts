import { proof } from "../../schema/builders";

export default proof({
  label: "prf:pieri-photon-shift",
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Moved out of the prose by the voice-leak drain (qou-d4kh, W14b, 2026-11-21): the four-term photon step is the Lean lemma `commute_photon_of_commute` in the sibling file." },
  ],
  title: "Proof of pieri photon shift",
  uses: ["prop:pieri-photon-shift"],
});
