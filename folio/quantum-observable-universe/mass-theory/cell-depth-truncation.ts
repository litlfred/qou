import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cell-depth-truncation",
  title:
    "Cell-depth truncation of a trace: the depth-$k$ parts vanish above $k_\\star(x)$, any weighted sum stabilises there, and the truncated $\\Phi_q$ product never stabilises",
  lean: {
    ref: "qou:QOU.MassCore.CellDepthTruncation.tower_stable",
  },
  uses: ["prop:cellular-depth-filtration"],
  cites: ["kazhdan-lusztig1979"],
  tags: ["phi-q", "truncation", "gb-depth", "a-function", "trace", "kazhdan-lusztig"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-16",
      body: "Proved core of conj:phi-q-categorical-truncation (issue #8094), with GB-depth fixed as Lusztig's a-function (owner ruling 2026-11-16). Items 1-3 hold for any depth function; item 4 shows the truncation removes nothing on T_w and braid images; item 5 shows the per-level Phi_q identity of the conjecture cannot hold together with stabilisation. No production number moves: production evaluates the full Phi_q product and reads no k_star. Sibling .lean sorry-free, lean-direct exit 0.",
    },
  ],
});
