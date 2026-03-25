import { definition } from "../../schema/builders";

export default definition({
  label: "def:mass-identity",
  lean: { decl: "QOU.categoricalMass" },
  title: "Mass (categorical trace)",
  tags: ["mass", "categorical-trace", "frobenius-hopf"],
  uses: [
    "def:quantum-observable-universe",
    "def:frobenius-pairing",
    "def:recursive-brane-tower",
  ],
});
