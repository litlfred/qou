import { definition } from "../../schema/builders";

export default definition({
  label: "def:mass-identity",
  examples: ["ex:mass-identity-su2"],
  // 2026-10-10: ref moved to the mass integrand Ψ (MassTraceIdentity). Before that:
  // was `qou:QOU.categoricalMass` — wrong declaration entirely. That name is
  // ambiguous (four distinct "categorical mass" constructs exist in the Lean
  // tree; see bean qou-qc6s) and none of them is this block. The canonical
  // declaration is `QOU.Torsion.MassIdentity`, which carries this block's own
  // LaTeX label `\label{def:mass-identity}`, and whose siblings back
  // `mass-identity-C.ts`, `mass-identity-exists.ts` and `mass-identity-unique.ts`.
  lean: { ref: "qou:QOU.Torsion.MassTraceIdentity.massIntegrand", validation: "not_checked" },
  title: "Mass (Frobenius form of the mass integrand)",
  tags: ["mass", "categorical-trace", "frobenius-hopf"],
  uses: [
    "def:frobenius-pairing",
    "def:recursive-brane-tower",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-10-10",
      body:
        "**Typed and proved (bean qou-puwe, defect 1; goal milestone qou-ywyq).** The definition used to " +
        "apply the categorical trace on $\\mathrm{End}(A)$ to $\\Psi \\circ \\varrho \\colon \\mathbf{1} \\to A$, " +
        "which does not typecheck. It now integrates the composite $\\int_A \\circ \\Psi \\circ \\varrho$, the reading " +
        "that reproduces the Markov-trace values of `prop:categorical-mass-markov`; the alternative " +
        "(trace of $L_\\varrho \\circ \\Psi$) is the regular trace and does not. Proved sorry-free in " +
        "`QOU/Torsion/MassTraceIdentity.lean`: `frobeniusForm_massIntegrand` ($\\int_A(\\Psi \\varrho) = \\int_A(u\\varrho)$), " +
        "`frobeniusForm_massIntegrand_of_frobeniusForm_eq_counit` ($= \\int_A \\varrho$ when $\\int_A = \\varepsilon$), " +
        "`massTrace_eq_functional_hol` (the trace reading). The choice between the two readings was put to the " +
        "owner on 2026-10-10. The sibling `mass-identity.lean` still documents the old formula, and " +
        "`QOU.Torsion.MassIdentity` (the multiplicative-integration structure) is not identified with this definition.",
    },
  ],
});
