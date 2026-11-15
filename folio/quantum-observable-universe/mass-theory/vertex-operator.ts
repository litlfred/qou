import { definition } from "../../schema/builders";

export default definition({
  label: "def:vertex-operator",
  lean: { ref: "qou:QOU.VertexOperator", validation: "not_checked" },
  title: "Vertex operator on the exceptional divisor",
  tags: [
    "vertex-operator", "exceptional-divisor", "reeb-bundle",
    "state-operator-correspondence", "R-matrix",
  ],
  uses: [
    "def:reeb-bundle",
    "def:contact-affine-chart",
    "ex:projective-line-su2",
    "rem:r-matrix-braiding",
    "thm:jones-markov-trace",
  ],
  examples: ["rem:skein-decomposition"],
  cites: ["frenkel2004", "kassel1995"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-04",
      body:
        "Two changes, both narrowing what the Lean claims rather than " +
        "widening it. (1) `VertexOperator` now takes the base space as a " +
        "TYPE PARAMETER `B` instead of naming `ReebBundle q`. That was not " +
        "merely unreachable (a content-block sibling cannot import a " +
        "sibling — they sit outside the Lake globs) but **type-wrong**: " +
        "`def:reeb-bundle` is `structure ReebBundle (q : R)` over the " +
        "REALS, with `q > 1` and a `Real.exp` holonomy, and its own header " +
        "says it is not part of the formal proof chain — while this file " +
        "is over the categorical ground ring `R_q = Z[q, q^-1]`. Applying " +
        "an R-indexed structure to a Laurent polynomial is the ss7c " +
        "straddle the ground-ring convention exists to prevent; an " +
        "archimedean consumer instantiates `B := ReebBundle q0` after the " +
        "tau functor. (2) `ope_is_skein` was a bare `axiom`, polluting " +
        "`#print axioms` for everything downstream. It is now a theorem — " +
        "and the proof is record construction, because `OPE` carries the " +
        "eigenvalues as FIELDS. So assuming it bought nothing, and what it " +
        "establishes is that such an OPE EXISTS, not that the Hecke pair " +
        "is FORCED. Forcing it needs `OPE` to carry the generator's action " +
        "and derive the eigenvalues from the quadratic relation; until " +
        "then `q` and `-q^-1` are put in by hand and the statement cannot " +
        "tell a right pair from a wrong one. Both facts are in the file's " +
        "docstrings rather than left to be rediscovered.",
    },
  ],
});
