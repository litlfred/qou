import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:delta-lambda-closure",
  title: "$\\Delta_\\lambda$ per-partition value (PROVED $(-1)^{n(\\lambda)}\\dim V_\\lambda$); many-body magnitude open",
  uses: [
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
