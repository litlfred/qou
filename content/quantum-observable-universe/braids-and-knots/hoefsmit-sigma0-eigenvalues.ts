import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hoefsmit-sigma0-eigenvalues",
  title:
    "Hoefsmit $\\rho_{(2,1)}(\\sigma_0) = \\mathrm{diag}(q, -q^{-1})$ eigenvalue identification (closed Lean proof): eigenvalues, trace, determinant, Hecke quadratic — all closed by direct matrix algebra",
  interprets: "prop:hoefsmit-V21-cos-symmetrization",
  uses: [
    "prop:hoefsmit-V21-cos-symmetrization",
  ],
  cites: ["hoefsmit1974"],
  tags: [
    "lean-infrastructure",
    "hoefsmit-seminormal",
    "eigenvalues",
    "hecke-quadratic",
    "class-discharge",
    "V_(2,1)",
  ],
});
