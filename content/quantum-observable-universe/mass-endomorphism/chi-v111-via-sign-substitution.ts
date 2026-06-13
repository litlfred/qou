import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chi-v111-via-sign-substitution",
  interprets: "rem:chi-per-irrep-cyclotomic-closed-forms",
  title:
    "V_(1,1,1) per-irrep character difference derivation via sign-rep substitution $\\sigma_i \\mapsto -q^{-1}$; closed form $-(q^2+1)^2(q^2-1)/(4q^5)$ proved via scalar arithmetic (conjugate-partition symmetry to V_(3))",
  uses: ["rem:chi-per-irrep-cyclotomic-closed-forms"],
  cites: ["kassel1995", "hoefsmit1974", "jones1985"],
  tags: [
    "lean-infrastructure",
    "v111-antisymmetric",
    "sign-rep",
    "conjugate-partition",
    "scalar-derivation",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**V_(1,1,1) FULLY DERIVED IN LEAN** (item 2 of  closure).\n\nThe derivation proceeds purely from the scalar sign-rep arithmetic,\nmirroring V_(3)'s template. Combined with V_(3) (`rem:chi-v3-closed-form-proof`),\nthis closes **both 1-d irreps** of $H_3(q)$ from first principles.\n\nThe remaining V_(2,1) case (item 1) is partially closed at the\nrational-identity level in\n[`rem:chi-v21-hoefsmit-matrix-derivation`](#rem:chi-v21-hoefsmit-matrix-derivation);\nfull matrix-product trace requires the 2$\\times$2 Hoefsmit machinery from\n`hoefsmit-V21-cos-symmetrization.lean` (currently chapter-isolated).",
    },
  ],
});
