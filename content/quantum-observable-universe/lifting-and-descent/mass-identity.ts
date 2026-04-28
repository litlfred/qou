import { definition } from "../../schema/builders";

export default definition({
  label: "def:mass-identity",
  lean: { ref: "qou:QOU.categoricalMass", validation: "not_checked" },
  title: "Mass (categorical trace)",
  tags: ["mass", "categorical-trace", "frobenius-hopf"],
  uses: [
    "def:frobenius-pairing",
    "def:recursive-brane-tower",
  ],
});
