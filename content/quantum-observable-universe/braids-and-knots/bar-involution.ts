import { definition } from "../../schema/builders";

export default definition({
  label: "def:bar-involution",
  lean: {
    ref: "qou:QOU.BraidKnot.BarInvolution",
    validation: "not_checked",
  },
  title:
    "Bar-involution and its $P_{\\mathrm{avg}}$ / $P_{\\mathrm{skew}}$ projections: the canonical $q \\leftrightarrow q^{-1}$, $\\sigma \\leftrightarrow \\sigma^{-1}$ involution on the Hecke algebra, splitting every $H_n(q)$-quantity into a bar-symmetric (even/cosh/cos/$\\mathrm{Li}_2^q$-like) part the framework retains and a bar-anti-symmetric (odd/sinh/sin/$\\Phi_q$-like) part the framework projects away.",
  uses: [],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
    "jones1985",
  ],
  tags: [
    "lean-infrastructure",
    "bar-invariance",
    "categorical-action",
    "notation",
    "classification",
  ],
});
