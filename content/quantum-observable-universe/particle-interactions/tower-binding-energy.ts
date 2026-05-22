import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tower-binding-energy",
  title:
    "Nuclear binding energy from the $3$-channel brane tower",
  tags: [
    "binding-energy",
    "brane-tower",
    "wedderburn",
    "three-channel",
    "partition-function",
    "zero-fitting",
    "analytic-continuation",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.towerBinding",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-tower-operator-valued",
        "rem:hecke-charge-mass-duality",
  ],
});
