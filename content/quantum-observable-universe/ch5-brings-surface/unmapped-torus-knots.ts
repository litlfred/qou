import { remark } from "../../schema/builders";

export default remark({
  label: "rem:unmapped-torus-knots",
  title: "Unmapped genus-$4$ torus knot generators",
  interprets: "prop:torus-embeddable-complete",
  tags: [
    "torus-knot",
    "genus-4",
    "saturating",
    "unmapped",
    "dark-sector",
    "graviton",
    "sterile-neutrino",
  ],
  uses: [
    "prop:torus-knot-generators",
    "prop:torus-embeddable-complete",
    "thm:embeddability-closure",
    "def:categorical-proton",
    "def:categorical-neutron",
    "def:knot-particle-generation",
  ],
});
