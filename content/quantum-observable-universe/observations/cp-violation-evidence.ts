import { prose } from "../../schema/builders";

export default prose({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Corrected (quantitative gap).** The section quoted " +
        "$\\tanh(\\ln q) \\approx 0.104$ as *the* EM-to-strong ratio supplied by " +
        "`prop:crossing-energy-decomposition`, unqualified. That constant is the " +
        "channel ratio only on the positive-braid locus $m = 0$; in general the " +
        "ratio carries a multiplicity factor $(p + m)/(p - m)$ " +
        "(`crossing-energy-decomposition.md` claim 4). Kaons are precisely the " +
        "mixed-chirality case, so the unqualified constant was the one reading " +
        "the cited proposition does not license. The $\\delta_{\\mathrm{CP}} " +
        "\\sim 10^{-3}$ order-of-magnitude agreement is retained as recorded; " +
        "the qualifier and the unevaluated factor are now stated. Additionally, " +
        "per the upstream `def:coulomb-charge` correction, identifying the " +
        "bar-odd channel as the electromagnetic one is withdrawn pending an " +
        "author call — $Q$ scales the bar-even channel, and the bar-odd " +
        "coefficient is a sign-blind crossing count.",
      see: "docs/audits/2026-08-08-coulomb-decomposition-downstream-propagation.md",
    },
  ],
  label: "sec:cp-violation-evidence",
  uses: [
    "conj:complex-chirality-rotation",
    "def:coulomb-charge",
    "prop:crossing-energy-decomposition",
  ],
  tags: [
    "cp-violation", "kaon", "b-meson", "CKM",
    "matter-antimatter", "experimental",
  ],
  cites: ["christenson1964", "aubert2001"],
});
