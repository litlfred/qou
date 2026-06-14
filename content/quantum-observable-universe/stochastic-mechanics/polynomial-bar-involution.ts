import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:polynomial-bar-involution",
  lean: {
    ref: "qou:QOU.BraidKnot.PolynomialBarInvolution",
    validation: "not_checked",
  },
  title:
    "Non-trivial bar-involution on the polynomial ring $R[X]$ via $X \\mapsto -X$: provides a concrete categorical setting where the indeterminate $X$ plays the role of the bar-anti-symmetric Hecke skein $h = q - q^{-1}$. All four ring-involution axioms proved via `Polynomial.comp` identities; the bar-symmetric subring is exactly $R[X^2]$ (even-degree polynomials).",
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
