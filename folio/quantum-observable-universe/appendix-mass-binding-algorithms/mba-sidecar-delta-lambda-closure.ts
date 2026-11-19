import { algorithm } from "../../schema/builders";

export default algorithm({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "Working-channel pointers pulled out of the published prose: the " +
        "cross-PR maintenance contract for this appendix is " +
        "`docs/coordination/2026-06-02-mba-appendix-maintenance-contract.md`, " +
        "and the candidate super-pairwise extensive-magnitude terms are " +
        "collected in `docs/coordination/option-e.md`.",
    },
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalization pointers moved out of published prose: the per-partition value and chirality sign are formalized in `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional` and `deltaSign_eq_nStat_parity`; the $A = 4$ pairwise determinant inequality $(1-m^2)^6 \\le (1+3m)(1-m)^3$ is formalized in `QOU.MassTheory.exchangeDet_pow_two_le_four` (`lean/QOU/MassTheory/BindingSaturationCapA4.lean`).",
    },
  ],
  label: "alg:delta-lambda-closure",
  title: "$\\Delta_\\lambda$ per-partition value (PROVED $(-1)^{n(\\lambda)}\\dim V_\\lambda$); many-body magnitude open",
  cites: ["shoji2019", "springer1976"],
  uses: [
    // The per-partition VALUE this algorithm computes is proved:
    // Δ_λ = (−1)^{n(λ)}·dim V_λ, identified as a DT/3d-index Euler characteristic
    // with geometric chirality (Lean dtEuler_eq_deltaLambda_unconditional,
    // sorry-free). That proposition had no content block until 2026-08-07, which
    // is why this algorithm previously cited only a remark and failed the
    // "algorithms are downstream of math" constraint.
    "prop:delta-lambda-dt-index-unification",
    "rem:term6-binding-density",
    // The magnitude leg of Δ_λ = (−1)^{n(λ)}·dim V_λ is the Wedderburn block
    // dimension d_λ = f^λ, which `prop:wedderburn-trace-identity` establishes
    // (Σ_λ d_λ·y_λ(q) = 1 partitions the Markov weight among those blocks).
    // Cited alongside `prop:delta-lambda-dt-index-unification` (`dtEuler_eq_deltaLambda_unconditional`,
    // bean qou-7ylg) because the magnitude leg rests on the Wedderburn block decomposition.
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
