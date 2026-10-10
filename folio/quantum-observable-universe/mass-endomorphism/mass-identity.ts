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
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-10",
      body:
        "**The prose and the `lean.ref` formalise different objects; not yet resolved.** " +
        "This block *defines* mass as the Frobenius–Hopf categorical trace " +
        "$\\mathfrak{m}(\\varrho) = \\lVert \\mathrm{tr}((\\int_A \\otimes \\mathrm{id}) \\circ \\Delta \\circ \\varrho) \\rVert$. " +
        "The referenced declaration `QOU.Torsion.MassIdentity` is a structure holding a vortex cycle " +
        "and two factors of **nonabelian multiplicative integration** " +
        "($m = \\lVert \\mathrm{MI}\\!\\int_\\Sigma (\\nabla_A q, L \\wedge F^+) \\rVert$); neither text " +
        "states the other's formula, and no declaration asserts that the two agree. " +
        "Separately, the sibling `.lean` defines `frobeniusMass` (generic $R$) and `scalarMass` " +
        "($R \\to \\mathbb{R}$), the two names the *Archimedean specialisation* paragraph uses, " +
        "but `frobeniusMass` takes the trace value as an input rather than computing it, so it " +
        "does not formalise the trace formula either. " +
        "As written, the argument of $\\mathrm{tr}$ is a morphism $\\mathbf{1} \\to A$ " +
        "(via $\\mathbf{1} \\otimes A \\cong A$), whereas $\\mathrm{tr}$ is declared on " +
        "$\\mathrm{End}_{\\mathbf{C}}(A)$; the endomorphism is $(\\int_A \\otimes \\mathrm{id}) \\circ \\Delta$ " +
        "before precomposition with $\\varrho$. Which object this block means is an open author decision " +
        "(bean qou-puwe, defect 1).",
    },
  ],
});
