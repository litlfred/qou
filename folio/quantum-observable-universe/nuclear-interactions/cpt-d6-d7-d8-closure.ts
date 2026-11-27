import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:cpt-d6-d7-d8-closure",
  title:
    "CPT closure: charge conjugation, parity and time reversal jointly preserve the Markov trace",
  lean: {
    ref: "qou:QOU.ParticleInteractions.CPTClosure",
    validation: "not_checked",
  },
  uses: [
    "conj:cpt-orbit-closure-density",
    "def:bar-involution",
  ],
  cites: [
    "wigner1937",
    "jones1987",
    "kassel1995",
  ],
  tags: [
    "cpt-closure",
    "discrete-symmetry",
    "compound-conjecture",
    "duality-d6-d7-d8",
    "markov-trace",
    "open-problem",
  ],
  authorNotes: [
    { kind: "deprecated", date: "2026-11-27", body: "**Refuted in the stated form; superseded by the qCPT law.** On a braid word the composite $C\\cdot P\\cdot T$ is braid inversion $\\beta \\mapsto \\beta^{-1}$, which does not preserve the Markov trace (Lean `QOU.IwahoriHecke.MarkovTraceSymmetries.cpt_not_trace_preserving`). The replacement is the proved qCPT law: the trace at $(q, z)$ of $\\mathrm{CPT}(\\beta)$ equals the trace at $(q^{-1}, z - (q - q^{-1}))$ of $\\beta$ (Lean `QOU.IwahoriHecke.MarkovTraceSymmetries.qcpt_law`, in `lean/HeckeTemperleyLieb/MarkovTraceSymmetries.lean`). See this block's Status section. The label is kept for graph stability. Bean `qou-za1a`." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The conjecture is class-axiomatised over the closed-braid space $B$, the trace $\\mathrm{tr}$ and the CPT action $\\mathrm{cpt}$ it concerns. Downstream blocks that require CPT closure as an explicit hypothesis take `[CPTClosure R B tr cpt]` as a class hypothesis, where $R$ is the coefficient ring of the trace." },
  ],
});
