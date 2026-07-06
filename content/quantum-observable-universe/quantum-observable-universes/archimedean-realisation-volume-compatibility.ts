import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:archimedean-realisation-volume-compatibility",
  title:
    "Compatibility of the local archimedean realisation $\\tau_\\infty$ with the global realization $\\mathcal{R}_{\\mathrm{top}}$ on QOU volume classes",
  tags: [
    "archimedean-realisation",
    "habiro-ring",
    "hyperbolic-volume",
    "volume-conjecture",
    "tau-infty",
  ],
  uses: [
    "rem:generating-functions-solve-reeb-flow",
    "def:q-dilogarithm",
    "prop:thurston-volume-additivity",
    "def:archimedean-realization-functor",
  ],
  cites: ["kashaev1997", "murakami-murakami2001"],
});
