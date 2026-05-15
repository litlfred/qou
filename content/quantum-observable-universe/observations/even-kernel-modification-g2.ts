import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:even-kernel-modification-g2",
  title:
    "Squared kernel $G_2(x, y) = \\mathrm{tr}_M((x \\cdot y)^2)$ as the even modification of $G$ — algebraic identity $\\mathcal{L}_{\\mathrm{CFS}} = n \\cdot G_2 - \\lVert x \\cdot y\\rVert_1^2$",
  uses: [
    "prop:qou-continuum-kernel-is-frobenius-gram",
    "prop:mu-arch-integral-match-symmetry-obstruction",
  ],
  cites: [
    "finster2021",
    "finster2024",
  ],
  tags: [
    "mu-arch",
    "even-kernel",
    "trace-modification",
    "hilbert-schmidt",
    "kernel-decomposition",
    "structural-identity",
  ],
  proofs: ["prf:even-kernel-modification-g2"],
});
