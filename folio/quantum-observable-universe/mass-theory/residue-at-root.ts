import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:residue-at-root",
  title:
    "Cyclotomic residues of $\\Phi_q \\cdot \\mathrm{tr}_{M, \\ell}$ — algebraic definition",
  lean: {
    ref: "qou:QOU.BraidKnot.residue_isRingHom_of_residueAtRoot",
    validation: "not_checked",
  },
  uses: ["conj:gs-residue-at-root-existence"],
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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): axiomatised as the Lean class `ResidueAtRoot` (fields: the target ring family and the projection ring homomorphism). Conditional on an instance of that class, ..." },
  ],
});
