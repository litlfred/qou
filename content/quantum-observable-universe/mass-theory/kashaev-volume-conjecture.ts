import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:kashaev-volume-conjecture",
  title: "Kashaev volume conjecture (axiomatised as Lean class)",
  lean: {
    ref: "qou:QOU.Kashaev.VolumeConjecture",
    validation: "not_checked",
  },
  uses: [
    "rem:kashaev-as-archimedean-realization",
    "def:quantum-bloch-group",
  ],
  cites: ["kashaev1997", "murakami-murakami2001", "zagier1986", "neumann-zagier1985"],
  tags: [
    "tier:famous",
    "kashaev",
    "volume-conjecture",
    "archimedean",
    "phi-q",
    "axiom-class",
    "open-problem",
  ],
});
