import { definition } from "../../schema/builders";

export default definition({
  label: "def:atom-inductive-construction",
  title:
    "Inductive atom construction in Gröbner-normalized words",
  tags: [
    "atom",
    "inductive",
    "groebner-basis",
    "normal-form",
    "hecke-algebra",
    "torus-knot",
    "shell-structure",
    "hydrogen",
    "helium",
    "lithium",
  ],
  lean: {
    decl: "QOU.Descartes.atom_inductive_construction",
    validation: "not_checked",
  },
  uses: [
    "prop:nuclear-groebner-reduction",
    "thm:groebner-shirshov-energy",
    "prop:shell-closure-normal-form",
    "def:transfer-matrix-operator",
    "def:stable-nucleus",
    "conj:electron-shells-hopf",
    "rem:helium-hopf-diagram",
    "prop:torus-knot-shell-binding",
  ],
});
