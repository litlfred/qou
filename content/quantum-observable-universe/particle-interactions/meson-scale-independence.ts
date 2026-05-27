import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:meson-scale-independence",
  title:
    "The meson mass scale $m_\\pi$ is independent of $(m_\\mathfrak{e}, q_0)$",
  uses: [
    "def:categorical-meson",
    "prop:lepton-meson-torus-knot-dictionary",
    "prop:borromean-markov-trace-closed-form",
  ],
  cites: [
    "jones1987",
    "wenzl1988hecke",
  ],
  tags: [
    "meson",
    "pion",
    "CAL-3",
    "independence",
    "hopf-link",
    "sdp",
    "shadow-price",
  ],
});
