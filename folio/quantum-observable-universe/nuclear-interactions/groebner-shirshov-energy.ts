import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:groebner-shirshov-energy",
  title:
    "Energy as a Gröbner--Shirshov invariant of the nuclear braid",
  tags: [
    "groebner-shirshov",
    "hecke-algebra",
    "energy",
    "braid-word",
    "normal-form",
    "division-algorithm",
    "topological-invariant",
  ],
  lean: { ref: "qou:QOU.Archimedean.groebner_shirshov_energy",
    validation: "not_checked",
  },
  uses: ["unital-groebner-bases:thm:main-theorem"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "The Lean sibling carried `beta_decay_energy_negative` with the statement `∃ (𝒮_par E_dau : ℝ), E_dau < 𝒮_par`, proved by `⟨1, 0, one_pos⟩`: the reals were tied to no parent or daughter and every hypothesis was unused, so it asserted nothing. Its docstring claim \"computationally verified for all A ≤ 6\" has no located producer. Replaced by `beta_decay_energy_sub_shortModel` (E(p) − E(n) = −|h|, every real h) and `beta_decay_energy_negative_shortModel` (daughter lower for q > 1), both sorry-free and scoped to the short typed-crossing model. PR #8682 measured the nucleon-only sign as opposite in the 11-letter model (+0.06389 at the proton q₀) and zero on V³, so no model-free statement is supported (scope (a)). Beans `qou-n2un`, `qou-99qc`.",
    },
  ],
});
