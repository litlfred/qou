import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:residue-at-root",
  title:
    "Cyclotomic residues of $\\Phi_q \\cdot \\mathrm{tr}_{M, \\ell}$ — algebraic definition",
  lean: {
    ref: "qou:QOU.BraidKnot.residue_at_root",
  },
  uses: [
    // conj:gs-residue-at-root-existence removed (qou-tm3c): the cyclotomic projection is now constructed (QOU/BraidKnot/QHabiroCompletion.lean); membership of Phi_q*tr in the Habiro ring is a stated hypothesis, not a conjectural input.
  ],
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
    { kind: "status", date: "2026-11-21", body: "The cyclotomic projection on the Habiro completion is constructed in `QOU/BraidKnot/QHabiroCompletion.lean` (sorry-free), so this block no longer depends on `conj:gs-residue-at-root-existence`. Membership of $\\Phi_q \\cdot \\mathrm{tr}_{M,\\ell}(T_w)$ in the Habiro ring is now an explicit hypothesis of the statement; it remains the open content of that conjecture (bean qou-rh4b)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): axiomatised as the Lean class `ResidueAtRoot` (fields: the target ring family and the projection ring homomorphism). Conditional on an instance of that class, ..." },
  ],
});
