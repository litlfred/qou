import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:em-coupling-projection",
  label: "rem:em-coupling-projection-discussion",
  title: "Spectral characterisation, the Chern--Simons correction, and the open bare residual",
  uses: [
    "prop:em-coupling-projection",
    "thm:em-spectral-completeness",
    "prop:force-carrier-bring-uniqueness",
    "rem:em-coupling-chern-simons",
    "rem:alpha-em-derivation-open-problems",
    "prop:em-coupling-bring-zero-mode",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): However, the $\\kappa \\approx 1.722$ value was admitted as `sorry` in the Lean formalisation and never closed." },
  ],
});
