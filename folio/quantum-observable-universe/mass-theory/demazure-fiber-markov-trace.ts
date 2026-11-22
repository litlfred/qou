import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "The Lean sibling carried `axiom demazure_principal_specialization_eq_schur_axiom`, asserting that every `DemazureModel` instance has `D_{w0}(λ)` equal to one opaque value. That axiom was inconsistent: two instances with constant characters 1 and 2 both satisfy `schur_nonzero`, and the axiom then proves `1 = 2` (checked lean-direct: a `theorem : False` compiled against it). The identity is now the class field `schur_recovery`, so it constrains a given instance rather than all of them. The statement also called $V_\\lambda$ an $S_n$-module; Demazure characters belong to highest-weight $\\mathrm{GL}_n$-modules, now stated.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** Two independent reasons the Lean sibling " +
        "stays on `ℝ`. (i) **Ordering**: every substantive declaration " +
        "carries `(q : ℝ) (hq : q > 1)` — the principal-specialisation " +
        "`x_i ↦ q^{i-1}` and the `schur_recovery` field of `DemazureModel` " +
        "are stated in the `q > 1` regime, and `q > 1` has no " +
        "generic-`CommRing` form. (ii) **`opaque`**: `yLambda` and " +
        "`demazureCharacter` are `opaque`, and a polymorphic `opaque` is a " +
        "*family of unrelated constants*, which would misrepresent the " +
        "specific Markov coefficient being named — the same ground on which " +
        "`markov_identification` was refuted in the 2026-08-08 audit §8. " +
        "Reclassified from WEAK to MED by that audit §7 for the `>` it was " +
        "missing; the `>` is genuine.",
    },
  ],
  label: "prop:demazure-fiber-markov-trace",
  title:
    "Demazure-fiber Markov-trace functional $T^{\\mathrm{Dem}}(\\lambda; w) = y_\\lambda \\cdot D_w(\\lambda) / D_{w_0}(\\lambda)$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.demazure_at_w0_equals_y_lambda",
    validation: "not_checked",
  },
  computation: {
    engine: "sympy",
    script: "computations/demazure_markov_trace.py",
    witness: "computations/demazure-markov-trace.witness.json",
    status: "verified",
    requires: ["sympy"],
  },
  uses: ["prop:macdonald-hook-telescope"],
  cites: ["kashiwara1991", "lecouvey2007"],
  tags: [
    "demazure",
    "markov-trace",
    "resonance",
    "kashiwara-graph",
    "weight-lattice",
    "wenzl-bridge",
    "crystal-basis-shortcut",
  ],
});
