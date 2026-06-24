import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:shell-closure-stability",
  proofs: ["prf:shell-closure-stability"],
  title:
    "Shell closure stability: noble-gas configurations are local terminal objects",
  lean: { ref: "qou:QOU.BraidKnot.ShellClosureStability",
    validation: "not_checked",
  },
  uses: ["def:dressed-particle"],
  tags: [
    "stability",
    "noble-gas",
    "shell-closure",
    "terminal-object",
    "frobenius-stability",
    "magic-numbers",
    "multi-operator-binding",
  ],
});
