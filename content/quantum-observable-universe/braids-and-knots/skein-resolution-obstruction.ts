import { definition } from "../../schema/builders";

export default definition({
  label: "def:skein-resolution-obstruction",
  title:
    "Skein resolution obstruction $\\kappa_c^{\\mathrm{comp}}(L, q)$",
  tags: [
    "obstruction",
    "yekutieli",
    "skein-resolution",
    "computational-horizon",
    "P-vs-NP",
    "q-dependent",
    "cohomology",
  ],
  lean: { ref: "qou:QOU.SkeinResolutionObstruction",
    validation: "not_checked",
  },
  uses: [
    // def:computational-horizon dropped (2026-06-09): the prose never
    // relies on the info-theory horizon — this skein obstruction is a
    // *parallel* evaluation of the same χ(A) class, not a consumer of
    // the computational horizon. The dependency direction was inverted.
    "thm:qou-obstruction-reduction",
    "rem:kummer-filtration-obstruction",
    "prop:ns-obstruction-tower",
  ],
});
