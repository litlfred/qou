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
