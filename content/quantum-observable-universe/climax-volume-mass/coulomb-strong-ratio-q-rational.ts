import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:coulomb-strong-ratio-q-rational",
  proofs: ["prf:coulomb-strong-ratio-q-rational"],
  title:
    "Coulomb/strong ratio $\\tanh(\\ln q)$ is the q-rational $(q^2-1)/(q^2+1)$",
  tags: ["coulomb", "ratio", "tanh", "q-rational", "identity", "lean"],
  lean: {
    ref: "qou:QOU.Braiding.coulomb_strong_ratio_q_rational",
    validation: "not_checked",
  },
  uses: ["def:coulomb-charge"],
});
