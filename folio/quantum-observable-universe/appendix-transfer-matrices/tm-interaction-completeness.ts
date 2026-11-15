import { prose } from "../../schema/builders";

export default prose({
  label: "tm-interaction-completeness",
  title: "Interaction completeness: the seven $\\Sigma_4$ transfer matrices",
  uses: [
    "tm-interactions",
    "tm-knot-pairs",
  ],
  tags: [
    "transfer-matrix",
    "completeness",
    "interaction",
    "summary",
    "appendix",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "The single-crossing local enumeration above is rigorous from the\nmatrix algebra of [tm-interactions](#tm-interactions).  The global\n**closure-under-composition** claim (every multi-crossing\n$\\Sigma_4$-admissible interaction is a finite product of these\nseven) is the content of *interaction completeness*; the explicit\nproof tracks the embeddability bound on $\\Sigma_4$ from\n[Chapter](#chap:brings-surface) §[force-knot-identification](#rem:force-knot-identification)\nand is left to the formalisation pass.  The seven operators are\nthe alphabet; closure is the grammar.",
    },
  ],
});
