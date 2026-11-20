import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-20",
      body: "**Gröbner--Shirshov basis corrected (owner decision, 2026-11-20; bean `qou-w12g`).** This block previously stated that $G = \\{$Hecke, Yang--Baxter, far commutativity$\\}$ is the Gröbner--Shirshov basis of $H_A(q)$. That is false for $A \\geq 4$: `UGB.GrobnerShirshov.Hecke.NotAGSBasis.hecke_not_gs_basis_four` (sorry-free) exhibits an irreducible composition. The basis is now the Bokut--Shiao completion, matching `def:hecke-normal-form` (corrected 2026-09-13, bean `qou-43co`). The Hecke-only chain reduction of `prop:tm-gs-normal-form` produces strictly increasing words, which contain no Bokut--Shiao leading word, so the chain normal forms it computes are unchanged by the completion.\n\n**Scope of the Lean support.** The GS-basis property of the completed system is machine-checked for real $q > 0$, $q \\neq 1$ (`heckeCompleted_isGrobnerShirshovBasis`), not over $\\mathbb{Z}[q^{\\pm 1}]$; the deformed type-A primary (Kang--Lee--Lee--Oh 2002) is not held (bean `qou-qspu`). Path-independence uses `local_confluence`, still an axiom citing Bergman 1978 §3; termination (`reduction_well_founded`) is proved since 2026-11-20.",
    },
  ],
  label: "prop:nuclear-groebner-reduction",
  title:
    "Unique nuclear normal form via Gröbner reduction in $H_n(q)$",
  tags: [
    "groebner-basis",
    "hecke-algebra",
    "braid-word",
    "normal-form",
    "nuclear",
    "skein-relation",
    "temperley-lieb",
    "admissible-system",
  ],
  lean: { ref: "qou:QOU.Archimedean.nuclear_groebner_reduction",
    validation: "not_checked",
  },
  uses: [
    "prop:braiding-eigenvalue-extraction",
    "rem:hecke-algebra-from-braiding",
    "unital-groebner-bases:def:groebner-basis",
    "unital-groebner-bases:def:division-algorithm",
    "def:hecke-normal-form",
  ],
  cites: ["bokut2001", "bergman1978"],
});
