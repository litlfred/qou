import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:gauge-conformal-invariance",
  title: "Gauge conformal invariance",
  lean: {
    ref: "qou:QOU.Archimedean.gauge_conformal_invariance",
    validation: "not_checked",
  },
  tags: [
    "conformal-shift",
    "emission-gaps",
    "jwst",
  ],
  uses: ["prop:spectrahedral-phase-collapse"],
});
