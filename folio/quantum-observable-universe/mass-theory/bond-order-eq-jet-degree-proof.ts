import { proof } from "../../schema/builders";

export default proof({
  label: "prf:bond-order-eq-jet-degree",
  title: "Proof that body order equals jet degree",
  uses: [
    "lem:bond-order-eq-jet-degree",
    "prop:gb-spectral-sequence",
  ],
  authorNotes: [
    { kind: "caveat", date: "2026-11-20", body: "**Caveat (2026-11-20, bean `qou-6qbv`): the cited `prop:gb-spectral-sequence` no longer supplies $E_2$ collapse.** It was rewritten on the Coxeter length filtration and now states the Hochschild spectral sequence of $H_n(R, q)$; at $n = 3$ that sequence has $d_4 \\neq 0$ and stabilises only at $E_5$ (`computations/probes/gb_spectral_sequence_h3_probe.py`, exact). The step here that relies on $E_2$ collapse is therefore unsupported by its citation. Whether a different filtered object collapses at $E_2$ is not settled here." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean witness\n[`QOU.Mass.bodyorder_eq_jet_total`](#lem:bond-order-eq-jet-degree) packages the\ngraded-match (Step 1--2) and exhaustiveness as the structure hypothesis and\nextracts the body-order = jet-graded sum identity." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): atomic braid `atom_braid_word_3A` builds" },
  ],
});
