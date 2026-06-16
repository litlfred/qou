import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:c5-involution-leibniz-decomposition",
  lean: {
    ref: "qou:QOU.BraidKnot.C5InvolutionLeibnizDecomposition",
    validation: "not_checked",
  },
  title:
    "$c_5$ decomposes as $-b^2 - 1/2$: pure-$\\sigma$ Kashiwara contribution plus bar-invariant involution fingerprint from averaged-crossing structure. Interpretation of the unique averaging-resonant rung k = 5 identified in `thm:averaging-resonance-rule` (planned, not yet derived); involution supplies the $1/2$ magnitude, while the half-fill cyclic structure supplies the rung selection.",
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
    {
      kind: "refined-framing",
      body:
        "Added when promoting this block from the source PR into the level-selection rule PR. This block *interprets* the unique averaging-resonant rung $k = 5$ identified in `thm:averaging-resonance-rule` (planned, not yet derived) — it does **not** by itself derive *why* the resonance lives at rung 5. The involution $P_{\\mathrm{avg}} = (1 + \\overline{\\,\\cdot\\,})/2$ supplies the **magnitude** of the $1/2$ fingerprint; the **half-fill cyclicity** $k = \\lfloor n_{\\text{total}}/2 \\rfloor = 5$ for the proton typed-$\\mathbf{B}_3$ recipe supplies the **rung selection**. The Leibniz propagation discussion below interprets the $1/2$ as a Markov-trace expansion fingerprint and is consistent with both layers, but reading 'Leibniz alone explains $c_5$' overfits the rung — the half-fill argument is essential. See `thm:averaging-resonance-rule` §'Why $k = 5$ specifically' (planned).",
    },
  ],
});
