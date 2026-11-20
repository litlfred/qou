import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:atom-knot-mass-derivation",
  label: "rem:atom-knot-mass-derivation-proof-sketch",
  title: "Proof sketch: the end-to-end mass derivation $B = \\rho \\cdot m_e \\cdot \\mathrm{Vol}_{\\mathrm{hyp}}(\\widehat{T_w})$",
  uses: [
    "conj:atom-knot-mass-derivation",
    "def:archimedean-realization-functor",
    "thm:jones-markov-trace",
  ],
  cites: [
    "gromov1982",
    "kashaev1997",
    "mostow1968",
    "murakami-murakami2001",
    "thurston1978",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The principled atlas\n ([prop:recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas))\n admits no such entry." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): by the canonical formalism\nand locked in [`gb-filtration-jet-order.witness.json`](../../../computations/gb-filtration-jet-order.witness.json))." },
  ],
});
