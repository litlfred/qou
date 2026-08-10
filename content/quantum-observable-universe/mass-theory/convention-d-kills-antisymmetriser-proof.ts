import { proof } from "../../schema/builders";

export default proof({
  label: "prf:convention-d-kills-antisymmetriser",
  title:
    "Proof: elimination, factorisation, and the exclusion of the trivial branch",
  of: "prop:convention-d-kills-antisymmetriser",
  lean: {
    ref: "qou:QOU.QBeta.TemperleyLiebTower.z_eq_q_forces_trivial",
    validation: "not_checked",
  },
  uses: ["prop:convention-d-kills-antisymmetriser"],
  tags: ["temperley-lieb", "convention-d", "wedderburn-weights"],
});
