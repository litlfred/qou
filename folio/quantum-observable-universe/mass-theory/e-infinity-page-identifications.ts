import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:e-infinity-page-identifications",
  title:
    "$E_\\infty$-page identifications with the six mass-formula terms",
  lean: {
    ref: "qou:QOU.BraidKnot.e_infinity_identifications",
    validation: "not_checked",
  },
  uses: [
    "conj:jet-prefix-gb-filtration",
    "prop:chirality-from-frobenius-self-pairing",
  ],
  tags: [
    "spectral-sequence",
    "hochschild",
    "page-identification",
    "mass-formula",
    "derivation",
  ],
  computation: {
    engine: "python",
    script: "computations/atom_level_wedderburn_tower.py",
    witness:
      "computations/atom-level-wedderburn-tower.witness.json",
    status: "verified",
    requires: ["mpmath", "numpy", "scipy"],
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body: `**Base ring (§7c) — mixed; \`ℝ\` kept for the measured half.** \`m_total\` is a mass and \`trM_T_w_abs\` an absolute value, both \`ℝ\` by meaning; the remaining fields (\`page_pairing\`, \`brane_pairing\`, \`brane_pairwise\`, \`chirality_sign = ±1\`) are algebraic and would live over a generic ring. Splitting the class to separate them is a larger change than a base-ring pass.\\n\\n**Separately noted, not fixed:** \`e_infinity_identifications\` is a \`def\` whose body is \`⟨ctx.claim_mass_formula_unified, ctx.claim_descended, …⟩\` — every conjunct is a class field asserting that conjunct. That is the §3b-cond item-5 self-assuming projection, the same shape as \`confinement_categorical\` and \`nucleon_ordering_factorization\`. Bean \`qou-mtc9\`.`,
    },
  ],
});
