import { remark } from "../../schema/builders";

export default remark({
  label: "rem:multi-link-jones-q1-extension",
  interprets: "prop:q-beta-categorical-precision-ladder",
  title:
    "Multi-link Jones values at $q=1$ (trefoil $+1$, Borromean $-8$, double-Hopf $+4$) as candidate $c_5/c_6$ inputs for the $\\mathfrak{Q}_\\beta$ precision ladder — Lean infrastructure with explicit open-R&D status: simple multi-link candidates do NOT match empirical $c_5 \\approx -395$, $c_6 \\approx -45485$",
  uses: ["rem:ck-extraction-from-algebraic-rules"],
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
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      body: "**Open R&D recorded.** The Lean class `MultiLinkJonesAtOne` is the\nhook — once an empirical or theoretical match is found, a new\ninstance plugs in the right $(c_5, c_6)$ values and the\nprecision-ladder extension auto-picks-up. Until then the default\ninstance carries the probe's exploratory placeholders with the\nmismatch explicitly documented.",
    },
  ],
});
