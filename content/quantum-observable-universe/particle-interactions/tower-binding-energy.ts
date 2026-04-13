import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tower-binding-energy",
  title:
    "Nuclear binding energy from the $2{\\times}2$ brane tower",
  tags: [
    "binding-energy",
    "brane-tower",
    "wedderburn",
    "standard-channel",
    "partition-function",
    "zero-fitting",
  ],
  lean: {
    decl: "QOU.ParticleInteractions.tower_binding_energy",
    validation: "not_checked",
  },
  uses: [
    "thm:topological-mass",
    "def:recursive-brane-tower",
    "prop:mass-endomorphism-tower",
    "prop:atomic-braid-mass",
    "rem:hecke-charge-mass-duality",
  ],
});
