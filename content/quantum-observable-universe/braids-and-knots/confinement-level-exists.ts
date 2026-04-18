import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-level-exists",
  title: "Existence of the confinement level",
  lean: {
    decl: "QOU.BraidKnot.ConfinementLevel.exists",
    validation: "not_checked",
  },
  uses: [
    "def:confinement-level",
    "def:knot-operator-energy",
    "prop:knot-operator-energy-exists",
    "def:hecke-normal-form",
  ],
  tags: ["existence", "confinement", "filtration"],
});
