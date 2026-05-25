import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:geom-yekutieli-alignment",
  title:
    "Geometric invariant $\\mathrm{Geom}(K)$ as rigid dualizing evaluation",
  lean: { ref: "qou:QOU.BraidKnot.geom_yekutieli_alignment",
    validation: "not_checked",
  },
  uses: [
    "prop:topological-mass-formula",
    "def:yekutieli-lifting-condition",
    "prop:yekutieli-lifting",
    "conj:hyperbolic-volume-transcendence",
  ],
  cites: ["yekutieli2010", "yekutieli2015"],
  tags: [
    "rigid-dualizing",
    "yekutieli",
    "frobenius-pairing",
    "self-duality",
    "thurston-geometrization",
    "volume-conjecture",
    "chern-simons",
  ],
});
