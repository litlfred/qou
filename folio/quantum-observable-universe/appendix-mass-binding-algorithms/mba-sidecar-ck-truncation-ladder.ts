import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:ck-truncation-ladder",
  title: "All-order Convention-D $c_k^{(D)}$ generating function and distinct-partition cumulant extraction",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
    "prop:q-beta-c-2-eq-neg-one-structural",
    "prop:q-beta-cos-resummation",
    "alg:q-beta-truncation",
  ],
  tags: [
    "mba",
    "sidecar",
    "ck-truncation",
    "convention-d",
    "lagrange-burmann",
    "q-beta",
  ],
});
