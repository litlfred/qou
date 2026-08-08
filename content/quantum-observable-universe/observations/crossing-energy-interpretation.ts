import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Corrected (channel identification).** The block asserted “the " +
        "antisymmetric part distinguishes charges” in the same paragraph that " +
        "noted the $\\sinh$ weight is *blind* to the crossing sign — an internal " +
        "contradiction, and the downstream form of the exchanged multiplicities " +
        "corrected upstream in `def:coulomb-charge`. The antisymmetric channel's " +
        "coefficient $p + m$ is a crossing count, hence non-negative, so that " +
        "channel cannot change sign with chirality and cannot be the " +
        "charge-sensitive one; $Q = \\tfrac{1}{2}(p - m)$ scales the *symmetric* " +
        "channel. The “Strong binding” / “Coulomb " +
        "(electromagnetic)” force column and the corresponding row " +
        "labels are withdrawn in favour of the channel totals, and the " +
        "identification is flagged open rather than replaced — relabelling is an " +
        "author call, matching the upstream posture. Also disambiguated the " +
        "antisymmetric *eigenvalue* $-q^{-1}$ (which " +
        "`prop:em-coupling-projection` uses) from the antisymmetric *channel* of " +
        "this decomposition; the shared adjective is a live conflation hazard. No " +
        "numerical value changed: the $m = 0$ table is arithmetically untouched " +
        "and its unqualified channel ratio is now explicitly scoped to $m = 0$.",
      see: "docs/audits/2026-08-08-coulomb-decomposition-downstream-propagation.md",
    },
  ],
  label: "rem:crossing-energy-interpretation",
  title: "Physical interpretation of the two crossing-energy channels",
  interprets: "prop:crossing-energy-decomposition",
  uses: [
    "def:coulomb-charge",
    "prop:crossing-energy-decomposition",
    "prop:em-coupling-projection",
    "prop:torus-hopf-stability",
    "rem:mass-comparison-table",
  ],
  tags: [
    "crossing-energy", "strong-force", "coulomb",
    "pair-creation", "electromagnetism", "interpretation",
  ],
});
