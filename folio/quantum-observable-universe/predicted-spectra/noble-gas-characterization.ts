import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:noble-gas-characterization",
  lean: { ref: "qou:QOU.Archimedean.noble_gas_characterization", validation: "not_checked" },
  title:
    "Noble gas characterization: a full shell has no free linking site",
  tags: [
    "noble-gas",
    "hopf-link",
    "sub-link",
    "braid-word",
    "closed-shell",
    "linking-site",
    "helium",
    "neon",
    "argon",
  ],
  uses: ["rem:helium-hopf-diagram"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner choice 2026-11-21, 'rebuild the rest on sigma_0 sigma_1 sigma_0'; issue #8822): rebuilt on the electron word sigma_0 sigma_1 sigma_0 in B_3, whose closure is the Hopf link. Photon absorption is the strand-adding curl (Markov stabilisation), so the level is n = w - 2 (QOU.BraidKnot.ElectronLevelWord). Where a statement was built on the trefoil's own geometry it is now stated as not re-derived; the trefoil is kept as the backup reading." },
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
