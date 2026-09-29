import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:plancherel-term-7-formulation",
  title:
    "Universal residue at curvature-rank $k \\geq 4$ (Molien-weighted log functional)",
  lean: {
    ref: "qou:QOU.WedderburnMass.plancherel_term_7",
    validation: "not_checked",
  },
  uses: [
    "prop:spectral-sequence-collapse",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-05",
      body:
        "**Weight family fixed to Molien.** The functional was defined " +
        "against `dim_q^2/[n]_q!` until this date; the replacement to " +
        "`f^lambda q^{-kappa} dim_q/[n]_q!` follows an owner ruling on " +
        "bean `qou-oots`. The two are not one normalisation apart — they " +
        "differ by up to 1831x per partition at n = 9 (= A = 3). The " +
        "requirement set R1/R2/R3 does NOT separate Molien from " +
        "`dim_q^2/D^2` (R2 asks only that the normaliser be " +
        "n-independent, and both satisfy it), so the second is retained " +
        "as a labelled comparison arm rather than dropped, and " +
        "`fr_pullback_k3_test.py` reports both. The two arms DISAGREE on " +
        "the best k=3 knot: Molien ranks 5_2 (+21.4%, with 6_1 worse " +
        "than baseline), `dim_q^2/D^2` ranks 6_1 (+1.7%).",
      see: "computations/fr_pullback_k3_test.py",
    },
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `mass-theory/plancherel-term-7-formulation.lean` " +
        "uses `Real.exp`, `Real.log`. These are real-analytic constructs " +
        "with no generic-`CommRing` counterpart, so the `ℝ` " +
        "specialisation is forced by the statement itself rather than " +
        "chosen. The block therefore sits on the archimedean side of the " +
        "§7c wall by construction.",
    },
  ],
});
