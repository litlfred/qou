import { definition } from "../../schema/builders";

export default definition({
  label: "def:mass-identity",
  lean: { decl: "QOU.MassIdentity" },
  status: "not_started",
  title: "Mass (categorical trace)",
  tags: ["mass", "categorical-trace", "frobenius-hopf"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
  ],
});
