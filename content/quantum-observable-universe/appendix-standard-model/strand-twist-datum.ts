import { definition } from "../../schema/builders";

export default definition({
  label: "def:strand-twist-datum",
  title: "Per-strand framing (twist) datum",
  lean: {
    ref: "qou:QOU.StandardModel.TwistDatum",
    validation: "not_checked",
  },
  uses: ["def:gauge-action-groupoid", "def:coulomb-charge"],
  defines: ["strand-twist-datum"],
  tags: ["appendix", "standard-model", "framing", "ribbon", "hypercharge"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-01",
      body:
        "**Step (a) of the hypercharge programme (beans qou-4tul, " +
        "qou-q377).** The datum + gauge invariance + bar negation + " +
        "writhe-independence are proved sorry-free in the Lean sibling. " +
        "Whether the normalised candidate Y = 2(Q_twist - I3) passes the " +
        "GMN and Z6-spectrum batteries is the open content of " +
        "conj:sm-hypercharge-invariant; the enumeration probe is " +
        "computations/strand_twist_y_battery.py (exploratory, not wired).",
    },
  ],
});
