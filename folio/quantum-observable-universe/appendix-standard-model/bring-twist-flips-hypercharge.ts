import { proposition } from "../../schema/builders";

/**
 * Under Bring's sign twist, the odd elements of S3 x S2 send hypercharge Y to -Y;
 * the twist does not fix the hypercharge sign.
 */
export default proposition({
  label: "prop:bring-twist-flips-hypercharge",
  title: "Bring's sign twist exchanges hypercharge with its negative",
  uses: ["prop:strand-charges-are-holomorphic-differentials", "prop:chirality-sign-is-hypercharge-sign"],
  lean: {
    ref: "qou:QOU.StandardModel.BringTwist.twist_flips_Y_isospin",
  },
  tags: ["appendix", "standard-model", "brings-surface"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`BringTwistFlipsHypercharge.lean`). Excludes the twisted S3 x S2 " +
        "action as a source of the hypercharge sign; other upstream sources are not " +
        "excluded. The sign stays open. Bean qou-h0zz.",
    },
  ],
});
