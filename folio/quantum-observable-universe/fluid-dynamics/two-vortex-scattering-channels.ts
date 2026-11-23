import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:two-vortex-channel-algebra",
  label: "rem:two-vortex-scattering-channels",
  title: "Two-vortex scattering: solitons, factorization, and channel decay",
  uses: [
    "rem:geodesic-vortices",
    "prop:r-matrix-braiding-structure",
    "def:van-der-waals-hopf-channel",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): over the [Hopf channel](#def:van-der-waals-hopf-channel) pair" },
  ],
  tags: ["vortex", "soliton", "scattering", "factorization", "hopf"],
});
