import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:colour-ratio-mobius-matrix",
  lean: { ref: "qou:QOU.BringsSurface.mobiusMatrix_eq_cayley_mul_diag",
    validation: "not_checked",
  },
  title: "The colour-ratio Möbius matrix",
  tags: ["brings-surface", "color-tube", "mobius-transformation", "branch-point"],
  uses: [],
});
