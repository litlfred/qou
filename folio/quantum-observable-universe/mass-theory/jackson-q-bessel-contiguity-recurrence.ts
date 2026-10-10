import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jackson-q-bessel-contiguity-recurrence",
  title:
    "First-order contiguity recurrence for the Jackson first- and second-kind $q$-Bessel coefficients (fibre-level)",
  lean: {
    ref: "qou:QOU.QBeta.qbessel_first_kind_coeff_closed_form",
    validation: "not_checked",
  },
  uses: ["rem:brings-curve"],
  tags: ["q-bessel", "su-q-1-1", "contiguity-recurrence", "fibre-level"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-30",
      body:
        "Statement extracted from rem:brings-q-hyperbolic-geometry per the q-Bessel deep-restructure plan (docs/workplans/2026-06-30-qbessel-deep-restructure-plan.md, bean c370). Conservative scope (first + second kind contiguity, fibre-level). Statement scope / SU_q(1,1)-weight phrasing flagged for the Q_beta/Habiro keystone (bean kehn) to confirm; lean ref resolves to the sorry-free QBesselContiguityRecurrence.lean.",
    },
  ],
});
