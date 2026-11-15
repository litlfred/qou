import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:convention-d-kills-antisymmetriser",
  title:
    "$z = q^{3}/(q^{2}+1)$ is the unique non-trivial Markov trace on $H_3(q)$ whose radical contains the three-strand antisymmetriser",
  lean: {
    ref: "qou:QOU.QBeta.TemperleyLiebTower.antisym_vanishes_only_at_two_roots",
    validation: "not_checked",
  },
  uses: [
    "prop:h3-markov-wenzl-weights",
    "prop:corrected-markov-trace",
  ],
  proofs: ["prf:convention-d-kills-antisymmetriser"],
  tags: [
    "temperley-lieb",
    "convention-d",
    "markov-trace",
    "wedderburn-weights",
    "characterisation",
    "trace-convention",
  ],
});
