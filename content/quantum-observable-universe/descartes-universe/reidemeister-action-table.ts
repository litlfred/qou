import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reidemeister-action-table",
  title:
    "Reidemeister moves on the categorical action: complete accounting",
  tags: [
    "reidemeister",
    "hecke-algebra",
    "lagrangian",
    "action",
    "writhe",
    "volume",
    "energy",
    "mass",
    "invariant",
  ],
  lean: { ref: "qou:QOU.Descartes.reidemeister_action_table",
    validation: "not_checked",
  },
  uses: ["thm:markov-trace-factorization"],
});
