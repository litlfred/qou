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
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "**Holonomy product and Temperley–Lieb state sum (owner decision Q-YWYQ-1, options 1 and 3; bean qou-puwe).** " +
        "(1) In `QOU/Torsion/MassTraceIdentity.lean`, a word $w$ of transports is multiplied first in the non-abelian " +
        "convolution monoid $\\mathrm{Hom}(\\mathbf{1}, A)$ via `hol` (`hol_append`, `leftMul_hol_append`), and then evaluated " +
        "under the Frobenius mass functional (`frobeniusForm_massIntegrand_hol`, `frobeniusForm_massIntegrand_hol_of_frobeniusForm_eq_counit`) " +
        "or the left-multiplication trace (`massTrace_eq_functional_hol`). The sibling `mass-identity.lean` now exposes " +
        "`cycleFrobeniusEval` and `cycleMassTrace` directly on `MassTraceIdentity.hol`. " +
        "(3) In `QOU/Torsion/MassTraceMarkov.lean` and `QOU/Torsion/MassTraceMarkovClass.lean`, each crossing transport " +
        "$T(a, \\varepsilon) = c(\\varepsilon)\\cdot 1 - e_a$ (`transport_eq_lead_sub_tlProjector`, `tlProjector_sq`) expands " +
        "the ordered holonomy `hol q qi ℓs` (`hol_eq_tlStateSum`), the Markov trace (`braidTrace_wordBraid_eq_tlStateSum`), " +
        "and the braid-class mass (`massClass_wordBraid_eq_tlStateSum`) as a state sum over $s \\colon \\mathrm{Fin}\\,\\ell s.\\mathrm{length} \\to \\mathrm{Bool}$, " +
        "with the $s \\equiv \\mathrm{false}$ state recovering the per-crossing scalar product (`braidTrace_wordBraid_eq_leadProd_add_tlStates`).",
    },
    {
      kind: "status",
      date: "2026-10-12",
      body:
        "**Braid classes (owner decision 1c, 2026-10-12; bean qou-ywyq).** The mass identity is stated on " +
        "braid classes, braids modulo conjugation and positive or negative stabilisation, so the algebra " +
        "covers it fully. Proved sorry-free in `QOU/Torsion/MassTraceMarkovClass.lean`: `artinTower` (the Artin " +
        "braid groups as a Markov tower), `jonesTot_isMarkovInvariant` (the framing-corrected trace at " +
        "$w = (1, q^2)$ respects both moves), `massClass` (its descent), `exists_wordBraid`, and " +
        "`massClass_wordBraid` (the identity on classes). The passage from braid classes to links " +
        "(Alexander–Markov) is cited, not proved, and is used by no statement.",
    },
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
