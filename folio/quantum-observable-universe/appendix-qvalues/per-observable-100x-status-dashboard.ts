import { remark } from "../../schema/builders";

/**
 * Wraps the live per-observable-100x precision dashboard
 * (computations/per-observable-100x-status.witness.json,
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
    "Per-observable 100× experimental accuracy status",
  // Tagged as a glossary-style status block: it does not interpret a
  // specific provable claim; it surfaces the live L2 dashboard so the
  // witness is auto-regenerated. Avoids the `interprets:` field (per
  // Copilot review on PR #1690 — `interprets` is reserved for remarks
  // that comment on a specific provable block).
  tags: [
    "glossary",
    "dashboard",
    "precision-goals",
    "L2-100x-experimental",
    "auditable",
    "paper-compute-wiring",
  ],
  computation: {
    engine: "python",
    script: "computations/per_observable_100x_status.py",
    witness:
      "computations/per-observable-100x-status.witness.json",
    status: "verified",
    requires: ["mpmath"],
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): *The per-observable accuracy record is the witness `computations/per-observable-100x-status.witness.json`, emitted by `per_observable_100x_status.py`. It records, for each predicted observable, whether the prediction meets its $100\\times$ absolute-accuracy target against experiment. Its `summary` field carries the headline counts. **The accuracy result is `beats_100x_scoreable` out of `scoreable_total`**, which count predictions only. `beats_100x_count` must *not* be quoted as an accuracy result: it also counts the calibration inputs the witness lists in `summary.calibration_inputs`, whose residuals are fixed by construction rather than measured. The remainder do not meet the target, and closing them is open.* || the authoritative values are the witness's per-row\n`pred_err`, `100x_target` and `beats_100x` flags, together with the `summary`\ncounts `beats_100x_scoreable` / `scoreable_total`. The witness is recomputed" },
    {
      kind: "note",
      date: "2026-06-02",
      body: "When this block was authored, the framework met the L2 100× target on 3 of 7 observables (the two anchored masses + the meson ratio m_K/m_π).",
    },
  ],
});
