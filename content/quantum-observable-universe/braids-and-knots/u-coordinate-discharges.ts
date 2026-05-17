import { remark } from "../../schema/builders";

export default remark({
  label: "rem:u-coordinate-discharges",
  lean: {
    ref: "qou:QOU.BraidKnot.u_coordinate_discharges",
    validation: "not_checked",
  },
  interprets: "rem:ck-extraction-from-algebraic-rules",
  title:
    "Macdonald coordinate $u = q^2$ discharges — closed-form rational identities replacing $\\mathtt{Real.sqrt}$-laden scalar invariants ($b^2 = (u^2+u+1)/(u+1)^2$, $\\dim_q^2 V_{(2,1)} = u + 2 + u^{-1}$, etc.)",
  uses: [
    "rem:ck-extraction-from-algebraic-rules",
    "rem:h3-hecke-idempotents",
    "prop:hoefsmit-V21-cos-symmetrization",
    "prop:q-beta-categorical-precision-ladder",
  ],
  cites: [
    "macdonald1995",
    "hoefsmit1974",
    "wenzl1988",
  ],
  tags: [
    "lean-infrastructure",
    "macdonald-coordinate",
    "u-substitution",
    "rational-identities",
    "explicit-residual",
  ],
});
