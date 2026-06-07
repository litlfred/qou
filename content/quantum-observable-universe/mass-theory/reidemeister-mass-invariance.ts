import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:reidemeister-mass-invariance",
  title:
    "Reidemeister invariance of mass and binding energy",
  tags: [
    "reidemeister",
    "mass",
    "binding-energy",
    "knot-invariant",
    "embedding",
    "shell-transition",
    "writhe",
  ],
  lean: { ref: "qou:QOU.Braiding.reidemeister_mass_invariance",
    validation: "not_checked",
  },
  uses: ["rem:hydrogen-orbitals"],
});
