import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:n-v-tower-depth-ninety",
  title: "Brane-tower depth from m_e to v equals 90",
  cites: [],
  uses: ["conj:mass-endomorphism"],
  defines: [],
  tags: ["n-v", "electroweak", "tower-depth", "substrate-axiom"],
  lean: { ref: "qou:QOU.Observations.tower_depth_m_e_to_v_is_ninety" },
});
