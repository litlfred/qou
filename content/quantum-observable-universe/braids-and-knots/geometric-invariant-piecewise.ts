import { remark } from "../../schema/builders";

export default remark({
  label: "rem:geometric-invariant-piecewise",
  title: "Piecewise geometric invariant $\\mathrm{Geom}(K)$",
  interprets: "prop:topological-mass-formula",
  uses: [
    "thm:topological-mass",
    "prop:nuclear-knot-classification",
    "conj:em-coupling-chern-simons",
  ],
  tags: [
    "thurston-geometrization",
    "volume-conjecture",
    "chern-simons",
    "frobenius-pairing",
    "self-duality",
  ],
});
