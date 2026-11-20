import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:weak-spectral-completeness",
  lean: { ref: "qou:QOU.Conjectures.WeakSpectralCompleteness" },
  title:
    "Plancherel completeness for the EW/Higgs $\\{T(2,4), T(2,6), T(2,8)\\}$ idempotent decomposition",
  uses: [
    "thm:em-spectral-completeness",
    "thm:hoefsmit-ew-cell-content",
    "conj:g-action-on-substrate",
    "prop:torus-embeddable-complete",
    "prop:bar-t-duality-substrate",
  ],
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): from\nthe [weak-sector symmetric-channel Plancherel normalization](#prop:weak-symmetric-normalization) (a downstream block that itself uses this conjecture)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): — the substrate-level\n[bar T-duality](#prop:bar-t-duality-substrate) at the trace level" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): each $\\sigma_i^{2k}$ is bar-self-dual on its own (`prop:even-twist-torus-link-psd-feasibility`) [label does not resolve to any block]" },
    {
      kind: "refined-framing",
      body: "**Demoted.** Earlier drafts of this proof used\nPlancherel weights $w_X = 1/[2]_q$ as a \"uniform completeness\nsignature.\" That uniform-weight expression was a degenerate\nartifact of the dimensionally-collapsed $H_2(q)$-only\nformulation (six rank-1 projectors cannot fit in a 2-dim\nalgebra). The Hoefsmit $n=6$ formulation supersedes it.",
    },
    {
      kind: "status",
      body: "**Open.** Requires two prerequisite conjectures (U2 + U4)\nplus authoring of $\\mathcal{N}_{\\rm sym}(q)$; see\n`docs/audits/-path-alpha-bring-refinement.md` for the\nprioritization plan.\n\n**To promote to `proposition`:**\n1. Discharge U2\n   (conj:force-carrier-knot-vs-link-dichotomy)\n   — categorical knot-vs-link distinction in $\\mathbf{Rep}$.\n   Note: this is now purely categorical, since the host-surface\n   distinctness assumption has been **dropped** (all carriers\n   live on Bring per\n   [prop:torus-embeddable-complete](#prop:torus-embeddable-complete)).\n2. Discharge U4\n   (conj:electroweak-mass-eigenstate-count)\n   — categorical broken-Wedderburn split.\n3. Author `prop:weak-symmetric-normalization` —\n   $\\mathcal{N}_{\\rm sym}(q) \\in R$ as the symmetric-channel\n   Plancherel weight, analog of\n   [`conj:gram-determinant-plancherel-ratio`](#conj:gram-determinant-plancherel-ratio).\n4. Run PSLQ at 1000 dps on the **structurally constrained**\n   extended basis $\\{[4]_q, [6]_q, [8]_q, [2]_q, q^k, h^k,\n   \\mathcal{N}_{\\rm sym}(q)\\}$ to search for a candidate closed\n   form for $N_v$. A PSLQ hit is a fit, not a derivation.",
    },
  ],
});
