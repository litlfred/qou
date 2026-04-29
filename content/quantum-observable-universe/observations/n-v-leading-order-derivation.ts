import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:n-v-leading-order-derivation",
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
