import { proposition } from "../../schema/builders";

/**
 * Palindromicity of the NF histogram characterises orbital type.
 */
export default proposition({
  label: "prop:palindromicity-orbital-type",
  title: "Palindromicity and orbital type",
  lean: { ref: "qou:QOU.Molecular.PalindromicityOrbitalType",
    validation: "not_checked",
  },
  uses: ["prop:shell-closure-nf-term-count"],
  cites: ["iwahori1964", "jones1987"],
  tags: [
    "normal-form",
    "palindromicity",
    "orbital-type",
    "poincare-duality",
  ],
});
