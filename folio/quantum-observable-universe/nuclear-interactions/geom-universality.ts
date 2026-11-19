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
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
