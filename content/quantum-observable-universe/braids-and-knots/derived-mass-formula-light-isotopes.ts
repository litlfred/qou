import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:derived-mass-formula-light-isotopes",
  title: "Derived-only mass formula reproduces light atomic masses to sub-percent",
  lean: {
    decl: "QOU.WedderburnMass.derivedLightIsotopeFormula",
    validation: "not_checked",
  },
  uses: [
    "thm:wedderburn-mass-formula",
    "prop:binding-scale-catalan",
    "prop:wigner-np-pairing",
    "prop:frobenius-s-classification",
    "prop:three-parameters-wedderburn",
    "prop:confined-knot-binding",
    "conj:shell-correction-term-seven",
  ],
});
