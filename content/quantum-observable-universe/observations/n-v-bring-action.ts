import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:n-v-bring-action",
  title: "S_5 action on H_n(q) at the electroweak slice",
  cites: ["bring1786", "klein1888"],
  uses: [
    "prop:brings-is-qou",
    "def:hyperelliptic-quintic",
    "conj:mass-endomorphism",
  ],
  defines: [],
  tags: [
    "tier:E","n-v", "electroweak", "bring", "s5", "substrate-axiom"],
  lean: { ref: "qou:QOU.Observations.s5_acts_on_ew_slice" },
});
