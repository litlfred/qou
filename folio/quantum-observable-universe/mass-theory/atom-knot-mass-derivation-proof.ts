import { proof } from "../../schema/builders";

export default proof({
  label: "prf:atom-knot-mass-derivation",
  title:
    "Proof of the end-to-end mass derivation $B = \\rho \\cdot m_e \\cdot \\mathrm{Vol}_{\\mathrm{hyp}}(\\widehat{T_w})$",
  uses: [
    "prop:atom-knot-mass-derivation",
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): by the canonical formalism\nand locked in [`gb-filtration-jet-order.witness.json`](../../../computations/gb-filtration-jet-order.witness.json))." },
  ],
});
