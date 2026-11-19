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
    {
      kind: "note",
      body: "Computational witness: computations/gb-filtration-jet-order.witness.json.",
    },
  ],
});
