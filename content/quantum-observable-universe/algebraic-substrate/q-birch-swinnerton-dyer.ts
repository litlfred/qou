import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-birch-swinnerton-dyer",
  title:
    "The $q$-deformed Birch and Swinnerton-Dyer conjecture",
  uses: [
    "thm:tannaka-krein-isomorphism",
    "thm:macroscopic-stability-equivalence",
    "prop:ns-kummer-specialisation",
  ],
  tags: [
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
