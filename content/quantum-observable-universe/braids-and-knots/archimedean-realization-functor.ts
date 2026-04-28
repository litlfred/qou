import { definition } from "../../schema/builders";

export default definition({
  label: "def:archimedean-realization-functor",
  title: "Archimedean realization functor $\\mathcal{R}_{\\mathrm{top}}$",
  tags: ["realization-functor", "archimedean", "motivic", "observable", "macroscopic-limit"],
  uses: [
    "def:adelic-substrate",
    "def:motivic-mass-measure",
    "def:algebraic-quantum-volume",
    "def:spatial-realization-functor",
  ],
  cites: ["tate1967", "kashaev1997", "murakami-murakami2001"],
  lean: {
    ref: "qou:QOU.BraidsKnots.ArchimedeanRealizationFunctor",
    validation: "not_checked",
  },
});
