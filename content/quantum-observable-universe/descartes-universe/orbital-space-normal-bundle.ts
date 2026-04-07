import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:orbital-space-normal-bundle",
  title:
    "The orbital space at shell $n$ is the space of framing-$k$ sections of the normal bundle",
  tags: [
    "orbital",
    "normal-bundle",
    "framing",
    "laplacian",
    "eigenmode",
    "resonance",
    "trefoil",
    "seifert-surface",
  ],
  lean: {
    decl: "QOU.orbital_space_normal_bundle",
    validation: "not_checked",
  },
  uses: ["prop:reidemeister-mass-invariance"],
});
