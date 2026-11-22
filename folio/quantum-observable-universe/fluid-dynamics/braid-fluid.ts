import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:braid-action-tensor",
  label: "rem:braid-fluid",
  title: "Braid--fluid correspondence: from categorical braiding to vortex dynamics",
  uses: [
    // Yang-Baxter, invoked to enforce Reidemeister III so three-vortex
    // braiding is path-independent.
    "prop:r-matrix-braiding-structure",
    "rem:madelung-fluid",
    "sec:webster-inner-product",
    // J_L(q), which this block reads as the topological helicity.
    "thm:jones-markov-trace",
    // The closure that turns the tangle's word into J_L.
    "prop:closure-unseen-subword",
  ],
  tags: ["braid-group", "fluid-dynamics", "arnold", "vortex", "correspondence"],
});
