import { conjecture } from "../../schema/builders";

// Demoted from `proposition` to `conjecture` per AGENTS.md §3b
// (conjectural propagation): the leading-order closed form
// `N_v = |S_5| · q_0^{90}` depends on two upstream `conj:` blocks
// (`conj:n-v-bring-action` and `conj:n-v-tower-depth-ninety`),
// hence the conditional result is itself conjectural.  The prose
// already acknowledges "Conditional theorem"; the block kind now
// matches.  See `docs/audits/conjecture-cones.md` (`conj:mass-
// endomorphism` cone) for the audit that flagged this.
export default conjecture({
  label: "conj:n-v-leading-order-derivation",
  title: "Leading-order N_v = |S_5| · q_0^90 (= 120 · q_0^90)",
  cites: [],
  uses: [
    "conj:n-v-bring-action",
    "conj:n-v-tower-depth-ninety",
    "ex:hadron-half-life-verification",
  ],
  defines: [],
  tags: ["n-v", "electroweak", "derivation", "conditional"],
  lean: { ref: "qou:QOU.Observations.n_v_leading_order" },
});
