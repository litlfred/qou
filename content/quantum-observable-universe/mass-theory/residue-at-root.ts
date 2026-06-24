import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:residue-at-root",
  proofs: ["prf:residue-at-root"],
  title:
    "Cyclotomic residues of $\\Phi_q \\cdot \\mathrm{tr}_{M, \\ell}$ — algebraic definition",
  lean: {
    ref: "qou:QOU.BraidKnot.ResidueAtRoot",
    validation: "not_checked",
  },
  cites: [
    "kassel1995",
    "geckpfeiffer2000",
    "habiro2002",
  ],
  tags: [
    "residue",
    "cyclotomic",
    "habiro-completion",
    "spectral-sequence",
    "gs-filtration",
    "narrative-replacement",
  ],
});
