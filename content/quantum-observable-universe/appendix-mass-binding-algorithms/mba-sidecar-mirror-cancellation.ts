import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mirror-baseline-cancellation",
  title: "Mirror-pair cancellation of the bar-even binding baseline",
  uses: [
    "alg:delta-lambda-closure",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.mirror_baseline_cancels",
  },
  computation: {
    engine: "python+canonical-binding",
    script: "computations/delta_lambda_z_coefficient_and_slope.py",
    witness: "computations/delta-lambda-z-coefficient-and-slope.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "sidecar",
    "delta-lambda",
    "mirror-pair",
    "bar-parity",
    "z-correction",
    "writhe",
  ],
});
