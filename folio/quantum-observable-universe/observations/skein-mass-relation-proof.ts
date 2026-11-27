import { proof } from "../../schema/builders";

export default proof({
  label: "prf:skein-mass-relation",
  title: "Proof of $q$-Deformed Skein Relation",
  uses: ["rem:skein-mass-relation"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation refutation guard (`qou-x60n`, `qou-z9ws`): `2026-08-30-skein-mass-relation-is-false.lean` (`skein_pnd_identity_false_guard`) guards removal of the false `SkeinMassRelationHolds` class from `QOU.HadronicMass`.",
      see: "docs/audits/2026-08-30-skein-mass-relation-is-false.lean",
    },
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body:
        "Opening sentence brought in line with the owner ruling of 2026-11-21: " +
        "the electron is $\\sigma_0\\sigma_1\\sigma_0 \\in B_3$ (Hopf-link closure), " +
        "with the trefoil as backup. The earlier sentence also stated " +
        "$\\mathrm{Vol}_q(\\beta_{3_1}) = 0$, citing `def:algebraic-quantum-volume`; " +
        "that definition is the full Markov trace, which does not vanish on a " +
        "torus knot or on the Hopf link, so the claim is replaced by the true " +
        "statement that both complements have hyperbolic volume $0$. A mass " +
        "formula of the form $m_e \\cdot \\mathrm{Vol} \\cdot \\rho/\\hbar_q^2$ " +
        "therefore assigns zero mass to the electron under either reading; " +
        "this block takes the electron as the unit, so that objection is not " +
        "resolved here.",
    },
  ],
  lean: { ref: "qou:QOU.MassTheory.HadronicMass.SkeinMassRelation",
    validation: "leanok",
  },
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
  ],
});
