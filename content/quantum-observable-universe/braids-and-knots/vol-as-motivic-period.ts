import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:archimedean-realization-functor",
  label: "rem:vol-as-motivic-period",
  title:
    "$\\mathrm{Vol}(K)$ as a motivic period: the Bloch--Wigner regulator reading of $\\tau_{\\mathrm{arch}}$",
  uses: [
    "def:archimedean-realization-functor",
    "def:algebraic-quantum-volume",
    "rem:quantum-bloch-group",
  ],
  cites: [
    "zagier1986",
    "neumann-zagier1985",
    "kontsevich1995",
  ],
  tags: [
    "motivic-period",
    "bloch-wigner",
    "regulator",
    "mixed-tate",
    "archimedean",
    "interpretive",
  ],
});
