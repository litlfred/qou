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
    engine: "python+mpmath",
    script: "computations/delta_lambda_z_coefficient_and_slope.py",
    witness: "computations/delta-lambda-z-coefficient-and-slope.witness.json",
    status: "failed",
    // status was "verified" until 2026-08-23; the cited witness's own
    // `allPassed` is false (slope_10A5_refuted_at_A_ge_5). Per ComputationStatus,
    // "failed" = script ran, witness does NOT match expected values.
    // Nothing compared the two until scripts/check-computation-status.py.,
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
