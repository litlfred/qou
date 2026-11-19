import { definition } from "../../schema/builders";

export default definition({
  label: "def:bar-involution",
  lean: {
    ref: "qou:QOU.BraidKnot.BarInvolution",
    validation: "not_checked",
  },
  title:
    "Bar-involution and its $P_{\\mathrm{avg}}$ / $P_{\\mathrm{skew}}$ projections",
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
