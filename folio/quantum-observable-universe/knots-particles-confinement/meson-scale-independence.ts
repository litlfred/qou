import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:meson-scale-independence",
  title:
    "The meson mass scale $m_\\pi$ is independent of $(m_\\mathfrak{e}, q_0)$",
  lean: {
    ref: "qou:QOU.ParticleInteractions.meson_scale_independence",
  },
  uses: [
    "def:categorical-meson",
    "prop:frobenius-lepton-meson-bridge",
    "prop:hoefsmit-binding-amplitude",
  ],
  cites: [
    "jones1987",
    "wenzl1988c",
  ],
  tags: [
    "meson",
    "pion",
    "independence",
    "hopf-link",
    "sdp",
    "calibration",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
