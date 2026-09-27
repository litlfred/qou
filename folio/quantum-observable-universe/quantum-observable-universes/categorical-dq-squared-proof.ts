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
        "here rather than done under this block.\n\n" +
        "Side effect, recorded rather than hidden: `wall-base-ring-minimal` " +
        "went `pass → warn` on this file in the same pass, on the single line " +
        "that instantiates the generic lemma with the scalar `cqd.q⁻¹`. The " +
        "warn asks whether the inverse admits a division-free restatement " +
        "over $\\mathbb{Z}[q,q^{-1}]$; the answer is that the lemma it feeds " +
        "*is already* division-free — it takes the scalar abstractly over a " +
        "bare `Ring`, which has no `Inv` — and the `⁻¹` is unavoidable at the " +
        "call site only because `CategoricalQExtDeriv.dq` is defined as " +
        "$q^{-1} d + (1 - q^{-1})\\,\\pi_V d$. So the warn is pointing at the " +
        "same structure-level obstruction described above, and it was left " +
        "visible deliberately: writing the scalar implicitly would have " +
        "cleared the marker without removing the inverse.",
      see: "folio/quantum-observable-universe/lean/QOU/CategoricalDqSquared.lean",
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
