import { remark } from "../../schema/builders";

export default remark({
  label: "rem:archimedean-realization-functor-interpretation",
  title:
    "Archimedean realization: functor vs. motivic measure and identification with $\\tau$",
  interprets: "def:archimedean-realization-functor",
  tags: ["realization-functor", "archimedean", "motivic", "fibre-functor"],
  uses: [
    "def:archimedean-realization-functor",
    "def:algebraic-quantum-volume",
  ],
  cites: ["kashaev1997", "murakami-murakami2001"],
});
