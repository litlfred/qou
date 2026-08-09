import { proof } from "../../schema/builders";

export default proof({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). The vanishing argument itself is not archimedean " +
        "and no longer pretends to be: it is now `dq_sq_eq_zero_of_scalar_one` " +
        "in `QOU/CategoricalDqSquared.lean`, stated over an arbitrary ring " +
        "`R` and an `R`-linear preadditive category. In the notation of the " +
        "proof body ($a = q^{-1}$, $b = 1 - q^{-1}$, $d_q = a\\,d + b\\,\\pi_V d$) " +
        "the classical-limit step uses nothing beyond $1 - 1 = 0$, so `Ring` " +
        "is the weakest class that carries it — `CategoryTheory.Linear` needs " +
        "a `Semiring` and the coefficient $b$ needs subtraction; " +
        "commutativity is never used. The intended instance is the Laurent " +
        "ground ring $R_q = \\mathbb{Z}[q, q^{-1}]$, declared in the same file.\n\n" +
        "The residual $\\mathbb{R}$ in `QOU.categorical_dq_squared` is carried " +
        "by the *structure*, not by the argument: `CategoricalQExtDeriv` " +
        "(declared in `QOU/QuantumObservableUniverse/Instanton.lean`) fixes " +
        "`q : ℝ`, so its `dq` is `ℝ`-linear. The theorem is now literally that " +
        "generic lemma instantiated at `R := ℝ`. Finishing the move means " +
        "adding a scalar parameter to `CategoricalQExtDeriv` itself, which is " +
        "not a pure generalisation: `dq` is defined with `q⁻¹`, and a bare " +
        "`Ring` has no inverse, so the structure would have to carry the " +
        "inverse as a field (or be stated over a `Field`/`DivisionRing`). That " +
        "is an edit to `Instanton.lean` and its four other consumers " +
        "(`categorical-q-ext-deriv{,-exists,-unique}.lean`), so it is recorded " +
        "here rather than done under this block.",
      see: "content/quantum-observable-universe/lean/QOU/CategoricalDqSquared.lean",
    },
  ],
  label: "prf:categorical-dq-squared",
  title: "Proof of Non-vanishing of $d_q^2$",
  uses: ["prop:categorical-dq-squared"],
  lean: { ref: "qou:QOU.categorical_dq_squared",
    validation: "leanok",
  },
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-dq-squared-proof-0.svg", blockIndex: 0, hash: "9269fbe261dd" },
  ],

});
