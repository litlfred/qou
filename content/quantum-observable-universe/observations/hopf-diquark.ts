import { definition } from "../../schema/builders";

export default definition({
  label: "def:hopf-diquark",
  title: "Hopf diquark",
  tags: [
    "diquark",
    "hopf",
    "cooper-pair",
    "color-superconductivity",
    "color-antitriplet",
  ],
  lean: {
    decl: "QOU.Descartes.HopfDiquark",
    validation: "not_checked",
  },
  uses: [
    "conj:borromean-quark",
    "def:crossing-energy",
    "def:coulomb-charge",
  ],
});
