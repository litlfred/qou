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
    { kind: "note", date: "2026-11-20", body: "**$E_2$-collapse claims removed (owner, 2026-11-20, bean `qou-6qbv`).** The sketch said the braid and Hecke relations are the only $E_2$-differentials of the GB spectral sequence and that it collapses at $E_2$ for semisimple $H_n(q)$. Both are false: the rewriting map is not a differential (`QOU.BraidKnot.GBRewriteDifferential`), and the length-filtered Hochschild sequence of $H_3$ has $d_2, d_4 \\neq 0$ (`computations/probes/gb_spectral_sequence_h3_probe.py`). The finiteness the sketch draws from it already follows from the Wedderburn decomposition two paragraphs on, which it now cites." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The principled atlas\n ([prop:recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas))\n admits no such entry." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): by the canonical formalism\nand locked in [`gb-filtration-jet-order.witness.json`](../../../computations/gb-filtration-jet-order.witness.json))." },
  ],
});
