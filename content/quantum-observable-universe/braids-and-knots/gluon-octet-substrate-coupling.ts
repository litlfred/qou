import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gluon-octet-substrate-coupling",
  title: "$8q = \\dim \\mathfrak{su}(3) \\cdot q$ — gluon-octet × substrate coupling at second order",
  lean: {
    ref: "qou:QOU.WedderburnMass.gluon_octet_substrate_coupling",
    validation: "not_checked",
  },
  uses: [
    "prop:alpha-em-categorical-trace",
    "prop:curvature-rank-delta-cs",
    "prop:borromean-baryon-interpretation",
    "prop:vol-through-tau",
    "rem:confinement-curvature-rank",
  ],
});
