import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:electron-period-base",
  lean: {
    ref: "qou:QOU.Mass.second_period_contains_me",
    validation: "validated",
  },
  title: "CAL-1 (m_e) is the n=0 base period of the prolongation tower",
  uses: [
    "prop:sl2-prolongation-recurrence",
    "prop:jet-sw-tau-decomposition",
  ],
  proofs: ["prf:electron-period-base"],
});
