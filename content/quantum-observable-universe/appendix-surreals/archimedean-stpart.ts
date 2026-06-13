import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:archimedean-stpart",
  title:
    "Archimedean QOU is the standard-part of surreal QOU",
  lean: { ref: "qou:QOU.AppendixSurreals.ArchimedeanStpart", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "archimedean",
    "categorical",
    "standard-part",
    "QOU-axioms",
    "open-problem",
  ],
  uses: ["conj:classical-limit-stpart"],
  cites: ["robinson1966", "ehrlich2012"],
  authorNotes: [
    {
      kind: "status",
      body: "**Open.** Even formulating the precise statement requires:\n\n- defining the category $\\mathbf{QOU}_{\\mathbf{No}}^{\\varepsilon}$\n with the relaxed axioms (the appendix's conjectures\n [infinitesimal-frobenius](#conj:infinitesimal-frobenius),\n [infinitesimal-observability](#conj:infinitesimal-observability),\n [vacuum-epsilon](#conj:vacuum-epsilon) make a start);\n- showing that $\\mathrm{St}$ extends from\n $\\mathbf{No}_{\\mathrm{fin}}$ to morphisms in this category in a\n functorial way.\n\nBoth steps require the surreal-categorical machinery that does\nnot yet exist in mathlib.",
    },
  ],
});
