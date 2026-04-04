import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-birch-swinnerton-dyer",
  title:
    "The $q$-deformed Birch and Swinnerton-Dyer conjecture",
  uses: [
    "prop:descartes-elliptic-curve",
    "def:local-q-zeta-function",
    "thm:macroscopic-stability-equivalence",
    "conj:classical-riemann-hypothesis",
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
  ],
  cites: ["birch1965", "wiles1995", "tate1974"],
});
