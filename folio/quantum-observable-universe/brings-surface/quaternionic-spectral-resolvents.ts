import { definition } from "../../schema/builders";

export default definition({
  label: "def:quaternionic-spectral-resolvents",
  lean: { ref: "qou:QOU.QuaternionicSpectralResolvents", validation: "not_checked" },
  title: "Quaternionic spectral resolvents",
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "**A sibling `.lean` was shadowing the declaration this ref names** " +
        "(bean `qou-lo1t`). `lean.ref` has always named " +
        "`QOU.QuaternionicSpectralResolvents`, which exists — in the library, " +
        "at `QOU/QuaternionicSpectralResolvents.lean`. But resolution takes the " +
        "sibling `<rootName>.lean` first, and that file declared no such thing: " +
        "a differently-named `structure QuaternionicResolvent` plus " +
        "`uncertainty_vanishes` and `three_resolvents_embed`, each returning " +
        "one of its own fields. Per §0a a stub may not shadow a real library " +
        "declaration, so the sibling is deleted and the ref now resolves to the " +
        "carrier it names — which is also the better formalisation: it fixes " +
        "`r = -log|q|` on `0 < |q| ≤ 1` and *proves* `r ≥ 0` and " +
        "`|q| = exp(-r)` from it, rather than projecting assumptions.",
    },
    {
      kind: "caveat",
      date: "2026-08-23",
      body:
        "**One claim is not carried forward, and is open rather than dropped.** " +
        "The deleted sibling asserted `ω₀ = 0` on balanced states, glossed as " +
        "\"the first power sum ∑xⱼ = 0, so ω₀ = 0\". Nothing in that file had " +
        "power sums: `omega_zero_balanced` was a field stating the conclusion, " +
        "and the theorem returned it, so the \"so\" was never an inference. The " +
        "library carrier does not state it either. Making it real needs `ω₀` " +
        "tied to the first power sum of a point of `QOU.BringsSurface` (whose " +
        "`power_sum_1 : ∑ coords j = 0` is already there) — at which point it " +
        "derives. The obstacle is that the two live over different rings " +
        "(`coords : Fin 5 → ℂ` against the sibling's `Fin 4 → R_q`), so the " +
        "identification is a real piece of work, not a rename.",
    },
  ],
  tags: ["brings-surface", "quaternionic", "spectral"],
  uses: ["def:brings-surface", "rem:jet-shell"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/quaternionic-spectral-resolvents-0.svg", blockIndex: 0, hash: "ab6a8e0c38af" },
    { mime: "image/svg+xml", url: "rendered/quaternionic-spectral-resolvents-1.svg", blockIndex: 1, hash: "2d7f8ea9b4a3" },
  ],
  simulator: { ref: "sim:brings-surface" },
});
