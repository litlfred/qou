import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:birthday-axioms-do-not-pin-the-birthday",
  title:
    "The six birthday axioms admit a two-valued model, so they bound birthday only from above",
  tags: [
    "surreals",
    "birthday",
    "axiom-audit",
    "independence",
    "hyperreals",
    "mixin",
  ],
  lean: {
    ref: "qou:QOU.AppendixSurreals.birthdayFaithful_independent_witnessed",
    validation: "leanok",
  },
  uses: ["thm:hyperreal-limit-transfer"],
  cites: ["conway1976", "gonshor1986"],
});
