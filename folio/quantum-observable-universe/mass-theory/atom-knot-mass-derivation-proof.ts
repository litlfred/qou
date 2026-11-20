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
});
