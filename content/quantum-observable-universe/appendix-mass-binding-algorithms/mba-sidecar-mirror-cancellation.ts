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
    // STAYS "failed" — the producer records a genuine negative and one of its
    // three assertions is red on purpose. It was "verified" until 2026-08-23
    // while `allPassed` was false; nothing had compared the two until
    // scripts/check-computation-status.py.
    //
    // The red line was `slope_10A5_refuted_at_A_ge_5`, whose name is the
    // FINDING (the global 10A−5 law is refuted at A≥5) — so it read as though
    // the refutation itself had failed. It had not. The assertion was a
    // conjunction: "the law holds for A≤4 AND is refuted at A≥5". The second
    // half is solidly true (|dev| = 22.7, 30.8, 32.6). The first half is false
    // against the producer's own output: |dev| for D, T, ⁴He measures 0.63,
    // 1.02, 1.70, none under the 0.5 bar the claim asserted.
    //
    // That 0.5 came from a docstring table which was STALE IN EVERY ROW —
    // it recorded −0.01/−0.07/+0.27. The witness payload itself had not
    // drifted (a re-run reproduces it byte for byte); the docstring simply
    // predated a change in the upstream Δ_λ residual and was never refreshed,
    // and the assertion's `source` string inherited its numbers.
    //
    // Now split into two assertions so each fact stands on its own line: the
    // refutation PASSES, the tight-light-fit claim FAILS. Removing a false
    // conjunct is not relaxing a gate — the witness is still red, for the
    // right reason, and `light_bar_needed` reports the smallest threshold the
    // data would actually satisfy so the 0.5 bar can be judged rather than
    // assumed.
    //
    // Another producer defect fixed: `all(... if a in by)` returned True
    // VACUOUSLY when no heavy rows were present — a refutation claimed on no
    // data at all.
    //
    // And a fix I got WRONG first, recorded because the wrong version looked
    // better. The producer emits 21 raw float64 fields; I "drained" them to 0
    // by lifting each through `mp.mpf(repr(x))` and serialising with `fmt`.
    // The float64-padding ratchet caught it: 26 NEW fake-precision values.
    // Those numbers are float64 AT SOURCE — read out of the residual witness
    // as JSON — so writing them to 50 digits invents 34 that were never
    // computed. A raw-float64 count is not a score to minimise; it was telling
    // the truth, and laundering it through mpmath makes the witness worse
    // while making the gate greener. Reverted. The count is now 21 -> 20,
    // drained by exactly the one genuine downcast (`float(q_at(30))`, where
    // q_at IS mpf at source). The rest belongs upstream.,
    //
    // ONE OBSERVATION WORTH KEEPING, offered as an observation and not a
    // result. Across that upstream drift, every absolute deviation moved — but
    // the A=7 mirror DIFFERENCE did not: ⁷Li and ⁷Be both shifted by exactly
    // −4.58, leaving ⁷Be−⁷Li = −1.77 in both tables. That is precisely the
    // baseline cancellation THIS BLOCK'S OWN PROPOSITION predicts, showing up
    // as invariance under an unrelated perturbation. The A=3 pair did not
    // behave that way (T shifted −0.95, ³He −0.58, so the penalty moved
    // −1.33 → −0.95). Why A=3 fails to cancel is not investigated here, and
    // the underlying Δ_λ drift is not traced — both are noted in qou-zf9n.,
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
