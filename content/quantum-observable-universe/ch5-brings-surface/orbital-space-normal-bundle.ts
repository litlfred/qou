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
    decl: "QOU.Descartes.orbital_space_normal_bundle",
    validation: "not_checked",
  },
  uses: [
    "def:electron-knot",
    "prop:reidemeister-mass-invariance",
    "rem:hydrogen-orbitals",
    "def:categorical-reeb",
    "prop:fiber-adjoint-involution",
  ],
});
