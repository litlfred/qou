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
  // Detangler forward-ref demote (bean foxn): def:computational-horizon
  // (information-theory, a later chapter) is a thematic link, not a logical
  // dependency — the .md defines κ_c^comp self-containedly via χ(A) + Kummer
  // reduction and never references it. Dropped the spurious forward edge.
  uses: [
    "thm:qou-obstruction-reduction",
    "rem:kummer-filtration-obstruction",
    "prop:ns-obstruction-tower",
  ],
});
