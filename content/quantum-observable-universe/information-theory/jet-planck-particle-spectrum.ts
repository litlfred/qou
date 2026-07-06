import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:jet-prolongation",
  label: "rem:jet-planck-particle-spectrum",
  title: "Particle spectrum per Planck step",
  tags: [
    "jet-bundle",
    "planck-time",
    "particle-spectrum",
    "crossing-number",
    "big-bang",
    "chiral-cubic",
    "information-theory",
  ],
  uses: [
    "rem:jet-planck-steps",
    "ex:photon-wavefront",
  ],
});
