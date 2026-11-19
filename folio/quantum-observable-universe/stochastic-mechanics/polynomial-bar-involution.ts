import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:polynomial-bar-involution",
  lean: {
    ref: "qou:QOU.BraidKnot.PolynomialBarInvolution.barPoly_involutive",
    validation: "not_checked",
  },
  title:
    "Polynomial bar involution $p(X) \\mapsto p(-X)$ on $R[X]$ and its even-degree invariant subring $R[X^2]$",
  uses: [
    "def:bar-involution",
  ],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
  ],
  tags: [
    "lean-infrastructure",
    "bar-invariance",
    "polynomial-ring",
    "categorical-action",
    "mathlib",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "Type-level infrastructure complete. Future work: instantiate\nspecific `BarHeckeFunctor R[X]` examples corresponding to\ntruncated $\\cos$ / $\\cosh$ / Li_2^q expansions in $X$, and\nextend to `RatFunc R = FractionRing (R[X])` for rational-function\nfunctors. Polynomial-level truncation work is `sorry`-free.",
    },
  ],
});
