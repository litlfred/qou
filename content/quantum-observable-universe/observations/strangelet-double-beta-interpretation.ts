import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Corrected (opening claim).** The block asserted that $s \\approx " +
        "0.104$ matching $\\tanh(\\ln q)$ “is not a coincidence: both " +
        "measure the antisymmetric channel”, citing " +
        "`prop:crossing-energy-decomposition`. That citation does not support it, " +
        "for two independent reasons surfaced by the upstream `def:coulomb-charge` " +
        "correction. (1) The channel-*total* ratio is $((p + m)/(p - m))\\tanh(\\ln " +
        "q)$, and this block works in the $Q = 0$ sector — i.e. $p = m$ — where " +
        "the denominator vanishes and the channel ratio is undefined, so " +
        "$\\tanh(\\ln q)$ can only be the *per-crossing* weight ratio here. " +
        "(2) Identifying the bar-odd channel as electromagnetic is withdrawn " +
        "upstream: its coefficient is a sign-blind crossing count, and $Q$ scales " +
        "the bar-even channel. The numerical coincidence is retained as recorded " +
        "and the causal claim is withdrawn and flagged open rather than replaced " +
        "with a new mechanism; $\\Gamma_{2\\beta} \\sim s^4 \\approx 10^{-4}$ is " +
        "unchanged, now written in terms of $s$ itself rather than an " +
        "“EM/strong” ratio.",
      see: "docs/audits/2026-08-08-coulomb-decomposition-downstream-propagation.md",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**Open (not addressed here).** The block places the genus-$2$ sector at " +
        "$Q = 0$ while its knots $T_{2,5}^{\\sigma}$, $4_1$, $T_{2,3}^{\\sigma}$ " +
        "are written as mirrors, i.e. all-negative crossings, which under " +
        "`def:coulomb-charge` ($Q = \\tfrac{1}{2}(n_+ - n_-)$) give $Q \\neq 0$. " +
        "Reconciling the sector's $Q = 0$ with the mirror superscripts is an " +
        "author call and was left untouched.",
      see: "docs/audits/2026-08-08-coulomb-decomposition-downstream-propagation.md",
    },
  ],
  interprets: "prop:strangelet-double-beta",
  label: "rem:strangelet-double-beta-interpretation",
  title:
    "Skein amplitude, intermediate $4_1$ state, and observable double-beta signature",
  uses: [
    "def:coulomb-charge",
    "prop:strangelet-double-beta",
    "prop:crossing-energy-decomposition",
    "rem:building-block-knots",
  ],
  tags: [
    "strangelet",
    "double-beta-decay",
    "skein-amplitude",
    "electromagnetic-signature",
    "falsifiability",
    "interpretation",
  ],
});
