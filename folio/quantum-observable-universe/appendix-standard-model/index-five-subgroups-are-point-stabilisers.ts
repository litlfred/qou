import { proposition } from "../../schema/builders";

/**
 * Every subgroup of index five (order 24) in S5 is the stabiliser of a point.
 */
export default proposition({
  label: "prop:index-five-subgroups-are-point-stabilisers",
  title: "Index-five subgroups of S5 are point stabilisers",
  uses: ["prop:strands-are-bring-elliptic-quotients"],
  lean: {
    ref: "qou:QOU.StandardModel.IndexFive.eq_stab_of_index_five",
  },
  tags: ["appendix", "standard-model", "brings-surface"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`OrderTwentyFourSubgroupsArePointStabilisers.lean`). Closes the cited " +
        "uniqueness step of prop:strands-are-bring-elliptic-quotients. Bean qou-h0zz.",
    },
  ],
});
