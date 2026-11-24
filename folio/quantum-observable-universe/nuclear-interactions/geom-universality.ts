import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:geom-universality",
  title:
    "Universality of $\\mathrm{Geom}(K)$: the categorical volume form yields $\\mathrm{Vol}(K)$ and $\\mathrm{CS}(K)$",
  lean: { ref: "qou:QOU.BraidKnot.geom_universality",
    validation: "not_checked",
  },
  uses: ["conj:geom-yekutieli-alignment"],
  cites: ["yekutieli2015", "neumann-zagier1985"],
  tags: [
    "tier:S",
    "universality",
    "volume-conjecture",
    "chern-simons",
    "neumann-zagier",
    "thurston",
    "rigid-dualizing",
    "frobenius-pairing",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-08-24-vacuous-prop-carrier-probe.lean` (`Cand22`) records that the pre-repair `PLCorrectnessHypotheses` field `(0 : ℝ) ≤ 0` was trivially inhabited.",
      see: "docs/audits/2026-08-24-vacuous-prop-carrier-probe.lean",
    },
  ],
});
