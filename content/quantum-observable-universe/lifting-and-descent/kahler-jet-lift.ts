import { definition } from "../../schema/builders";

export default definition({
  label: "def:kahler-jet-lift",
  lean: {
    decl: "QOU.LiftingAndDescent.Stubs.kahler_jet_lift",
    file: "QOU/LiftingAndDescent/Stubs.lean",
    validation: "not_checked",
  },
  title: "Kähler differential jet lift of the per-generator traced volume",
  uses: [
    "def:recursive-brane-tower",
    "def:jet-prolongation",
    "prop:tower-binding-energy",
  ],
  tags: [
    "kahler-differential",
    "jet-lift",
    "brane-tower",
    "vertex-volume",
  ],
});
