import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-fourier",
  title: "Categorical Fourier transform",
  tags: ["hopf-algebra", "grouplike", "monoidal-functor", "fourier", "peter-weyl", "tannakian"],
  lean: { ref: "qou:QOU.CategoricalFourier",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-laplace",
    "prop:tannaka-krein-reconstruction",
    "rem:brings-smoothness",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`quantum-observable-universes/categorical-fourier-transform.lean` " +
        "uses `Complex.*`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
