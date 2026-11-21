import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:derived-atom",
  label: "rem:antiquark-channel-ledger",
  title: "The antiquark ledger: why the meson channel is absent from step 2",
  tags: ["meson", "antiquark", "binding", "channel", "hyperbolic-volume", "confinement"],
  uses: [
    "def:derived-atom",
    "def:categorical-meson",
    "conj:atom-knot-mass-derivation",
    "rem:pion-mass-hyperbolic-threshold",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "Closes a gap rather than only flagging it. `def:derived-atom` step 2 " +
        "disposes of the antiquarks as 'either annihilate or form " +
        "antinucleons', omitting the third available channel — three q-qbar " +
        "pairs binding as three mesons. The omission turns out to be " +
        "justified: on `conj:atom-knot-mass-derivation`'s formula the " +
        "meson's Hopf-link binding topology has Vol = 0, so channel B " +
        "carries no binding, while the Borromean rings of channel A carry " +
        "8G. But the text gives no reason, and the reason matters because it " +
        "also says where the argument would fail.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "Records a trap found while checking this. The three channels are all " +
        "elements of the same H_3(q) at the same q_0, so their normal-form " +
        "nets look commensurable — net(p) ≈ 0.999, net(bare pair) ≈ 1.418, " +
        "net(M_+) ≈ 1.515. They must not be ranked that way: binding RAISES " +
        "the net, so a minimum-net rule would prefer the unbound pair to the " +
        "bound meson and no meson would ever form. The minimised functional " +
        "is the confinement SDP's optimal dual objective (the nu_SDP of the " +
        "mass invariant), not the net.",
    },
  ],
});
