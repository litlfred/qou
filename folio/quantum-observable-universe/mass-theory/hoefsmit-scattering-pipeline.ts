import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hoefsmit-scattering-pipeline",
  title:
    "From Hoefsmit scattering weights to physical mass via the observation frame",
  lean: { ref: "qou:QOU.BraidsAndKnots.BraidKnot.hoefsmit_pipeline_conditional",
    validation: "not_checked",
  },
  uses: ["conj:geom-yekutieli-alignment"],
  cites: ["hoefsmit1974", "wenzl1988"],
  tags: [
    "hoefsmit",
    "r-matrix",
    "scattering",
    "markov-trace",
    "jones-polynomial",
    "observation-frame",
    "pipeline",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-08-24-vacuous-prop-carrier-probe.lean` (`Cand13`) records the pre-repair `QOU.BraidKnot.PLCorrectnessHypotheses` vacuity check on `QOU.BraidKnot.ConditionalClasses`.",
      see: "docs/audits/2026-08-24-vacuous-prop-carrier-probe.lean",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): and `rem:baryon-period-ratio`).**" },
  ],
});
