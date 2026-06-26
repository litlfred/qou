import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-26",
      body: "While the underlying Diophantine constraint $(m-1)(n-1)=2g$ is standard, its application here as a *genus-saturation* condition on the symplectic homology of Bring's surface provides a uniquely rigid, novel algebraic-geometric derivation of the exact force-carrier pair (the crossing-number 9 and 10 knots), replacing the ad-hoc symmetry assumptions historically required in the literature.",
    },
  ],
  label: "prop:force-carrier-bring-uniqueness",
  title: "$(T_{2,9}, T_{3,5})$ is the unique pair of genus-$4$ torus knots",
  lean: {
    ref: "qou:QOU.Archimedean.force_carrier_bring_uniqueness",
    validation: "not_checked",
  },
  uses: ["prop:torus-knot-genus-four-unique"],
  tags: [
    "force-carrier",
    "torus-knot",
    "genus-4",
    "brings-surface",
    "uniqueness",
    "number-theoretic",
  ],
});
