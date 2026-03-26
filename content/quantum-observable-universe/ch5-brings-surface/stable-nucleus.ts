import { definition } from "../../schema/builders";

export default definition({
  label: "def:stable-nucleus",
  title: "Stable nucleus (Skein energy minimum)",
  tags: [
    "nucleus",
    "stability",
    "hadron",
    "proton",
    "neutron",
    "binding",
    "beta-stability",
    "lagrangian",
  ],
  lean: {
    decl: "QOU.Torsion.StableNucleus",
    validation: "not_checked",
  },
  uses: [
    "def:hadron",
    "def:categorical-proton",
    "def:categorical-neutron",
    "def:skein-binding-lagrangian",
    "prop:beta-stability",
    "def:substrate-parameter",
  ],
});
