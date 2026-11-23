import { remark } from "../../schema/builders";

export default remark({
  label: "rem:physics-names-knot-operations",
  title: "Physics names $\\leftrightarrow$ categorical knot operations (table; depends on $q_0$)",
  interprets: "prop:confinement-categorical",
  uses: [
    "rem:borromean-baryon-interpretation",
    "prop:chirality-residue-mass-term",
    "cor:gauge-coupling-uniqueness",
    "conj:cp-violation-spectral-form",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The lookup `physics-names.json` maps cache keys to physics names at the current $q_0$." },
  ],
});
