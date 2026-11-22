import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:colour-relabel-singlet",
  lean: {
    ref: "qou:QOU.Braiding.ColourRelabel.swap01_eps_proportional_iff",
    validation: "not_checked",
  },
  title: "Swapping two colours preserves the quantum singlet only at q squared equal to one",
  tags: ["colour", "quantum-group", "braid-group"],
  uses: ["prop:colour-singlet-flavour-generator"],
});
