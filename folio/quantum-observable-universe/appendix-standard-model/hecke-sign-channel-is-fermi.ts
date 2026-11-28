import { proposition } from "../../schema/builders";

/**
 * Replaces the Fermi-exchange input of prop:fermi-pair-wedge by the -q^{-1}
 * eigenspace of the Jimbo braiding on two strands. At q = 1 the two coincide.
 */
export default proposition({
  label: "prop:hecke-sign-channel-is-fermi",
  title: "The Hecke sign channel is Fermi exchange",
  uses: ["prop:fermi-pair-wedge"],
  lean: {
    ref: "qou:QOU.EightfoldWay.HeckeSignChannelIsFermi.sign_iff",
  },
  tags: ["appendix", "standard-model", "hecke", "fermi-statistics"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "Sorry-free (`HeckeSignChannelIsFermi.lean`). Input left: that a matter " +
        "strand pair lives in the -q^{-1} channel rather than the q channel. " +
        "Spin-statistics is still not derived. Bean qou-h0zz.",
    },
  ],
});
