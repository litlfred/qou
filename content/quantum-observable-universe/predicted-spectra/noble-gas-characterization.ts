import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:noble-gas-characterization",
  lean: { ref: "qou:QOU.Archimedean.noble_gas_characterization", validation: "not_checked" },
  title:
    "Noble gas characterization: full shell as full curls",
  tags: [
    "noble-gas",
    "hopf-link",
    "sub-link",
    "trefoil",
    "closed-shell",
    "curl",
    "helium",
    "neon",
    "argon",
  ],
  uses: ["rem:helium-hopf-diagram"],
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "This full-shell-as-full-curls topological characterization breaks from standard heuristic chemistry, introducing a novel sub-Hopf link invariant to rigidly classify noble gas inertness and formally binding empirical ionization energy peaks to crossing-energy maxima." },
    {
      kind: "caveat",
      date: "2026-06-16",
      body:
        "**Categorical σ_F does not reproduce the stated ionization mechanism.** " +
        "An exploratory 50-dps computation of the confinement shadow price " +
        "σ_F(k) along the electron-dressing chain (auditOnly witness " +
        "`sigma-f-electron-shell-chain`) does **not** support the *Relation to " +
        "ionization energy* mechanism as written: σ_F(k) *decays* monotonically " +
        "along the chain rather than peaking at closed shells, and the " +
        "Wedderburn degeneracy μ≥2 (the categorical analogue of 'full curls') " +
        "is *generic* across Hecke levels, not specific to closed shells. " +
        "Separately, the pure 2n² cumulative-closure series (2,10,28,60,…) " +
        "reproduces the observed noble-gas Z (2,10,18,36,54,86) only for He and " +
        "Ne — the C1 'magic numbers observed, not derived' gap (see " +
        "`shell-construction-rules`), made precise for electron shells. The " +
        "topological characterization (full shell = full curls) stands as a " +
        "definition; the ionization-energy and shell-closure claims are " +
        "*interpretations* pending a categorical derivation, not results. " +
        "See docs/audits/2026-06-16-gram-q-approximation-audit.md context.",
    },
  ],
});
