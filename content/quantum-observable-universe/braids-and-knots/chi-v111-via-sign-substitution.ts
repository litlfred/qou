import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chi-v111-via-sign-substitution",
  interprets: "rem:chi-per-irrep-cyclotomic-closed-forms",
  title:
    "V_(1,1,1) per-irrep character difference derivation via sign-rep substitution $\\sigma_i \\mapsto -q^{-1}$; closed form $-(q^2+1)^2(q^2-1)/(4q^5)$ proved via scalar arithmetic (conjugate-partition symmetry to V_(3))",
  uses: [
    "rem:chi-per-irrep-cyclotomic-closed-forms",
    "rem:chi-v3-closed-form-proof",
  ],
  cites: ["kassel1995", "hoefsmit1974", "jones1985"],
  tags: [
    "lean-infrastructure",
    "v111-antisymmetric",
    "sign-rep",
    "conjugate-partition",
    "scalar-derivation",
  ],
});
