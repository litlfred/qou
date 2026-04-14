import { conjecture } from "../../schema/builders";

/**
 * Shell closure is detectable from NF term count in the quotient atom model.
 */
export default conjecture({
  label: "conj:shell-closure-nf-term-count",
  title: "Shell closure from NF term count",
  lean: {
    decl: "QOU.Molecular.ShellClosureNFTermCount",
    validation: "not_checked",
  },
  uses: [
    "def:electron-shell-braid-capacity",
    "conj:electron-shells-hopf",
  ],
  cites: ["iwahori1964", "jones1987"],
  tags: [
    "electron-shell",
    "normal-form",
    "quotient-ideal",
    "hecke-algebra",
    "shell-closure",
  ],
});
