import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mu-arch-strict-match-fails-at-n2",
  title:
    "Strict $\\mu_{\\mathrm{arch}}$ kernel-match fails at $n=2$: $G(1,1) = 1$ but $\\mathcal{L}_{\\mathrm{CFS}}(1,1) = 0$",
  uses: [
    "prop:qou-continuum-kernel-is-frobenius-gram",
    "thm:jones-markov-trace",
  ],
  cites: [
    "finster2021",
    "finster2024",
  ],
  tags: [
    "mu-arch",
    "lagrangian-mismatch",
    "kernel-comparison",
    "small-n-resolution",
    "established-disagreement",
  ],
  proofs: ["prf:mu-arch-strict-match-fails-at-n2"],
});
