import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mirror-baseline-cancellation",
  title: "Mirror-pair cancellation of the bar-even binding baseline",
  uses: [
    "alg:delta-lambda-closure",
    "alg:per-isotope-binding",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.mirror_baseline_cancels",
  },
  tags: [
    "mba",
    "sidecar",
    "mirror-pair",
    "bar-parity",
    "writhe",
  ],
});
