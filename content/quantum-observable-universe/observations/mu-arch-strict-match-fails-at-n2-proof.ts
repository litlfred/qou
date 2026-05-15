import { proof } from "../../schema/builders";

export default proof({
  label: "prf:mu-arch-strict-match-fails-at-n2",
  title:
    "Proof: strict $\\mu_{\\mathrm{arch}}$ kernel-match fails at $n=2$ via explicit $G(1,1) \\neq \\mathcal{L}_{\\mathrm{CFS}}(1,1)$ computation",
  uses: [
    "prop:mu-arch-strict-match-fails-at-n2",
    "prop:qou-continuum-kernel-is-frobenius-gram",
  ],
});
