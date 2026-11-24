import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mirror-baseline-cancellation",
  title: "Mirror-pair cancellation of the bar-even binding baseline",
  uses: [
    "prop:delta-lambda-dt-index-unification",
    "prop:bar-involution-invariance",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.mirror_baseline_cancels",
  },
  computation: {
    engine: "python+mpmath",
    script: "computations/delta_lambda_z_coefficient_and_slope.py",
    witness: "computations/delta-lambda-z-coefficient-and-slope.witness.json",
    status: "failed",
    // Preserved verbatim from mba-sidecar-mirror-cancellation.ts:
    // STAYS "failed" — the producer records a genuine negative (the global
    // 10A-5 law is refuted at A>=5 while the tight-light-fit conjunct fails
    // against the 0.5 bar).
  },
  tags: [
    "delta-lambda",
    "mirror-pair",
    "bar-parity",
    "z-correction",
    "writhe",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Relocated intact from `appendix-mass-binding-algorithms/mba-sidecar-mirror-cancellation` to Chapter 12 (`nuclear-interactions`) under `qou-mba8`, preserving label `prop:mirror-baseline-cancellation`.",
    },
  ],
});
