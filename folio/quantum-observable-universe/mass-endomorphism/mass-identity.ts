import { definition } from "../../schema/builders";

export default definition({
  label: "def:mass-identity",
  examples: ["ex:mass-identity-su2"],
  // Was `qou:QOU.categoricalMass` — wrong declaration entirely. That name is
  // ambiguous (four distinct "categorical mass" constructs exist in the Lean
  // tree; see bean qou-qc6s) and none of them is this block. The canonical
  // declaration is `QOU.Torsion.MassIdentity`, which carries this block's own
  // LaTeX label `\label{def:mass-identity}`, and whose siblings back
  // `mass-identity-C.ts`, `mass-identity-exists.ts` and `mass-identity-unique.ts`.
  lean: { ref: "qou:QOU.Torsion.MassIdentity", validation: "not_checked" },
  title: "Mass (categorical trace)",
  tags: ["mass", "categorical-trace", "frobenius-hopf"],
  uses: [
    "def:frobenius-pairing",
    "def:recursive-brane-tower",
  ],
});
