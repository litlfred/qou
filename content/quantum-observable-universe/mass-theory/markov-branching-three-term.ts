import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-branching-three-term",
  title:
    "Branching coherence of the Markov trace reduces to $[m+2]_q + [m]_q = [2]_q\\,[m+1]_q$",
  lean: {
    ref: "qou:QOU.QBeta.TemperleyLiebTower.markov_branching_general",
    validation: "not_checked",
  },
  uses: ["prop:convention-d-kills-antisymmetriser"],
  tags: [
    "branching",
    "q-integer",
    "bratteli",
    "temperley-lieb",
    "markov-trace",
  ],
});
