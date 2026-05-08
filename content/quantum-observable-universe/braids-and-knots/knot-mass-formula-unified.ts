import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:knot-mass-formula-unified",
  title:
    "Unified mass formula: tower + Frobenius co-Casimir correction",
  lean: {
    ref: "qou:QOU.BraidKnot.knot_mass_unified",
    validation: "not_checked",
  },
  uses: [
    "prop:atomic-mass-gb-nf",
    "thm:frobenius-codim-universal",
    "prop:partition-sum-proton-residual",
    "conj:knot-factor-frobenius-pairing",
  ],
  cites: ["kassel1995"],
  tags: [
    "mass",
    "knot",
    "vortex",
    "frobenius",
    "co-casimir",
    "tower",
    "unified-formula",
    "universal",
  ],
});
