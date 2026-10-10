import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-birch-swinnerton-dyer",
  title:
    "The $q$-deformed Birch and Swinnerton-Dyer conjecture",
  lean: { ref: "qou:QOU.AppendixSurreals.QBirchSwinnertonDyer", validation: "stub" },
  uses: [
    "def:categorical-mordell-weil",
    "conj:tannaka-krein-isomorphism",
    "prop:ns-kummer-specialisation",
  ],
  tags: [
    "tier:famous",
    "birch-swinnerton-dyer",
    "millennium-problem",
    "elliptic-curve",
    "l-function",
    "mordell-weil",
    "tate-shafarevich",
    "categorical",
    "fibre-functor",
    "gm-torsion",
    "kummer",
    "projective-line",
  ],
  cites: ["birch1965", "wiles1995", "tate1974"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "`WeakQBSD` and `FullQBSD_rank_zero` take an L-value, a Reeb " +
        "period `Ω_q` and a Tamagawa product over `ℝ`. An L-function " +
        "value at `s = 1` and a period are analytic objects by " +
        "definition; the categorical Mordell–Weil data the file also " +
        "carries is generic, and the two coexist deliberately across the " +
        "wall.",
    },
  ],
});
