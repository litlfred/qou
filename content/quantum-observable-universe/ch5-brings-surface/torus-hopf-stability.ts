import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:torus-hopf-stability",
  title:
    "Torus knot composites on Bring's surface are stable hadrons",
  tags: [
    "stability",
    "torus-knot",
    "hadron",
    "euler-characteristic",
    "crossing-energy",
  ],
  lean: {
    decl: "QOU.Descartes.torus_hopf_stability",
    validation: "not_checked",
  },
  uses: [
    "def:hadron",
    "def:crossing-energy",
    "def:coulomb-charge",
    "prop:torus-knot-generators",
    "rem:skein-crossing-asymmetry",
    "def:categorical-proton",
    "def:categorical-neutron",
  ],
});
