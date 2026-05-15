import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mu-arch-integral-match-symmetry-obstruction",
  title:
    "Integral-match version of $\\mu_{\\mathrm{arch}}$ fails under any centered free-probability limit, by trace-symmetry obstruction",
  uses: [
    "prop:qou-continuum-kernel-is-frobenius-gram",
    "prop:mu-arch-strict-match-fails-at-n2",
  ],
  cites: [
    "finster2021",
    "finster2024",
    "biane1998",
  ],
  tags: [
    "mu-arch",
    "integral-match",
    "free-probability",
    "symmetry-argument",
    "fourier-transform",
    "established-obstruction",
  ],
  proofs: ["prf:mu-arch-integral-match-symmetry-obstruction"],
});
