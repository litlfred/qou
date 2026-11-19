import { remark } from "../../schema/builders";

export default remark({
  label: "rem:adelic-substrate-integration",
  title: "Motivation for the adelic substrate and Tate integration",
  interprets: "def:adelic-substrate",
  tags: ["adeles", "macroscopic-limit", "tate-integral", "global"],
  uses: [
    "def:adelic-substrate",
    "def:archimedean-realization-functor",
    "def:algebraic-quantum-volume",
    "def:classical-limit-functor",
  ],
  cites: ["tate1967"],
});
