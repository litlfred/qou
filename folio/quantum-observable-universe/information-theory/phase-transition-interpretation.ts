import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:phase-transition-boundary",
  label: "rem:phase-transition-interpretation",
  title: "Three phases from Hecke channels and the triple point",
  tags: [
    "phase-transition",
    "hecke-algebra",
    "gas",
    "liquid",
    "solid",
    "sublimation",
    "triple-point",
  ],
  uses: [
    "prop:phase-transition-boundary",
    "conj:composite-crossing-parity",
    "rem:composite-crossing-sublimation-criteria",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-24",
      body:
        "**Sublimation mechanism withdrawn.** The paragraph read \"When the crossing number $n_K$ is odd, the Hecke extension at the mixed-channel temperature forms non-split. The Hopf invariant uniquely classifies this extension.\" That extension does not exist — see the status note on [`prop:phase-transition-boundary`](#prop:phase-transition-boundary) for the evidence. The three-phase reading itself is untouched: the channels are still the $q$ and $-q^{-1}$ eigenvalues and the mixed sector between them, and nothing in the triple-point or classical-comparison paragraphs used the extension. What is gone is the claim that an $\\mathrm{Ext}^1$ class explains why the liquid phase is skipped. Bean `qou-zut2`.",
    },
  ],
});
