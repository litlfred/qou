import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-q-categorical-truncation-argument",
  interprets: "conj:phi-q-categorical-truncation",
  uses: [
    "conj:phi-q-categorical-truncation",
    "prop:cell-depth-truncation",
    "prop:categorical-mass-markov",
    // Step 4's starting identity: the transient trace at p_i evaluates to
    // Phi_q(z_i). Unstratified, which is why the next entry is also needed.
    "cor:quantum-dilogarithm",
    // The level-by-level refinement Step 4 actually consumes, and which the
    // gap-closure section already names as the structural bridge for it.
    "conj:quantum-dilogarithm-stratified",
    // conj:brane-tower-z-habiro is NOT listed although the prose cites it
    // twice: once naming it as the open target, once observing the empirical
    // k=2 sweet spot is consistent with this proposition. Corroboration and
    // an open-target pointer, not a prerequisite -- and a proof of a
    // provable-kind parent may not depend on a conjecture.
  ],
  tags: [
    "brane-tower",
    "spectral-sequence",
    "centre-stratification",
  ],
});
