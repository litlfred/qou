import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:h3-frobenius-casimir-markov-trace",
  title:
    "Frobenius Casimir of $H_3(q)$: Schur elements, Markov weights, its Markov trace, and $\\sum_{\\lambda\\vdash3}1/\\dim_q\\lambda = 2+1/[2]_q$",
  lean: {
    ref: "qou:QOU.MassCore.H3FrobeniusCasimir.tr_casimir_D",
  },
  uses: ["thm:frobenius-codim-universal"],
  cites: ["jones1987", "geckpfeiffer2000"],
  tags: ["frobenius", "casimir", "schur-elements", "markov-trace", "convention-D", "hecke-algebra"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Two inputs are cited rather than formalised: that $C_{\\mathrm{Frob}}$ acts on block $\\lambda$ by the scalar $c_\\lambda d_\\lambda$ in item 1, which the Lean checks only through the trace identity it implies, and" },
    {
      kind: "status",
      date: "2026-11-16",
      body: "Proved algebraic core of conj:partition-sum-proton-residual (issue #8094). Sibling .lean is sorry-free over an arbitrary field (lean-direct exit 0). Scope: H_3 is modelled as K^6 with the standard basis multiplication; the Hecke relations, the trace property on basis pairs and the Markov property on H_2 are proved, while associativity of the basis product and uniqueness of the Ocneanu trace are cited.",
    },
  ],
});
