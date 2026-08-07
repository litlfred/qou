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
