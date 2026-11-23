import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:electron-period-base",
  lean: {
    ref: "qou:QOU.Mass.second_period_contains_me",
    validation: "validated",
  },
  title: "CAL-1 (m_e) is the n=0 base period of the prolongation tower",
  uses: [
    "prop:sl2-prolongation-recurrence",
    "prop:jet-sw-tau-decomposition",
  ],
  proofs: ["prf:electron-period-base"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The formal backing is `QOU.Mass.second_period_contains_me`, which *derives* that identity from the recurrence together with the base condition $a_0 = m_e$. The base condition itself is a defining field of the tower, not a result: it is the CAL-1 identification, and the accessor `electron_period_is_base` returns it verbatim." },
  ],
});
