import { proof } from "../../schema/builders";

export default proof({
  label: "prf:jet-sw-tau-decomposition",
  title: "Proof of the jet decomposition of the Archimedean realisation",
  uses: [
    "prop:jet-sw-tau-decomposition",
    "prop:mi-sw-abelianisation",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean witness [`QOU.Brings.jet_sw_tau_decomposition`](#prop:jet-sw-tau-decomposition) packages the exhaustiveness and additivity as the structure hypothesis and extracts the graded-sum identity." },
  ],
});
