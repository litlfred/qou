import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:colour-singlet-exterior-flavour-symmetric",
  lean: {
    ref: "qou:QOU.Braiding.ColourFlavourMirror.singlet_exterior_iff",
    validation: "not_checked",
  },
  title: "A colour-singlet state is q-exterior exactly when its flavour part is q-symmetric",
  tags: ["braid-group", "colour", "hecke-algebra", "quantum-group", "howe-duality"],
  uses: ["prop:colour-singlet-flavour-generator"],
});
