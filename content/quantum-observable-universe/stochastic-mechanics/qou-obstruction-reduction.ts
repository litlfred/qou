import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:qou-obstruction-reduction",
  title:
    "In a QOU the classical limit obstruction is one-dimensional",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.qou_obstruction_reduction",
    validation: "not_checked",
  },
  uses: [
    "def:classical-limit-obstruction",
    "thm:qu-to-qou",
  ],
  tags: [
    "obstruction",
    "classical-limit",
    "hochschild-cohomology",
    "observability",
    "frobenius-duality",
    "euler-characteristic",
    "kummer",
  ],
  cites: ["yekutieli2010"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The single `ℝ` here, `phi_1_image`, is only ever equated to an " +
        "integer cast (`phi_1_image = (chi_A : ℝ)`), so on its own content " +
        "this block would be a regenericisation candidate. It is **blocked by " +
        "an `extends` edge**: `QouObstructionReductionContext` is extended by " +
        "`CollatzContactBoundaryContext` in " +
        "`lean/QOU/AlgebraicSubstrate/collatz_contact_boundary.lean` and " +
        "consumed by four further library files, so parameterising it " +
        "rewrites downstream instance binders — the blast radius that blocked " +
        "`qmn_recursive_memoized`, and one of the affected files is currently " +
        "owned by another branch. Recorded here so the next agent does not " +
        "re-derive the diagnosis.",
    },
  ],
});
