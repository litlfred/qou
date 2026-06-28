import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:exceptional-divisor",
  label: "rem:breit-wheeler-vertex-hecke-parity",
  title:
    "Hecke asymmetry $q \\neq q^{-1}$ as topological parity violation: the two roots $+q, -q^{-1}$ are the left/right helicity eigenvalues",
  tags: [
    "breit-wheeler",
    "hecke",
    "parity-violation",
    "helicity",
  ],
  uses: ["rem:breit-wheeler-vertex"],
  cites: ["kauffman1991"],
});
