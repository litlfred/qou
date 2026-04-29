import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:kashaev-volume-conjecture",
  title: "Kashaev volume conjecture (axiomatised as Lean class)",
  lean: {
    ref: "qou:QOU.Kashaev.VolumeConjecture",
    validation: "not_checked",
  },
  uses: [
    "rem:kashaev-volume-density",
    "rem:kashaev-as-archimedean-realization",
    "def:archimedean-realization-functor",
    "def:algebraic-quantum-volume",
  ],
  cites: ["kashaev1997", "murakami-murakami2001"],
  tags: [
    "kashaev",
    "volume-conjecture",
    "archimedean",
    "phi-q",
    "axiom-class",
    "open-problem",
  ],
});
