import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:weak-spectral-completeness",
  lean: { ref: "qou:QOU.BraidKnot.WeakSpectralCompleteness" },
  title:
    "Plancherel completeness for the EW/Higgs $\\{T(2,4), T(2,6), T(2,8)\\}$ idempotent decomposition",
  uses: ["thm:em-spectral-completeness"],
  tags: [
    "tier:S",
    "electroweak",
    "spectral-completeness",
    "plancherel",
    "weak-coupling",
    "force-carrier",
    "nv-1",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Open.** Requires two prerequisite conjectures (U2 + U4)\nplus authoring of $\\mathcal{N}_{\\rm sym}(q)$; see\n`docs/audits/-path-alpha-bring-refinement.md` for the\nprioritization plan.\n\n**To promote to `proposition`:**\n1. Discharge U2\n   (conj:force-carrier-knot-vs-link-dichotomy)\n   — categorical knot-vs-link distinction in $\\mathbf{Rep}$.\n   Note: this is now purely categorical, since the host-surface\n   distinctness assumption has been **dropped** (all carriers\n   live on Bring per\n   [prop:torus-embeddable-complete](#prop:torus-embeddable-complete)).\n2. Discharge U4\n   (conj:electroweak-mass-eigenstate-count)\n   — categorical broken-Wedderburn split.\n3. Author `prop:weak-symmetric-normalization` —\n   $\\mathcal{N}_{\\rm sym}(q) \\in R$ as the symmetric-channel\n   Plancherel weight, analog of\n   [`prop:gram-determinant-plancherel-ratio`](#prop:gram-determinant-plancherel-ratio).\n4. Run PSLQ at 1000 dps on the **structurally constrained**\n   extended basis $\\{[4]_q, [6]_q, [8]_q, [2]_q, q^k, h^k,\n   \\mathcal{N}_{\\rm sym}(q)\\}$ to verify the closed-form\n   prediction for $N_v$.",
    },
  ],
});
