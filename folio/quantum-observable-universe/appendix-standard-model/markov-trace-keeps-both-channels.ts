import { proposition } from "../../schema/builders";

/**
 * Tests whether the Markov trace chooses between the two two-strand Hecke
 * channels. Convention D gives both nonzero weight; only z = q kills the sign
 * channel and only z = -q^{-1} kills the symmetric one. Scope (a) negative.
 */
export default proposition({
  label: "prop:markov-trace-keeps-both-channels",
  title: "Convention D keeps both two-strand channels",
  uses: ["prop:hecke-sign-channel-is-fermi"],
  lean: {
    ref: "qou:QOU.EightfoldWay.MarkovTraceKeepsBothChannels.zD_keeps_both",
  },
  tags: ["appendix", "standard-model", "hecke", "markov-trace", "fermi-statistics"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "Sorry-free (`MarkovTraceKeepsBothChannels.lean`). Scope (a): the Markov " +
        "trace at z_D does not choose the matter channel. Which channel matter takes " +
        "stays open. Bean qou-h0zz.",
    },
  ],
});
