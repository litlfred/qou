import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:colour-braid-commuting-singlet",
  lean: {
    ref: "qou:QOU.Braiding.ColourRelabel.braid_commuting_fixes_singlet",
    validation: "not_checked",
  },
  title: "A linear map commuting with the colour braiding keeps the singlet line",
  tags: ["colour", "quantum-group", "braid-group"],
  uses: ["prop:colour-singlet-flavour-generator", "prop:colour-relabel-singlet"],
});
