import { definition } from "../../schema/builders";

export default definition({
  label: "def:nuclear-threading-link",
  title: "Nuclear threading link (braid shortcut)",
  tags: [
    "nucleus",
    "threading-link",
    "braid-shortcut",
    "torus-link",
    "binding-energy",
    "stability",
    "lower-energy",
  ],
  lean: {
    decl: "QOU.Torsion.NuclearThreadingLink",
    validation: "not_checked",
  },
  uses: [
    "def:stable-nucleus",
    "def:threading-link",
    "def:crossing-energy",
    "def:skein-binding-lagrangian",
    "rem:skein-crossing-asymmetry",
    "def:categorical-proton",
    "def:categorical-neutron",
  ],
});
