import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:delta-lambda-closure",
  title: "$\\Delta_\\lambda$ per-partition value (PROVED $(-1)^{n(\\lambda)}\\dim V_\\lambda$); many-body magnitude open",
  uses: [
    // The two provable legs this algorithm sits downstream of: the extensive
    // jet-filtration statement, and the many-body magnitude conjecture whose
    // OPEN status is exactly what the title records. Without a provable here
    // the block fails `algorithms are downstream of math` and — because the
    // failed import never registers the label — takes
    // `alg:mirror-cancellation` down with it as an unresolved `uses`.
    "prop:jet-filtration-binding-extensive",
    "conj:binding-manybody-eq-jet-filtration",
    "rem:term6-binding-density",
    // The magnitude leg of Δ_λ = (−1)^{n(λ)}·dim V_λ is the Wedderburn block
    // dimension d_λ = f^λ, which `prop:wedderburn-trace-identity` establishes
    // (Σ_λ d_λ·y_λ(q) = 1 partitions the Markov weight among those blocks).
    // Cited because an algorithm block must rest on a provable, and this is the
    // math the magnitude actually comes from.
    //
    // NOTE: the ideal citation would be a content block for the proved value
    // theorem itself — Δ_λ = (−1)^{n(λ)}·dim V_λ, sorry-free general-n,
    // `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional` in
    // `lean/QOU/BraidsAndKnots/DeltaLambdaGeneralNUnconditional.lean` (PR #4580).
    // That theorem currently has NO content-block face: it is referenced only
    // from this algorithm's `.md` and from step 9b's. Giving it one is the
    // proper follow-up (bean qou-7ylg).
    "prop:wedderburn-trace-identity",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/delta_lambda_value_witness.py",
    witness: "computations/delta-lambda-witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "sidecar",
    "delta-lambda",
    "value-proved",
    "magnitude-open",
  ],
});
