import { conjecture } from "../../schema/builders";

/**
 * Palindromicity of the NF histogram characterises orbital type.
 */
export default conjecture({
  label: "conj:palindromicity-orbital-type",
  title: "Palindromicity and orbital type",
  lean: { ref: "qou:QOU.Molecular.PalindromicityOrbitalType",
    validation: "not_checked",
  },
  uses: ["conj:shell-closure-nf-term-count"],
  cites: ["iwahori1964", "jones1987"],
  tags: [
    "electron-shell",
    "normal-form",
    "palindromicity",
    "orbital-type",
    "poincare-duality",
  ],
});
