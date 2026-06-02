import { remark } from "../../schema/builders";

/**
 * Wraps the live per-observable-100x precision dashboard
 * (folio-assistant/computations/per-observable-100x-status.witness.json,
 * emitted by per_observable_100x_status.py).
 *
 * Purpose: declare the dashboard witness as a first-class artifact so
 * `run_pipeline.py` auto-regenerates it on upstream changes (closing the
 * paper↔compute wiring gap documented in
 * docs/audits/2026-05-19-deprecated-but-valid-scripts-catalog.md).
 *
 * Authoring history: created 2026-06-02 in claude/dashboard-lean-ci-batch-2026-06-02
 * as part of the "small/mechanical" Stage A items (dashboard wiring +
 * proton-mass-substrate-identity Lean sibling + CI escape).
 */
export default remark({
  label: "rem:per-observable-100x-status-dashboard",
  title:
    "Per-observable 100× experimental status dashboard (L2 precision-goal)",
  interprets: "prop:proton-mass-substrate-identity",
  computation: {
    engine: "python",
    script: "folio-assistant/computations/per_observable_100x_status.py",
    witness:
      "folio-assistant/computations/per-observable-100x-status.witness.json",
    status: "verified",
    requires: ["mpmath"],
  },
  tags: [
    "dashboard",
    "precision-goals",
    "L2-100x-experimental",
    "auditable",
    "paper-compute-wiring",
  ],
});
