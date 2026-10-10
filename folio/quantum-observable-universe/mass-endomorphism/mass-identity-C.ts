import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:mass-identity-C",
  lean: { ref: "qou:QOU.MassIdentityC", validation: "not_checked" },
  title: "Archimedean realisation: nonabelian multiplicative integration",
  proofs: ["prf:mass-identity-C"],
  tags: ["archimedean", "mass", "multiplicative-integral", "yekutieli"],
  uses: [
    "ex:c-quantum-observable-universe",
    "def:mass-identity",
  ],
  cites: [
    "yekutieli2015",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-06",
      body:
        "**The sibling `.lean` backed this corollary with two false " +
        "axioms.** `nonabelian_stokes` asserted " +
        "`mult_integral_norm = holonomy_norm` and " +
        "`categorical_equals_multiplicative_integral` asserted " +
        "`categorical_mass_norm = mult_integral_norm`, over an " +
        "`ArchimedeanMassData` that carries all three as independent real " +
        "fields -- its only relating field, `mass_nonneg`, constrains one " +
        "of them and says nothing about the others. Both fail at " +
        "`⟨0, 1, 0, le_refl 0⟩`, and so did `mass_is_holonomy`, the " +
        "theorem derived from them. All three are replaced by live " +
        "refutations. Yekutieli's nonabelian Stokes theorem is real and " +
        "the prose argument is the right one; what was wrong is that the " +
        "type mentions no path, no connection and no surface, so nothing " +
        "in it could ever have made the equality hold. Stating it needs " +
        "the norms DERIVED from a connection and a multiplicative " +
        "integral, which is a real formalisation and is not guessed at. " +
        "This block's `lean.ref` points at the library structure " +
        "`QOU.MassIdentityC`, not at the deleted theorem, so the ref is " +
        "unaffected.",
      see: "docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md",
    },
  ],
});
