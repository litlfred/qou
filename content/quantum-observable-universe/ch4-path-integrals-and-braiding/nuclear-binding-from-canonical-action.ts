import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:nuclear-binding-from-canonical-action",
  title:
    "Nuclear binding as evaluation of the canonical action on multi-nucleon links",
  tags: [
    "lagrangian",
    "canonical-action",
    "binding",
    "nuclear",
    "coulomb",
    "skein",
    "derivation",
  ],
  lean: {
    decl: "QOU.Braiding.nuclear_binding_from_canonical_action",
    validation: "not_checked",
  },
  uses: [
    "def:qou-canonical-action",
    "def:categorical-lagrangian",
    "def:skein-binding-lagrangian",
    "def:mass-identity",
    "rem:skein-crossing-asymmetry",
    "def:categorical-proton",
    "def:categorical-neutron",
    "def:substrate-parameter",
    "def:r-matrix-braiding",
    "def:categorical-dirac-operator",
  ],
  proofs: ["prf:nuclear-binding-from-canonical-action"],
});
