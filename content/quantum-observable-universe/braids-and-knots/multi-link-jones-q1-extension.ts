import { remark } from "../../schema/builders";

export default remark({
  label: "rem:multi-link-jones-q1-extension",
  lean: {
    ref: "qou:QOU.BraidKnot.multi_link_jones_q1_extension",
    validation: "not_checked",
  },
  interprets: "prop:q-beta-categorical-precision-ladder",
  title:
    "Multi-link Jones values at $q=1$ (trefoil $+1$, Borromean $-8$, double-Hopf $+4$) as candidate $c_5/c_6$ inputs for the $Q_\\beta$ precision ladder — Lean infrastructure with explicit open-R&D status: simple multi-link candidates do NOT match empirical $c_5 \\approx -395$, $c_6 \\approx -45485$",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
    "rem:braid-link-types",
    "rem:ck-extraction-from-algebraic-rules",
  ],
  cites: [
    "jones1985",
    "habiro2002",
    "wenzl1988",
  ],
  tags: [
    "lean-infrastructure",
    "multi-link",
    "jones-q1",
    "borromean",
    "trefoil",
    "double-hopf",
    "c5-c6-investigation",
    "open-rd",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_q_beta_c5_c6_multilink.py",
    witness: [
      "folio-assistant/computations/q-beta-c5-c6-multilink.witness.json",
    ],
    status: "experimental",
  },
});
