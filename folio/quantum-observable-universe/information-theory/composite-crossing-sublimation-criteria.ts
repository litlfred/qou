import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:composite-crossing-parity",
  label: "rem:composite-crossing-sublimation-criteria",
  title: "Sublimation, crossing parity, and the full phase criterion",
  tags: [
    "sublimation",
    "crossing-parity",
    "phase-behaviour",
    "withdrawn-mechanism",
  ],
  uses: [
    "prop:phase-transition-boundary",
    "prop:knot-eigenbasis-complete",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-24",
      body:
        "**The $\\mathrm{Ext}^1$ mechanism is withdrawn; the classification is retained as empirical.** This remark stated the sublimation criterion as a split/non-split dichotomy for an extension classified by $\\mathrm{Ext}^1_{H_n(q)}(S_{\\mathrm{asym}}, S_{\\mathrm{sym}}) \\cong \\mathbb{Z}$ — the same claim as [`prop:phase-transition-boundary`](#prop:phase-transition-boundary), with $S$ in place of $V$. It falls for the same reasons, recorded in full on that block: $\\mathrm{Ext}^1$ over a $k$-algebra is a $k$-module and cannot be $\\mathbb{Z}$ over $\\mathbb{R}$; $H_n(q)$ is semisimple away from roots of unity, so $\\mathrm{Ext}^1$ vanishes outright. One reason is specific to this block's phrasing: the $S_\\lambda$ are the *irreducible* summands of $V^{\\otimes n}$ by [`prop:knot-eigenbasis-complete`](#prop:knot-eigenbasis-complete)(1), and an irreducible module admits no short exact sequence with nonzero ends at all, semisimplicity aside. The four-case valence-shell classification and the crossing-parity statement $n_K(\\mathcal{A}) \\equiv Z \\pmod 2$ are untouched by the withdrawal — the parity is arithmetic from the crossing budget, and the classification never depended on the Ext group for anything but its vocabulary. Both are now stated without a derivation, which is what they are. `tags` lost `hecke-extension` accordingly. Bean `qou-zut2`.",
    },
  ],
});
