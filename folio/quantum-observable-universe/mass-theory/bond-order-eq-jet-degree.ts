import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bond-order-eq-jet-degree",
  lean: {
    ref: "qou:QOU.Mass.bodyorder_eq_jet_total",
    validation: "validated",
  },
  title: "Body order equals jet degree: the n-nucleon cluster sits at jet vertical degree n",
  uses: [
    "prop:gb-spectral-sequence",
    "conj:jet-prefix-gb-filtration",
  ],
  authorNotes: [
    { kind: "status", date: "2026-11-21", body: "Demoted from `conj:bond-order-eq-jet-degree` (owner, #8526, 2026-11-21; bean qou-tm3c). Step 1 of the argument places the $n$-nucleon cluster at jet degree $n$ by reading the Gröbner–Shirshov normal-form length through the jet-prefix order, which is itself a conjecture (`conj:jet-prefix-gb-filtration`). The claim that adding a nucleon raises the normal-form length by a fixed increment is not shown either. The Lean takes the degree-wise match and exhaustiveness as structure fields and derives only the sum identity, so the coincidence of the body-order and jet filtrations is open." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): assembled by\n`atom_braid_word_3A` — and equip" },
  ],
});
