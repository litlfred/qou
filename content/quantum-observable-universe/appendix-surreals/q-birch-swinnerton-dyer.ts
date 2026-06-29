import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-birch-swinnerton-dyer",
  title:
    "The $q$-deformed Birch and Swinnerton-Dyer conjecture",
  lean: { ref: "qou:QOU.AppendixSurreals.QBirchSwinnertonDyer", validation: "stub" },
  uses: [
    "def:categorical-mordell-weil",
    "thm:tannaka-krein-isomorphism",
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
});
