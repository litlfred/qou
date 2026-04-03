import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:aeon-boundary-generates-chart",
  title: "Aeon boundary generates an affine chart",
  tags: [
    "aeon", "jet-horizon", "affine-chart",
    "integrability", "light-cone",
  ],
  lean: {
    decl: "QOU.aeon_boundary_generates_chart",
    validation: "not_checked",
  },
  uses: [
    "def:aeon",
    "def:jet-horizon",
    "def:big-bang-state",
    "def:bundle-initial-conditions",
  ],
});
