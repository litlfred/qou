import { proposition } from "../../schema/builders";

/**
 * LP stability criterion for atoms.
 */
export default proposition({
  label: "prop:atomic-lp-stability",
  lean: { ref: "qou:QOU.ParticleInteractions.atomic_lp_stability", validation: "not_checked" },
  title: "LP stability of the atomic braid",
  uses: ["def:atomic-braid"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-hand-adjudicated.lean` inhabits `AtomicLPStabilityContext` on `Unit` with `bareVolume := 0` and `dressedVolume := 1`.",
      see: "docs/audits/2026-08-30-context-classes-hand-adjudicated.lean",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "`lean/QOU/ParticleInteractions/atomic_lp_stability.lean` proves its " +
        "one sorry-free lemma by **arithmetic on substrate decimal " +
        "literals**: `bareAnnihilationRatio : ℝ := 0.537` versus " +
        "`dressedAnnihilationRatio := (1.109978595554181 : ℝ) ^ (-10 : ℤ)`, " +
        "with `annihilation_ratios_distinct` discharged by `norm_num` / " +
        "`nlinarith` on those numerals. A numerical evaluation at the " +
        "substrate anchor is the §7c \"experimental value → `ℝ`\" row, so the " +
        "`ℝ` is forced by the statement rather than chosen.",
    },
  ],
});
