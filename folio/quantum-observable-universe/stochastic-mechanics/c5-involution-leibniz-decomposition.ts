import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:c5-involution-leibniz-decomposition",
  lean: {
    ref: "qou:QOU.BraidKnot.c5_decomposition_via_quantum_two",
    validation: "not_checked",
  },
  title:
    "Decomposition quantity $c_5^{\\mathrm{dec}} = -b^2 - 1/2 = -3/2 + 1/[2]_q^2$",
  uses: ["prop:silver-ratio-beta-decay-null"],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
    "jones1985",
  ],
  tags: [
    "lean-infrastructure",
    "c5-outlier",
    "involution-operator",
    "averaged-crossing",
    "bar-invariance",
    "leibniz-propagation",
  ],
  computation: {
    engine: "python",
    script: "computations/qbeta/qbeta_silver_ratio_pell_lucas_ck.py",
    witness: [
      "computations/qbeta/qbeta-silver-ratio-pell-lucas-ck.witness.json",
    ],
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "refined-framing",
      body:
        "Added when promoting this block from the source PR into the level-selection rule PR. This block *interprets* the unique averaging-resonant rung $k = 5$ identified in `thm:averaging-resonance-rule` (planned, not yet derived) — it does **not** by itself derive *why* the resonance lives at rung 5. The involution $P_{\\mathrm{avg}} = (1 + \\overline{\\,\\cdot\\,})/2$ supplies the **magnitude** of the $1/2$ fingerprint; the **half-fill cyclicity** $k = \\lfloor n_{\\text{total}}/2 \\rfloor = 5$ for the proton typed-$\\mathbf{B}_3$ recipe supplies the **rung selection**. The Leibniz propagation discussion below interprets the $1/2$ as a Markov-trace expansion fingerprint and is consistent with both layers, but reading 'Leibniz alone explains $c_5$' overfits the rung — the half-fill argument is essential. See `thm:averaging-resonance-rule` §'Why $k = 5$ specifically' (planned).",
    },
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "**Statement restated 2026-11-21 to what the Lean proves (owner ruling on the PR #8819 follow-up): it now defines c₅^dec = −b² − 1/2 and states b² = 1 − 1/[2]_q², hence c₅^dec = −3/2 + 1/[2]_q²; the identification with the ladder rung c₅ is explicitly not claimed.** Earlier disclosure: the `lean.ref` theorem proves a rational-function identity for `c5Decomposition q`, which the Lean *defines* as −b(q)² − 1/2 with b² the Hoefsmit expression. That this quantity is the rung-5 ladder coefficient c₅ is not derived in the Lean. The narrative proof contains two slips recorded by the audit: it writes h/2 = 1/2, but at the silver ratio h = q − q⁻¹ = 2; and it speaks of two averaged crossings where the second factor is σ₁⁻¹. Found by the blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B01; bean qou-xxa9).",
    },
  ],
});
