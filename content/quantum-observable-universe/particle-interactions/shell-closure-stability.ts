import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:shell-closure-stability",
  title:
    "Shell closure stability: categorical shell closures are local terminal objects",
  lean: { ref: "qou:QOU.BraidKnot.ShellClosureStability",
    validation: "not_checked",
  },
  uses: ["def:dressed-particle"],
  tags: [
    "stability",
    "shell-closure",
    "terminal-object",
    "frobenius-stability",
    "multi-operator-binding",
  ],
});
