import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:mass-identity-exists",
  renamedFrom: ["prop:mass-identity-exists"],
  title: "Well-definedness of the inertial mass identity",
  uses: ["def:mass-identity"],
  tags: ["well-definedness", "mass-identity", "inertial-mass"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "**Mass is valued in the ring (owner ruling 2026-11-27, bean qou-5o1v, constructive item 2.1).** " +
        "The definition no longer applies a norm: the mass is the composite $\\int_A \\circ \\Psi \\circ \\varrho \\in R$. " +
        "`BraidKnotOctonion/MassClassRingHom.lean` proves `map_massClass`: the braid-class mass commutes with every ring " +
        "homomorphism, so evaluation at a point is applied after the mass is computed. The absolute value and the " +
        "logarithm of the binding law are confined to `QOU/Transcendental/MassTheory/MassComparison.lean` " +
        "(`comparedMass`, `comparedBinding`, `comparedBinding_mul`). The quadratic `frobeniusMass` and the real-valued " +
        "`scalarMass` were removed from the sibling `mass-identity.lean`.",
    },
    {
      kind: "status",
      date: "2026-11-22",
      body:
        "**Demoted from prop: to rem: (owner card, 2026-11-22, \"Demote both to remarks\").** " +
        "The claim holds by construction: the mass is defined as a norm, so it is an element of R for every cycle. " +
        "The old Lean sibling proved `[Nonempty R] : Nonempty R` by `infer_instance`, which says nothing about the mass " +
        "(caught by the triviality re-probe and the self-assuming audit rule `instance-is-conclusion`). " +
        "The non-negative real value is `QOU.MassIdentity.scalarMass_nonneg` in mass-identity.lean. Issue #9004, PR #9005, bean qou-jy1r.",
    },
  ],
});
