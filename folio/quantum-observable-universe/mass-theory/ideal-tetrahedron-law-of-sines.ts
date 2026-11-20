import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ideal-tetrahedron-law-of-sines",
  title:
    "The law of sines for an ideal tetrahedron: $\\lVert z \\rVert = " +
    "\\sin\\theta_2 / \\sin\\theta_3$",
  tags: [
    "hyperbolic-volume",
    "ideal-tetrahedron",
    "dilogarithm",
    "kummer",
    "law-of-sines",
  ],
  lean: {
    ref: "qou:QOU.Knot.IdealTet.norm_eq_sin_div_sin",
    validation: "leanok",
  },
  uses: ["thm:rivin-concavity-one-tetrahedron"],
  cites: ["thurston1978", "neumann-zagier1985", "milnor1982"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): which needs a theory of hyperbolic $3$-manifolds that neither Mathlib nor this corpus has." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): What the corpus supplies is the machine-checked proof" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): No analysis is involved. Mathlib's $\\sin(\\arg x) = \\mathrm{Im}\\, x / \\lVert x \\rVert$ holds *unconditionally*, so no $x \\neq 0$ bookkeeping is needed for the sine computations themselves." },
  ],
});
