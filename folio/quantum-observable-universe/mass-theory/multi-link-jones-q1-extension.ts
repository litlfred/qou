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
    script: "computations/probe_q_beta_c5_c6_multilink.py",
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Multi-link Jones values at $q = 1$ — Lean infrastructure for the $c_5 / c_6$ candidate investigation.**\n\nWhat follows is **infrastructure, not closure**. The Lean module `QOU.BraidKnot.multi_link_jones_q1_extension` exports:\n\n1. **Three new `Link` constructors** (extending the `Link` inductive in [`rem:braid-link-types`](#rem:braid-link-types)): `trefoil`, `borromean`, `doubleHopf`.\n2. **Three new `jonesAtOne` cases**, each proved by `rfl`:\n\n   | constructor | $J_L(q{=}1)$ | source |\n   |---|---:|---|\n   | `trefoil` | $+1$ | Jones 1985, $T(2,3)$ 1-component unnormalised |\n   | `borromean` | $-8$ | Jones 1985 / Habiro 2002, 3-component Brunnian |\n   | `doubleHopf` | $+4$ | $J_{\\mathrm{Hopf}}^2$ by disjoint-union multiplicativity |\n\n3. **Two combination values**: `jonesHopfTimesBorromean = 16`, `jonesBorromeanFlipped = 8`. Both candidates carry **explicit docstrings noting the empirical mismatch**. They are not closures." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      body: "**Open R&D recorded.** The Lean class `MultiLinkJonesAtOne` is the\nhook — once an empirical or theoretical match is found, a new\ninstance plugs in the right $(c_5, c_6)$ values and the\nprecision-ladder extension auto-picks-up. Until then the default\ninstance carries the probe's exploratory placeholders with the\nmismatch explicitly documented.",
    },
  ],
});
