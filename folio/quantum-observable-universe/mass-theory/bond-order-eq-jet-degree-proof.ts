import { remark } from "../../schema/builders";

// Was rem:bond-order-eq-jet-degree-sketch. The block it argued for is now the conjecture
// conj:bond-order-eq-jet-degree (owner, #8526, 2026-11-21; bean qou-tm3c), so the
// argument is recorded as an interpretive sketch, not a proof (AGENTS.md §3b).
export default remark({
  label: "rem:bond-order-eq-jet-degree-sketch",
  interprets: "conj:bond-order-eq-jet-degree",
  title: "Argument sketch: body order equals jet degree",
  uses: [
    "conj:bond-order-eq-jet-degree",
    "prop:gb-spectral-sequence",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "**$E_2$ collapse removed from this block (owner, 2026-11-20, bean `qou-6qbv`).** It was cited from `prop:gb-spectral-sequence`, which no longer asserts it; for the Hochschild complex of $H_3$ filtered by length, $d_2$ and $d_4$ are nonzero and the sequence stabilises at $E_5$ (`computations/probes/gb_spectral_sequence_h3_probe.py`, exact). The step only needed that the standard basis splits the length filtration, which is now what it cites. The witness `gb-filtration-jet-order.witness.json` never carried a $d_2$ certificate, although this appendix said it did." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean witness\n[`QOU.Mass.bodyorder_eq_jet_total`](#conj:bond-order-eq-jet-degree) packages the\ngraded-match (Step 1--2) and exhaustiveness as the structure hypothesis and\nextracts the body-order = jet-graded sum identity." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): atomic braid `atom_braid_word_3A` builds" },
  ],
});
