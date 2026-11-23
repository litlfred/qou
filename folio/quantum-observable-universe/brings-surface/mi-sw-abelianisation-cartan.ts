import { lemma } from "../../schema/builders";

export default lemma({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "The Lean derives the conclusion by composing two local identities carried as hypotheses (`cartan_local_form`, `sw_eq_local_form`), so $A^0 = \\lambda_{\\mathrm{SW}}$ is assumed piecewise rather than derived (round-trip audit pass 2, C18). $H, E_\\pm$ span $\\mathfrak{sl}_2(\\mathbb{C})$, not $\\mathfrak{su}(2)$; the narrative is corrected. The Cartan component of a connection form is gauge-dependent, so its equality with $\\lambda_{\\mathrm{SW}}$ holds only in a chosen gauge." },
  ],
  label: "lem:mi-sw-abelianisation-cartan",
  title: "Cartan reduction recovers the SW differential",
  lean: {
    ref: "qou:QOU.ArchimedeanUniverse.mi_sw_cartan_reduction",
    validation: "not_checked",
  },
  uses: [
    "rem:brings-smoothness",
    "rem:weight-space-decomposition",
    "rem:color-bundles",
  ],
  proofs: ["prf:mi-sw-abelianisation-cartan"],
  tags: [
    "seiberg-witten",
    "abelianisation",
    "cartan-reduction",
    "exceptional-divisor",
    "spectral-curve",
  ],
});
