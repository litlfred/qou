import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:shared-denominator-cusp-holonomy",
  title:
    "Shared-denominator cusp holonomy: roots of $(x; q)_n$ enforce Thurston completeness",
  lean: {
    ref: "qou:QOU.QPochhammer.shared_denominator_cusp_holonomy",
    validation: "not_checked",
  },
  uses: [
    "def:q-pochhammer-partial-product",
    "conj:algebraic-geometric-dilog-equivalence",
    "conj:dilogarithm-archimedean-limit",
    "conj:kashaev-volume-conjecture",
    "rem:kashaev-as-archimedean-realization",
  ],
  cites: [
    "thurston1978",
    "neumann-zagier1985",
    "kashaev1997",
    "murakami-murakami2001",
  ],
  tags: [
    "q-pochhammer",
    "thurston",
    "cusp",
    "holonomy",
    "gluing-equations",
    "newton-raphson",
    "open-problem",
  ],
});
