import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:diophantine-birthday",
  title:
    "Algebraic vs transcendental numbers are separated by birthday trajectory",
  lean: { ref: "qou:QOU.AppendixSurreals.DiophantineBirthday", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "birthday",
    "diophantine",
    "liouville",
    "roth",
    "algebraic",
    "transcendental",
    "open-problem",
  ],
  uses: ["rem:conway-normal-form"],
  cites: [
    "conway1976",
    "gonshor1986",
    "ehrlich2012",
  ],
});
