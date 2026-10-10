import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:diophantine-birthday-trajectory",
  title:
    "The birthday-trajectory separation: impossible at the birthday, unobstructed at the trajectory, and blocked only by a quantifier",
  tags: [
    "surreal-numbers",
    "birthday",
    "sign-expansion",
    "diophantine",
    "liouville",
    "roth",
    "gonshor",
    "dyadic-approximation",
  ],
  lean: {
    ref: "qou:QOU.AppendixSurreals.liouvilleWith_separates",
    validation: "leanok",
  },
  uses: ["conj:diophantine-birthday"],
  cites: ["conway1976", "gonshor1986"],
});
