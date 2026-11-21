import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:topological-mass-dilogarithm",
  renamedFrom: ["lem:topological-mass-dilogarithm"],
  lean: { ref: "qou:QOU.LiftingDescent.tm_dilogarithm_evaluation",
    validation: "not_checked",
  },
  title: "Quantum dilogarithm evaluation of exceptional-divisor contributions",
  tags: ["quantum-dilogarithm", "exceptional-divisor", "briggs-klein", "spectral-coordinates"],
  uses: [
    "lem:topological-mass-holonomy",
    "lem:topological-mass-transient-localisation",
    "def:quantum-dilogarithm-disambiguation",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "Demoted from lemma to conjecture (owner card \"Demote confinement-phase-stratification and topological-mass-dilogarithm to conjectures?\", option \"Demote both\", thread \"N2 Lean foundations\"). Proving was tried first: the first equality needs a definition of the non-abelian multiplicative integral and its evaluation in the Briggs–Klein chart, neither of which exists in Lean or Mathlib, and the Lean only projected a class field carrying it. Only the second equality, the integral form of the dilogarithm, holds, and it holds by definition.",
    },
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "The statement used to read MI = Φ_q(z_i) = ∫₀^{z_i} ln_q(1+t)/t dt. The middle term was wrong: `def:quantum-dilogarithm-disambiguation` records that the integral is the bounded symmetric q-dilogarithm −Li₂^q(−z), not the unbounded product Φ_q. A 40-digit check at the proton q₀ agrees (z = 0.3: integral 0.28016 = −Li₂^q(−0.3), Φ_q(0.3) ≈ 19.13). The statement now ends in −Li₂^q(−z_i), and the Lean function is renamed `negLi2q`. For the same reason the conjecture was not restated through the discrete holonomy `partBHolonomy`, which is the partial product of Φ_q (owner asked to check first: \"3 1\").",
    },
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/LiftingDescent/tm_dilogarithm_evaluation.lean` uses an " +
        "integral `∫`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
