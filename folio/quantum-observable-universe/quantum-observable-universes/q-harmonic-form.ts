import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-harmonic-form",
  title: "Particle ($q$-harmonic form)",
  tags: ["particle", "harmonic"],
  lean: { ref: "qou:QOU.QHarmonicForm",
    validation: "leanok",
  },
  uses: ["def:categorical-q-ext-deriv"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** `QHarmonicForm'` " +
        "extends `ReebDecomposition M`, whose components are `M → ℝ`, and adds " +
        "`q_laplacian : M → ℝ`. The specialisation is inherited rather than " +
        "gratuitous: a q-harmonic form is by construction the *archimedean " +
        "realisation* of a section in $\\ker \\Delta_q$, evaluated pointwise. " +
        "The Lean module docstring already records this, but the " +
        "`wall-side-correct` criterion reads the acknowledgement only from " +
        "this manifest and the `.md` — never from the `.lean` — so the note " +
        "has to live here to count.",
    },
  ],
});
