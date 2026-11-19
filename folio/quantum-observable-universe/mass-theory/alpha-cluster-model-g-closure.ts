import { remark } from "../../schema/builders";

/**
 * Model G — the phenomenological α-cluster binding closure, recorded as an
 * INTERPRETATION of the proved activation gate `prop:alpha-cluster-activation-gate`.
 *
 * ANTI-LAUNDERING STRICT (owner directive 2026-07-18): this is NOT a
 * parameter-free derivation and must never be presented as one. The cluster
 * bindings enter at their measured AME values (an input/fit); b = 0.78 MeV is
 * calibrated empirically; g = 2.4155 MeV is a guarded near-match (≈ 3b, −2.9%);
 * the C(k,2) saturation count is data-selected. Model G derives the *composite
 * structure* (which α·α pairs activate, via the proved gate), not the absolute
 * cluster base. A `remark` (not a proposition/conjecture) is the correct vehicle:
 * it makes no logical claim, it records a structural/phenomenological model.
 *
 * Witnesses (audit-only; nothing wired to production dashboards):
 *  - computations/deltalambda/alpha-activation-brunnian.witness.json      (9/9)
 *  - computations/deltalambda/alpha-cluster-volume-additivity.witness.json (7/7)
 *  - computations/deltalambda/inter-cluster-bond-term.witness.json        (10/10)
 */
export default remark({
  label: "rem:alpha-cluster-model-g-closure",
  title:
    "Model G: a phenomenological $\\alpha$-cluster binding closure (structural model — not a parameter-free derivation)",
  interprets: "prop:alpha-cluster-activation-gate",
  uses: [
    "prop:alpha-cluster-activation-gate",
    "prop:linear-chain-bond-count",
  ],
  tags: [
    "binding",
    "alpha-cluster",
    "phenomenological",
    "empirical-fit",
    "model-g",
    "anti-laundering",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witnesses: computations/deltalambda/alpha-activation-brunnian.witness.json, alpha-cluster-volume-additivity.witness.json, inter-cluster-bond-term.witness.json.",
    },
    {
      kind: "note",
      date: "2026-07-18",
      body:
        "Consolidated audit record: [docs/audits/2026-07-14-model-g-consolidated-record.md](../../../docs/audits/2026-07-14-model-g-consolidated-record.md) (rounds 4–7: #3780/#3784/#3786/#3789). Promoted to a content block per owner direction with STRICT phenomenological labelling — the fit is recorded, not laundered as a derivation. The ab-initio piece for the cluster bases is the separate bond-count tower (³H ≈ −0.16%; ⁴He open, the Vol₄ census gap).",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/deltalambda/alpha-activation-brunnian.witness.json",
      "computations/deltalambda/alpha-cluster-volume-additivity.witness.json",
      "computations/deltalambda/inter-cluster-bond-term.witness.json",
    ],
    status: "verified",
  },
});
