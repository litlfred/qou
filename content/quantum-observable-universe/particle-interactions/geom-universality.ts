import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:geom-universality",
  title:
    "Universality of $\\mathrm{Geom}(K)$: the categorical volume form yields $\\mathrm{Vol}(K)$ and $\\mathrm{CS}(K)$",
  lean: { ref: "qou:QOU.BraidKnot.geom_universality",
    validation: "not_checked",
  },
  uses: [
    "prop:geom-yekutieli-alignment",
    "prop:topological-mass-formula",
    "thm:topological-mass",
    "def:yekutieli-lifting-condition",
  ],
  cites: ["yekutieli2015", "neumann-zagier1985"],
  tags: [
    "universality",
    "volume-conjecture",
    "chern-simons",
    "neumann-zagier",
    "thurston",
    "rigid-dualizing",
    "frobenius-pairing",
  ],
});
