import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:polynomial-bar-involution",
  lean: {
    ref: "qou:QOU.BraidKnot.PolynomialBarInvolution.barPoly_involutive",
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): First, algebraic decidability: `Polynomial.comp` lemmas give the four ring-involution axioms for free.\n\n## Proved theorems (Lean)\n\nThe Lean sibling [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean) proves the following (see [Table](#tbl:polynomial-bar-involution-table-data)). All proofs use only `Polynomial.comp` lemmas from Mathlib.\n\nIn `prop:bar-symmetric-three-layer-synthesis`, the universal kernel is bar-anti-symmetric.\n\nEach layer functor is concretely realised as a `BarHeckeFunctor R[X]` sending bar-anti-symmetric inputs to bar-symmetric outputs. The synthesis-class fields become explicit elements of $R[X^2]$.\n\n## Proofs (Lean $\\leftrightarrow$ paper bridge)\n\nEvery Lean theorem below has both a narrative proof here and a fully formalised Lean proof in [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean). The core bar-involution proofs use only the four ring-involution axioms plus Mathlib's `Polynomial.comp` lemmas." },
    {
      kind: "status",
      body: "Type-level infrastructure complete. Future work: instantiate\nspecific `BarHeckeFunctor R[X]` examples corresponding to\ntruncated $\\cos$ / $\\cosh$ / Li_2^q expansions in $X$, and\nextend to `RatFunc R = FractionRing (R[X])` for rational-function\nfunctors. Polynomial-level truncation work is `sorry`-free.",
    },
  ],
});
