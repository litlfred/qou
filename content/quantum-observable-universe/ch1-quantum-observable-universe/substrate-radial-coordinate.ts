import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:substrate-radial-coordinate",
  lean: {
    decl: "QOU.substrate_radial_coordinate",
    validation: "not_checked",
  },
  title: "Substrate parameter as the radial coordinate",
  tags: ["substrate", "projective", "boson", "fermion"],
  uses: [
    "def:contact-affine-chart",
    "def:substrate-parameter",
    "def:fermion-boson-decomposition",
    "def:quantum-planck-constant",
  ],
});
